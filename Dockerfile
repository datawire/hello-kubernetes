FROM python:3-alpine
MAINTAINER Datawire <dev@datawire.io>
LABEL PROJECT_REPO_URL         = "git@github.com:datawire/hello-kubernetes.git" \
      PROJECT_REPO_BROWSER_URL = "https://github.com/datawire/hello-kubernetes" \
      DESCRIPTION              = "Hello Kubernetes!" \
      VENDOR                   = "Datawire, Inc." \
      VENDOR_URL               = "https://datawire.io/"

WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./

EXPOSE 5000
ENTRYPOINT ["python3", "hello/hello.py"]
