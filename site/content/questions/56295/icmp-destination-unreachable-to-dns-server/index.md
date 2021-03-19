+++
type = "question"
title = "ICMP destination unreachable to DNS server?"
description = '''Hi, Could someone validate the explanation given in 2007 (3rd post) https://community.barracudanetworks.com/forum/index.php?/topic/8683-icmp-destination-unreachable-to-dns-server/ for the last ICMP packet in the DNS trace? I am seeing similar behavior on a Windows client.  https://www.dropbox.com/s/...'''
date = "2016-10-11T08:53:00Z"
lastmod = "2016-10-11T11:12:00Z"
weight = 56295
keywords = [ "icmp", "dns" ]
aliases = [ "/questions/56295" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP destination unreachable to DNS server?](/questions/56295/icmp-destination-unreachable-to-dns-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56295-score" class="post-score" title="current number of votes">0</div><span id="post-56295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Could someone validate the explanation given in 2007 (3rd post) <a href="https://community.barracudanetworks.com/forum/index.php?/topic/8683-icmp-destination-unreachable-to-dns-server/">https://community.barracudanetworks.com/forum/index.php?/topic/8683-icmp-destination-unreachable-to-dns-server/</a> for the last ICMP packet in the DNS trace?</p><p>I am seeing similar behavior on a Windows client. <a href="https://www.dropbox.com/s/aef1rbjuj5lz1bj/dns_icmp.pcapng?dl=0">https://www.dropbox.com/s/aef1rbjuj5lz1bj/dns_icmp.pcapng?dl=0</a></p><p>Windows Client - 192.168.30.124 Windows DNS Server - 192.168.30.5</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '16, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p><span>net_tech</span><br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-56295" class="comments-container"></div><div id="comment-tools-56295" class="comment-tools"></div><div class="clear"></div><div id="comment-56295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56301"></span>

<div id="answer-container-56301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56301-score" class="post-score" title="current number of votes">1</div><span id="post-56301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I totally agree with that explanation. The DNS client's timeout for arrival of a DNS response does exist, and in your case it is shorter than the server's response time. After expiration of that timeout the client unbinds from the socket, causing <code>icmp destination unreachable</code> to be sent in response to anything arriving to that socket, including a valid DNS response.</p><p>If you are interested in details, you can create a batch file like</p><pre><code>@echo off
for /l %%x in (1, 1, 60) do (
   echo %%x
   netstat -p udp
   timeout 1
)</code></pre><p>run it with output redirected to a file and initiate, from another window, the DNS query which you know will fail this way. In the output file, you should see for how long the DNS client keeps the socket open.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '16, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56301" class="comments-container"></div><div id="comment-tools-56301" class="comment-tools"></div><div class="clear"></div><div id="comment-56301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

