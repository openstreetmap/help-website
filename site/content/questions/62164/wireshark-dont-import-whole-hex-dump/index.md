+++
type = "question"
title = "Wireshark don&#x27;t import whole hex dump"
description = '''I captured some traffic and made a hex dump file out of this. This one here: Just two Beacon Frames. But if i import them (File &amp;gt; Import Hexdump &amp;gt; IEEE 802.11 Wireless LAN) it just show one Beacon Frame instead of two: ![alt text][1] Do i something wrong?'''
date = "2017-06-20T05:16:00Z"
lastmod = "2017-06-20T05:50:00Z"
weight = 62164
keywords = [ "import", "hexdump" ]
aliases = [ "/questions/62164" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark don't import whole hex dump](/questions/62164/wireshark-dont-import-whole-hex-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62164-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured some traffic and made a hex dump file out of this. This one here:</p><p>Just two Beacon Frames. But if i import them (File &gt; Import Hexdump &gt; IEEE 802.11 Wireless LAN) it just show one Beacon Frame instead of two:</p><p>![alt text][1]</p><p>Do i something wrong?</p></div><div id="question-tags" class="tags-container tags">import hexdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '17, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/99aa7bab1317487e17831ff692a6cf19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whateverever&#39;s gravatar image" /><p>whateverever<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whateverever has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '17, 08:19</p></div></div><div id="comments-container-62164" class="comments-container"></div><div id="comment-tools-62164" class="comment-tools"></div><div class="clear"></div><div id="comment-62164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62167"></span>

<div id="answer-container-62167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62167-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The byte offsets are continuous.</p><pre><code>....
000108 00 00
000110 80 00 00 00 FF FF FF FF
....</code></pre><p>They should reset between the two:</p><pre><code>....
000108 00 00
000000 80 00 00 00 FF FF FF FF
....</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '17, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62167" class="comments-container"></div><div id="comment-tools-62167" class="comment-tools"></div><div class="clear"></div><div id="comment-62167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

