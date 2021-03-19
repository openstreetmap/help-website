+++
type = "question"
title = "Need help Trace 2 nic together"
description = '''Hi Guys, I&#x27;m new in wireshark. Lets say I want to trace packet from two nic together? What is the right command.. If I want to trace from 1 nic below is the command..but if i want to trace from 2 nic? dumpcap -i NIC Thank you in advance'''
date = "2015-11-09T23:55:00Z"
lastmod = "2015-11-10T00:19:00Z"
weight = 47452
keywords = [ "dumpcap" ]
aliases = [ "/questions/47452" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Need help Trace 2 nic together](/questions/47452/need-help-trace-2-nic-together)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47452-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I'm new in wireshark. Lets say I want to trace packet from two nic together? What is the right command..</p><p>If I want to trace from 1 nic below is the command..but if i want to trace from 2 nic?</p><p>dumpcap -i NIC</p><p>Thank you in advance</p></div><div id="question-tags" class="tags-container tags">dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '15, 23:55</strong></p><img src="https://secure.gravatar.com/avatar/2f3cd2b779b89ba8ff42855ead5745c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wunan&#39;s gravatar image" /><p>wunan<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wunan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Nov '15, 23:56</p></div></div><div id="comments-container-47452" class="comments-container"></div><div id="comment-tools-47452" class="comment-tools"></div><div class="clear"></div><div id="comment-47452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47453"></span>

<div id="answer-container-47453" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47453-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>from <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html:">https://www.wireshark.org/docs/man-pages/dumpcap.html:</a></p><p>-i &lt; capture interface &gt;|rpcap://&lt; host &gt;/&lt; capture interface &gt;|[email protected]&lt; host &gt;:&lt; port &gt;|-</p><p>...</p><p><strong>This option can occur multiple times. When capturing from multiple interfaces, the capture file will be saved in pcap-ng format.</strong></p><p>so simply</p><p><strong>dumpcap -i nic1 -i nic2</strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-47453" class="comments-container"><span id="47458"></span><div id="comment-47458" class="comment"><div id="post-47458-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much =D</p></div><div id="comment-47458-info" class="comment-info"><span class="comment-age">(10 Nov '15, 00:33)</span> wunan</div></div></div><div id="comment-tools-47453" class="comment-tools"></div><div class="clear"></div><div id="comment-47453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

