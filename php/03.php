<?php
$str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
$wordList = preg_split('/[\s,.]+/', $str);
$wordCntList = [];
foreach ($wordList as $word) {
    if (strlen($word) > 0) { #これがないとピリオド分割した時に最後の文字に空文字が入る
        $wordCntList[] = strlen($word);
    }
}
print_r($wordCntList);