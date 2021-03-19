+++
type = "question"
title = "How widespread is gratuitous ARP implementation?"
description = '''When I change the IPv4 address on my Juniper router interface, it causes router to send out the gratuitous ARP message: 17:30:25.567297 00:19:e2:9f:ed:f0 &amp;gt; ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.10.10.126 tell 10.10.10.126, length 46 17:32:39.938593 00:19:e2:9f:e...'''
date = "2013-03-06T08:32:00Z"
lastmod = "2013-03-06T09:09:00Z"
weight = 19224
keywords = [ "arp" ]
aliases = [ "/questions/19224" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How widespread is gratuitous ARP implementation?](/questions/19224/how-widespread-is-gratuitous-arp-implementation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19224-score" class="post-score" title="current number of votes">0</div><span id="post-19224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I change the IPv4 address on my Juniper router interface, it causes router to send out the gratuitous ARP message:</p><pre><code>17:30:25.567297 00:19:e2:9f:ed:f0 &gt; ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.10.10.126 tell 10.10.10.126, length 46
17:32:39.938593 00:19:e2:9f:ed:f0 &gt; ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.10.10.65 tell 10.10.10.65, length 46</code></pre><p>As you can see, I first set the IPv4 address to 10.10.10.126 and then changed it to 10.10.10.65. However, are there operating-system platforms, which do not send gratuitous ARP message in case IPv4 address is changed?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '13, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/c153148e19e1e7c04c48a2a5c4f68b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrtn&#39;s gravatar image" /><p><span>mrtn</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrtn has no accepted answers">0%</span></p></div></div><div id="comments-container-19224" class="comments-container"></div><div id="comment-tools-19224" class="comment-tools"></div><div class="clear"></div><div id="comment-19224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19230"></span>

<div id="answer-container-19230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19230-score" class="post-score" title="current number of votes">3</div><span id="post-19230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>RFC 5227 requires every host to perform IP address conflict detection before beginning to use an IPv4 address, regardless of how that address is assigned (manually, DHCP, other). See section 2.1 of the RFC. Almost all implementations perform the IP address conflict detection by sending gratuitous ARPs. Technically, this is an error, because the RFC requires them to send ARP probes instead of gratuitous ARPs, but using gratuitous ARPs for this purpose is accepted practice.</p><p>In a gratuitous ARP, the target IP address and the sender IP address are the same. In an ARP probe, the sender IP address is 0.0.0.0.</p><p>So there <em>should not be</em> any operating systems that don't perform IP address conflict detection with either a gratuitous ARP or an ARP probe when their IP address is changed. Given the wide variety of implementations, complete with bugs, it wouldn't surprise me if somewhere there is a non-compliant implementation that does not conform to this requirement.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '13, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Mar '13, 19:08</strong> </span></p></div></div><div id="comments-container-19230" class="comments-container"></div><div id="comment-tools-19230" class="comment-tools"></div><div class="clear"></div><div id="comment-19230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19227"></span>

<div id="answer-container-19227" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19227-score" class="post-score" title="current number of votes">0</div><span id="post-19227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>However, are there operating-system platforms, which do not send gratuitous ARP message in case IPv4 address is changed?</p></blockquote><p>a gratuitous ARP is sent by many (current) OSes while the system boots and if the link of an interface goes down and comes back up. I don't think there is a requirement in any RFC to send an gratuitous ARP after an IP change. So, you may or may not see such an ARP after an IP change. Some loadbalancer and/or cluster software will issue a gratuitous ARP after a failover has taken place, but that depends on the software used and also it's configuration.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '13, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19227" class="comments-container"></div><div id="comment-tools-19227" class="comment-tools"></div><div class="clear"></div><div id="comment-19227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

