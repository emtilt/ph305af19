GlowScript 2.6 VPython
scene.width = 800
scene.height = 800

G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
deltat = 60

Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
craft = sphere(pos=vector(-10*Earth.radius, 0,0), radius=1e6,
               color=color.yellow, make_trail=True)
vcraft = vector(0,2e3,0)
pcraft = mcraft*vcraft
t = 0
scene.autoscale = False ##turn off automatic camera zoom

print(pcraft)

sf=2.5e-1
sfg=5e3
parr=arrow(pos=craft.pos,axis=sf*pcraft)
fgarrow=arrow(pos=craft.pos,axis=vector(0,0,0),color=color.red)

while t < 10*365*24*60*60:
    if mag(craft.pos-Earth.pos)<Earth.radius:
      break
    rate(100)
    rhat=(craft.pos-Earth.pos)/mag(craft.pos-Earth.pos)
    fg=-G*mcraft*mEarth*rhat/mag(craft.pos-Earth.pos)**2
    fgarrow.pos=craft.pos
    fgarrow.axis=sfg*fg
    pcraft=pcraft+fg*deltat
    craft.pos = craft.pos + (pcraft/mcraft)*deltat
    
    parr.pos=craft.pos
    parr.axis=pcraft*sf
    t = t+deltat