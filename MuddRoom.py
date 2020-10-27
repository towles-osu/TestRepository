#Stewbaloo
#october 2020
#This file contains class and function definitions pertaining to rooms in the mudd

class RoomFeat:
    """An object for storing the features of a location"""

class MuddRoom:
    """A MuddRoom is a room for the text based adventure game."""
    #The rooms have locations based on a standard x,y coordinate system that does not consider room size
    # so every room/location is assumed to be roughly the same size

    def __init__(self, name = "empty room", x_loc = 0, y_loc = 0, description = "You see an empty room", features = RoomFeat()):
        """initializes a new room, takes (respectively) name, x location, y location, description, and features
        features should be a RoomFeat object containing all the interactable things in the room
        """
        self._name = name
        self._x = x_loc
        self._y = y_loc
        self._txt = description
        self._features = features

