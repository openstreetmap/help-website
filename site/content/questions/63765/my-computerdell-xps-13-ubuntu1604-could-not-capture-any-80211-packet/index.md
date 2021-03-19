+++
type = "question"
title = "My computer(DELL-XPS-13 Ubuntu16.04) could not capture any 802.11 packet"
description = '''I have set it to monitor mode , But it doesn&#x27;t work. Can anyone help me??Thanks! '''
date = "2017-10-09T08:00:00Z"
lastmod = "2017-10-21T03:32:00Z"
weight = 63765
keywords = [ "802.11" ]
aliases = [ "/questions/63765" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [My computer(DELL-XPS-13 Ubuntu16.04) could not capture any 802.11 packet](/questions/63765/my-computerdell-xps-13-ubuntu1604-could-not-capture-any-80211-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63765-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have set it to monitor mode , But it doesn't work. Can anyone help me??Thanks! <img src="https://osqa-ask.wireshark.org/upfiles/Selection_002.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '17, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/71f5ab99e4930387e62e2088e0466d2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ysing&#39;s gravatar image" /><p>ysing<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ysing has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '17, 10:36</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-63765" class="comments-container"><span id="63768"></span><div id="comment-63768" class="comment"><div id="post-63768-score" class="comment-score"></div><div class="comment-text"><p>Not enough information. First, have you tried on a wired interface, or in plain promiscuous mode on the wireless interface, with more success? In another words, is just the monitoring mode problematic or capturing in general? If it is just a monitor mode issue, what wireless card (chipset) does your machine use?</p></div><div id="comment-63768-info" class="comment-info"><span class="comment-age">(09 Oct '17, 10:34)</span> sindy</div></div><span id="64058"></span><div id="comment-64058" class="comment"><div id="post-64058-score" class="comment-score"></div><div class="comment-text"><p>Sorry, My fault, In plain promiscuous mode, it work success(TCP, ARP...) . But in monitor mode , I can't see any 802.11packet be captured. And my wireless card is <code>Network controller: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter</code></p></div><div id="comment-64058-info" class="comment-info"><span class="comment-age">(20 Oct '17, 19:19)</span> ysing</div></div></div><div id="comment-tools-63765" class="comment-tools"></div><div class="clear"></div><div id="comment-63765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64061"></span>

<div id="answer-container-64061" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64061-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This isn't likely a Wireshark issue but rather a HW problem. For one example, see here:</p><p><a href="https://forum.aircrack-ng.org/index.php/topic,1671.msg5591.html#msg5591">https://forum.aircrack-ng.org/index.php/topic,1671.msg5591.html#msg5591</a></p><p>And there are other complaints about using that chipset for this type of work (monitor/injection, etc.).</p><p>At this point I would change adapters - since this is likely a PCI based, obtain an inexpensive USB adapter that will do monitor+promisc mode. You can search here for specific chipsets, or try the aircrack-ng and/or the Kali Linux forums.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '17, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-64061" class="comments-container"><span id="64073"></span><div id="comment-64073" class="comment"><div id="post-64073-score" class="comment-score"></div><div class="comment-text"><p>Thanks for you help!..I would upvote the answer until I have enough reputaion</p></div><div id="comment-64073-info" class="comment-info"><span class="comment-age">(21 Oct '17, 19:07)</span> ysing</div></div><span id="64092"></span><div id="comment-64092" class="comment"><div id="post-64092-score" class="comment-score"></div><div class="comment-text"><p>Per the FAQ, the original author of the question can accept the answer so others will know that an acceptable answer has been provided. I think the up vote is for non-authors to indicate that the like the answer as well.</p><p><a href="https://ask.wireshark.org/faq/">https://ask.wireshark.org/faq/</a></p></div><div id="comment-64092-info" class="comment-info"><span class="comment-age">(22 Oct '17, 07:30)</span> Bob Jones</div></div></div><div id="comment-tools-64061" class="comment-tools"></div><div class="clear"></div><div id="comment-64061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

