+++
type = "question"
title = "speed of sending and receiving packets"
description = '''hello would you plz guide me if i want to use Wireshark to measure the seep of my requests to the other client on my wired network? the LAN is 100Mbps but i think it is less than this, how can i be sure the speed of my request, spouse i want to ask to calling a method of my Web application uploaded ...'''
date = "2010-12-04T01:26:00Z"
lastmod = "2010-12-04T14:12:00Z"
weight = 1242
keywords = [ "speed" ]
aliases = [ "/questions/1242" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [speed of sending and receiving packets](/questions/1242/speed-of-sending-and-receiving-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1242-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello</p><p>would you plz guide me if i want to use Wireshark to measure the seep of my requests to the other client on my wired network? the LAN is 100Mbps but i think it is less than this, how can i be sure the speed of my request, spouse i want to ask to calling a method of my Web application uploaded on my server which is in my wired LAN, now if i want to check how lung does it take from the time when i send my request until my server receive my request (network time)?</p><p>thank u</p></div><div id="question-tags" class="tags-container tags">speed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '10, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/54bdf8e6def85067af58596e7d7c0b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SAP&#39;s gravatar image" /><p>SAP<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SAP has no accepted answers">0%</span></p></div></div><div id="comments-container-1242" class="comments-container"></div><div id="comment-tools-1242" class="comment-tools"></div><div class="clear"></div><div id="comment-1242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1246"></span>

<div id="answer-container-1246" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1246-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to measure how fast a single TCP connection performed you can isolate it by using the popup menu on one of the packets belonging to the connection and select "Conversation Filter" -&gt; "TCP" (or do the one trick everybody learns the first time they run Wireshark: PopupMenu -&gt; "Follow TCP Stream").</p><p>Next, go to the Statistics menu and select "Summary". Your connection throughput will be listed in the "Displayed" column. If you want to stress test you network you might consider running a test with a traffic generator like <strong>netio</strong> and look at the results for that test.</p><p>Webapplications on the other hand very often do not consist of a single TCP connection (unless using HTTP/1.1 with connection keep alive), so you might not be happy by tracking down single communication flows. If you're more interested in how long a web page takes to load you might want to take a look at HTTP proxy tools like "Fiddler" or Firefox plugins like "Firebug" that can show you exactly which part took how long to load and in which order:</p><p><img src="http://www.synerity.com/images/firebug.png" title="Firebug plugin" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '10, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '10, 14:13</p></div></div><div id="comments-container-1246" class="comments-container"></div><div id="comment-tools-1246" class="comment-tools"></div><div class="clear"></div><div id="comment-1246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

