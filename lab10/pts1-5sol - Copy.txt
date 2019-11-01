GlowScript 2.6 VPython
scene.width = 1000
pmass=6e24
prad=3e6
smass=1.5e4
g=6.673e-11
fgarrowscale=7e4

planet=sphere(pos=vec(0,-2e7,0), radius=6e6, color=color.red)

i=0
inc=6.5e7
while i<5:
  rate(2)
  ship=sphere(pos=vec(-13e7+i*inc,4.5e7,0), radius=prad, color=color.cyan)
  rhat=(ship.pos-planet.pos)/mag(ship.pos-planet.pos)
  fg=-g*pmass*smass*rhat/mag(ship.pos-planet.pos)**2
  print(fg)
  fgarrow=arrow(pos=ship.pos, axis=fgarrowscale*fg,shaftwidth=prad/2.0)
  fgarrowp=arrow(pos=planet.pos, axis=-fgarrowscale*fg,shaftwidth=prad/2.0,color=color.magenta)
  i=i+1