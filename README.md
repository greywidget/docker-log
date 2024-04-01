One of my projects uses Playwright, and that involves a pretty big image. 
When you run the Playwright install, even if you only include one of the 
browsers, the size of that layer is about 800MB.  

This was a quick investigation to see how I could control rebuilding image 
layers. Remember of course that once one layer needs to be rebuild, all the 
layers below that layer will also need rebuilding.

In this example I wanted to rebuild the `RUN git clone...` and below it I had 
changed the repo. To achieve that, I added the `ARG CACHEBUST` line above the 
`RUN git clone...`. The value of CACHEBUST is defined in the `docker-compose.yml` file and to force a rebuild, the value needs to be changed. This will cause that layer and all subsequent layers to be rebuilt. 

The actual value for that `ARG` is stored as part of the Image and so if you haven't cleaned up your images and you set it to a value that you have used before, you might find you use an old cached version instead of building a new image.

Note that in order for this to work, you must include the `--build` option when running your `docker-compose` cmd e.g.:  

```yml
docker-compose up --build -d
```

I also decided to get rid of the `startup.sh` file and call my real `CMD` directly in the Dockerfile as I was having issues with permissions and line endings.
