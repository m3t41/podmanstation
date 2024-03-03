"""Demonstrate PodmanClient."""
import json
from podman import PodmanClient
from flask import Flask, render_template

# Provide a URI path for the libpod service.  In libpod, the URI can be a unix
# domain socket(UDS) or TCP.  The TCP connection has not been implemented in this
# package yet.

uri = "unix:///run/podman/podman.sock"

with PodmanClient(base_url=uri) as client:
  version = client.version()
  print("Release: ", version["Version"])
  print("Compatible API: ", version["ApiVersion"])
  print("Podman API: ", version["Components"][0]["Details"]["APIVersion"], "\n")

#    # get all images
#  for image in client.images.list():
#    print(image, image.id, "\n")

    # find all containers
  imagename = {}
  i = 0
  for container in client.containers.list():
    print(container, container.name, "\n")
    data = container.inspect()
    print(data)
    imagename[i] = data['ImageName']
    print(imagename[i], "\n")
    status = data["State"]
    running = status["Running"]
    print(running, "\n")
    i = i + 1

print("LOL: ", imagename)


app = Flask('testapp')

@app.route('/')
def index():
    return render_template('index.html', imagename=imagename, running=running)

if __name__ == '__main__':
    app.run()
