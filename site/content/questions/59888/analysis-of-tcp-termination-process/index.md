+++
type = "question"
title = "Analysis of TCP Termination process"
description = '''From the WS capture link below, can anyone tell me why I am getting server retransmission packets from this simple connect/disconnect TCP sequence from my email server? Am I missing an ACK somewhere? I&#x27;ve tried several different extra ACKs, but nothing has worked. Extra ACKs seems to produce &#x27;Duplic...'''
date = "2017-03-07T06:32:00Z"
lastmod = "2017-03-07T06:48:00Z"
weight = 59888
keywords = [ "disconnect", "connect", "tcp" ]
aliases = [ "/questions/59888" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Analysis of TCP Termination process](/questions/59888/analysis-of-tcp-termination-process)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59888-score" class="post-score" title="current number of votes">0</div><span id="post-59888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From the WS capture link below, can anyone tell me why I am getting server retransmission packets from this simple connect/disconnect TCP sequence from my email server? Am I missing an ACK somewhere? I've tried several different extra ACKs, but nothing has worked. Extra ACKs seems to produce 'Duplicate ACK' packets. This is from my own TCP/IP stack.</p><p>Thanks.</p><p>Sutton</p><p><a href="https://www.cloudshark.org/captures/1e8542d7b55c">https://www.cloudshark.org/captures/1e8542d7b55c</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disconnect" rel="tag" title="see questions tagged &#39;disconnect&#39;">disconnect</span> <span class="post-tag tag-link-connect" rel="tag" title="see questions tagged &#39;connect&#39;">connect</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '17, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/9f303f38b9221d23f72e6d2e5a651184?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dodge55&#39;s gravatar image" /><p><span>dodge55</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dodge55 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Mar '17, 06:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-59888" class="comments-container"></div><div id="comment-tools-59888" class="comment-tools"></div><div class="clear"></div><div id="comment-59888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59889"></span>

<div id="answer-container-59889" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59889-score" class="post-score" title="current number of votes">1</div><span id="post-59889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I figured it out. I wasn't adding 1 to the sequence number for the server's FIN packet. So, the seq. number was wrong.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '17, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/9f303f38b9221d23f72e6d2e5a651184?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dodge55&#39;s gravatar image" /><p><span>dodge55</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dodge55 has no accepted answers">0%</span></p></div></div><div id="comments-container-59889" class="comments-container"></div><div id="comment-tools-59889" class="comment-tools"></div><div class="clear"></div><div id="comment-59889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

