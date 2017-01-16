# -*- coding: utf-8 -*-

from rest_framework.views import APIView

from .cube_summation import CubeSummation


class ExecuteCommandView(APIView):
    """
    Execute View
    """

    def __init__(self, **kwargs):
        super(ExecuteCommandView, self).__init__(**kwargs)
        self.cube_summation = CubeSummation()

    def post(self, request, *args, **kwargs):
        data = request.data
        command = data.get("command").split()
        command_len = len(command)
        if command_len == 1:
            return self.cube_summation.t(command[0])
        elif command_len == 2:
            return self.cube_summation.n_m(command[0], command[1])
        else:
            return self.cube_summation.process_operation(command)
