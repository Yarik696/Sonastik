from random import randint
from Sonastik import *
from module1 import *

est = []
rus = []
est = Loe_failist("est.txt")
rus = Loe_failist("rus.txt")
connect(est,rus)
est_to_rus(est,rus)
rus_to_est(est,rus)
mang(est,rus)
