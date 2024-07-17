docker login

cd client
docker buildx build --platform linux/amd64 -t mrsarius/test1-client:latest --push .
cd ..
cd server
docker buildx build --platform linux/amd64 -t mrsarius/test1-server:latest --push .

sudo ctr -n oakestra images pull docker.io/mrsarius/test1-client:latest
sudo ctr -n oakestra images pull docker.io/mrsarius/test1-server:latest