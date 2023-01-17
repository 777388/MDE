import xmlrpc.client
import os

# create a proxy object for the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# folder name
folder_path = "received_folder"

# call the transmit_files function on the server
files = proxy.transmit_files(folder_path)

# create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# write the received files
for file_path, file_data in files.items():
    # create directory if not exist
    directory = os.path.dirname(os.path.join(folder_path, file_path))
    if not os.path.exists(directory):
        os.makedirs(directory)
    # write the received data to the file
    with open(os.path.join(folder_path, file_path), 'wb') as f:
        f.write(file_data.data)
