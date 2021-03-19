+++
type = "question"
title = "Can&#x27;t seem to capture only http traffic with wireless card"
description = '''Hey there, I am running Kali linux and I have a TP-Link USB adapter. I have also started airmon-ng for the wlan adapter, then selected it in Wireshark and started a capture. I can see all sorts of broadcast traffic on the 802.11 network but if I want to filter with something like tcp.port==80 that w...'''
date = "2014-05-21T06:08:00Z"
lastmod = "2014-05-25T11:30:00Z"
weight = 32951
keywords = [ "wireless", "wireshark", "linux" ]
aliases = [ "/questions/32951" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't seem to capture only http traffic with wireless card](/questions/32951/cant-seem-to-capture-only-http-traffic-with-wireless-card)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32951-score" class="post-score" title="current number of votes">0</div><span id="post-32951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there,</p><p>I am running Kali linux and I have a TP-Link USB adapter. I have also started airmon-ng for the wlan adapter, then selected it in Wireshark and started a capture. I can see all sorts of broadcast traffic on the 802.11 network but if I want to filter with something like tcp.port==80 that won't work. I have a test laptop next to me and I would like to be able to see the HTTP traffic that is sent from that when they are both connected to the same network</p><p>Is there a way I can get the card to see the actual protocol being used as it does when connected via ethernet? Right now the whole protocol column is 802.11 instead of seeing things like HTTP, HTTPS, SNMP, etc.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '14, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/d2aafd4e993622cbae80753269d04589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fac3l3ss&#39;s gravatar image" /><p><span>fac3l3ss</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fac3l3ss has no accepted answers">0%</span></p></div></div><div id="comments-container-32951" class="comments-container"></div><div id="comment-tools-32951" class="comment-tools"></div><div class="clear"></div><div id="comment-32951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33067"></span>

<div id="answer-container-33067" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33067-score" class="post-score" title="current number of votes">0</div><span id="post-33067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I can see all sorts of broadcast traffic on the 802.11 network but if I want to filter with something like tcp.port==80 that won't work.</p></blockquote><p>sounds like your wifi traffic is encrypted. Do you have to enter a password while you connect to the wifi network?</p><p>If so, please read the wifi/wlan decryption Wiki.</p><blockquote><p><a href="http://wiki.wireshark.org/HowToDecrypt802.11">http://wiki.wireshark.org/HowToDecrypt802.11</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '14, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33067" class="comments-container"></div><div id="comment-tools-33067" class="comment-tools"></div><div class="clear"></div><div id="comment-33067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

