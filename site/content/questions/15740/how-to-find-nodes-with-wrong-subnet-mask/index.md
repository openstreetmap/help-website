+++
type = "question"
title = "how to find nodes with wrong subnet mask"
description = '''how would i filter a capture to find what nodes have the wrong subnet mask? i.e my network is 10.128.5.x / 255.255.255.0 but a client is misconfigured using 255.255.0.0 '''
date = "2012-11-08T12:16:00Z"
lastmod = "2012-11-08T23:53:00Z"
weight = 15740
keywords = [ "subnet", "capture-filter", "mask" ]
aliases = [ "/questions/15740" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to find nodes with wrong subnet mask](/questions/15740/how-to-find-nodes-with-wrong-subnet-mask)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15740-score" class="post-score" title="current number of votes">0</div><span id="post-15740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how would i filter a capture to find what nodes have the wrong subnet mask? i.e my network is 10.128.5.x / 255.255.255.0 but a client is misconfigured using 255.255.0.0</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-subnet" rel="tag" title="see questions tagged &#39;subnet&#39;">subnet</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-mask" rel="tag" title="see questions tagged &#39;mask&#39;">mask</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '12, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/e0c59165eb1ef458114b01959e1a0ce4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pcmonkey&#39;s gravatar image" /><p><span>pcmonkey</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pcmonkey has no accepted answers">0%</span></p></div></div><div id="comments-container-15740" class="comments-container"></div><div id="comment-tools-15740" class="comment-tools"></div><div class="clear"></div><div id="comment-15740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="15741"></span>

<div id="answer-container-15741" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15741-score" class="post-score" title="current number of votes">1</div><span id="post-15741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can find wrong subnetmasks either by finding for ARP requests that are looking for MAC addresses of IP addresses they should not be able to reach directly (which is your case), or by finding ICMP redirect messages from default gateways that tell clients to talk to the target node directly (if the mask is too narrow).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '12, 12:19</strong> </span></p></div></div><div id="comments-container-15741" class="comments-container"><span id="15742"></span><div id="comment-15742" class="comment"><div id="post-15742-score" class="comment-score"></div><div class="comment-text"><p>So i make a filter for icmp.redir_gw ??</p></div><div id="comment-15742-info" class="comment-info"><span class="comment-age">(08 Nov '12, 12:29)</span> <span class="comment-user userinfo">pcmonkey</span></div></div><span id="15758"></span><div id="comment-15758" class="comment"><div id="post-15758-score" class="comment-score"></div><div class="comment-text"><p>you could filter for icmp.type==5, because type 5 is a redirect message. And if you combine that with an IP filter on your default gateway you should be able to spot these things.</p></div><div id="comment-15758-info" class="comment-info"><span class="comment-age">(08 Nov '12, 23:53)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-15741" class="comment-tools"></div><div class="clear"></div><div id="comment-15741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15743"></span>

<div id="answer-container-15743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15743-score" class="post-score" title="current number of votes">0</div><span id="post-15743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you for something like <strong>arp and not arp.dst.proto_ipv4 == 10.128.5.0/24</strong> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-15743" class="comments-container"><span id="15744"></span><div id="comment-15744" class="comment"><div id="post-15744-score" class="comment-score"></div><div class="comment-text"><p>I will try that packethunter</p></div><div id="comment-15744-info" class="comment-info"><span class="comment-age">(08 Nov '12, 13:48)</span> <span class="comment-user userinfo">pcmonkey</span></div></div></div><div id="comment-tools-15743" class="comment-tools"></div><div class="clear"></div><div id="comment-15743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15747"></span>

<div id="answer-container-15747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15747-score" class="post-score" title="current number of votes">0</div><span id="post-15747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In addition to what <span>@Jasper</span> said, look for broadcast packets to 10.128.255.255. If it's a Windows machine it will eventually send some broadcasts to it's network broadcast address.</p><p>Filter: ip.address eq 10.128.255.255</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 19:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-15747" class="comments-container"></div><div id="comment-tools-15747" class="comment-tools"></div><div class="clear"></div><div id="comment-15747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

