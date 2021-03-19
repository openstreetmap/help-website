+++
type = "question"
title = "weird windows copy behaviour"
description = '''I have a problem with a very slow copy action from a window 2003 server to an XP workstation. In the trace of the workstation large delays of 1 second are seen for retransmissions. What happens is that 2 lost segments are encountered. The XP workstation sends one duplicate ack (so 2 ack all together...'''
date = "2012-07-20T03:22:00Z"
lastmod = "2012-07-20T03:34:00Z"
weight = 12880
keywords = [ "windows", "xp", "copy" ]
aliases = [ "/questions/12880" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [weird windows copy behaviour](/questions/12880/weird-windows-copy-behaviour)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12880-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a problem with a very slow copy action from a window 2003 server to an XP workstation.</p><p>In the trace of the workstation large delays of 1 second are seen for retransmissions. What happens is that 2 lost segments are encountered. The XP workstation sends one duplicate ack (so 2 ack all together) but not any more. After this it takes 1 second for the server to do a retransmission.</p><p>Copying from another server doesn't give any problems. There are also lost segments, but enough multiple acks.</p><p>Can anybody explain why the workstation stops after sending one duplicate ack ??</p></div><div id="question-tags" class="tags-container tags">windows xp copy</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '12, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/fa842ad48d99c642a22081fcacada9c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="easterman&#39;s gravatar image" /><p>easterman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="easterman has no accepted answers">0%</span></p></div></div><div id="comments-container-12880" class="comments-container"></div><div id="comment-tools-12880" class="comment-tools"></div><div class="clear"></div><div id="comment-12880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12881"></span>

<div id="answer-container-12881" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12881-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You did not mention if the server also stops sending. The client will only send a DUP ack for each segment it receives after missing a segment. So if the server stops sending (maybe because the second lost packet was the final packet of a higher layer PDU), then the client will not be able to send DUP acks and the normal retransmission timer of the server kicks in. Which results in the larger delay.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '12, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12881" class="comments-container"></div><div id="comment-tools-12881" class="comment-tools"></div><div class="clear"></div><div id="comment-12881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

