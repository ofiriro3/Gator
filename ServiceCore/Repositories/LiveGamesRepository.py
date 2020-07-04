from flask import json


class LiveGamesRepositoryInterface:

    def get_latest_games(self, parameters: dict) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass


class LiveGamesRepository(LiveGamesRepositoryInterface):

    # Need to address another service and asks for the current games
    def get_latest_games(self, parameters):
        latest_games_mocked_response = {
            "game_id": "12345",
            "active": "false",
            "Team_A_name": "Team_A_name",
            "Team_B_name": "Team_B_name",
            "Team_A_score": "1",
            "Team_B_score": "2",
        }

        return json.dumps(latest_games_mocked_response)
