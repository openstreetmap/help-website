+++
type = "question"
title = "DHCP broadcast packets not displayed"
description = '''Hello, I&#x27;m tracing on a TAP the connection of a machine. I want to see the DHCP exchange of this machine. Normally I expect to see the sequence Discover - Offer - Request - Ack. But I see only Offer and Ack, the broadcast messages sent from the machine are not displayed. I tried several Wireshark Ve...'''
date = "2013-06-20T03:00:00Z"
lastmod = "2013-06-20T04:20:00Z"
weight = 22194
keywords = [ "broadcast", "dhcp", "windows7", "hp" ]
aliases = [ "/questions/22194" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DHCP broadcast packets not displayed](/questions/22194/dhcp-broadcast-packets-not-displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22194-score" class="post-score" title="current number of votes">0</div><span id="post-22194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm tracing on a TAP the connection of a machine. I want to see the DHCP exchange of this machine. Normally I expect to see the sequence Discover - Offer - Request - Ack. But I see only Offer and Ack, the broadcast messages sent from the machine are not displayed. I tried several Wireshark Version from 1.6 to 1.10 with different WinPcap (4.1.2 / 4.1.3) also 32 Bit and 64 Bit versions and different Network Ports/cards on the PC. If I connect the TAP to a XP Laptop I see the full sequence but on the PC I don't see them. The Windows Firewall is disabled and no additional one is installed. The capture run in promiscous mode without any capture filter.</p><p>The PC I have to use is an HP 8300 under Win7-64 with an additional 2 Port Ethernet Card from HP. I tried the Port of the cards and also the internal Port on the mainboard without success.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-hp" rel="tag" title="see questions tagged &#39;hp&#39;">hp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '13, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/372bb231ae144c8f985241d10916c21e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thaloss&#39;s gravatar image" /><p><span>thaloss</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thaloss has no accepted answers">0%</span></p></div></div><div id="comments-container-22194" class="comments-container"></div><div id="comment-tools-22194" class="comment-tools"></div><div class="clear"></div><div id="comment-22194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22195"></span>

<div id="answer-container-22195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22195-score" class="post-score" title="current number of votes">0</div><span id="post-22195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I tried the Port of the cards and also the internal Port on the mainboard without success.</p></blockquote><p>Please try to disable the TCP/IP "binding" of the capturing adapter.</p><blockquote><p>Interface Properties -&gt; remove check mark at "Internet Protocol Version V4" (and V6).</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '13, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22195" class="comments-container"><span id="22196"></span><div id="comment-22196" class="comment"><div id="post-22196-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I tried it but no change, still only Offer and Ack visible.</p><p>regards</p><p>Thaloss</p></div><div id="comment-22196-info" class="comment-info"><span class="comment-age">(20 Jun '13, 04:03)</span> <span class="comment-user userinfo">thaloss</span></div></div><span id="22197"></span><div id="comment-22197" class="comment"><div id="post-22197-score" class="comment-score"></div><div class="comment-text"><p>What kind of TAP is it (brand, modell)?</p><p>Can you try to use a switch mirror port instead of the TAP, to rule out the TAP as a possible source of the problem?</p><p>However, I think you already checked that, right?</p><blockquote><p>If I connect the TAP to a XP Laptop I see the full sequence but on the PC I don't see them.</p></blockquote><p>So, the problem occurs only if your capturing system is Windows 7, right?<br />
</p><p>If so, is there any security software installed on that system (AV, Firewall, Endpoint Secuirty, VPN Client)? If yes, please disable/uninstall that piece of software and try again.</p></div><div id="comment-22197-info" class="comment-info"><span class="comment-age">(20 Jun '13, 04:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22195" class="comment-tools"></div><div class="clear"></div><div id="comment-22195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

