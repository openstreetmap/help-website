+++
type = "question"
title = "Getting only ACK after 3 handshake"
description = '''In the capture getting only ACK after 3 way handshake, there are also some dup ack and psh ack packet. But major count of packet is ACK.  after 3 way handshake, there must be data packet but don&#x27;t see any in complete capture. '''
date = "2016-12-05T07:41:00Z"
lastmod = "2016-12-06T01:42:00Z"
weight = 57866
keywords = [ "ack", "ony", "getting" ]
aliases = [ "/questions/57866" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting only ACK after 3 handshake](/questions/57866/getting-only-ack-after-3-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57866-score" class="post-score" title="current number of votes">0</div><span id="post-57866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the capture getting only ACK after 3 way handshake, there are also some dup ack and psh ack packet. But major count of packet is ACK.</p><p>after 3 way handshake, there must be data packet but don't see any in complete capture.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_2WIlzOg.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-ony" rel="tag" title="see questions tagged &#39;ony&#39;">ony</span> <span class="post-tag tag-link-getting" rel="tag" title="see questions tagged &#39;getting&#39;">getting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '16, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/78f2d943102555b1c191b044ca584ba8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajputparveen&#39;s gravatar image" /><p><span>Rajputparveen</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajputparveen has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57866" class="comments-container"></div><div id="comment-tools-57866" class="comment-tools"></div><div class="clear"></div><div id="comment-57866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57867"></span>

<div id="answer-container-57867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57867-score" class="post-score" title="current number of votes">1</div><span id="post-57867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check all the packets with "Len=" at the end - those are packets with TCP data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '16, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-57867" class="comments-container"><span id="57868"></span><div id="comment-57868" class="comment"><div id="post-57868-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for reply. Does all data packet keep ACK tag? there are only ACK tag whether sender or receiver sending the packet.</p><p>yes, have capture of length 1200 byte but with ACK tag only.</p></div><div id="comment-57868-info" class="comment-info"><span class="comment-age">(05 Dec '16, 07:54)</span> <span class="comment-user userinfo">Rajputparveen</span></div></div><span id="57869"></span><div id="comment-57869" class="comment"><div id="post-57869-score" class="comment-score">1</div><div class="comment-text"><p>Yes, all TCP packets except the first SYN packet of a conversation have the ACK flag set. Every packet except the first always acknowledges the packets from the other side, even if there's no new data (in which case the ACK number simply stays the same).</p></div><div id="comment-57869-info" class="comment-info"><span class="comment-age">(05 Dec '16, 08:00)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="57888"></span><div id="comment-57888" class="comment"><div id="post-57888-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the information.</p></div><div id="comment-57888-info" class="comment-info"><span class="comment-age">(05 Dec '16, 23:53)</span> <span class="comment-user userinfo">Rajputparveen</span></div></div><span id="57890"></span><div id="comment-57890" class="comment"><div id="post-57890-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-57890-info" class="comment-info"><span class="comment-age">(06 Dec '16, 01:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-57867" class="comment-tools"></div><div class="clear"></div><div id="comment-57867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

