+++
type = "question"
title = "New user needs help identifying IP address to setup Ethernet Network"
description = '''Please help me as I&#x27;m fairly new to this type of thing. I have a Windows 7 laptop and I need to use a cross-over cable to connect to another device via FTP. I need to download firmware to the memory of that device. Any way, the FTP of that device is unknown. Can I use Wireshark to capture that IP ad...'''
date = "2012-11-13T08:22:00Z"
lastmod = "2012-11-13T14:07:00Z"
weight = 15873
keywords = [ "unknown", "ftp", "cross-over", "cable", "ethernet" ]
aliases = [ "/questions/15873" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [New user needs help identifying IP address to setup Ethernet Network](/questions/15873/new-user-needs-help-identifying-ip-address-to-setup-ethernet-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15873-score" class="post-score" title="current number of votes">0</div><span id="post-15873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please help me as I'm fairly new to this type of thing. I have a Windows 7 laptop and I need to use a cross-over cable to connect to another device via FTP. I need to download firmware to the memory of that device. Any way, the FTP of that device is unknown. Can I use Wireshark to capture that IP address so that I can setup the ethernet network and then use my cross-over cable to connect and make the needed file transfer? If anyone can help please list the steps in detail on how I do this. I downloaded Wireshark ver 1.8.3, but I'm not really sure where to begin. I did click the START button and I checked all the available capture devices but there is so much scrolling and so many IPs I'm lost at this point.</p><p>Thanks for any guidance you can provide.</p><p>Regards,</p><p>Bill.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span> <span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-cross-over" rel="tag" title="see questions tagged &#39;cross-over&#39;">cross-over</span> <span class="post-tag tag-link-cable" rel="tag" title="see questions tagged &#39;cable&#39;">cable</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '12, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/c60231d599759a80963fd529158d69ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="semiturbo&#39;s gravatar image" /><p><span>semiturbo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="semiturbo has no accepted answers">0%</span></p></div></div><div id="comments-container-15873" class="comments-container"></div><div id="comment-tools-15873" class="comment-tools"></div><div class="clear"></div><div id="comment-15873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15875"></span>

<div id="answer-container-15875" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15875-score" class="post-score" title="current number of votes">0</div><span id="post-15875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you at least know the MAC address of the interface of the device you want to FTP to, that would help. Anyway, you could setup your cross-over cable right away and have a look with Wireshark what comes up on the laptop. That would keep out all the other traffic.</p><p>If the device gets its IP address dynamically, then it probably falls back to a default when no DHCP server is around. Maybe you need to powercycle the device to trigger it to send something, or use a broadcast ping to poke it for an ARP response. This should tell you something about its IP address</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '12, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-15875" class="comments-container"><span id="15876"></span><div id="comment-15876" class="comment"><div id="post-15876-score" class="comment-score"></div><div class="comment-text"><p>Thank you. The MAC Address I found on a chip shows to be 00-60-A9-00-08-80. What would I do ith that information to help me? How do a do a broadcast ping? I assume I do this from CMD prompt but not sure what the procedure is. Sorry, I'm pretty much a novice at this.</p></div><div id="comment-15876-info" class="comment-info"><span class="comment-age">(13 Nov '12, 09:14)</span> <span class="comment-user userinfo">semiturbo</span></div></div><span id="15877"></span><div id="comment-15877" class="comment"><div id="post-15877-score" class="comment-score"></div><div class="comment-text"><p>I tried another laptop (Windows XP) and got a smaller list of information from Wireshark. When I power cycled the unit the first numbers that came up were 0.0.0.0 255.255.255.255. Looks like the IP address is not setup on the unit I'm trying to connect to. If I know the MAC Address is there a way for me to set the IP address so I can then connect to it? Thanks.</p></div><div id="comment-15877-info" class="comment-info"><span class="comment-age">(13 Nov '12, 10:26)</span> <span class="comment-user userinfo">semiturbo</span></div></div><span id="15880"></span><div id="comment-15880" class="comment"><div id="post-15880-score" class="comment-score"></div><div class="comment-text"><p>Ok, so your device needs a DHCP server. Well then, have Wireshark capture the network interface, powercycle the device and use the following display filter: eth.addr == 00:60:A9:00:08:80. You probably see an ARP request for the IP address it's assigned.</p></div><div id="comment-15880-info" class="comment-info"><span class="comment-age">(13 Nov '12, 14:07)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-15875" class="comment-tools"></div><div class="clear"></div><div id="comment-15875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

