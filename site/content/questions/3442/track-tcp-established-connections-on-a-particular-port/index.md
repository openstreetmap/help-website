+++
type = "question"
title = "track tcp established connections on  a particular port"
description = '''Is there a tool out there that can show me the # of established connections, per second, on a specific port? We have an application that listens on a custom port that was developed by a 3rd party. there&#x27;s no internal tools provided by them that tracks the # of established socketed connections to a s...'''
date = "2011-04-11T09:05:00Z"
lastmod = "2011-04-11T14:19:00Z"
weight = 3442
keywords = [ "count", "established", "connections", "socket", "tcp" ]
aliases = [ "/questions/3442" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [track tcp established connections on a particular port](/questions/3442/track-tcp-established-connections-on-a-particular-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3442-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a tool out there that can show me the # of established connections, per second, on a specific port?</p><p>We have an application that listens on a custom port that was developed by a 3rd party. there's no internal tools provided by them that tracks the # of established socketed connections to a specific port. THey're using a Java SocketServer Class library, but i don't know much more than that.</p><p>we were using netstat -an to try and get some data about this, but as you know, it doesnt' really count established connections, and i can't find a way to limit to just one port.</p><p>i also saw that MS PERFMON has a TCP counter that's "established connections" but that's not per port (server only).</p><p>what i'm trying to do is some testing to trend the # of established connections to a particular port for a 2 minute interval.</p><p>any advice would be great.</p></div><div id="question-tags" class="tags-container tags">count established connections socket tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '11, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/2ce55a604bc27b5e99159944c96d9046?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bubbawny69&#39;s gravatar image" /><p>bubbawny69<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bubbawny69 has no accepted answers">0%</span></p></div></div><div id="comments-container-3442" class="comments-container"></div><div id="comment-tools-3442" class="comment-tools"></div><div class="clear"></div><div id="comment-3442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3446"></span>

<div id="answer-container-3446" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3446-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use wireshark's IO graph. The final ACK of the 3-way-handhsake has tcp.len=0 and SEQ=1 and ACK=1 (when using relative sequence numbers). So you can create an IO graph based on that filter.</p><ol><li>Select "Advanced" at the "unit" dropdown.</li><li>Use the filter "tcp.len==0 and tcp.seq==1 and tcp.ack==1", calc: "COUNT(*)" and fill in "tcp.seq" to count.</li><li>Click on "Graph 1".</li></ol><p>You might want to change the tick frequency and/or pixels per tick to get a nicely formatted graph.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '11, 14:17</p></div></div><div id="comments-container-3446" class="comments-container"></div><div id="comment-tools-3446" class="comment-tools"></div><div class="clear"></div><div id="comment-3446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3455"></span>

<div id="answer-container-3455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3455-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might also want to look at the answer given to <a href="http://ask.wireshark.org/questions/2877/report-on-number-of-sockets-established">your other question</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3455" class="comments-container"></div><div id="comment-tools-3455" class="comment-tools"></div><div class="clear"></div><div id="comment-3455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

