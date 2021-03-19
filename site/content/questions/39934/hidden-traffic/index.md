+++
type = "question"
title = "Hidden Traffic"
description = '''does anybody know if there is traffic that Wireshak can`t capture, I mean, you don&#x27;t see this traffic in the program. '''
date = "2015-02-18T13:02:00Z"
lastmod = "2015-02-23T08:20:00Z"
weight = 39934
keywords = [ "hidden", "traffic" ]
aliases = [ "/questions/39934" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Hidden Traffic](/questions/39934/hidden-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39934-score" class="post-score" title="current number of votes">0</div><span id="post-39934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>does anybody know if there is traffic that Wireshak can`t capture, I mean, you don't see this traffic in the program.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hidden" rel="tag" title="see questions tagged &#39;hidden&#39;">hidden</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '15, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/d483adfbcf277a7694953592d06c68b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pim&#39;s gravatar image" /><p><span>Pim</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pim has no accepted answers">0%</span></p></div></div><div id="comments-container-39934" class="comments-container"></div><div id="comment-tools-39934" class="comment-tools"></div><div class="clear"></div><div id="comment-39934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39943"></span>

<div id="answer-container-39943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39943-score" class="post-score" title="current number of votes">1</div><span id="post-39943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can't capture anything....</p><p>It uses dumpcap to do the capture for it. How does dumpcap do it? Well, it uses the libpcap library (as applicable for the platform) capabilities to capture traffic.</p><p>How does libpcap do it? As said, depending on the platform, it latches on to the network stack and gets its packets from there. This means NDIS5 on Windows, it means (ever more capable) (packet) socket on Un*x like platforms, etc.</p><p>So, any traffic that is not passing via a path that libpcap can latch on to cannot be captured.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '15, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39943" class="comments-container"><span id="40008"></span><div id="comment-40008" class="comment"><div id="post-40008-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Jaap but could you give some type of traffic that is not passing via a path that libpcap can latch on? and with this type of traffic in wireshark you don't see anything, no?</p></div><div id="comment-40008-info" class="comment-info"><span class="comment-age">(21 Feb '15, 10:35)</span> <span class="comment-user userinfo">Pim</span></div></div><span id="40020"></span><div id="comment-40020" class="comment"><div id="post-40020-score" class="comment-score"></div><div class="comment-text"><p>Nothing much really. Traffic going directly onto an bus that's not serviced by the network stack come to mind. Eg. traffic on an I2C bus probably won't show up on an interface that libpcap can select. But the relevance of such interface as an network interface is questionable. Still it could be doen given the right hardware. Look at DECT for instance. Not something available in stock network capture, but with the right hardware it can be captured, and readily decoded in Wireshark.</p></div><div id="comment-40020-info" class="comment-info"><span class="comment-age">(23 Feb '15, 04:33)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="40021"></span><div id="comment-40021" class="comment"><div id="post-40021-score" class="comment-score"></div><div class="comment-text"><p>If the reason for the question is that you think that you ought to see some tarffic that you are not seeing chanses are that there's something wrong with your capture setup or if you are expecting protocol foo but only seeing UDP/TCP that some preference needs tuning. If you try to describe what you think arte missing we might be able to help you further.</p></div><div id="comment-40021-info" class="comment-info"><span class="comment-age">(23 Feb '15, 04:57)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="40025"></span><div id="comment-40025" class="comment"><div id="post-40025-score" class="comment-score"></div><div class="comment-text"><p>He, we're tracking into the wilderness here, into uncharted territories ;) But I guess you're right; <span>@Pim</span>: what did you expect to see?</p></div><div id="comment-40025-info" class="comment-info"><span class="comment-age">(23 Feb '15, 08:20)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-39943" class="comment-tools"></div><div class="clear"></div><div id="comment-39943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

