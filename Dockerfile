ARG BASE_IMAGE
ARG PROJECT_NAME
FROM ${BASE_IMAGE}
ENV PROJECT_NAME=whatsapp_agent

USER root
RUN mkdir -p /usr/src/${PROJECT_NAME}
RUN chown -R 1001:0 /usr/src/${PROJECT_NAME}
COPY entrypoint.sh /usr/src/${PROJECT_NAME}/entrypoint.sh
RUN chmod +x /usr/src/${PROJECT_NAME}/entrypoint.sh
USER 1001

WORKDIR /usr/src/${PROJECT_NAME}
RUN python -m venv /usr/src/${PROJECT_NAME}/env

ENV PATH="/usr/src/${PROJECT_NAME}/env/bin:$PATH"

COPY --chown=1001 app app
COPY --chown=1001 requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD /usr/src/${PROJECT_NAME}/entrypoint.sh