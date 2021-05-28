import os
import re
import string
from collections import Counter
import json

literals = []
fuzzy_bytes = []

def get_leterals_hex():
    return [hex(num) for num in range(0x0, 0xff) if num in range(0x30, 0x3a) or num in range(0x41,0x5b) or num in range(0x61,0x7a)]

def get_hex_exclude_literals(strip_zero=False, add_slash=False, ex_literals=False):
    if ex_literals:
        literals = get_leterals_hex()
        if strip_zero:
            if add_slash:
                return ["\\" + str(hex(num).lstrip("0")) for num in range(0x0,0x100) if hex(num) not in literals]
            else:
                return [str(hex(num).lstrip("0")) for num in range(0x0,0x100) if hex(num) not in literals]
        elif add_slash:
            return ["\\" + str(hex(num)) for num in range(0x0,0x100) if hex(num) not in literals] 
        return [str(hex(num)) for num in range(0x0,0x100) if hex(num) not in literals]
    else:
        if strip_zero:
            if add_slash:
                return ["\\" + str(hex(num).lstrip("0")) for num in range(0x0,0x100) if hex(num)]
            else:
                return [str(hex(num).lstrip("0")) for num in range(0x0,0x100) if hex(num)]
        elif add_slash:
            return ["\\" + str(hex(num)) for num in range(0x0,0x100) if hex(num)] 
        return [str(hex(num)) for num in range(0x0,0x100) if hex(num)]

fuzzy_bytes = get_hex_exclude_literals()
# fuzzy_bytes.extend("\\" + str(hex(num)) for num in range(0x0,0x10))

famale_names = ["Mary", "Jessie", "Molly", "Anna", "Elsa", "Carolina", "Victoria", "Angela", "Nicole", "Jackie", "Sarah", "Chloe", "Charlotte", "Cora", "Eva"]
male_names = ["Alex", "Mark", "Robert", "Thomas", "Charles", "Matt", "Andrew", "Dean", "Samuel", "Clark", "Steven", "Paul", "Sean", "Harry", "Ross", "Chandler"]
ages = [num for num in range(5,90) if num] # from 5 yo to 90 yo
emails = ["mary@m.com", "copy@m.com", "salut@l.com", "shshsh@l.net", "peppy@a.ru", "roll@r.com", "look@u.uk", "bonjour@b.fr", "hello@world.hey", "bytes@dont.lie"]

# loop to generate different data types filled with the above data randomly
messages = [
    {"sender": "Mark",
    "receiver": "Molly",
    "message": "Hello"},
    {"sender": "Mark",
    "receiver": "Jassie",
    "message": "Hello"},
    {"sender": "Jessie",
    "receiver": "Mark",
    "message": "Hello"},
    {"sender": "Jessie",
    "receiver": "Molly",
    "message": "Hello"},
    {"sender": "Jessie",
    "receiver": "Molly",
    "message": "Hello"},
    {"sender": "Jessie",
    "receiver": "Mark",
    "message": "Hello"},
    {"sender": "Jessie",
    "receiver": "Mark",
    "message": "Hello"},
    {"sender": "Jessie",
    "receiver": "Mark",
    "message": "Hello"},
    {"sender": "Jessie",
    "receiver": "Mark",
    "message": "Hello"}
]

candidates = [
  {"name": "Matt",
   "age": 17,
   "score": 1
  },
  {"name": "Matt",
   "age": 17,
   "score": 1
  },
  {"name": "Mark",
   "age": 90,
   "score": 1
  },
  {"name": "Mark",
   "age": 90,
   "score": 1
  },  
  {"name": "Matt",
   "age": 17,
   "score": 1
  },
  {"name": "Lucie",
   "age": 19,
   "score": 1
  },
  {"name": "Matt",
   "age": 17,
   "score": 1
  },
  {"name": "Matt",
   "age": 17,
   "score": 1
  },
   {"name": "Lucie",
   "age": 19,
   "score": 1
  },
   {"name": "Lucie",
   "age": 19,
   "score": 1
  },
   {"name": "Lucie",
   "age": 19,
   "score": 1
  },
  {"name": "Matt",
   "age": 17,
   "score": 1
  },
  {"name": "Michael",
   "age": 19,
   "score": 1
  },
  {"name": "Matt",
   "age": 17,
   "score": 1
  },
  {"name": "Linda",
   "age": 24,
   "score": 1
  },
  {"name": "Linda",
   "age": 24,
   "score": 1
  },
  {"name": "Michael",
   "age": 19,
   "score": 1
  },
  {"name": "Michael",
   "age": 19,
   "score": 1
  },
  {"name": "Linda",
   "age": 24,
   "score": 1
  },
  {"name": "Mark",
   "age": 90,
   "score": 1
  }  
]

kpi = Counter([x["receiver"] for x in messages])
print(kpi.most_common(3))


scores_hashtable = Counter([x["name"] for x in candidates])
sorted_scores_table = sorted(scores_hashtable.items(), key=lambda x: x[1], reverse=True)