+++
type = "question"
title = "Topology Change inside STP"
description = '''Hi, I am seeing this messages across my network as per attach picture. Should I be worried of this topology changes stp.flags.tc==1 . I also saw there is no stop.flags.tack==0 Or perhaps something misconfiguration on the STP? Thanks.'''
date = "2014-07-25T20:50:00Z"
lastmod = "2014-07-25T21:50:00Z"
weight = 34918
keywords = [ "stp" ]
aliases = [ "/questions/34918" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Topology Change inside STP](/questions/34918/topology-change-inside-stp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34918-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am seeing this messages across my network as per attach picture.<img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-07-26_at_11.48.22_AM.png" alt="alt text" /></p><p>Should I be worried of this topology changes stp.flags.tc==1 . I also saw there is no stop.flags.tack==0</p><p>Or perhaps something misconfiguration on the STP?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">stp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '14, 20:50</strong></p><img src="https://secure.gravatar.com/avatar/da0590c1b52e4d823169fec48c06946a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Macha&#39;s gravatar image" /><p>Macha<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Macha has no accepted answers">0%</span></p></img></div></div><div id="comments-container-34918" class="comments-container"></div><div id="comment-tools-34918" class="comment-tools"></div><div class="clear"></div><div id="comment-34918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34920"></span>

<div id="answer-container-34920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34920-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To confirm whether it's a problem, trace it to the source switch and check the status of its interfaces. It could be a flapping Ethernet link to something unimportant, or it could be a critical trunk (the trace won't tell you that).</p><p>TCN BPDUs don't rigger any kind of network recalculation, so the packet itself shouldn't really cause harm. All it does is speed up the age out timer for related mac addresses.</p><p>Also note, the TCN BPDU is sent out on root ports and should be acked by the immediate switch upstream. Perhaps your trace isn't capturing both sides of the connection? It is odd for them to not be acknowledged.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '14, 21:50</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-34920" class="comments-container"><span id="34925"></span><div id="comment-34925" class="comment"><div id="post-34925-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks for the reply. Indeed, this capture only from one side.</p><p>regards.</p></div><div id="comment-34925-info" class="comment-info"><span class="comment-age">(26 Jul '14, 12:34)</span> Macha</div></div><span id="34926"></span><div id="comment-34926" class="comment"><div id="post-34926-score" class="comment-score"></div><div class="comment-text"><p>Just follow the BPDU to the originating switch. My guess is it's simply a physical interface flapping. Depending on how you have this set up, it could even be the link between an access switch and one client workstation.</p></div><div id="comment-34926-info" class="comment-info"><span class="comment-age">(26 Jul '14, 13:19)</span> Quadratic</div></div></div><div id="comment-tools-34920" class="comment-tools"></div><div class="clear"></div><div id="comment-34920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

