+++
type = "question"
title = "Checksum offload info from out-of-band data of a captured packet"
description = '''Hi There Does Wireshark/WinPCAP capture and show the checksum offload info from the out-of-band data? Thanks Arun'''
date = "2010-10-12T10:22:00Z"
lastmod = "2010-10-13T11:01:00Z"
weight = 491
keywords = [ "checksum", "offload", "oob" ]
aliases = [ "/questions/491" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Checksum offload info from out-of-band data of a captured packet](/questions/491/checksum-offload-info-from-out-of-band-data-of-a-captured-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-491-score" class="post-score" title="current number of votes">0</div><span id="post-491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There</p><p>Does Wireshark/WinPCAP capture and show the checksum offload info from the out-of-band data?</p><p>Thanks Arun</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-offload" rel="tag" title="see questions tagged &#39;offload&#39;">offload</span> <span class="post-tag tag-link-oob" rel="tag" title="see questions tagged &#39;oob&#39;">oob</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '10, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/64768a1efed360818357a0b38f63b073?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun&#39;s gravatar image" /><p><span>Arun</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun has no accepted answers">0%</span></p></div></div><div id="comments-container-491" class="comments-container"><span id="495"></span><div id="comment-495" class="comment"><div id="post-495-score" class="comment-score"></div><div class="comment-text"><p>Hi Arun - can you be a bit more specific regarding which out-of-band data you are interested in? If the out-of-band data is carried in a packet and it is passed up to Wireshark, then you should be able to see it. There is some out-of-band data that does not actually cross the network, but is used between a driver and protocol stack, hence the question for clarification.</p></div><div id="comment-495-info" class="comment-info"><span class="comment-age">(12 Oct '10, 21:20)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div><span id="497"></span><div id="comment-497" class="comment"><div id="post-497-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Thanks for the quick response. Sorry I should have been more clear. This is about the out-of-band data used between NIC driver and protocol stack. Specifically I want to find out if a Checksum offloading adapter/driver said good checksum or bad checksum for an incoming packet.</p><p>Thanks Arun</p></div><div id="comment-497-info" class="comment-info"><span class="comment-age">(12 Oct '10, 22:15)</span> <span class="comment-user userinfo">Arun</span></div></div></div><div id="comment-tools-491" class="comment-tools"></div><div class="clear"></div><div id="comment-491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="505"></span>

<div id="answer-container-505" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-505-score" class="post-score" title="current number of votes">0</div><span id="post-505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm going to guess a big No on this one. Dropped packet stats <em>may</em> be recorded by the driver somewhere - but those communications are probably not seen by wireshark. Its kind of against the point to have an offloading NIC report back to the CPU when it drops a packet...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '10, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-505" class="comments-container"></div><div id="comment-tools-505" class="comment-tools"></div><div class="clear"></div><div id="comment-505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

