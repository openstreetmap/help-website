+++
type = "question"
title = "How to capture SIP / RTP traffic over wireless LAN? Is it possible to decrypt the SIP / RTP frame headers?"
description = '''Hi Experts, Am trying to capture SIP / RTP traffic from my wireless laptop. I&#x27;m making a SIP call over Wireless. I can capture the 802.11 packets with appropriate QoS settings. But i dont&#x27; see any SIP / RTP packets captured by the Wireshark. Are we able to capture the SIP / RTP packets over WLAN? My...'''
date = "2013-04-11T11:21:00Z"
lastmod = "2013-04-11T14:18:00Z"
weight = 20344
keywords = [ "sip" ]
aliases = [ "/questions/20344" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture SIP / RTP traffic over wireless LAN? Is it possible to decrypt the SIP / RTP frame headers?](/questions/20344/how-to-capture-sip-rtp-traffic-over-wireless-lan-is-it-possible-to-decrypt-the-sip-rtp-frame-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20344-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>Am trying to capture SIP / RTP traffic from my wireless laptop. I'm making a SIP call over Wireless. I can capture the 802.11 packets with appropriate QoS settings. But i dont' see any SIP / RTP packets captured by the Wireshark.</p><p>Are we able to capture the SIP / RTP packets over WLAN?</p><p>My network setup : SIP server --&gt; WLAN controller --&gt; L3 Switch --&gt; Access point ===&gt; 2 Wireless laptop with SIP clients.</p><p>Wireshark (observer) is running in a machine connected in that L3 switch. End to End QoS settings implemented in L3 switch.</p><p>Encrypted wireless packets are sent to the Access point over Wireless LAN. In turn, Access point will decrypt the 802.11 packets and send it to the above observer connected in L3 switch.</p><p>I'm able to capture the 802.11 packets with appropriate QoS settings. But there are no SIP / RTP traffic seen in my wireshark capture.</p><p>Can any expert help me ?</p><p>Thank you.</p><p>/Manik</p></div><div id="question-tags" class="tags-container tags">sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '13, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/172b03cca4b5533fe2d01ae83a673790?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manikd&#39;s gravatar image" /><p>manikd<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manikd has no accepted answers">0%</span></p></div></div><div id="comments-container-20344" class="comments-container"></div><div id="comment-tools-20344" class="comment-tools"></div><div class="clear"></div><div id="comment-20344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20351"></span>

<div id="answer-container-20351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20351-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>WLAN controller --&gt; L3 Switch --&gt; Access point</p></blockquote><p>If that is really a <strong>WLAN controller</strong>, then the communication between the AP and the WLAN Controller is probably encrypted, so all you will see on a switch port is encrypted traffic (thus no SIP/RTP).</p><p>However, I don't quite understand why you see 802.11 packets while you are capturing traffic on a L3 switch, but maybe I misinterpret your setup. Did you capture on an ethernet port of the switch (with port mirroring) or via a WLAN interface in your Wireshark PC/Laptop?</p><p>BTW: Can you add some information about the WLAN controller (brand, modell) and the AP. It will help to understand if the communication is encrypted or not.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '13, 14:44</p></div></div><div id="comments-container-20351" class="comments-container"><span id="20373"></span><div id="comment-20373" class="comment"><div id="post-20373-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your reply. I got know that the Access point is not capable enough to capture SIP traffic and send it to the observer. It can send the basic info about 802.11 packets.</p><p>So using the above network setup we can't achieve capturing the detailed SIP packets.!!!</p><p>I will have to go for a MacBook or Alfa / airpcap card.</p><p>Thanks a lot for your feedback.</p><p>/Manik</p></div><div id="comment-20373-info" class="comment-info"><span class="comment-age">(12 Apr '13, 03:01)</span> manikd</div></div><span id="20375"></span><div id="comment-20375" class="comment"><div id="post-20375-score" class="comment-score"></div><div class="comment-text"><p>@manikd</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-20375-info" class="comment-info"><span class="comment-age">(12 Apr '13, 03:11)</span> grahamb ♦</div></div></div><div id="comment-tools-20351" class="comment-tools"></div><div class="clear"></div><div id="comment-20351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

