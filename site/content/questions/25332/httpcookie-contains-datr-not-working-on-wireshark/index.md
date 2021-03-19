+++
type = "question"
title = "http.cookie contains “datr”  not working on Wireshark"
description = '''Hi guys After sniffing for 10 minutes, I have stopped the process and  when I enter ths ---&amp;gt; http.cookie contains “datr” in the Filter box for search it says  ” http.cookie contains “datr” isn’t a valid display filter: ” ” was unexpected in this context. ” I want to use Wireshark for Facebook Why...'''
date = "2013-09-28T09:56:00Z"
lastmod = "2013-09-28T11:03:00Z"
weight = 25332
keywords = [ "filter", "expressions", "capture-filter", "display-filter", "syntax" ]
aliases = [ "/questions/25332" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [http.cookie contains “datr” not working on Wireshark](/questions/25332/httpcookie-contains-datr-not-working-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25332-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys After sniffing for 10 minutes, I have stopped the process and when I enter ths ---&gt; http.cookie contains “datr” in the Filter box for search it says ” http.cookie contains “datr” isn’t a valid display filter: ” ” was unexpected in this context. ”</p><p>I want to use Wireshark for Facebook</p><p>Why is it wrong?? please reply me quickly</p><p>Thx in advance</p></div><div id="question-tags" class="tags-container tags">filter expressions capture-filter display-filter syntax</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/b8642cf3dd778193c13f3dc8113fffcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Unknown%20Guy&#39;s gravatar image" /><p>Unknown Guy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Unknown Guy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '13, 11:01</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-25332" class="comments-container"><span id="25333"></span><div id="comment-25333" class="comment"><div id="post-25333-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark and what OS? The filter works (or at least doesn't give an error) for me with Wireshark 1.10.2 on Windows 8.1</p></div><div id="comment-25333-info" class="comment-info"><span class="comment-age">(28 Sep '13, 10:58)</span> grahamb ♦</div></div></div><div id="comment-tools-25332" class="comment-tools"></div><div class="clear"></div><div id="comment-25332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25334"></span>

<div id="answer-container-25334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25334-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Possibly you have an odd type of double quotes in the filter box. Just try the plain text <code>http.cookie contains datr</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '13, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-25334" class="comments-container"><span id="32787"></span><div id="comment-32787" class="comment"><div id="post-32787-score" class="comment-score"></div><div class="comment-text"><p>not working it doesnot show the packets after creating the filter http.cookie contains datr</p></div><div id="comment-32787-info" class="comment-info"><span class="comment-age">(14 May '14, 02:10)</span> Lucky Masram</div></div></div><div id="comment-tools-25334" class="comment-tools"></div><div class="clear"></div><div id="comment-25334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

