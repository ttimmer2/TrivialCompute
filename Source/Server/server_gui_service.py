from __future__ import print_function
from concurrent import futures


import sys
sys.path.append("..")
sys.path.append("../protos/")

import logging
import random
import sqlite3

import grpc
from protos import server_gui_pb2
from protos import server_gui_pb2_grpc


server_gui_pb2_grpc.ServerGUIServicer
class ServerGUIServicer_Server(server_gui_pb2_grpc.ServerGUIServicer):

    def RollDiceAndGetValidLandingSpots(self, request, context):
        def get_possible_positions(current_position):
            # Define the offsets
            offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            # Use a nested list comprehension to get the possible positions
            possible_positions = [(current_position[0] + offset[0], current_position[1] + offset[1]) for offset in offsets]
            # Filter out the positions that are not in the POSITIONS list
            valid_positions = [position for position in possible_positions if position in POSITIONS]
            # Return the valid positions
            return valid_positions

            # Use map() to apply the function to each element in POSITIONS
            possible_positions_map = map(get_possible_positions, POSITIONS)
            # Convert the map object to a list of lists
            possible_positions_list = list(possible_positions_map)
            # Print the possible positions for (4, 4)
            print(possible_positions_list[POSITIONS.index((4, 4))])
        print(f"Player {request.Player} from location: {request.Location}")
        return server_gui_pb2.ValidSpotMessage(ValidSpot="4,11,23,1")

    def HandleNewSpot(self, request, context):
        # TODO add logic for question entering here
        print(f"Player {request.Player} is in spot {request.Spot}")
        return server_gui_pb2.NewSpotActionOrMessage(Player=request.Player,RT=0)  # rt = response type
 
    def GetQuestion(self, request, context):
        # Connect to database
        conn = sqlite3.connect("trivial_compute.db")
        cursor = conn.cursor()
        # Execute query to select all questions
        query = "SELECT * FROM questions"
        cursor.execute(query)
        # Fetch all rows as a list of tuples
        rows = cursor.fetchall()
        # Select a random row from the list
        random_row = random.choice(rows)
        # Get the question from the row
        question = random_row[0]
        print(f"Player {request.Player} is requesting a question") # don't need to specify their location, because logic part should have it.
        return server_gui_pb2.QuestionGS(CategoryType="Meta trivia", Question=str("What is the most meta aspect of this category?"))

    def QuestionSuccess(self, request, context):
        print(f"Player {request.player} succeeded at answering question: {request.success}")
        return server_gui_pb2.UpdatePlayerScoreMessage(player=request.player, Category="Science", answered=request.success)

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
