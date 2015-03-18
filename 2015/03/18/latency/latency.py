#!/usr/bin/python
"RED (random early drop) simple implementation"
import random


def request_ok(current, th_min, th_max):
    """return OK with a probability proportional to
       'low' current, between th_min and th_max

    request_ok()  |
                  |
      FALSE       |          /
    ---------------         +
      TRUE 25%    -        /
           ...    |       /
      TRUE 50% - - - - - -
           ...    |     /:
      TRUE 75%    -    / :
    --------------|   +  :
      TRUE        |  /   :
                  | /    :
                  +---|--|--|--------------
                      |  |  th_max
                      |  current
                      th_min
    e.g. for current in the middle between th_min, th_max
    randomly return TRUE half of the time
    """
    return random.uniform(th_min, th_max) > current