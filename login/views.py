from django.http import JsonResponse
from rest_framework.views import APIView
from login.models import Credencial
import json

class CriarCadastroView(APIView):

    def post(self, request):
        dados = json.loads(request.body)

        try:
            cadastro = Credencial.objects.create(
                login = dados['login'],
                senha = dados['senha'],
            )
            return JsonResponse({"login": cadastro.login, "senha": cadastro.senha})

        except Exception as e:
            return JsonResponse({"error": str(e)})
