+++
type = "question"
title = "MUX27010 decoding in Wireshark"
description = '''Hi All, I found out that Wireshark could decode MUX 27.010 protocol, which if confirmed would be of great help to me. Please note for the below that I&#x27;m working with both Linux and Windows. So any hint for one or the otehr OS is welcome. 1/ In windows, I&#x27;ve read here and there that there is no way t...'''
date = "2014-07-15T05:12:00Z"
lastmod = "2014-07-15T17:23:00Z"
weight = 34659
keywords = [ "27.010", "27010", "mux" ]
aliases = [ "/questions/34659" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MUX27010 decoding in Wireshark](/questions/34659/mux27010-decoding-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34659-score" class="post-score" title="current number of votes">0</div><span id="post-34659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I found out that Wireshark could decode MUX 27.010 protocol, which if confirmed would be of great help to me. Please note for the below that I'm working with both Linux and Windows. So any hint for one or the otehr OS is welcome.</p><p>1/ In windows, I've read here and there that there is no way to capture directly traffic over RS232 interface through Wireshark. I came to the conclusion that I should capture the MUX traffic in raw mode, and this not obviously not an issue for both windows and OS. Is my understanding right ?</p><p>2/ Assuming that I well understood in 1/, once I have the MUX traffic captured in a file, I suppose I need to process it to make it readable by Wireshark. The point is that all the tools I found are related to network interfaces and IP traffic which MUX 27010 is not.</p><p>3/ Additionally, Once I'm able to decode MUX traffic, I would like also to decode the PPP traffic running in one of the virtual channels established iby the MUX protocol. I've not yet investigated since I need first to sort out points 1 and 2.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-27.010" rel="tag" title="see questions tagged &#39;27.010&#39;">27.010</span> <span class="post-tag tag-link-27010" rel="tag" title="see questions tagged &#39;27010&#39;">27010</span> <span class="post-tag tag-link-mux" rel="tag" title="see questions tagged &#39;mux&#39;">mux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '14, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/ebcadbc3f35027070675237b4e6a8aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Moema&#39;s gravatar image" /><p><span>Moema</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Moema has no accepted answers">0%</span></p></div></div><div id="comments-container-34659" class="comments-container"></div><div id="comment-tools-34659" class="comment-tools"></div><div class="clear"></div><div id="comment-34659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34695"></span>

<div id="answer-container-34695" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34695-score" class="post-score" title="current number of votes">0</div><span id="post-34695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found part of the answer : File &gt; Import from hexdump. Choose the file and select MUX27010. Issue I tried different format of hex file, once imported either no decoded packets appear or it says my packet is corrupted and indeed there is the last byte (MUX flag 0xf9) missing while it is in my original packet</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/ebcadbc3f35027070675237b4e6a8aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Moema&#39;s gravatar image" /><p><span>Moema</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Moema has no accepted answers">0%</span></p></div></div><div id="comments-container-34695" class="comments-container"></div><div id="comment-tools-34695" class="comment-tools"></div><div class="clear"></div><div id="comment-34695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

