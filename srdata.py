import numpy as np
import matplotlib.pyplot as plt
# https://srd.nist.gov/jpcrdreprint/1.3449176.pdf, https://arxiv.org/pdf/2405.18109, https://arxiv.org/pdf/physics/0407021

h=6.634e-34;
hbar=6.634e-34/(2*np.pi);
c=3e8;
e0=8.85e-12;
e=1.6022e-19;
a0=5.3e-11;
val = 0.5
ms = 1.4597068678e-25;
kb = 1.38e-23


srlevel = np.array([
    "5s5s 0 0 0",    # 0 5s2 1S0
    "5s5p 0 1 1",    # 1 5s5p 1P1
    "5s5p 1 1 1",    # 2 5s5p 3P1
    "5s6p 0 1 1",    # 3 5s6p 1P1
    "4d5p 0 1 1",    # 4 4d5p 1P1
    "5s4d 1 2 1",    # 5 5s4d 3D1
    "5s4d 1 2 2",    # 6 5s4d 3D2
    "5s6s 1 0 1",    # 7 5s6s 3S1
    "5s5d 1 2 1",    # 8 5s5d 3D1
    "5s5d 1 2 2",    # 9 5s5d 3D2
    "5p5p 1 1 0",    # 10 5p2 3P0
    "5p5p 1 1 1",    # 11 5p2 3P1
    "5p5p 1 1 2",    # 12 5p2 3P2
    "5p5p 0 2 2",    # 13 5p2 1D2
    "5p5p 0 0 0",    # 14 5p2 1S0
    "5s7s 1 0 1",    # 15 5s7s 3S1
    "5s4d 0 2 2",    # 16 5s4d 1D2
    "5s5p 1 1 2",    # 17 5s5p 3P2
    "5s7p 0 1 1",    # 18 5s7p 1P1
    "5s8p 0 1 1",    # 19 5s8p 1P1
    "5s5p 1 1 0",    # 20 5s5p 3P0
    "5s6d 1 2 1",    # 21 5s6d 3D1
    "5s8s 1 1 1",    # 22 5s8s 3P1
    "5s7d 1 2 1",    # 23 5s7d 3D1
    "5s9s 1 0 1",    # 24 5s9s 3S1
    "5s8d 1 2 1"     # 25 5s8d 3D1
])

data = np.empty([ len(srlevel),len(srlevel) ],dtype=object)

for i in range(len(srlevel)):
    for j in range(len(srlevel)):
        data[i][j] = np.zeros(2)

# Transitions for 5s2 1S0
data[0][1] = np.array([460.872, 5.272])   # 5s2 -> 5s5p, S=0
data[0][2] = np.array([689.465, 0.158])   # 5s2 -> 5s5p, S=1
data[0][3] = np.array([293.2723, 0.281]) # 5s2 -> 5s6p
data[0][4] = np.array([242.8835, 0.517]) # 5s2 -> 4d5p
data[0][19] = np.array([235.4, 0.340])

# Transitions for 5s5p 1P1
data[1][5] = np.array([2735.98, 2.318])  # 5s5p, S=1 -> 5s4d, J=1
data[1][6] = np.array([2692.515, 4.013]) # 5s5p, S=1 -> 5s4d, J=2
data[1][7] = np.array([688.042, 3.435])  # 5s5p, S=1 -> 5s6s
data[1][8] = np.array([487.7335, 2.005]) # 5s5p, S=1 -> 5s5d, J=1
data[1][9] = np.array([487.377, 3.671])  # 5s5p, S=1 -> 5s5d, J=2
data[1][10] = np.array([483.349, 2.658]) # 5s5p, S=1 -> 5p2, J=0
data[1][11] = np.array([478.5605, 2.363])# 5s5p, S=1 -> 5p2, J=1
data[1][12] = np.array([472.367, 2.867]) # 5s5p, S=1 -> 5p2, J=2
data[1][13] = np.array([445.2955, 0.228])# 5s5p, S=1 -> 5p2, S=0, L=2
data[1][14] = np.array([441.384, 0.291]) # 5s5p, S=1 -> 5p2, S=0, L=0
data[1][15] = np.array([436.3, 0.921])   # 5s5p, S=1 -> 5s7s

#Transitions for 5s4d 1D2
data[16][1] = np.array([6456, 1.23])
data[16][3] = np.array([716.7, 1.305])
data[16][18] = np.array([532.9, 1.125])
data[16][19] = np.array([448, 0.917])
data[2][16] = np.array([1800, 0.190])
data[17][16] = np.array([1900, 0.145])

#Transitions for 5s5p 3P0
data[20][5] = np.array([2642.4,2.714])
data[20][7] = np.array([682,1.972])
data[20][8] = np.array([484.2,2.458])
data[20][11] = np.array([471.5,2.627])
data[20][15] = np.array([433.3,0.522])
data[20][21] = np.array([394.3,1.175])
data[20][22] = np.array([377.1,0.302])
data[20][23] = np.array([361.4,0.822])
data[20][24] = np.array([348.4,0.270])
data[20][25] = np.array([336.7,0.820])

for i in range(len(srlevel)):
    for j in range(len(srlevel)):
        data[i][j] = data[i][j] + np.matmul( data[j][i] , np.array([ [-1,0],[0,1] ])  )

        
        
