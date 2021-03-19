+++
type = "question"
title = "Is there a way to show all packet captures for one site capture"
description = '''I would like to know if it possible to zero it on a packet capture by finding the the first syn ack and then find all sites associated with this.'''
date = "2010-10-16T12:35:00Z"
lastmod = "2010-10-19T07:38:00Z"
weight = 520
keywords = [ "capture", "packet", "associate" ]
aliases = [ "/questions/520" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to show all packet captures for one site capture](/questions/520/is-there-a-way-to-show-all-packet-captures-for-one-site-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-520-score" class="post-score" title="current number of votes">0</div><span id="post-520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know if it possible to zero it on a packet capture by finding the the first syn ack and then find all sites associated with this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-associate" rel="tag" title="see questions tagged &#39;associate&#39;">associate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '10, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/5aafe332b72bad2f1c98be9ffc46de2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eparl&#39;s gravatar image" /><p><span>eparl</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eparl has no accepted answers">0%</span></p></div></div><div id="comments-container-520" class="comments-container"><span id="533"></span><div id="comment-533" class="comment"><div id="post-533-score" class="comment-score"></div><div class="comment-text"><p>Can you give a little more explanation? I'm assuming you have a large packet capture and you're looking to find a session initialization (the SYN ACK). Once you find the pertinent session(s) you want to find all "sites"? This is the confusing part.</p></div><div id="comment-533-info" class="comment-info"><span class="comment-age">(19 Oct '10, 07:38)</span> <span class="comment-user userinfo">GeonJay</span></div></div></div><div id="comment-tools-520" class="comment-tools"></div><div class="clear"></div><div id="comment-520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="531"></span>

<div id="answer-container-531" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-531-score" class="post-score" title="current number of votes">0</div><span id="post-531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When I want to find the first TCP SYN in a packet capture, I'll open the Find dialog ("CTRL+F" or Edit | Find Packet) and apply the following display filter:</p><pre><code>tcp.flags eq 0x02</code></pre><p>This will bring you to the first TCP SYN packet in the packet capture. If you want a list of all the sites associated with this host (I'm not sure if you mean source or destination host), I right-click on the IP address in question and select Apply as Filter | Selected.</p><p>-Josh</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '10, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/8f0c7ef69be39a820dca2c32ca3df1c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joswr1ght&#39;s gravatar image" /><p><span>joswr1ght</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joswr1ght has no accepted answers">0%</span></p></div></div><div id="comments-container-531" class="comments-container"></div><div id="comment-tools-531" class="comment-tools"></div><div class="clear"></div><div id="comment-531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

