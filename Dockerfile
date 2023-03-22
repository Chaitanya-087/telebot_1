FROM python:alpine3.17
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV TELEGRAM_TOKEN=5621145137:AAFzWxaGL_t0FqUg-T5BzUieGVa3_DElmJo \
    GIPHY_TOKEN=HgPFKe1qUiDj8FYOgID3yQifXWayak1p
CMD ["python3","main.py"]