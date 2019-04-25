<?php
// "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ

function ngram($target, $n)
{
    $result = [];
    for($i=0; $i<count($target)-$n+1; ++$i) {
        $result[] = array_slice($target, $i, $n);
    }
    return $result;
}

$str1 = "paraparaparadise";
$str2 = "paragraph";

$charas1 = str_split($str1);
$charas2 = str_split($str2);

$X = ngram($charas1, 2);
$Y = ngram($charas2, 2);
// 配列の要素ごとにimplodeを適用させてマッピング
$X = array_map('implode', $X);
$Y = array_map('implode', $Y);
// この時点では集合の重複が考えられる
// array_flipでキーと要素を反転させることで重複をなくす(反転してキーが重複する場合は上書きされる)
// $X = array_flip($X);
// $Y = array_flip($Y);

// とサイトではやってたけどarray_uniqueでいいやん
$X = array_unique($X);
$Y = array_unique($Y);

print_r(json_encode($X));
print("\n");
print_r(json_encode($Y));
print("\n");
print_r(json_encode(array_merge($X, $Y)));
print("\n");
print_r(json_encode(array_intersect($X, $Y)));
print("\n");
print_r(json_encode(array_diff($X, $Y)));