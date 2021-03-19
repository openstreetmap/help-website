+++
type = "question"
title = "Wireshark - add little functionality"
description = '''Hello developers, would it be possible to add multi column sorting functionality into Wireshark? That would be really appreciated. It is not that efficient to analyze packets sorted by time. I rather use sort by TCP stream, however then packets are not sorted by time as well but rather in some rando...'''
date = "2011-02-22T02:50:00Z"
lastmod = "2011-11-07T15:36:00Z"
weight = 2471
keywords = [ "new", "request", "columns", "wireshark" ]
aliases = [ "/questions/2471" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - add little functionality](/questions/2471/wireshark-add-little-functionality)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2471-score" class="post-score" title="current number of votes">0</div><span id="post-2471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello developers, would it be possible to add multi column sorting functionality into Wireshark? That would be really appreciated. It is not that efficient to analyze packets sorted by time. I rather use sort by TCP stream, however then packets are not sorted by time as well but rather in some random order. Really, multi column sorting is needed. Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-new" rel="tag" title="see questions tagged &#39;new&#39;">new</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '11, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/1eb3036266e37b2f62d5dbdf584f09c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nightbass&#39;s gravatar image" /><p><span>nightbass</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nightbass has no accepted answers">0%</span></p></div></div><div id="comments-container-2471" class="comments-container"><span id="7265"></span><div id="comment-7265" class="comment"><div id="post-7265-score" class="comment-score"></div><div class="comment-text"><p>Just found this link via Google, because I have the same issue. I would like to sort first by Protocol, and then sequentially for any given protocol. I only need any given protocol packets, but then all is out of order. Ideally (in SQL parlance): ORDER BY protocol, time (or no.)</p><p>I get the GTK limitations, but just wanted to add my concern as well.</p></div><div id="comment-7265-info" class="comment-info"><span class="comment-age">(07 Nov '11, 15:23)</span> <span class="comment-user userinfo">Eric</span></div></div></div><div id="comment-tools-2471" class="comment-tools"></div><div class="clear"></div><div id="comment-2471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2472"></span>

<div id="answer-container-2472" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2472-score" class="post-score" title="current number of votes">1</div><span id="post-2472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to add this as a feature request in the Wireshark <a href="https://bugs.wireshark.org/bugzilla/">bugzilla</a> ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '11, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2472" class="comments-container"><span id="2482"></span><div id="comment-2482" class="comment"><div id="post-2482-score" class="comment-score">1</div><div class="comment-text"><p>I looked into that earlier, as I do find it annoying too. However, as far as I could tell at the time, we use GTK sorting functionality and it did not seem to include sorting on multiple columns. But I might be wrong in that...</p></div><div id="comment-2482-info" class="comment-info"><span class="comment-age">(22 Feb '11, 08:06)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-2472" class="comment-tools"></div><div class="clear"></div><div id="comment-2472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7266"></span>

<div id="answer-container-7266" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7266-score" class="post-score" title="current number of votes">0</div><span id="post-7266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I did just figure out I could user the filtering capabilities to isolate the protocol then can sort on time. So there is a work around. Thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '11, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/770aa2ab4ad652841d2cbc6f8c75bb0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eric&#39;s gravatar image" /><p><span>Eric</span><br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eric has no accepted answers">0%</span></p></div></div><div id="comments-container-7266" class="comments-container"></div><div id="comment-tools-7266" class="comment-tools"></div><div class="clear"></div><div id="comment-7266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

