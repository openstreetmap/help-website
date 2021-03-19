+++
type = "question"
title = "I can not see ipv4 and http, I can just see ipv6 and SSDP WHY ?"
description = '''Hi ! I have a real huge problem, when I am connected through the wireless of my university, I can just see adresses like this : 1823731 14856.287768 fe80::74b6:2d79:4343:41e1 ff02::c SSDP 208 M-SEARCH * HTTP/1.1  Here is a picture to understand more :  How Can I solve this problem ? Because I want t...'''
date = "2012-03-01T12:45:00Z"
lastmod = "2012-03-02T01:18:00Z"
weight = 9296
keywords = [ "ssdp", "http", "ipv4", "ipv6" ]
aliases = [ "/questions/9296" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I can not see ipv4 and http, I can just see ipv6 and SSDP WHY ?](/questions/9296/i-can-not-see-ipv4-and-http-i-can-just-see-ipv6-and-ssdp-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9296-score" class="post-score" title="current number of votes">0</div><span id="post-9296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ! I have a real huge problem, when I am connected through the wireless of my university, I can just see adresses like this :</p><p>1823731 14856.287768 fe80::74b6:2d79:4343:41e1 ff02::c SSDP 208 M-SEARCH * HTTP/1.1</p><p>Here is a picture to understand more :</p><p><img src="http://data.imagup.com/12/1145300151.jpg" alt="alt text" /></p><p>How Can I solve this problem ? Because I want to see the IP ADDRESS connected in the same wireless. Thank you !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssdp" rel="tag" title="see questions tagged &#39;ssdp&#39;">ssdp</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '12, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/68b0fdc74a63c214b76c58b11385d097?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WIRELOVER&#39;s gravatar image" /><p><span>WIRELOVER</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WIRELOVER has no accepted answers">0%</span></p></img></div></div><div id="comments-container-9296" class="comments-container"></div><div id="comment-tools-9296" class="comment-tools"></div><div class="clear"></div><div id="comment-9296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9300"></span>

<div id="answer-container-9300" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9300-score" class="post-score" title="current number of votes">0</div><span id="post-9300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you have an IPv6 address and that's what all the traffic is running over. Those long strings in the source and destination columns like fe80::74b6:2d79:4343:41e1 and ff02::c are really the IP addresses!</p><p>Here is, aptly named, <a href="http://arstechnica.com/hardware/news/2007/03/IPv6.ars">everything you need to know about IPv6</a></p><p>Is it possible that you only have an IPv6 address on the 'en1' interface? In the terminal, you can check by running <code>ifconfig en1</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '12, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p><span>zachad</span><br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Mar '12, 20:35</strong> </span></p></div></div><div id="comments-container-9300" class="comments-container"><span id="9305"></span><div id="comment-9305" class="comment"><div id="post-9305-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer, but still I can not see the http addresses, the cookie.... After running the command in the terminal I receive this.</p><p><code>en1: flags=8863 &lt;up,broadcast,smart,running,simplex,multicast&gt; mtu 1500          ether c2:bc:c5:e1:d3:72         inet6 fe80::cabc:c8ff:fee2:d377%en1 prefixlen 64 scopeid 0x5          inet 192.168.24.41 netmask 0xffffff00 broadcast 192.168.24.255          media: autoselect          status: active</code></p><p>Any Idea ?</p></div><div id="comment-9305-info" class="comment-info"><span class="comment-age">(02 Mar '12, 01:18)</span> <span class="comment-user userinfo">WIRELOVER</span></div></div></div><div id="comment-tools-9300" class="comment-tools"></div><div class="clear"></div><div id="comment-9300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

