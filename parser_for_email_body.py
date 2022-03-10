# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2.0. ("Port.")
#
# Port. is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Port. is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Port. If not, see <https://www.gnu.org/licenses/>.
#
# Questions? Contact hi@runport.io.

"""

Module defines routines for parsing the body of an email. 
------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:
N/a

FUNCTIONS:
casefold_items      removes capitals from each string in a container
parse_body          takes header off the email, decodes text
parse_header        turns lines of text in the header into a dictionary of data
prep_string         separates and parses header, cleans whitespace
remove_nonalnum     takes string down to letters and numbers only
strip_header        removes header from the body of the email
strip_links         [ND] removes links from body

CLASSES:
N/a
------------------  ------------------------------------------------------------
"""


# Imports
# 1) Built-ins
import copy

# 2) Port.
import constants
import mini_html
import observ2
import references

# 3) Data
HTML_PARSER = mini_html.MiniParser()

# 4) Functions
def casefold_items(iterable):
    """

    casefold_items() -> list

    Function folds the case of each item in the iterable. You get a list of
    casefolded items back.
    """
    result = list()
    for item in iterable:
        adj_item = item.casefold()
        result.append(adj_item)
        
    return result

def get_body_as_text(msg):
    """

    get_body_as_text() -> string

    Function returns the text content of the message, if any.
    """
    raw = observ2.get_body(msg)
    return raw

def make_alnum(string, include_chars=[constants.HYPHEN]):
    """

    make_alnum -> string

    Function strips string of characters that are not letters or numbers. You
    can specify characters you want to keep in addition to these.
    """
    result = ""
    for char in string:
        if char.isalnum():
            result = result + char
        else:
            if char in include_chars:
                result = result + char
            else:
                pass
            
    return result
    
def parse_header(header, match_case=False, strip_whitespace=True):
    """

    parse_header() -> dict

    Function splits lines that represent the header into keys and values. You
    should put in a list of strings into the header.
    """
    result = dict()
    wip = dict()
    assignment_operators = [constants.COLON, constants.EQUALS]
    
    if not match_case:
        header = casefold_items(header)
        assignment_operators = casefold_items(assignment_operators)
    
    for line in header:
        # line1: "Content-Type: text/plain; charset=utf-8"
        segments = line.split(constants.SEMICOLON)
        for segment in segments:
            # segment: "Content-Type: text/plain;"
            operator = ""
            for operator in assignment_operators:
                if operator in segment:
                    key, value = segment.split(operator)
                    permitted_chars = [constants.FWD_SLASH, constants.HYPHEN]
                    cleaned_value = make_alnum(value, permitted_chars)
                    wip[key] = cleaned_value

    if strip_whitespace:
        for k, v in wip.items():
            adjk = k.strip()
            adjv = v.strip()
            result[adjk] = adjv
    else:
        result = wip

    return result

def parse_html(html):
    """

    parse_html() -> string, dict

    Function returns a tuple that represents the text inside the html and
    information about that text. 
    """
    data = dict()
    # not assigned for now, later may contain links, etc.
    lines_of_html = html.splitlines()
    body = parse_lines_of_html(lines_of_html)
    # could potentially send this down to references for additional cleaning.
    
    result = (body, data)
    # I am using a placeholder for data to match signature from function for
    # processing text.
    return result

def parse_lines_of_html(lines_of_html, parser=HTML_PARSER):
    """

    parse_lines_of_html() -> string

    Function returns a list of output from the parser, skipping exceptions.
    """
    result = list()
    parser.reset()
    parser.container_for_text = ""
    #<-----------------------------------------------------------------! really need to make sure this is automatic
    
    for line_of_html in lines_of_html:
        try:
            parser.feed(line_of_html)
        except Exception:
            pass
            # add to log?

    wip = parser.container_for_text
    wip = x_remove_space(wip)
    
    result = wip

    return result

def parse_text(string, trace=False):
    """

    parse_text() -> string, dict

    Function attempts to turn the text into a string without headers or
    escapes. You can use this to clean plain text emails.
    """
    body, data = prep_string(string)
    if trace:
        print("Input: ")
        print(string)

        print("Data: ")
        print(data)
        
    if body:
        if data:    
            charset = data[constants.CHARSET]
            charset = charset.casefold()
            if trace:
                print("Charset:  ", charset)

            if charset == constants.UTF8.casefold():
                body = references.clean_string(body, trace=trace, encoding=charset)
            if trace:
                print("Body, cleaned: \n", body)
                print("\n\n\n\n")
    
    return body, data

