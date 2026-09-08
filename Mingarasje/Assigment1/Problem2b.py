
def make_last(pattern):
    last = {}

    for j in range(len(pattern)):
        last[pattern[j]] = j

    return last

def boyer_moore(text, pattern):
    last = make_last(pattern)
    n = len(text)
    m = len(pattern)

    start = 0
    comparisons = 0
    round_number = 1

    while start <= n - m:
        print(f"\nRunde {round_number}, start = {start}")

        #Vi begynner til høyre i mønsteret.
        j = m - 1

        while j >= 0:
            # Finner tilhørende posisjon i teksten.
            i = start + j
            comparisons += 1
            print(
                f"Sammenligner T[{i}] = {text[i]} "
                f"med P[{j}] = {pattern[j]}"
            )

            if text[i] == pattern[j]:
                print("Match")
                j -= 1

            else:
                print("Mismatch")
                # Bokstaven i teksten som skapte mismatchen.
                mismatch_letter = text[i]
                # Bruk -1 hvis bokstaven ikkje finnes.
                last_position = last.get(mismatch_letter, -1)
                # Boyer–Moore-formelen.
                jump = max(1, j - last_position)

                print(f"last({mismatch_letter}) = {last_position}")
                print(
                    f"Hopp = max(1, {j} - "
                    f"{last_position}) = {jump}"
                )
                # Flytt mønsteret.
                start = start + jump
                # Avslutt den innerste løkken.
                break
        # Denne testen skal være etter den innerste løkken.
        if j < 0:
            return start, comparisons
        round_number += 1
    # Kjøres bare hvis mønsteret ikke ble funnet.
    return -1, comparisons

# Testkoden skal stå utenfor funksjonen.
text = """En mandag morgen våknet Nora av regnet som traff vinduet. Byen lå
  stille under tunge skyer, og gatene var nesten tomme. Hun laget kaffe, fant
  fram sekken og sjekket rutetidene på telefonen. Nora bestemte seg derfor for å
  gå til høyskolen. Turen tok litt over en halv time, og hun likte vanligvis å
  bruke tiden til å tenke.

  På veien passerte hun biblioteket, bakeriet og den lille parken ved elven. Noen
  syklister hastet mot sentrum, mens andre ventet under tak for å slippe regnet.
  Ved fotgjengerfeltet møtte Nora en medstudent som het Elias. Han hadde også
  valgt å gå fordi bussene sto fast i trafikken. De snakket om dagens
  forelesning, som skulle handle om algoritmer for søking i tekst.

  Da de kom fram, var klasserommet allerede fullt. Læreren hadde skrevet flere
  ord og tall på tavlen. Først forklarte hun hvordan en enkel algoritme
  undersøker teksten fra venstre mot høyre. Deretter viste hun hvordan Boyer-
  Moore begynner sammenligningen på høyre side av mønsteret. Dersom et tegn ikke
  finnes i mønsteret, kan algoritmen hoppe over flere posisjoner. Dette kan
  redusere antallet sammenligninger betydelig.

  Studentene fikk beskjed om å teste algoritmen på en lengre norsk tekst. De
  skulle telle hver gang et tegn i teksten ble sammenlignet med et tegn i
  mønsteret. Arbeidet som ble brukt til å lage tabellen over de siste
  posisjonene, skulle ikke være med i tellingen. Til slutt skulle de dele
  antallet sammenligninger på antallet tegn som var undersøkt.

  Nora og Elias begynte med korte eksempler. De oppdaget raskt at resultatet
  endret seg når de valgte et annet mønster. Et mønster med sjeldne bokstaver ga
  ofte store hopp, mens vanlige bokstaver førte til flere treff og mindre hopp.
  Plasseringen av ordet hadde også betydning. Dersom ordet sto tidlig, stoppet
  programmet før resten av teksten var undersøkt.

  Etter lunsj bestemte de seg for å bruke et mønster som ikke fantes i teksten.
  Da måtte algoritmen fortsette helt til slutten, og resultatet ble lettere å
  sammenligne med andre forsøk. De kontrollerte at mønsteret hadde nøyaktig fem
  tegn, siden teorien de skulle undersøke, handlet om mønstre med denne lengden.

  De kjørte programmet flere ganger og skrev resultatene i en tabell. Tabellen
  viste tekstlengde, mønster, antall sammenligninger og gjennomsnitt per tegn.
  Den dynamiske utskriften fra programmet var nyttig under utviklingen, men
  produserte svært mange linjer. Da de visste at algoritmen fungerte, fjernet de
  fleste utskriftene og beholdt bare det endelige resultatet.

  Resultatet var ikke nøyaktig likt tallet fra den engelske undersøkelsen. Nora
  mente dette var naturlig fordi norske og engelske tekster har forskjellige
  bokstavfrekvenser. Tekstens tema, lengde og tegnsetting kunne også påvirke hvor
  langt algoritmen hoppet. Ett enkelt forsøk kunne derfor ikke bevise at språket
  alene var årsaken til forskjellen.

  Da Nora gikk hjem, hadde regnet stoppet. Skyene åpnet seg, og kveldssolen lyste
  over elven. Hun var fortsatt usikker på enkelte detaljer, men hun forsto nå
  hvorfor Boyer-Moore ofte arbeider raskere enn et enkelt søk. Algoritmen
  undersøker ikke nødvendigvis hvert tegn. Den bruker informasjon fra mønsteret
  til å unngå arbeid som ikke er nødvendig."""
pattern = "huset"
position, comparisons = boyer_moore(text.lower(), pattern.lower())

if position == -1:
    characters_searched = len(text)
else:
    characters_searched = position + len(pattern)
average = comparisons / characters_searched

print("\nResultat:")
print("Mønsteret blei funne på posisjon:",
      position)
print("Undersøkt tekstlengd:",
      characters_searched)
print("Talet på samanlikningar:",
      comparisons)
print("Samanlikningar per teikn:", average)
