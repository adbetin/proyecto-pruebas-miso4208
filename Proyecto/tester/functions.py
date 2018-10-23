import os
import sys
import subprocess as sub
from threading import Thread
from queue import Queue, Empty


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


def cypress_tester():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    p = sub.Popen(["/home/andresdavid/PruebasAutomaticas/cypress/node_modules/.bin/cypress", "run", "."], stdout=sub.PIPE,
                  stderr=sub.PIPE)

    output, errors = p.communicate()

    os.chdir(dir_path)
    return output, errors


def mdroid_tester(application, options, multithread, workspace):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # sub.chdir(workspace)
    # os.system("start /wait cmd ")

    # p = sub.Popen(["/home/andresdavid/.sdkman/candidates/gradle/current/bin/gradle", "test"], stdout=sub.PIPE, stderr=sub.PIPE)

    mdroid_path = '/home/andresdavid/PruebasAutomaticas/S9/'

    p = sub.Popen(['/usr/local/java/jdk1.8.0_181/bin/java',
                   '-jar',
                   mdroid_path + 'MDroidPlus/target/MDroidPlus-1.0.0.jar',
                   mdroid_path + 'MDroidPlus/libs4ast/',
                   mdroid_path + application + '/',
                   application,
                   mdroid_path + 'MDroidPlus/tmp/mutants/' + application + '/',
                   mdroid_path + 'MDroidPlus/',
                   multithread], stdout=sub.PIPE, stderr=sub.PIPE)
    q = Queue()
    t = Thread(target=enqueue_output, args=(p.stdout, q))
    t.daemon = True  # thread dies with the program
    t.start()

    # output = ""
    # for c in iter(lambda: p.stdout.read(1), b''):  # replace '' with b'' for Python 3
    #    print(c.decode() + "\n")
    #    output += c.decode() + "\n"

    # output1, errors = p.communicate()

    # os.chdir(os.joi) creo se debe regresar al anterior
    os.chdir(dir_path)
    return ""


def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        print(line)
        #queue.put(line)
    out.close()
