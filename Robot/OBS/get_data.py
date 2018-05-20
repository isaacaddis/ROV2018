def gata_data(dir):
    for i in os.listdir(directory):
        full_path = os.path.join(directory,i)
        if os.path.isdir(full_path):
            for entry in grab_files(full_path):
                yield entry
            elif os.path.isfile(full_path):
                yield full_path
            else:
                print('No such path %s' % full_path)
