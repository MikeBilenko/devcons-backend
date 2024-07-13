FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf

ADD ./nginx.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 80

CMD ["nginx-debug", "-g", "daemon off;"]