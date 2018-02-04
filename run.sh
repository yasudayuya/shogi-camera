docker run -ti --privileged -e DISPLAY=$DISPLAY -v $PWD:/app -v /tmp/.X11-unix/:/tmp/.X11-unix --name shogi naoys/shogi-camera:nogpu bash
