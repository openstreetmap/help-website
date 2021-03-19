+++
type = "question"
title = "TCP Previous Segment not Captured"
description = '''Trying to solve issue for getting quickbooks updates during what looks like three attempts to pull updates from their apache download servers: first error is TCP Previous segment not captured from quickbooks server to our system. Also TCP Retransmission ACK in both directions during exchanges'''
date = "2017-06-19T14:47:00Z"
lastmod = "2017-06-21T06:51:00Z"
weight = 62143
keywords = [ "tcp_retransmission", "segment_not_captured", "tcp-segment", "tcp", "retransmissions" ]
aliases = [ "/questions/62143" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Previous Segment not Captured](/questions/62143/tcp-previous-segment-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62143-score" class="post-score" title="current number of votes">0</div><span id="post-62143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to solve issue for getting quickbooks updates during what looks like three attempts to pull updates from their apache download servers: first error is TCP Previous segment not captured from quickbooks server to our system. Also TCP Retransmission ACK in both directions during exchanges</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_retransmission" rel="tag" title="see questions tagged &#39;tcp_retransmission&#39;">tcp_retransmission</span> <span class="post-tag tag-link-segment_not_captured" rel="tag" title="see questions tagged &#39;segment_not_captured&#39;">segment_not_captured</span> <span class="post-tag tag-link-tcp-segment" rel="tag" title="see questions tagged &#39;tcp-segment&#39;">tcp-segment</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '17, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/e2d5504e07bacc5ad2a7618169a1d10d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="QuickN&#39;s gravatar image" /><p><span>QuickN</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="QuickN has no accepted answers">0%</span></p></div></div><div id="comments-container-62143" class="comments-container"></div><div id="comment-tools-62143" class="comment-tools"></div><div class="clear"></div><div id="comment-62143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62199"></span>

<div id="answer-container-62199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62199-score" class="post-score" title="current number of votes">0</div><span id="post-62199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A sample capture would help. Only one (or few) "Previous Segment not Captured" towards the beginning usually is due to an ongoing TCP connection when the capture begins. If you have more down the line it suggests the capture itself it not keeping up (so it misses the data packet but sees the ACK). You get just ACK retransmission or data retransmission also?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '17, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/ae9b5fba493daf2baf29a681f99e7418?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silvio&#39;s gravatar image" /><p><span>silvio</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silvio has one accepted answer">50%</span></p></div></div><div id="comments-container-62199" class="comments-container"><span id="62205"></span><div id="comment-62205" class="comment"><div id="post-62205-score" class="comment-score"></div><div class="comment-text"><p>Thanks ..looks like I can upload pic file in JPG the pcapng wouldnt upload for some reason</p><p><img src="https://osqa-ask.wireshark.org/upfiles/InuitTraffic.jpg" width="640" /></p><p>Thanks Mike</p></div><div id="comment-62205-info" class="comment-info"><span class="comment-age">(21 Jun '17, 05:20)</span> <span class="comment-user userinfo">QuickN</span></div></div><span id="62206"></span><div id="comment-62206" class="comment"><div id="post-62206-score" class="comment-score"></div><div class="comment-text"><p>Analysis by screenshot is painful and mostly unproductive, i.e. we want to see things that aren't visible.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-62206-info" class="comment-info"><span class="comment-age">(21 Jun '17, 06:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-62199" class="comment-tools"></div><div class="clear"></div><div id="comment-62199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

