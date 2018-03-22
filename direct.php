<?php
include 'config.php';

$func = new LibFunc($argv[1]);

$ret = $func->run((array)json_decode(base64_decode($argv[2])));

echo base64_encode(json_encode($ret));
 ?>
