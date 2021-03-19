+++
type = "question"
title = "Why TCP sequence number from sender is more greater than window size value ?"
description = '''Hi, Here&#x27;s a question which confuse me for a long time. From current TCP designed,  sender shall not keep send the packet which more greater than window size before sender receive TCP ack. But I&#x27;ve found this symptom whenever I capture the tcp packet by wireshark. For example : Packet No.100 shows a...'''
date = "2016-07-14T02:19:00Z"
lastmod = "2016-07-14T18:41:00Z"
weight = 54060
keywords = [ "tcpwindowsize" ]
aliases = [ "/questions/54060" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why TCP sequence number from sender is more greater than window size value ?](/questions/54060/why-tcp-sequence-number-from-sender-is-more-greater-than-window-size-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54060-score" class="post-score" title="current number of votes">0</div><span id="post-54060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Here's a question which confuse me for a long time.</p><p>From current TCP designed, sender shall not keep send the packet which more greater than window size before sender receive TCP ack. But I've found this symptom whenever I capture the tcp packet by wireshark.</p><p>For example : Packet No.100 shows a TCP ACK from server, and ACK is 19492177, Calculate window size value is 31950. So the next packet sequence from Sender shall not exceed 19524127(19492177 + 31950), right?</p><p>But I've just found the next packet(No.101) sequence number send from sender is 1960509. And it is same TCP session.</p><p>Window size unit is byte on wireshark right? Could anyone help answer this question if possible ?</p><p>Thanks a lot!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '16, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/1f97b58287808efea0875fa8eb9d1167?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coverknox&#39;s gravatar image" /><p><span>coverknox</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coverknox has no accepted answers">0%</span></p></div></div><div id="comments-container-54060" class="comments-container"></div><div id="comment-tools-54060" class="comment-tools"></div><div class="clear"></div><div id="comment-54060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54071"></span>

<div id="answer-container-54071" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54071-score" class="post-score" title="current number of votes">0</div><span id="post-54071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, answer question by myself. I've just found if you'd like to get correct window size calculate number. You'll need to capture full TCP handshake such as TCP SYNC/SYN-ACK. Otherwise, you'll get wrong window size/sequence number mapping on wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '16, 18:41</strong></p><img src="https://secure.gravatar.com/avatar/1f97b58287808efea0875fa8eb9d1167?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coverknox&#39;s gravatar image" /><p><span>coverknox</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coverknox has no accepted answers">0%</span></p></div></div><div id="comments-container-54071" class="comments-container"></div><div id="comment-tools-54071" class="comment-tools"></div><div class="clear"></div><div id="comment-54071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

