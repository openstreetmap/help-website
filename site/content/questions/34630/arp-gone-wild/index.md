+++
type = "question"
title = "arp gone wild"
description = '''The server goes crazy from time to time with arp who has? tell? packets beyond the range of our network. We use x.x.4-10.x, but the server begins making massive requests at x.x.11.x and running up the range. I have stopped the computer browser service on the server. Any ideas on what is causing this...'''
date = "2014-07-14T08:40:00Z"
lastmod = "2014-07-15T15:06:00Z"
weight = 34630
keywords = [ "arp" ]
aliases = [ "/questions/34630" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [arp gone wild](/questions/34630/arp-gone-wild)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34630-score" class="post-score" title="current number of votes">0</div><span id="post-34630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The server goes crazy from time to time with arp who has? tell? packets beyond the range of our network. We use x.x.4-10.x, but the server begins making massive requests at x.x.11.x and running up the range. I have stopped the computer browser service on the server. Any ideas on what is causing this and how to stop it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '14, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/6ee6494e3b424d28cde018bb25e8ee24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stringer&#39;s gravatar image" /><p><span>Stringer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stringer has no accepted answers">0%</span></p></div></div><div id="comments-container-34630" class="comments-container"><span id="34643"></span><div id="comment-34643" class="comment"><div id="post-34643-score" class="comment-score"></div><div class="comment-text"><p>can you please post the following information</p><ul><li>OS and OS release</li><li>ip configuration of that server (ipconfig /all)</li><li>a sample capture file with those ARP requests on google drive, dropbox or cloudshark.org</li></ul></div><div id="comment-34643-info" class="comment-info"><span class="comment-age">(15 Jul '14, 00:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-34630" class="comment-tools"></div><div class="clear"></div><div id="comment-34630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34640"></span>

<div id="answer-container-34640" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34640-score" class="post-score" title="current number of votes">1</div><span id="post-34640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One possible explanation is a misconfigured subnet mask. If the server believes that x.x.11.x is part of its own local subnet, and it wants to reach those IPs, it won't address it to the MAC of its gateway and will instead try to resolve the local MACs with ARP requests.</p><p>Can you confirm the subnet mask that is configured, and the intended subnet size? If the range you gave there is meant to represent one whole subnet (x.x.4-10.x), then that would call for a minimal subnet mask length of 20, or 255.255.240.0, which would put x.x.11.x into that same subnet, which would explain the ARPs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '14, 18:35</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jul '14, 18:45</strong> </span></p></div></div><div id="comments-container-34640" class="comments-container"><span id="34667"></span><div id="comment-34667" class="comment"><div id="post-34667-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Quadratic</span>, I will change the subnet mask and see if it limits the arp requests.</p><p>Your attention to this is much appreciated.</p></div><div id="comment-34667-info" class="comment-info"><span class="comment-age">(15 Jul '14, 08:30)</span> <span class="comment-user userinfo">Stringer</span></div></div><span id="34694"></span><div id="comment-34694" class="comment"><div id="post-34694-score" class="comment-score"></div><div class="comment-text"><p>What is the <em>intended</em> subnet mask of this network, and what is it currently on the server? A /20 subnet mask isn't necessarily "wrong" depending on your network design but it would explain why you're seeing the ARPs.</p></div><div id="comment-34694-info" class="comment-info"><span class="comment-age">(15 Jul '14, 15:06)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-34640" class="comment-tools"></div><div class="clear"></div><div id="comment-34640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

