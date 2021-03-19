+++
type = "question"
title = "Can I capture traffic between two physical devices?"
description = '''Hi All, I have two bits of hardware connected to each other via an ethernet cable, they are basically two computerised controllers for a very advanced boiler, lets call them A and B, so A and B are not seeing each other and the vendor has told me to replace the ethernet cable which I have done alrea...'''
date = "2015-11-30T07:05:00Z"
lastmod = "2015-11-30T07:37:00Z"
weight = 48087
keywords = [ "packet-capture", "networking", "devices" ]
aliases = [ "/questions/48087" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I capture traffic between two physical devices?](/questions/48087/can-i-capture-traffic-between-two-physical-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48087-score" class="post-score" title="current number of votes">0</div><span id="post-48087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have two bits of hardware connected to each other via an ethernet cable, they are basically two computerised controllers for a very advanced boiler, lets call them A and B, so A and B are not seeing each other and the vendor has told me to replace the ethernet cable which I have done already, but A and B still do not see each other.</p><p>To try and deep dive the issue I wanted to know if there is a way or is there any such device that I can plug in between A and B which would allow me to capture the network traffic, if any, between them, please bear in mind that A and B do not have any external monitor connections nor do they allow any interaction with the O/S installed on them, so does anything exist that would allow me to do what I want?</p><p>So at the moment it is like this ...</p><p>A -----EthernetCable ----- B</p><p>And what I want to do is this ...</p><p>A -----EthernetCable ----- NetworkCaptureDevice -----EthernetCable ----- B</p><p>I hope that makes sense! :)</p><p>Thanks</p><p>Jim</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-devices" rel="tag" title="see questions tagged &#39;devices&#39;">devices</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '15, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/256dc1a99f157d9aa3d7ca85cdd5d165?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JimBob321&#39;s gravatar image" /><p><span>JimBob321</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JimBob321 has no accepted answers">0%</span></p></div></div><div id="comments-container-48087" class="comments-container"></div><div id="comment-tools-48087" class="comment-tools"></div><div class="clear"></div><div id="comment-48087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48090"></span>

<div id="answer-container-48090" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48090-score" class="post-score" title="current number of votes">1</div><span id="post-48090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use either a switch that will mirror or span ports, an old hub if you can find one, or for $$$ a network tap, or even a machine in the middle.</p><p>See the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a>, and the <a href="https://wiki.wireshark.org/HubReference">hub</a> and <a href="https://wiki.wireshark.org/SwitchReference">switch</a> reference pages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48090" class="comments-container"></div><div id="comment-tools-48090" class="comment-tools"></div><div class="clear"></div><div id="comment-48090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48091"></span>

<div id="answer-container-48091" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48091-score" class="post-score" title="current number of votes">0</div><span id="post-48091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It does make sense but there may be a difficulty negotiating the link between the devices at L1 - in such case a capturing device would show nothing.</p><p>I wonder whether the Ethernet interfaces of your hardware could be so old that they would not be able to auto-detect which pair is which (this functionality is often called "auto MDI/MDI-X") and so you would need to connect both of them to a switch (which is supposed to handle that) or use a so-called "crossed cable".</p><p>Can you state the parameters/make of the Ethernet interfaces of your rocket boilers?</p><p>If the cable turns out not to be the issue, a PC with two network cards (probably most easily available), or a switch with monitoring capability, or a "tap" would help you capture what happens on the wire once the link is established at L1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48091" class="comments-container"></div><div id="comment-tools-48091" class="comment-tools"></div><div class="clear"></div><div id="comment-48091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

