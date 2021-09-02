import math
import numpy as np
def unitvec(v):
    return v / np.linalg.norm(v)

surfaceNormal = np.array([0.0, 1.0, 0.0])
vertexPosition = np.array([3.0, 4.0, 0.0])
viewer = np.array([7,7,0])
v_unit = unitvec(viewer - vertexPosition)
# Estructura de la formula
# ()
ambientReflection = 1.0 
diffuseReflection = 0.5
specularReflection = 0.5
lightAmbient = 0.01
ambientColor = np.array([0.0, 0.0, 0.1])
diffuseColor = np.array([0.0, 0.0, 1.0])
specularColor = np.array([0.0, 0.0, 0.5])
lightPosition = np.array([1.0, 7.0, 0.0])
lightIntensity = np.array([3.0, 4.0, 0.0])

alpha = 100
# function to get unit vector

N = surfaceNormal
# Sacar vector de la delta de la intensidad y posicion de la luz 
L = unitvec(lightPosition - lightIntensity) 
NL = max(np.dot(unitvec(N), L), 0.0)
Lp = N * (np.dot(N, L))
Lo = L - Lp
r = unitvec(Lp - Lo)
vr = np.dot(r, v_unit)
specularTerm = math.pow(vr, alpha)

color = diffuseColor * NL + (specularColor * specularTerm) + (ambientColor * lightAmbient)
print(color)