import uuid
from enum import Enum
from django.db import models


class ApplicationType(models.Model):
    name = models.CharField(max_length=255)  # el nombre de la tipo
    mobile = models.BooleanField(default=False)  # verifica si se ejecuta sobre moviles

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=255)  # el nombre de la aut
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=500, blank=True)  # url de recurso aut bajo pruebas
    repositoryUrl = models.URLField(max_length=500, blank=True)  # url del repositorio
    apphash = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    applicationType = models.ForeignKey(ApplicationType, on_delete=models.PROTECT, related_name="applications")
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    ready = models.BooleanField(default=False)
    package_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TestResult(Enum):
    NOTRUN = "No ejecutado"
    START = "Iniciado"
    PROGRESS = "Progreso"
    SUCCESS = "Exitosa"
    FAIL = "Fallida"
    UNDEFINED = "No definido"


class TestType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    testType = models.ForeignKey(TestType, on_delete=models.PROTECT, related_name="libraries")
    command = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ApplicationTest(models.Model):
    name = models.CharField(max_length=255)  # el nombre de la prueba
    description = models.TextField(blank=True, null=True)
    value = models.TextField()
    testType = models.ForeignKey(TestType, on_delete=models.PROTECT, related_name="appTests")
    library = models.ForeignKey(Library, on_delete=models.PROTECT, related_name="libraries")
    testhash = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    application = models.ForeignKey(Application, on_delete=models.PROTECT, related_name="applicationTests")
    status = models.CharField(
        max_length=100,
        choices=[(tag.value, tag.name) for tag in TestResult],
        default=TestResult.NOTRUN.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    last_run = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s: %s" % (self.application.name, self.name)


class TestExecution(models.Model):
    applicationTest = models.ForeignKey(ApplicationTest, on_delete=models.PROTECT, related_name="testExecutions")
    status = models.CharField(
        max_length=100,
        choices=[(tag.value, tag.name) for tag in TestResult],
        default=TestResult.NOTRUN.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(default=None, blank=True, null=True)
    finished_at = models.DateTimeField(default=None, blank=True, null=True)
    reportText = models.TextField(blank=True, null=True)
    executionhash = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    report_status = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s: %s - %s" % (self.applicationTest.application.name, self.applicationTest.name, str(self.created_at))


class TestParameter(models.Model):
    test = models.ForeignKey(TestExecution, db_index=True, on_delete=models.CASCADE, related_name="parameters")
    key = models.CharField(max_length=240, db_index=True)
    value = models.CharField(max_length=240, db_index=True)
    type = models.CharField(max_length=240, db_index=True)
