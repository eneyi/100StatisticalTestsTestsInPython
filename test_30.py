# Test 30 Dunnett’s test for comparing K treatments with a control

def dunnettstest(vari,k,n):
    varw=np.sum(vari)/((k-1)*(n-1))
    statistics=sqrt((2*varw)/n)
    D1=abs(vari[1]-vari[0])
    D2=abs(vari[2]-vari[0])
    return statistics,D1,D2