+++
type = "question"
title = "Need direction on MGCP flow in Wireshark"
description = '''When analyzing MCGP call flow, Wireshark is able to determine RTP (call packets) flow after a the session has been set up. Viewing the packets (MGCP and RTP) I cannot see how Wireshark is able to do this as there are no session info contained from the MGCP setup to the RTP packets. I would like some...'''
date = "2011-02-08T07:59:00Z"
lastmod = "2011-02-08T14:11:00Z"
weight = 2229
keywords = [ "mgcp" ]
aliases = [ "/questions/2229" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need direction on MGCP flow in Wireshark](/questions/2229/need-direction-on-mgcp-flow-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2229-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When analyzing MCGP call flow, Wireshark is able to determine RTP (call packets) flow after a the session has been set up. Viewing the packets (MGCP and RTP) I cannot see how Wireshark is able to do this as there are no session info contained from the MGCP setup to the RTP packets. I would like someone who knows the code to please direct me to the area where this is resolved, so I can figure out how it works. Thanks in advance for saving me hours of time looking through an unfamiliar codebase.</p></div><div id="question-tags" class="tags-container tags">mgcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '11, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/a2c36e0535e33d86a1738e74e85101fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drewcrewof2&#39;s gravatar image" /><p>drewcrewof2<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drewcrewof2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '11, 08:00</p></div></div><div id="comments-container-2229" class="comments-container"></div><div id="comment-tools-2229" class="comment-tools"></div><div class="clear"></div><div id="comment-2229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2241"></span>

<div id="answer-container-2241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2241-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, In the MGCP setup info ther is presumably SDP giving the IP port and codec information for the RTP flow. Tse SDP information (pan/dissectors/packet-sdp.c) is used to set up a "conversation" (epan/conversation.c, doc/README.developer) for the upcomming RTP session and info is conveied to the RTP dissector (packet-rtp.c).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-2241" class="comments-container"><span id="2257"></span><div id="comment-2257" class="comment"><div id="post-2257-score" class="comment-score"></div><div class="comment-text"><p>Thanks, highly instructional, I got it!</p></div><div id="comment-2257-info" class="comment-info"><span class="comment-age">(09 Feb '11, 10:17)</span> drewcrewof2</div></div></div><div id="comment-tools-2241" class="comment-tools"></div><div class="clear"></div><div id="comment-2241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

