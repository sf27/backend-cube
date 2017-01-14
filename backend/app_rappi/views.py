import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ExecuteCommandView(APIView):
    """
    Execute View
    """

    def post(self, request, *args, **kwargs):
        data = request.data
        print("d: ", data.get("command"))
        return Response({"data": data.get("command")}, status=status.HTTP_204_NO_CONTENT)
