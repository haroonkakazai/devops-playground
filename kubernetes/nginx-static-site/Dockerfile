FROM ubuntu AS builder

WORKDIR /app

COPY index.html .
COPY style.css .

FROM nginx

COPY --from=builder /app/index.html /usr/share/nginx/html/index.html
COPY --from=builder /app/style.css /usr/share/nginx/html/style.css