+++
type = "question"
title = "TCP initial congestion window (slow-start)"
description = '''I have noticed that the initial congestion window in my traces is 8920bytes~=6*1448. rfc3390 states the initial cwand should be max 4000 bytes(around 3*1448).  At first i thought it might be because i&#x27;m running my server on mac os x, so apple might have modified the tcp stack. Therefore I tried runn...'''
date = "2011-12-23T16:09:00Z"
lastmod = "2011-12-24T12:05:00Z"
weight = 8120
keywords = [ "cwnd", "tcp" ]
aliases = [ "/questions/8120" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [TCP initial congestion window (slow-start)](/questions/8120/tcp-initial-congestion-window-slow-start)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8120-score" class="post-score" title="current number of votes">0</div><span id="post-8120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have noticed that the initial congestion window in my traces is <a href="http://s12.postimage.org/h2zk4615n/macos_cwand.png">8920bytes~=6*1448</a>. rfc3390 states the initial cwand should be max 4000 bytes(around 3*1448).</p><p>At first i thought it might be because i'm running my server on mac os x, so apple might have modified the tcp stack. Therefore I tried running the server on a Linux box (2.6.38) however i'm getting similar results <a href="http://s17.postimage.org/4odvsgqlp/linux_cwand.png">13032bytes=9*1448</a>. Both server and client machines are running on a local network (via a router). Any ideas why the initial cwand is so large?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cwnd" rel="tag" title="see questions tagged &#39;cwnd&#39;">cwnd</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '11, 16:09</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p><span>ddayan</span><br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Dec '11, 02:59</strong> </span></p></div></div><div id="comments-container-8120" class="comments-container"></div><div id="comment-tools-8120" class="comment-tools"></div><div class="clear"></div><div id="comment-8120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8130"></span>

<div id="answer-container-8130" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8130-score" class="post-score" title="current number of votes">1</div><span id="post-8130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ddayan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You already correctly used the term "should" in your question ;)</p><p>RFCs recommend lots of stuff, especially when it comes to tcp behaviour and the more you spend time to get inside views into the real behaviour of certain stacks, the more you will find that there are LOTS of differences in implementation.</p><p>Initial cwnd "should" have an upper limit like e.g. 2-4 MSS in bytes but I would not worry if it was larger (like in your trace), especially when looking at open source OSs.</p><p>slowstart_flightsize and local_slowstart_flightsize from their description posted by you both use packets to measure initial cwnd. Be aware that at least on Microsoft stacks years ago there was a change to measure initial cwnd in bytes instead of packets in order to better deal with different MTUs and when pulling up cwnd better applying to delayed ACKs and stuff, because the ACK frequency also is highly dependent on the OS and its version etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '11, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-8130" class="comments-container"></div><div id="comment-tools-8130" class="comment-tools"></div><div class="clear"></div><div id="comment-8130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8129"></span>

<div id="answer-container-8129" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8129-score" class="post-score" title="current number of votes">0</div><span id="post-8129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have found that the reason is both the server and the client are on the same subnet: FreeBSD tcp stack has these configurations:</p><pre><code> slowstart_flightsize
        The number of packets allowed to be in-flight during
        the TCP slow-start phase on a non-local network.

 local_slowstart_flightsize
        The number of packets allowed to be in-flight during
        the TCP slow-start phase to local machines in the same
        subnet.</code></pre><p>Anyone knows how these configurations are called in Linux kernels?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '11, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p><span>ddayan</span><br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div></div><div id="comments-container-8129" class="comments-container"></div><div id="comment-tools-8129" class="comment-tools"></div><div class="clear"></div><div id="comment-8129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

