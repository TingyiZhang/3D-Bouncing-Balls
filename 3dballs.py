import sys
import math

inf = float("inf")

class ball():
  def __init__(self, x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0, m = 0, r = 0, n = None):
    self.x = x
    self.y = y
    self.z = z
    self.m = m
    self.r = r
    self.vx = vx
    self.vy = vy
    self.vz = vz
    self.name = n
    self.life = 0
    self.hit = {} # a dictionary to store when the collision happens and objects to collidd with 

  def __repr__(self):
    return "({:g})".format([self.x,self.y,self.z,self.vx,self.vy,self.vz,self.name])

  def hit_with_ball(a, b):
    if a != b: 
      x = a.x - b.x
      y = a.y - b.y
      z = a.z - b.z
      vx = a.vx - b.vx
      vy = a.vy - b.vy
      vz = a.vz - b.vz
      r = a.r + b.r
      delta = (2*(vx*x+vy*y+vz*z))**2 - (4*(vx**2+vy**2+vz**2)*((x**2+y**2+z**2)-r**2))
      if x*vx + y*vy + z*vz < 0 and delta >= 0: #whether they are approaching each other
        r1 = ((-2*(vx*x+vy*y+vz*z))+math.sqrt(delta)) / (2*(vx**2+vy**2+vz**2))
        r2 = ((-2*(vx*x+vy*y+vz*z))-math.sqrt(delta)) / (2*(vx**2+vy**2+vz**2))
        if r1 >= 0 and r2 >= 0:
          t = r1 if r1 < r2 else r2
        elif r1 >= 0 and r2 < 0:
          t = r1
        elif r1 < 0 and r2 >= 0:
          t = r2
        else:
          t = inf
      else:
        t = inf

      if a.life > 0:
        if t in a.hit:
          a.hit[t].append(b)
        else:
          a.hit.update({t : [b]})
      return t
    else:
      return inf


  def hit_with_wall(a, wall):
    spot = hit_ball(wall)
    x = a.x
    y = a.y
    z = a.z
    vx = a.vx
    vy = a.vy
    vz = a.vz
    r = wall.r - a.r
    delta = (2*(vx*x+vy*y+vz*z))**2 - (4*(vx**2+vy**2+vz**2)*((x**2+y**2+z**2)-r**2))
    if vx!=0 or vy!=0 or vz!=0:
      r1 = ((-2*(vx*x+vy*y+vz*z))+math.sqrt(delta)) / (2*(vx**2+vy**2+vz**2))
      r2 = ((-2*(vx*x+vy*y+vz*z))-math.sqrt(delta)) / (2*(vx**2+vy**2+vz**2))
      if round(math.sqrt((x**2)+(y**2)+(z**2))+a.r, 10) == wall.r:
        if r1 >r2:
          t = r1
        else:
          t = r2
      else:
        if r1 > 0 and r2 > 0: #t should always larger than 0 of the ball gonna keep reflecting the wall
          if r1 <= r2:
            t = r1
          else:
            t = r2
        elif r1 > 0 or r2 > 0:
          if r1 > 0:
             t = r1
          else:
            t = r2
        else:
            t = inf
    else:
      t = inf
    # store the spot on the wall where the ball hits
    spot.x = hit_spot(a, t, wall.r)[0]
    spot.y = hit_spot(a, t, wall.r)[1]
    spot.z = hit_spot(a, t, wall.r)[2]

    if a.life > 0:
      if t in a.hit:        
        a.hit[t].append(spot)
      else:
        a.hit.update({t : [spot]})

    return t

  def update_position(a, t):
    a.x = a.x + a.vx * t
    a.y = a.y + a.vy * t
    a.z = a.z + a.vz * t

  def update_v(a, b, t):
    x = a.x - b.x
    y = a.y - b.y
    z = a.z - b.z
    vx = a.vx - b.vx
    vy = a.vy - b.vy
    vz = a.vz - b.vz
    for ball in a.hit[t]:
      if ball.m == inf:
        hitwall = 1 
      else:
        hitwall = 0

    if b.m == inf and hitwall == 1: #ball hits with wall
      for ball in a.hit[t]:
        if ball.m == inf:
          spot = ball
      x = a.x - spot.x
      y = a.y - spot.y
      z = a.z - spot.z
      vx = a.vx - spot.vx
      vy = a.vy - spot.vy
      vz = a.vz - spot.vz
      m1 = a.m
      m2 = spot.m
      a.vx = a.vx - 2*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))*x
      a.vy = a.vy - 2*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))*y
      a.vz = a.vz - 2*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))*z
      a.life = a.life - 1
      return True
    elif b in a.hit[t] and a.life > 0 and b.life > 0 and (x*vx) + (y*vy) + (z*vz) < 0: # ball hits with other ball
          x = a.x - b.x
          y = a.y - b.y
          z = a.z - b.z
          vx = a.vx - b.vx
          vy = a.vy - b.vy
          vz = a.vz - b.vz
          m1 = a.m
          m2 = b.m
          a.vx = a.vx - (((2*m2) / (m1+m2))*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))) * x
          a.vy = a.vy - (((2*m2) / (m1+m2))*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))) * y
          a.vz = a.vz - (((2*m2) / (m1+m2))*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))) * z
          b.vx = b.vx + (((2*m1) / (m1+m2))*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))) * x
          b.vy = b.vy + (((2*m1) / (m1+m2))*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))) * y
          b.vz = b.vz + (((2*m1) / (m1+m2))*((vx*x+vy*y+vz*z)/(x**2+y**2+z**2))) * z
          a.life = a.life - 1 
          b.life = b.life - 1 
          return True
    else:
        return False

