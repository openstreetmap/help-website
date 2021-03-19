+++
type = "question"
title = "Difference between VoIP using GVSP and UDP?"
description = '''I have instances of VoIP traffic to sites where Wireshark says some of the flows are using UDP and some are marked as GVSP. I know that GVSP is UDP too, I was just wondering why Wireshark displays them differently?'''
date = "2016-03-23T07:47:00Z"
lastmod = "2016-03-23T08:03:00Z"
weight = 51126
keywords = [ "gvsp" ]
aliases = [ "/questions/51126" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between VoIP using GVSP and UDP?](/questions/51126/difference-between-voip-using-gvsp-and-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51126-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have instances of VoIP traffic to sites where Wireshark says some of the flows are using UDP and some are marked as GVSP. I know that GVSP is UDP too, I was just wondering why Wireshark displays them differently?</p></div><div id="question-tags" class="tags-container tags">gvsp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '16, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/361604a5e59b3a63cce487009ef5c41f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aztecdoug&#39;s gravatar image" /><p>Aztecdoug<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aztecdoug has no accepted answers">0%</span></p></div></div><div id="comments-container-51126" class="comments-container"></div><div id="comment-tools-51126" class="comment-tools"></div><div class="clear"></div><div id="comment-51126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51127"></span>

<div id="answer-container-51127" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51127-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Because Wireshark tries to give an as detailed as possible dissection of the network data. If it thinks there's GVSP payloads in there and the relevant dissector is enabled, it will try to dissect that payload. Why does it think it's there in the first place? That may depend on external signaling, heuristics, or manual configuration of the dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '16, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-51127" class="comments-container"></div><div id="comment-tools-51127" class="comment-tools"></div><div class="clear"></div><div id="comment-51127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

