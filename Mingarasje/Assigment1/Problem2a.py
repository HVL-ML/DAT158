"""
Dette gjelder de forrige oppgavene
last-tabellen lagrer den siste, altså den bokstaven som er sist, posisjonen til hver bokstav:

last(a) = 5
last(b) = 2
last(d) = -1

Visuelt:
P:       a  a  b  a  a  a
Indeks:  0  1  2  3  4  5
               ↑        ↑
           siste b    siste a


Runde 1:
T:  a a a b a a d a a b a a a
P:  a a b a a a

P[5] = a  og T[5] = a    ✓
P[4] = a  og T[4] = a    ✓
P[3] = a  og T[3] = b    ✗

Runde 2:
T:  a a a b a a d a a b a a a
P:    a a b a a a

a og d blir mismatch så det blir

5 - -1 = 6
Vi hopper med 6 posisjoner fra runde 2 så vi hopper i fra ideks 1 og da havner vi på indeks 7

Runde 3:
T:  a a a b a a d a a b a a a
P:                a a b a a a

FULL MATCH

DETTE ER DET VIKTIGASTE EGT I BUNN OG GRUNN
last_pos = last.get(mismatch_letter, -1)
jump = max(1,j-last_position)
start = start + jump
"""