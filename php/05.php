<?php
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

function ngram($target, $n)
{
    $result = [];
    for($i=0; $i<count($target)-$n+1; ++$i) {
        $result[] = array_slice($target, $i, $n);
    }
    return $result;
}

#こっちの方が処理速度は速い
function word_ngram_fast($sentence, $n)
{
    $pos = [-1];
    $curr = 0;
    while (($curr = strpos($sentence, ' ', $curr)) !== false) {
        $pos[] = $curr++;
    }
    $pos[] = strlen($sentence);

    $ngram = [];
    for ($i = 0; $i < count($pos) - $n; ++$i) {
        $start = $pos[$i] + 1;
        $end = $pos[$i + $n] - 1;
        $ngram[] = substr($sentence, $start, $end - $start + 1);
    }

    return $ngram;
}

$target = "I am an NLPer";
$words = explode(' ', $target);
$result = ngram($words, 2);
print_r(json_encode($result));
print("\n");

$charas = str_split($target);
$result = ngram($charas, 2);
print_r(json_encode($result));
print("\n");

print("fast\n");
$word_ngram_fast = word_ngram_fast($target, 2);
print_r(json_encode($word_ngram_fast));
print("\n");