from __future__ import print_function
from concurrent import futures


import sys
sys.path.append("..")
sys.path.append("../protos/")

import logging
import random

import grpc
from protos import server_gui_pb2
from protos import server_gui_pb2_grpc


server_gui_pb2_grpc.ServerGUIServicer
class ServerGUIServicer_Server(server_gui_pb2_grpc.ServerGUIServicer):

    def RollDiceAndGetValidLandingSpots(self, request, context):
        # TODO enter logic for category creation here
        print(f"Player {request.Player} from location: {request.Location}")
        return server_gui_pb2.ValidSpotMessage(ValidSpot="4,11,23,1")


    def HandleNewSpot(self, request, context):
        # TODO add logic for question entering here
        print(f"Player {request.Player} is in spot {request.Spot}")
        return server_gui_pb2.NewSpotActionOrMessage(Player=1,RT=0)  # rt = response type
 
    def GetQuestion(self, request, context):
        # TODO add db logic for getting question here
        print(f"Player {request.Player} is requesting a question") # don't need to specify their location, because logic part should have it.
        return server_gui_pb2.QuestionGS(CategoryType=1, QuestionGS='What is the most meta aspect of this category?')

    def QuestionSuccess(self, request, context):
        print(f"Player {request.player} succeeded at answering question: {request.success}")
        return server_gui_pb2.UpdatePlayerScoreMessage(player=2, Category="Science", answered=True)

    def CreateCategory(self,request, context):
        print(f"Request to create category {request.CategoryName}")
        return server_gui_pb2.SuccessMessageGS(Success=True, messageText="Successfully created new category")


    def CreateNewQuestion(self, request, context):
        print(f"Request to create new question in {request.CategoryType}: {request.Question}")
        return server_gui_pb2.SuccessMessageGS(Success=True, messageText=f"Successfully created new category {request.Question}")



def serve():
    port = '50053'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_gui_pb2_grpc.add_ServerGUIServicer_to_server(ServerGUIServicer_Server(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Server started and listening on {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()