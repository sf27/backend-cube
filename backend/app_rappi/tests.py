# -*- coding: utf-8 -*-
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_valid_for_t_command(self):
        data = {'command': '1'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.get('message'), u'Debe realizar {} de caso(s) de prueba'.format(
            data.get('command')
        ))

    def test_invalid_for_t_command_zero_value(self):
        data = {'command': '0'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 50]')

    def test_invalid_for_t_command_wrong_value(self):
        data = {'command': 'wewew'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'Por favor ingrese un valor entero válido.')

    def test_invalid_for_t_command_wrong_number_of_arguments(self):
        data = {'command': '1 1 1'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'Comando no valido.')

    def test_invalid_for_t_command_max_value(self):
        data = {'command': '51'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 50]')

    def test_valid_for_n_m_command(self):
        data = {'command': '2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.get('message'), u'Ingrese las 4 operaciones')

    def test_invalid_for_n_m_command_max_value_for_n(self):
        data = {'command': '101 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        message = response.data.get('message')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 100]')

    def test_invalid_for_n_m_command_max_value_for_m(self):
        data = {'command': '10 1001'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        message = response.data.get('message')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 1000]')

    def test_invalid_for_n_m_command_wrong_value_for_n(self):
        data = {'command': 'e 10'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        message = response.data.get('message')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message, 'Por favor ingrese un valor entero válido.')

    def test_invalid_for_n_m_command_wrong_value_for_m(self):
        data = {'command': '19 zzzxzxz'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        message = response.data.get('message')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(message, 'Por favor ingrese un valor entero válido.')

    def test_valid_for_update_command(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 1 3 3 3'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(json.get('message'), u'Resultado de suma')
        self.assertEqual(json.get('value'), 4)

    def test_valid_for_update_command_wrong_number_of_arguments(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'La cantidad de parametros ingresada no es válida. Ej. UPDATE x y z W')

    def test_valid_for_update_command_no_valid_constraints_for_x(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 0 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 9223372036854775807]')

    def test_valid_for_update_command_no_valid_constraints_for_y(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 0 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 9223372036854775807]')

    def test_valid_for_update_command_no_valid_constraints_for_z(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 0 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 9223372036854775807]')

    def test_valid_for_query_command(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 1 2 2 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(json.get('message'), u'Resultado de suma')
        self.assertEqual(json.get('value'), 4)

    def test_valid_for_query_command_wrong_number_of_arguments(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 1 2 2 2 3'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'La cantidad de parametros ingresada no es válida. Ej. QUERY x1 y1 z1 x2 y2 z2')

    def test_valid_for_query_command_no_valid_constraints_for_x1(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 0 1 1 2 2 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 2]')

    def test_valid_for_query_command_no_valid_constraints_for_x2(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 1 0 2 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 9223372036854775807]')

    def test_valid_for_query_command_no_valid_constraints_for_y1(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 0 1 2 2 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 2]')

    def test_valid_for_query_command_no_valid_constraints_for_y2(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 1 2 0 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 9223372036854775807]')

    def test_valid_for_query_command_no_valid_constraints_for_z1(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 0 2 2 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 2]')

    def test_valid_for_query_command_no_valid_constraints_for_z2(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 1 2 2 0'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        message = response.data.get('message')
        self.assertEqual(message, 'El valor ingresado no está dentro del rango válido. Rango [1, 9223372036854775807]')

    def test_valid_for_a_complete_list_of_commands(self):
        data = {'command': '2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': '4 5'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 1 2 2 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(json.get('message'), u'Resultado de suma')
        self.assertEqual(json.get('value'), 4)

        data = {'command': 'UPDATE 1 1 1 23'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 2 2 2 4 4 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(json.get('message'), u'Resultado de suma')
        self.assertEqual(json.get('value'), 4)

        data = {'command': 'QUERY 1 1 1 3 3 3'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(json.get('message'), u'Resultado de suma')
        self.assertEqual(json.get('value'), 27)

        data = {'command': '2 4'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'UPDATE 2 2 2 1'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'command': 'QUERY 1 1 1 1 1 1'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(json.get('message'), u'Resultado de suma')
        self.assertEqual(json.get('value'), 0)

        data = {'command': 'QUERY 1 1 1 2 2 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(json.get('message'), u'Resultado de suma')
        self.assertEqual(json.get('value'), 1)

        data = {'command': 'QUERY 2 2 2 2 2 2'}
        url = reverse('execute_command')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json = response.json()
        self.assertEqual(json.get('message'), u'Resultado de suma')
        self.assertEqual(json.get('value'), 1)