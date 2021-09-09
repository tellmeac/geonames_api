FROM python:3.7

EXPOSE 8000  

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY main.py .
COPY RU.txt .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
