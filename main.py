from Operation import Operation
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy.special
import scipy.stats as stats


def normal_dist(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density


p1 = {
         'B': 0.999,
         'M': 5.1,
         'D': 0.3
     }
p2 = {
        'B': 0.998,
        'M': 3,
        'D': 0.4
    }
p3 = {
        'B': 0.997,
        'M': 8.5,
        'D': 0.7
    }
p4 = {
        'B': 0.995,
        'M': 1.7,
        'D': 0.1
    }
p5 = {
        'B': 0.989,
        'M': 2.3,
        'D': 0.2
    }
p6 = {
        'B': 0.999,
        'M': 10,
        'D': 1.1
    }
p7 = {
        'B': 0.999,
        'M': 9,
        'D': 0.8
    }
k1 = {
        'K11': 0.99,
        'K00': 0.975,
        'M': 4,
        'D': 0.7
    }
k2 = {
        'K11': 0.995,
        'K00': 0.99,
        'M': 4.5,
        'D': 0.6
    }
k3 = {
        'K11': 0.997,
        'K00': 0.99,
        'M': 5,
        'D': 1
    }
# k1 = {
#         'K11': 1,
#         'K00': 0,
#         'M': 0,
#         'D': 0
#     }
# # k2 = {
#         'K11': 1,
#         'K00': 0,
#         'M': 0,
#         'D': 0
#     }
# k3 = {
#         'K11': 1,
#         'K00': 0,
#         'M': 0,
#         'D': 0
#     }
p = [p1, p2, p3, p4, p5, p6, p7]
k = [k1, k2, k3]
ob = []
op = []
ok = []
for el in p:
    ob.append(Operation('P', el))
    op.append(Operation('P', el))
for el in k:
    ob.append(Operation('K', el))
    ok.append(Operation('K', el))


def plt_for_lab3(x, pdf):
    plt.plot(x, pdf, color='red')
    plt.xlabel('Data points')
    plt.ylabel('Probability Density')


def print_result(o):
    for el in o:
        print(el.to_string())

    x = np.linspace(o[15].get_m(), o[15].get_m() + 2.5*o[15].get_d(), 15)
    fig = plt.figure(tight_layout=True)
    gs = gridspec.GridSpec(1, 2)
    ax = fig.add_subplot(gs[0, 0])
    # pdf = normal_dist(x, o[15].get_m(), np.sqrt(o[15].get_d()))
    x_do = (x - o[15].get_m()) / o[15].get_d()
    # pdf = scipy.special.erf(x_do)
    pdf = stats.norm.cdf(x_do)
    plt_for_lab3(x, pdf)
    print(f'Psv(' + "{:2.3f}".format(x[8]) + f') = {pdf[8]}\nT:')
    for i in x:
        print("{:3.3f}".format(i), end='\t')
    print('\nPcv:')
    for i in range(0, len(pdf)):
        print("{:3.3f}".format(pdf[i]), end='\t')
    print('\nPf:')
    for i in range(0, len(pdf)):
        pdf[i] *= o[15].get_b()
        print("{:3.3f}".format(pdf[i]), end='\t')
    print()
    ax = fig.add_subplot(gs[0, 1])
    plt_for_lab3(x, pdf)
    plt.show()


def lab3():
    o = copy.deepcopy(ob)
    # o.append(Operation('K', k3))
    o.append(Operation('RR', [o[0], o[1]]))  # Pэ1 - 10
    o.append(Operation('RK', {o[10].get_type(): o[10], o[7].get_type(): o[7]}))  # Pэ2 - 11
    o.append(Operation('RKR', {'P1': o[2], 'P2': o[3], 'K': o[8]}))  # Pэ3 - 12
    o.append(Operation('RR', [o[4], o[5], o[6]]))  # Pэ4 - 13
    o.append(Operation('RR', [o[11], o[12]]))  # Pэ5 - 14
    o.append(Operation('RKR', {'P1': o[14], 'P2': o[13], 'K': o[9]}))  # Pэ6 - 15
    # o.append(Operation('RK', {o[16].get_type(): o[16], o[10].get_type(): o[10]})) # Pэ6 - 17

    print_result(o)


def lab41():
    o = copy.deepcopy(ob)
    o.append(Operation('RR', op))  # Pэ1 - 10
    print('with out K')
    for el in o:
        print(el.to_string())


def lab42():
    o = copy.deepcopy(ob)
    o.append(Operation('RR', [op[0], op[1]]))  # Pэ1 - 10
    o.append(Operation('RR', [op[2], op[3], op[4], op[5], op[6]]))  # Pэ1 - 11
    o.append(Operation('RK', {o[10].get_type(): o[10], ok[0].get_type(): ok[0]}))  # Pэ2 - 12
    o.append(Operation('RR', [o[11], o[12]]))  # Pэ1 - 13

    print('\nK1')
    for el in o:
        print(el.to_string())


def lab43():
    o = copy.deepcopy(ob)
    o.append(Operation('RKR', {'P1': op[2], 'P2': op[3], 'K': ok[1]}))  # Pэ3 - 10
    o.append(Operation('RR', [op[0], op[1], o[10], op[4], op[5], op[6]]))  # Pэ1 - 11

    print('\nK2')
    for el in o:
        print(el.to_string())


def lab44():
    o = copy.deepcopy(ob)
    o.append(Operation('RR', [o[0], o[1]]))  # Pэ1 - 10
    o.append(Operation('RK', {o[10].get_type(): o[10], ok[0].get_type(): ok[0]}))  # Pэ2 - 11
    o.append(Operation('RKR', {'P1': op[2], 'P2': op[3], 'K': ok[1]}))  # Pэ3 - 12

    print('\nK3')
    for el in o:
        print(el.to_string())


def lab45():
    o = copy.deepcopy(ob)
    o.append(Operation('RR', [op[0], op[1]]))  # Pэ1 - 10
    o.append(Operation('RK', {o[10].get_type(): o[10], ok[0].get_type(): ok[0]}))  # Pэ2 - 11
    o.append(Operation('RKR', {'P1': op[2], 'P2': op[3], 'K': ok[1]}))  # Pэ3 - 12
    o.append(Operation('RR', [o[11], o[12], op[4], op[5], op[6]]))  # Pэ1 - 13

    print('\nK1,K2')
    for el in o:
        print(el.to_string())


def lab46():
    o = copy.deepcopy(ob)
    o.append(Operation('RR', [op[0], op[1]]))  # Pэ1 - 10
    o.append(Operation('RK', {o[10].get_type(): o[10], ok[0].get_type(): ok[0]}))  # Pэ2 - 11
    o.append(Operation('RR', [op[4], op[5], op[6]]))  # Pэ1 - 12
    o.append(Operation('RR', [o[10], op[2], op[3]]))  # Pэ1 - 13
    o.append(Operation('RKR', {'P1': o[13], 'P2': o[12], 'K': ok[1]}))  # Pэ3 - 14

    print('\nK1,K3')
    for el in o:
        print(el.to_string())


def lab47():
    o = copy.deepcopy(ob)
    o.append(Operation('RR', [o[0], o[1]]))  # Pэ1 - 10
    o.append(Operation('RKR', {'P1': o[2], 'P2': o[3], 'K': o[8]}))  # Pэ3 - 11
    o.append(Operation('RR', [o[4], o[5], o[6]]))  # Pэ4 - 12
    o.append(Operation('RR', [o[10], o[11]]))  # Pэ5 - 13
    o.append(Operation('RKR', {'P1': o[13], 'P2': o[12], 'K': o[9]}))  # Pэ6 - 14

    print('\nK2,K3')
    for el in o:
        print(el.to_string())


def lab49():
    k4 = {
        'K11': 0.997,
        'K00': 0.99,
        'M': 5,
        'D': 1
    }
    ob.append(Operation('K', k4))
    ok.append(Operation('K', k4))
    o = copy.deepcopy(ob)
    o.append(Operation('RR', [op[0], op[1]]))  # Pэ1 - 11
    o.append(Operation('RK', {o[11].get_type(): o[11], ok[0].get_type(): ok[0]}))  # Pэ2 - 12
    o.append(Operation('RKR', {'P1': op[2], 'P2': op[3], 'K': ok[1]}))  # Pэ3 - 13
    o.append(Operation('RR', [op[4], op[5], op[6]]))  # Pэ4 - 14
    o.append(Operation('RR', [o[12], o[13]]))  # Pэ5 - 15
    o.append(Operation('RKR', {'P1': o[15], 'P2': o[14], 'K': ok[2]}))  # Pэ6 - 16
    o.append(Operation('RK', {o[16].get_type(): o[16], ok[3].get_type(): ok[3]}))  # Pэ2 - 17

    print('\nK1,K2,K3,K4')
    for el in o:
        print(el.to_string())


if __name__ == '__main__':
    print('Lab3:')
    lab3()
    # print('\nLab4:')
    lab41()
    # lab42()
    # lab43()
    # lab44()
    # lab45()
    # lab46()
    # lab47()
    # lab49()
