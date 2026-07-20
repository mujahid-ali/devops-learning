FROM python:3.12-alpine

WORKDIR /app
COPY app/main.py ./main.py

EXPOSE 8080
USER 65532:65532
CMD ["python", "main.py"]
