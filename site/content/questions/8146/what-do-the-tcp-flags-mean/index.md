+++
type = "question"
title = "What do the TCP flags mean?"
description = ''' Source Destination Protocol Info 85.73.133.27 150.140.141.181 TCP hi3182&amp;gt;http [SYN] Seq=0 Len=0 MSS=1420,win=,..etc   What is the meaning of the values of TCP flags in the Info column?'''
date = "2011-12-27T23:17:00Z"
lastmod = "2011-12-28T17:20:00Z"
weight = 8146
keywords = [ "info", "tcp" ]
aliases = [ "/questions/8146" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What do the TCP flags mean?](/questions/8146/what-do-the-tcp-flags-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8146-score" class="post-score" title="current number of votes">0</div><span id="post-8146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>  Source                   Destination    Protocol         Info
85.73.133.27           150.140.141.181     TCP        hi3182&gt;http [SYN] Seq=0 Len=0 MSS=1420,win=,..etc</code></pre><p>What is the meaning of the values of TCP flags in the Info column?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '11, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/a367f6528e094b0a6af8d025bfcc6e4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="george&#39;s gravatar image" /><p><span>george</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="george has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Dec '11, 06:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8146" class="comments-container"></div><div id="comment-tools-8146" class="comment-tools"></div><div class="clear"></div><div id="comment-8146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8148"></span>

<div id="answer-container-8148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8148-score" class="post-score" title="current number of votes">2</div><span id="post-8148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP flags shows what the sending TCP entity wants the receiving TCP entity to do. In this case SYNchronize with the sender, using the other data listed. Check the <a href="http://www.tcpipguide.com/free/t_TCPMessageSegmentFormat-3.htm">TCP/IP Guide</a> for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '11, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8148" class="comments-container"><span id="8157"></span><div id="comment-8157" class="comment"><div id="post-8157-score" class="comment-score"></div><div class="comment-text"><p>And be sure to have a look at the various TCP-related RFC's, such as the original TCP RFC, <a href="http://tools.ietf.org/html/rfc793#section-3.1">RFC 793</a>, as well as <a href="http://tools.ietf.org/html/rfc3168#section-6.1">RFC 3168</a>, which introduced the ECE and CWR flags, and <a href="http://tools.ietf.org/html/rfc3540">RFC 3540</a>, which introduced the NS flag. These 3 latter flags are not [yet] mentioned in the TCP/IP Guide.</p></div><div id="comment-8157-info" class="comment-info"><span class="comment-age">(28 Dec '11, 17:20)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-8148" class="comment-tools"></div><div class="clear"></div><div id="comment-8148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

