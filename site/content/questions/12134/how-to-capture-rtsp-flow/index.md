+++
type = "question"
title = "How to capture RTSP flow?"
description = '''Hi! I&#x27;m using Unreal Media Server and would like to capture the network traffic related to RTSP protocol. I&#x27;m able to get some data but it is not in the format I was expecting. I can&#x27;t see OPTIONS in the info column and can&#x27;t follow the RTSP negotiation. Is there any specific setting in wireshark so...'''
date = "2012-06-22T14:57:00Z"
lastmod = "2012-06-23T09:20:00Z"
weight = 12134
keywords = [ "rtsp" ]
aliases = [ "/questions/12134" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture RTSP flow?](/questions/12134/how-to-capture-rtsp-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12134-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I'm using Unreal Media Server and would like to capture the network traffic related to RTSP protocol. I'm able to get some data but it is not in the format I was expecting. I can't see OPTIONS in the info column and can't follow the RTSP negotiation.</p><p>Is there any specific setting in wireshark so it can show RSTP packets in the full form?</p></div><div id="question-tags" class="tags-container tags">rtsp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '12, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/19672a66be88cf630ec91e730c9771b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfsdev&#39;s gravatar image" /><p>hfsdev<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfsdev has no accepted answers">0%</span></p></div></div><div id="comments-container-12134" class="comments-container"></div><div id="comment-tools-12134" class="comment-tools"></div><div class="clear"></div><div id="comment-12134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12136"></span>

<div id="answer-container-12136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12136-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>maurizio simoni wrote:</p><blockquote><p>RTP is not automatically detected over UDP.</p></blockquote><p>RTP is difficult to detect reliably.</p><p>There is a heuristic, but it's a weak heuristic, and not enabled by default. Turn on the "Try to decode RTP outside of conversations" preference for RTP to enable it.</p><p>Note that it looks for a version number of 2 in the first octet, and a known payload type in the second octet, rather than a dynamic payload type.</p><blockquote><p>Same problem for RTCP.</p></blockquote><p>Same solution for RTCP ("Try to decode RTCP outside of conversations" preference for RTCP); the heuristics are a bit stronger, but still not enabled by default.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '12, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/a9eeb7d217a945ee04f4c3ec2945c59a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="braca&#39;s gravatar image" /><p>braca<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="braca has no accepted answers">0%</span></p></div></div><div id="comments-container-12136" class="comments-container"></div><div id="comment-tools-12136" class="comment-tools"></div><div class="clear"></div><div id="comment-12136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

