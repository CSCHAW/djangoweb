from django.shortcuts import render
from django.http import HttpResponse
from aws_logger.models import Log


def log(request):
    data = request.GET["log"]
    if data:
        Log(ip=data).save()
    return HttpResponse(f"Hello world! data: {data}")


def view_log(request):
    data = {"logs": Log.objects.all()}
    return render(request, "view_log.html", data)
