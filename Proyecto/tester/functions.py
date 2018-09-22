import os
import subprocess as sub


# Create your views here.

def create_file(directory, filename, content):
    file_output = os.path.join(directory, filename)
    f = open(filename, "w+")
    f.write(content)
    f.close()
    print(file_output)
    return file_output


def delete_file(filepath):
    os.remove(filepath)


def cypress_tester(command, workspace):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    os.chdir(workspace)
    # os.system("start /wait cmd ")

    p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = p.communicate()

    # os.chdir(os.joi) creo se debe regresar al anterior
    os.chdir(dir_path)
    return output, errors
