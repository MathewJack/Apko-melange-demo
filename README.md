# Apko-melange-demo
A Demo python app created using melange application has a APK and build a container using APKO container builder

## To get started follow the below
#### Make sure both apko and melange are installed

    git clone https://github.com/MathewJack/Apko-melange-demo.git
	cd Apko-melange-demo
	melange keygen

#### Run the below command to build the demo decoder app
```bash
melange build melange-app.yaml --arch amd64 --signing-key melange.rsa
```
#### Run the below command to build the demo decoder container
```bash
  apko build apko-decoder.yaml apko-decoder:0.1 apko-decoder.tar -k melange.rsa.pub
```

#### Now the container shoudld be in tar file under current folder
```bash
  docker load < decoder.tar
  docker images
  docker run -it decoder:version
```
##### This will get you a shell inside your build container


## You can check out below links for the install instructions for apk and melange

[Apko](https://github.com/chainguard-dev/apko)
[Melange](https://github.com/chainguard-dev/melange)
