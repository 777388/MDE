import os
from xmlrpc.server import SimpleXMLRPCServer

def transmit_files(folder_path):
    files = {}
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'rb') as f:
                file_data = xmlrpc.client.Binary(f.read())
                files[file_path] = file_data
    return files

# create an xml-rpc server
server = SimpleXMLRPCServer(("localhost", 8000))
# register the transmit_files function
server.register_function(transmit_files)
# start the server's main loop
server.serve_forever()
