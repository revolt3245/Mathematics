import matplotlib.pyplot as plt
import math as m

fig = plt.figure(figsize = (12, 6))
fig.suptitle("Motion on the Circular plate", fontsize = 16)

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.set_xlim(left = -10, right = 10)
ax1.set_ylim(bottom = -10, top = 10)
ax2.set_xlim(left = -10, right = 10)
ax2.set_ylim(bottom = -10, top = 10)

ax1.title.set_text("observe on the circular plate")
ax2.title.set_text("observe outside of the circular plate")

T = [0]

#initial Value
r = [0.1]
phi = [0]
dr = [3]
dphi = [m.pi]

Cx = []
Cy = []

#Drawing Circular Plate
for i in range(1000):
    Cx.append(3*m.cos(m.pi*i/500))
    Cy.append(3*m.sin(m.pi*i/500))
    
ax1.plot(Cx, Cy)
ax2.plot(Cx, Cy)
    
j = 0

#solving Equation(It can be derived by Lagrangian)
for i in range(2000):
    T.append(T[i]+1/1000)
    '''
    r이 3보다 작을 때는 회전하는 원판 위에서 운동하고 있으므로 입자의 에너지 중 회전운동성분은 (m(rphi'+rw)^2)/2가 된다.
    r이 3보다 클 경우는 외부 계에서의 회전 성분은 없으므로 입자의 에너지 중 회전운동성분은 mr^2 *phi^2 /2가 된다.
    다만 여기서 주의할 점은 이 프로그램에서 r과 phi의 기준으로 잡은 것은 계 위에서 운동하고 있는 입자를 중심으로 보았다는 것이다.
    따라서 경계면을 통과하게 되면 각 phi는 회전한 만큼이 더해진 값이 될 것이고, 각속도 dphi는 관성의 법칙에 의해 원판에서의 회전속도가 더해진 형태로 나타나게 될 것이다.
    '''
    if r[i] <= 3:
        r.append(r[i]+dr[i]/1000)
        phi.append(phi[i]+dphi[i]/1000)
        dr.append(dr[i]+(r[i]*((dphi[i]+m.pi/3)**2))/1000)
        dphi.append(dphi[i]+(-2*dr[i]*(dphi[i]+m.pi/3)/r[i])/1000)
        k = m.pi/3*i/1000
        phi_ = phi[i]+k
        dphi_ = dphi[i]+m.pi/3
    else:
        if j == 0 and i != 0:
            phi[i] = phi_
            dphi[i] = dphi_
        r.append(r[i]+dr[i]/1000)
        phi.append(phi[i]+dphi[i]/1000)
        dr.append(dr[i]+(dphi[i]*(r[i]*dphi[i]))/1000)
        dphi.append(dphi[i]+(-dr[i]*(2*r[i]*dphi[i])/(r[i]**2))/1000)
        j += 1

#좌표 이동을 위한 리스트 설정    
X = []
Y = []
Y2 = []
X2 = []
j = 0

for i in T:
    '''
    r이 3보다 작을 경우 판 위에서 보는 입자의 움직임은 위에서 구한 궤적과 같은 형태로 나타나게 될 것이다.
    하지만 3보다 커질 경우 원판 내에서 관측할 때 3보다 큰 영역 전부가 -w의 각속도로 회전하는 것으로 보일 것임을 감안해야 한다.
    r이 3보다 작을 경우 판 밖에서 보는 입자의 움직임은 판 위에서 보는 입자의 움직임에 각속도 w가 더해진 형태로 보이게 될 것이다.
    r이 3보다 클 경우 위에서 구한 식과 유사한 형태가 나타날 것이다.
    
    정리 : 위에서 구한 해 : 3보다 작은 경우 : 원판 위에서 관찰한 원판 위에서의 입자의 운동
                           3보다 큰 경우 : 원판 밖에서 관찰한 원판 밖에서의 입자의 운동
    '''
    if r[j] <= 3:
        X.append(r[j]*m.cos(phi[j]))
        Y.append(r[j]*m.sin(phi[j]))
        X2.append(r[j]*m.cos(phi[j]+m.pi/3*j/1000))
        Y2.append(r[j]*m.sin(phi[j]+m.pi/3*j/1000))
        k = m.pi/3*j/1000
    else:
        X.append(r[j]*m.cos(phi[j]-m.pi/3*j/1000))
        Y.append(r[j]*m.sin(phi[j]-m.pi/3*j/1000))
        X2.append(r[j]*m.cos(phi[j]))
        Y2.append(r[j]*m.sin(phi[j]))
    j += 1
    
ax1.plot(X, Y)
ax2.plot(X2, Y2)