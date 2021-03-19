+++
type = "question"
title = "ACK number error"
description = '''Hi, everyone: As I know, in TCP, the ACK number of N+1th packet is: Seq number of Nth packet+Length of Nth packet.  But I have found that in some scenario the ACK number of N+1th packet is: Seq number of Nth packet + Length of Nth packet +1, like this:   Seq of frame 2481 is 1243466, and the next pa...'''
date = "2014-06-29T02:20:00Z"
lastmod = "2014-06-29T18:37:00Z"
weight = 34266
keywords = [ "ack", "tcp" ]
aliases = [ "/questions/34266" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ACK number error](/questions/34266/ack-number-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34266-score" class="post-score" title="current number of votes">0</div><span id="post-34266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, everyone:</p><p>As I know, in TCP, the ACK number of N+1th packet is:</p><pre><code>Seq number of Nth packet+Length of Nth packet.</code></pre><p>But I have found that in some scenario the ACK number of N+1th packet is:</p><pre><code>Seq number of Nth packet + Length of Nth packet +1, like this:</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/lzq_1.jpg" alt="alt text" /></p><pre><code>Seq of frame 2481 is 1243466, and the next packet ACK should be Seq+len=1243466+1179=1244645.</code></pre><p>But in fact the ACK of next packet is 1244646. Why this happends?</p><p>Here is my trace file, this happens at the end of this trace file. <a href="https://www.dropbox.com/s/gn8nyrv1cr147eq/bug.pcap">https://www.dropbox.com/s/gn8nyrv1cr147eq/bug.pcap</a></p><p>Anyone could help me? Thank you very much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '14, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/44959625f5849a8c85cdf05ca9802478?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lzq8272587&#39;s gravatar image" /><p><span>lzq8272587</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lzq8272587 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '14, 02:25</strong> </span></p></div></div><div id="comments-container-34266" class="comments-container"></div><div id="comment-tools-34266" class="comment-tools"></div><div class="clear"></div><div id="comment-34266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34272"></span>

<div id="answer-container-34272" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34272-score" class="post-score" title="current number of votes">1</div><span id="post-34272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lzq8272587 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The fin and the syn bit need to get acknowledged without any data bytes flowing so they increment the ack number by one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '14, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-34272" class="comments-container"><span id="34276"></span><div id="comment-34276" class="comment"><div id="post-34276-score" class="comment-score"></div><div class="comment-text"><p>Hi, mrEEde2:</p><p>Thank you very much.</p><p>But in another trace, I have found a fin bit without increasing ack number by one.</p><p>Here is the trace: <a href="https://www.dropbox.com/s/e712npql6xsj31z/good.pcap">https://www.dropbox.com/s/e712npql6xsj31z/good.pcap</a></p><p>Note that the ack number of FIN packet is equal to the prior one.</p><p>I cannot post figure in comment. Please find it in answer.</p><p>Thank you very much again!</p></div><div id="comment-34276-info" class="comment-info"><span class="comment-age">(29 Jun '14, 17:47)</span> <span class="comment-user userinfo">lzq8272587</span></div></div><span id="34277"></span><div id="comment-34277" class="comment"><div id="post-34277-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/1_7.jpg" alt="alt text" /></p></div><div id="comment-34277-info" class="comment-info"><span class="comment-age">(29 Jun '14, 17:48)</span> <span class="comment-user userinfo">lzq8272587</span></div></div><span id="34279"></span><div id="comment-34279" class="comment"><div id="post-34279-score" class="comment-score"></div><div class="comment-text"><p>Oh! I see that! You are right, Jim. Thank you very much!</p></div><div id="comment-34279-info" class="comment-info"><span class="comment-age">(29 Jun '14, 18:37)</span> <span class="comment-user userinfo">lzq8272587</span></div></div></div><div id="comment-tools-34272" class="comment-tools"></div><div class="clear"></div><div id="comment-34272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

