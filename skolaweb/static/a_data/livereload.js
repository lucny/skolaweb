LiveReload = Klass(Aldryn.Realtime)({
	'__init__': function(self, options){
		self.logged_user_email = options.logged_user_email;
		$.get(options.credential_url, function(credentials){
			self.key = credentials.key;
			self.uri = credentials.uri;
			self.channel = credentials.channel;
			self.session = null;
			self.connect();
			self.timers = null;
		});
	},
	'on_message': function(self, topic, event){
		var filepath = event.purge,
			reload = function() {
				window.parent.location.reload(true);
			};
		if (filepath.indexOf('templates/') === 0 ||
				filepath.indexOf('.js') !== -1){
			clearTimeout(self.timer);
			self.timer = setTimeout(reload, 500);
		} else {
			$("link[href*='" + filepath + "']", window.parent.document).each(function(i, obj) {
				var oldHref = $(obj).attr('href');
				oldHref = oldHref.split('?')[0];
				$(obj).attr('href', oldHref + '?' + new Date().getTime());
			});
		}
	}
});
