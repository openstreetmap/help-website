+++
type = "question"
title = "Retransmission Troubleshooting"
description = '''https://www.cloudshark.org/captures/e2392f0293d3 We are getting these resets intermittently. Is this caused by network congestion? The capture filter was set for the .32 address and was captured on .52. We are trying to find the cause. Could one of the two servers be overloaded?'''
date = "2015-02-10T05:17:00Z"
lastmod = "2015-02-13T21:58:00Z"
weight = 39760
keywords = [ "reset", "dup-ack" ]
aliases = [ "/questions/39760" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Retransmission Troubleshooting](/questions/39760/retransmission-troubleshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39760-score" class="post-score" title="current number of votes">0</div><span id="post-39760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="https://www.cloudshark.org/captures/e2392f0293d3">https://www.cloudshark.org/captures/e2392f0293d3</a></p><p>We are getting these resets intermittently. Is this caused by network congestion? The capture filter was set for the .32 address and was captured on .52. We are trying to find the cause. Could one of the two servers be overloaded?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reset" rel="tag" title="see questions tagged &#39;reset&#39;">reset</span> <span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/8df2c56f86d36f5e9f6f52b618c62781?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="realisticspeakers&#39;s gravatar image" /><p><span>realisticspe...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="realisticspeakers has no accepted answers">0%</span></p></div></div><div id="comments-container-39760" class="comments-container"><span id="39861"></span><div id="comment-39861" class="comment"><div id="post-39861-score" class="comment-score"></div><div class="comment-text"><p>This capture is taken on windows system(17.52) and there are lot of packet drops and i can see only retransmitted packets and not the actual packet from 10.32(linux server,can also verify this by looking at gap in ip.id)it means drop could be at network or .32 server itself.Destination is one hop away from source(look at TTL Value).So to truly find out wheather its network or server, you need to capture at both client and server at same time.</p></div><div id="comment-39861-info" class="comment-info"><span class="comment-age">(13 Feb '15, 21:58)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-39760" class="comment-tools"></div><div class="clear"></div><div id="comment-39760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

