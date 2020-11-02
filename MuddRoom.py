#Stewbaloo
#october 2020
#This file contains class and function definitions pertaining to rooms in the mudd

class NPC:
    """This is a class for creating non-player characters, which can be hostile, neutral, or friendly,
    have stats like characters, and possibly equipment"""

class RoomFeat:
    """An object for storing the features of a location, such as objects (visible or hidden), creatures,
    routes out of the room (in open spaces this is limitted to the 8 cardinal directions, though there can be portals
    also contains functions such as, look_around(), which returns a list of the visible objects and any clues
    to finding the hidden objects
    """

class MuddRoom:
    """A MuddRoom is a room for the text based adventure game.
    it has a name, an (x,y) location, a description, and a RoomFeat which is an object
    that contains all the interactable and observoble aspects of the room, including exits"""
    #The rooms have locations based on a standard x,y coordinate system that does not consider room size
    # so every room/location is assumed to be roughly the same size
    #Should the location simply be stored by the rooms location in the list of rooms? right now no

    def __init__(self, name = "empty room", x_loc = 0, y_loc = 0, description = "You see an empty room", features = RoomFeat()):
        """initializes a new room, takes (respectively) name, x location, y location, description, and features
        features should be a RoomFeat object containing all the interactable things in the room
        """
        self._name = name
        self._x = x_loc
        self._y = y_loc
        self._txt = description
        self._features = features

