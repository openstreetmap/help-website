+++
type = "question"
title = "ICMP Data to file"
description = '''In my particular case, someone has been sending a gzip file in 1024-byte increments via data in ICMP (ping). Wireshark doesn&#x27;t seem to have an option to join all those data together, and export to a file. What&#x27;s the best way to do this?'''
date = "2015-09-27T20:10:00Z"
lastmod = "2015-09-28T01:11:00Z"
weight = 46205
keywords = [ "files", "icmp", "ping", "file" ]
aliases = [ "/questions/46205" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP Data to file](/questions/46205/icmp-data-to-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46205-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my particular case, someone has been sending a gzip file in 1024-byte increments via data in ICMP (ping). Wireshark doesn't seem to have an option to join all those data together, and export to a file. What's the best way to do this?</p></div><div id="question-tags" class="tags-container tags">files icmp ping file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '15, 20:10</strong></p><img src="https://secure.gravatar.com/avatar/e6f191759027911fe013fdf7ad998a41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andzerb&#39;s gravatar image" /><p>andzerb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andzerb has no accepted answers">0%</span></p></div></div><div id="comments-container-46205" class="comments-container"><span id="46216"></span><div id="comment-46216" class="comment"><div id="post-46216-score" class="comment-score"></div><div class="comment-text"><p>Could you provide a trace?</p></div><div id="comment-46216-info" class="comment-info"><span class="comment-age">(28 Sep '15, 04:19)</span> Christian_R</div></div></div><div id="comment-tools-46205" class="comment-tools"></div><div class="clear"></div><div id="comment-46205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46209"></span>

<div id="answer-container-46209" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46209-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What's the best way to do this?</p></blockquote><p>scripting with tshark or a TAP with Lua.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '15, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46209" class="comments-container"></div><div id="comment-tools-46209" class="comment-tools"></div><div class="clear"></div><div id="comment-46209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

