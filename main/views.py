from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from translate import Translator
from deep_translator import GoogleTranslator





def function_1(request):
	text = request.GET.get('texting')
	lang = request.GET.get('language')

	if text and lang is not None:


		
		# my_translator = GoogleTranslator(source='auto', target='lang')
		# tt = my_translator.translate(text)

		translator = GoogleTranslator(source='auto', target=lang)
		translated =translator.translate(text)
		# trans = translator.translate(lang)
		tt = translated
		tl = lang
		stt = text
		return render(request, 'pages/function_1.html', {
			'tt': tt,
			'tl': tl,
			'stt': stt
			})
		# # return HttpResponse(tt)
	else:
		return render(request, 'pages/function_1.html', {
			})

	


def home_1(request):
	return render(request, 'pages/home_1.html', {})


def home(request):
	return render(request, 'pages/home.html', {})
