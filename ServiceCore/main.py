from flask import Flask, request
from ServiceCore.LatestGameEndPoint.LiveGamesRepository import LiveGamesRepository

app = Flask(__name__)


@app.route('/')
def hello():
    print("I am here")
    user_agent = request.headers.get('User-Agent')
    return 'Hello! I see you are using %s' % user_agent


@app.route("/getLatestGames")
def get_latest_games():
    live_games_repo = LiveGamesRepository()
    json_response = live_games_repo.get_latest_games(None)

    response = app.response_class(
        response=json_response,
        status=200,
        mimetype='application/json'
    )

    return response


def main():
    print("program is up and running")


if __name__ == "__main__":
    main()
    app.run("127.0.0.1", 5000, True)
