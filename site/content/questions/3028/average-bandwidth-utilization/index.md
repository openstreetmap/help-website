+++
type = "question"
title = "Average bandwidth utilization"
description = '''Wireshark comes highly recommended and I am very interested in using it. But I would like to know beforehand if the software can can plot, over a 24 hour period, the average bandwidth utilization of my T1 line.'''
date = "2011-03-22T11:00:00Z"
lastmod = "2011-03-22T16:02:00Z"
weight = 3028
keywords = [ "bandwidthutilization" ]
aliases = [ "/questions/3028" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Average bandwidth utilization](/questions/3028/average-bandwidth-utilization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3028-score" class="post-score" title="current number of votes">0</div><span id="post-3028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark comes highly recommended and I am very interested in using it. But I would like to know beforehand if the software can can plot, over a 24 hour period, the average bandwidth utilization of my T1 line.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidthutilization" rel="tag" title="see questions tagged &#39;bandwidthutilization&#39;">bandwidthutilization</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '11, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/74b1aade56d35e4b4ab28651a3511225?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VelaSystems&#39;s gravatar image" /><p><span>VelaSystems</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VelaSystems has no accepted answers">0%</span></p></div></div><div id="comments-container-3028" class="comments-container"></div><div id="comment-tools-3028" class="comment-tools"></div><div class="clear"></div><div id="comment-3028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3033"></span>

<div id="answer-container-3033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3033-score" class="post-score" title="current number of votes">0</div><span id="post-3033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you can manage to fit that 24 hour period into one single capture file without crashing Wireshark on loading it you might be able to do that with the I/O graph feature found in the statistics menu.</p><p>I kinda expect your line to go way beyond a couple of hundred megabytes though, which usually means you're going to hit the dreaded out of memory wall on loading it again. Maybe capturing only a couple of bytes per frame could drastically reduce the capture file size but you might still encounter memory problems caused by the sheer number of packets you'll record.</p><p>Maybe you want to look at other tools instead, like MRTG or something - it's possible they are a better solution for you if you're not interested in capturing packet data but graphing throughput.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '11, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3033" class="comments-container"></div><div id="comment-tools-3033" class="comment-tools"></div><div class="clear"></div><div id="comment-3033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

