FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf

ADD ./nginx.conf /etc/nginx/conf.d/nginx.conf

ADD ./fullchain1.pem /etc/nginx/fullchain1.pem
ADD ./privkey1.pem /etc/nginx/privkey1.pem

EXPOSE 80 443

CMD ["nginx-debug", "-g", "daemon off;"]