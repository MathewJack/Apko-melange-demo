# Apko-melange-demo
A Demo python app created using melange application has a APK and build a container using APKO container builder

    git clone this repo
	cd apko-melange-demo
	melange keygen

```bash
Run the below command to build the demo decoder app
  melange build melange-app.yaml --arch amd64 --signing-key melange.rsa
Run the below command to build the demo decoder container
  apko build apko-decoder.yaml apko-decoder:0.1 apko-decoder.tar -k melange.rsa.pub
```