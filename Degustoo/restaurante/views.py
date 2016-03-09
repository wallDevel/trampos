# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from .models import *
from .forms import *


################################################################### MIXINS
class RestauranteMixin(object):
    """ 
        Verify if there are some restaurant logged in and raises an error if not 

    """
    restaurante = None
    "Verify if there is some restaurant logged in"
    def dispatch(self, request, *args, **kwargs):
        try:
            self.restaurante = request.user.restaurante
        except Exception:
            raise Http404("You are not allowed visiting here")
        return super(RestauranteMixin, self).dispatch(request, *args, **kwargs)

class CardapioMixin(object):
    """
        Verify if there are some the given menu.pk belows to this user
    """
    cardapio = None
    def dispatch(self, request, *args, **kwargs):
        id = kwargs.pop('card_id', 0)
        if not id == 0:
            try:
                restaurante = self.restaurante
                self.cardapio = restaurante.cardapio_set.get(pk=id)
            except Cardapio.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(CardapioMixin, self).dispatch(request, *args, **kwargs)

class SubcardapioMixin(object):
    """
        Ao carregar a view verifica se o subcardapio pertence a este cardapio.
        Se sim, aplica a variavel "subcardapio" ao objeto view
    """
    subcardapio = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('id', 0)
        if id:
            try:
                self.subcardapio = self.cardapio.subcardapio_set.get(pk=id)
            except Subcardapio.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(SubcardapioMixin, self).dispatch(request, **kwargs)


class OpcaoMixin(object):
    """
        Ao carregar a view verifica se a opcao pertence a este cardapio.
        Se sim, aplica a variavel "opcao" ao objeto view
    """
    opcao = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('id', 0)
        if id:
            try:
                self.opcao = self.cardapio.opcao_set.get(pk=id)
            except Opcao.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(OpcaoMixin, self).dispatch(request, **kwargs)

class ItemCardapioMixin(object):
    """
        Ao carregar a view verifica se o item pertence a este cardapio.
        Se sim, aplica a variavel "item" ao objeto view
    """
    item = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('i_id', 0)
        if id:
            try:
                self.item = self.cardapio.item_set.get(pk=id)
            except Item.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(ItemCardapioMixin, self).dispatch(request, **kwargs)

class ItemSubcardapioMixin(object):
    """
        Ao carregar a view verifica se o item pertence a este subcardapio.
        Se sim, aplica a variavel "item" ao objeto view
    """
    item = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('i_id', 0)
        if id:
            try:
                self.item = self.subcardapio.item_set.get(pk=id)
            except Item.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(ItemSubcardapioMixin, self).dispatch(request, **kwargs)

class ItemOpcaoMixin(object):
    """
        Ao carregar a view verifica se o item pertence a esta opcao.
        Se sim, aplica a variavel "item" ao objeto view
    """
    item = None
    def dispatch(self, request, **kwargs):
        id = kwargs.pop('i_id', 0)
        if id:
            try:
                self.item = self.opcao.item_set.get(pk=id)
            except Item.DoesNotExist:
                raise Http404("Object does not exist or does not below to this user")
        return super(ItemOpcaoMixin, self).dispatch(request, **kwargs)

################################################################### UTILS
class Index(RestauranteMixin, View):
    template = "restaurante/index.html"
    def get(self, request):
        return render(request, self.template, {})

