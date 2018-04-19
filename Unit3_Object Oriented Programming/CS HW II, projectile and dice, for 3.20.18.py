from projectile import Projectile


def getInputs():
    a = input("Enter the launch angle (in degrees): ")
    v = input("Enter the initial velocity (in meters/sec): ")
    h = input("Enter the initial height (in meters): ")
    t = input("Enter the time interval between position calculations: ")
    return a,v,h,t

def main():
  #  angle = input("Enter the launch angle (in degrees): ")
  #  vel = input("Enter the initial velocity (in meters/sec): ")
  #  h0 = input("Enter the initial height (in meters): ")
  #  time = input("Enter the time interval between position calculations: ")
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        print(cball.getY(), cball.getX())
        cball.update(time)

    print("\nDistance traveled: %0.1f meters." % (cball.getX()))

main()
