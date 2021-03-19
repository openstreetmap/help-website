+++
type = "question"
title = "At which layer does Wireshark capture packets in terms of OSI network model?"
description = '''Hi, Could someone please tell me at which layer does wireshark capture packets interms of OSI network model?'''
date = "2014-09-22T19:07:00Z"
lastmod = "2014-09-22T20:11:00Z"
weight = 36511
keywords = [ "capture", "packet" ]
aliases = [ "/questions/36511" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [At which layer does Wireshark capture packets in terms of OSI network model?](/questions/36511/at-which-layer-does-wireshark-capture-packets-in-terms-of-osi-network-model)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36511-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Could someone please tell me at which layer does wireshark capture packets interms of OSI network model?</p></div><div id="question-tags" class="tags-container tags">capture packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '14, 19:07</strong></p><img src="https://secure.gravatar.com/avatar/c72fc171b601ea5694b60561ca3c1aed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iamvicky&#39;s gravatar image" /><p>iamvicky<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iamvicky has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Sep '14, 11:20</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-36511" class="comments-container"></div><div id="comment-tools-36511" class="comment-tools"></div><div class="clear"></div><div id="comment-36511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36512"></span>

<div id="answer-container-36512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, captures are done from the wire, but the lowest OSI layer you get in a frame is layer 2. In most cases that means Ethernet these days. It does not capture things like autonegitiation or preambles etc, just the frames.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '14, 20:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36512" class="comments-container"><span id="36515"></span><div id="comment-36515" class="comment"><div id="post-36515-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper! So, does that mean either wireshark captures packets only at layer 2 or it captures from layer 2 till layer 7?</p></div><div id="comment-36515-info" class="comment-info"><span class="comment-age">(23 Sep '14, 03:56)</span> iamvicky</div></div><span id="36595"></span><div id="comment-36595" class="comment"><div id="post-36595-score" class="comment-score"></div><div class="comment-text"><p>It captures layer 2 and above...</p><p>The "and above" part is a result of L3-L7 being encapsulated within the L2 frame.</p></div><div id="comment-36595-info" class="comment-info"><span class="comment-age">(25 Sep '14, 06:09)</span> smp</div></div></div><div id="comment-tools-36512" class="comment-tools"></div><div class="clear"></div><div id="comment-36512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

