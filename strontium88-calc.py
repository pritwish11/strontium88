import numpy as np
import matplotlib.pyplot as plt
# https://srd.nist.gov/jpcrdreprint/1.3449176.pdf, https://arxiv.org/pdf/2405.18109, https://arxiv.org/pdf/physics/0407021

print("-------------------------------------------------------------------------------")
print("* Welcome to the Strontium Atom Calculator, the name of the class is SR")
print("* To define the initial state, create the atom by writing state1 = SR('level','S','L','J') ")
print("* You can see all the states by SR.srlevel")
print("* You can use TransitionTo(state1), TransitionFrom(state2)")
print("* Use TransitionLinewidth(lower-state,higher-state) and TotalLinewidth(state)")
print("* Find the Polarisability by writing Polarisability(state1, laser_wav(nm))")
print("-------------------------------------------------------------------------------")

h=6.634e-34;
hbar=6.634e-34/(2*np.pi);
c=3e8;
e0=8.85e-12;
e=1.6022e-19;
a0=5.3e-11;
val = 0.5
ms = 1.4597068678e-25;
kb = 1.38e-23

class LASER:
    w0 = 0
    lamL = 0
    P = 0;

    def __init__ (laser, w0, lamL, P):
        LASER.w0 = w0
        LASER.lamL = lamL
        LASER.P = P
        print('The Laser is ready with a Rayleigh Range of: ',1e3*np.pi*(w0**2)/lamL, 'mm')
        I = 2*P*1e3/(np.pi*w0**2)
        E = np.sqrt(I*2*377)
        print('The Peak Electric Field is: ',E, 'V/m')
        print(' ')


class SR:
    s = ''
    l = ''
    j = ''
    lev = ''
    Sval = ''
    Lval = ''
    Jval = ''

    srlevel = np.array([
        "5s5s 0 0 0",    # 0
        "5s5p 0 1 1",    # 1
        "5s5p 1 1 1",    # 2
        "5s6p 0 1 1",    # 3
        "4d5p 0 1 1",    # 4
        "5s4d 1 2 1",    # 5
        "5s4d 1 2 2",    # 6
        "5s6s 1 0 1",    # 7
        "5s5d 1 2 1",    # 8
        "5s5d 1 2 2",    # 9
        "5p5p 1 1 0",    # 10
        "5p5p 1 1 1",    # 11
        "5p5p 1 1 2",    # 12
        "5p5p 0 2 2",    # 13
        "5p5p 0 0 0",    # 14
        "5s7s 1 0 1",    # 15
        "5s4d 0 2 2",    # 16
        "5s5p 1 1 2",    # 17
        "5s7p 0 1 1",    # 18
        "5s8p 0 1 1"     # 19
    ])
    
    data = np.empty([ len(srlevel),len(srlevel) ],dtype=object)

    for i in range(len(srlevel)):
        for j in range(len(srlevel)):
            data[i][j] = np.zeros(2)

    data[0][1] = np.array([460.872, 5.272])   # 5s2 -> 5s5p, S=0
    data[0][2] = np.array([689.465, 0.158])   # 5s2 -> 5s5p, S=1
    data[0][3] = np.array([293.2723, 0.281]) # 5s2 -> 5s6p
    data[0][4] = np.array([242.8835, 0.517]) # 5s2 -> 4d5p
    data[0][19] = np.array([235.4, 0.340])

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

    data[16][1] = np.array([6456, 1.23])
    data[16][3] = np.array([716.7, 1.305])
    data[16][18] = np.array([532.9, 1.125])
    data[16][19] = np.array([448, 0.917])

    data[2][16] = np.array([1800, 0.190])

    data[17][16] = np.array([1900, 0.145])

    for i in range(len(srlevel)):
        for j in range(len(srlevel)):
            data[i][j] = data[i][j] + np.matmul( data[j][i] , np.array([ [-1,0],[0,1] ])  )


    def __init__(sr88,level,s,l,j):
        sr88.level = level
        sr88.s = s
        sr88.l = l
        sr88.j = j

