def prepareAjaxErrorMessage(message):
	return {'success':0, 'message':message}

def prepareAjaxSuccessData(result, dataLength=0):
	return {'success':1, 'result':result, 'length':dataLength}