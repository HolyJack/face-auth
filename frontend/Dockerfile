FROM node:alpine as build

COPY . /app/
WORKDIR /app
RUN rm -rf node_modules && npm install && npm run build


FROM node:alpine as production
WORKDIR /app
COPY --from=build /app/dist/ /app/
COPY --from=build /app/node_modules /app/

RUN npm install -g serve
ENTRYPOINT ["serve", "-s", "/app", "-l", "8080"]