def prep_string(string, strip_whitespace=True):
    """

    prep_string() -> tuple

    Function prepares string for processing by removing header and stripping
    whitespace. You should err on side of stripping whitespace.
    """
    body = string
    data = dict()
    if body:
        if strip_whitespace:
            body = body.strip()
            # Remove leading whitespace to reduce odds of missing header.
        
        header, body = strip_header(body)
        if strip_whitespace:
            body.strip()
            # Remove whitespace again now that I separated the header.
            
        data = parse_header(header)
    
    return (body, data)

def strip_header(string):
    """

    strip_header() -> list, string

    Function splits the string into lines and takes the first "line_count" lines
    as the header. 
    """
    result = tuple()
    header = list()
    wip = string.strip()
    lines = wip.splitlines(keepends=True)

    line1 = lines.pop(0)
    
    line1_copy = copy.copy(line1)
    line1_copy.strip()
    # strip leading whitespace
    
    if line1_copy.startswith(constants.CONTENT_TYPE):
        header.append(line1_copy)
        # Line is part of the header. I use the copy here because we already
        # stripped it of whitespace. 
        
        line2 = lines.pop(0)
        # Get the next line and test it.
        line2_copy = copy.copy(line2)
        line2_copy = line2_copy.strip()
        
        if line2_copy.startswith(constants.CONTENT_ENCODING):
            header.append(line2_copy)
        else:
            lines.insert(0, line2)
            # Second line is not part of the header. Put it back.
    else:
        lines.insert(0, line1)
        # Line1 does not start with the right thing, put it back
    
    body = "".join(lines)
    # Put the lines back together. I used pop to remove the header lines, so
    # they should no longer be here.

    result = (header, body)
    return result

def strip_links(string):
    """

    strip_links() -> dictionary

    Function removes links, replaces them with numbers. Returns dictionary of
    number to link.
    """
    c = "Have not built this functionality yet."
    raise exceptions.PlaceholderError(c)

def x_remove_space(string, recur=False):
    """

    experimental
    
    removes triple spaces from strings.
    """
    spaces = {" ", "\t", "\r", "\n"}
    string = string.strip()
    i = 0
    wip = ""
    length = len(string)
    while i < length:
        char_1 = string[i]
        if char_1 in spaces:
            if i < (length - 2):
                char_2 = string[i+1]
                char_3 = string[i+2]
                if char_2 in spaces and char_3 in spaces:
                    pass
                    # skip triple spaces
                else:
                    wip = wip + char_1
        else:
            wip = wip + char_1
            # just take suffix as is
    
        i = i + 1

    result = wip
    return result

# Testing

