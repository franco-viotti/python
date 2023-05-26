from math import sqrt

def Q_func(val):
  return 0.5-0.5*sp.erf(val/sqrt(2))

def Q_func_inv(val):
  return 1/Q_func(val)

def get_fap(N, pf_fix, var):  # false alarm probability, var = varianza
  return (sqrt(2/N)*(1/erfc(2*pf_fix)) + 1) * N*var

def get_mdp(N, pm_fix, var):  # miss detection probability
  lm = 0
  for sigma_p in range(-30, -8, 2):
    lm = N*var * (sqrt(2/N)*(1+sigma_p)*(1/erfc(2*(1-pm_fix))+(1+sigma_p)))
  return lm 

def get_ep(N, var):   # error probability
  le = 0
  for sigma_p in range(-30, -8, 2):
    le = (N*var/2) * (1 + sqrt(1 + (2*(2+sigma_p)*ln(1+sigma_p))/(N*sigma_p))) * ((1+sigma_p)/(1+sigma_p/2))  
  return le
  
get_ep(20, 0.2)
