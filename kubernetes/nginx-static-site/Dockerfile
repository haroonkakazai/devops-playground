FROM ubuntu:24.04 AS builder

WORKDIR /app

COPY index.html .
COPY style.css .

FROM nginx:1.29.0

COPY --from=builder /app/index.html /usr/share/nginx/html/index.html
COPY --from=builder /app/style.css /usr/share/nginx/html/style.css