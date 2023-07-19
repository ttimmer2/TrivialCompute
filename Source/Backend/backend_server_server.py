from __future__ import print_function
from concurrent import futures


import sys
sys.path.append("..")
sys.path.append("../protos/")

import logging
import random

import grpc
from protos import backend_server_pb2_grpc
from protos import backend_server_pb2



class BackendServer_Server(backend_server_pb2_grpc.BackendServerServicer):

    def CreateCategory(self, request, context):
        # TODO enter logic for category creation here
        print(f"received create category request: {request.Category}")
        return backend_server_pb2.SuccessMessage(Success=True, MessageText=f"Successfully created category {request.Category}")


    def EnterQuestion(self, request, context):
        # TODO add logic for question entering here
        print(f"Received enter question request.\nCategory: {request.Category}\nQuestion Text {request.QuestionText}")
        return backend_server_pb2.SuccessMessage(Success=True, MessageText=f"Successfully entered new question {request.Question}")

    def GetQuestion(self, request, context):
        # TODO add db logic for getting question here
        print(f"Received get question request.\nCategory: {request.Category}")
        return backend_server_pb2.Question(Category=request.Category, QuestionType=2, QuestionText=f"Describe the category `{request.Category}` in four words.")



def serve():
    port = '50052'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    backend_server_pb2_grpc.add_BackendServerServicer_to_server(BackendServer_Server(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Server started and listening on {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()