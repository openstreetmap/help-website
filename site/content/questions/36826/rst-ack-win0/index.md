+++
type = "question"
title = "RST ACK Win=0?"
description = '''I&#x27;m a Systems Engineer and not a network guru, so please bear with me. Trying to figure out a major issue with inbound email attachment delivery. Our headquarters Exchange servers are unable to receive any emails with attachments. Other emails are delivered fine. Our Exchange servers at our DR site ...'''
date = "2014-10-03T13:16:00Z"
lastmod = "2014-10-03T16:14:00Z"
weight = 36826
keywords = [ "attachments", "smtp", "email", "exchange" ]
aliases = [ "/questions/36826" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [RST ACK Win=0?](/questions/36826/rst-ack-win0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36826-score" class="post-score" title="current number of votes">0</div><span id="post-36826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a Systems Engineer and not a network guru, so please bear with me. Trying to figure out a major issue with inbound email attachment delivery. Our headquarters Exchange servers are unable to receive any emails with attachments. Other emails are delivered fine. Our Exchange servers at our DR site CAN receive attachments. The Exchange servers show no performance issues, and we can delivery large attachments to them fine internally. Several network devices sit in front of the Exchange boxes (firewall, IDS, load balancer, etc) but the network team has run their own captures and say it is not a network issue. So I ran a capture on the Exchange server and sent a large attachment from the Internet.</p><p>I'm a novice at reading captures, but I see a packet highlighted in red that shows "RST,ACK" and "Win=0". This is from the sending server to our server. Is this abnormal?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-attachments" rel="tag" title="see questions tagged &#39;attachments&#39;">attachments</span> <span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span> <span class="post-tag tag-link-email" rel="tag" title="see questions tagged &#39;email&#39;">email</span> <span class="post-tag tag-link-exchange" rel="tag" title="see questions tagged &#39;exchange&#39;">exchange</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '14, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/3c69c6b1cb7be5cc3ab9f7e2136b1854?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SassyMoose&#39;s gravatar image" /><p><span>SassyMoose</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SassyMoose has no accepted answers">0%</span></p></div></div><div id="comments-container-36826" class="comments-container"></div><div id="comment-tools-36826" class="comment-tools"></div><div class="clear"></div><div id="comment-36826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36827"></span>

<div id="answer-container-36827" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36827-score" class="post-score" title="current number of votes">2</div><span id="post-36827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SassyMoose has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It can be, but today, in most cases it's not, especially if you're using Microsoft products. Reset packets were once used exclusively to signal connection abort due to trouble, while FIN was used for graceful shutdowns. These days, many products terminate perfectly good sessions with RST to perform a quicker shutdown compared to FIN. So you'd have to determine if there was a problem with the TCP session to tell if the RST was sent because there was a problem, or if it is just normal session termination.</p><p>BTW, TCP window size is <strong>always</strong> zero in packets with the RST flag set. That's normal, too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '14, 16:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36827" class="comments-container"></div><div id="comment-tools-36827" class="comment-tools"></div><div class="clear"></div><div id="comment-36827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

