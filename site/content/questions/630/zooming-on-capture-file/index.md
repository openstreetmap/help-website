+++
type = "question"
title = "Zooming on capture file"
description = '''Hi all Lets say I have a large capture file from my network and I would like to zoom on a specific period of time on the capture. How can I do it with wireshark, it seams that the IO Graphs is very basic. If it is not possible, can someone advice for a tool which can do it? Thanks'''
date = "2010-10-25T13:50:00Z"
lastmod = "2010-10-27T01:06:00Z"
weight = 630
keywords = [ "zooming" ]
aliases = [ "/questions/630" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Zooming on capture file](/questions/630/zooming-on-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-630-score" class="post-score" title="current number of votes">0</div><span id="post-630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all Lets say I have a large capture file from my network and I would like to zoom on a specific period of time on the capture. How can I do it with wireshark, it seams that the IO Graphs is very basic. If it is not possible, can someone advice for a tool which can do it? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zooming" rel="tag" title="see questions tagged &#39;zooming&#39;">zooming</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '10, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/6b587f5fd952e8151edcad9d1256ce8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ron&#39;s gravatar image" /><p><span>ron</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ron has no accepted answers">0%</span></p></div></div><div id="comments-container-630" class="comments-container"></div><div id="comment-tools-630" class="comment-tools"></div><div class="clear"></div><div id="comment-630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="631"></span>

<div id="answer-container-631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-631-score" class="post-score" title="current number of votes">0</div><span id="post-631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Pilot does this beautifully - you just click and drag over a section of the graphs and then select to open the packets in Wireshark. See www.cacetech.com for more information.</p><p>In Wireshark you can create a display filter that will show packets between certain times - for example, <code>frame.time_relative &gt; 0 &amp;&amp; frame.time_relative &lt; 4</code>. This displays all packets that arrived in the first four seconds of the trace file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '10, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-631" class="comments-container"></div><div id="comment-tools-631" class="comment-tools"></div><div class="clear"></div><div id="comment-631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="651"></span>

<div id="answer-container-651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-651-score" class="post-score" title="current number of votes">0</div><span id="post-651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Right, Pilot does it well , I came across a tool today found on softpedia Which also does it , it is kind of new but it looks good. Maybe it will help you.</p><p><a href="http://www.softpedia.com/get/Network-Tools/Network-Testing/CapsGraph.shtml">http://www.softpedia.com/get/Network-Tools/Network-Testing/CapsGraph.shtml</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/b54551b7dbfcd6f277b6623256bf2bb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mitusjosh&#39;s gravatar image" /><p><span>mitusjosh</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mitusjosh has no accepted answers">0%</span></p></div></div><div id="comments-container-651" class="comments-container"><span id="666"></span><div id="comment-666" class="comment"><div id="post-666-score" class="comment-score"></div><div class="comment-text"><p>Installed CapsGraph, but it crashes immediately upon load. Lost patience and dumped it... have you run it successfully?</p></div><div id="comment-666-info" class="comment-info"><span class="comment-age">(26 Oct '10, 09:25)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div><span id="683"></span><div id="comment-683" class="comment"><div id="post-683-score" class="comment-score"></div><div class="comment-text"><p>Yes it worked, but you need to install Microsoft .NET Framework 3.5 and then install Microsoft Chart Controls, the links are at the site, it works fine looks cool just what I was looking for. Maybe you need to restart your pc after installing the Microsoft .NET Framework 3.5 and Microsoft Chart Controls</p></div><div id="comment-683-info" class="comment-info"><span class="comment-age">(26 Oct '10, 12:55)</span> <span class="comment-user userinfo">ron</span></div></div><span id="684"></span><div id="comment-684" class="comment"><div id="post-684-score" class="comment-score"></div><div class="comment-text"><p>Installed both, but it just died... will restart a few more times for good measure &lt;g&gt;. Thanks!</p></div><div id="comment-684-info" class="comment-info"><span class="comment-age">(26 Oct '10, 13:07)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-651" class="comment-tools"></div><div class="clear"></div><div id="comment-651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="700"></span>

<div id="answer-container-700" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-700-score" class="post-score" title="current number of votes">0</div><span id="post-700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>it works when you install Microsoft .NET Framework 3.5 SP1</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/b54551b7dbfcd6f277b6623256bf2bb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mitusjosh&#39;s gravatar image" /><p><span>mitusjosh</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mitusjosh has no accepted answers">0%</span></p></div></div><div id="comments-container-700" class="comments-container"></div><div id="comment-tools-700" class="comment-tools"></div><div class="clear"></div><div id="comment-700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

