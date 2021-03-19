+++
type = "question"
title = "Using find packet in a combined trace"
description = '''I have a trace that was taken at various endpoints in the network and combined. If I view the trace by Date and Time of Day, packet 1 ends somewhere down in the display as I expect because it&#x27;s not the first packet as viewed by Time. When I then use the edit&amp;gt;find packet (Packet details, string), ...'''
date = "2015-10-09T05:42:00Z"
lastmod = "2015-10-09T08:25:00Z"
weight = 46429
keywords = [ "find" ]
aliases = [ "/questions/46429" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using find packet in a combined trace](/questions/46429/using-find-packet-in-a-combined-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46429-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace that was taken at various endpoints in the network and combined. If I view the trace by Date and Time of Day, packet 1 ends somewhere down in the display as I expect because it's not the first packet as viewed by Time. When I then use the edit&gt;find packet (Packet details, string), and search for a value, the first found packet is Packet 1, and not the time sorted first packet where it also exists.</p><p>It is like the find packet function defaults to sort by packet number.</p><p>Is this a bug?</p><p>Can I change an option or setting so that WS will find the string when sorted by Time?</p><p>This behavior has been noted against : Windows 7 Enterprise / Version 1.8.6 (SVN Rev 48142 from /trunk-1.8) OS X Yosemite / Verions 1.99.9 (v1.99.9-0-g52a4a78)</p></div><div id="question-tags" class="tags-container tags">find</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '15, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/50d7f4d70e0333ffaaca29f735689b9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dumbmick&#39;s gravatar image" /><p>dumbmick<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dumbmick has no accepted answers">0%</span></p></div></div><div id="comments-container-46429" class="comments-container"></div><div id="comment-tools-46429" class="comment-tools"></div><div class="clear"></div><div id="comment-46429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46430"></span>

<div id="answer-container-46430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46430-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried using reordercap to sort the packets into timestamp order? Not sure if it's in your quite old Windows version, but that's an easy upgrade.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '15, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '15, 06:11</p></div></div><div id="comments-container-46430" class="comments-container"><span id="46433"></span><div id="comment-46433" class="comment"><div id="post-46433-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham, Where should the "reordercap" be located?</p></div><div id="comment-46433-info" class="comment-info"><span class="comment-age">(09 Oct '15, 06:38)</span> dumbmick</div></div><span id="46434"></span><div id="comment-46434" class="comment"><div id="post-46434-score" class="comment-score"></div><div class="comment-text"><p>It's a command line tool in the same directory as the Wireshark executable. The documentation for it can be found <a href="https://www.wireshark.org/docs/man-pages/reordercap.html">here</a>.</p></div><div id="comment-46434-info" class="comment-info"><span class="comment-age">(09 Oct '15, 06:49)</span> grahamb ♦</div></div></div><div id="comment-tools-46430" class="comment-tools"></div><div class="clear"></div><div id="comment-46430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46436"></span>

<div id="answer-container-46436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46436-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First, if you really want to merge the trace files, consider using reordercap as suggested by Graham.</p><p>But merged traces are hard to read. Wireshark will think you have retransmissions when you don't. Consider keeping the trace files separate. You can have multiple instances of Wireshark running, so you can have multiple trace files open at the same time in order to compare.</p><p>The Find dialog will find all packets that match your search. Just keep using Find Next (Ctrl-N), but it will find them in order of packet number, not in the order in which they are displayed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '15, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-46436" class="comments-container"></div><div id="comment-tools-46436" class="comment-tools"></div><div class="clear"></div><div id="comment-46436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

