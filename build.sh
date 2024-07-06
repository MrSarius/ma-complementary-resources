cd simple-client || exit
docker buildx build --platform linux/amd64 -t mrsarius/simple-client:latest --push .
cd ..
cd simple-client || exit
docker buildx build --platform linux/amd64 -t mrsarius/simple-server:latest --push .