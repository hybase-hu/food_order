from django.shortcuts import render


def error_404(request,exception):
    print("http error not found",exception)
    return render(request=request,template_name="404.html")