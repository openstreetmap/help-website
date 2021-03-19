+++
type = "question"
title = "UDP Packets Missing From RFID Receiver"
description = '''Hi there, I have an RFID receiver that constantly sends UDP packets to port 5757. When connected over ethernet to my desktop, all packets are received and valid (confirmed with Wireshark), and there is no issue. When I connect the receiver via ethernet to my laptop, not one UDP packet is received. T...'''
date = "2015-09-25T08:37:00Z"
lastmod = "2015-09-25T10:18:00Z"
weight = 46173
keywords = [ "netcat", "udp", "rfid", "packet", "bittwist" ]
aliases = [ "/questions/46173" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP Packets Missing From RFID Receiver](/questions/46173/udp-packets-missing-from-rfid-receiver)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46173-score" class="post-score" title="current number of votes">0</div><span id="post-46173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I have an RFID receiver that constantly sends UDP packets to port 5757. When connected over ethernet to my desktop, all packets are received and valid (confirmed with Wireshark), and there is no issue. When I connect the receiver via ethernet to my laptop, not one UDP packet is received.</p><p>Things I have tried: I have connected the laptop to the desktop over ethernet, and have sent UDP packets via netcat in both directions. Netcat has no issues with sending/receiving the data.</p><p>I've also captured and saved the RFID UDP packets on the desktop, and played them back using bittwist, first on the desktop, and had no issues capturing them in Wireshark(desktop). Then I copied the saved packets over to the laptop, played them back using bittwist, and had zero UDP packets captured in Wireshark(laptop).</p><p>Finally, I updated the ethernet driver and had the same results.</p><p>Any help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netcat" rel="tag" title="see questions tagged &#39;netcat&#39;">netcat</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-rfid" rel="tag" title="see questions tagged &#39;rfid&#39;">rfid</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-bittwist" rel="tag" title="see questions tagged &#39;bittwist&#39;">bittwist</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '15, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/27f8fa0105583cb5da111bc0185bacd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aohcm&#39;s gravatar image" /><p><span>aohcm</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aohcm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '15, 10:58</strong> </span></p></div></div><div id="comments-container-46173" class="comments-container"></div><div id="comment-tools-46173" class="comment-tools"></div><div class="clear"></div><div id="comment-46173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46174"></span>

<div id="answer-container-46174" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46174-score" class="post-score" title="current number of votes">0</div><span id="post-46174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If netcat is working correctly to\from the laptop it seems to me this is more of a capturing issue on the laptop rather than a networking one.</p><ul><li>What sort of Ethernet NIC is being used on the laptop?</li><li>What's the OS on the latop?</li><li>What's the Wireshark version you're using?</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46174" class="comments-container"><span id="46176"></span><div id="comment-46176" class="comment"><div id="post-46176-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply, grahamb.</p><p>Laptop side:</p><p>Intel(R) Ethernet Connection I217-LM, Windows 7 Professional(64 bit), Wireshark v1.12.7-0-g7fc8978 from master-1.12</p><p>Desktop side:</p><p>Intel(R) 82579LM Gigabit Network Connection, Windows 7 Professional (64 bit), Wireshark v1.12.7-0-g7fc8978 from master-1.12</p><p>For the record, netcat is working correcting when it listens for packets sent from netcat. The RFID receiver's packets are still missing (I do have an application that listens on port 5757 for the RFID packets, which works fine on the desktop, but that too fails to receive packets on the laptop).</p><p>Also, by disabling the DNS protocol profile, the malformed packets are now being captured correctly as UDP, and that is no longer the issue.</p></div><div id="comment-46176-info" class="comment-info"><span class="comment-age">(25 Sep '15, 10:18)</span> <span class="comment-user userinfo">aohcm</span></div></div></div><div id="comment-tools-46174" class="comment-tools"></div><div class="clear"></div><div id="comment-46174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

