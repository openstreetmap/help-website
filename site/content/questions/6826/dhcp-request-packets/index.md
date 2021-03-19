+++
type = "question"
title = "DHCP request packets"
description = '''on my trace I have  DHCP Request DHCP ACK DHCP Request  I don&#x27;t understand what triggers the second request.  the difference between the two request packets is the packet subtype first request packet flags: .... ..01 = DS status: Frame from STA to DS via an AP (To DS: 1 From DS: 0) (0x01) second req...'''
date = "2011-10-10T05:16:00Z"
lastmod = "2011-10-10T06:24:00Z"
weight = 6826
keywords = [ "dhcp", "wlan", "bootp" ]
aliases = [ "/questions/6826" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [DHCP request packets](/questions/6826/dhcp-request-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6826-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>on my trace I have</p><pre><code>DHCP Request
DHCP ACK
DHCP Request</code></pre><p>I don't understand what triggers the second request. the difference between the two request packets is the packet subtype first request packet flags: .... ..01 = DS status: Frame from STA to DS via an AP (To DS: 1 From DS: 0) (0x01) second request packet flags: .... ..10 = DS status: Frame from DS to a STA via AP(To DS: 0 From DS: 1) (0x02)</p><p>anyone can help me to figure out whats going on?</p></div><div id="question-tags" class="tags-container tags">dhcp wlan bootp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '11, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p>ddayan<br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Oct '11, 05:24</p></div></div><div id="comments-container-6826" class="comments-container"></div><div id="comment-tools-6826" class="comment-tools"></div><div class="clear"></div><div id="comment-6826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6830"></span>

<div id="answer-container-6830" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6830-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On your wireless lan, all traffic within the same subnet is sent to the AP first and then from the AP to the destination. Depending on the physical location of the capturing device compared to the source, the AP and the destination you will see some or all of the packets.</p><p>I suspect that the AP is also the DHCP server and that it responds to the DHCP request. The second Request is most probably due to the fact that it was a broadcast packet so the AP needs to send it to all systems too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '11, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6830" class="comments-container"><span id="6832"></span><div id="comment-6832" class="comment"><div id="post-6832-score" class="comment-score"></div><div class="comment-text"><p>Makes sense, right now i'm using a simple topology where the AP is the DHCP server and the client is also the capturing device. thanks!</p></div><div id="comment-6832-info" class="comment-info"><span class="comment-age">(10 Oct '11, 06:31)</span> ddayan</div></div></div><div id="comment-tools-6830" class="comment-tools"></div><div class="clear"></div><div id="comment-6830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6827"></span>

<div id="answer-container-6827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6827-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you will find the first request is the "DHCP Discover", where your client doesn't know of any DHCP servers. Once it sees a response, the ACK, it can then send a proper "DHCP Request". This is still a broadcast, but it will contain a non-zero entry in the the Server IP address field indicating a particular server it would like a DHCP Offer from.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '11, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-6827" class="comments-container"><span id="6828"></span><div id="comment-6828" class="comment"><div id="post-6828-score" class="comment-score"></div><div class="comment-text"><p>How come theres no 2nd ACK packet? Also in both request packets the bootp protocol info is the same</p></div><div id="comment-6828-info" class="comment-info"><span class="comment-age">(10 Oct '11, 05:43)</span> ddayan</div></div></div><div id="comment-tools-6827" class="comment-tools"></div><div class="clear"></div><div id="comment-6827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

