docker login

cd testing || exit
docker buildx build --platform linux/amd64 -t mrsarius/testing:latest --push .

cd debug || exit
docker buildx build --platform linux/amd64 -t mrsarius/debug:latest --push .
cd ..
cd simple-client || exit
docker buildx build --platform linux/amd64 -t mrsarius/simple-client:latest --push .
cd ..
cd simple-server || exit
docker buildx build --platform linux/amd64 -t mrsarius/simple-server:latest --push .
cd ..
cd simple-udp-client || exit
docker buildx build --platform linux/amd64 -t mrsarius/simple-udp-client:latest --push .
cd ..
cd simple-udp-server || exit
docker buildx build --platform linux/amd64 -t mrsarius/simple-udp-server:latest --push .
cd ..

sudo ctr -n oakestra images pull docker.io/mrsarius/testing:latest
sudo ctr -n oakestra images pull docker.io/mrsarius/debug:latest
sudo ctr -n oakestra images pull docker.io/mrsarius/simple-server:latest
sudo ctr -n oakestra images pull docker.io/mrsarius/simple-client:latest
sudo ctr -n oakestra images pull docker.io/mrsarius/simple-udp-server:latest
sudo ctr -n oakestra images pull docker.io/mrsarius/simple-udp-client:latest