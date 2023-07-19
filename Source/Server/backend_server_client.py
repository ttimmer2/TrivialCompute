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

def run():
    port = 50052
    with grpc.insecure_channel(f'localhost:{port}') as channel:
        stub = backend_server_pb2_grpc.BackendServerStub(channel)
        c = "games"
        qt = "How many sides are on a six-side die?"
        #response = stub.EnterQuestion(backend_server_pb2.Question(Category="games", QuestionType=0, QuestionText=qt))
        response = stub.EnterQuestion(request=backend_server_pb2.Question())
    print(f"Response success: {response.Success}\nmessage:{ response.MessageText}")


if __name__ == '__main__':
    logging.basicConfig()
    run()
