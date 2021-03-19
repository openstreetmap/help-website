+++
type = "question"
title = "How to get &quot;dialed number&quot; in a MGCP/SDP/RTP  VoIP call"
description = '''in wireshark if I go to Telephony -&amp;gt; VoIP calls I get a list of VoIP (MGCP) calls (not all of them with the corresponding RTP packets) In that list I can see the &quot;To&quot; field (dialed number) but I have no clue how to get the same result with TShark. I have inspecte MGCP, and SDP and RTP packets but...'''
date = "2015-09-15T15:20:00Z"
lastmod = "2015-09-29T12:34:00Z"
weight = 45866
keywords = [ "mgcp", "voip" ]
aliases = [ "/questions/45866" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get "dialed number" in a MGCP/SDP/RTP VoIP call](/questions/45866/how-to-get-dialed-number-in-a-mgcpsdprtp-voip-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45866-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>in wireshark if I go to Telephony -&gt; VoIP calls I get a list of VoIP (MGCP) calls (not all of them with the corresponding RTP packets)</p><p>In that list I can see the "To" field (dialed number) but I have no clue how to get the same result with TShark. I have inspecte MGCP, and SDP and RTP packets but none of them has this value.</p></div><div id="question-tags" class="tags-container tags">mgcp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '15, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/47164287da0e0d6aec8ee380f9237932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qsebas&#39;s gravatar image" /><p>qsebas<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qsebas has one accepted answer">100%</span></p></div></div><div id="comments-container-45866" class="comments-container"></div><div id="comment-tools-45866" class="comment-tools"></div><div class="clear"></div><div id="comment-45866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46267"></span>

<div id="answer-container-46267" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46267-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I decided to download the wireshark sourcecode and inspect it to try to figure where the hell is getting this information.</p><p>The field is "mgcp.param.observedevents" it can be "hd" for a pick-up, numbers (in my case they were sepparated by comma, is why i din't found the numbers in a raw search) or "hu" for a hang-up, or the numbers.</p><p>What I've read in the protocol specification is that they can come in several mgcp packets and they should be concatened, and also they should be checket against the field "digitMap" interpreted as regexp to see if it is a valid number (or maybe a prefix). But in my case they came allways in a single mgcp packet and the correctness of the number was not part of what i needed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '15, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/47164287da0e0d6aec8ee380f9237932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qsebas&#39;s gravatar image" /><p>qsebas<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qsebas has one accepted answer">100%</span></p></div></div><div id="comments-container-46267" class="comments-container"></div><div id="comment-tools-46267" class="comment-tools"></div><div class="clear"></div><div id="comment-46267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

