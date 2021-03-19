+++
type = "question"
title = "Cannot see TCP messages of 3rd party device on my Windows 7 laptop"
description = '''I am using a Windows XP laptop with Wireshark to capture all network messages to and from another device. I am using a port-mirroring switch between that device and its regular network connection. When I connect my Windows XP laptop to the output port of the mirroring switch, Wireshark sees and capt...'''
date = "2013-10-03T07:44:00Z"
lastmod = "2013-10-03T08:46:00Z"
weight = 25590
keywords = [ "windows7", "promiscuous-mode", "mirroring" ]
aliases = [ "/questions/25590" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot see TCP messages of 3rd party device on my Windows 7 laptop](/questions/25590/cannot-see-tcp-messages-of-3rd-party-device-on-my-windows-7-laptop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25590-score" class="post-score" title="current number of votes">0</div><span id="post-25590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using a Windows XP laptop with Wireshark to capture all network messages to and from another device. I am using a port-mirroring switch between that device and its regular network connection. When I connect my Windows XP laptop to the output port of the mirroring switch, Wireshark sees and captures all message received by and transmitted by the other device. So I know that the port mirroring switch is working as expected.<br />
</p><p>However, when I use my Windows 7 laptop instead of my old Windows XP laptop and plug it into that same output port on the mirroring switch, Wireshark does not see any TCP messages that are being sent to/from the other device.</p><p>Why doesn't my Windows 7/Wireshark laptop capture 3rd party messages when they are captured just fine on my Windows XP/Wireshark laptop?</p><p>On my Windows 7 laptop, I am using Wireshark 1.10.2 (64-bit) with WinPcap 4.1.3 The Capture Option "Use promiscuous mode" box is checked.</p><p>Could it be a promiscuous mode issue with Windows?<br />
Could it be a promiscuous mode issue with the NIC?</p><p>Is it possible that the firewall is blocking traffic that is for 3rd party devices?</p><p>Thank you for any insight or suggestions</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-promiscuous-mode" rel="tag" title="see questions tagged &#39;promiscuous-mode&#39;">promiscuous-mode</span> <span class="post-tag tag-link-mirroring" rel="tag" title="see questions tagged &#39;mirroring&#39;">mirroring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '13, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/1b5e9889238ca9b14298c597d39c658c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markyi476&#39;s gravatar image" /><p><span>markyi476</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markyi476 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-25590" class="comments-container"></div><div id="comment-tools-25590" class="comment-tools"></div><div class="clear"></div><div id="comment-25590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25595"></span>

<div id="answer-container-25595" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25595-score" class="post-score" title="current number of votes">0</div><span id="post-25595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're using a firewall on the Windows 7 system, I'd certainly suspect that might be the problem.</p><p>Can you disable the firewall temporarily to see if that improves matters ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Oct '13, 08:47</strong> </span></p></div></div><div id="comments-container-25595" class="comments-container"></div><div id="comment-tools-25595" class="comment-tools"></div><div class="clear"></div><div id="comment-25595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

