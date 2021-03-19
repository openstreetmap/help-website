+++
type = "question"
title = "What do dropped packets look like ?"
description = '''Im using wireshark to measure command to response times as I slam a server with high rate messaging. Every once in a while a message is an outlier duration wise. It may be just dropped packets as seen at http://cloudshark.org/captures/0995a4524824 . Thanks for inputs. '''
date = "2013-01-26T20:39:00Z"
lastmod = "2013-01-27T03:37:00Z"
weight = 17975
keywords = [ "packets", "dropped" ]
aliases = [ "/questions/17975" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What do dropped packets look like ?](/questions/17975/what-do-dropped-packets-look-like)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17975-score" class="post-score" title="current number of votes">0</div><span id="post-17975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im using wireshark to measure command to response times as I slam a server with high rate messaging. Every once in a while a message is an outlier duration wise. It may be just dropped packets as seen at <a href="http://cloudshark.org/captures/0995a4524824">http://cloudshark.org/captures/0995a4524824</a> . Thanks for inputs.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-dropped" rel="tag" title="see questions tagged &#39;dropped&#39;">dropped</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '13, 20:39</strong></p><img src="https://secure.gravatar.com/avatar/a3d3d442ba6a0eb1b3086e142e66f0bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dogma&#39;s gravatar image" /><p><span>dogma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dogma has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jan '13, 20:45</strong> </span></p></div></div><div id="comments-container-17975" class="comments-container"></div><div id="comment-tools-17975" class="comment-tools"></div><div class="clear"></div><div id="comment-17975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17981"></span>

<div id="answer-container-17981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17981-score" class="post-score" title="current number of votes">1</div><span id="post-17981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you have in that trace are expert messages saying "acked unseen segment" and "previous segment not captured".</p><ul><li>"acked unseen segment" is a message that basically tells you that there was an acknowledge to a data packet that you do not have in your capture, but the receiver got it. This means that your capture device was to slow to pick that data packet, you only got the ACk. Which is quite often the case because ACK packets are small (unless the ACK is piggybacked on some data) and so the chances of being captured are higher.</li><li>"previous segment not captured" either means that the packet was lost on the way, so neither the receiver nor the capture device got it. Or it got through to the receiver but the capture device didn't record it for performance reasons. Usually you'd have to track to the gap in the sequence numbers and check if there is a retransmission (which would indicate a packet loss, unless it is just an out-of-order - it can get very complicated :-)), or if you find an ACK to that "lost" packet you know that it was dropped by the capture device - because the receiver got it.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '13, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17981" class="comments-container"></div><div id="comment-tools-17981" class="comment-tools"></div><div class="clear"></div><div id="comment-17981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

