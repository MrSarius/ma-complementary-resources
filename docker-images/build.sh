cd debug || exit
docker buildx build --platform linux/amd64 -t mrsarius/debug:latest --push .
cd ..
cd simple-client || exit
docker buildx build --platform linux/amd64 -t mrsarius/simple-client:latest --push .
cd ..
cd simple-server || exit
docker buildx build --platform linux/amd64 -t mrsarius/simple-server:latest --push .

sudo ctr -n oakestra images pull docker.io/mrsarius/debug:latest
sudo ctr -n oakestra images pull docker.io/mrsarius/simple-server:latest
sudo ctr -n oakestra images pull docker.io/mrsarius/simple-client:latest