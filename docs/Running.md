# Running the project

Here a simple diagram of how the system works:

![Overview](./images/UML_NGINX.jpeg)

In order to run this project you will need to:

1. Turn on your `Go Pro` and Raspberry
2. Connect the Raspberry to the Go Pro's Wifi
3. Start NGINX 
4. Open a terminal on the Raspberry and run the [Go Pro Stream Start Script](./scripts/GoPro.md). This will allow you to 
receive the images recorded by the camera.
5. Open another Terminal and Run the [Adaptative Livestream Script](./scripts/Livestream.md)
6. Connect the Smartphone to the Hotspot Created by the Raspberry
2. [Access the Stream on the Smartphone](./Website/Test.md)

