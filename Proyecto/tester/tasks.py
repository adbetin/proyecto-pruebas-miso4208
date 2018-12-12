from __future__ import absolute_import, unicode_literals

import os
import subprocess

from celery import shared_task
from testcore.models import Application


def getApplicationById(app_id):
    obj, created = Application.objects.get(id=app_id)
    return obj


@shared_task
def random_testing(application_id, num_event, package):
    # se crea registro mutantTest y mutant log
    # application = getApplicationById(application_id)
    # test = ApplicationTest.objects.create(name="Random Testing", applica=mutant, testType=MutantType.MONKEY.value)
    # log = MutantLog.objects.create(mutantTest=test, worker_ip=get_machine_url(), report_text="",
    #                                started_at=datetime.datetime.now())

    # se firma la aplicacion
    keystore_path = os.path.join(os.environ.get("HOME"), "ks", "proyecto.keystore")
    apk_path = os.path.join(os.environ.get("HOME"), "test", "apps", str(application_id), package + ".apk")
    proc = subprocess.Popen([
        "jarsigner",
        "-verbose",
        "-sigalg",
        "SHA1withRSA",
        "-digestalg",
        "SHA1",
        "-keystore",
        keystore_path,
        apk_path,
        "proyecto_alias",
        "-storepass",
        "123456",
    ], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    # log.report_text += str(out)
    # log.save()

    # se desinstala la aplicacion
    proc = subprocess.Popen([
        "adb",
        "uninstall",
        package
    ], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    # log.report_text += str(out)
    # log.save()

    # se instala la aplicacion
    proc = subprocess.Popen([
        "adb",
        "install",
        apk_path
    ], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    # log.report_text += str(out)
    # log.save()

    # proceso que ejecuta el monkey testing
    proc = subprocess.Popen([
        "adb",
        "shell",
        "monkey",
        "-p",
        package,
        "-v",
        str(num_event)
    ], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    # log.report_text += str(out)

    if "Monkey aborted due to error" not in str(out):
        print("Random ejecutado con exito para aplicacion" + package)
    # test.status = MutantStatus.SUCCESS.value
    else:
        print("Random ejecutado fallido para application" + package)
        # test.status = MutantStatus.FAIL.value

    # log.finished_at = datetime.datetime.now()
    # log.save()

    # test.save()

# # Calabash
# @shared_task
# def calabash_testing(mutant_n, packageHerramienta):
#     # se crea registro mutantTest y mutant log
#     mutant = getMutantByName(mutant_n)
#     test = MutantTest.objects.create(name="Calabash Testing", mutant=mutant, testType=MutantType.CALABASH.value)
#     log = MutantLog.objects.create(mutantTest=test, worker_ip=get_machine_url(), report_text="",
#                                    started_at=datetime.datetime.now())
#
#     mutant_folder = os.path.join(os.environ.get("HOME"), "parcial2", "parcial2", mutant.name)
#     print("mutant_folder", mutant_folder)
#     mutant_path = os.path.join(os.environ.get("HOME"), "parcial2", "parcial2", mutant.name,
#                                packageHerramienta) + "_3110.apk"
#     mutant_path_uncompressed = os.path.join(os.environ.get("HOME"), "parcial2", "parcial2", mutant.name, "uncompress")
#     mutant_path_final = os.path.join(os.environ.get("HOME"), "parcial2", "parcial2", mutant.name,
#                                      packageHerramienta) + "_3110_Compressed.apk"
#     rutaJar = os.path.join(os.environ.get("HOME"), "tools", "apktool.jar")
#     rutaFeature = os.path.join(os.environ.get("HOME"), "tools")
#
#     # se descomprime el archivo
#     proc = subprocess.Popen([
#         "/usr/bin/java",
#         "-jar",
#         rutaJar,
#         "d",
#         "-f",
#         mutant_path,
#         "-o",
#         mutant_path_uncompressed
#     ], stdout=subprocess.PIPE)
#     (out, err) = proc.communicate()
#     log.report_text += str(out)
#     log.save()
#
#     # se edita el archivo
#     prefileRead = open(mutant_path_uncompressed + "/AndroidManifest.xml", 'r')
#     print("file: ", prefileRead)
#     if "android.permission.INTERNET" not in prefileRead.read():
#         fileRead = open(mutant_path_uncompressed + "/AndroidManifest.xml", 'r')
#         data = fileRead.readlines()
#         data[3] = data[3] + '\n\t<uses-permission android:name="android.permission.INTERNET" />\n'
#
#         with open(mutant_path_uncompressed + "/AndroidManifest.xml", 'w') as fileWrite:
#             fileWrite.writelines(data)
#         fileRead.close()
#
#     # se comprime el archivo
#     proc = subprocess.Popen([
#         "/usr/bin/java",
#         "-jar",
#         rutaJar,
#         "b",
#         "-f",
#         mutant_path_uncompressed,
#         "-o",
#         mutant_path_final
#     ], stdout=subprocess.PIPE)
#     (out, err) = proc.communicate()
#     log.report_text += str(out)
#     log.save()
#
#     print("Crea carpeta para screenshots")
#     command = "mkdir " + mutant_n
#     print("comando", command)
#     subprocess.call(command, shell=True, cwd=rutaFeature)
#
#     # se firma el apk
#     proc = subprocess.Popen([
#         "calabash-android",
#         "resign",
#         mutant_path_final
#     ], stdout=subprocess.PIPE, cwd=rutaFeature)
#     (out, err) = proc.communicate()
#     log.report_text += str(out)
#     log.save()
#
#     # se ejecuta calabash
#     my_env = os.environ.copy()
#     my_env["SCREENSHOT_PATH"] = mutant_n + "/"
#     proc = subprocess.Popen([
#         "calabash-android",
#         "run",
#         mutant_path_final
#     ], stdout=subprocess.PIPE, cwd=rutaFeature, env=my_env)
#     (out, err) = proc.communicate()
#     log.report_text += str(out)
#     log.save()
#
#     if "failed" not in log.report_text:
#         print("Calabash ejecutado con exito para mutante" + mutant.name)
#         test.status = MutantStatus.SUCCESS.value
#     else:
#         print("Calabash ejecutado fallido para mutante" + mutant.name)
#         test.status = MutantStatus.FAIL.value
#
#     log.finished_at = datetime.datetime.now()
#     log.save()
#
#     test.save()
#
#
# # Vrt
# @shared_task
# def vrt_testing(mutant_n):
#     # se crea registro mutantTest y mutant log
#     mutant = getMutantByName(mutant_n)
#     test = MutantTest.objects.create(name="VRT Testing", mutant=mutant, testType=MutantType.VRT.value)
#     log = MutantLog.objects.create(mutantTest=test, worker_ip=get_machine_url(), report_text="",
#                                    started_at=datetime.datetime.now())
#
#     mutant_folder = os.path.join(os.environ.get("HOME"), "tools", mutant.name)
#     baseline_folder = os.path.join(os.environ.get("HOME"), "tools", "baseline")
#
#     # se ejecuta el script para las 8 screenshots que se toman
#     for x in range(8):
#         proc = subprocess.Popen([
#             "node",
#             "vrt.js",
#             baseline_folder,
#             mutant_folder,
#             x
#         ], stdout=subprocess.PIPE)
#         (out, err) = proc.communicate()
#         log.report_text += str(out)
#         log.save()
#
#     test.status = MutantStatus.SUCCESS.value
#     log.finished_at = datetime.datetime.now()
#     log.save()
#
#     test.save()
