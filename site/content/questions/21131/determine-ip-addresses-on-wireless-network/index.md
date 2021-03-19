+++
type = "question"
title = "Determine IP Addresses on Wireless Network."
description = '''I would like to capture the traffic of one wireless device on my wireless network. I have placed a switch between the Wireless router and my DSL modem and am port forwarding traffic to a laptop. When I capture traffic all I see is the IP address of the Wireless router. Is there a way to capture just...'''
date = "2013-05-14T06:28:00Z"
lastmod = "2013-05-15T12:33:00Z"
weight = 21131
keywords = [ "wireless" ]
aliases = [ "/questions/21131" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Determine IP Addresses on Wireless Network.](/questions/21131/determine-ip-addresses-on-wireless-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21131-score" class="post-score" title="current number of votes">0</div><span id="post-21131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to capture the traffic of one wireless device on my wireless network. I have placed a switch between the Wireless router and my DSL modem and am port forwarding traffic to a laptop. When I capture traffic all I see is the IP address of the Wireless router. Is there a way to capture just the traffic of the one wireless device?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '13, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/6e7b0ab603de0bc2e18b2191450d8400?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tanuki&#39;s gravatar image" /><p><span>Tanuki</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tanuki has no accepted answers">0%</span></p></div></div><div id="comments-container-21131" class="comments-container"></div><div id="comment-tools-21131" class="comment-tools"></div><div class="clear"></div><div id="comment-21131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21132"></span>

<div id="answer-container-21132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21132-score" class="post-score" title="current number of votes">0</div><span id="post-21132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you're capturing the packets after they have been through the Network Address Translation (NAT) process. In that process the internal IPs are replaced with your public IP. Unfortunately you cannot capture the internal IP addresses on the outside of a NAT gateway. The only workaround is to dump the NAT table to see what external connection represents what internal connection, but not all devices support this, and it is tedious work.</p><p>It may be easier to try and capture the WiFi traffic directly, but that is a bit more complicated. On Windows you'd need an AirPCAP adapter, while on Linux etc. you need to enable monitor mode manually before running Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21132" class="comments-container"><span id="21157"></span><div id="comment-21157" class="comment"><div id="post-21157-score" class="comment-score"></div><div class="comment-text"><blockquote><p>while on Linux etc. you need to enable monitor mode manually before running Wireshark.</p></blockquote><p>...and while on OS X you need to check the monitor mode checkbox (that doesn't currently work on most Linux systems, for various reasons; it may work on some *BSD systems, but not all).</p></div><div id="comment-21157-info" class="comment-info"><span class="comment-age">(15 May '13, 12:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="21158"></span><div id="comment-21158" class="comment"><div id="post-21158-score" class="comment-score"></div><div class="comment-text"><p>Note also that on a "protected" network (i.e., a network using WEP or WPA/WPA2, on which the traffic is encrypted), you will have to <a href="http://wiki.wireshark.org/HowToDecrypt802.11">arrange that the traffic can be decrypted</a>.</p></div><div id="comment-21158-info" class="comment-info"><span class="comment-age">(15 May '13, 12:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-21132" class="comment-tools"></div><div class="clear"></div><div id="comment-21132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21133"></span>

<div id="answer-container-21133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21133-score" class="post-score" title="current number of votes">0</div><span id="post-21133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As <span>@Jasper</span> said, your wireless router is doing NAT. If your DSL modem is also doing NAT, then you could decide to configure your wireless router to work in bridging mode. That way, the traffic from the wireless clients will no longer be translated and you can use the current capture setup to monitor a specific client.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '13, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21133" class="comments-container"><span id="21137"></span><div id="comment-21137" class="comment"><div id="post-21137-score" class="comment-score"></div><div class="comment-text"><p>Thank you both for your help. I will try putting the router in bridge mode tonight and report back tomorrow.</p></div><div id="comment-21137-info" class="comment-info"><span class="comment-age">(14 May '13, 09:33)</span> <span class="comment-user userinfo">Tanuki</span></div></div></div><div id="comment-tools-21133" class="comment-tools"></div><div class="clear"></div><div id="comment-21133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

