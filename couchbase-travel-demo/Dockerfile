FROM ubuntu:16.04

MAINTAINER Couchbase Docker Team <docker@couchbase.com>

# Install dependencies:
#  runit: for container process management
#  wget: for downloading .deb
#  chrpath: for fixing curl, below
#  tzdata: timezone info used by some N1QL functions
# Additional dependencies for system commands used by cbcollect_info:
#  lsof: lsof
#  lshw: lshw
#  sysstat: iostat, sar, mpstat
#  net-tools: ifconfig, arp, netstat
#  numactl: numactl
RUN apt-get update && \
    apt-get install -yq apt-utils runit wget chrpath tzdata git\
    lsof lshw sysstat net-tools numactl python-httplib2 python-pip lsb-core lsb-release && \
    apt-get autoremove && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ARG CB_VERSION=6.5.0
ARG CB_RELEASE_URL=https://packages.couchbase.com/releases/6.5.0
ARG CB_PACKAGE=couchbase-server-enterprise_6.5.0-ubuntu16.04_amd64.deb
ARG CB_SHA256=5505c6bb026090dae7351e9d83caeab00437f19e48e826afd4cb6bafc484cd2b

ARG SG_VERSION=2.7.0
ARG SG_RELEASE_URL=http://packages.couchbase.com/releases/couchbase-sync-gateway/2.7.0
ARG SG_PACKAGE=couchbase-sync-gateway-enterprise_2.7.0_x86_64.deb
ARG SG_SHA256=d30ad3009a3ec0dc43e0ee2d8312b370572bc8219031a104b044bc22d3053d14
ARG SG_PACKAGE_NAME=couchbase-sync-gateway

ENV PATH=$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install:/opt/couchbase-sync/gateway/:/opt/couchbase-sync-gateway/bin

# Create Couchbase user with UID 1000 (necessary to match default
# boot2docker UID)
RUN groupadd -g 1000 couchbase && useradd couchbase -u 1000 -g couchbase -M


# possible todo
# Add section for downloading the travel-sample config
# move travel sample config to the default location
# create search index
# include search index build below
# include travel app container as secondary container deployment resulting in a 2 container deployment
# limit CPUs to 2 for couchbase and 1 for travel app containers

# Install couchbase
RUN export INSTALL_DONT_START_SERVER=1 && \
    wget -N --no-verbose $CB_RELEASE_URL/$CB_PACKAGE && \
    echo "$CB_SHA256  $CB_PACKAGE" | sha256sum -c - && \
    dpkg -i ./$CB_PACKAGE && rm -f ./$CB_PACKAGE

# Install couchbase-sync-gateway
RUN export INSTALL_DONT_START_SERVER=1 && \
    wget -N --no-verbose $SG_RELEASE_URL/$SG_PACKAGE && \
    echo "$SG_SHA256  $SG_PACKAGE" | sha256sum -c - && \
    dpkg --unpack ./$SG_PACKAGE &&\ 
    rm /var/lib/dpkg/info/"$SG_PACKAGE_NAME".postinst -f &&\ 
    dpkg --configure $SG_PACKAGE_NAME && rm -f ./$SG_PACKAGE &&\
    apt-get install -yf &&\
    mkdir -p /opt/couchbase-sync-gateway/data && \
    mkdir /etc/sync-gateway && \
    chown -R couchbase:couchbase /opt/couchbase-sync-gateway

# Add runit script for couchbase-server
COPY scripts/run /etc/service/couchbase-server/run
RUN cp -av /etc/service/couchbase-server /etc/service/couchbase-sync-gateway
COPY scripts/runsg /etc/service/couchbase-sync-gateway/run

RUN chown -R couchbase:couchbase /etc/service


#create a default configuration for SG
COPY config/sync-gateway-config-travelsample.json /etc/sync-gateway/config.json
COPY config/fts-hotels-index.json /tmp/fts-hotels-index.json

# Add dummy script for commands invoked by cbcollect_info that
# make no sense in a Docker container
COPY scripts/dummy.sh /usr/local/bin/
RUN ln -s dummy.sh /usr/local/bin/iptables-save && \
    ln -s dummy.sh /usr/local/bin/lvdisplay && \
    ln -s dummy.sh /usr/local/bin/vgdisplay && \
    ln -s dummy.sh /usr/local/bin/pvdisplay

# Fix curl RPATH
RUN chrpath -r '$ORIGIN/../lib' /opt/couchbase/bin/curl

# Add bootstrap script
COPY scripts/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["couchbase-server"]
# If user doesn't specify any args, use the default config
#CMD ["/etc/sync-gateway/config.json"]

# 4984: Couchbase Sync Gateway REST/HTTP/WSS Interface
# 4985: Couchbase Sync Gateway REST/HTTP Admin interface on /_admin/
# 8091: Couchbase Web console, REST/HTTP interface
# 8092: Views, queries, XDCR
# 8093: Query services (4.0+)
# 8094: Full-text Search (4.5+)
# 8095: Analytics (5.5+)
# 8096: Eventing (5.5+)
# 11207: Smart client library data node access (SSL)
# 11210: Smart client library/moxi data node access
# 11211: Legacy non-smart client library data node access
# 18091: Couchbase Web console, REST/HTTP interface (SSL)
# 18092: Views, query, XDCR (SSL)
# 18093: Query services (SSL) (4.0+)
# 18094: Full-text Search (SSL) (4.5+)
# 18095: Analytics (SSL) (5.5+)
# 18096: Eventing (SSL) (5.5+)
EXPOSE 4984 4985 8091 8092 8093 8094 8095 8096 11207 11210 11211 18091 18092 18093 18094 18095 18096

