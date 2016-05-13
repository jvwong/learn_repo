from django.conf.urls import url
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        """<!DOCTYPE html>
            <html>
                <body>
                    <h1>My First Heading</h1>
                    <p>My first paragraph.</p>
                </body>
            </html>
        """)
