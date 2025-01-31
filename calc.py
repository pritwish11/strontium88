import srdata
import numpy as np
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

    def __init__(sr88,level,s,l,j):
        sr88.level = level
        sr88.s = s
        sr88.l = l
        sr88.j = j

# To find the index of the state from a defined object
    def ind(sr88):
        for i in range(len(srdata.srlevel)):
            if (srdata.srlevel[i]==sr88.level+' '+sr88.s+' '+sr88.l+' '+sr88.j):
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

        lam = srdata.data[SR.ind(sr88)][SR.ind(level2)][0]
        d = srdata.data[SR.ind(sr88)][SR.ind(level2)][1]
        d = d*e*a0
        d_ren = d/np.sqrt(2*J + 1)
        omega= 2*np.pi*c*1e9/lam;
        J_fac = (2*J + 1)/(2*Jp + 1)
        return ((omega**3)*J_fac*1e-6*(d_ren)**2/(6*(np.pi**2)*e0*hbar*c**3 ) );

    def TotalLinewidth(sr88):
        gamma = 0
        for i in range(len(srdata.srlevel)):
            if srdata.data[i][SR.ind(sr88)][0] > 0 :
                lev = srdata.srlevel[i][0:4]
                Sval = srdata.srlevel[i][5]
                Lval = srdata.srlevel[i][7]
                Jval = srdata.srlevel[i][9]
                gamma = gamma + SR.TransitionLinewidth(SR(lev,Sval,Lval,Jval),sr88 )
        return gamma
    
    def TransitionFrom(sr88):
        for i in range(len(srdata.srlevel)):
            if srdata.data[SR.ind(sr88)][i][0] > 0 :
                print('There is a transition to ',srdata.srlevel[i])
                print('of ',srdata.data[SR.ind(sr88)][i][0],' nm')
                print('with Matrix Element ',srdata.data[SR.ind(sr88)][i][1])
                print(' ')
        
    def TransitionTo(sr88):
        for i in range(len(srdata.srlevel)):
            if srdata.data[SR.ind(sr88)][i][0] < 0 :
                print('There is a transition from ',srdata.srlevel[i])
                print('of ',srdata.data[i][SR.ind(sr88)][0],' nm')
                print('with Matrix Element ',srdata.data[i][SR.ind(sr88)][1])
                print(' ')

    def Polarisability(sr88, lamL):
        alpha = 0
        j_state = int(sr88.j)
        for i in range(len(srdata.srlevel)):
            if srdata.data[SR.ind(sr88)][i][1] != 0:
                fl = c/lamL
                f = np.abs( c/srdata.data[SR.ind(sr88)][i][0] )
                d = srdata.data[SR.ind(sr88)][i][1]
                alpha = alpha + (2/3)*(1/(2*j_state + 1))*f*(d**2)/( f**2 - fl**2 )

        return (alpha*1e-9*(8.748**2)*1e-60/h)

    def MOT (sr88,state2,laser):
        k = 1e9*2*np.pi/laser.lamL
        vc = 1e6*SR.TotalLinewidth(sr88)/k
        Tc = ms*(vc**2)/kb
        print('Capture Velocity is: ',vc,' m/s')
        print('Capture Energy is: ',1e3*Tc,' mK')

        I = 2*1e3*laser.P/(np.pi*laser.w0**2)
        E = np.sqrt(I*2*377)
        d = e*a0*srdata.data[SR.ind(sr88)][SR.ind(state2)][1]
        s0 = 1e-12*( 2*E*d/SR.TotalLinewidth(sr88) )**2
        Td = 0.5*hbar*1e6*SR.TotalLinewidth(sr88)*np.sqrt(1 + s0)/kb

        print('The value of s0 is: ',s0)
        print('The Achievable Doppler Temperature is: ',1e3*Td,' mK')
        print('The optimal Red Detuning is: ',0.5*SR.TotalLinewidth(sr88)*np.sqrt(1 + s0), ' MHz')

        det = 2*np.pi*c*1e-6*1e9*(1/(laser.lamL) - 1/(srdata.data[SR.ind(sr88)][SR.ind(state2)][0]) )
        print('Your laser detuning is: ', det, ' MHz')
        #Tcool = ( 1/(16*1e6*det*kb) )*hbar*1e12*( 1 + s0 + 4*(det**2)/SR.TotalLinewidth(sr88)**2 )*SR.TotalLinewidth(sr88)**2
        
    def DipoleTrap(sr88,state2,laser):
        I = 2*1e3*laser.P/(np.pi*laser.w0**2)
        E = np.sqrt(I*2*377)
        d = e*a0*srdata.data[SR.ind(sr88)][SR.ind(state2)][1]
        rabi = E*d/hbar
        det = 2*np.pi*c*1e-6*1e9*(1/(laser.lamL) - 1/(srdata.data[SR.ind(sr88)][SR.ind(state2)][0]) )
        U = -1*hbar*(rabi**2)/(4*det*kb)
        wTrapx = np.sqrt( -1*(1e6*(d*E)**2)/(2*ms*det*hbar*laser.w0**2) )
        zr = np.pi*(1e3*laser.w0**2)/(laser.lamL)
        wTrapz = np.sqrt( -1*((d*E)**2)/(4*ms*det*hbar*zr**2) )
        print('The depth is: ', 1e3*U, ' mK')
        print('Trap Frequency along beam direction is: ', wTrapz, ' Hz')
        print('Trap Frequency along the transverse direction is : ', wTrapx, ' Hz')
        
        
