+++
type = "question"
title = "Trace a call between two MGWs"
description = '''Hi, I need to trace one call between two media gateways in mobile core network (H.248 and sigtran). Can this be done with wireshark? if yes, how can I do this? Thanks in advance.'''
date = "2011-02-05T14:23:00Z"
lastmod = "2011-02-05T16:29:00Z"
weight = 2168
keywords = [ "mgw" ]
aliases = [ "/questions/2168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trace a call between two MGWs](/questions/2168/trace-a-call-between-two-mgws)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need to trace one call between two media gateways in mobile core network (H.248 and sigtran). Can this be done with wireshark? if yes, how can I do this?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">mgw</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '11, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/ec755a8ba7c6c91e95a0515d10d1afb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorgferr&#39;s gravatar image" /><p>jorgferr<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorgferr has no accepted answers">0%</span></p></div></div><div id="comments-container-2168" class="comments-container"></div><div id="comment-tools-2168" class="comment-tools"></div><div class="clear"></div><div id="comment-2168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2172"></span>

<div id="answer-container-2172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2172-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presuming you work for the telco in question, just arrange for a port-mirror/SPAN to a port on a switch in the transit path and capture to a locally connected wireshark enabled PC. (If you have a switch that supports remote capture you might be able to use that facility as well).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '11, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-2172" class="comments-container"><span id="2177"></span><div id="comment-2177" class="comment"><div id="post-2177-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. But in the media gateways passes several calls and I need to trace just one (to measure some parameters). Is it possible to filter in wireshark just to catch one call?</p></div><div id="comment-2177-info" class="comment-info"><span class="comment-age">(06 Feb '11, 07:28)</span> jorgferr</div></div><span id="2218"></span><div id="comment-2218" class="comment"><div id="post-2218-score" class="comment-score"></div><div class="comment-text"><p>To just catch one call e.g have a capture filter catching a single call is impossible I'd say, it might be possible to filter out one call using display filter. But even that is not so easy and requires a bit of manual work as there is nothing in MEGACO/H.248 that ties the signals to a subscriber number or something similar.</p></div><div id="comment-2218-info" class="comment-info"><span class="comment-age">(07 Feb '11, 23:26)</span> Anders ♦</div></div></div><div id="comment-tools-2172" class="comment-tools"></div><div class="clear"></div><div id="comment-2172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

