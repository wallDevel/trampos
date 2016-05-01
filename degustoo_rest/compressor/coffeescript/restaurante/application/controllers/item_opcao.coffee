angular
	.module('RestauranteAPP')
	.controller(
		'itemOpcaoController',
		($scope, itemOpcaoAJAX) ->
			reload = (opcao_id) ->
				itemOpcaoAJAX
					.listarItens(opcao_id)
					.success(
						(data) ->
							$scope.lista_item_opcao = data
							$scope.novoItem.nome = ""
							$scope.novoItem.preco = ""
							return
					)
				return

			this.novoItem = (opcao_id) ->
				itemOpcaoAJAX
					.novoItem(opcao_id)
					.success(
						(data) ->
							reload(opcao_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return

			this.listarItens = (opcao_id) ->
				itemOpcaoAJAX
					.listarItens(opcao_id)
					.success(
						(data) ->
							reload(opcao_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return

			this.getItem = (opcao_id, item_id) ->
				itemOpcaoAJAX
					.getItem(opcao_id, item_id)
					.success(
						(data) ->
							return
					)
					.error(
						(data) ->
							return
					)
				return

			this.editarItem = (opcao_id, item_id, dados) ->
				itemOpcaoAJAX
					.editarItem(opcao_id, item_id, dados)
					.success(
						(data) ->
							return
					)
					.error(
						(data) ->
							return
					)
				return

			this.deletarItem = (opcao_id, item_id) ->
				itemOpcaoAJAX
					.deletarItem(opcao_id, item_id)
					.success(
						(data) ->
							reload(opcao_id)
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return

			return
	)