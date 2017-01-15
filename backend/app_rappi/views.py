from django.db.models import Q, Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app_rappi.models import Matriz


class ExecuteCommandView(APIView):
    """
    Execute View
    """

    def reset_matriz(self):
        Matriz.objects.all().delete()

    def t(self, value):
        self.reset_matriz()
        data = {
            'result': False,
            'error': False,
            'message': 'Debe realizar {} de casos de prueba'.format(value)
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def n_m(self, value_n, value_m):
        self.reset_matriz()
        data = {
            'result': False,
            'error': False,
            'message': 'Ingrese las {} operaciones'.format(value_m)
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def process_query(self, params):
        x1, y1, z1, x2, y2, z2 = params
        x_valid = Q(Q(x__gte=x1) & Q(x__lte=x2))
        y_valid = Q(Q(y__gte=y1) & Q(y__lte=y2))
        z_valid = Q(Q(z__gte=z1) & Q(z__lte=z2))
        result = Matriz.objects.filter(
            x_valid & y_valid & z_valid
        ).aggregate(Sum('w'))
        data = {
            'error': False,
            'result': True,
            'message': 'Resultado de suma',
            'value': result.get('w__sum') if result.get('w__sum') else 0
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def process_update(self, params):
        x, y, z, W = params
        objs = Matriz.objects.filter(
            Q(x=x) & Q(y=y) & Q(z=z)
        )
        if objs.exists():
            obj = objs[0]
            obj.value = W
            obj.save()
        else:
            Matriz.objects.create(
                x=x,
                y=y,
                z=z,
                w=W
            )
        data = {
            'error': False,
            'result': False,
            'message': 'Matriz actualizada correctamente',
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def process_operation(self, command):
        command_type = str(command[0]).upper()
        if command_type == 'QUERY':
            params = map(int, command[1:])
            return self.process_query(params)
        elif command_type == 'UPDATE':
            params = map(int, command[1:])
            return self.process_update(params)
        else:
            data = {
                'result': False,
                'error': True,
                'message': 'Error: Comando no valido',
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        data = request.data
        command = data.get("command").split()
        command_len = len(command)
        if command_len == 1:
            return self.t(command[0])
        elif command_len == 2:
            return self.n_m(command[0], command[1])
        else:
            return self.process_operation(command)
