+++
type = "question"
title = "Trying to create a graph that show the time of day when activity against servers were the highest."
description = '''Hi, Im trying to get a graph that show whitch time of the day my computer had the most activity with external servers? I found the external servers on IP destination. But how can i create a graph? Thanks'''
date = "2015-12-15T06:45:00Z"
lastmod = "2015-12-15T09:57:00Z"
weight = 48532
keywords = [ "ask.wireshark.org", "wireshark" ]
aliases = [ "/questions/48532" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to create a graph that show the time of day when activity against servers were the highest.](/questions/48532/trying-to-create-a-graph-that-show-the-time-of-day-when-activity-against-servers-were-the-highest)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48532-score" class="post-score" title="current number of votes">0</div><span id="post-48532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Im trying to get a graph that show whitch time of the day my computer had the most activity with external servers?</p><p>I found the external servers on IP destination. But how can i create a graph?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ask.wireshark.org" rel="tag" title="see questions tagged &#39;ask.wireshark.org&#39;">ask.wireshark.org</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/464c35db7abc9a7a3ec7b163eac84d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marko&#39;s gravatar image" /><p><span>Marko</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marko has no accepted answers">0%</span></p></div></div><div id="comments-container-48532" class="comments-container"></div><div id="comment-tools-48532" class="comment-tools"></div><div class="clear"></div><div id="comment-48532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48535"></span>

<div id="answer-container-48535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48535-score" class="post-score" title="current number of votes">0</div><span id="post-48535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Start from <code>Statistics -&gt; I/O graph</code>.</p><p>In the graph window which pops up, you may specify display filters to limit each curve to packets meeting some criteria, e.g. to draw one curve for incoming traffic and another one in the same graph for outgoing traffic. The default is a single curve showing all packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '15, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48535" class="comments-container"><span id="48539"></span><div id="comment-48539" class="comment"><div id="post-48539-score" class="comment-score"></div><div class="comment-text"><p>Below the graph (I talk about Wireshark 2.x with Qt ("new") GUI), there is a table where you define the curves. [+] and [-] symbols are used to add and remove rows to/from that table. By double-clicking the "display filter" column of a given row, you can define which packets you want to contribute to that curve using the syntax of display filters.</p><p>So as an example, <code>ip.dst == 10.0.0.0/8</code> will cause the curve to show packets sent to any IP in the private A-type subnet.</p><p>In Y-Axis column you can define what value you want to show: number of packets, number of bytes, etc. or an operation over packet field specified in "Y field" column where you can specify a protocol field in the packet (quick &amp; mostly useless example: <code>ip.len</code>).</p><p>When you finish, double-click the line outside any edit field, and then tick the tickbox in the leftmost column ("name").</p></div><div id="comment-48539-info" class="comment-info"><span class="comment-age">(15 Dec '15, 09:57)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48535" class="comment-tools"></div><div class="clear"></div><div id="comment-48535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

