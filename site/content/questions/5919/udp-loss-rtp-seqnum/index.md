+++
type = "question"
title = "UDP loss (RTP, SeqNum)"
description = '''When transmitting video using RTP (H.264) over UDP, which is natural for SIP/H.323, it can be loss of some UDP datagrams. So it will be Sequnce Number of RTP of packet not equal Seq of previous packet + 1. It will be awesome if Wireshark can show, that it is incorrect SeqNum (frame lost). Curretly, ...'''
date = "2011-08-29T08:44:00Z"
lastmod = "2011-08-30T00:41:00Z"
weight = 5919
keywords = [ "loss", "udp", "h.264", "rtp" ]
aliases = [ "/questions/5919" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [UDP loss (RTP, SeqNum)](/questions/5919/udp-loss-rtp-seqnum)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5919-score" class="post-score" title="current number of votes">0</div><span id="post-5919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When transmitting video using RTP (H.264) over UDP, which is natural for SIP/H.323, it can be loss of some UDP datagrams. So it will be Sequnce Number of RTP of packet not equal Seq of previous packet + 1. It will be awesome if Wireshark can show, that it is incorrect SeqNum (frame lost). Curretly, it shows all the frames with same color. So I need to additionaly analyze the stream (I used Excel) for incorrect flow of SeqNum. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-loss" rel="tag" title="see questions tagged &#39;loss&#39;">loss</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-h.264" rel="tag" title="see questions tagged &#39;h.264&#39;">h.264</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '11, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/ed1f596bf4fc383f8ca4527c80cc8be7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%D0%9A%D0%BE%D1%81%D1%82%D1%8F%20%D0%A2%D1%80%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2&#39;s gravatar image" /><p><span>Костя Трушников</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Костя Трушников has no accepted answers">0%</span></p></div></div><div id="comments-container-5919" class="comments-container"></div><div id="comment-tools-5919" class="comment-tools"></div><div class="clear"></div><div id="comment-5919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5928"></span>

<div id="answer-container-5928" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5928-score" class="post-score" title="current number of votes">1</div><span id="post-5928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Костя Трушников has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can the menu option Telephony|RTP|Stream analysis help here?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '11, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5928" class="comments-container"><span id="5944"></span><div id="comment-5944" class="comment"><div id="post-5944-score" class="comment-score"></div><div class="comment-text"><p>Many thanks! It's exactly what I was searching for.</p></div><div id="comment-5944-info" class="comment-info"><span class="comment-age">(30 Aug '11, 00:25)</span> <span class="comment-user userinfo">Костя Трушников</span></div></div><span id="5947"></span><div id="comment-5947" class="comment"><div id="post-5947-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a "comment", please see the FAQ for details. Also please accept Jaap's answer by clicking on the checkmark on the left, this way the question will not appear on the "unanswered" question list anymore.</p></div><div id="comment-5947-info" class="comment-info"><span class="comment-age">(30 Aug '11, 00:41)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5928" class="comment-tools"></div><div class="clear"></div><div id="comment-5928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

