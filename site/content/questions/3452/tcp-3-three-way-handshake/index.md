+++
type = "question"
title = "TCP 3 three way handshake"
description = '''I have captured my personal network through wireshark.. now i want to know the TCP three-way-shandshake information. Where do i go and how to filter the TCP three-way-handshake. Thank'''
date = "2011-04-11T13:16:00Z"
lastmod = "2011-04-11T14:06:00Z"
weight = 3452
keywords = [ "meow" ]
aliases = [ "/questions/3452" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP 3 three way handshake](/questions/3452/tcp-3-three-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3452-score" class="post-score" title="current number of votes">0</div><span id="post-3452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captured my personal network through wireshark.. now i want to know the TCP three-way-shandshake information. Where do i go and how to filter the TCP three-way-handshake. Thank</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-meow" rel="tag" title="see questions tagged &#39;meow&#39;">meow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '11, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/837927f1c9adfe4589641435c5fa0577?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kv2004&#39;s gravatar image" /><p><span>kv2004</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kv2004 has no accepted answers">0%</span></p></div></div><div id="comments-container-3452" class="comments-container"></div><div id="comment-tools-3452" class="comment-tools"></div><div class="clear"></div><div id="comment-3452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3454"></span>

<div id="answer-container-3454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3454-score" class="post-score" title="current number of votes">1</div><span id="post-3454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The easy way is to right click a packet in a stream and choose follow tcp stream. The three way handshake will be the first three packets, unless there are issues. You could get creative and display filter something like--</p><p>((tcp.flags == 0x02) || (tcp.flags == 0x12) ) || ((tcp.flags == 0x10) &amp;&amp; (tcp.ack==1) &amp;&amp; (tcp.len==0))</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-3454" class="comments-container"></div><div id="comment-tools-3454" class="comment-tools"></div><div class="clear"></div><div id="comment-3454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

