<?php
    //database name = "simple_ajax"
    //table name = "users"
    $con = mysql_connect("localhost","root","");
    $dbs = mysql_select_db("simple_ajax",$con);
    $result= mysql_query("select * from users");
    $array = mysql_fetch_row($result);
?>