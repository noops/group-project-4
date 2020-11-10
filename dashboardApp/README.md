#building docker image
docker build --tag team4:latest .

#running docker
docker run --publish 5000:5000 --detach --name team4 team4:latest

#stop container
docker stop team4

#starting container
docker start team4

#removing
docker stop team4 && docker rm team4