+++
type = "question"
title = "Retransmission even after receiving ack."
description = '''Dear All, We are observing disconnections from source to destination,while capturing i found that client is retransmitting a packet even after it has received ack from server.'''
date = "2014-02-11T01:47:00Z"
lastmod = "2014-02-11T01:55:00Z"
weight = 29672
keywords = [ "retransmissions", "tcp" ]
aliases = [ "/questions/29672" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Retransmission even after receiving ack.](/questions/29672/retransmission-even-after-receiving-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29672-score" class="post-score" title="current number of votes">0</div><span id="post-29672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All, We are observing disconnections from source to destination,while capturing i found that client is retransmitting a packet even after it has received ack from server.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '14, 02:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29672" class="comments-container"></div><div id="comment-tools-29672" class="comment-tools"></div><div class="clear"></div><div id="comment-29672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29674"></span>

<div id="answer-container-29674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29674-score" class="post-score" title="current number of votes">0</div><span id="post-29674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you verify the ACK numbers and whether SACK options are used? Did you capture on the client side or the server side? If capturing on the server side, the ACK might have been lost or still underways? Please post a capture file to www.cloudshark.org (or somewhere else) if you need any help in interpreting the behavior.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-29674" class="comments-container"><span id="29676"></span><div id="comment-29676" class="comment"><div id="post-29676-score" class="comment-score"></div><div class="comment-text"><p>Thanks syn with for your reply,yes the capture was taken on server end and agree that ack might have been lost.</p></div><div id="comment-29676-info" class="comment-info"><span class="comment-age">(11 Feb '14, 01:55)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-29674" class="comment-tools"></div><div class="clear"></div><div id="comment-29674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

