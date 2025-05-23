
from concurrent import futures
import grpc
import time
import hello_pb2
import hello_pb2_grpc

class HelloServicer(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message=f"Hello, {request.name}!")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("gRPC server running on port 50051")
server.wait_for_termination()
