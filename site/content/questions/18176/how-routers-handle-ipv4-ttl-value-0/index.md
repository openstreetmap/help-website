+++
type = "question"
title = "How routers handle IPv4 TTL value 0"
description = '''I have a following setup:  If I send IPv4 packets with TTL value 0 from T60 I receive: ICMP time exceeded in-transit  ..message from 10.10.10.2(R1) as I should. Now if I send IPv4 packets with TTL value 1 from T60 I receive once again: ICMP time exceeded in-transit  message from 10.10.10.2(R1). If I...'''
date = "2013-01-31T04:20:00Z"
lastmod = "2014-09-02T00:37:00Z"
weight = 18176
keywords = [ "ip", "ttl" ]
aliases = [ "/questions/18176" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How routers handle IPv4 TTL value 0](/questions/18176/how-routers-handle-ipv4-ttl-value-0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18176-score" class="post-score" title="current number of votes">0</div><span id="post-18176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a following setup:</p><p><img src="http://s4.postimage.org/yox35cbbh/TTL_test.png" alt="http://s4.postimage.org/yox35cbbh/TTL_test.png" /></p><p>If I send IPv4 packets with TTL value 0 from <strong>T60</strong> I receive:</p><pre><code>ICMP time exceeded in-transit</code></pre><p>..message from 10.10.10.2(R1) as I should. Now if I send IPv4 packets with TTL value 1 from <strong>T60</strong> I receive once again:</p><pre><code>ICMP time exceeded in-transit</code></pre><p>message from 10.10.10.2(R1). If I change TTL to 2, then I receive</p><pre><code>ICMP time exceeded in-transit</code></pre><p>..from 10.10.11.2(R2).</p><p>Looks like routers do not send out packets with TTL value of 0. Am I correct that the reason for this is that <strong>before</strong> router will send the packet it reduces the TTL by one and if it sees that the TTL value became 0, it will process the packet further and will not send the packet towards destination, but sends ICMP error message back to the source IP instead? This means that it's not possible to send packets with TTL value of 0 to hosts which are not in the same broadcast domain with the sender?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-ttl" rel="tag" title="see questions tagged &#39;ttl&#39;">ttl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '13, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/c153148e19e1e7c04c48a2a5c4f68b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrtn&#39;s gravatar image" /><p><span>mrtn</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrtn has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jan '13, 04:21</strong> </span></p></div></div><div id="comments-container-18176" class="comments-container"></div><div id="comment-tools-18176" class="comment-tools"></div><div class="clear"></div><div id="comment-18176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18177"></span>

<div id="answer-container-18177" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18177-score" class="post-score" title="current number of votes">1</div><span id="post-18177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrtn has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Routers always decrement the TTL by 1 and forward the packet if the new TTL is greater than zero. If it is zero, some routers issue a ICMP time exceeded in transit packet as you've noticed, but some don't (mostly for security reasons). It is not possible to send IP packets to hosts in other broadcast domains if the TTL is less than 2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '13, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jan '13, 04:28</strong> </span></p></div></div><div id="comments-container-18177" class="comments-container"></div><div id="comment-tools-18177" class="comment-tools"></div><div class="clear"></div><div id="comment-18177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35924"></span>

<div id="answer-container-35924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35924-score" class="post-score" title="current number of votes">0</div><span id="post-35924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>IPv4 TTL value 0 , when set to 0 the packet will not even leave the current host , so in this case its rejected at T60 level itself. When you set TTL 1 , it reaches till Fa0/0 on R1 (10.10.10.2) and R1 deducts 1 from it , hence making it zero again and you receive ICMP time exceeded in-transit from 10.10.10.2 this time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '14, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/3d479605b028eeddf5fe6db3ff9a7908?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unixmaster&#39;s gravatar image" /><p><span>unixmaster</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unixmaster has no accepted answers">0%</span></p></div></div><div id="comments-container-35924" class="comments-container"></div><div id="comment-tools-35924" class="comment-tools"></div><div class="clear"></div><div id="comment-35924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

