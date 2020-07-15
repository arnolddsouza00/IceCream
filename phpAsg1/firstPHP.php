<?php
$n1=$_POST["n1"];
$n2=$_POST["n2"];
$flag = 0;
$count = 0;
echo "Prime numbers between " . $n1 . " and " . $n2 . " are: <br>";
for($i = $n1; $i <= $n2; $i++) {
  if ($i >= 2) {
    $flag = 0;
    for($j = 2; $j <= $i/2; $j++) {
      if($i % $j == 0) {
        $flag = 1;
        break;
      }
    }
    if ($flag == 0) {
      $count += 1;
      echo $i."\n";
    }
  }
  else {
    continue;
  }
}
echo "<br><br>Total " . $count . " prime numbers."
?>