s1 = """
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: quoted-printable


10 FEBRUARY 2022Online lesen ( https://api-esp.piano.=
io/story/estored/480/16976/-1/13455436/344622/vib-ckzgn3xf4002z0144cufz9rf5=
?sig=3D705ff8b2975779ebab06de2a4967bb45225f03c554f28a5ae39c88686282d3de )
https://api-esp.piano.io/-c/480/16976/256344/13455436/344622/-YutwnkBUCtMWQ=
2xxWWZ/-1/-1?attrs=3D0&order=3D0
Willkommen bei EURACTIV's Europa Kompakt =
Newsletter! Wir tragen die wichtigsten News und Infos an der Schnittstelle =
zwischen deutscher und Europapolitik f=C3=BCr Sie zusammen.
Autoindustrie schl=C3=A4gt beim Ausbau der E-Lades=C3=A4ulen die =
Alarmglocken
Nichts steht so oft im Verruf ein Rohrkrepierer zu werden wie =
die E-Mobilit=C3=A4t. Dass Deutschland beim Ausbau der Ladeinfrastruktur =
zwar europ=C3=A4ische Spitzenklasse ist, allerdings doch weit hinter den =
Anspr=C3=BCchen zur=C3=BCckliegt, sollte uns da zu denken geben. =
=E2=80=9CDie L=C3=BCcke wird gr=C3=B6=C3=9Fer, nicht kleiner. Eine =
L=C3=BCcke, die uns den Erfolg kosten kann. Scheitern ist aber keine Option=
,=E2=80=9D warnt daher Hildegard M=C3=BCller, die Pr=C3=A4sidentin des =
Verbands der Automobilindustrie.
Sie vertritt damit auch die Zulieferer, =
deren Gesch=C3=A4ftsmodell nicht nur mit 2035 mehr oder wenig wegbricht, =
sondern auch jahrzehntelang aufgebaute Wettbewerbsvorteile und =
Lernkurveneffekte in der Herstellung von Teilen f=C3=BCr =
Verbrennungsmotoren zunichtegemacht werden.
Und trotzdem k=C3=A4mpft =
M=C3=BCller f=C3=BCr die Verkehrswende, denn diese ist l=C3=A4ngst =
Gewissheit. Jetzt m=C3=BCssen auch die Regierungen Europas ihren Frieden =
damit machen und endlich den Grundstein f=C3=BCr eine der gr=C3=B6=C3=9Ften=
 und wichtigsten gesellschaftlichen Transformationen unserer Zeit legen. =
Denn einen Rohrkrepierer in der E-Mobilit=C3=A4t k=C3=B6nnen wir uns weder =
wirtschaftlich noch klimaschutztechnisch leisten.
Es wird Schlag auf Schlag=
 gehen m=C3=BCssen, denn diese Bundesregierung wird binnen zwei Jahren das =
EU-weite Verbrenner-Aus von 2035 gesetzlich festschreiben.
Den vollst=C3=A4ndigen Artikel k=C3=B6nnen Sie hier ( https://api-esp.piano=
.io/-c/480/16976/256346/13455436/344622/5e1e3b8bfe6eedff586a35f65ff04e43/-1=
/-1?attrs=3D0&order=3D0 ) lesen.
@NKurmayer ( https://api-esp.piano.=
io/-c/480/16976/276166/13455436/344622/62SB4X0BBDhbr34ShG6H/-1/-1?=
attrs=3D0&order=3D0 )
Der Umweltausschuss im EU-Parlament stimmt =C3=BCber =
neue Batterieverordnung ab. F=C3=BCr ein klimaneutrales Europa sind =
Batterien von gro=C3=9Fer Wichtigkeit, sei es f=C3=BCr die E-Mobilit=C3=A4t=
 oder f=C3=BCr die Speicherung von volatilen erneuerbaren Energien. Laut =
der Industrie kann Europa globale Standards setzen, solange die Verordnung =
ambitioniert genug ist. Die franz=C3=B6sische Ratspr=C3=A4sidentschaft hat =
Batterien ebenfalls zur Priorit=C3=A4t erhoben. Es bleibt zu sehen, ob ein =
tragbarer Kompromiss gefunden wird.
Berlin und Paris auf der Suche nach =
Industrie- und Energiesynergien. Mithilfe von Arbeitsgruppe ( =
https://api-esp.piano.io/-c/480/16976/256350/13455436/344622/2a40512d0bf373=
e651e4d50116245c9e/-1/-1?attrs=3D0&order=3D0 ) n, einem Vorschlag, der nur =
von Bundeswirtschaftsminister Robert Habeck kommen kann, will das =
deutsch-franz=C3=B6sische Duo die Kooperation in Themen wie Wasserstoff =
intensivieren. Ob der deutsche Konsument ein Auto, das mit Stahl unter der =
Verwendung von Atomstrom-Wasserstoff hergestellt wurde, kaufen w=C3=BCrde, =
bleibt jedoch offen. Knackpunkt bleibt dabei die deutsche Anti-Atomkraft =
Haltung.
Die LNG-Saga geht weiter. F=C3=BCr die USA ist es nach wie vor von=
 h=C3=B6chster Wichtigkeit, dass Deutschland eine Alternative zum zunehmend=
 problematischen russischen Erdgas bekommt. Nachdem die USA sowohl in Japan=
 als auch in Katar interveniert hatten, wird Japan jetzt =
=C3=BCbersch=C3=BCssiges fl=C3=BCssiges Erdgas (LNG) nach Europa schicken. =
Das Thema wird wohl auch beim jetzt angek=C3=BCndigten Treffen der =
Gas-Exportl=C3=A4nder am 22. Februar in Katar angeschnitten werden.
@NKurmayer ( https://api-esp.piano.io/-c/480/16976/256376/13455436/344622/6=
2SB4X0BBDhbr34ShG6H/-1/-1?attrs=3D0&order=3D0 )
W=C3=BCrden Sie diesen =
Newsletter gerne sponsern? Kontaktieren Sie uns ( https://api-esp.piano.=
io/-c/480/16976/256359/13455436/344622/odnkW3oBfER2vdXr1msp/-1/-1?=
attrs=3D0&order=3D0 )
Meta rudert zur=C3=BCck. Der Digitalkonzern Meta, dem=
 neben Facebook auch Instagram und Twitter geh=C3=B6ren, wird Europa nicht =
verlassen. Dies gab das Unternehmen am Mittwoch bekannt. =E2=80=9EMeta =
droht nicht damit, Europa zu verlassen und jede Berichterstattung, die dies=
 impliziert, ist schlichtweg falsch,=E2=80=9C schrieb der =
Vizepr=C3=A4sident f=C3=BCr Public Policy Europe, Markus Reinisch in einem =
Blogeintrag.
EU-Parlament bekommt Pegasus Untersuchungsausschuss. Der =
Ausschuss wird auch Antrag der Renew Europe Fraktion eingerichtet, um sich =
n=C3=A4her mit dem Pegasus Skandal vom vergangenen Juli zu befassen. Damals=
 wurde bekannt, dass die Spyware m=C3=B6glicherweise auch zum Hacken der =
Telefone von Journalisten, Aktivisten und Politikern verwendet wurde. Der =
Ausschuss =E2=80=9Emuss so schnell wie m=C3=B6glich eingerichtet werden und=
 den Vorw=C3=BCrfen der illegalen Bespitzelung von Regierungskritikern =
umfassend nachgehen,=E2=80=9C schrieb die liberale EU-Abgeordnete Sophie in=
 =E2=80=98t Veld auf Twitter.
Britische Aufsichtsbeh=C3=B6rden warnen vor =
russischen Cyberangriffen. Inmitten der angespannten Lage an der =
ukrainischen Grenze warnt die Finanzaufsichtsbeh=C3=B6rde Banken vor =
m=C3=B6glichen Cyberangriffen durch Russland. Die Beh=C3=B6rde rief den =
Bankensektor daher dazu auf, Abwehrm=C3=B6glichkeiten zu verst=C3=A4rken, =
um f=C3=BCr einen m=C3=B6glichen Angriff gewappnet zu sein.
@noyan_oliver ( https://api-esp.piano.io/-c/480/16976/256377/13455436/34462=
2/M-u0dn0BQ4p2jWscjEW0/-1/-1?attrs=3D0&order=3D0 )
Carbon Farming: =
Wenigstens aufs Schlagwort k=C3=B6nnen sich alle einigen. Beim informellen =
Treffen der Agrarminister:innen in Stra=C3=9Fburg hat der franz=C3=B6sische=
 Gastgeber Julien Denormandie den gemeinsamen Enthusiasmus aller =
EU-L=C3=A4nder f=C3=BCr eine kohlenstoffarme Landwirtschaft beschworen. =
Doch dar=C3=BCber, wie der CO2-Abbau in der Praxis gef=C3=B6rdert werden =
soll, blieben wesentliche Fragen offen. Lesen Sie hier ( https://api-esp.=
piano.io/-c/480/16976/256363/13455436/344622/e42bddd99845a8c7384393aa5ba3ab=
b1/-1/-1?attrs=3D0&order=3D0 ) unseren Bericht aus Stra=C3=9Fburg.
Covid-Apps k=C3=B6nnten auch f=C3=BCr andere Impfungen n=C3=BCtzlich sein. =
Apps nach dem Vorbild der digitalen Covidtracker k=C3=B6nnten in Zukunfts =
auch zur =C3=9Cberwachung der Impfraten ( https://api-esp.piano.=
io/-c/480/16976/256363/13455436/344622/d6f3abf0c32eb9fbbce6e840b1de3e55/-1/=
-1?attrs=3D0&order=3D1 ) bei anderen Krankheiten genutzt werden, sagte die =
Direktorin des Europ=C3=A4ischen Zentrums f=C3=BCr die Pr=C3=A4vention von =
Infektionskrankheiten, Andrea Ammon, auf einer Konferenz. Auch die =
EU-Gesundheitsminister:innen besch=C3=A4ftigten sich zum Start ihres =
Treffens in Frankreich mit digitalen Anwendungen.
Gef=C3=A4hrden die =
EU-Umweltziele Europas Lebensmittelproduktion? Laut mehreren Studien =
k=C3=B6nnte durch die Umsetzung der europ=C3=A4ischen Klima- und =
Naturschutzziele im Lebensmittelsektor die Produktion senken ( =
https://api-esp.piano.io/-c/480/16976/256363/13455436/344622/53972e18ce9fc7=
4eb980dad75114214e/-1/-1?attrs=3D0&order=3D2 ) . Doch wie valide die =
Studien sind und was die Ergebnisse f=C3=BCr die Politik bedeuten, bleibt =
unter Abgeordneten und Interessenvertretern umstritten.
@dahm_julia ( https://api-esp.piano.io/-c/480/16976/256378/13455436/344622/=
xGJ3lX0BcqwGw-Kk1Gma/-1/-1?attrs=3D0&order=3D0 )
Griechenland und Bulgarien=
 f=C3=BChren Corona-Todesliste der EU an. W=C3=A4hrend die Ausbreitung der =
Omicron-Variante zu rekordverd=C3=A4chtigen Infektionsraten in ganz Europa =
gef=C3=BChrt hat, lockern viele Regierungen ihre Corona-Auflagen und =
erkl=C3=A4ren, dass ein Ende in Sicht sei. In der Realit=C3=A4t haben =
einige Staaten jedoch noch immer mit unverh=C3=A4ltnism=C3=A4=C3=9Fig hohen=
 Sterblichkeitsraten zu k=C3=A4mpfen ( https://api-esp.piano.=
io/-c/480/16976/256367/13455436/344622/32745d34feb6f5a2b65d962889d4e22d/-1/=
-1?attrs=3D0&order=3D0 ) .
Diaspora-Vertreter: Bulgariens Veto schadet der =
Zukunft Nordmazedoniens. Die EU-Beitrittsverhandlungen mit Nordmazedonien =
sollten unverz=C3=BCglich aufgenommen werden. Die politischen Probleme mit =
Bulgarien lassen sich l=C3=B6sen, sobald die Verhandlungskapitel =
er=C3=B6ffnet sind ( https://api-esp.piano.io/-c/480/16976/256367/13455436/=
344622/c5dbee82fc16867276b68c633e5217ce/-1/-1?attrs=3D0&order=3D1 ) , so =
Metodija Koloski, Pr=C3=A4sident der Vereinigten Mazedonischen Diaspora =
(UMD).
Frankreich erw=C3=A4gt Corona-Lockerungen und Abschaffung der =
Impfnachweise. Die franz=C3=B6sische Regierung erw=C3=A4gt, die =
Corona-Ma=C3=9Fnahmen zu lockern. Dies gab Regierungssprecher Gabriel Attal=
 am Ende der Sitzung des Ministerrats gestern bekannt, wo er die =
Bereitschaft seiner Regierung bekr=C3=A4ftigte, den Impfnachweis =
abzuschaffen ( https://api-esp.piano.io/-c/480/16976/256367/13455436/344622=
/d73a503bcc2d70a220dc63da92296a2b/-1/-1?attrs=3D0&order=3D2 ) , wenn sich =
die Situation in den Krankenh=C3=A4usern verbessert.
Spaniens Au=C3=9Fenminister: Keine Zeit f=C3=BCr Spekulationen =C3=BCber =
=E2=80=9EKriegsszenarien=E2=80=9C in der Ukraine. Es sei Zeit f=C3=BCr =
Diplomatie und Dialog ( https://api-esp.piano.io/-c/480/16976/256367/134554=
36/344622/a8561b9cab4f866303534af12cb3596a/-1/-1?attrs=3D0&order=3D3 ) , =
betonte Albares von der sozialdemokratischen Regierungspartei PSOE bei =
einem Kurzbesuch in Kiew. =E2=80=9EDas ist der Weg, den wir gew=C3=A4hlt =
haben. Wir glauben, dass jetzt die Zeit f=C3=BCr Diplomatie gekommen ist =
und nicht f=C3=BCr das Aufstellen von Szenarien und Hypothesen, die es =
nicht gibt=E2=80=9C, betonte er.
Polnisches Parlament verabschiedet =
umstrittenes Bildungsgesetz trotz Opposition. Der Sejm, das Unterhaus des =
polnischen Parlaments, hat ein Veto des Senats gegen einen Entwurf zur =
=C3=84nderung des Bildungsrechts abgelehnt. ( https://api-esp.piano.=
io/-c/480/16976/256367/13455436/344622/d87ceb491a8447b01b04d8ac3ad0efaa/-1/=
-1?attrs=3D0&order=3D4 ) Nach Ansicht von Kritiker:innen k=C3=B6nnte die =
=C3=84nderung die Kontrolle der Regierung =C3=BCber die Schulen =
verst=C3=A4rken und zu einer Politisierung des Bildungswesens f=C3=BChren.
COVID-19 soll in Tschechien zu einer =E2=80=9Enormalen Krankheit=E2=80=9C =
werden. Die tschechische Regierung hat beschlossen, die meisten =
Corona-Ma=C3=9Fnahmen des Landes abzuschaffen ( https://api-esp.piano.=
io/-c/480/16976/256367/13455436/344622/ed06cabc6297926776610e1fef9f7cdd/-1/=
-1?attrs=3D0&order=3D5 ) , so dass ab dem 18. Februar in Restaurants und =
anderen Betrieben keine Impfp=C3=A4sse mehr erforderlich sind.
EURACTIV unterst=C3=BCtzen.
Ihre Spende, ob gro=C3=9F oder klein ( =
https://api-esp.piano.io/-c/480/16976/256357/13455436/344622/yaD_0XkBHgSt8v=
oYNdvD/-1/-1?attrs=3D0&order=3D0 ) , unterst=C3=BCtzt unser Bem=C3=BChen, =
unabh=C3=A4ngige und qualitativ hochwertige Berichterstattung kostenlos =
f=C3=BCr alle bereitzustellen.
EU: EU-Kommissionspr=C3=A4sidentin Ursula =
von der Leyen und Kommissare setzen Besuch im Senegal fort / =
Wirtschaftskommissar Paolo Gentiloni pr=C3=A4sentiert Winterprognose
Frankreich: Gesundheitskommissarin Stella Kyriakides nimmt am Treffen der =
EU-Gesundheitsminister in Grenoble teil.
Deutschland: Bundeskanzler Scholz =
empf=C3=A4ngt den litauischen Pr=C3=A4sidenten Naus=C4=97da, den estnischen=
 Premierminister Kallas und den lettischen Premierminister Kari=C5=86=C5=A1=
 in Berlin.
Gro=C3=9Fbritannien: Premierminister Johnson trifft sich mit =
NATO-Chef Jens Stoltenberg in Br=C3=BCssel und reist weiter nach Warschau.
Spanien: Kommissions-Vizepr=C3=A4sident Margaritis Schinas trifft =
spanischen Au=C3=9Fenminister Jose Manuel Albares / Spanien beendet die =
Maskenpflicht im Freien.
Polen: Der britische Premierminister Boris Johnson=
 besucht am Donnerstag Polen, um mit dem polnischen Pr=C3=A4sidenten =
Andrzej Duda und Premierminister Mateusz Morawiecki =C3=BCber die Ukraine =
und bilaterale Beziehungen zu sprechen.
Kroatien: Premierminister Andrej =
Plenkovi=C4=87 trifft sich mit dem griechischen Premierminister Kyriakos =
Mitsotakis, der einen offiziellen Besuch abstatten wird.
Bosnien und Herzegowina: Die kroatischen und bosniakischen politischen =
Parteien werden ihre Verhandlungen =C3=BCber =C3=84nderungen des =
Wahlgesetzes fortsetzen.
Ukraine: Der polnische Au=C3=9Fenminister Zbigniew=
 Rau, derzeitiger Vorsitzender der OSZE, besucht Kiew.
Vielen Dank, dass Sie sich die Zeit genommen haben Europa Kompakt zu lesen!=
 Weitere tagesaktuelle News und Infos zur Europapolitik gibt's auf EURACTIV=
.de
Oliver Noyan ( https://api-esp.piano.io/-c/480/16976/256355/13455436/34=
4622/M-u0dn0BQ4p2jWscjEW0/-1/-1?attrs=3D0&order=3D0 )
mailto:oliver.noyan@euractiv.com
Julia Dahm ( https://api-esp.piano.=
io/-c/480/16976/256355/13455436/344622/xGJ3lX0BcqwGw-Kk1Gma/-1/-1?=
attrs=3D0&order=3D2 )
mailto:julia.dahm@euractiv.de
Nikolaus J. Kurmayer ( https://api-esp.piano.io/-c/480/16976/256355/1345543=
6/344622/62SB4X0BBDhbr34ShG6H/-1/-1?attrs=3D0&order=3D4 )
mailto:nikolaus.kurmayer@euractiv.com
https://api-esp.piano.=
io/-c/480/16976/256352/13455436/344622/3bR3lX0BRIYttNNC1IWh/-1/-1?attrs=3D0=
 https://api-esp.piano.io/-c/480/16976/256352/13455436/344622/D9CtwnkBIiiba=
YbRxZ-b/-1/-1?attrs=3D0 https://api-esp.piano.io/-c/480/16976/256352/134554=
36/344622/Q82twnkBSrHStmTGxUWh/-1/-1?attrs=3D0 https://api-esp.piano.=
io/-c/480/16976/256352/13455436/344622/UhJT2XcBDDgI0gS1qdi4/-1/-1?attrs=3D0=
 https://api-esp.piano.io/-c/480/16976/256352/13455436/344622/ygIQ0XkBpaQXz=
n7mQvCv/-1/-1?attrs=3D0
Feedback ( https://site-esp.piano.=
io/faq-and-feedback/en?pub_id=3D480&ml_id=3D16976&reply_to=3Dnewsletters%40=
euractiv.com&pub_name=3D&ml_name=3D ) Abmelden ( https://api-esp.piano.=
io/-s/9810b53db56e5afcb79c5ff731344eb7 ) EURACTIV ( https://www.euractiv.=
de/ )
EURACTIV Media Network BV: International Press Centre Boulevard =
Charlemagne 1 Brussels B-1000 Belgium
https://piano.io/product/esp/?=
utm_source=3Dintegration&utm_medium=3Demail&utm_campaign=3D16976
"""

