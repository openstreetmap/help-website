+++
type = "question"
title = "How do you filter so that there is one listing per IP?"
description = '''I wanted to find out how to filter my results so that I don&#x27;t have one listing per packet and just have one listing per ip. Thanks in advance'''
date = "2016-02-14T01:13:00Z"
lastmod = "2016-02-14T07:20:00Z"
weight = 50179
keywords = [ "filter", "ip", "results", "packet" ]
aliases = [ "/questions/50179" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do you filter so that there is one listing per IP?](/questions/50179/how-do-you-filter-so-that-there-is-one-listing-per-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50179-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to find out how to filter my results so that I don't have one listing per packet and just have one listing per ip.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">filter ip results packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '16, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/525180525586821431613aa3acf652e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theH0MEBREWER&#39;s gravatar image" /><p>theH0MEBREWER<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theH0MEBREWER has no accepted answers">0%</span></p></div></div><div id="comments-container-50179" class="comments-container"><span id="50180"></span><div id="comment-50180" class="comment"><div id="post-50180-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid you'll have to be far more specific as for the desired result. E.g. "I want to get a list of all IP addresses seen in the capture, with the number of sent and received packets for each of them" or something alike. A "listing" may be nearly anything.</p></div><div id="comment-50180-info" class="comment-info"><span class="comment-age">(14 Feb '16, 01:47)</span> sindy</div></div><span id="50186"></span><div id="comment-50186" class="comment"><div id="post-50186-score" class="comment-score"></div><div class="comment-text"><p>I am new to wireshark so i don't really know how to ask what I want to do... this might better explain it. In this video <a href="https://youtu.be/NWsnTLPGrts?t=3m">https://youtu.be/NWsnTLPGrts?t=3m</a> at 4:30 the he says "you can limit it to one ip per listing" but he doesn't explain how to do that. I am trying to figure that out. I also wat to be able to do that as a filter so I can just scroll through the results and not have to export anything. Thanks again.</p></div><div id="comment-50186-info" class="comment-info"><span class="comment-age">(14 Feb '16, 12:31)</span> theH0MEBREWER</div></div></div><div id="comment-tools-50179" class="comment-tools"></div><div class="clear"></div><div id="comment-50179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50183"></span>

<div id="answer-container-50183" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50183-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go have a look in the Statistics menu to get several options of overviews of the captured data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '16, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-50183" class="comments-container"><span id="50187"></span><div id="comment-50187" class="comment"><div id="post-50187-score" class="comment-score"></div><div class="comment-text"><p>This helps but I wanted to know if there is a filter that does that in the Live Capture window.</p></div><div id="comment-50187-info" class="comment-info"><span class="comment-age">(14 Feb '16, 12:34)</span> theH0MEBREWER</div></div><span id="50197"></span><div id="comment-50197" class="comment"><div id="post-50197-score" class="comment-score">1</div><div class="comment-text"><p>If we admit that watching the list of IP addresses grow live has some advantage, then nothing prevents you from doing the following:</p><ul><li><p>apply the display filter <code>ip.src == your.ip.add.ress</code></p></li><li><p>go <code>Statistics -&gt; Conversations</code>, a new window will open</p></li><li><p>tick the <code>Limit to display filter</code> checkbox in that window, and choose the <code>IPv4</code> tab</p></li><li><p>go back to the main window and start the capture</p></li><li><p>go to the Conversations window again and watch the "one row per IP" table grow live.</p></li></ul><p>In this table, you can sort the rows up to one column's values, by clicking the column header.</p><p>I don't know what the guy on the video had in mind, but to the best of my knowledge, there is no way to change the behaviour of the <em>packet list pane</em> so that it would display all packets which have the same value of a given protocol field (like <code>ip.dst</code> in your case) in a single row. As @Jaap has suggested, other tools have to be used for that purpose.</p></div><div id="comment-50197-info" class="comment-info"><span class="comment-age">(15 Feb '16, 00:27)</span> sindy</div></div><span id="50539"></span><div id="comment-50539" class="comment"><div id="post-50539-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy.</p></div><div id="comment-50539-info" class="comment-info"><span class="comment-age">(26 Feb '16, 05:22)</span> theH0MEBREWER</div></div></div><div id="comment-tools-50183" class="comment-tools"></div><div class="clear"></div><div id="comment-50183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

