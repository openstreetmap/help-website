+++
type = "question"
title = "Overlapping TCP Sack options"
description = '''Hi, I&#x27;m facing a strange issue. We have two systems communicating via RFC, but this communication breaks everytime with the following issue: The Client receives an TCP ACK with an SLE=2734286 and SLR=2777173 Client then starts a retransmission of the &quot;missing&quot; packages Then receives a TCP DUP ACK wi...'''
date = "2012-11-07T07:13:00Z"
lastmod = "2012-11-08T07:10:00Z"
weight = 15646
keywords = [ "ack", "overlapping", "sack", "tcp" ]
aliases = [ "/questions/15646" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overlapping TCP Sack options](/questions/15646/overlapping-tcp-sack-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15646-score" class="post-score" title="current number of votes">0</div><span id="post-15646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm facing a strange issue. We have two systems communicating via RFC, but this communication breaks everytime with the following issue:</p><p>The Client receives an TCP ACK with an SLE=2734286 and SLR=2777173 Client then starts a retransmission of the "missing" packages Then receives a TCP DUP ACK with SACK: 2777089-2777173 2734286-2777173</p><p>This is weird, isnt it? The SACK parameters are overlapping. The Client then sends again the missing packages but always receives the TCP DUP ACK. After 5 tries the client gives up.</p><p>Its Windows 2003 to Linux 2.6.32.</p><p>Is someone of you aware of such an issue? The Network connection itself is working without issues (for ex. when copying data via SSH, there the SACK protocol seems to work correct).</p><p>Thanks and kind regards Stefan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-overlapping" rel="tag" title="see questions tagged &#39;overlapping&#39;">overlapping</span> <span class="post-tag tag-link-sack" rel="tag" title="see questions tagged &#39;sack&#39;">sack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '12, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/6edf5924d036010b1bd2230fa74be47e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sLy&#39;s gravatar image" /><p><span>sLy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sLy has no accepted answers">0%</span></p></div></div><div id="comments-container-15646" class="comments-container"><span id="15652"></span><div id="comment-15652" class="comment"><div id="post-15652-score" class="comment-score"></div><div class="comment-text"><p>you need to supply the ACK number from the Acknowledgements in order to solve this, please provide ACK and SACK information for those packets plus if possible the tcp.len of the data packets</p></div><div id="comment-15652-info" class="comment-info"><span class="comment-age">(07 Nov '12, 07:57)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="15722"></span><div id="comment-15722" class="comment"><div id="post-15722-score" class="comment-score"></div><div class="comment-text"><p>Better yet, put the offending capture on cloudshark for us all to see.</p></div><div id="comment-15722-info" class="comment-info"><span class="comment-age">(08 Nov '12, 07:10)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-15646" class="comment-tools"></div><div class="clear"></div><div id="comment-15646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

