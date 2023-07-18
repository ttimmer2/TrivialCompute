# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_gui_pb2 as server__gui__pb2


class ServerGUIStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RollDiceAndGetValidLandingSpots = channel.unary_stream(
                '/backendserver.ServerGUI/RollDiceAndGetValidLandingSpots',
                request_serializer=server__gui__pb2.RollDiceMessage.SerializeToString,
                response_deserializer=server__gui__pb2.ValidSpotMessage.FromString,
                )
        self.HandleNewSpot = channel.unary_unary(
                '/backendserver.ServerGUI/HandleNewSpot',
                request_serializer=server__gui__pb2.NewSpotMessage.SerializeToString,
                response_deserializer=server__gui__pb2.NewSpotActionOrMessage.FromString,
                )
        self.GetQuestion = channel.unary_unary(
                '/backendserver.ServerGUI/GetQuestion',
                request_serializer=server__gui__pb2.RequestQuestion.SerializeToString,
                response_deserializer=server__gui__pb2.Question.FromString,
                )
        self.QuestionSuccess = channel.unary_unary(
                '/backendserver.ServerGUI/QuestionSuccess',
                request_serializer=server__gui__pb2.ResponseSuccess.SerializeToString,
                response_deserializer=server__gui__pb2.UpdatePlayerScoreMessage.FromString,
                )
        self.CreateCategory = channel.unary_unary(
                '/backendserver.ServerGUI/CreateCategory',
                request_serializer=server__gui__pb2.Category.SerializeToString,
                response_deserializer=server__gui__pb2.SuccessMessage.FromString,
                )
        self.CreateNewQuestion = channel.unary_unary(
                '/backendserver.ServerGUI/CreateNewQuestion',
                request_serializer=server__gui__pb2.Question.SerializeToString,
                response_deserializer=server__gui__pb2.SuccessMessage.FromString,
                )


class ServerGUIServicer(object):
    """Interface exported by the server.
    """

    def RollDiceAndGetValidLandingSpots(self, request, context):
        """player rolls dice - checks where valid places to move are
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleNewSpot(self, request, context):
        """send the question
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetQuestion(self, request, context):
        """if NewSpotActionOrMessage is roll again, redo RollDiceAndGetValidLandingSpots - else, request question for spot. If final question condition - send the final question request with the added category parameter from user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuestionSuccess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCategory(self, request, context):
        """for the add question ui - creates a new message, returns success
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNewQuestion(self, request, context):
        """for the add question ui - creates a new category, returns success or not
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerGUIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RollDiceAndGetValidLandingSpots': grpc.unary_stream_rpc_method_handler(
                    servicer.RollDiceAndGetValidLandingSpots,
                    request_deserializer=server__gui__pb2.RollDiceMessage.FromString,
                    response_serializer=server__gui__pb2.ValidSpotMessage.SerializeToString,
            ),
            'HandleNewSpot': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleNewSpot,
                    request_deserializer=server__gui__pb2.NewSpotMessage.FromString,
                    response_serializer=server__gui__pb2.NewSpotActionOrMessage.SerializeToString,
            ),
            'GetQuestion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetQuestion,
                    request_deserializer=server__gui__pb2.RequestQuestion.FromString,
                    response_serializer=server__gui__pb2.Question.SerializeToString,
            ),
            'QuestionSuccess': grpc.unary_unary_rpc_method_handler(
                    servicer.QuestionSuccess,
                    request_deserializer=server__gui__pb2.ResponseSuccess.FromString,
                    response_serializer=server__gui__pb2.UpdatePlayerScoreMessage.SerializeToString,
            ),
            'CreateCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCategory,
                    request_deserializer=server__gui__pb2.Category.FromString,
                    response_serializer=server__gui__pb2.SuccessMessage.SerializeToString,
            ),
            'CreateNewQuestion': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNewQuestion,
                    request_deserializer=server__gui__pb2.Question.FromString,
                    response_serializer=server__gui__pb2.SuccessMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'backendserver.ServerGUI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServerGUI(object):
    """Interface exported by the server.
    """

    @staticmethod
    def RollDiceAndGetValidLandingSpots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/backendserver.ServerGUI/RollDiceAndGetValidLandingSpots',
            server__gui__pb2.RollDiceMessage.SerializeToString,
            server__gui__pb2.ValidSpotMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleNewSpot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backendserver.ServerGUI/HandleNewSpot',
            server__gui__pb2.NewSpotMessage.SerializeToString,
            server__gui__pb2.NewSpotActionOrMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetQuestion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backendserver.ServerGUI/GetQuestion',
            server__gui__pb2.RequestQuestion.SerializeToString,
            server__gui__pb2.Question.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QuestionSuccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backendserver.ServerGUI/QuestionSuccess',
            server__gui__pb2.ResponseSuccess.SerializeToString,
            server__gui__pb2.UpdatePlayerScoreMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backendserver.ServerGUI/CreateCategory',
            server__gui__pb2.Category.SerializeToString,
            server__gui__pb2.SuccessMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNewQuestion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/backendserver.ServerGUI/CreateNewQuestion',
            server__gui__pb2.Question.SerializeToString,
            server__gui__pb2.SuccessMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
