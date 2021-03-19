+++
type = "question"
title = "Microsoft Visual C++ Runtime Library - Runtime Error"
description = '''Team, I am running Wireshark 1.8.9 software on a Windows 2003 server, running Spirent client and monitoring the connectivity from the server to the Spirent Chassis. I see &quot;Runtime Error! Program This application has requested the Runtime to terminate it in an unusual way.&quot; Any thoughts, what could h...'''
date = "2013-08-13T20:21:00Z"
lastmod = "2013-08-19T08:47:00Z"
weight = 23758
keywords = [ "runtimeerrorprogram" ]
aliases = [ "/questions/23758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Microsoft Visual C++ Runtime Library - Runtime Error](/questions/23758/microsoft-visual-c-runtime-library-runtime-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23758-score" class="post-score" title="current number of votes">0</div><span id="post-23758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Team, I am running Wireshark 1.8.9 software on a Windows 2003 server, running Spirent client and monitoring the connectivity from the server to the Spirent Chassis.</p><p>I see "Runtime Error! Program This application has requested the Runtime to terminate it in an unusual way."</p><p>Any thoughts, what could have gone wrong ?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-runtimeerrorprogram" rel="tag" title="see questions tagged &#39;runtimeerrorprogram&#39;">runtimeerrorprogram</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '13, 20:21</strong></p><img src="https://secure.gravatar.com/avatar/7a1362f8ca2c05b8e3f20300b1ede910?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leonfrs&#39;s gravatar image" /><p><span>leonfrs</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leonfrs has no accepted answers">0%</span></p></div></div><div id="comments-container-23758" class="comments-container"></div><div id="comment-tools-23758" class="comment-tools"></div><div class="clear"></div><div id="comment-23758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23849"></span>

<div id="answer-container-23849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23849-score" class="post-score" title="current number of votes">0</div><span id="post-23849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I see "Runtime Error! Program This application has requested the Runtime to terminate it in an unusual way."</p></blockquote><p>This is most certainly a problem with the available RAM.</p><blockquote><p><a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a></p></blockquote><p>This is what you can do:</p><pre><code>- Get more physical RAM and a 64 Bit OS.
- reduce the amount of captured traffic by using capture filters
- use [dumpcap][1] with ring buffers to capture the traffic ([long term capture][2])</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '13, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23849" class="comments-container"></div><div id="comment-tools-23849" class="comment-tools"></div><div class="clear"></div><div id="comment-23849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

