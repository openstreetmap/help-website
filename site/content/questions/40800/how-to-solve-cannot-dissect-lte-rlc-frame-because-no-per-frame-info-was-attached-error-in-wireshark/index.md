+++
type = "question"
title = "How to solve cannot dissect LTE-RLC frame because no per frame info was attached error in wireshark."
description = '''Hi all, I am trying to dissect RLC-LTE PCAP messagges from openlte. DLT USER:156 ,PAYLOAD:RLC-LTE I got the following error. cannot dissect LTE-RLC frame because no per frame info was attached error in wireshark. Help me to solve this issue. Thanks &amp;amp; Regards, Sathish'''
date = "2015-03-24T06:12:00Z"
lastmod = "2015-03-24T06:53:00Z"
weight = 40800
keywords = [ "dissector" ]
aliases = [ "/questions/40800" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to solve cannot dissect LTE-RLC frame because no per frame info was attached error in wireshark.](/questions/40800/how-to-solve-cannot-dissect-lte-rlc-frame-because-no-per-frame-info-was-attached-error-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40800-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am trying to dissect RLC-LTE PCAP messagges from openlte.</p><p>DLT USER:156 ,PAYLOAD:RLC-LTE</p><p>I got the following error.</p><p>cannot dissect LTE-RLC frame because no per frame info was attached error in wireshark.</p><p>Help me to solve this issue.</p><p>Thanks &amp; Regards, Sathish</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '15, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/7ba5607f38325cbf87766b918e1d76a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sathish%20kannan&#39;s gravatar image" /><p>Sathish kannan<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sathish kannan has no accepted answers">0%</span></p></div></div><div id="comments-container-40800" class="comments-container"></div><div id="comment-tools-40800" class="comment-tools"></div><div class="clear"></div><div id="comment-40800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40801"></span>

<div id="answer-container-40801" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40801-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot call directly the RLC LTE dissector as it requires some metadata (RLC mode, Sequence Number length, ...) that are normally provided by the Catapult product, or by the UDP framing protocol described <a href="https://code.wireshark.org/review/#/c/6680/">here</a>.</p><p>So you need to modify the openlte code to match this UDP framing protocol (that adds the per frame info), and then enable the "try heuristic LTE-RLC over UDP framing" option in Wireshark.</p><p>Alternatively, you can follow this <a href="https://code.wireshark.org/review/#/c/6680/">link</a>, you can find the start of a development adding support for the dump of LTE MAC PDUs (by addeing the per frame info required by the dissector) coming from openlte. But the contributor did not do any follow-up after the initial review so it has stalled.</p><p>Anyway, this is more an openlte question than a Wireshark one. It's up to them to decide which format (UDP framing or enhancement of the GSMTAP format) they want to use. If this is the latter, then they should do a follow-up of the Gerrit code review above. I'm willing to help them but it seems like they lost interest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-40801" class="comments-container"></div><div id="comment-tools-40801" class="comment-tools"></div><div class="clear"></div><div id="comment-40801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

