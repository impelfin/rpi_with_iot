<html>
<head>
<title>bottle-Sqlite Test</title>
</head>
<body>
<div style="padding-top:20px;">
<table border> 
<tr>
	<th>Id</th>
	<th>Name</th>
	<th>Birthday</th>
	<th>Gender</th>
</tr>
% for item in items:
	<tr>
	% for column in item:
		<td>{{column}}</td>
	% end
	</tr>
% end
</table>
</div> 
</body>
</html>
