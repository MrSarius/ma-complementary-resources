cd client
sudo docker buildx build --platform linux/amd64 -t mrsarius/test1-client:latest --push .
cd ..
cd server
sudo docker buildx build --platform linux/amd64 -t mrsarius/test1-server:latest --push .