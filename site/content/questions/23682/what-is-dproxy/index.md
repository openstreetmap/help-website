+++
type = "question"
title = "What is dproxy?"
description = '''I am doing some network traces and expecting communication directly between 2 servers. Under the Info column I see conversations between the target port 8004 and dproxy. anybody out there know what dproxy is? I have placed the ip address of the target computer in the local host file to bypass dns. I...'''
date = "2013-08-09T10:41:00Z"
lastmod = "2013-08-24T12:10:00Z"
weight = 23682
keywords = [ "dproxy" ]
aliases = [ "/questions/23682" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [What is dproxy?](/questions/23682/what-is-dproxy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23682-score" class="post-score" title="current number of votes">0</div><span id="post-23682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am doing some network traces and expecting communication directly between 2 servers. Under the Info column I see conversations between the target port 8004 and dproxy. anybody out there know what dproxy is? I have placed the ip address of the target computer in the local host file to bypass dns. I am using the host file to bypass our F5 load balancer. I would appreciate any help here.</p><p>Thanks, Berney</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dproxy" rel="tag" title="see questions tagged &#39;dproxy&#39;">dproxy</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '13, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/3f56402441e3029e000dba405fe9061d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="the%20third&#39;s gravatar image" /><p><span>the third</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="the third has no accepted answers">0%</span></p></div></div><div id="comments-container-23682" class="comments-container"></div><div id="comment-tools-23682" class="comment-tools"></div><div class="clear"></div><div id="comment-23682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="23686"></span>

<div id="answer-container-23686" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23686-score" class="post-score" title="current number of votes">2</div><span id="post-23686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>anybody out there know what dproxy is?</p></blockquote><p>That's just the resolved name for the source port of the connection (dproxy == tcp/udp 1296). If you disable name resolution for that, you will see the real port (1296).</p><blockquote><p>Edit -&gt; Preferences -&gt; Name Resolution -&gt; Resolve transport names [remove the check mark]</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '13, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Aug '13, 14:41</strong> </span></p></div></div><div id="comments-container-23686" class="comments-container"></div><div id="comment-tools-23686" class="comment-tools"></div><div class="clear"></div><div id="comment-23686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24006"></span>

<div id="answer-container-24006" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24006-score" class="post-score" title="current number of votes">0</div><span id="post-24006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>dproxy is a caching DNS proxy for use on dial-up gateway machines. It is designed to behave nicely when the gateway is not connected.</p><p>Regards <a href="http://www.education4world.net/">http://www.education4world.net/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/a53fb462484f0b68b7db43d5a7cec873?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ali%20Hassan&#39;s gravatar image" /><p><span>Ali Hassan</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ali Hassan has no accepted answers">0%</span></p></div></div><div id="comments-container-24006" class="comments-container"></div><div id="comment-tools-24006" class="comment-tools"></div><div class="clear"></div><div id="comment-24006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24007"></span>

<div id="answer-container-24007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24007-score" class="post-score" title="current number of votes">0</div><span id="post-24007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A proxy or proxy server is basically another computer which serves as a hub through which internet requests are processed. Regards <a href="http://www.virtualians.pk/">http://www.virtualians.pk/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/7aebe1734e86efdbc5c65cc0974e0954?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irfan%20Khan&#39;s gravatar image" /><p><span>Irfan Khan</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irfan Khan has no accepted answers">0%</span></p></div></div><div id="comments-container-24007" class="comments-container"></div><div id="comment-tools-24007" class="comment-tools"></div><div class="clear"></div><div id="comment-24007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

