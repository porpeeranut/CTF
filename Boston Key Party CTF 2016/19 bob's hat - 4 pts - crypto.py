from Crypto.Util.number import *
from sympy.solvers import solve
from sympy import Symbol
import libnum

'''
inspect file .pub to find e, n with below command
openssl rsa -pubin -in almost_almost_almost_almost_there.pub -text -modulus
and use yafu (https://sourceforge.net/projects/yafu/)
to find factor p, q from n(modulus) if it weak
    yafu-x64.exe
    factor(0x86E996013E77C41699000E0941D480C046B2F71A4F95B350AC1A4D426372923D8A4561D96FBFB0240595907201AD3225CF6EDED7DE02D91C386FFAC280B72D0F95CAE71F42EBE0D3EDAEACE7CEA3195FA32C1C6080D90EF853D06DD4572C92B9F8310BBC0C635A5E26952511751030A6590816554E763031BCBB31E3F119C65F)
'''

def partial_quotiens(x, y):
    pq = []
    while x != 1:
        pq.append(x / y)
        a = y
        b = x % y
        x = a
        y = b
    return pq

def rational(pq):
    i = len(pq) - 1
    num = pq[i]
    denom = 1
    while i > 0:
        i -= 1
        a = (pq[i] * num) + denom
        b = num
        num = a
        denom = b
    return (num, denom)

def convergents(pq):
    c = []
    for i in range(1, len(pq)):
        c.append(rational(pq[0:i]))
    return c

def phiN(e, d, k):
    return ((e * d) - 1) / k

def wiener_attack(e, n):
    pq = partial_quotiens(e, n)
    c = convergents(pq)
    x = Symbol('x')
    for (k, d) in c:
        if k != 0:
            y = n - phiN(e, d, k) + 1
            roots = solve(x**2 - y*x + n, x)
            if len(roots) == 2:
                p = roots[0]
                q = roots[1]
                if p * q == n:
                    break
    return p, q

def decrypt(p, q, e, n, ct):
    phi = (p - 1 ) * (q - 1)
    d = libnum.invmod(e, phi)
    pt = pow(ct, long(d), n)
    return libnum.n2s(pt)

################### LAYER 1 ######################
################### Solving layer 1: Weak key factored with ECM method"
m = libnum.s2n(open('almost_almost_almost_almost_there.encrypted','rb').read())
e = 65537
p1 = 9733382803370256893136109840971590971460094779242334919432347801491641617443615856221168611138933576118196795282443503609663168324106758595642231987246769
q1 = 9733382803370256893136109840971590971460094779242334919432347801491641617443615856221168611138933576118196795282443503609663168324106758595642231987245583
n1 = 0x86E996013E77C41699000E0941D480C046B2F71A4F95B350AC1A4D426372923D8A4561D96FBFB0240595907201AD3225CF6EDED7DE02D91C386FFAC280B72D0F95CAE71F42EBE0D3EDAEACE7CEA3195FA32C1C6080D90EF853D06DD4572C92B9F8310BBC0C635A5E26952511751030A6590816554E763031BCBB31E3F119C65F
print "pass1:",decrypt(p1, q1, e, n1, m)

################### LAYER 2 ######################
################### Solving layer 2: Common factors attack!"
m = libnum.s2n(open('./almost_almost_almost_almost_there/almost_almost_almost_there.encrypted','rb').read())
n2 = 0xABE633CEC2E7EC10A851927905A657DF4E10416023C0C34FC64D64BD8B8257B7BF207ADD047B0ADF21C525B052068C70295C746C3B1BE1436F39ED8BF7A813E4B845CE0CA89CA828B45763D46B1898C7A2FA5F8FE78428CAB6CDF70EF871DB971B3232841A1CE2459CE650A154362F80CFB64163C3CA63AD72BCFBDBF0154FF7
p2 = p1
q2 = n2/p2
print "pass2:",decrypt(p2, q2, e, n2, m)

################### LAYER 3 ######################
################### Solving layer 3: Small q "
m = libnum.s2n(open('./almost_almost_almost_almost_there/almost_almost_almost_there/almost_almost_there.encrypted','rb').read())
n3 = 0xBAD20CF97ED5042DF696CE4DF3E5A678CF4FB3693D3DF12DFE9FD3FD8CC8AAB8B95533E414E3FC0C377F4EE54827118B1D30561A3C741BEA7C76899789B51743E076092DF9EB05DC97EB1505CE9EB12B5AB9E10ABF56F920A58E7E00ECF05977E872834DD8584CF4AC87CB7DC50159BD962C75CBEFB6C6AC3A31A74E7D8F1E4C10D5
p3 = 54311
q3 = 158304142767773473275973624083670689370769915077762416888835511454118432478825486829242855992134819928313346652550326171670356302948444602468194484069516892927291240140200374848857608566129161693687407393820501709299228594296583862100570595789385365606706350802643746830710894411204232176703046334374939501731
print "pass3:",decrypt(p3, q3, e, n3, m)

################### LAYER 4 ######################
################### Solving layer 4: Wieners attack!(small d, big e)"
m = libnum.s2n(open('./almost_almost_almost_almost_there/almost_almost_almost_there/almost_almost_there/almost_there.encrypted','rb').read())
e = 0x466a169e8c14ac89f39b5b0357effc3e2139f9b19e28c1e299f18b54952a07a932ba5ca9f4b93b3eaa5a12c4856981ee1a31a5b47a0068ff081fa3c8c2c546feaa3619fd6ec7dd71c9a2e75f1301ec935f7a5b744a73df34d21c47592e149074a3ccef749ece475e3b6b0c8eecac7c55290ff148e9a29db8480cfe2a57801275
n3 = 0x9C2F6505899120906E5AFBD755C92FEC429FBA194466F06AAE484FA33CABA720205E94CE9BF5AA527224916D1852AE07915FBC6A3A52045857E0A1224C72A360C01C0CEF388F1693A746D5AFBF318C0ABF027661ACAB54E0290DFA21C3616A498210E2578121D7C23877429331D428D756B957EB41ECAB1EAAD87018C6EA3445
p3, q3 = wiener_attack(e, n3)
print "pass4:",decrypt(p3, q3, e, n3, m)
