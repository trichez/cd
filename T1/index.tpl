
<hmtl>
	<form action="http://localhost:8080/chat" method="POST" style="float:left;">
		Username: <input name="username" type="text"/><br>
		Message: <input name="msg" type="text"/><br>
		<input value="Send" type="submit" />
	</form>

	
	<table>
	% for msg in data:
	  <tr style="bgcolor="#FFFF00">
		<td>{{msg['sender']}} </td>
		<td>{{msg['msg']}}</td>
	  </tr>
	% end
	</table>


</hmtl>
