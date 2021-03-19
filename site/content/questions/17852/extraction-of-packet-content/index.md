+++
type = "question"
title = "Extraction of packet content"
description = '''Dear all, I am new in packet sniffing and processing. I would like to ask you if there is an easy way to filter packets according to their content. For example if payload consists of temperature data, do you think that a query such that (if data &amp;gt; 30deg) is possible? Thank you in advance '''
date = "2013-01-22T03:18:00Z"
lastmod = "2013-01-22T07:17:00Z"
weight = 17852
keywords = [ "content", "data", "routing" ]
aliases = [ "/questions/17852" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extraction of packet content](/questions/17852/extraction-of-packet-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17852-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>I am new in packet sniffing and processing.</p><p>I would like to ask you if there is an easy way to filter packets according to their content.</p><p>For example if payload consists of temperature data, do you think that a query such that (if data &gt; 30deg) is possible?</p><p>Thank you in advance<br />
</p></div><div id="question-tags" class="tags-container tags">content data routing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '13, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/7bf1bea3b12c841c704c749201b47727?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Foued&#39;s gravatar image" /><p>Foued<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Foued has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-17852" class="comments-container"></div><div id="comment-tools-17852" class="comment-tools"></div><div class="clear"></div><div id="comment-17852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17853"></span>

<div id="answer-container-17853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17853-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Data is just that, raw data. To give it meaning, like temperature in degrees Celsius, you either:</p><ul><li>Create a display filter which selects part of the data, which you then give meaning.</li><li>Create a dissector to make the interpretation of the data, and present it to the user.</li></ul><p>For example, if you know that the byte you want to look at (the temp) is at offset 10 from the start of the data payload, and you know the data is the temperature in degrees, then you can use <code>data.data[10:1] &gt; "\x1e"</code> to filter them out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-17853" class="comments-container"></div><div id="comment-tools-17853" class="comment-tools"></div><div class="clear"></div><div id="comment-17853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17858"></span>

<div id="answer-container-17858" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17858-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Look here <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayFilterSection.html">Filter packets</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p>Ewgenijkkg<br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span></p></div></div><div id="comments-container-17858" class="comments-container"></div><div id="comment-tools-17858" class="comment-tools"></div><div class="clear"></div><div id="comment-17858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

