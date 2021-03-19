+++
type = "question"
title = "Passive Capture"
description = '''I was wondering if anyone has tried using a multiport gigabit switch adapter NIC such as the HP NC150T whilst capturing traffic, and if so does it affect results when capturing, such as jitter and delay at all? I am trying to model the affects of any virtualisation overhead on QoS for RTSP traffic. ...'''
date = "2012-08-27T05:39:00Z"
lastmod = "2012-08-27T10:11:00Z"
weight = 13912
keywords = [ "nic", "rtsp", "citrix" ]
aliases = [ "/questions/13912" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Passive Capture](/questions/13912/passive-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13912-score" class="post-score" title="current number of votes">0</div><span id="post-13912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering if anyone has tried using a multiport gigabit switch adapter NIC such as the <a href="http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?lang=en&amp;cc=us&amp;taskId=120&amp;prodSeriesId=428161&amp;prodTypeId=329290&amp;objectID=c00245681">HP NC150T</a> whilst capturing traffic, and if so does it affect results when capturing, such as jitter and delay at all? I am trying to model the affects of any virtualisation overhead on QoS for RTSP traffic.</p><p>How have you used them, as packets pass-through or tap off from the source/destination?<br />
</p><p>Regards</p><p>Papasean</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-rtsp" rel="tag" title="see questions tagged &#39;rtsp&#39;">rtsp</span> <span class="post-tag tag-link-citrix" rel="tag" title="see questions tagged &#39;citrix&#39;">citrix</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '12, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/a1ef1733ac698c2f0c73440b3efb503e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Papasean&#39;s gravatar image" /><p><span>Papasean</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Papasean has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-13912" class="comments-container"></div><div id="comment-tools-13912" class="comment-tools"></div><div class="clear"></div><div id="comment-13912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13916"></span>

<div id="answer-container-13916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13916-score" class="post-score" title="current number of votes">0</div><span id="post-13916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In advance: I have <strong>not used</strong> that adapter (kind of "interesting" concept).</p><p>According to the available docs, it's an unmanaged switch powered by the PCI card and internally connected to the server NIC on the same PCI card. As it's an unmanaged switch I don't think you can configure port mirroring on the switch. So you will be able to capture only the traffic to/from the server while running Wireshark on the server. As such, I don't see any advantage of this adapter for packet capturing.</p><blockquote><p>and if so does it affect results when capturing, such as jitter and delay at all?</p></blockquote><p>Capturing network packets is a passive process, so there "should" be no influence on the captured packets. HOWEVER, if the capturing system is overloaded, it may drop packets or tag the packets with varying/wrong time stamps, which may result in wrong jitter calculation during the analysis of the data. To make that happen, the capturing machine must be <strong>heavily</strong> overloaded. Not a good foundation for proper network analysis ;-)</p><blockquote><p>I am trying to model the affects of any virtualisation overhead on QoS for RTSP traffic.</p></blockquote><p>How is that related to the NIC in use?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '12, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13916" class="comments-container"></div><div id="comment-tools-13916" class="comment-tools"></div><div class="clear"></div><div id="comment-13916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

