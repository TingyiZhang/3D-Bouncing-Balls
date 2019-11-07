# 3D-Bouncing-Balls
Simulation of elastic collisions between spheres in 3-dimension universe.

Basic model is based on this:https://en.wikipedia.org/wiki/Elastic_collision. It also can be applied to 3-dimension situation.

## Introduction
- Every balls have a max collisions limit. Once a ball reach this limit, it disappears. A ball colliding with a ball or reflecting with wall is counted for one collision, called 'bounces'.
- Everytime when multiple collisions happen simultaneously, I deal with the balls pair-wise.
- The function of this programm is to keep printing out a report that record every collision events, until there no events gonna happen.

## Universe parameters
- Command line: In command line, there are two parameters, the universe radius, and the max collision.
>`python 3dballs.py 120 3`
That means the universe radius is 120m, and the max collision of a ball is 3 times.

- Input: 9 parameters: mass, radius, x, y, z, vx, vy, vz, name. The position of the centre of a ball is (x,y,z), and the velocity is (vx,vy,vz). Use space to separate different parameters, and use enter to switch line, and input parameters for a new ball.
>`5 1 10 10 10 2 2 2 one`
That means, the ball's name is 'one', mass=5, radius=1, position=(10,10,10), velocity(2,2,2).

- Input format: Please input parameters in right format, or the programm will exit with return code 1. But in this programm, there is no detections for the initial state error such as balls overlapping or balls outside of the universe. Please make sure the initial states is right, or the results will be strange...

## Output example
In this case, it's called "smash up", and it's really fun.
```
Here are the initial conditions.
universe radius 2000.0
max collisions 5
xdown m=10 r=10 p=(100,0,0) v=(-1,0,0) bounces=0
xup m=20 r=10 p=(-100,0,0) v=(1,0,0) bounces=0
ydown m=30 r=10 p=(0,100,0) v=(0,-1,0) bounces=0
yup m=40 r=10 p=(0,-100,0) v=(0,1,0) bounces=0
zdown m=50 r=10 p=(0,0,100) v=(0,0,-1) bounces=0
zup m=60 r=10 p=(0,0,-100) v=(0,0,1) bounces=0
energy: 105
momentum: (10,10,10)
```

There are six balls, colliding toghter in the middle.

