import os
import shutil
import time

source_folder = "C:\\Users\\SORINAKE\\Desktop\\Veeam\\source_folder" #/path/to/folder
replica_folder = "C:\\Users\\SORINAKE\\Desktop\\Veeam\\replica_folder" #/path/to/folder
sync_interval = 60 # the interval of synchronization

while True:
    # create replica folder if it doesn't exist
    if not os.path.exists(replica_folder):
        os.mkdir(replica_folder)
    
    # synchronize files from source folder to replica folder
    for root, dirs, files in os.walk(source_folder):
        # construct corresponding directory in replica folder
        replica_root = root.replace(source_folder, replica_folder, 1)
        if not os.path.exists(replica_root):
            os.mkdir(replica_root)

        # synchronize files in the directory
        for file in files:
            source_path = os.path.join(root, file)
            replica_path = os.path.join(replica_root, file)

            # if file exists in replica folder, delete it
            if os.path.exists(replica_path):
                os.remove(replica_path)

            # copy file from source folder to replica folder
            shutil.copy2(source_path, replica_path)
    
    # remove any files in replica folder that are not in source folder
    for root, dirs, files in os.walk(replica_folder):
        source_root = root.replace(replica_folder, source_folder, 1)
        for file in files:
            source_path = os.path.join(source_root, file)
            replica_path = os.path.join(root, file)
            if not os.path.exists(source_path):
                os.remove(replica_path)

    # sleep for the synchronization interval
    time.sleep(sync_interval)
