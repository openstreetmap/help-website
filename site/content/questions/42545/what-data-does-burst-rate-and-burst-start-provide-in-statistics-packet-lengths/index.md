+++
type = "question"
title = "What data does &quot;Burst rate&quot; and &quot;Burst Start&quot; provide in Statistics / Packet Lengths?"
description = '''In Wireshark, I can view some basic packet statistics by going to Statistics -&amp;gt; Packet Lengths. I am able to understand all the values in each column except the following:  Burst rate = is this the number of packets sent in a given time? Burst start = is this when the burst starts? '''
date = "2015-05-19T08:15:00Z"
lastmod = "2015-06-12T08:45:00Z"
weight = 42545
keywords = [ "burst" ]
aliases = [ "/questions/42545" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What data does "Burst rate" and "Burst Start" provide in Statistics / Packet Lengths?](/questions/42545/what-data-does-burst-rate-and-burst-start-provide-in-statistics-packet-lengths)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42545-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark, I can view some basic packet statistics by going to Statistics -&gt; Packet Lengths. I am able to understand all the values in each column except the following:</p><ol><li>Burst rate = is this the number of packets sent in a given time?</li><li>Burst start = is this when the burst starts?</li></ol></div><div id="question-tags" class="tags-container tags">burst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '15, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42545" class="comments-container"><span id="42560"></span><div id="comment-42560" class="comment"><div id="post-42560-score" class="comment-score"></div><div class="comment-text"><p>Some clarification on my question. How does Wireshark determine the "burst rate" and the "burst start" parameters? I interpret "burst rate" as the maximum amount of packets sent within a time-frame. So it would be the maximum packets-per-second (pps) within the capture. The "burst start" would then be the time when the highest burst rate was experienced.</p><p>Are these interpretations correct?</p></div><div id="comment-42560-info" class="comment-info"><span class="comment-age">(19 May '15, 13:11)</span> Amato_C</div></div></div><div id="comment-tools-42545" class="comment-tools"></div><div class="clear"></div><div id="comment-42545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43097"></span>

<div id="answer-container-43097" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43097-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>After performing my own analysis, the following was determined:</p><ol><li>Burst = the maximum number of packets sent per interval of time</li><li>Burst start = the time when the maximum number of packets sent occurred</li></ol><p>Wireshark calculates the maximum number of packets sent per interval of time. The user is able to adjust the interval of time in 1 millisecond intervals.</p><p>Under Preferences -&gt; Statistics, the following parameters can be adjusted:</p><ul><li>Show burst count for item rather rate = if selected, the statistics will show the count of events within the burst window instead of a burst rate. Burst rate is calculated as the number of packets within the burst window divided by the burst window length.</li><li>Burst rate resolution = sets the duration of the time interval into which packets are grouped when calculating the burst rate.</li><li>Burst rate window size = sets the duration of the sliding window during which the burst rate is measured</li></ul><p>For my analyses, I set the following:</p><ul><li>Show burst count for item rather than rate = Enabled (check mark in the box)</li><li>Burst rate resolution = Burst rate window size</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '15, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-43097" class="comments-container"></div><div id="comment-tools-43097" class="comment-tools"></div><div class="clear"></div><div id="comment-43097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

