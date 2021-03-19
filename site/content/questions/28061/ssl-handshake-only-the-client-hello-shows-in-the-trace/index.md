+++
type = "question"
title = "SSL Handshake - only the Client Hello shows in the trace"
description = '''I am tracing traffic between an iPhone and our Exchange server. When the iPhone syncs, Wireshark shows only the Client Hello. The remainder of the handshake does not show. I know the handshake is successful and that encrypted data is passed because email is synced, and Schannel Event ID 36880 &quot;An SS...'''
date = "2013-12-12T11:22:00Z"
lastmod = "2013-12-12T12:46:00Z"
weight = 28061
keywords = [ "handshake" ]
aliases = [ "/questions/28061" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Handshake - only the Client Hello shows in the trace](/questions/28061/ssl-handshake-only-the-client-hello-shows-in-the-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28061-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am tracing traffic between an iPhone and our Exchange server. When the iPhone syncs, Wireshark shows only the Client Hello. The remainder of the handshake does not show. I know the handshake is successful and that encrypted data is passed because email is synced, and Schannel Event ID 36880 "An SSL server handshake completed successfully" is generated soon after the Client Hello.</p><p>What am I missing?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">handshake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/4660ac99c7ac8e29c3d3f82fe5a41dd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sejong&#39;s gravatar image" /><p>sejong<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sejong has no accepted answers">0%</span></p></div></div><div id="comments-container-28061" class="comments-container"></div><div id="comment-tools-28061" class="comment-tools"></div><div class="clear"></div><div id="comment-28061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28064"></span>

<div id="answer-container-28064" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28064-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps partially answering my own question - the behavior I posted was when the iPhone was connected to the Internet via the cellular data network (Verizon, in this case). I retried it with the iPhone connected to the Internet via WiFi - all the expected elements of the handshake appeared in the Wireshark trace.</p><p>Update - The previous WiFi connection was internal. A WiFi connection routed via the Internet has the same behavior as over the cellular data network.</p><p>Typical details: Frame 1 is from the iPhone to the server, SSL protocol, destination port is 443 (this is the Client Hello) Frame 2 is from the iPhone to the server, TCP protocol, destination port is 443 Frame 3 is from the server to the iPhone, TCP protocol, source port is 443 Frame 4 is from the iPhone to the server, TCP protocol, destination port is 443</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '13, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/4660ac99c7ac8e29c3d3f82fe5a41dd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sejong&#39;s gravatar image" /><p>sejong<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sejong has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Dec '13, 16:57</p></div></div><div id="comments-container-28064" class="comments-container"></div><div id="comment-tools-28064" class="comment-tools"></div><div class="clear"></div><div id="comment-28064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

