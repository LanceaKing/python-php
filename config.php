<?php

// ref https://zhidao.baidu.com/question/691583631801759684.html

class LibFunc extends ReflectionFunction
{
  const FUNC_DIR = 'libs/';
  const COMMON_FUNC_NAME = 'libfunc';

  private $func_name = '';

  function __construct($func_name){
    $this->func_name = basename($func_name);
    include self::FUNC_DIR . $this->func_name . '.php';
    parent::__construct(self::COMMON_FUNC_NAME);
  }

  public function run($params){
    if(!is_array($params))
      $params = [$params];
    $depend = array();
    foreach($this->getParameters() as $v){
      if(isset($params[$v->name])){
          $depend[] = $params[$v->name];
      }elseif($v->isDefaultValueAvailable()){
          $depend[] = $v->getDefaultValue();
      }else{
          throw new Exception("Losing param '{$v->name}'");
      }
    }
    return call_user_func_array(self::COMMON_FUNC_NAME, $depend);
  }
}
 ?>
