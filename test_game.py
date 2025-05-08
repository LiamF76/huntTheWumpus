import unittest
import game

class TestWumpusGame(unittest.TestCase):

    def test_valid_move(self):
        self.assertTrue(game.is_valid_move(1, 2))
        self.assertFalse(game.is_valid_move(1, 3))

    def test_check_hazard(self):
        self.assertEqual(game.check_hazard(5, 5, [2, 3]), "wumpus")
        self.assertEqual(game.check_hazard(2, 5, [2, 3]), "pit")
        self.assertEqual(game.check_hazard(4, 5, [2, 3]), "safe")

    def test_generate_locations(self):
        player, wumpus, pits, bats = game.generate_locations(seed=42)
        locations = [player, wumpus] + pits + bats
        self.assertEqual(len(set(locations)), 6)
        self.assertIn(player, range(1, 21))
        self.assertNotIn(wumpus, [player])
        self.assertEqual(len(pits), 2)
        self.assertEqual(len(bats), 2)

    def test_move_player_valid(self):
        self.assertEqual(game.move_player(1, 2), 2)

    def test_move_player_invalid(self):
        self.assertEqual(game.move_player(1, 3), 1)

    def test_bat_transport(self):
        new_room = game.bat_transport(1, seed=99)
        self.assertIn(new_room, range(1, 21))
        # Result will be deterministic because of seed
        self.assertEqual(new_room, 4)

if __name__ == '__main__':
    unittest.main()
