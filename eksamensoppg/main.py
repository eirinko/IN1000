from bruktmarked import Bruktmarked

def main():
    marked=Bruktmarked()
    marked.nyKategori("sykkellykt")
    annonseSykkellykt=marked["sykkellykt"].nyAnnonse("New York sykkellykt")
    Peter_bud=annonseSykkellykt.giBud("Peter",42)
    Ann_bud=annonseSykkellykt.giBud("Ann",0)
    Mary_bud=annonseSykkellykt.kraftBud("Mary",40,50)
    
    vinnerBud=annonseSykkellykt.hoyesteBud()
    
    assert vinnerBud.hentBudStr()==43
    assert vinnerBud.hentBudgiver()=="Mary"
    assert vinnerBud==Mary_bud
    
main()
