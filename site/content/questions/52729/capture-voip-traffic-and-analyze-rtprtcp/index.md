+++
type = "question"
title = "Capture VoIP traffic and analyze RTP/RTCP"
description = '''Hello I want to analyze VoIP traffic in order to calculate jitter, packet loss and so on. Then comparing them to the values reported by RTCP.  Can I analyze that traffic if the application (for example WebRTPC or Hangouts)encrypts the traffic? I guess I can&#x27;t. Is there an application I can use to an...'''
date = "2016-05-18T07:35:00Z"
lastmod = "2016-05-18T07:58:00Z"
weight = 52729
keywords = [ "rtcp", "rtp", "voip" ]
aliases = [ "/questions/52729" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture VoIP traffic and analyze RTP/RTCP](/questions/52729/capture-voip-traffic-and-analyze-rtprtcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52729-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I want to analyze VoIP traffic in order to calculate jitter, packet loss and so on. Then comparing them to the values reported by RTCP.<br />
</p><p>Can I analyze that traffic if the application (for example WebRTPC or Hangouts)encrypts the traffic? I guess I can't. Is there an application I can use to analyze this traffic, establishing a connection between two computers I have?</p></div><div id="question-tags" class="tags-container tags">rtcp rtp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/9057d9972c7dbd2019d1785547a0e146?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Haumea&#39;s gravatar image" /><p>Haumea<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Haumea has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-52729" class="comments-container"></div><div id="comment-tools-52729" class="comment-tools"></div><div class="clear"></div><div id="comment-52729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52735"></span>

<div id="answer-container-52735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52735-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hard to say exactly without seeing the capture. To be able to use the jitter and loss analysis which Wireshark offers for RTP, you need access to the information in the RTP header (sequence numbers and timestamps). For SRTP this is still possible as only the audio payload is encrypted there.</p><p>If some kind of UDP transport layer security is used (but where would you get access to the RTCP in such case?), it may still be possible to evaluate jitter if the codec uses fixed packet rate, and loss if the jitter is small. With big jitter and no access to sequence numbers, detection of loss would be more complex (counting packets over a time interval leaves some uncertainty).</p><p>With a TCP-based encrypted transport, loss at packet level can be seen directly on TCP level but does not exist at all from application point of view; on the other hand, the jitter coming from eventual retransmissions caused by packet loss is so massive that the "natural" one becomes insignificant. But also here, the packet rate must be constant so that jitter could be evaluated without access to the timestamps (unless TCP timestamp option is used).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52735" class="comments-container"></div><div id="comment-tools-52735" class="comment-tools"></div><div class="clear"></div><div id="comment-52735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

