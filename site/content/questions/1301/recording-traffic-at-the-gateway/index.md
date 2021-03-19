+++
type = "question"
title = "recording traffic at the gateway"
description = '''hi, somebody is constantly hacking my firewall. which way is there to record traffic at the gateway (which is a modem-router in my case)? do i need a hub where a second pc is running on which wireshark is recording? is there any tutorial on how to do this? a total beginner'''
date = "2010-12-09T07:59:00Z"
lastmod = "2010-12-29T05:34:00Z"
weight = 1301
keywords = [ "recording", "traffic", "gateway" ]
aliases = [ "/questions/1301" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [recording traffic at the gateway](/questions/1301/recording-traffic-at-the-gateway)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1301-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, somebody is constantly hacking my firewall. which way is there to record traffic at the gateway (which is a modem-router in my case)?</p><p>do i need a hub where a second pc is running on which wireshark is recording? is there any tutorial on how to do this?</p><p>a total beginner</p></div><div id="question-tags" class="tags-container tags">recording traffic gateway</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '10, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/7d69a51ae803b51b82ed57f4b40f1da8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C8H10N4O2&#39;s gravatar image" /><p>C8H10N4O2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C8H10N4O2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Feb '12, 19:01</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-1301" class="comments-container"></div><div id="comment-tools-1301" class="comment-tools"></div><div class="clear"></div><div id="comment-1301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

6 Answers:

</div>

</div>

<span id="1305"></span>

<div id="answer-container-1305" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1305-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is the device that you are calling the firewall and "modem-router" the same device? And by modem-router, is that terminating a DSL or cable modem connection? If so, you are going to have difficulty capturing in front of it. If this is all one device, it could conceivably log the information to a syslog server on the private side. This does not give you the detail that you could see if you could capture packets on the public side. The reason that your ability to capture in front of it is limited (again, assuming this is a single device) is that you would need hardware capability to sniff the connection. It's not likely that you have this hardware.<br />
</p><p>If you have a cable or dsl connection terminating in what you are calling a modem-router and your firewall is behind it, then you could capture traffic between the two. This would involve the standard methods.<br />
</p><p>1) A hub with the modem-router, firewall and capture pc.</p><p>2) A switch with span (or monitor) capability and the above devices connected</p><p>3) Network TAPs</p><p>Please post back where you need clarification to this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '10, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></br></p></div></div><div id="comments-container-1305" class="comments-container"></div><div id="comment-tools-1305" class="comment-tools"></div><div class="clear"></div><div id="comment-1305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1309"></span>

<div id="answer-container-1309" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1309-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>dear paul:</p><p>thank you for your feedback! the device is a modem and can be used as a router too. I guess I will run it only as a modem. I have a zyxel router/firewall too. do I need a hub or a switch (I have all the stuff stored in the company, so no problem at all. what would be the best configuration?</p><p>thanks</p><p>mike</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '10, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/7d69a51ae803b51b82ed57f4b40f1da8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C8H10N4O2&#39;s gravatar image" /><p>C8H10N4O2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C8H10N4O2 has no accepted answers">0%</span></p></div></div><div id="comments-container-1309" class="comments-container"></div><div id="comment-tools-1309" class="comment-tools"></div><div class="clear"></div><div id="comment-1309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1310"></span>

<div id="answer-container-1310" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1310-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>dear paul:</p><p>thanks for your feedback! the device is a modem and can be used as a router too. I guess I will run it only as a modem. I have a zyxel router/firewall too which I can put right after the modem. do I need a hub or a switch (monitored port) (I have all the stuff stored in the company, so no problem at all. what would be the best configuration?</p><p>thanks</p><p>mike</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '10, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/7d69a51ae803b51b82ed57f4b40f1da8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C8H10N4O2&#39;s gravatar image" /><p>C8H10N4O2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C8H10N4O2 has no accepted answers">0%</span></p></div></div><div id="comments-container-1310" class="comments-container"></div><div id="comment-tools-1310" class="comment-tools"></div><div class="clear"></div><div id="comment-1310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1312"></span>

<div id="answer-container-1312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1312-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you run it as a modem only, it should basically be a bridge from your flavor of broadband to Ethernet. So you can then capture traffic between the modem and your firewall. To do so a 'dumb' hub connected to a capture station would suffice. The side effect of this is that the communication will drop to half duplex. I have seen cases where a hub isn't necessarily just a hub. So just be for warned, that the oldest, simplest, single speed hub you can find is the one that will always work.</p><p>A switch has the added advantage of allowing full duplex communication to continue. However, it requires configuration and not all switches are capable of this span or monitor mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '10, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1312" class="comments-container"></div><div id="comment-tools-1312" class="comment-tools"></div><div class="clear"></div><div id="comment-1312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1497"></span>

<div id="answer-container-1497" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1497-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>dear paul:</p><p>can you give me a hint, in which way the recording system should be configured due to safety aspects? I would like to use this setup regarding forensics / proof of evidence.</p><p>is there any way to ensure that the recording system won't be corrupted. should I use linux? windows without web access / EFS-filesystem for the recording device?</p><p>can the traffic which is recorded be secured by hash-code in any way so you really get proof?</p><p>best regards</p><p>max</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '10, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/7d69a51ae803b51b82ed57f4b40f1da8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C8H10N4O2&#39;s gravatar image" /><p>C8H10N4O2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C8H10N4O2 has no accepted answers">0%</span></p></div></div><div id="comments-container-1497" class="comments-container"></div><div id="comment-tools-1497" class="comment-tools"></div><div class="clear"></div><div id="comment-1497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1507"></span>

<div id="answer-container-1507" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1507-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A capture that will withstand forensic scrutiny brings up several concerns. For example:</p><p>1) was every related packet captured</p><p>2) were any packets corrupted during the capture process</p><p>3) were the capture file(s) modified post capture</p><p>I'm not sure I can answer them all. Each frame has a hash, but that would only help authenticate a capture file if that hash could be written to another secure location during the capture process. Missing frames are always possible due to various issues. For example, if the switch span port was changed or if capacity was exceeded.</p><p>I think, as you suggested, post capture storage security is about the best we can do. So it would be nice to md5 each file as soon as writing is complete. It would also be good to audit the file system and record the md5 hash externally (to another destination). Beyond that, general security best practices. Since this does not fully address your concerns, I'll be watching for other's comments as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '10, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1507" class="comments-container"></div><div id="comment-tools-1507" class="comment-tools"></div><div class="clear"></div><div id="comment-1507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

