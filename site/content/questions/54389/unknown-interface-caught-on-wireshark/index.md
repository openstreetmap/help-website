+++
type = "question"
title = "unknown interface caught on wireshark"
description = '''i am using win7 operating system connected wireless to zte F660. when trying to sniff the traffic using wireshark , i&#x27;ve capture lots of ARP request from unknown interface, which is not exist on my router neither on my window host client. below is the screenshot: the unknown interface shows &quot;78:19:f...'''
date = "2016-07-27T17:58:00Z"
lastmod = "2016-07-30T19:01:00Z"
weight = 54389
keywords = [ "interface", "vlan", "juniper", "wireshark" ]
aliases = [ "/questions/54389" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [unknown interface caught on wireshark](/questions/54389/unknown-interface-caught-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54389-score" class="post-score" title="current number of votes">0</div><span id="post-54389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am using win7 operating system connected wireless to zte F660.</p><p>when trying to sniff the traffic using wireshark , i've capture lots of ARP request from unknown interface, which is not exist on my router neither on my window host client.</p><p>below is the screenshot:</p><p>the unknown interface shows "<strong>78:19:f7:40:b7:c5</strong>" as its mac address <a href="http://imgur.com/a/Nsyrp">http://imgur.com/a/Nsyrp</a></p><p><strong>my lan interface</strong> <a href="http://imgur.com/a/8NKMF">http://imgur.com/a/8NKMF</a></p><p><strong>my wlan interface</strong> <a href="http://imgur.com/a/EMCzl">http://imgur.com/a/EMCzl</a></p><p>I'm not an network administrator and i hope someone can light me up.</p><p>i really appreciate for your help.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-juniper" rel="tag" title="see questions tagged &#39;juniper&#39;">juniper</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '16, 17:58</strong></p><img src="https://secure.gravatar.com/avatar/4cd0c5aa1d71c1556ef3415f9992ad50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="noobie&#39;s gravatar image" /><p><span>noobie</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="noobie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '16, 17:59</strong> </span></p></div></div><div id="comments-container-54389" class="comments-container"><span id="54392"></span><div id="comment-54392" class="comment"><div id="post-54392-score" class="comment-score"></div><div class="comment-text"><p>Cable modem user?</p></div><div id="comment-54392-info" class="comment-info"><span class="comment-age">(27 Jul '16, 22:37)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="54462"></span><div id="comment-54462" class="comment"><div id="post-54462-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Jaap</span>, yes sir</p><p>it is ADSL fiber optic modem,and i connect using wifi to the modem.</p><p>it is strange because i catch lots of internal ips with different range than my network</p></div><div id="comment-54462-info" class="comment-info"><span class="comment-age">(30 Jul '16, 11:49)</span> <span class="comment-user userinfo">noobie</span></div></div></div><div id="comment-tools-54389" class="comment-tools"></div><div class="clear"></div><div id="comment-54389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54466"></span>

<div id="answer-container-54466" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54466-score" class="post-score" title="current number of votes">0</div><span id="post-54466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the strange subnet ARP packets, it looks like there are at least 5 devices.</p><p>Two IP senders [10.11.48.2 &amp; 10.11.48.3] and they are asking for three other devices MAC address [10.11.50.43, 10.11.51.28 &amp; 10.11.51.220]. So it's most likely that they are all on a subnet 10.11.48.0/22 (range: 10.11.48.1 ~ 10.11.51.255).</p><p>Also look at your LAN 4 interface. It doesn't show IP address of that interface, but you can see both send &amp; receive traffic (and not in any small numbers either).</p><p>But as you're attached to WLAN on subnet 192.168.0.0/16, these packets shouldn't be broadcast to you at all as it's an entirely different subnet.</p><p>Likewise, the strange ARP request packets don't have any replies over a several minute span meaning that this is only 1 way traffic you're seeing. That too is strange because the ARP requesting devices have a specific IP whom they are probably talking to and thus there should be two way traffic. But that's not the case.</p><p>As such, I recommend you look at the IP settings for your LAN 4 first and if it is in the 10.11.48.0/22 range, then perhaps your router is set to bridging mode?</p><p>And if LAN 4 is NOT in the 10.11.48.0/22 range, then perhaps somebody elses wireless packets are bleeding over and you're picking them up and capturing them. But if you don't use 10.11.48.0/22 subnet range, then there will be no route from your router to that subnet and thus you will only see one way incoming packets, but no returned packets which is what this looks like.</p><p>FWIW</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '16, 19:01</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-54466" class="comments-container"></div><div id="comment-tools-54466" class="comment-tools"></div><div class="clear"></div><div id="comment-54466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

