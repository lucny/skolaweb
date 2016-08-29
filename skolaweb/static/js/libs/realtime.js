var Aldryn = Aldryn || {};

Aldryn.Realtime = Klass()({
	'__init__': function(self, options){
		self.key = options.key;
		self.uri = options.uri;
		self.channel = options.channel;
		self.session = null;
		self.connect();
	},
	'connect': function(self){
		try {
			ab.connect(self.uri, self.session_established, self.session_gone);
		} catch(err) {
			// catching Websocket's insecure connection exception (https with insecure websocket)
			if (window.console.log) {
				window.console.log(err.name + '\n' + err.message);
			};
		};
	},
	'session_established': function(self, session){
		self.session = session
		self.session.call('authenticate', self.key).then(self.session_authenticated, self.authentication_failed);
	},
	'session_gone': function(self, code, reason){
		self.session = null;
	},
	'session_authenticated': function(self){
		self.subscribe();
	},
	'authentication_failed': function(self){

	},
	'subscribe': function(self){
		self.session.subscribe(self.channel, self.on_message);
	},
	'on_message': function(self, topic, event){

	}
});
