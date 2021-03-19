+++
type = "question"
title = "RTP Analysis and Assessment"
description = '''Hi I have captured RTP stream and now trying to play it in the inbuilt wireshark player. It is reporting &quot;Drop by Jitter Buffer&quot;, &quot;Out of Sequence&quot; and Wrong Time Stamp. But in the player how do I know which one is showan as what. I have Red, Yellow color lines in the player and see Choppy voice but...'''
date = "2010-10-18T13:04:00Z"
lastmod = "2010-10-20T13:41:00Z"
weight = 527
keywords = [ "analysis", "voip", "calls", "rtp" ]
aliases = [ "/questions/527" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP Analysis and Assessment](/questions/527/rtp-analysis-and-assessment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-527-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I have captured RTP stream and now trying to play it in the inbuilt wireshark player. It is reporting "Drop by Jitter Buffer", "Out of Sequence" and Wrong Time Stamp. But in the player how do I know which one is showan as what. I have Red, Yellow color lines in the player and see Choppy voice but not able to interpret/separate these issues/packets.</p></div><div id="question-tags" class="tags-container tags">analysis voip calls rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '10, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/2771325c90a6728b571c45ac6e82d0ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RTPissues&#39;s gravatar image" /><p>RTPissues<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RTPissues has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '10, 13:06</p></div></div><div id="comments-container-527" class="comments-container"></div><div id="comment-tools-527" class="comment-tools"></div><div class="clear"></div><div id="comment-527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="567"></span>

<div id="answer-container-567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-567-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This part of the RTP player code tells you what's going on:</p><pre><code>                        if (status == S_DROP_BY_JITT) {
                                gc = red_gc;
                        } else if (status == S_WRONG_TIMESTAMP) {
                                gc = amber_gc;
                        } else {
                                gc = rci-&gt;draw_area-&gt;style-&gt;black_gc;
                        }</code></pre>So thats:<ol><li>Red for dropped packets</li><li>Amber for wrong time stamps</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '10, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-567" class="comments-container"></div><div id="comment-tools-567" class="comment-tools"></div><div class="clear"></div><div id="comment-567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

