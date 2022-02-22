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

Module defines routines for parsing references to hexadecimals in text. Emails
often contain references to hexadecimals to represent characters that might not
be compatible with HTML.
------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:
HEX_PREFIX          first two characters of hex bytes in python
STRICT              handle for strict decoding
UTF8                handle for UTF-8

FUNCTIONS:
adjust_base         turn hexadecimal or other input into a number in base10
clean_string        replace references with characters in a string
construct_sequence  turns token into a string with escapes
get_bytes           turns a container of hex strings into a bytestring
get_integers        turns a container of hex strings into base 10 integers
get_next            walk a string, pull out one reference at a time
get_tokens          extract tokens from string
locate_references   find substrings that start with the prefix you specify
turn_tokens_into_bytes     maps tuples to bytestrings
turn_tokens_into_strings   maps tuples to unicode characters
unescape_chars      removes escapes from breaks in the string

CLASSES:
N/a
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
# n/a

# 2) Port.
import constants

# 3) Data
HEX_PREFIX = "0x"
STRICT = "strict"

# 4) Functions
def adjust_base(string, starting_base=16, ending_base=10,
                prefix=HEX_PREFIX):
    """

    adjust_base() -> int

    Function recomputes the string as an integer in the ending_base. Throws a
    PlaceholderError if you try to compute a result other than in base 10.
    """
    result = None
    
    if ending_base != 10:
        c = "I have defined only transformations into base 10."
        raise exceptions.PlaceholderError(c)
    else:
        adj_string = prefix + string
        result = int(adj_string, starting_base)

    return result

def clean_string(string, trace=False, escape=constants.EQUALS,
                 encoding=constants.UTF8):
    """

    clean_string -> string

    Function replaces references to bytes in string with the string equivalents.
    You should replace escaped new lines first, otherwise this will break.
    """
    result = ""
    result = unescape_chars(string, escape=escape)
    
    tokens = get_tokens(result, prefix=escape)

    if trace:
        print("Tokens:   ", tokens)

    lookup = turn_tokens_into_strings(tokens, encoding=encoding)
    
    sorted_keys = sorted(lookup.keys())
    # Non-ordered nature of dictionary complicates debugging. For example, I
    # found a blank key (tuple()). The logic in this function used to translate
    # that into a "=", the same as the escape. As a result, the key would strip
    # out the escapes from the string, effectively ending translation. Depending
    # on where this key fell in the keys() sequence, the translation would end
    # at the beginning, middle, or end of the same string! 
    
    for key in sorted_keys:
        if not key:
            continue
            # Should skip empty keys
            
        adj_key = construct_sequence(key, escape)
        # key is now a tuple, need to put in the escapes back in to detect
        # occurences in the string
        value = lookup[key]
        
        if trace:
                print("Key:      ", key)
                print("Adj. key: ", adj_key)
                print("Value:    ", value)
        
        result = result.replace(adj_key, value)
        
    return result

def construct_sequence(token, escape):
    """

    construct_sequence -> string

    Function returns the string that corresponds to the token. You should use
    a container of strings as the token.
    """
    result = escape + escape.join(token)
    return result

def get_bytes(token, prefix=HEX_PREFIX):
    """

    get_bytes() -> bytestring

    Function changes a token of references into a bytestring. You should use a
    tuple or list of strings as the token, for example ("C5", "A0").
    """
    result = bytes()

    seed = get_integers(token)
    result = bytes(seed)
        
    return result

def get_integers(token, prefix=HEX_PREFIX):
    """

    get_integers -> list

    Function returns a list of integers that correspond to each item in the
    token. 
    """
    result = list()

    for node in token:
        value = adjust_base(node, prefix=prefix)
        result.append(value)

    return result

