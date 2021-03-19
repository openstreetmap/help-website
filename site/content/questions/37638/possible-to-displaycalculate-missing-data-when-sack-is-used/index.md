+++
type = "question"
title = "Possible to display/calculate missing data when SACK is used?"
description = '''Is it possible to easily calculate and display e.g. a column that optimally shows the number of bytes of missing data whenever missing data is indicated using SACK? E.g. a server indicates missing data, by sending a packet with ACK 1000 and SLE 1100 and SRE 1400. The original data sent by the client...'''
date = "2014-11-07T00:17:00Z"
lastmod = "2014-11-07T14:06:00Z"
weight = 37638
keywords = [ "retransmission", "sack" ]
aliases = [ "/questions/37638" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Possible to display/calculate missing data when SACK is used?](/questions/37638/possible-to-displaycalculate-missing-data-when-sack-is-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37638-score" class="post-score" title="current number of votes">0</div><span id="post-37638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to easily calculate and display e.g. a column that optimally shows the number of bytes of missing data whenever missing data is indicated using SACK?</p><p>E.g. a server indicates missing data, by sending a packet with ACK 1000 and SLE 1100 and SRE 1400. The original data sent by the client was 1400 bytes.</p><p>So, in essence I would like to have a column that for the particular packet with SACK used, displays 100 bytes - i.e. the missing amount of traffic.</p><p>If a column is not possible, is this type of analysis possible using scripting or similar?</p><p>Reason being is that I see all data being received at the server, but for some reason, the server does not acknowledge it. I'm trying to find the smoking gun and my idea is that for whatever reason there might be a pattern where e.g. the server always "misses" 100 bytes of data.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-sack" rel="tag" title="see questions tagged &#39;sack&#39;">sack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/5a55fd7d0ca800a3b0724f350dbfec0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NJL&#39;s gravatar image" /><p><span>NJL</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NJL has no accepted answers">0%</span></p></div></div><div id="comments-container-37638" class="comments-container"></div><div id="comment-tools-37638" class="comment-tools"></div><div class="clear"></div><div id="comment-37638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37668"></span>

<div id="answer-container-37668" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37668-score" class="post-score" title="current number of votes">1</div><span id="post-37668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NJL has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think Wireshark can do this because you can't have columns that calculate stuff for you on the fly. You could try to add a custom column containing the SACK edges and export the packet list to CSV (via the file menu). Then import that file into Excel and have it calculate the missing pieces. I'm not sure though if this can be easily done, because you might have more than one SACK block in the options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37668" class="comments-container"><span id="37671"></span><div id="comment-37671" class="comment"><div id="post-37671-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the suggestion, but you were right, it's not something that's easily done unfortunately - at least not to be able to cover the full details as you suggest yourself.</p></div><div id="comment-37671-info" class="comment-info"><span class="comment-age">(07 Nov '14, 14:06)</span> <span class="comment-user userinfo">NJL</span></div></div></div><div id="comment-tools-37668" class="comment-tools"></div><div class="clear"></div><div id="comment-37668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

