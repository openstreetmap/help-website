+++
type = "question"
title = "Display time in seconds without date using -T fields -e"
description = '''When I use the command below: $ tshark -r fie.pcap -T fields -e frame.number -e frame.time -e ip.src -e ip.proto I get the time with the date including. How can I display just the time (not the date) only in seconds (not hours or minutes). if I add -t a before -r, I still get the date displayed toge...'''
date = "2016-11-25T00:08:00Z"
lastmod = "2016-11-25T02:47:00Z"
weight = 57631
keywords = [ "seconds", "fields", "display", "time" ]
aliases = [ "/questions/57631" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Display time in seconds without date using -T fields -e](/questions/57631/display-time-in-seconds-without-date-using-t-fields-e)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57631-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I use the command below: $ tshark -r fie.pcap -T fields -e frame.number -e frame.time -e ip.src -e ip.proto</p><p>I get the time with the date including. How can I display just the time (not the date) only in seconds (not hours or minutes). if I add -t a before -r, I still get the date displayed together with the time in hours, min and seconds. After sorting by IP source address, I am trying to determine the duration of those flows that have 100 packets or more for each IP source address. Thank you.</p></div><div id="question-tags" class="tags-container tags">seconds fields display time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '16, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/b3f6579bb81c4e2875f9293da09b05c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaryR&#39;s gravatar image" /><p>MaryR<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaryR has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '16, 03:16</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-57631" class="comments-container"></div><div id="comment-tools-57631" class="comment-tools"></div><div class="clear"></div><div id="comment-57631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57632"></span>

<div id="answer-container-57632" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57632-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're not looking for frame.time but what presented in the Time column (that's not the same).</p><pre><code>$ tshark -r fie.pcap -T fields -e frame.number -t e -e _ws.col.Time -e ip.src -e ip.proto</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '16, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57632" class="comments-container"><span id="57636"></span><div id="comment-57636" class="comment"><div id="post-57636-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your help Jaap. Just to clarify (for me):</p><p>I get a display with 4 columns/fileds: frame#, time (in secs), ip source, protocol, so "-t e _ws.col.Time" , all this expression displays the time in seconds, correct?<br />
</p><p>The last column I wanted to display whether UDP, TCP or ICMP traffic, so I don't think ip.proto was the right filter because I just get a column with the number "6". What would be the right filter for that purpose?</p><p>Thank you very much.</p></div><div id="comment-57636-info" class="comment-info"><span class="comment-age">(25 Nov '16, 07:55)</span> MaryR</div></div></div><div id="comment-tools-57632" class="comment-tools"></div><div class="clear"></div><div id="comment-57632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