def get_next(string, prefix, length=2, trace=False):
    """

    get_next() -> (list, string)

    Function picks out the first token from string and returns the remainder of
    the string. Tokens start with the prefix and consist of strings of the
    length you specify. For example, if the prefix is "=", a token might be
    "=A0=C2".

    Function ignores tokens that repeat (e.g., it treats "=3D=3D" as "=3D") but
    treats other tokens that follow each other as one token, to ensure that you
    pick up the bytes necessary to decode a character.
    """
    # goal of this function if to return one token of variable length, as well
    # as the remainder of the string
    result = list()
    remainder = None
    
    skip = len(prefix)
    
    location = string.find(prefix)
    found = False
    if location != -1:
        found = True

    if found:
        start = location + skip
        end = start + length
        token = string[start:end]
        result.append(token)
        remainder = string[end:]

        if remainder and remainder[0] == prefix:
            # next step is also a reference potentially
            next_part = get_next(remainder, prefix, length)
            if trace:
                print(next_part)
                print("\n")
                print("token: ", token)
                print("result: ", result)
                print("next part:  ", next_part[0])
            
            next_tokens = next_part[0]
            if next_tokens and next_tokens[0]!= token:
                result.extend(next_tokens)

            remainder = next_part[1]
        else:
            pass

    return (result, remainder)

def get_tokens(string, prefix, length=2, trace=False):
    """

    get_tokens() -> set

    Function returns a set of tokens in the string that start with the prefix
    you specify. Tokens are tuples of strings.
    """
    result = set()
    rem = string
    while rem:
        token, rem = get_next(rem, prefix, length, trace=trace)
        adj_token = tuple(token)
        result.add(adj_token)

    return result

# OBSOLETE
def locate_references(string, prefix=constants.EQUALS):
    """

    locate_references(string) -> list

    [OBS]

    Returns a list of integers that represent the locations of the handle in the
    string. You should remove newlines from a string before sending.
    """
    result = list()
    i = 0

    while i < length(string):
        if string[i] == prefix:
            result.append(i)
        i = i + 1
    
    return result

def turn_tokens_into_bytes(tokens, prefix=HEX_PREFIX):
    """

    turn_tokens_into_bytes() -> dict
    
    Function returns a mapping of each token to a bytestring. You should input
    an iterable for "tokens."
    """
    result = dict()
    for token in tokens:
        result[token] = get_bytes(token)

    return result

def turn_tokens_into_strings(tokens, prefix=HEX_PREFIX, encoding=constants.UTF8,
                             errors=STRICT):
    """

    turn_tokens_into_strings() -> dict

    Function returns a dictionary of each token mapped to the string it
    represents. 
    """
    result = dict()
    for token in tokens:
        wip = get_bytes(token, prefix=prefix)
        value = wip.decode(encoding=encoding, errors=errors)
        result[token] = value
    return result

def unescape_chars(string, escape=constants.EQUALS, chars=constants.BREAKS,
                   lookup=None):
    """

    unescape_chars() -> string

    Function removes escapes from characters. For example, if you have a string
    where newlines have escapes, you can use this routine to strip the escape
    from the newline without affecting other escaped values.

    If you specify lookup, function will replace the character with the value in
    the lookup. You should provide a dictionary for the lookup.
    """
    result = string
    
    for char in chars:
        query = escape+char
        replacement = char
        if lookup:
            replacement = lookup[char]
            
        result = result.replace(query, replacement)

    return result

