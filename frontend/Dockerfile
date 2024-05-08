FROM node:alpine as build

COPY . /app/
WORKDIR /app
RUN rm -rf node_modules && npm install && npm run build

FROM nginx:alpine as production
WORKDIR /app

COPY --from=build /app/dist/ /usr/share/nginx/html
COPY /deployment/nginx.default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
