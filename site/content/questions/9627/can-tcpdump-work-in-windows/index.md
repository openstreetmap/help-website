+++
type = "question"
title = "can tcpdump work in windows?"
description = '''Does TCPDUMP work in windows?'''
date = "2012-03-20T03:34:00Z"
lastmod = "2012-03-20T08:00:00Z"
weight = 9627
keywords = [ "windows", "tcpdump" ]
aliases = [ "/questions/9627" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [can tcpdump work in windows?](/questions/9627/can-tcpdump-work-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9627-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does TCPDUMP work in windows?</p></div><div id="question-tags" class="tags-container tags">windows tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '12, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/4ffb36ec4ee25beb69f3e0fa8969c8b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alice&#39;s gravatar image" /><p>Alice<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alice has no accepted answers">0%</span></p></div></div><div id="comments-container-9627" class="comments-container"></div><div id="comment-tools-9627" class="comment-tools"></div><div class="clear"></div><div id="comment-9627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9643"></span>

<div id="answer-container-9643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9643-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.tcpdump.org/">Tcpdump</a> on Windows is called <a href="http://www.winpcap.org/windump/">WinDump</a>.</p><p>And apparently there is also at least one commercially available version of tcpdump for Windows. See the <a href="http://www.microolap.com/products/network/tcpdump/">MicroOLAP TCPDUMP for Windows 3.9.8</a> page for more details.</p><p>Wireshark also provides other command-line packet capture tools that you might find useful as well, such as <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a>, as Jasper already mentioned, and <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a>.</p><p>If you're looking for Windows packet capture solutions in general, and not necessarily just command-line sniffer solutions, then you could also try <a href="http://www.microsoft.com/download/en/details.aspx?id=4865">Microsoft Network Monitor</a>, or a number of other <a href="http://wiki.wireshark.org/Tools">tools</a> as well. Finally, you can use Wikipedia's <a href="http://en.wikipedia.org/wiki/Comparison_of_packet_analyzers">Comparison of packet analyzers</a> page to quickly find many analyzers that run on Windows and rather quickly and easily compare them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '12, 16:21</p></div></div><div id="comments-container-9643" class="comments-container"></div><div id="comment-tools-9643" class="comment-tools"></div><div class="clear"></div><div id="comment-9643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9628"></span>

<div id="answer-container-9628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9628-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can just use dumpcap.exe that comes with Wireshark, it basically does the same as tcpdump. You'll find it in the Wireshark installation directory, and <strong>dumpcap -h</strong> will give you a help screen.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9628" class="comments-container"></div><div id="comment-tools-9628" class="comment-tools"></div><div class="clear"></div><div id="comment-9628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

