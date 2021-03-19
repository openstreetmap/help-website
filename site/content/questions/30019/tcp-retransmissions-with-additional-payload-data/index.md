+++
type = "question"
title = "TCP retransmissions with additional payload data?"
description = '''I&#x27;m seeing exactly what the question suggests - TCP retransmissions in which the retransmitted packet has more payload data than does the original transmission. In other words, packet A has X bytes of data when originally transmitted, but the retransmitted packet A has X+Y bytes of data. I&#x27;ve found ...'''
date = "2014-02-19T09:23:00Z"
lastmod = "2014-02-19T10:37:00Z"
weight = 30019
keywords = [ "retransmissions", "tcp", "sequence" ]
aliases = [ "/questions/30019" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP retransmissions with additional payload data?](/questions/30019/tcp-retransmissions-with-additional-payload-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30019-score" class="post-score" title="current number of votes">1</div><span id="post-30019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm seeing exactly what the question suggests - TCP retransmissions in which the retransmitted packet has more payload data than does the original transmission. In other words, packet A has X bytes of data when originally transmitted, but the retransmitted packet A has X+Y bytes of data.</p><p>I've found one or two references that simply say, "Oh, that's perfectly acceptable," but they provide no references to definitive information on the subject. It seems to me that once a TCP segment is assigned a sequence number, sent, and placed in the retransmission queue, it doesn't make sense to go add data to it later. Assuming that both the original packet and the (extra payload) retransmission arrive at the destination endpoint, how is the receiving stack supposed to handle two packets with the same sequence number?</p><p>Is there anything in the RFCs to address this behavior one way or the other?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '14, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-30019" class="comments-container"></div><div id="comment-tools-30019" class="comment-tools"></div><div class="clear"></div><div id="comment-30019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30020"></span>

<div id="answer-container-30020" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30020-score" class="post-score" title="current number of votes">2</div><span id="post-30020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wesmorgan1 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer:</p><p>The behavior you describe is the way TCP works.</p><p>The somewhat longer answer:</p><p>TCP is a <em>streaming</em> protocol (not a block oriented protocol).</p><p>There's no notion of what you call a "tcp segment with an assigned sequence number".</p><p>Each byte has its own sequence number. (0, 1, 2, 3, ...). A TCP packet specifies the sequence number of the first byte and the length (and thus the sequence number of the last byte can be determined).</p><p>So: a retransmission may include additional data if the sender has same available at the time of retransmission. The receiver just keeps track (via the sequence numbers) of what bytes have been received.</p><p>This is the way TCP works and will be described in most any book about TCP/IP and in the TCP RFCs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '14, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Feb '14, 09:42</strong> </span></p></div></div><div id="comments-container-30020" class="comments-container"><span id="30025"></span><div id="comment-30025" class="comment"><div id="post-30025-score" class="comment-score"></div><div class="comment-text"><p>Found it - in RFC 793 under 'Managing the Window': "The sending TCP packages the data to be transmitted into segments which fit the current window, and may repackage segments on the retransmission queue. Such repackaging is not required, but may be helpful."</p><p>You're right - I was conflating IP packets with TCP segments. Argh.</p><p>Thanks!</p></div><div id="comment-30025-info" class="comment-info"><span class="comment-age">(19 Feb '14, 10:37)</span> <span class="comment-user userinfo">wesmorgan1</span></div></div></div><div id="comment-tools-30020" class="comment-tools"></div><div class="clear"></div><div id="comment-30020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

