$(document).ready(function(){


	$(document).on("click", ".deg_fpanel_container", function(event){
		$(this).children('.deg_fpanel').show();
	});
	$(document).on("click", '.deg_fpanel_closer', function(event){
		$(this).parent().parent().fadeOut();
	});


	$(document).on(".deg-addCardapio-form, .deg-editCardapio-form, .deg-deleteCardapio-form", function(event){
		event.preventDefault();
		$.post($(event.target).attr('action'), $(event.target).serialize(), function(json){
			if(json.success){
				_insertTableContent($('#deg-cardapio-table'), json.result);
			}
		}, "json");
	});


	$(document).on(".deg-addSubcardapio-form", function(event){
		event.preventDefault();
		$.post($(event.target).attr('action'), $(event.target).serialize(), function(json){
			if(json.success){
				_insertTableContent($('#deg-subcardapio-table'), json.result);
			}
		}, "json");
	});


	$(document).on("submit", ".deg-addItem-form, .deg-editItem-form, .deg-deleteItem-form", function(event){
		event.preventDefault();
		$.post($(event.target).attr('action'), $(event.target).serialize(), function(json){
			if(json.success){
				_insertTableContent($('#deg-item-table'), json.result);
			}
		}, "json");
	});

	
});

function _insertTableContent(obj, text){
	obj.html(text);
}