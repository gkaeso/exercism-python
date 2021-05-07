NORTH, SOUTH, EAST, WEST = 1, 2, 3, 4


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction: int = direction
        self.coordinates: tuple[int, int] = x, y

    def move(self, actions: str):
        for action in actions: self._do_action(action)

    def _do_action(self, action):
        return {'R': self._turn_right, 'L': self._turn_left, 'A': self._advance}[action]()

    def _turn_left(self) -> None:
        self.direction = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}[self.direction]

    def _turn_right(self) -> None:
        self.direction = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}[self.direction]

    def _advance(self) -> None:
        if self.direction == NORTH:
            self.coordinates = self.coordinates[0], self.coordinates[1]+1
        elif self.direction == SOUTH:
            self.coordinates = self.coordinates[0], self.coordinates[1]-1
        elif self.direction == WEST:
            self.coordinates = self.coordinates[0]-1, self.coordinates[1]
        elif self.direction == EAST:
            self.coordinates = self.coordinates[0]+1, self.coordinates[1]
        else:
            raise ValueError('invalid direction')
