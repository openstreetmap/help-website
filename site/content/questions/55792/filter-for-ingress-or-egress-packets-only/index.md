+++
type = "question"
title = "filter for ingress or egress packets only"
description = '''Is it possible to have a filter to display only ingress packets(or only egress ones)? or something that identifies which packet is ingress and which one is egress?'''
date = "2016-09-24T04:38:00Z"
lastmod = "2016-09-24T04:55:00Z"
weight = 55792
keywords = [ "filter", "ingress", "egress" ]
aliases = [ "/questions/55792" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [filter for ingress or egress packets only](/questions/55792/filter-for-ingress-or-egress-packets-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55792-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to have a filter to display only ingress packets(or only egress ones)? or something that identifies which packet is ingress and which one is egress?</p></div><div id="question-tags" class="tags-container tags">filter ingress egress</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '16, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/ba02c181c309b201706731f114663453?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hamed%20nz&#39;s gravatar image" /><p>hamed nz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hamed nz has no accepted answers">0%</span></p></div></div><div id="comments-container-55792" class="comments-container"></div><div id="comment-tools-55792" class="comment-tools"></div><div class="clear"></div><div id="comment-55792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55794"></span>

<div id="answer-container-55794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55794-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you capture on an interface which has a MAC address, then frames with this MAC address as a source one (<code>eth.src == my:ma:ca:dd:re:ss</code>) are egress and frames with other source MAC addresses (<code>!(eth.src == my:ma:ca:dd:re:ss)</code>) are ingress. If you capture on a port of a switch, nothing in the frame itself tells you the direction. But on switches with monitoring capabilities it is often possible (and useful for bandwidth-related reasons) to copy each direction of a source port to its own monitoring port, and capture on the two monitoring ports simultaneously, using two interfaces on the capturing machine. In this case, the interface id becomes the parameter telling you ingress frames from egress ones. You can make it a column in the packet list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '16, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55794" class="comments-container"></div><div id="comment-tools-55794" class="comment-tools"></div><div class="clear"></div><div id="comment-55794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

