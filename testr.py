from rpy2.robjects.packages import importr
base = importr('base')
print(base.R_home())
