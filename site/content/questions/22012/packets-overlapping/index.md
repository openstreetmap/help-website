+++
type = "question"
title = "packets overlapping"
description = '''I have found in pcap file of wireshark that some packets overlap in time on the wire. For example certain packet is 1514 bytes long and another packet goes only five micro seconds after him. So on 100Mb/s link this packet should last approximately 120 micro seconds but another packet goes only 5 mik...'''
date = "2013-06-13T06:57:00Z"
lastmod = "2013-06-14T07:33:00Z"
weight = 22012
keywords = [ "overlapping" ]
aliases = [ "/questions/22012" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [packets overlapping](/questions/22012/packets-overlapping)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22012-score" class="post-score" title="current number of votes">0</div><span id="post-22012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have found in pcap file of wireshark that some packets overlap in time on the wire. For example certain packet is 1514 bytes long and another packet goes only five micro seconds after him. So on 100Mb/s link this packet should last approximately 120 micro seconds but another packet goes only 5 mikro seconds after the begining of first packet. How is this possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-overlapping" rel="tag" title="see questions tagged &#39;overlapping&#39;">overlapping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '13, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/78a6e59556f3af952df58b4ffd32cb3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="micacim&#39;s gravatar image" /><p><span>micacim</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="micacim has no accepted answers">0%</span></p></div></div><div id="comments-container-22012" class="comments-container"></div><div id="comment-tools-22012" class="comment-tools"></div><div class="clear"></div><div id="comment-22012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22021"></span>

<div id="answer-container-22021" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22021-score" class="post-score" title="current number of votes">1</div><span id="post-22021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please note that libpcap and WinPcap do the timestamping during capturing and that the timestamp is not added at the time the frame enters or leaves the NIC. But at the time libpcap or WInPcap get to process the packet.</p><p>It can happen that a few frames enter the NIC and while the host is processing the IRQ to fetch the packets, some more packets come in. Then the OS will read all packets from the buffer on the NIC and so libpcap/WinPcap will not be able to tell the exact time of arrival of the packets.</p><p>The same goes for sending packets, libpcap/WinPcap can already have timestamped them, even though the packets are still waiting in the NIC's buffer for tranmission.</p><p>If you want exact timestamps, you will need a capture card and driver where the timestamping is done on the capture card. Riverbed's TurboCap cards can be used for example to accomplish this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22021" class="comments-container"><span id="22064"></span><div id="comment-22064" class="comment"><div id="post-22064-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response. I suppose I need timestamping on the card, but I measure traffic on 100Mb/s, so can you tell me where I can find a 100Mb/s Ethernet card that supports timestamping on it?</p></div><div id="comment-22064-info" class="comment-info"><span class="comment-age">(14 Jun '13, 07:33)</span> <span class="comment-user userinfo">micacim</span></div></div></div><div id="comment-tools-22021" class="comment-tools"></div><div class="clear"></div><div id="comment-22021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22014"></span>

<div id="answer-container-22014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22014-score" class="post-score" title="current number of votes">0</div><span id="post-22014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On certain switches you can either monitor packets entering/leaving physical interface either packets entering/leaving on specific vlan. If you are mirroring vlan and you did not specify direction then you see same packet when it enters the vlan on switch and when leaving vlan on switch. And yes, switching times are in microseconds so thats probably the case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/0817cf7965ef06a56ada1be48a4244bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klodovic&#39;s gravatar image" /><p><span>klodovic</span><br />
<span class="score" title="42 reputation points">42</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klodovic has no accepted answers">0%</span></p></div></div><div id="comments-container-22014" class="comments-container"><span id="22019"></span><div id="comment-22019" class="comment"><div id="post-22019-score" class="comment-score"></div><div class="comment-text"><p>Sorry I didn't say that it was the traffic in one direction already filtered.</p></div><div id="comment-22019-info" class="comment-info"><span class="comment-age">(13 Jun '13, 10:34)</span> <span class="comment-user userinfo">micacim</span></div></div></div><div id="comment-tools-22014" class="comment-tools"></div><div class="clear"></div><div id="comment-22014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

