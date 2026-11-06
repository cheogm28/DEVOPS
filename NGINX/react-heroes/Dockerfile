from node:19-alpine3.15 as install
RUN echo "------install fase -----"
WORKDIR /app
COPY package.json package.json
RUN yarn install --frozen-lockfile

from node:19-alpine3.15 as build
RUN echo "-----build fase-----"
WORKDIR /app
COPY --from=install /app/node_modules ./node_modules
COPY . .
RUN yarn add esbuild --platform=linux --arch=x64
RUN yarn build


from nginx as execute
RUN echo "-----exec fase-----"

COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx","-g","daemon off;"]
