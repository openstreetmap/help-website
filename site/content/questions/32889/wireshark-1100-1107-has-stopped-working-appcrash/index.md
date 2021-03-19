+++
type = "question"
title = "Wireshark 1.10.0 &amp; 1.10.7 has stopped working: APPCrash"
description = '''I&#x27;m running Wireshark win64 1.10.7 on a Windows 2008 server R2 Enterprise SP1. From time to time - randomly the Wireshark program stops working. Sometime first a pop-up is shown first:  Then the following pop-up is shown:  Detailed info: Problem signature:  Problem Event Name: APPCRASH  Application ...'''
date = "2014-05-19T06:05:00Z"
lastmod = "2014-05-19T06:07:00Z"
weight = 32889
keywords = [ "stopped", "runtime", "crash", "1.10.7" ]
aliases = [ "/questions/32889" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 1.10.0 & 1.10.7 has stopped working: APPCrash](/questions/32889/wireshark-1100-1107-has-stopped-working-appcrash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32889-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Wireshark win64 1.10.7 on a Windows 2008 server R2 Enterprise SP1. From time to time - randomly the Wireshark program stops working. Sometime first a pop-up is shown first: <img src="https://osqa-ask.wireshark.org/upfiles/Runtime.png" alt="alt text" /></p><p>Then the following pop-up is shown: <img src="https://osqa-ask.wireshark.org/upfiles/WS-stopped.png" alt="alt text" /></p><p>Detailed info: Problem signature: Problem Event Name: APPCRASH Application Name: Wireshark.exe Application Version: 1.10.7.0 Application Timestamp: 53569d96 Fault Module Name: libglib-2.0-0.dll Fault Module Version: 2.34.1.0 Fault Module Timestamp: 508d9e80 Exception Code: 40000015 Exception Offset: 00000000000509c2 OS Version: 6.1.7601.2.1.0.274.10 Locale ID: 2067 Additional Information 1: 26cb Additional Information 2: 26cb520882fc9cea3b5c8c04fa568662 Additional Information 3: 4e5b Additional Information 4: 4e5bdfca931be366a570b86a034f3954</p><p>The same problem occurred also in v1.10.0 but the upgrade did not solve the problem.</p></div><div id="question-tags" class="tags-container tags">stopped runtime crash 1.10.7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '14, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/2c6e52dcc3854f1ab3947f2651fa3afb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beesman59&#39;s gravatar image" /><p>Beesman59<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beesman59 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-32889" class="comments-container"></div><div id="comment-tools-32889" class="comment-tools"></div><div class="clear"></div><div id="comment-32889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32890"></span>

<div id="answer-container-32890" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32890-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at this: <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '14, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-32890" class="comments-container"><span id="32896"></span><div id="comment-32896" class="comment"><div id="post-32896-score" class="comment-score"></div><div class="comment-text"><p>If it's a bug you need to try to narrow it down. Does it happen durig live capturing? Does it happen when you have captured a lot of traffic(big file) then it might be the out-of-memory problem. If it happens during live captures the capture file might still be in the tmp dir and you can try to load that into wireshark and see if the crash is reproducible. If it is you can try to edit the file to narrow the problem down to fewer packets and open a bug report and attach the capture file to that bug report if it does not contain private data.</p></div><div id="comment-32896-info" class="comment-info"><span class="comment-age">(19 May '14, 07:07)</span> Anders ♦</div></div><span id="32898"></span><div id="comment-32898" class="comment"><div id="post-32898-score" class="comment-score"></div><div class="comment-text"><p>Oh BTW the recent automated builds contain a GTK fix to a memory leak problem. You could try that to see if it fixes the problem.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9914">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9914</a></p></div><div id="comment-32898-info" class="comment-info"><span class="comment-age">(19 May '14, 07:09)</span> Anders ♦</div></div></div><div id="comment-tools-32890" class="comment-tools"></div><div class="clear"></div><div id="comment-32890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

