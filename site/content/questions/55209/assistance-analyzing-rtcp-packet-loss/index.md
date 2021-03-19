+++
type = "question"
title = "Assistance analyzing RTCP packet loss"
description = '''Hi all, I have an Interworking Function Gateway that does V4 to V6 conversions. Basically one side of the call comes in v4 and the IWF converts to v6 and sends the packet out the other side. I am getting complaints of packet loss at RTCP. I have taken a capture on both the ingress and egress side, s...'''
date = "2016-08-30T09:26:00Z"
lastmod = "2016-08-30T21:39:00Z"
weight = 55209
keywords = [ "rtcp", "v4", "v6" ]
aliases = [ "/questions/55209" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Assistance analyzing RTCP packet loss](/questions/55209/assistance-analyzing-rtcp-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55209-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I have an Interworking Function Gateway that does V4 to V6 conversions. Basically one side of the call comes in v4 and the IWF converts to v6 and sends the packet out the other side. I am getting complaints of packet loss at RTCP. I have taken a capture on both the ingress and egress side, so I have the v4 and v6 capture side. What I want to do is compare the two side by side to see what packet loss I have at RTCP. In theory I should have a 1 for 1 packet count - v4 packet in, and v6 packet out. Is there something unique in the v4 packet and the v6 packet that would "tie" the two together so I know which v4 packet goes to which v6 packet?</p></div><div id="question-tags" class="tags-container tags">rtcp v4 v6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '16, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/8a4299bf739632fbea42f5efee059873?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joeydmendoza&#39;s gravatar image" /><p>joeydmendoza<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joeydmendoza has no accepted answers">0%</span></p></div></div><div id="comments-container-55209" class="comments-container"></div><div id="comment-tools-55209" class="comment-tools"></div><div class="clear"></div><div id="comment-55209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55218"></span>

<div id="answer-container-55218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55218-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Why don't you try to match up the time stamps in the RTCP Sender reports. You can apply the time stamps as a column to quickly match them up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '16, 21:39</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-55218" class="comments-container"></div><div id="comment-tools-55218" class="comment-tools"></div><div class="clear"></div><div id="comment-55218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

