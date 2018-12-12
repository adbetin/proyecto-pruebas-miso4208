import os
import subprocess as sub
from threading import Thread
from queue import Queue, Empty
import channels.layers
from asgiref.sync import async_to_sync

# Create your views here.

# from proyectoprueba.consumers import ws_message
from testcore.models import ApplicationTest, TestExecution, TestResult


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
    dir_path = os.path.dirname(__file__)
    cypress_path = os.path.abspath(os.path.join(dir_path, '..', 'tools', 'cypress'))
    cypress_bin_path = os.path.abspath(
        os.path.join(dir_path, '..', 'tools', 'cypress', 'node_modules', '.bin', 'cypress'))

    p = sub.Popen([cypress_bin_path,
                   "run",
                   "--project",
                   cypress_path, ], stdout=sub.PIPE, stderr=sub.PIPE)

    # se crea la ejecucion

    # se obtiene el test
    test = ApplicationTest.objects.get(testhash='31c4fb6c-41d8-4b7b-a16e-fc531155398e')

    testExecution = TestExecution()
    testExecution.applicationTest = test
    testExecution.reportText = ''
    testExecution.save()

    q = Queue()
    t = Thread(target=enqueue_output, args=(p.stdout, testExecution, q))
    t.daemon = True  # thread dies with the program

    testExecution.status = TestResult.PROGRESS.value
    testExecution.save()

    t.start()

    # output, errors = p.communicate()

    os.chdir(dir_path)
    return ""


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
                   mdroid_path + application + '/app/src/main/',
                   application,
                   mdroid_path + 'MDroidPlus/tmp/mutants/' + application + '/',
                   mdroid_path + 'MDroidPlus/',
                   multithread], stdout=sub.PIPE, stderr=sub.PIPE)

    # se obtiene el test
    test = ApplicationTest.objects.get(testhash='31c4fb6c-41d8-4b7b-a16e-fc531155398e')

    testExecution = TestExecution()
    testExecution.applicationTest = test
    testExecution.reportText = ''
    testExecution.save()

    q = Queue()
    t = Thread(target=enqueue_output, args=(p.stdout, testExecution, q))
    t.daemon = True  # thread dies with the program

    testExecution.status = TestResult.PROGRESS.value
    testExecution.save()
    t.start()

    # output = ""
    # for c in iter(lambda: p.stdout.read(1), b''):  # replace '' with b'' for Python 3
    #    print(c.decode() + "\n")
    #    output += c.decode() + "\n"

    # output1, errors = p.communicate()

    # os.chdir(os.joi) creo se debe regresar al anterior
    os.chdir(dir_path)
    return ""


def enqueue_output(out, testExecution, queue):
    for line in iter(out.readline, b''):
        testExecution.reportText = testExecution.reportText + str(line.decode('utf-8'))
        testExecution.save()
        print(line)
        # ws_message(line.decode('utf-8'), str(testExecution.executionhash))

        channel_layer = channels.layers.get_channel_layer()
        terminal_name = 'terminal_%s' % testExecution.executionhash

        async_to_sync(channel_layer.group_send)(
            terminal_name,
            {
                'type': 'chat_message',
                'message': str(line.decode('utf-8'))
            }
        )
    out.close()
