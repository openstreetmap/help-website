+++
type = "question"
title = "Application going slow same time at night"
description = '''Working ona project where application users complains about the issue every night almost same time everyday. The issue reported only at night. To my wonder same application works fine and no complaint during night. We disablled all nightly batch to drill down if this might be causing due to nightly ...'''
date = "2013-08-05T01:46:00Z"
lastmod = "2013-08-08T07:35:00Z"
weight = 23547
keywords = [ "ack", "keep-alaive", "keep-alive", "tcp" ]
aliases = [ "/questions/23547" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Application going slow same time at night](/questions/23547/application-going-slow-same-time-at-night)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23547-score" class="post-score" title="current number of votes">0</div><span id="post-23547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Working ona project where application users complains about the issue every night almost same time everyday. The issue reported only at night. To my wonder same application works fine and no complaint during night. We disablled all nightly batch to drill down if this might be causing due to nightly batch. However, this is nt the case.</p><p>Colllected some network related elements which I need your help on. Can some one help me with this.</p><p>I could see lot os [TCP Keep Alive] and [TCP Keep-Alive ACK] on the wireshark pane. How can I come drill down to an issue? I just have screenshots for those and I do ot find option to attach ythose screenshots here.</p><p>Some previous similar experiences may be helpful. We are on Solaris.</p><p>R, Kiddle.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-keep-alaive" rel="tag" title="see questions tagged &#39;keep-alaive&#39;">keep-alaive</span> <span class="post-tag tag-link-keep-alive" rel="tag" title="see questions tagged &#39;keep-alive&#39;">keep-alive</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '13, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/19da02559a9fac5cc6f4d0ea40ff87e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kiddle&#39;s gravatar image" /><p><span>kiddle</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kiddle has no accepted answers">0%</span></p></div></div><div id="comments-container-23547" class="comments-container"></div><div id="comment-tools-23547" class="comment-tools"></div><div class="clear"></div><div id="comment-23547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23553"></span>

<div id="answer-container-23553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23553-score" class="post-score" title="current number of votes">0</div><span id="post-23553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Keepalive probes are not causing any performance problem, they just indicate that a long living connection is idle. So a good start is probably to remove those using</p><pre><code>!tcp.analysis.keep_alive and !tcp.analysis.keep_alive_ack</code></pre><p>and 'Export specified packets'. Then you might want to remove (most of) the data portion by running</p><pre><code>editcap -2 100 infile outfile</code></pre><p>and share it on <a href="http://www.cloudshark.org">www.cloudshark.org</a> for others to give it a try...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '13, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '13, 05:08</strong> </span></p></div></div><div id="comments-container-23553" class="comments-container"></div><div id="comment-tools-23553" class="comment-tools"></div><div class="clear"></div><div id="comment-23553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23649"></span>

<div id="answer-container-23649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23649-score" class="post-score" title="current number of votes">0</div><span id="post-23649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>where application users complains about the issue every night almost same time everyday. The issue reported only at night.</p></blockquote><p>Please check if there are another applications that utilize (overload) the network during the night. I mean not only batch jobs on your system, but also large backup or data sync jobs (as you said: every night at the same time !!), that run over the network and put high load on switches, routers, firewalls, etc.. That often causes the kind of problems you describe.</p><p>However, without any further information (about the nature of the application, the involved systems, the involved network infrastructure, a capture file, etc.), it is hard to give any good advice.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23649" class="comments-container"></div><div id="comment-tools-23649" class="comment-tools"></div><div class="clear"></div><div id="comment-23649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

