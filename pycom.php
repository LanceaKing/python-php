<?php
class PyCom{
  private $socket = NULL;
  function __construct($port=31337){
    $this->socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    socket_connect($this->socket, 'localhost', $port);
    $this->send('RDY');
  }
  function __destruct(){
    socket_close($this->socket);
  }
  public function send($data){
    socket_write($this->socket, $data, strlen($data));
  }
  public function recv($size){
    return socket_read($this->socket, $size);
  }
}
 ?>
