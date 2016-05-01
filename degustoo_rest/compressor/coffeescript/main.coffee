angular
	.module('main', [])
	.config([
		'$httpProvider',
		'$interpolateProvider',
		($httpProvider, $interpolateProvider) ->
			$interpolateProvider.startSymbol('[[')
			$interpolateProvider.endSymbol(']]')
			$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
			$httpProvider.defaults.xsrfCookieName = 'csrftoken'
			return
	])