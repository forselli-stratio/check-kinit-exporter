FROM alpine:latest

USER root
ADD kms_utils.sh kms_utils.sh
ADD b-log.sh b-log.sh
ADD entrypoint.sh /entrypoint.sh
ADD check-kinit-http.py check-kinit-http.py

RUN apk update && \
    apk --no-cache add krb5 bash coreutils curl vim jq strace python3 && \
    pip3 install --no-cache-dir --upgrade --force-reinstall pip && \
    chmod +x /entrypoint.sh && \
    chmod +x /b-log.sh && \
    chmod +x check-kinit-http.py && \
    mkdir /tmp/0 && \
    touch /tmp/0/krb5cc_0

RUN cd /usr/bin \
  && ln -sf easy_install-3.5 easy_install \
  && ln -sf idle3.5 idle \
  && ln -sf pydoc3.5 pydoc \
  && ln -sf python3.5 python \
  && ln -sf python3.5-config python-config \
  && ln -sf pip3.5 pip

EXPOSE 9118

ENTRYPOINT [ "/entrypoint.sh" ]