s2 = """
Content-Type: text/plain; charset=us-ascii

Post       : Zurich renews aggregate catastrophe reinsurance at tighter terms
URL        : https://www.artemis.bm/news/zurich-renews-aggregate-catastrophe-reinsurance-at-tighter-terms/
Posted     : 10th February 2022 at 8:02 am
Author     : Steve Evans
Tags       : insurance, reinsurance, Reinsurance renewals news
Categories : News, Reinsurance News

Global insurance and reinsurance giant Zurich has revealed its new reinsurance program for 2022 and it appears that tighter terms and a tougher market for placing aggregate limit has resulted in a higher attachment point, adjusted deductible and a larger co-participation being taken.
Read more of this post ( https://www.artemis.bm/news/zurich-renews-aggregate-catastrophe-reinsurance-at-tighter-terms/#more-87387 )

--


Manage Subscriptions
https://subscribe.wordpress.com/?key=1c4097fb88eec03ccd4ac5fa30b77b88&email=put%40runport.io

Unsubscribe:
https://subscribe.wordpress.com/?key=1c4097fb88eec03ccd4ac5fa30b77b88&email=put%40runport.io&b=szebPNHuyzBRvZ277EWp4gArypzGlScsUiQeqHKEkNtVlrpNg_s8vAIg_JrnjPSl2sesxPjw0X5pp_PUow%3D%3D
"""

def run_test(string):    
    body, data = parse_text(string, trace=True)

if __name__ == "__main__":
    run_test(s1)
    run_test(s2)