def hit_ball(a): # make a copy of a colliding object
  hit = ball()
  hit.x = a.x
  hit.y = a.y
  hit.z = a.z
  hit.vx = a.vx
  hit.vy = a.vy
  hit.vz = a.vz
  hit.m = a.m
  hit.r = a.r
  hit.name = a.name
  hit.life = a.life
  hit.life = a.life
  return hit

def hit_spot(s, t, r): # make a copy of the spot where the ball hits the wall
  x = s.x + s.vx * t
  y = s.y + s.vy * t
  z = s.z + s.vz * t
  if x == 0 and y != 0 and z != 0:
    a = 0
    b = r / (math.sqrt(1 + (z / y) ** 2)) 
    c = (b * z) / y
  elif y == 0 and x != 0 and z != 0:
    b = 0
    a = r / (math.sqrt(1 + (z / x) ** 2))
    c = (a * z) / x
  elif z == 0 and x != 0 and y != 0:
    c = 0
    a = r / (math.sqrt(1 + (y / x) ** 2))
    b = (a * y) / x
  elif x == 0 and y == 0 and z != 0:
    a = 0
    b = 0
    c = z + s.r
  elif y == 0 and z == 0 and x != 0:
    a = x + s.r
    b = 0
    c = 0
  elif x == 0 and z == 0 and y != 0:
    a = 0
    b = y + s.r
    c = 0
  else: 
    a = r / (math.sqrt(1 + ((y / x)**2) + ((z / x)**2)))
    b = (y * a) / x
    c = (z * a) / x
  return [a,b,c]

def energy(balls):
  energy = 0
  for ball in balls:
    energy += 0.5 * ball.m * ((ball.vx**2) + (ball.vy**2) + (ball.vz**2))
  return energy

def momentum(balls):
  mx = 0
  my = 0
  mz = 0
  for ball in balls:
    mx += ball.m * ball.vx
    my += ball.m * ball.vy
    mz += ball.m * ball.vz
  return [mx, my, mz]

