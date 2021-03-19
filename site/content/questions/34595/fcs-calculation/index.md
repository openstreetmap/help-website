+++
type = "question"
title = "FCS calculation"
description = '''Hi, I want to calculate the FCS in pcap library over the packet.can i do that.If yes then how please let us know. If it can be calculated then how we will verify that it is correct or not Thanks and Advance.'''
date = "2014-07-11T04:08:00Z"
lastmod = "2014-07-11T14:36:00Z"
weight = 34595
keywords = [ "fcscalculation" ]
aliases = [ "/questions/34595" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FCS calculation](/questions/34595/fcs-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34595-score" class="post-score" title="current number of votes">0</div><span id="post-34595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I want to calculate the FCS in pcap library over the packet.can i do that.If yes then how please let us know. If it can be calculated then how we will verify that it is correct or not</p><p>Thanks and Advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fcscalculation" rel="tag" title="see questions tagged &#39;fcscalculation&#39;">fcscalculation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '14, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/76b6f92528aa678f6f54c4de570977bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="irajeev&#39;s gravatar image" /><p><span>irajeev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="irajeev has no accepted answers">0%</span></p></div></div><div id="comments-container-34595" class="comments-container"></div><div id="comment-tools-34595" class="comment-tools"></div><div class="clear"></div><div id="comment-34595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34596"></span>

<div id="answer-container-34596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34596-score" class="post-score" title="current number of votes">0</div><span id="post-34596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure if the PCAP library supports calculating the FCS. Problem is that you will not be able to record (and thus verify) the FCS, unless you're using a commercial capture solution that supports this.</p><p>The Ethernet FCS is just a CRC32 checksum, so you can use any library that has a CRC32 routine and pass the frame content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '14, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34596" class="comments-container"><span id="34608"></span><div id="comment-34608" class="comment"><div id="post-34608-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I'm not sure if the PCAP library supports calculating the FCS.</p></blockquote><p>libpcap/WinPcap is for capturing packets, not processing them; it doesn't include code to calculate an FCS.</p></div><div id="comment-34608-info" class="comment-info"><span class="comment-age">(11 Jul '14, 14:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-34596" class="comment-tools"></div><div class="clear"></div><div id="comment-34596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

