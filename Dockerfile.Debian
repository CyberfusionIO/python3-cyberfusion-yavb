FROM debian:latest

RUN apt-get update
RUN apt-get install -y build-essential devscripts equivs dh-python

COPY ./ /build/
WORKDIR /build/

RUN mk-build-deps -i -t 'apt -o Debug::pkgProblemResolver=yes --no-install-recommends -y'
RUN dpkg-buildpackage -us -uc

RUN apt-get install -y ../python3-cyberfusion-yavb_*.deb

ENTRYPOINT ["/usr/bin/yavb"]