def run(balls, wall):
  life = float(sys.argv[2])
  time = [] # array to store every posible collision timing
  real_time = 0 # the track of time
  temp =[]

  print("Here are the initial conditions.")
  print("universe radius", wall.r)
  print("max collisions", life)

  for ball in balls:
    print(ball.name,"m={:g} r={:g} p=({:g},{:g},{:g}) v=({:g},{:g},{:g}) bounces={:g}".format(ball.m, ball.r,ball.x,ball.y,ball.z,ball.vx,ball.vy,ball.vz,life - ball.life))
  print("energy: {:g}".format(energy(balls)))
  print("momentum: ({:g},{:g},{:g})".format(momentum(balls)[0],momentum(balls)[1],momentum(balls)[2]))

  print("\nHere are the events.\n")
  while (balls and energy(balls) > 0): #if there are balls still have lives and balls are still moving
    # predict every possible events: every pairs of balls and balls with wall
    for ball in balls:
      time.append(ball.hit_with_wall(wall))
    for i in range(len(balls)):
      for j in range(len(balls)):
        time.append(balls[i].hit_with_ball(balls[j]))

    if real_time == 0: # assume that no collisions happen when time = 0
      for t in time:
        if t == 0:
          time.remove(t)

    time = sorted(time) # finding the minimum collision time

    real_time += time[0]
    for ball in balls: # once got the time, update all balls' position first
      ball.update_position(time[0])

    collision = [] # array to store balls that collides at this time
    for ball in balls:
      if time[0] in ball.hit:
        collision.append(ball)

    collision.append(wall)

    # print out the report of ball-hit-ball events at that time
    for i in range(len(collision) - 1):
      for j in range(len(collision) - 1):
        if j > i:
          if collision[i].update_v(collision[j], time[0]):
            print("time of events: {:g}".format(real_time))
            print("colliding", collision[i].name,collision[j].name)
            for ball in balls:
              print(ball.name,"m={:g} r={:g} p=({:g},{:g},{:g}) v=({:g},{:g},{:g}) bounces={:g}".format(ball.m, ball.r,ball.x,ball.y,ball.z,ball.vx,ball.vy,ball.vz,life - ball.life))
            print("energy: {:g}".format(energy(balls)))
            print("momentum: ({:g},{:g},{:g})".format(momentum(balls)[0],momentum(balls)[1],momentum(balls)[2]))
            print()
            for ball in balls:
              if ball.life == 0:
                print("disappear", ball.name)
                print("")

      j = len(collision) - 1 
      if collision[i].update_v(collision[j], time[0]): #print out the report of ball-hit-wall at that time
          print("time of events: {:g}".format(real_time))
          print("reflecting", collision[i].name)
          for ball in balls:
            print(ball.name,"m={:g} r={:g} p=({:g},{:g},{:g}) v=({:g},{:g},{:g}) bounces={:g}".format(ball.m, ball.r,ball.x,ball.y,ball.z,ball.vx,ball.vy,ball.vz,life - ball.life))
          print("energy: {:g}".format(energy(balls)))
          print("momentum: ({:g},{:g},{:g})".format(momentum(balls)[0],momentum(balls)[1],momentum(balls)[2]))
          print()
          for ball in balls:
            if ball.life == 0:
              print("disappear", ball.name)
              print("")

    collision.remove(wall)

    new_balls = []
    for ball in balls:
      if ball.life > 0:
        new_balls.append(ball)

    balls = new_balls

    for ball in balls: #clear all the events that record in the ball
      ball.hit.clear()

    time = [] # empty the time records for this states

  sys.exit(0)

    
def the_big_bang(): # initialize the universe
  life = float(sys.argv[2])
  objects = []
  n = []
  balls = []
    
  a = [x.strip() for x in sys.stdin.readlines()]

  for i in range(len(a)):
    objects.append([x for x in a[i].split()])
  #check if the input format is right
  for obj in objects:
    if len(obj) != 9:
      sys.exit(1)

  for i in range(len(objects)):
    n.append(objects[i][-1])
    objects[i].pop()
  #check if there are invalid numbers in input
  for obj in objects:
    for i in range(len(obj)):
      try:
        float(obj[i])
      except:
        sys.exit(1)

  for i in range(len(objects)):
    objects[i] = [float(x) for x in objects[i]]

  for i in range(len(objects)):
    objects[i].append(n[i])

  for i in range(len(objects)):
    new = ball(objects[i][2],objects[i][3],objects[i][4],objects[i][5],objects[i][6],objects[i][7],objects[i][0],objects[i][1],objects[i][8])
    new.life = life
    balls.append(new)

  return balls


if __name__=="__main__":
  #check the format of arguments from the command line
  if len(sys.argv) != 3: 
    sys.exit(1)

  #check if the argument can convert to a float
  for arg in sys.argv[1:]:
    try:
      float(arg)
    except:
      sys.exit(1) 

  wall = ball(0,0,0,0,0,0,inf,float(sys.argv[1]),"universe")
  wall.life = inf
  balls = []

  balls = the_big_bang()

  run(balls, wall)












