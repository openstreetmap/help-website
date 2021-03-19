+++
type = "question"
title = "retransmission after ack"
description = '''Hello Everyone! I tried to understand why there is retransmision after getting ack picture1. Could anybody explain me why there is retransmission after getting correct ack? picture2'''
date = "2015-06-22T10:48:00Z"
lastmod = "2015-06-24T09:12:00Z"
weight = 43453
keywords = [ "sack", "tcp", "retransmissions" ]
aliases = [ "/questions/43453" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [retransmission after ack](/questions/43453/retransmission-after-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43453-score" class="post-score" title="current number of votes">0</div><span id="post-43453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Everyone!</p><p>I tried to understand why there is retransmision after getting ack <a href="http://screenshot.sh/oeWnYTn7s9nDv" title="Title">picture1</a>. Could anybody explain me why there is retransmission after getting correct ack? <a href="http://screenshot.sh/m3DXPqFKBt6k7" title="Title">picture2</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sack" rel="tag" title="see questions tagged &#39;sack&#39;">sack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '15, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/2c0ab4176817b28eaa2a0f0a9eb5cd99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kabun&#39;s gravatar image" /><p><span>Kabun</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kabun has no accepted answers">0%</span></p></div></div><div id="comments-container-43453" class="comments-container"></div><div id="comment-tools-43453" class="comment-tools"></div><div class="clear"></div><div id="comment-43453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43454"></span>

<div id="answer-container-43454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43454-score" class="post-score" title="current number of votes">0</div><span id="post-43454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, the ACK number is the next expected sequence number by the receiver. So the server at 5001 has received all bytes up to 1595113 (tcp.nxtseq==1595113) and is now expecting the segment with tcp.seq==1595113. When wireshark flags it as a retransmission this indicates that it was lost in transit when it was initially sent.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-262_0X11ZW9.png" alt="alt text" /></p><hr /><p>So this is the same trace as in <a href="https://ask.wireshark.org/questions/43361/why-retransmission-occured-before-duplicated-ack">why-retransmission-occured-before-duplicated-ack</a> if you filter tcp.nxtseq==1595113 or tcp.ack==1595113 or tcp.seq==1595113 and go to Statistics -&gt; Flow Graph you see the relevant packets.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-263.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '15, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jun '15, 11:55</strong> </span></p></div></div><div id="comments-container-43454" class="comments-container"><span id="43455"></span><div id="comment-43455" class="comment"><div id="post-43455-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer</p></div><div id="comment-43455-info" class="comment-info"><span class="comment-age">(22 Jun '15, 11:40)</span> <span class="comment-user userinfo">Kabun</span></div></div><span id="43509"></span><div id="comment-43509" class="comment"><div id="post-43509-score" class="comment-score"></div><div class="comment-text"><p>If you think that the question is answered to your satisfaction would you mind marking the given answer by clicking the checkmark icon ... That will close the question out. BTW maybe you can also close the other thread if it is the same issue ...</p></div><div id="comment-43509-info" class="comment-info"><span class="comment-age">(24 Jun '15, 09:12)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-43454" class="comment-tools"></div><div class="clear"></div><div id="comment-43454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

