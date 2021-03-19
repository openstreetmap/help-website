+++
type = "question"
title = "Meaning of the TCP dump entry"
description = '''Hello all, I am monitoring a remote system. The TCP dump shows the following entry. Does anybody has any idea what this entry means??  29 2.199163 10.142.4.10 62.254.196.34 TCP 54 41620 &amp;gt; 18081 [RST] Seq=4360 Win=49680 Len=0 30 20216171 62.254.196.34 10.142.4.10 TCP 60 18081 &amp;gt; 41620 [RST] Seq=...'''
date = "2012-11-05T02:55:00Z"
lastmod = "2012-11-06T03:45:00Z"
weight = 15539
keywords = [ "wireshark" ]
aliases = [ "/questions/15539" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Meaning of the TCP dump entry](/questions/15539/meaning-of-the-tcp-dump-entry)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15539-score" class="post-score" title="current number of votes">0</div><span id="post-15539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am monitoring a remote system. The TCP dump shows the following entry. Does anybody has any idea what this entry means??</p><p><code> 29 2.199163 10.142.4.10 62.254.196.34 TCP 54 41620 &gt; 18081 [RST] Seq=4360 Win=49680 Len=0 30 20216171 62.254.196.34 10.142.4.10 TCP 60 18081 &gt; 41620 [RST] Seq=6849 Win=0 Len=0</code></p><p>Its too urgent please revert to this</p><p>Thanks, Raj</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '12, 02:55</strong></p><img src="https://secure.gravatar.com/avatar/9bf03bf5759f0476cbc97234f8f1add6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rajm&#39;s gravatar image" /><p><span>rajm</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rajm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Nov '12, 04:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-15539" class="comments-container"></div><div id="comment-tools-15539" class="comment-tools"></div><div class="clear"></div><div id="comment-15539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15541"></span>

<div id="answer-container-15541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15541-score" class="post-score" title="current number of votes">1</div><span id="post-15541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It tells you, that the client (10.142.4.10) decided to terminate the tcp connection to 62.254.196.34:18081 and thus it sent a TCP RESET (RST). The server decided to answer with a RESET.</p><p>Please read the following wikipedia article to learn more about TCP connection termination:</p><blockquote><p><code>http://en.wikipedia.org/wiki/Transmission_Control_Protocol</code><br />
</p></blockquote><p>Regarding the next question you might have: Based on just that information, it is impossible to figure out why the connection has been terminated in that way. It depends on the application and possible errors that might have occurred (or not, if the application just works like that).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '12, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Nov '12, 04:27</strong> </span></p></div></div><div id="comments-container-15541" class="comments-container"><span id="15575"></span><div id="comment-15575" class="comment"><div id="post-15575-score" class="comment-score"></div><div class="comment-text"><p>Great Thanks Kurt.</p></div><div id="comment-15575-info" class="comment-info"><span class="comment-age">(06 Nov '12, 03:29)</span> <span class="comment-user userinfo">rajm</span></div></div><span id="15576"></span><div id="comment-15576" class="comment"><div id="post-15576-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-15576-info" class="comment-info"><span class="comment-age">(06 Nov '12, 03:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15541" class="comment-tools"></div><div class="clear"></div><div id="comment-15541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

