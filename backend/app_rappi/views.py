# -*- coding: utf-8 -*-
import sys

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

    def constraints(self, value, min_value=1, max_value=sys.maxsize):
        try:
            value_int = int(value)
        except Exception:
            data = {
                'result': False,
                'error': True,
                'message': 'Por favor ingrese un valor entero válido.'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        if value_int < min_value or value_int > int(max_value):
            data = {
                'result': False,
                'error': True,
                'message': 'El valor ingresado no está '
                           'dentro del rango válido. '
                           'Rango [{}, {}]'.format(min_value, max_value)
            }
            print(data)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def constraints_update(self, *params):
        if len(params) != 4:
            data = {
                'result': False,
                'error': True,
                'message': 'La cantidad de parametros ingresada no es válida. '
                           'Ej. UPDATE x y z W'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        x, y, z, w = params
        constraints = self.constraints(x)
        if constraints:
            return constraints

        constraints = self.constraints(y)
        if constraints:
            return constraints

        constraints = self.constraints(z)
        if constraints:
            return constraints

        constraints = self.constraints(w)
        if constraints:
            return constraints

    def constraints_query(self, *params):
        if len(params) != 6:
            data = {
                'result': False,
                'error': True,
                'message': 'La cantidad de parametros ingresada no es válida. '
                           'Ej. QUERY x1 y1 z1 x2 y2 z2'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        x1, y1, z1, x2, y2, z2 = params
        if x1 > x2:
            data = {
                'result': False,
                'error': True,
                'message': 'El valor de x1 no puede ser mayor a x2. '
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        if y1 > y2:
            data = {
                'result': False,
                'error': True,
                'message': 'El valor de y1 no puede ser mayor a y2. '
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        if z1 > z2:
            data = {
                'result': False,
                'error': True,
                'message': 'El valor de z1 no puede ser mayor a z2. '
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        constraints = self.constraints(x1, max_value=x2)
        if constraints:
            return constraints

        constraints = self.constraints(x2)
        if constraints:
            return constraints

        constraints = self.constraints(y1, max_value=y2)
        if constraints:
            return constraints

        constraints = self.constraints(y2)
        if constraints:
            return constraints

        constraints = self.constraints(z1, max_value=z2)
        if constraints:
            return constraints

        constraints = self.constraints(z2)
        if constraints:
            return constraints

    def t(self, value):
        constraints = self.constraints(value, max_value=50)
        if constraints:
            return constraints

        self.reset_matriz()
        data = {
            'result': False,
            'error': False,
            'message': 'Debe realizar {} de caso(s) '
                       'de prueba'.format(int(value))
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def n_m(self, value_n, value_m):
        constraints = self.constraints(value_n, max_value=100)
        if constraints:
            return constraints

        constraints = self.constraints(value_m, max_value=1000)
        if constraints:
            return constraints

        self.reset_matriz()
        data = {
            'result': False,
            'error': False,
            'message': 'Ingrese las {} operaciones'.format(int(value_m))
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def process_query(self, params):
        constrains = self.constraints_query(*params)
        if constrains:
            return constrains

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
            'message': 'Resultado de consulta',
            'value': result.get('w__sum') if result.get('w__sum') else 0
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def process_update(self, params):
        constrains = self.constraints_update(*params)
        if constrains:
            return constrains

        x, y, z, w = params
        objs = Matriz.objects.filter(
            Q(x=x) & Q(y=y) & Q(z=z)
        )
        if objs.exists():
            obj = objs[0]
            obj.value = w
            obj.save()
        else:
            Matriz.objects.create(
                x=x,
                y=y,
                z=z,
                w=w
            )
        data = {
            'error': False,
            'result': False,
            'message': 'Matriz actualizada correctamente',
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def process_operation(self, command):
        command_type = str(command[0]).upper()
        params = command[1:]
        if command_type == 'QUERY':
            return self.process_query(params)
        elif command_type == 'UPDATE':
            return self.process_update(params)
        else:
            data = {
                'result': False,
                'error': True,
                'message': 'Comando no valido.',
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

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
