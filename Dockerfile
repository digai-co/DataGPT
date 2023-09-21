FROM python:3

workdir /datagpt

COPY . /datagpt

RUN pip install -r requirements.txt

ENV GRADIO_SERVER_NAME="0.0.0.0"

EXPOSE 7860

CMD ["python", "server/app.py"]