s1 = "=C5=A0"
s2 = """
www.dot.la
https://assets.rbl.ms/29294544/origin.jpg
Wednesday=2C February 09 (https://dot.la/dotla-newsletter-2656611745.html)

Despite their decentralized and inherently riskier nature=2C investors are=
 still eager to pour their retirement savings into cryptocurrencies. Repor=
ter Pat Maio looks at the rise of new players seeking to manage such funds=
=E2=80=93and how Los Angeles quickly established itself as an epicenter of=
 the crypto IRA industry.

Here=E2=80=99s what else we=E2=80=99re reading in the news:

- Recent production delays are worrying Rivian investors (https://www.nyti=
mes.com/2022/02/09/business/rivian-stock-electric-cars.html) .

- The WarnerMedia-Discovery merger gets cleared (https://www.thewrap.com/w=
arnermedia-discovery-merger-clears-major-u-s-antitrust-hurdle/) by regulat=
ors.

- Rocket Lab will partner (https://www.businesswire.com/news/home/20220209=
006197/en/Rocket-Lab-Brings-Forward-Launch-for-Earth-Imaging-Company-Synsp=
ective) with Japanese imaging company Syspective for its next mission.

- Cybersecurity startups had a record-breaking year in 2021 (https://techc=
runch.com/2022/02/09/vc-cybersecurity-startups-record-year/) .
The Latest Crypto Investing Craze: Crypto IRAs (https://dot.la/bitcoin-ira=
-2656603452.html)

Despite a rattled market and an uncertain regulatory future=2C cryptocurre=
ncies continue to entrench themselves further in the mainstream (https://d=
ot.la/bitcoin-ira-2656603452.html) . Now=2C the digital asset class has fo=
und relevancy in a new investment market: self-directed individual retirem=
ent accounts=2C or IRAs.
------------------------------------------------------------
Twitter Leads $20 Million Investment Into An LA Crypto Startup  (https://d=
ot.la/opennode-raise-twitter-2656610960.html)

Twitter is putting its money where its mouth is when it comes to the block=
chain=2C backing one of Los Angeles=E2=80=99 most notable crypto startups=
 (https://dot.la/opennode-raise-twitter-2656610960.html) : OpenNode.
------------------------------------------------------------
OC Fintech Lender Hits Unicorn Status  (https://dot.la/happy-money-unicorn=
-status-2656610733.html)

Tustin-based Happy Money=2C a fintech platform that helps borrowers refina=
nce high-interest rate credit card debt=2C has claimed unicorn status=2C a=
nnouncing $50 million in new funding.
------------------------------------------------------------
Endgame Raises $30M to Help Software Sales Teams Analyze Data (https://dot=
=2Ela/endgame-saas-upfront-ventures-2656611634.html)

Since it was founded one year ago=2C Endgame has quickly attracted attenti=
on from venture investors. The company locked down $17 million (https://do=
t.la/endgame-customer-relationship-management-software-2653771331.html) la=
st summer in back-to-back funding rounds. The new Series B announced Wedne=
sday (https://dot.la/endgame-saas-upfront-ventures-2656611634.html) brings=
 its total raised to $47.5 million.
------------------------------------------------------------
=F0=9F=8E=A7 Listen Up:  How Fintech Is Reinventing Financial Infrastructu=
re (https://dot.la/zach-noorani-foundation-capital-2656602318.html)

Traditional banking is changing. On this episode of LA Venture=2C Foundati=
on Capital=E2=80=99s Zach Noorani (https://dot.la/zach-noorani-foundation-=
capital-2656602318.html) talks about the rise of neobanks=2C digital walle=
ts and new models for payment.
------------------------------------------------------------

=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=
=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D=3D
** (http://www.dot.la)
** 2c660c42-5e30-45c5-a1fd-542f9bc2e560.png (https://www.facebook.com/dot.=
losangeles/)
** 6b3a8342-3ff1-4104-b05c-c3feeb985449.png (https://twitter.com/dotla)
** 6b3a8342-3ff1-4104-b05c-c3feeb985449.png (https://instagram.com/dotla)
** 6b3a8342-3ff1-4104-b05c-c3feeb985449.png (https://www.linkedin.com/comp=
any/dot-la/)
** unsubscribe from this list (https://dot.us20.list-manage.com/unsubscrib=
e?u=3Db9409d010687b28f69b43a26a&id=3D5af9b79cc4&e=3D6a1c4c58f7&c=3D4149f434b=
2)
| ** update subscription preferences (https://dot.us20.list-manage.com/pro=
file?u=3Db9409d010687b28f69b43a26a&id=3D5af9b79cc4&e=3D6a1c4c58f7&c=3D4149f4=
34b2)
| ** view email in browser (https://mailchi.mp/a4a15f1d5b4a/1koiwd5b56?e=
=3D6a1c4c58f7)
"""

def run_test(string):
    print("Test")
    print("Input:  ", string)
    output = clean_string(string, trace=True)
    print("Output: ", output)
    print("****")

if __name__ == "__main__":
    run_test(s1)
    run_test(s2)

