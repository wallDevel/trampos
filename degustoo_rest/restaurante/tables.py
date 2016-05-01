def buildCardapioTable(data, token=""):
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
                                <a class="deg_fpanel_closer">X</a>
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
                                <a class="deg_fpanel_closer">X</a>
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

def buildSubcardapioTable(data, c_id, token=""):
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
                                <a class="deg_fpanel_closer">X</a>
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
                                <a class="deg_fpanel_closer">X</a>
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

def buildOpcaoTable(data, c_id, token=""):
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
                                <a class="deg_fpanel_closer">X</a>
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
                                <a class="deg_fpanel_closer">X</a>
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

def buildItemTable(data, c_id, token=""):
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
                                <a class="deg_fpanel_closer">X</a>
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
                                <a class="deg_fpanel_closer">X</a>
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

def buildItemOpcaoTable(data, c_id, o_id, token=""):
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
                                <a class="deg_fpanel_closer">X</a>
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
                                <a class="deg_fpanel_closer">X</a>
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

def buildItemSubcardapioTable(data, c_id, s_id, token=""):
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
                                <a class="deg_fpanel_closer">X</a>
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
                                <a class="deg_fpanel_closer">X</a>
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