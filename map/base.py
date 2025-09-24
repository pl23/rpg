import json


class game_map:
    def load_map(self, path):
        """Loads map data from a JSON file."""
        self.path = path
        try:
            with open(path, "r") as f:
                data = json.load(f)["data"]["map"]
                self.map_data = data["map_data"]
                self.mapId = data["mapId"]
                self.mapName = data["mapName"]
        except (FileNotFoundError, KeyError) as e:
            print(f"Error loading map: {e}")
            
    def __init__(self, map = [[{}]], path = ""):
        self.map = map
        self.path = path
        self.mapId = 0
        if path != "":
            self.load_map(path)


    def save_map(self, path):
        """Saves map data to a JSON file."""
        self.path = path
        with open(path, "w") as f:
            json_data = {
                "data": {
                    "map": {
                        "mapId": self.mapId,
                        "mapName": self.mapName,
                        "map_data": self.map_data
                    }
                }
            }
            json.dump(json_data, f, indent=4)



class view_port_class:
    """
    Manages a view of a portion of the game map, using distinct
    attribute names to avoid confusion with the map's coordinates.
    """
    def __init__(self, game_map_instance):
        self.map_source = game_map_instance # Use a clear name for the map instance
        self.view_port = [[{}]]
        self.view_port_x = 0
        self.view_port_y = 0
        self.view_port_width = 10
        self.view_port_height = 10

    def update_view_port(self, x, y, width, height):
        """
        Updates the viewport's position and dimensions and
        populates its data from the map.
        """
        self.view_port_x = x
        self.view_port_y = y
        self.view_port_width = width
        self.view_port_height = height

        # Re-initialize the viewport with the new size
        self.view_port = [[{} for _ in range(self.view_port_width)] for _ in range(
            self.view_port_height
        )]

        for i in range(self.view_port_height):
            for j in range(self.view_port_width):
                map_y = self.view_port_y + i
                map_x = self.view_port_x + j
                try:
                    self.view_port[i][j] = self.map_source.map_data[map_y][map_x]
                except IndexError:
                    self.view_port[i][j] = {} # Out of bounds


class entity_port_class(view_port_class):
    def __init__(self, game_map_instance):
        super().__init__(game_map_instance)

    def update_entity(self, x, y, state):
        pass