################################################################### CARDAPIO
class CriarCardapio(RestauranteMixin, View):
    """
        Cria cardapio via json
    """
    form_class = Form_Cardapio_Default
    
    def post(self, request, **kargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cardapio = self.restaurante.cardapio_set.filter(titulo=form.cleaned_data['titulo'])
            if cardapio:
                # cliente possui cardapio com este mesmo nome
                data={'success':0, 'message':'Menu already exists in this restaurant page'}
            else:
                cardapio = Cardapio(
                    restaurante=self.restaurante, imagem=form.cleaned_data['imagem'],
                    titulo=form.cleaned_data['titulo'], tipo=form.cleaned_data['tipo'])
                cardapio.save()
    
                #preparar resultado e enviar
                cardapios = self.restaurante.cardapio_set.all()
                result = _buildCardapioTable(cardapios)
                data = {'success': 1, 'result': result}
        else:
            #formulario invalido
            data = {'success': 0, "message":"Erro de formulario"}
        return JsonResponse(data)

class Cardapio_(RestauranteMixin, CardapioMixin, View):
    template = 'restaurante/cardapio/cardapio.html'
    form_class = Form_Cardapio_Default

    def get(self, request):
        itens = self.cardapio.item_set.all()
        opcoes = self.cardapio.opcao_set.all()
        subcardapios = self.cardapio.subcardapio_set.all()
        return render(request, self.template, 
            {'cardapio':self.cardapio, 'itens':itens, 'opcoes':opcoes, 
            'subcardapios':subcardapios})

class ListaCardapio(RestauranteMixin, View):
    """
        Mostra lista de cardapios em template
    """
    template = 'restaurante/cardapio/lista_cardapio.html'
    form_class = Form_Cardapio_Default
    def get(self, request):
        cardapios = self.restaurante.cardapio_set.all()
        form = self.form_class()
        return render(request, self.template, {'cardapios':cardapios, 'form':form}) 

class EditarCardapio(RestauranteMixin, CardapioMixin, View):
    """
        Edita cardapio via json
    """
    form_class = Form_Cardapio_Default
    def post(self, request):
        form = self.form_class(request.POST, instance=self.cardapio)
        if form.is_valid():
            form.save()
            cardapios = self.restaurante.cardapio_set.all()
            result = _buildCardapioTable(cardapios, request.COOKIES['csrftoken'])
            data = {'success':1, 'result':result}
        else:
            data = {'success':0, 'message':'form has errors'}
        return JsonResponse(data)

class DeletarCardapio(RestauranteMixin, CardapioMixin, View):
    """
        Deleta cardapio via json
    """
    form_class = Form_Subcardapio_Delete
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cardapio = Cardapio.objects.get(pk=form.cleaned_data['id'])
            cardapio.delete()
            cardapios = self.restaurante.cardapio_set.all()
            result = _buildCardapioTable(cardapios, request.COOKIES['csrftoken'])
            data = {'success':1, 'result':result}
        else:
            data = {'success':0, 'message':'form has errors'}
        return JsonResponse(data)

################################################################### SUBCARDAPIO
class Subcardapio_(RestauranteMixin, CardapioMixin, SubcardapioMixin, View):
    """
        View de pagina de subcardapio onde o usuario pode adicionar/editar/deletar itens
        de determinado subcardapio
    """
    template = 'restaurante/cardapio/subcardapio.html'
    def get(self, request):
        itens = self.subcardapio.item_set.all()
        return render(request, self.template, {'cardapio':self.cardapio, 'subcardapio':self.subcardapio, 'itens':itens})

class CriarSubcardapio(RestauranteMixin, CardapioMixin, View):
    """
        Cria subcardapio via json
    """
    form_class = Form_Subcardapio_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            subcardapio = self.cardapio.subcardapio_set.filter(titulo=form.cleaned_data['titulo'])
            if not subcardapio:
                # can save the data, any subcardapio was found
                subcardapio = Subcardapio(cardapio = self.cardapio, titulo=form.cleaned_data['titulo'])
                subcardapio.save()

                # prepare data to send back using json
                subcardapios = self.cardapio.subcardapio_set.all()
                result = _buildSubcardapioTable(subcardapios, self.cardapio.id, token=request.COOKIES['csrftoken'])
                data = {'success': 1, 'result': result}
            else:
                # there is an object with the same name in the same menu
                data = {'success':0, 'message':'There is an object with the same in this menu'}
        else:
            data = {'success': 0, 'message': 'Your form has errors'}
        return JsonResponse(data)

class EditarSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, View):
    """
        Edita subcardapio via json
    """
    template = 'restaurante/cardapio/editar_subcardapio.html'
    form_class = Form_Subcardapio_Default
    def get(self, request):
        form = self.form_class(instance=self.subcardapio)
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST, instance=self.subcardapio)
        if form.is_valid():
            form.save()
            subcardapios = self.cardapio.subcardapio_set.all()
            result = _buildSubcardapioTable(subcardapios, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success':1, 'result':result}
        return JsonResponse(data)

class DeletarSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, View):
    """
        Deleta subcardapio via json
    """

    form_class = Form_Subcardapio_Delete
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            subcardapio = Subcardapio.objects.get(pk=form.cleaned_data['id'])
            subcardapio.delete()
            subcardapios = self.cardapio.subcardapio_set.all()
            result = _buildSubcardapioTable(subcardapios, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success':1, 'result':result}
        return JsonResponse(data)

################################################################### OPCAO
class Opcao_(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    """
        View de pagina de opcao onde o usuario pode adicionar/editar/deletar itens
        de determinada opcao
    """
    template = 'restaurante/cardapio/opcao.html'
    form_class = Form_Opcao_Import
    def get(self, request):
        form = self.form_class(cardapio=self.cardapio)
        itens = self.opcao.item_set.all()
        return render(request, self.template, {'cardapio':self.cardapio, 'opcao':self.opcao, 'itens':itens, 'form':form})

    def post(self, request):
        form = self.form_class(request.POST, cardapio=self.cardapio)
        data = {'success':0}
        if form.is_valid():
            response = form.cleaned_data['options']
            for r in response:
                i = r.export_itens()
                self.opcao.import_itens(i)
            result = _buildItemOpcaoTable(self.opcao.item_set.all(), self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
            data = {'success':1,'result':result}
        return JsonResponse(data)

class CriarOpcao(RestauranteMixin, CardapioMixin, View):
    """
        Cria opcao via json
    """
    form_class = Form_Opcao_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            opcao = self.cardapio.opcao_set.filter(rotulo=form.cleaned_data['rotulo'])
            if not opcao:
                # can save the data, any subcardapio was found
                op = Opcao(cardapio = self.cardapio, rotulo=form.cleaned_data['rotulo'])
                op.save()
                # prepare data to send back using json
                opcoes = self.cardapio.opcao_set.all()
                result = _buildOpcaoTable(opcoes, self.cardapio.id, token=request.COOKIES['csrftoken'])
                data = {'success': 1, 'result': result}
            else:
                # there is an object with the same name in the same menu
                data = {'success':0, 'message':'There is an object with the same in this menu'}
        else:
            data = {'success': 0, 'message': 'Your form has errors'}
        return JsonResponse(data)

class EditarOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    """
        Edita opcao via json
    """
    template = 'restaurante/cardapio/editar_opcao.html'
    form_class = Form_Opcao_Default
    def get(self, request):
        form = self.form_class(instance=self.opcao)
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST, instance=self.opcao)
        if form.is_valid():
            form.save()
            opcoes = self.cardapio.opcao_set.all()
            result = _buildOpcaoTable(opcoes, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success':1,'result':result}
        return JsonResponse(data)

class DeletarOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    """
        Deleta opcao via json
    """
    form_class = Form_Item_Delete
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            opcao = Opcao.objects.get(pk=form.cleaned_data['id'])
            opcao.delete()
            opcoes = self.cardapio.opcao_set.all()
            result = _buildOpcaoTable(opcoes, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success':1,'result':result}
        return JsonResponse(data)

################################################################### ITEM
class CriarItem(RestauranteMixin, CardapioMixin, View):
    """
        Cria item via json
    """
    form_class = Form_Item_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            item = self.cardapio.item_set.filter(nome=form.cleaned_data['nome'])
            if not item:
                # can save the data, any subcardapio was found
                item = Item(
                    cardapio = self.cardapio, nome=form.cleaned_data['nome'],
                    preco=form.cleaned_data['preco'],ingredientes=form.cleaned_data['ingredientes'])
                item.save()

                # prepare data to send back using json
                itens = self.cardapio.item_set.all()
                result = _buildItemTable(itens, self.cardapio.id, token=request.COOKIES['csrftoken'])
                
                data = {'success': 1, 'result': result}
            else:
                # there is an object with the same name in the same menu
                data = {'success':0, 'message':'There is an object with the same in this menu'}
        else:
            data = {'success': 0, 'message': 'Your form has errors'}
        return JsonResponse(data)

class CriarItemOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, View):
    """
        Cria item de opcao via json
    """
    form_class = Form_Item_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            item = self.opcao.item_set.filter(nome=form.cleaned_data['nome'])
            if not item:
                # can save the data, any subcardapio was found
                item = Item(
                    opcao = self.opcao, nome=form.cleaned_data['nome'],
                    preco=form.cleaned_data['preco'],ingredientes=form.cleaned_data['ingredientes'])
                item.save()

                # prepare data to send back using json
                itens = self.opcao.item_set.all()
                result = _buildItemOpcaoTable(itens, self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
                
                data = {'success': 1, 'result': result}
            else:
                # there is an object with the same name in the same menu
                data = {'success':0, 'message':'There is an object with the same in this menu'}
        else:
            data = {'success': 0, 'message': 'Your form has errors'}
        return JsonResponse(data)

class CriarItemSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, View):
    """
        Cria item de subcardapio via json
    """
    form_class = Form_Item_Default
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # prepare data to save
            item = self.subcardapio.item_set.filter(nome=form.cleaned_data['nome'])
            if not item:
                # can save the data, any subcardapio was found
                item = Item(
                    sub_cardapio = self.subcardapio, nome=form.cleaned_data['nome'],
                    preco=form.cleaned_data['preco'],ingredientes=form.cleaned_data['ingredientes'])
                item.save()

                # prepare data to send back using json
                itens = self.subcardapio.item_set.all()
                result = _buildItemSubcardapioTable(itens, self.cardapio.id, self.subcardapio.id, token=request.COOKIES['csrftoken'])
                
                data = {'success': 1, 'result': result}
            else:
                # there is an object with the same name in the same menu
                data = {'success':0, 'message':'There is an object with the same in this menu'}
        else:
            data = {'success': 0, 'message': 'Your form has errors'}
        return JsonResponse(data)

class EditarItem(RestauranteMixin, CardapioMixin, ItemCardapioMixin, View):
    """
        Edita item de cardapio via json
    """

    form_class = Form_Item_Default

    def post(self, request):
        form = self.form_class(request.POST, instance=self.item)
        if form.is_valid():
            form.save()
            itens = self.cardapio.item_set.all()
            result = _buildItemTable(itens, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success': 1, 'result': result}
        return JsonResponse(data)

class EditarItemOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, ItemOpcaoMixin, View):
    """
        Edita item de opcao via json
    """

    form_class = Form_Item_Default

    def post(self, request):
        form = self.form_class(request.POST, instance=self.item)
        if form.is_valid():
            form.save()
            itens = self.opcao.item_set.all()
            result = _buildItemOpcaoTable(itens, self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
            data = {'success': 1, 'result': result}
        return JsonResponse(data)

class EditarItemSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, ItemSubcardapioMixin, View):
    """
        Edita item de subcardapio via json
    """

    form_class = Form_Item_Default

    def post(self, request):
        form = self.form_class(request.POST, instance=self.item)
        if form.is_valid():
            form.save()
            itens = self.subcardapio.item_set.all()
            result = _buildItemSubcardapioTable(itens, self.cardapio.id, self.subcardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success': 1, 'result': result}
        return JsonResponse(data)

class DeletarItemCardapio(RestauranteMixin, CardapioMixin, ItemCardapioMixin, View):
    """
        Deleta item de cardapio via json
    """

    form_class = Form_Item_Delete

    def post(self, request):
        form = self.form_class(request.POST) 
        if form.is_valid():
            item = Item.objects.get(pk=form.cleaned_data['id'])
            item.delete()
            itens = self.cardapio.item_set.all()
            result = _buildItemTable(itens, self.cardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success':1,'result':result}
        else:
            data = {'success':0,'message':form.errors}
        return JsonResponse(data)

class DeletarItemOpcao(RestauranteMixin, CardapioMixin, OpcaoMixin, ItemOpcaoMixin, View):
    """
        Deleta item de cardapio via json
    """

    form_class = Form_Item_Delete

    def post(self, request):
        form = self.form_class(request.POST) 
        if form.is_valid():
            item = Item.objects.get(pk=form.cleaned_data['id'])
            item.delete()
            itens = self.opcao.item_set.all()
            result = _buildItemOpcaoTable(itens, self.cardapio.id, self.opcao.id, token=request.COOKIES['csrftoken'])
            data = {'success':1,'result':result}
        return JsonResponse(data)

class DeletarItemSubcardapio(RestauranteMixin, CardapioMixin, SubcardapioMixin, ItemSubcardapioMixin, View):
    """
        Deleta item de subcardapio via json
    """

    form_class = Form_Item_Delete

    def post(self, request):
        form = self.form_class(request.POST) 
        if form.is_valid():
            item = Item.objects.get(pk=form.cleaned_data['id'])
            item.delete()
            itens = self.subcardapio.item_set.all()
            result = _buildItemSubcardapioTable(itens, self.cardapio.id, self.subcardapio.id, token=request.COOKIES['csrftoken'])
            data = {'success':1,'result':result}
        return JsonResponse(data)



##########################################################################################################
################################################################### TABLE BUILDERS
def _buildCardapioTable(data, token=""):
    """
        Constroi tabela de cardapio
    """
    token = token
    result = ""
    for d in data:
        result += """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>

                <div class="deg_c_container">
                    <a href="/restaurante/cardapio/%s/" class="btn btn-success">Alterar <span class="glyphicon glyphicon-plus"></span></a>
                    <div class="deg_fpanel_container">
                        <a class="btn btn-warning" title="Novo Cardapio">Editar <span class="glyphicon glyphicon-pencil"></span></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Editar Cardapio</h3>
                                <form class="deg-editCardapio-form" method="POST" action="/restaurante/editar_cardapio/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s' />
                                    <input name="titulo" type="text" placeholder="Titulo:" value="%s"/>
                                    <input name="tipo" type="text" placeholder="Tipo:" value="%s"/><br/>
                                    <input name="imagem" type="file" value="%s">
                                    <input type="submit" value="Salvar"/>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="deg_fpanel_container">
                        <a class="btn btn-danger" title="Novo Cardapio">Excluir <span class="glyphicon glyphicon-trash"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Deletar Cardapio</h3>
                                <form class="deg-deleteCardapio-form" method="POST" action="/restaurante/deletar_cardapio/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s' />
                                    <h4>Tem certeza que deseja excluir o cardapio %s ?</h4>
                                    <input name="id" type="hidden" value="%s"/>
                                    <input type="submit" value="Excluir"/>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
        </tr>""" % (
            d.id, d.titulo, d.tipo, 
            d.id, 
            d.id, token, d.titulo, d.tipo, d.imagem,
            d.id, token, d.titulo, d.id)

    table = """
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Tipo</th>
                    <th>Acoes</th>
                </tr>
            </thead>
            <tbody>
                %s
            </tbody>
    """ % (result)
    return table

def _buildSubcardapioTable(data, c_id, token=""):
    """
        Constroi tabela de subcardapio
    """
    token = token
    result = ""
    for d in data:
        result += """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>
                <div class="deg_c_container">
                    <a class="btn btn-success" href="/restaurante/subcardapio/%s/%s/">Adicionar Item <span class="glyphicon glyphicon-plus"></a> 
                    <div class="deg_fpanel_container">
                        <a class="btn btn-warning" title="Novo Item">Editar <span class="glyphicon glyphicon-pencil"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Editar Item</h3>
                                <form class="deg-editSubcardapio-form" method="POST" action="/restaurante/editar_subcardapio/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s'/>
                                    <input name="titulo" type="text" placeholder="Titulo:" value="%s"/>
                                    <input type="submit" value="Alterar"/>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="deg_fpanel_container">
                        <a class="btn btn-danger" title="Novo Item">Excluir <span class="glyphicon glyphicon-trash"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Deletar Item</h3>
                                <form class="deg-deleteSubcardapio-form" method="POST" action="/restaurante/deletar_subcardapio/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s' />
                                    <h4>Tem certeza que deseja excluir o item %s ?</h4>
                                    <input name="id" type="hidden" value="%s"/>
                                    <input type="submit" value="Excluir"/>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
        </tr>
        """ % (d.id, d.titulo,
            c_id, d.id,
            c_id, d.id, token, d.titulo,
            c_id, d.id, token, d.titulo, d.id)

    table = """
            <thead>
                <tr>
                    <td>ID</td>
                    <td>Titulo</td>
                    <td>Acoes<td>
                </tr>
            </thead>
            <tbody>
                %s
            </tbody>
    """ % (result)
    return table

def _buildOpcaoTable(data, c_id, token=""):
    """
        Constroi tabela de opcao
    """
    token = token
    result = ""
    for d in data:
        result += """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>
                <div class="deg_c_container">
                    <a class="btn btn-success" href="/restaurante/opcao/%s/%s/">Adicionar Item <span class="glyphicon glyphicon-plus"></a>
                    <div class="deg_fpanel_container">
                        <a class="btn btn-warning" title="Editar Opção">Editar <span class="glyphicon glyphicon-pencil"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Editar Opção</h3>
                                <form class="deg-editOpcao-form" method="POST" action="/restaurante/editar_opcao/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s' />
                                    <input name="rotulo" type="text" placeholder="Nome:" value="%s"/>
                                    <input type="submit" value="Salvar"/>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="deg_fpanel_container">
                        <a class="btn btn-danger" title="Excluir Opção">Excluir <span class="glyphicon glyphicon-trash"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Deletar Opção</h3>
                                <form class="deg-deleteOpcao-form" method="POST" action="/restaurante/deletar_opcao/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s' />
                                    <h4>Tem certeza que deseja excluir a opção %s ?</h4>
                                    <input name="id" type="hidden" value="%s"/>
                                    <input type="submit" value="Excluir"/>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
        </tr>
        """ % (d.id, d.rotulo,
            c_id, d.id,
            c_id, d.id, token, d.rotulo,
            c_id, d.id, token, d.rotulo, d.id)

    table = """
            <thead>
                <tr>
                    <td>ID</td>
                    <td>Rotulo</td>
                    <td>Acoes<td>
                </tr>
            </thead>
            <tbody>
                %s
            </tbody>
    """ % (result)
    return table

def _buildItemTable(data, c_id, token=""):
    """
        Constroi tabela de item de cardapio
    """
    token = token
    result = ""
    for d in data:
        result += """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <div class="deg_c_container">
                    <div class="deg_fpanel_container">
                        <a class="btn btn-warning" title="Novo Item">Editar <span class="glyphicon glyphicon-pencil"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Editar Item</h3>
                                <form class="deg-editItem-form" method="POST" action="/restaurante/editar_item/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s'/>
                                    <input name="nome" type="text" placeholder="Nome:" value="%s"/>
                                    <input name="ingredientes" type="text" placeholder="Ingredientes:" value="%s"/><br/>
                                    <input name="preco" type="text" placeholder="Preço:" value="%s"/>
                                    <input type="submit" value="Alterar"/>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="deg_fpanel_container">
                        <a class="btn btn-danger" title="Novo Item">Excluir <span class="glyphicon glyphicon-trash"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Deletar Item</h3>
                                <form class="deg-deleteItem-form" method="POST" action="/restaurante/deletar_item/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s' />
                                    <h4>Tem certeza que deseja excluir o item %s ?</h4>
                                    <input name="id" type="hidden" value="%s"/>
                                    <input type="submit" value="Excluir"/>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
        </tr>
        """ % (d.id, d.nome, d.preco, 
            c_id, d.id, token, d.nome, d.ingredientes, d.preco,
            c_id, d.id, token, d.nome, d.id)

    table = """
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Preco</th>
                    <th>Acoes</th>
                </tr>
            </thead>
            <tbody>
                %s
            </tbody>
    """ % (result)
    return table

def _buildItemOpcaoTable(data, c_id, o_id, token=""):
    """
        Constroi tabela de item de opcao
    """
    token = token
    result = ""
    for d in data:
        result += """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <div class="deg_c_container">
                    <div class="deg_fpanel_container">
                        <a class="btn btn-warning" title="Novo Item">Editar <span class="glyphicon glyphicon-pencil"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Editar Item</h3>
                                <form class="deg-editItem-form" method="POST" action="/restaurante/editar_item_opcao/%s/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s'/>
                                    <input name="nome" type="text" placeholder="Nome:" value="%s"/>
                                    <input name="ingredientes" type="text" placeholder="Ingredientes:" value="%s"/><br/>
                                    <input name="preco" type="text" placeholder="Preço:" value="%s"/>
                                    <input type="submit" value="Alterar"/>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="deg_fpanel_container">
                        <a class="btn btn-danger" title="Novo Item">Excluir <span class="glyphicon glyphicon-trash"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Deletar Item</h3>
                                <form class="deg-deleteItem-form" method="POST" action="/restaurante/deletar_item_opcao/%s/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s' />
                                    <h4>Tem certeza que deseja excluir o item %s ?</h4>
                                    <input name="id" type="hidden" value="%s"/>
                                    <input type="submit" value="Excluir"/>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
        </tr>
        """ % (d.id, d.nome, d.preco, 
            c_id, o_id, d.id, token, d.nome, d.ingredientes, d.preco,
            c_id, o_id, d.id, token, d.nome, d.id)

    table = """
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Preco</th>
                    <th>Acoes</th>
                </tr>
            </thead>
            <tbody>
                %s
            </tbody>
    """ % (result)
    return table

def _buildItemSubcardapioTable(data, c_id, s_id, token=""):
    """
        Constroi tabela de item de subcardapio
    """
    token = token
    result = ""
    for d in data:
        result += """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <div class="deg_c_container">
                    <div class="deg_fpanel_container">
                        <a class="btn btn-warning" title="Novo Item">Editar <span class="glyphicon glyphicon-pencil"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Editar Item</h3>
                                <form class="deg-editItem-form" method="POST" action="/restaurante/editar_item_subcardapio/%s/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s'/>
                                    <input name="nome" type="text" placeholder="Nome:" value="%s"/>
                                    <input name="ingredientes" type="text" placeholder="Ingredientes:" value="%s"/><br/>
                                    <input name="preco" type="text" placeholder="Preço:" value="%s"/>
                                    <input type="submit" value="Alterar"/>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="deg_fpanel_container">
                        <a class="btn btn-danger" title="Novo Item">Excluir <span class="glyphicon glyphicon-trash"></snap></a>
                        <div class="deg_fpanel">
                            <div>
                                <span class="deg_fpanel_closer">X</span>
                                <h3>Deletar Item</h3>
                                <form class="deg-deleteItem-form" method="POST" action="/restaurante/deletar_item_subcardapio/%s/%s/%s/">
                                    <input type='hidden' name='csrfmiddlewaretoken' value='%s' />
                                    <h4>Tem certeza que deseja excluir o item %s ?</h4>
                                    <input name="id" type="hidden" value="%s"/>
                                    <input type="submit" value="Excluir"/>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
        </tr>
        """ % (d.id, d.nome, d.preco, 
            c_id, s_id, d.id, token, d.nome, d.ingredientes, d.preco,
            c_id, s_id, d.id, token, d.nome, d.id)

    table = """
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Preco</th>
                    <th>Acoes</th>
                </tr>
            </thead>
            <tbody>
                %s
            </tbody>
    """ % (result)
    return table