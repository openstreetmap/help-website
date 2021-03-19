+++
type = "question"
title = "How to identify packets"
description = '''Can column number be read? I need to identify packets with some unique identifier. Since packets are dissected more than once in some cases it would be nice to know when the same packet has come back. In wireshark you see &quot;packet number&quot; as the first column but I don&#x27;t know how to access this number...'''
date = "2015-01-15T13:23:00Z"
lastmod = "2015-01-15T13:52:00Z"
weight = 39175
keywords = [ "dissector", "packets", "tcp", "packet", "id" ]
aliases = [ "/questions/39175" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to identify packets](/questions/39175/how-to-identify-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39175-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can column number be read?</p><p>I need to identify packets with some unique identifier. Since packets are dissected more than once in some cases it would be nice to know when the same packet has come back. In wireshark you see "packet number" as the first column but I don't know how to access this number in a function. Presumably, just being able to know that would be great; I could tell which packet was which from just that information. However, any other identifier would work too; is there some kind of read column function (TCP)? I'm working with the dissector, I can't just use filter options.</p></div><div id="question-tags" class="tags-container tags">dissector packets tcp packet id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/ca562b18c08fc77caf70657719e1629f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicole_identity&#39;s gravatar image" /><p>nicole_identity<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicole_identity has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jan '15, 13:28</p></div></div><div id="comments-container-39175" class="comments-container"></div><div id="comment-tools-39175" class="comment-tools"></div><div class="clear"></div><div id="comment-39175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39176"></span>

<div id="answer-container-39176" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39176-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @grahamb told you in <a href="https://ask.wireshark.org/questions/39168/revisiting-in-split-packages">your previous thread</a>, you can check whether a packet was already seen thanks to the PINFO_FD_VISITED(pinfo) macro (=0 when packet is seen for the first time, 1 for all subsequent decodings).</p><p>If you really need it, frame number can be retrieved by PINFO_FD_NUM(pinfo) macro.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '15, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39176" class="comments-container"></div><div id="comment-tools-39176" class="comment-tools"></div><div class="clear"></div><div id="comment-39176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

