from gunicorn.app.base import Application

class RemotePyServer:
	def run(self, app, host='192.168.1.7', port=5000, workers=1, threads=2):
	    class FlaskApplication(Application):
	        def init(self, parser, opts, args):
	            return {
	                'bind': '{0}:{1}'.format(host, port),
	                'workers': workers,
	                'threads': threads
	            }

	        def load(self):
	            return app

	    FlaskApplication().run()


if __name__ == "__main__":
	from app import app
	server = RemotePyServer()
	server.run(app)