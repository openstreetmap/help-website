+++
type = "question"
title = "wireless card not detected, and cannot capture low-level traffic"
description = '''I&#x27;m running Wireshark 1.2.4 on Windows 7 and I have WinPcap 4.1.1 installed. In Wireshark only the following three interfaces are listed: &quot;Microsoft&quot; &quot;NDIS-WDM Driver for HighSpeed USB-Ethernet Adapter&quot; &quot;Realtek RTL8102/8103 Family PCI-E FE NIC&quot; It doesn&#x27;t list the wireless card inside my Dell lapto...'''
date = "2012-02-17T07:02:00Z"
lastmod = "2012-02-17T09:02:00Z"
weight = 9093
keywords = [ "wireless" ]
aliases = [ "/questions/9093" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireless card not detected, and cannot capture low-level traffic](/questions/9093/wireless-card-not-detected-and-cannot-capture-low-level-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9093-score" class="post-score" title="current number of votes">0</div><span id="post-9093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Wireshark 1.2.4 on Windows 7 and I have WinPcap 4.1.1 installed. In Wireshark only the following three interfaces are listed: "Microsoft" "NDIS-WDM Driver for HighSpeed USB-Ethernet Adapter" "Realtek RTL8102/8103 Family PCI-E FE NIC"</p><p>It doesn't list the wireless card inside my Dell laptop, the wireless card which is listed in Control Panel as "Dell Wireless 1520 Wireless-N WLAN Mini-Card" (and through which I am currently connected).</p><p>Now, I'm able to select "Microsoft" as the interface I want to capture, and it will display packets sent and received. However, my problem is that I want to test a program called Psiphon (Psiphon.ca) which automatically establishes a VPN or SSH connection to a remote IP address. I want to use Wireshark to determine what IP address it's connecting to. However, if I capture the "Microsoft" interface while I'm connected through that VPN, and I load a site like www.peacefire.org, Wireshark captures packets showing their destination as 69.72.177.140 (the IP of www.peacefire.org), even though that's NOT where the packets are actually being sent to from my machine. The packets are being sent to whatever VPN server I'm connected through.</p><p>I assume this is because when the "Microsoft" interface is selected, Wireshark captures traffic at the high level that the Internet Explorer API thinks it's sending traffic to, not at the low level of the IP address that my wireless card thinks it's sending traffic to.</p><p>So, any idea why my wireless card isn't listed and how to capture traffic at the low level that I want, to see what IP address the VPN software is connecting to?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/82151f68754805aef7d137705c16e16b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bennetthaselton&#39;s gravatar image" /><p><span>bennetthaselton</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bennetthaselton has no accepted answers">0%</span></p></div></div><div id="comments-container-9093" class="comments-container"></div><div id="comment-tools-9093" class="comment-tools"></div><div class="clear"></div><div id="comment-9093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9094"></span>

<div id="answer-container-9094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9094-score" class="post-score" title="current number of votes">0</div><span id="post-9094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Windows is a bit difficult wrt capturing on wireless interfaces. See the <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WLAN</a> capture page on the Wiki for more info.</p><p>Edit:</p><p>I did a little more checking on my Dell Laptop, the "Microsoft" interface is probably the MS ISATAP pseudo interface for IPv6 tunnelling. My wireless card (a 6205) does show up, a colleagues 1501 doesn't. I'm guessing it's a driver/NDIS issue.</p><p>The only other option I have to offer is to try Network Monitor from MS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '12, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '12, 07:51</strong> </span></p></div></div><div id="comments-container-9094" class="comments-container"></div><div id="comment-tools-9094" class="comment-tools"></div><div class="clear"></div><div id="comment-9094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9097"></span>

<div id="answer-container-9097" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9097-score" class="post-score" title="current number of votes">0</div><span id="post-9097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>also try the version of WinPCAP (4.1.2) and the new version of Wiresharl (1.6.5)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '12, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/b119c1795a1d51f2d7d0aa7af9c54a9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dixglata&#39;s gravatar image" /><p><span>dixglata</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dixglata has no accepted answers">0%</span></p></div></div><div id="comments-container-9097" class="comments-container"></div><div id="comment-tools-9097" class="comment-tools"></div><div class="clear"></div><div id="comment-9097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

