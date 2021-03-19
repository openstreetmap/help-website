+++
type = "question"
title = "Limit / tailor tshark conversations output"
description = '''Hi I have to analyze a large number of pcap files and made a little script that outputs the conversations for tcp and udp.  -q -z conv,tcp -z conv,udp Thus far everything works fine. The problem is that I only need the top 10-20 entries of total bytes and don&#x27;t need the last ~60000 entries.  Is ther...'''
date = "2017-02-09T04:38:00Z"
lastmod = "2017-02-09T07:45:00Z"
weight = 59277
keywords = [ "filter", "tshark" ]
aliases = [ "/questions/59277" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Limit / tailor tshark conversations output](/questions/59277/limit-tailor-tshark-conversations-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59277-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I have to analyze a large number of pcap files and made a little script that outputs the conversations for tcp and udp.</p><p>-q -z conv,tcp -z conv,udp</p><p>Thus far everything works fine. The problem is that I only need the top 10-20 entries of total bytes and don't need the last ~60000 entries.</p><p>Is there an output filter that can limit the entries to top 10? Or maybe a way to only print the entry if the total traffic (or frames) is greater than a specified value?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">filter tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '17, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/2b55b040ef13c2d0b86bd0711b2a9b4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="laminatorius&#39;s gravatar image" /><p>laminatorius<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="laminatorius has no accepted answers">0%</span></p></div></div><div id="comments-container-59277" class="comments-container"></div><div id="comment-tools-59277" class="comment-tools"></div><div class="clear"></div><div id="comment-59277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59293"></span>

<div id="answer-container-59293" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59293-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no filtering on statistics output, That is left to external scripts.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '17, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59293" class="comments-container"></div><div id="comment-tools-59293" class="comment-tools"></div><div class="clear"></div><div id="comment-59293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

