function postform(url, fields)
{
	var form = '<form method="post" action="'+url+'">"'+fields+'"</form>';
	$(form).appendTo('body').submit();
}