I redirected the output to a txt file, here is the result:
```
Here are the events.

time of events: 85.8579
colliding xdown ydown
xdown m=10 r=10 p=(14.1421,0,0) v=(0.5,-1.5,0) bounces=1
xup m=20 r=10 p=(-14.1421,0,0) v=(1,0,0) bounces=0
ydown m=30 r=10 p=(0,14.1421,0) v=(-0.5,-0.5,0) bounces=1
yup m=40 r=10 p=(0,-14.1421,0) v=(0,1,0) bounces=0
zdown m=50 r=10 p=(0,0,14.1421) v=(0,0,-1) bounces=0
zup m=60 r=10 p=(0,0,-14.1421) v=(0,0,1) bounces=0
energy: 105
momentum: (10,10,10)


time of events: 85.8579
colliding xdown yup
xdown m=10 r=10 p=(14.1421,0,0) v=(2.1,0.1,0) bounces=2
xup m=20 r=10 p=(-14.1421,0,0) v=(1,0,0) bounces=0
ydown m=30 r=10 p=(0,14.1421,0) v=(-0.5,-0.5,0) bounces=1
yup m=40 r=10 p=(0,-14.1421,0) v=(-0.4,0.6,0) bounces=1
zdown m=50 r=10 p=(0,0,14.1421) v=(0,0,-1) bounces=0
zup m=60 r=10 p=(0,0,-14.1421) v=(0,0,1) bounces=0
energy: 105
momentum: (10,10,10)


time of events: 85.8579
colliding xup ydown
xdown m=10 r=10 p=(14.1421,0,0) v=(2.1,0.1,0) bounces=2
xup m=20 r=10 p=(-14.1421,0,0) v=(-0.2,-1.2,0) bounces=1
ydown m=30 r=10 p=(0,14.1421,0) v=(0.3,0.3,0) bounces=2
yup m=40 r=10 p=(0,-14.1421,0) v=(-0.4,0.6,0) bounces=1
zdown m=50 r=10 p=(0,0,14.1421) v=(0,0,-1) bounces=0
zup m=60 r=10 p=(0,0,-14.1421) v=(0,0,1) bounces=0
energy: 105
momentum: (10,10,10)


time of events: 85.8579
colliding xup yup
xdown m=10 r=10 p=(14.1421,0,0) v=(2.1,0.1,0) bounces=2
xup m=20 r=10 p=(-14.1421,0,0) v=(-1.53333,0.133333,0) bounces=2
ydown m=30 r=10 p=(0,14.1421,0) v=(0.3,0.3,0) bounces=2
yup m=40 r=10 p=(0,-14.1421,0) v=(0.266667,-0.0666667,0) bounces=2
zdown m=50 r=10 p=(0,0,14.1421) v=(0,0,-1) bounces=0
zup m=60 r=10 p=(0,0,-14.1421) v=(0,0,1) bounces=0
energy: 105
momentum: (10,10,10)


time of events: 85.8579
colliding ydown zdown
xdown m=10 r=10 p=(14.1421,0,0) v=(2.1,0.1,0) bounces=2
xup m=20 r=10 p=(-14.1421,0,0) v=(-1.53333,0.133333,0) bounces=2
ydown m=30 r=10 p=(0,14.1421,0) v=(0.3,0.7375,-0.4375) bounces=3
yup m=40 r=10 p=(0,-14.1421,0) v=(0.266667,-0.0666667,0) bounces=2
zdown m=50 r=10 p=(0,0,14.1421) v=(0,-0.2625,-0.7375) bounces=1
zup m=60 r=10 p=(0,0,-14.1421) v=(0,0,1) bounces=0
energy: 105
momentum: (10,10,10)


time of events: 85.8579
colliding ydown zup
xdown m=10 r=10 p=(14.1421,0,0) v=(2.1,0.1,0) bounces=2
xup m=20 r=10 p=(-14.1421,0,0) v=(-1.53333,0.133333,0) bounces=2
ydown m=30 r=10 p=(0,14.1421,0) v=(0.3,1.20417,0.0291667) bounces=4
yup m=40 r=10 p=(0,-14.1421,0) v=(0.266667,-0.0666667,0) bounces=2
zdown m=50 r=10 p=(0,0,14.1421) v=(0,-0.2625,-0.7375) bounces=1
zup m=60 r=10 p=(0,0,-14.1421) v=(0,-0.233333,0.766667) bounces=1
energy: 105
momentum: (10,10,10)


time of events: 85.8579
colliding yup zdown
xdown m=10 r=10 p=(14.1421,0,0) v=(2.1,0.1,0) bounces=2
xup m=20 r=10 p=(-14.1421,0,0) v=(-1.53333,0.133333,0) bounces=2
ydown m=30 r=10 p=(0,14.1421,0) v=(0.3,1.20417,0.0291667) bounces=4
yup m=40 r=10 p=(0,-14.1421,0) v=(0.266667,-0.585185,-0.518519) bounces=3
zdown m=50 r=10 p=(0,0,14.1421) v=(0,0.152315,-0.322685) bounces=2
zup m=60 r=10 p=(0,0,-14.1421) v=(0,-0.233333,0.766667) bounces=1
energy: 105
momentum: (10,10,10)


time of events: 85.8579
colliding yup zup
xdown m=10 r=10 p=(14.1421,0,0) v=(2.1,0.1,0) bounces=2
xup m=20 r=10 p=(-14.1421,0,0) v=(-1.53333,0.133333,0) bounces=2
ydown m=30 r=10 p=(0,14.1421,0) v=(0.3,1.20417,0.0291667) bounces=4
yup m=40 r=10 p=(0,-14.1421,0) v=(0.266667,-1.14519,0.0414815) bounces=4
zdown m=50 r=10 p=(0,0,14.1421) v=(0,0.152315,-0.322685) bounces=2
zup m=60 r=10 p=(0,0,-14.1421) v=(0,0.14,0.393333) bounces=2
energy: 105
momentum: (10,10,10)


time of events: 97.4285
colliding zdown zup
xdown m=10 r=10 p=(38.4404,1.15706,0) v=(2.1,0.1,0) bounces=2
xup m=20 r=10 p=(-31.8838,1.54275,0) v=(-1.53333,0.133333,0) bounces=2
ydown m=30 r=10 p=(3.47119,28.0751,0.337476) v=(0.3,1.20417,0.0291667) bounces=4
yup m=40 r=10 p=(3.0855,-27.3926,0.479966) v=(0.266667,-1.14519,0.0414815) bounces=4
zdown m=50 r=10 p=(0,1.76238,10.4085) v=(0,0.157879,0.458291) bounces=3
zup m=60 r=10 p=(0,1.61989,-9.59102) v=(0,0.135363,-0.25748) bounces=3
energy: 105
momentum: (10,10,10)


time of events: 1025.69
reflecting xdown
xdown m=10 r=10 p=(1987.78,93.9827,0) v=(-2.10007,-0.0985803,0) bounces=3
xup m=20 r=10 p=(-1455.21,125.31,0) v=(-1.53333,0.133333,0) bounces=2
ydown m=30 r=10 p=(281.948,1145.85,27.4116) v=(0.3,1.20417,0.0291667) bounces=4
yup m=40 r=10 p=(250.621,-1090.42,38.9854) v=(0.266667,-1.14519,0.0414815) bounces=4
zdown m=50 r=10 p=(0,148.315,435.82) v=(0,0.157879,0.458291) bounces=3
zup m=60 r=10 p=(0,127.272,-248.598) v=(0,0.135363,-0.25748) bounces=3
energy: 105
momentum: (-32.0007,8.0142,10)


time of events: 1369.65
reflecting xup
xdown m=10 r=10 p=(1265.43,60.0745,0) v=(-2.10007,-0.0985803,0) bounces=3
xup m=20 r=10 p=(-1982.62,171.172,0) v=(1.5335,-0.131445,0) bounces=3
ydown m=30 r=10 p=(385.138,1560.04,37.444) v=(0.3,1.20417,0.0291667) bounces=4
yup m=40 r=10 p=(342.345,-1484.32,53.2536) v=(0.266667,-1.14519,0.0414815) bounces=4
zdown m=50 r=10 p=(0,202.62,593.456) v=(0,0.157879,0.458291) bounces=3
zup m=60 r=10 p=(0,173.832,-337.163) v=(0,0.135363,-0.25748) bounces=3
energy: 105
momentum: (29.3359,2.71863,10)


time of events: 1677.94
reflecting ydown
xdown m=10 r=10 p=(618.002,29.6833,0) v=(-2.10007,-0.0985803,0) bounces=3
xup m=20 r=10 p=(-1509.86,130.649,0) v=(1.5335,-0.131445,0) bounces=3
ydown m=30 r=10 p=(477.625,1931.27,46.4357) v=(-0.295862,-1.2052,-0.0287643) bounces=5
yup m=40 r=10 p=(424.555,-1837.37,66.0419) v=(0.266667,-1.14519,0.0414815) bounces=4
zdown m=50 r=10 p=(0,251.292,734.742) v=(0,0.157879,0.458291) bounces=3
zup m=60 r=10 p=(0,215.563,-416.541) v=(0,0.135363,-0.25748) bounces=3
energy: 105
momentum: (11.4601,-69.5624,8.26207)

disappear ydown

time of events: 1765.54
reflecting yup
xdown m=10 r=10 p=(434.045,21.0481,0) v=(-2.10007,-0.0985803,0) bounces=3
xup m=20 r=10 p=(-1375.54,119.135,0) v=(1.5335,-0.131445,0) bounces=3
yup m=40 r=10 p=(447.914,-1937.68,69.6755) v=(-0.262976,1.14606,-0.0409074) bounces=5
zdown m=50 r=10 p=(0,265.121,774.886) v=(0,0.157879,0.458291) bounces=3
zup m=60 r=10 p=(0,227.42,-439.095) v=(0,0.135363,-0.25748) bounces=3
energy: 81.887
momentum: (-0.849789,58.2434,5.82944)

disappear yup

time of events: 2918.78
reflecting xdown
xdown m=10 r=10 p=(-1987.84,-92.6389,0) v=(2.10013,0.0971605,0) bounces=4
xup m=20 r=10 p=(392.956,-32.4531,0) v=(1.5335,-0.131445,0) bounces=3
zdown m=50 r=10 p=(0,447.194,1303.41) v=(0,0.157879,0.458291) bounces=3
zup m=60 r=10 p=(0,383.527,-736.032) v=(0,0.135363,-0.25748) bounces=3
energy: 54.2014
momentum: (51.6713,14.3584,7.46574)


time of events: 3955.54
reflecting xup
xdown m=10 r=10 p=(189.505,8.09385,0) v=(2.10013,0.0971605,0) bounces=4
xup m=20 r=10 p=(1982.83,-168.731,0) v=(-1.53366,0.129557,0) bounces=4
zdown m=50 r=10 p=(0,610.878,1778.55) v=(0,0.157879,0.458291) bounces=3
zup m=60 r=10 p=(0,523.867,-1002.98) v=(0,0.135363,-0.25748) bounces=3
energy: 54.2014
momentum: (-9.67181,19.5785,7.46574)


time of events: 4181.38
reflecting zdown
xdown m=10 r=10 p=(663.793,30.0363,0) v=(2.10013,0.0971605,0) bounces=4
xup m=20 r=10 p=(1636.48,-139.472,0) v=(-1.53366,0.129557,0) bounces=4
zdown m=50 r=10 p=(0,646.533,1882.05) v=(0,-0.157085,-0.458563) bounces=4
zup m=60 r=10 p=(0,554.437,-1061.13) v=(0,0.135363,-0.25748) bounces=3
energy: 54.2014
momentum: (-9.67181,3.8303,-38.377)


time of events: 4811.87
reflecting xdown
xdown m=10 r=10 p=(1987.9,91.295,0) v=(-2.1002,-0.0957407,0) bounces=5
xup m=20 r=10 p=(669.523,-57.788,0) v=(-1.53366,0.129557,0) bounces=4
zdown m=50 r=10 p=(0,547.493,1592.93) v=(0,-0.157085,-0.458563) bounces=4
zup m=60 r=10 p=(0,639.782,-1223.46) v=(0,0.135363,-0.25748) bounces=3
energy: 54.2014
momentum: (-51.6751,1.90128,-38.377)

disappear xdown

time of events: 6541.44
reflecting xup
xup m=20 r=10 p=(-1983.04,166.29,0) v=(1.53382,-0.127669,0) bounces=5
zdown m=50 r=10 p=(0,275.804,799.81) v=(0,-0.157085,-0.458563) bounces=4
zup m=60 r=10 p=(0,873.901,-1668.79) v=(0,0.135363,-0.25748) bounces=3
energy: 32.1014
momentum: (30.6763,-2.28582,-38.377)

disappear xup

time of events: 6906.64
reflecting zup
zdown m=50 r=10 p=(0,218.437,632.343) v=(0,-0.157085,-0.458563) bounces=4
zup m=60 r=10 p=(0,923.336,-1762.82) v=(0,-0.134579,0.257891) bounces=4
energy: 8.41247
momentum: (0,-15.929,-7.45473)


time of events: 12392.3
reflecting zdown
zdown m=50 r=10 p=(0,-643.271,-1883.16) v=(0,0.15629,0.458835) bounces=5
zup m=60 r=10 p=(0,185.088,-348.134) v=(0,-0.134579,0.257891) bounces=4
energy: 8.41247
momentum: (0,-0.260216,38.4152)

disappear zdown

time of events: 20588.6
reflecting zup
zup m=60 r=10 p=(0,-917.965,1765.63) v=(0,0.133793,-0.258299) bounces=5
energy: 2.53857
momentum: (0,8.02757,-15.498)

disappear zup
```
I appologize for there is no visualization, hope someone can figure it out. And I'm so sorry that my code isn't pretty.

This programm should not be hard, but the math and logic can be tricky sometimes, needs to be very cautious. It's really really interesting to straighten up a mess and finally get the results, enjoy it.
