SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

soma = SP + RJ + MG + ES + Outros

psp = (SP/soma)*100
prj = (RJ/soma)*100
pmg = (MG/soma)*100
pes = (ES/soma)*100
pou = (Outros/soma)*100

print(f"O percentual de São Paulo é {psp:,.2f}%")
print(f"O percentual do Rio de Janiero  é {prj:,.2f}%")
print(f"O percentual de Minas Gerais é {pmg:,.2f}%")
print(f"O percentual do Espírito Santo é {pes:,.2f}%")
print(f"O percentual de outros é {pou:,.2f}%")


