+++
type = "question"
title = "reassembling data from two or more packages for c dissector"
description = '''Hello, I have a problem to reassemble data of my dissector in c. My protocols is above the Ethernet. The dissector is called with dissector_add_uint on a &quot;ethertype&quot; The protocol contains of a header and a payload area. An here comes the problem, the data can be split in more than one package. What ...'''
date = "2013-11-19T10:05:00Z"
lastmod = "2013-11-20T07:36:00Z"
weight = 27106
keywords = [ "reassembly", "dissector" ]
aliases = [ "/questions/27106" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [reassembling data from two or more packages for c dissector](/questions/27106/reassembling-data-from-two-or-more-packages-for-c-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27106-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a problem to reassemble data of my dissector in c. My protocols is above the Ethernet. The dissector is called with dissector_add_uint on a "ethertype"</p><p>The protocol contains of a header and a payload area. An here comes the problem, the data can be split in more than one package.</p><p>What I want is that I collect all the data and then send it to another dissector. Is this possible with customs dissectors?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">reassembly dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '13, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/9b1dc01f2575b09d0852f7a4245a0318?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gatherer&#39;s gravatar image" /><p>Gatherer<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gatherer has no accepted answers">0%</span></p></div></div><div id="comments-container-27106" class="comments-container"></div><div id="comment-tools-27106" class="comment-tools"></div><div class="clear"></div><div id="comment-27106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27164"></span>

<div id="answer-container-27164" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27164-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at conversation interface.</p><p>I had the same problem, you can find my post here: <a href="http://ask.wireshark.org/questions/23894/passing-data-between-packets-and-not-between-dissectors">http://ask.wireshark.org/questions/23894/passing-data-between-packets-and-not-between-dissectors</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p>Afrim<br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-27164" class="comments-container"><span id="27203"></span><div id="comment-27203" class="comment"><div id="post-27203-score" class="comment-score"></div><div class="comment-text"><p>thanks .. that is what I was looking for</p></div><div id="comment-27203-info" class="comment-info"><span class="comment-age">(21 Nov '13, 01:30)</span> Gatherer</div></div></div><div id="comment-tools-27164" class="comment-tools"></div><div class="clear"></div><div id="comment-27164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

