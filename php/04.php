<?php
// "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ

// $str1 = "paraparaparadise";
// $str2 = "paragraph";

function word_ngram_fast($sentence, $n)
{
    $pos = [-1];
    $curr = 0;
    while (($curr = strpos($sentence, ' ', $curr)) !== false) {
        $pos[] = $curr++;
    }
    $pos[] = strlen($sentence);

    print_r($pos,true);

    $ngram = [];
    for ($i = 0; $i < count($pos) - $n; ++$i) {
        $start = $pos[$i] + 1;
        $end = $pos[$i + $n] - 1;
        $ngram[] = substr($sentence, $start, $end - $start + 1);
    }

    return $ngram;
}

$str = "I am an NLPer";
$array = word_ngram_fast($str, 2);
print(' array');
print_r($array, true);