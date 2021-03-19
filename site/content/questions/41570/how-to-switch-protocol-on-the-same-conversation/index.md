+++
type = "question"
title = "how to switch protocol on the same conversation"
description = '''Hi, I have a proprietary protocol (tcp transport layer) that starts (on the same connection ie. same port ) before an underlying known protocol such as HTTP. Is there a way to dissect the the proprietary protocol and than let wireshark to continue dissecting it as the underlying protocol? I am using...'''
date = "2015-04-19T04:30:00Z"
lastmod = "2015-04-19T04:30:00Z"
weight = 41570
keywords = [ "lua", "dissector", "proprietary" ]
aliases = [ "/questions/41570" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to switch protocol on the same conversation](/questions/41570/how-to-switch-protocol-on-the-same-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a proprietary protocol (<strong>tcp transport layer</strong>) that starts (<strong>on the same connection</strong> ie. same port ) before an underlying known protocol such as HTTP. Is there a way to dissect the the proprietary protocol and than let wireshark to continue dissecting it as the underlying protocol? I am using lua. Thanks</p><p>addition On application layer... My protocol dissects on port 8080, and get some info from proprietary protocol then it should switch to HTTP and continue to work as usual till the and of the stream (conversation).</p></div><div id="question-tags" class="tags-container tags">lua dissector proprietary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '15, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/d21f25a5f4d65373505534f991a4512f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acohen&#39;s gravatar image" /><p>acohen<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acohen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Apr '15, 04:23</p></div></div><div id="comments-container-41570" class="comments-container"><span id="41594"></span><div id="comment-41594" class="comment"><div id="post-41594-score" class="comment-score"></div><div class="comment-text"><p>Please define protocol stack.</p><p>From what I make up from your text this is: Ethernet / IP / TCP / Prop.Proto</p><p>Which later becomes</p><p>Ethernet / IP / TCP / HTTP</p><p>on the same ports. Is this correct?</p></div><div id="comment-41594-info" class="comment-info"><span class="comment-age">(20 Apr '15, 02:34)</span> Jaap ♦</div></div><span id="41597"></span><div id="comment-41597" class="comment"><div id="post-41597-score" class="comment-score"></div><div class="comment-text"><p>Yes, On application layer... My protocol dissects on port 8080, and get some info from proprietary protocol then it should switch to HTTP and continue to work as usual till the and of the stream (conversation).</p></div><div id="comment-41597-info" class="comment-info"><span class="comment-age">(20 Apr '15, 04:22)</span> acohen</div></div></div><div id="comment-tools-41570" class="comment-tools"></div><div class="clear"></div><div id="comment-41570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

