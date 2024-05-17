import os
import sumo_rl
from sumo_rl import env, parallel_env
# PATH = os.path.dirname(sumo_rl.__file__)
PATH = '/home/mrprodigy01/Documents/Final-Run/'

def amman9(parallel=True, **kwargs):
    """Amman 9 network.

    Number of agents: 9
    Number of actions: variable
    """
    kwargs.update(
        {
            "net_file": PATH + "osm.net.xml.gz",
            "route_file": PATH + "osm.passenger.trips.xml",
            "begin_time": 10,
            "num_seconds": 5000,
        }
    )
    if parallel:
        return parallel_env(**kwargs)
    else:
        return env(**kwargs)
    

def uni_area(parallel=True, **kwargs):
    """University of Jordan Area

    Number of agents: 9
    Number of actions: variable
    """
    kwargs.update(
        {
            "net_file": PATH + "uni-area2/osm.net.xml.gz",
            "route_file": PATH + "uni-area2/osm.passenger.trips.xml",
            "begin_time": 0,
            "num_seconds": 7000,
        }
    )
    if parallel:
        return parallel_env(**kwargs)
    else:
        return env(**kwargs)


def seventh_area(parallel=True, **kwargs):
    """Seventh Intersection Area

    Number of agents: 1
    Number of actions: variable
    """
    kwargs.update(
        {
            "net_file": PATH + "7th-area/osm.net.xml.gz",
            "route_file": PATH + "7th-area/osm.passenger.trips.xml",
            "begin_time": 0,
            "num_seconds": 5000,
        }
    )
    if parallel:
        return parallel_env(**kwargs)
    else:
        return env(**kwargs)
