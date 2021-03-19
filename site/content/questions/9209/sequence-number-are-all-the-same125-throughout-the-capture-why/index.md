+++
type = "question"
title = "Sequence number are all the same(125) throughout the capture why?"
description = '''Hi every body  For my project (the TCP performance) I dowloaded a file and capture it on the wireshark and now when I look at the captured wireshark all the sequence number are the same throughout the file, they all are seq=125,this is when I have the Acks number all different.I am sure it shouldn&#x27;t...'''
date = "2012-02-25T16:08:00Z"
lastmod = "2012-02-25T22:51:00Z"
weight = 9209
keywords = [ "number", "tcp", "sequence" ]
aliases = [ "/questions/9209" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Sequence number are all the same(125) throughout the capture why?](/questions/9209/sequence-number-are-all-the-same125-throughout-the-capture-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9209-score" class="post-score" title="current number of votes">0</div><span id="post-9209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi every body For my project (the TCP performance) I dowloaded a file and capture it on the wireshark and now when I look at the captured wireshark all the sequence number are the same throughout the file, they all are seq=125,this is when I have the Acks number all different.I am sure it shouldn't be like this can you help me and tell me what is wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '12, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/1bd99c8e05b8b8f8ba3cd9de3a4a5559?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mahsa&#39;s gravatar image" /><p><span>mahsa</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mahsa has no accepted answers">0%</span></p></div></div><div id="comments-container-9209" class="comments-container"></div><div id="comment-tools-9209" class="comment-tools"></div><div class="clear"></div><div id="comment-9209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9213"></span>

<div id="answer-container-9213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9213-score" class="post-score" title="current number of votes">2</div><span id="post-9213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like data is flowing in one direction only, and you're only seeing packets sent by one side (the data receiver) of the conversation.</p><p>This is exactly what you will see if data is flowing from A to B, and you're only looking at packets sent by B. If B's packets do not contain any data, but are only "pure" TCP--ACKs, window updates, zero window, etc.--then B will never increase its sequence number. However, because B is receiving data from A, B will keep increasing the ACK number as it acknowledges the data packets from A.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '12, 22:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Feb '12, 22:54</strong> </span></p></div></div><div id="comments-container-9213" class="comments-container"></div><div id="comment-tools-9213" class="comment-tools"></div><div class="clear"></div><div id="comment-9213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

