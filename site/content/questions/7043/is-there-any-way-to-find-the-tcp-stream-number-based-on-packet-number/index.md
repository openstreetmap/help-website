+++
type = "question"
title = "Is there any way to find the tcp stream number based on packet number?"
description = '''Hi, I am wondering if i can follow the tcp stream when i have the packet number in tshark? For example, I　only know packet 10 is a HTTP packet, and I want to follow the tcp stream of packet 10. Is there any way to do that?'''
date = "2011-10-22T19:33:00Z"
lastmod = "2017-04-12T21:01:00Z"
weight = 7043
keywords = [ "packet", "tcp", "tshark", "stream" ]
aliases = [ "/questions/7043" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there any way to find the tcp stream number based on packet number?](/questions/7043/is-there-any-way-to-find-the-tcp-stream-number-based-on-packet-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7043-score" class="post-score" title="current number of votes">0</div><span id="post-7043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am wondering if i can follow the tcp stream when i have the packet number in tshark? For example, I　only know packet 10 is a HTTP packet, and I want to follow the tcp stream of packet 10. Is there any way to do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '11, 19:33</strong></p><img src="https://secure.gravatar.com/avatar/61c771620f5b1da1a7fa027cb558f0b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timho1985&#39;s gravatar image" /><p><span>timho1985</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timho1985 has no accepted answers">0%</span></p></div></div><div id="comments-container-7043" class="comments-container"></div><div id="comment-tools-7043" class="comment-tools"></div><div class="clear"></div><div id="comment-7043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7044"></span>

<div id="answer-container-7044" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7044-score" class="post-score" title="current number of votes">2</div><span id="post-7044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SYN-bit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When Wireshark processes the capture, it simply assigns the tcp stream index to each new TCP session it sees. If you look at the packet details of any TCP packet, any look at the TCP section, you will see "Stream index: nn" line, where nn is the stream. To then filter on that stream, then just apply the display filter "tcp.stream eq nn" (nn being the stream from the packet you are interested. Of course this is just the hard way to do it, right-clicking on any TCP packet, and selecting Follow TCP stream, followed Filter out this stream does the same thing.</p><p>You could possibly write a LUA script that would take a give packet number, then determine the TCP stream wireshark has for that, and then filter out the stream. This hasn't been published by anyone to my knowledge.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '11, 21:42</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-7044" class="comments-container"><span id="7190"></span><div id="comment-7190" class="comment"><div id="post-7190-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer. I have tried and it works perfectly.</p></div><div id="comment-7190-info" class="comment-info"><span class="comment-age">(01 Nov '11, 23:27)</span> <span class="comment-user userinfo">timho1985</span></div></div></div><div id="comment-tools-7044" class="comment-tools"></div><div class="clear"></div><div id="comment-7044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60796"></span>

<div id="answer-container-60796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60796-score" class="post-score" title="current number of votes">0</div><span id="post-60796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can display Stream Index column (which is TCP Stream number) In Packet Details &gt; Transmission Control Protocol, find 'Stream Index' field, right click and select Apply as a Column</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 21:01</strong></p><img src="https://secure.gravatar.com/avatar/3c9ea34649c8d322e9cfd6dca1280643?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evgenia&#39;s gravatar image" /><p><span>evgenia</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evgenia has no accepted answers">0%</span></p></div></div><div id="comments-container-60796" class="comments-container"></div><div id="comment-tools-60796" class="comment-tools"></div><div class="clear"></div><div id="comment-60796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

