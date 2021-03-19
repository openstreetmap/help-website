+++
type = "question"
title = "15-75% of captured packets are ARP requests"
description = '''I ran a packet capture on my wired network today. Each floor is separated into a /23 space and we&#x27;re not even at 50% usage (many users prefer wireless). The capture I ran showed anywhere between 15-75% of total packets were ARP requests.  The source/destination ip&#x27;s vary, but for example if I filter...'''
date = "2016-07-13T16:42:00Z"
lastmod = "2016-07-14T01:09:00Z"
weight = 54049
keywords = [ "arp", "packets", "excessive" ]
aliases = [ "/questions/54049" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [15-75% of captured packets are ARP requests](/questions/54049/15-75-of-captured-packets-are-arp-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54049-score" class="post-score" title="current number of votes">0</div><span id="post-54049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran a packet capture on my wired network today. Each floor is separated into a /23 space and we're not even at 50% usage (many users prefer wireless). The capture I ran showed anywhere between 15-75% of total packets were ARP requests.<br />
</p><p>The source/destination ip's vary, but for example if I filter by one arp destination address, I see one host querying for another every 1.2 seconds or so and making up 0.5% of the total packets captured. Obviously no one is replying to this host, so it is sending out the same ARP query over and over. Other hosts are also querying for the same destination host as well, and there are multiple destinations being queried for. It's not all the same source/destination.</p><p>I could enable broadcast storm-control on our switches, but I don't think that would solve the root of the problem, which seems to be that we're seeing so much of this type of traffic. What is strange here is that the hosts being queried for appear to be DHCP clients or standard users, so I'm not sure why other clients are querying for them.</p><p>Any thoughts on this traffic, or what could be done to stop it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-excessive" rel="tag" title="see questions tagged &#39;excessive&#39;">excessive</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '16, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/e28941c3afd088cba75c9885d82ba5a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pwz&#39;s gravatar image" /><p><span>pwz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pwz has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-54049" class="comments-container"></div><div id="comment-tools-54049" class="comment-tools"></div><div class="clear"></div><div id="comment-54049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54050"></span>

<div id="answer-container-54050" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54050-score" class="post-score" title="current number of votes">1</div><span id="post-54050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pwz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you use a Monitor/SPAN port, or just captured plugged in into a random port? Because if you do not did not mirror traffic you'll only see broadcast and multicast. That also explains why you see no ARP answers, because they are unicast and you won't see them without a montior/SPAN session.</p><p>See this page for more information about how to capture: <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '16, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '16, 16:47</strong> </span></p></div></div><div id="comments-container-54050" class="comments-container"><span id="54051"></span><div id="comment-54051" class="comment"><div id="post-54051-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>That is a good point -- I did only capture from a random switch port which captured broadcasts visible, but not unicast arp replies. Still, it is my understanding that arp requests unanswered would prompt another arp request, which is what we are seeing.</p><p>Tomorrow I plan to perform a SPAN session with the user who brought the original issue to our attention. I hope to be able to compare their traffic to my own, and potentially find the root cause of the original issue.</p><p>Thank you for replying, it is the correct answer for the question I asked and I will mark it as such.</p><p>pwz</p></div><div id="comment-54051-info" class="comment-info"><span class="comment-age">(13 Jul '16, 19:11)</span> <span class="comment-user userinfo">pwz</span></div></div><span id="54058"></span><div id="comment-54058" class="comment"><div id="post-54058-score" class="comment-score"></div><div class="comment-text"><p>if you have the SPAN session you should see the ARP answers. If not you need to find out why not (the most common reasons is a wrong subnet mask, meaning that the source node thinks it can reach the destination directly while it can't). If you see the answers you need to find out why they aren't cached.</p></div><div id="comment-54058-info" class="comment-info"><span class="comment-age">(14 Jul '16, 01:09)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-54050" class="comment-tools"></div><div class="clear"></div><div id="comment-54050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

