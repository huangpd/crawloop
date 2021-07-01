# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import callback_pb2 as result__pb2


class ResultStub(object):
    """定义服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SaveResult = channel.unary_unary(
            '/result.Result/SaveResult',
            request_serializer=result__pb2.SaveResultRequest.SerializeToString,
            response_deserializer=result__pb2.SaveResultResponse.FromString,
        )


class ResultServicer(object):
    """定义服务
    """

    def SaveResult(self, request, context):
        """保存基本爬取信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResultServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SaveResult': grpc.unary_unary_rpc_method_handler(
            servicer.SaveResult,
            request_deserializer=result__pb2.SaveResultRequest.FromString,
            response_serializer=result__pb2.SaveResultResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'result.Result', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Result(object):
    """定义服务
    """

    @staticmethod
    def SaveResult(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/result.Result/SaveResult',
                                             result__pb2.SaveResultRequest.SerializeToString,
                                             result__pb2.SaveResultResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
