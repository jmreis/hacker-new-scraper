FROM python:3-alpine
LABEL author="Jair Reis"
LABEL description="For run the hacker-news-scraper"
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
RUN apk add --no-cache pcre
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
CMD ["python", "scraper_hn.py"]