+++
type = "question"
title = "wireshark shows SIP packets but gateway didn&#x27;t received."
description = '''Hi, We are troubleshooting an issue where we are able to see SIP packets in wireshark but the gateway didn&#x27;t received.  The SIP dialer used to send SIP packets to cisco voice gateway. For one call the gateway receives the SIP packets. For the next call the gateway didn&#x27;t receive the SIP packet. from...'''
date = "2015-07-05T23:18:00Z"
lastmod = "2015-07-06T12:35:00Z"
weight = 43878
keywords = [ "sip" ]
aliases = [ "/questions/43878" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark shows SIP packets but gateway didn't received.](/questions/43878/wireshark-shows-sip-packets-but-gateway-didnt-received)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43878-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We are troubleshooting an issue where we are able to see SIP packets in wireshark but the gateway didn't received.</p><ol><li>The SIP dialer used to send SIP packets to cisco voice gateway.</li><li>For one call the gateway receives the SIP packets.</li><li>For the next call the gateway didn't receive the SIP packet. from the SIP dialer system we are able to see the SIP packets in wireshark.</li><li>The transport used is UDP.</li></ol><p>Environment: [sip dialer]-------(lan router)------------[cisco gateway]</p><p>Is the lan router which blocks the SIP packets?? If so is there a way to detect that packets being blocked?</p><p>Thanks and Regards</p></div><div id="question-tags" class="tags-container tags">sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '15, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/874b7628ad99a5242e04072733c437b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mws&#39;s gravatar image" /><p>mws<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mws has no accepted answers">0%</span></p></div></div><div id="comments-container-43878" class="comments-container"></div><div id="comment-tools-43878" class="comment-tools"></div><div class="clear"></div><div id="comment-43878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43880"></span>

<div id="answer-container-43880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43880-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>UDP is a unreliable transport protocol, tracing on the SIP dialer won't show transport problems elsewhere in the network.</p><p>The SIP UA should retry and eventually fail the transaction if the situation persists. That's what you could see when tracing at the dialer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-43880" class="comments-container"><span id="43882"></span><div id="comment-43882" class="comment"><div id="post-43882-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap, yes and as you said SIP ua retries and fails after 7 attempts. Few points to for understanding. 1.The sip dialer uses x-cisco-cpa sip headers &amp; sends it to cisco gateway. 2.The first SIP call got succeeded. 3.The second SIP call retires and fails after 7 attempts. 4.The UDP trace in cisco gateway shows nothing from this sip dialer ip address for the problematic call.</p><p>5.From the sip dialer logs the sip call being sent and in wireshark log, we are able to see the SIP calls going outside. but those packets were lost/blocked somewhere before reaching the gateway.</p><p>Interesting case: If the sip dialer removes the x-cisco-cpa header (pl refer point-1), then all the calls are succeeded.</p><p>For Success calls: The sip call contains Message body-application/sdp. For the packets blocked/lost calls: The sip call contains Messagebody (multipart/mime)-application/sdp &amp; application/x-cisco-cpa.</p><p>With the help of wireshark we are confirming the packet are sent to wire.</p><p>Is there a possibility the packets be blocked somewhere in the LAN router?</p><p>And the blocking happens randomly like one call it allows and the next call being blocked/lost. If we restart sip dialer application, the first call is succeeding for the most of the times. This behavior shows the team that there is something to be looked in the sip dialer system.</p><p>Sorry to dump everything here, trying to explain the scenario what we are facing...because we relayed on wire-shark output.And we don't have doubt on wire-shark.</p><p>Finally we asked the LAN router team to check for any blocking calls. Is there anyother way we can troubleshoot this on sip dialer system. Thanks</p></div><div id="comment-43882-info" class="comment-info"><span class="comment-age">(06 Jul '15, 03:43)</span> mws</div></div><span id="43895"></span><div id="comment-43895" class="comment"><div id="post-43895-score" class="comment-score"></div><div class="comment-text"><p>Are you able to perform a capture at the SIP gateway? Or at least after the router? This could help to confirm where the drop is occurring and allow you to troubleshoot the correct network element.</p></div><div id="comment-43895-info" class="comment-info"><span class="comment-age">(06 Jul '15, 09:53)</span> Amato_C</div></div><span id="43911"></span><div id="comment-43911" class="comment"><div id="post-43911-score" class="comment-score"></div><div class="comment-text"><p>Since we are taking remote control of gateway using putty.exe console and unable to run wireshark or for port mirroring. The capture after the router was not performed. We have another system where its able to make calls successfully and all SIP INVITE reached to gateway. The only difference we see is the non working system is in separate vlan i.e x.x.A.x and the working system is in separate vlan i.e. x.x.B.x</p></div><div id="comment-43911-info" class="comment-info"><span class="comment-age">(06 Jul '15, 19:51)</span> mws</div></div></div><div id="comment-tools-43880" class="comment-tools"></div><div class="clear"></div><div id="comment-43880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43899"></span>

<div id="answer-container-43899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43899-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The x-cisco-cpa is not a header, it's a MIME body type; and as you pointed out when it's enabled it makes the INVITE continue a multi-part body: one for SDP, one for x-cisco-cpa. So perhaps either:</p><ol><li>Due to the extra body part for x-cisco-cpa the size of INVITE grew bigger than fit in a single IP packet, and the dialer had to fragment the UDP, and that's causing problems (like if you go through a NAT or Firewall, they sometimes have problems with fragmented IP/UDP). Or...</li><li>Perhaps the Cisco gateway isn't configured for CPA under the <code>voice service voip</code> mode, and won't accept the x-cisco-cpa body part without it?</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43899" class="comments-container"><span id="43912"></span><div id="comment-43912" class="comment"><div id="post-43912-score" class="comment-score"></div><div class="comment-text"><p>Yes its one of the MIME body type. 1. Just for clarity, if the fragmented IP/UDP pass through a NAT or Firewall, then all packets should be blocked, correct!! In our case, for the first SIP call it allows and SIP INVITE reached to gateway and sip call got succeeded. The next packet was blocked.And after a period of time it allows. As mentioned if the dialer application restarts then for most of the cases the first SIP INVITE succeeds. 2. The gateway is configured for the below cases, and it allows SIP calls with and without x-cisco-cpa body part. Meaning for the regular SIP INVITE the application/sdp is alone present and gateway accepts it. For the CPA calls the SIP INVITE contains both sdp's. There is no case where the SIP Header: Multipart-MIME/x-cisco-cpa present and not having x-cisco-cpa header. And at the time of non working calls, the UDP debug trace in the gateway shows no packets arrived from the dialer.</p></div><div id="comment-43912-info" class="comment-info"><span class="comment-age">(06 Jul '15, 20:00)</span> mws</div></div></div><div id="comment-tools-43899" class="comment-tools"></div><div class="clear"></div><div id="comment-43899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

