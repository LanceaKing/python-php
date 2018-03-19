<?php
include 'pycom.php';

define('FUNC_DIR', 'funcs/');

$pc = new PyCom();

try{
  $status = True;
  $call = json_decode($pc->recv(1024));
  include FUNC_DIR.$call->func;
  $ret_data = call_user_func_array($call->func, $call->args);
}catch(Exception $e){
  $status = False;
  $ret_data = $e->getMessage();
}
$data = Array('status' => $status, 'ret_data' => $ret_data);
$pc->send(json_encode($data));
$pc->recv(3);

unset($pc);
 ?>
