angular
	.module('RestauranteAPP')
	.controller(
		'opcaoController',
		($scope, opcaoAJAX) ->
			reload = (cardapio_id) ->
				opcaoAJAX
					.listarOpcoes(cardapio_id)
					.success(
						$scope.lista_opcao = data
					)
				return


			this.novaOpcao = (cardapio_id, dados) -> 
				opcaoAJAX
					.novaOpcao(cardapio_id, dados)
					.success(
						(data) ->
							reload cardapio_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.listarOpcoes = (cardapio_id) -> 
				opcaoAJAX
					.listarOpcoes(cardapio_id)
					.success(
						(data) ->
							reload cardapio_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.getOpcao = (cardapio_id, opcao_id) -> 
				opcaoAJAX
					.getOpcao(cardapio_id, opcao_id)
					.success(
						(data) ->
							console.log data
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.editarOpcao = (cardapio_id, opcao_id, dados) -> 
				opcaoAJAX
					.editarOpcao(cardapio_id, opcao_id, dados)
					.success(
						(data) ->
							reload cardapio_id
							return
					)
					.error(
						(data) ->
							console.log data
							return
					)
				return
			this.deletarOpcao = (cardapio_id, opcao_id) -> 
				opcaoAJAX
					.deletarOpcao(cardapio_id, opcao_id)
					.success(
						(data) ->
							reload cardapio_id
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