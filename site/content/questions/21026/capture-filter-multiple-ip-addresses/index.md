+++
type = "question"
title = "Capture Filter Multiple IP Addresses"
description = '''Hello, I need to capture all the traffic from 12 IP addresses. I am using WS1.8 and running on Windows 2003. These are all on an internal network with 4 separate sub-nets (10.128.12.xx, 10.128.80.xx, 10.128.56.xx, 10.128.20.xx). On the first sub-net, I need to specify 2 IPs directly, on the remainin...'''
date = "2013-05-08T06:34:00Z"
lastmod = "2013-05-08T07:06:00Z"
weight = 21026
keywords = [ "subnet", "capture", "ip" ]
aliases = [ "/questions/21026" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter Multiple IP Addresses](/questions/21026/capture-filter-multiple-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21026-score" class="post-score" title="current number of votes">0</div><span id="post-21026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I need to capture all the traffic from 12 IP addresses. I am using WS1.8 and running on Windows 2003. These are all on an internal network with 4 separate sub-nets (10.128.12.xx, 10.128.80.xx, 10.128.56.xx, 10.128.20.xx). On the first sub-net, I need to specify 2 IPs directly, on the remaining sub-nets I could grab all the traffic from the sub-net.<br />
</p><p>I have tried to enter them as by stringing together "host 10.128.xx.xx and host 10.128.xx.xx ...." but there seems to be too many.</p><p>I have tried net 10.128.xx.xx/x but the dialog remains red.</p><p>Thank you in advance for any help!</p><p>Ron</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-subnet" rel="tag" title="see questions tagged &#39;subnet&#39;">subnet</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '13, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/a0b3ed8eb2a14c732a55294e2363ecfd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mechron&#39;s gravatar image" /><p><span>Mechron</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mechron has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-21026" class="comments-container"></div><div id="comment-tools-21026" class="comment-tools"></div><div class="clear"></div><div id="comment-21026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21027"></span>

<div id="answer-container-21027" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21027-score" class="post-score" title="current number of votes">4</div><span id="post-21027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have tried to enter them as by stringing together "host 10.128.xx.xx <strong>and</strong> host 10.128.xx.xx ...." but there seems to be too many.</p></blockquote><p>you can't use <strong>and</strong> as that will only capture packets where <strong>all</strong> conditions are fulfilled, which will never be the case (think about the src ip and dst ip of a packet!).</p><p>Please use <strong>or</strong> instead.</p><p>If you want to capture a whole network, your must use <strong>net</strong> instead of <strong>host</strong></p><blockquote><p>net 10.128.0.0/24 or net 10.129.0.0/24 or host 10.1.2.3 or host 10.2.3.4</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '13, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 May '13, 14:06</strong> </span></p></div></div><div id="comments-container-21027" class="comments-container"></div><div id="comment-tools-21027" class="comment-tools"></div><div class="clear"></div><div id="comment-21027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

