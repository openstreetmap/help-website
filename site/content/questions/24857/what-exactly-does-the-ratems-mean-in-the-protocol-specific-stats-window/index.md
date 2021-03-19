+++
type = "question"
title = "What exactly does the rate(ms) mean in the protocol specific stats window"
description = '''I&#x27;ve created a stats_tree for a protocol that has different object types . This was implemented with a plugin dissector. When I open Statistics and choose my protocol a window opens up with the columns Topic/Item, Count, Rate(ms), and Percent. I can make reasonable guesses on this. However, getting ...'''
date = "2013-09-17T10:01:00Z"
lastmod = "2013-09-22T16:50:00Z"
weight = 24857
keywords = [ "statistics", "stats_tree", "plugin" ]
aliases = [ "/questions/24857" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What exactly does the rate(ms) mean in the protocol specific stats window](/questions/24857/what-exactly-does-the-ratems-mean-in-the-protocol-specific-stats-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24857-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've created a stats_tree for a protocol that has different object types . This was implemented with a plugin dissector.</p><p>When I open Statistics and choose my protocol a window opens up with the columns Topic/Item, Count, Rate(ms), and Percent.<br />
I can make reasonable guesses on this. However, getting confirmation on this will probably help someone out later. Plus I'm having a hard understanding the documentation. At least when I use the <a href="http://wiki.wireshark.org/Statistics">wiki</a> or <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChStatXXX.html">the online user manual</a></p><ul><li>Topic/Item Is the item received(specified packet type in calls to things like stats_tree_create_pivot, stats_tree_tick_pivot);</li><li>Count is the number of this item received.</li><li>Percent is the amount of packets of this type that make up the total count.<br />
</li><li>Rate(ms) the rate the packets arrive in ms?</li></ul></div><div id="question-tags" class="tags-container tags">statistics stats_tree plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '13, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p>tlann<br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></br></p></div></div><div id="comments-container-24857" class="comments-container"></div><div id="comment-tools-24857" class="comment-tools"></div><div class="clear"></div><div id="comment-24857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25083"></span>

<div id="answer-container-25083" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25083-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your time column is configured to display "seconds since beginning of capture" and you look at the timestamp (call it <code>T</code>) of the last packet in the capture file, this is the total elapsed time from the first packet to the last. (Note: You can also see this if you look at <code>Statistics -&gt; Summary -&gt; Elapsed</code>; however, that currently only displays second resolution, so it won't be as accurate.)</p><p>The last packet's frame number (call it <code>F</code>) will also indicate the number of packets in the capture file. The average number of packets/sec for this capture file is then just <code>F/T</code>. The stats show Rate(ms), so the first stat will apply to all packets and be <code>F/T/1000</code>. All the other stats will be computed based on the count (call it <code>C</code>) of matching packets for the particular stat, i.e., <code>C/T/1000</code>.</p><p>For example, in one capture file I happened to be looking at, the elapsed time <code>T</code> was 14.891 seconds. During that time the total number of packets captured <code>F</code> was 771; therefore, the average packet rate is 771 packets/14.891 seconds = 51.776 packets/second. Wireshark displays the Rate stats in milliseconds, so for the overall rate, it shows 0.051776 packets/ms. Within the trace, once particular stat count <code>C</code> shows that there were 332 packets having a packet length of 40-79 bytes, so the rate for those packets is 332/14.891/1000 = 0.022295.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '13, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '13, 16:53</p></div></div><div id="comments-container-25083" class="comments-container"><span id="25164"></span><div id="comment-25164" class="comment"><div id="post-25164-score" class="comment-score"></div><div class="comment-text"><p>Thank you for this in depth comment. This would be really good to add to either the wiki or the docs. Especially, the README.stats_tree document.</p></div><div id="comment-25164-info" class="comment-info"><span class="comment-age">(24 Sep '13, 10:23)</span> tlann</div></div></div><div id="comment-tools-25083" class="comment-tools"></div><div class="clear"></div><div id="comment-25083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

