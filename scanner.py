# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2 ("Port.")
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

Module contains logic for detecting mentions of brands in a string. 

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
Scanner             Object the finds mentions of brands in a string.
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
import re
# 2) Port.
# N/a

class Scanner:
    """
    
    Object finds occurences of substrings.
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    
    FUNCTIONS:
    index_brand()       Find all mentions of a brand in a string
    index_brands()      Find all mentions of multiple brands in a string
    scan()              Find all mentions of brands in the body of an event.    
    ------------------  --------------------------------------------------------
    """
    def __init__(self):
        pass

    def scan(self, event, brands, fold_case=True):
        """

        scan() -> dict

        Method checks the event's body for the location of brands. You get a
        dictionary keyed to brand where the values are list of (start, end)
        tuples. 
        """
        body = event.get_body()
        
        if fold_case:
            body = body.casefold()
            folded_brands = set()
            
            for brand in brands:
                folded = brand.casefold()
                folded_brands.add(folded)

            brands = folded_brands      

        matches = self.index_brands(body, brands)                
        return matches       

    # this is the simple equivalent to the brands detection in parser.
    def index_brand(self, string, brand):
        """

        index_brand() -> list

        Method finds the location of each mention of the brand in the string.
        You get back a list of tuples showing the starting and ending location.
        """
        result = list()
        wip = re.finditer(brand, string)
        # wip is a generator
        for match in wip:
            span = match.span()
            result.append(span)

        return result

    def index_brands(self, string, brands):
        """

        index_brands() -> dict

        Method returns a dictionary of the locations of each brand in the
        string. 
        """
        result = dict()
        for brand in brands:
            spans = self.index_brand(string, brand)
            result[brand] = spans
        return result
    
b1 = {"Queen of Glory", "Film Movement"}
s1 = """
Queen of Glory was produced by Jamund Washington, Kelley Robin Hicks and Baff
Akoto and also stars Meeko, Oberon K.A. Adjepong and Adam Leon. The film made
its world premiere at the 2021 Tribeca Film Festival, where it won the award for
Best New Narrative Director. It has subsequently claimed the Hamptons
International Film Festival’s Excellence in Directing Award and the Mill Valley
Film Festival’s inaugural Mind the Gap Creation Prize, and is currently
nominated for Independent Spirit Awards in the categories of Best First Feature
and Best Supporting Male, with the latter recognition going to Mensah’s co-star,
Meeko.

“Queen of Glory heralds a true coming-out-party for Nana–both in front of and
behind the camera,” said Film Movement President Michael Rosenberg. “Throughout
the years, we’re proud of our track record of introducing unique new talents to
cinema lovers, and we’re excited that we’re able to play a part in Nana’s career
– one that’s sure to be rich, varied and successful.”

“Our entire team is thrilled to partner with Film Movement and is honored to be
a part of their history of bold, passionate and boundary-pushing films,” added
Mensah. “We can’t wait for them to introduce this very special film to audiences
this year.”

Film Movement is a North American distributor founded in 2002 that has also
recently acquired Stefan Ruzowitzky’s thriller Hinterlands; Hong Sung-eun’s
feature directorial debut, Aloners; Bobbi Jo Hart’s doc Fanny: The Right to
Rock; Laura Wandel’s Playground; French actress Sandrine Kiberlain’s feature
directorial debut, A Radiant Girl; Mario Martone’s Italian period drama, The
King of Laughter, starring Toni Servillo; Olivia Peace’s coming-of-age drama
Tahara; Philipp Stölzl’s Chess Story, based on the Stefan Zweig novel of the
same name; Jacqueline Lentzou’s debut feature Moon, 66 Questions; and Bogdan
George Apetri’s acclaimed Romanian crime thriller, Miracle.
"""

hp = Scanner()

def run_test1():
    print("Text: ")
    print(s1)
    print("Brands: ")
    print(b1)
    index = hp.index_brands(s1, b1)
    print("Index: ")
    print(index)
    return index

if __name__ == "__main__":
    run_test1()
