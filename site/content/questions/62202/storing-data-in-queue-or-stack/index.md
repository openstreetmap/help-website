+++
type = "question"
title = "storing data in queue or stack"
description = '''I&#x27;m trying to create a dissector that filters a retransmission packet by comparing DSN. Retransmission packets have the same data sequence number as the original packet, so I want to store the DSN and compare if there is the same DSN. Where could I store the values of DSN? How do I create the storag...'''
date = "2017-06-21T01:59:00Z"
lastmod = "2017-06-22T02:04:00Z"
weight = 62202
keywords = [ "queue", "dissector", "stack", "store" ]
aliases = [ "/questions/62202" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [storing data in queue or stack](/questions/62202/storing-data-in-queue-or-stack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62202-score" class="post-score" title="current number of votes">0</div><span id="post-62202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to create a dissector that filters a retransmission packet by comparing DSN.</p><p>Retransmission packets have the same data sequence number as the original packet, so I want to store the DSN and compare if there is the same DSN.</p><p>Where could I store the values of DSN? How do I create the storage? and is it possible to store them in something like a queue or stack?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-queue" rel="tag" title="see questions tagged &#39;queue&#39;">queue</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-stack" rel="tag" title="see questions tagged &#39;stack&#39;">stack</span> <span class="post-tag tag-link-store" rel="tag" title="see questions tagged &#39;store&#39;">store</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '17, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/3a702eaa9f4d90c81f74480545063c71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ngn505&#39;s gravatar image" /><p><span>ngn505</span><br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ngn505 has no accepted answers">0%</span></p></div></div><div id="comments-container-62202" class="comments-container"></div><div id="comment-tools-62202" class="comment-tools"></div><div class="clear"></div><div id="comment-62202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62204"></span>

<div id="answer-container-62204" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62204-score" class="post-score" title="current number of votes">0</div><span id="post-62204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at request-response tracking, which is the same problem. You can find it in a README file in the sources /doc directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '17, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62204" class="comments-container"><span id="62226"></span><div id="comment-62226" class="comment"><div id="post-62226-score" class="comment-score"></div><div class="comment-text"><p>Thanks for you help. I've read the README file, but I don't think I have a basic understanding of this.</p><p>So here is the question : let's say I make the c file, following the instructions of the READ file, then do I add the c file into wireshark directory? And after I do everything like making the file and writing my dissector, How does it work? Does my dissector reads the data from the memory pool that was made by the c file?</p><p>Sorry for such fundamental questions but I really don't get it and know where to ask these..</p></div><div id="comment-62226-info" class="comment-info"><span class="comment-age">(22 Jun '17, 01:48)</span> <span class="comment-user userinfo">ngn505</span></div></div><span id="62227"></span><div id="comment-62227" class="comment"><div id="post-62227-score" class="comment-score">1</div><div class="comment-text"><p>If you want to learn how to write a dissector then the Wireshark Developers Guide would be a good starting point.</p></div><div id="comment-62227-info" class="comment-info"><span class="comment-age">(22 Jun '17, 02:04)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-62204" class="comment-tools"></div><div class="clear"></div><div id="comment-62204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