# To find the index of the state from a defined object
    def ind(sr88):
        for i in range(len(SR.srlevel)):
            if (SR.srlevel[i]==sr88.level+' '+sr88.s+' '+sr88.l+' '+sr88.j):
                val = i
                break;

        return val

    def TransitionLinewidth(sr88,level2):
        L = int(sr88.l)
        S = int(sr88.s)
        J = int(sr88.j)

        Lp = int(level2.l)
        Sp = int(level2.s)
        Jp = int(level2.j)

        lam = SR.data[SR.ind(sr88)][SR.ind(level2)][0]
        d = SR.data[SR.ind(sr88)][SR.ind(level2)][1]
        d = d*e*a0
        d_ren = d/np.sqrt(2*J + 1)
        omega= 2*np.pi*c*1e9/lam;
        J_fac = (2*J + 1)/(2*Jp + 1)
        return ((omega**3)*J_fac*1e-6*(d_ren)**2/(6*(np.pi**2)*e0*hbar*c**3 ) );

    def TotalLinewidth(sr88):
        gamma = 0
        for i in range(len(SR.srlevel)):
            if SR.data[i][SR.ind(sr88)][0] > 0 :
                lev = SR.srlevel[i][0:4]
                Sval = SR.srlevel[i][5]
                Lval = SR.srlevel[i][7]
                Jval = SR.srlevel[i][9]
                gamma = gamma + SR.TransitionLinewidth(SR(lev,Sval,Lval,Jval),sr88 )
        return gamma
    
    def TransitionFrom(sr88):
        for i in range(len(SR.srlevel)):
            if SR.data[SR.ind(sr88)][i][0] > 0 :
                print('There is a transition to ',SR.srlevel[i])
                print('of ',SR.data[SR.ind(sr88)][i][0],' nm')
                print('with Matrix Element ',SR.data[SR.ind(sr88)][i][1])
                print(' ')
        
    def TransitionTo(sr88):
        for i in range(len(SR.srlevel)):
            if SR.data[SR.ind(sr88)][i][0] < 0 :
                print('There is a transition from ',SR.srlevel[i])
                print('of ',SR.data[i][SR.ind(sr88)][0],' nm')
                print('with Matrix Element ',SR.data[i][SR.ind(sr88)][1])
                print(' ')

    def Polarisability(sr88, lamL):
        alpha = 0
        for i in range(len(SR.srlevel)):
            if SR.data[SR.ind(sr88)][i][1] != 0:
                fl = c/lamL
                f = np.abs( c/SR.data[SR.ind(sr88)][i][0] )
                d = SR.data[SR.ind(sr88)][i][1]
                alpha = alpha + 2*f*(d**2)/( f**2 - fl**2 )

        return (alpha*1e-9*(8.748**2)*1e-60/h)

    def MOT (sr88,state2,laser):
        k = 1e9*2*np.pi/laser.lamL
        vc = 1e6*SR.TotalLinewidth(sr88)/k
        Tc = ms*(vc**2)/kb
        print('Capture Velocity is: ',vc,' m/s')
        print('Capture Energy is: ',1e3*Tc,' mK')

        I = 2*1e3*laser.P/(np.pi*laser.w0**2)
        E = np.sqrt(I*2*377)
        d = e*a0*SR.data[SR.ind(sr88)][SR.ind(state2)][1]
        s0 = 1e-12*( 2*E*d/SR.TotalLinewidth(sr88) )**2
        Td = 0.5*hbar*1e6*SR.TotalLinewidth(sr88)*np.sqrt(1 + s0)/kb

        print('The value of s0 is: ',s0)
        print('The Achievable Doppler Temperature is: ',1e3*Td,' mK')
        print('The optimal Red Detuning is: ',0.5*SR.TotalLinewidth(sr88)*np.sqrt(1 + s0), ' MHz')

        det = 2*np.pi*c*1e-6*1e9*(1/(laser.lamL) - 1/(SR.data[SR.ind(sr88)][SR.ind(state2)][0]) )
        print('Your laser detuning is: ', det, ' MHz')
        #Tcool = ( 1/(16*1e6*det*kb) )*hbar*1e12*( 1 + s0 + 4*(det**2)/SR.TotalLinewidth(sr88)**2 )*SR.TotalLinewidth(sr88)**2
        
    def DipoleTrap(sr88,state2,laser):
        I = 2*1e3*laser.P/(np.pi*laser.w0**2)
        E = np.sqrt(I*2*377)
        d = e*a0*SR.data[SR.ind(sr88)][SR.ind(state2)][1]
        rabi = E*d/hbar
        det = 2*np.pi*c*1e-6*1e9*(1/(laser.lamL) - 1/(SR.data[SR.ind(sr88)][SR.ind(state2)][0]) )
        U = -1*hbar*(rabi**2)/(4*det*kb)
        wTrapx = np.sqrt( -1*(1e6*(d*E)**2)/(2*ms*det*hbar*laser.w0**2) )
        zr = np.pi*(1e3*laser.w0**2)/(laser.lamL)
        wTrapz = np.sqrt( -1*((d*E)**2)/(4*ms*det*hbar*zr**2) )
        print('The depth is: ', 1e3*U, ' mK')
        print('Trap Frequency along beam direction is: ', wTrapz, ' Hz')
        print('Trap Frequency along the transverse direction is : ', wTrapx, ' Hz')
        
        
