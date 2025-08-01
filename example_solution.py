import sympy as sym
from library import *

x, q, F, EI = sym.symbols('x, q, F, EI')
C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12 = sym.symbols('C1 C2 C3 C4 C5 C6 C7 C8 C9 C10 C11 C12')

q_AC = q
q_CD = 0
q_DB = 0

V_AC = sym.integrate(-q_AC,x)+C1
M_AC = sym.integrate(V_AC,x)+C2
kappa_AC = M_AC / EI
phi_AC = sym.integrate(kappa_AC,x)+C3
w_AC = sym.integrate(-phi_AC,x)+C4

V_CD = sym.integrate(-q_CD,x)+C5
M_CD = sym.integrate(V_CD,x)+C6
kappa_CD = M_CD / EI
phi_CD = sym.integrate(kappa_CD,x)+C7
w_CD = sym.integrate(-phi_CD,x)+C8

V_DB = sym.integrate(-q_DB,x)+C9
M_DB = sym.integrate(V_DB,x)+C10
kappa_DB = M_DB / EI
phi_DB = sym.integrate(kappa_DB,x)+C11
w_DB = sym.integrate(-phi_DB,x)+C12

print(w_AC)
display(w_AC)
display(w_DB)
