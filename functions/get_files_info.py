import os



def get_files_info(working_directory, directory=None):
    dir = os.path.join(working_directory, directory)
    # print(dir)
    abs_dir = os.path.abspath(dir)
    abs_working_dir = os.path.abspath(working_directory)
    if not (abs_dir == abs_working_dir or abs_dir.startswith(abs_working_dir + os.sep)):
        # print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_dir):
        # print(f'Error: "{directory}" is not a directory')
        return f'Error: "{directory}" is not a directory'
    
    directory_files = os.listdir(abs_dir)
    return_string = ''
    try:
        for file in directory_files:
            s = '- '+str(file)+': file_size='+str(os.path.getsize(os.path.join(abs_dir,file)))+' bytes, is_dir='+str(os.path.isdir(os.path.join(abs_dir,file)))+'\n'
            return_string += s 
        # print(return_string)
        return return_string
    except Exception as e:
        return f"Error: listing files - {e}"


get_files_info('calculator','.')