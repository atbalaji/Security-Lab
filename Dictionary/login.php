<?php
session_start();
$_SESSION['user']="";
$con = mysqli_connect('127.0.0.1','root','');
if( !$con )
{
echo "Not Connected to Server";
}
if(!mysqli_select_db($con ,"Dictionary"))
{
echo "Not Connected to DB";
}
if( isset( $_POST['sub']) )
{
$name= $_POST['uname'];
$query = "SELECT password FROM users WHERE uname = '$name' ";
$rec = mysqli_query( $con, $query );
$arr=mysqli_fetch_row($rec);
$password=$arr[0];
$query="python dictionary_attack.py ".$password;
$queryReturnValue = system($query,$retval);
}
?>

<!DOCTYPE html>
<html>
<head>
<title>Dictionary Attack</title>
</head>
<body>
<form method="post" action="#">
<label>Username</label>
<input type="text" name="uname" id="uname">
<br>
<button name="sub">Login</button>
</form>
</body>
</html>
