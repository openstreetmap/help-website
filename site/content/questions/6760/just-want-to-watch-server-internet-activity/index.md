+++
type = "question"
title = "Just want to watch Server Internet Activity"
description = '''Can I easily use Wireshark installed on a Windows SBS 2003 server to capture traffic sent and received from the server (IP 192.168.1.10) to and from the internet. I want to eaily hide the traffic sent to other 192.168.1.x systems since they are internal. Woudl also like to then hide traffic to and f...'''
date = "2011-10-06T13:50:00Z"
lastmod = "2011-10-06T23:46:00Z"
weight = 6760
keywords = [ "filter", "internet", "hide", "server" ]
aliases = [ "/questions/6760" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Just want to watch Server Internet Activity](/questions/6760/just-want-to-watch-server-internet-activity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6760-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I easily use Wireshark installed on a Windows SBS 2003 server to capture traffic sent and received from the server (IP 192.168.1.10) to and from the internet. I want to eaily hide the traffic sent to other 192.168.1.x systems since they are internal.</p><p>Woudl also like to then hide traffic to and from known applications or services on my system, such as logmein, exchange SMTP port 25 packets, etc.</p><p>I am trying to identify what is utilizing too much internet bandwidth and possibly somehting not authorized on my server.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">filter internet hide server</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '11, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/e902d3bf6f2a0cd46603212c9ad9c5c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NeedWiresharkHelp&#39;s gravatar image" /><p>NeedWireshar...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NeedWiresharkHelp has no accepted answers">0%</span></p></div></div><div id="comments-container-6760" class="comments-container"></div><div id="comment-tools-6760" class="comment-tools"></div><div class="clear"></div><div id="comment-6760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6767"></span>

<div id="answer-container-6767" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6767-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to verse yourself in capture filters first. So have a look <a href="http://manpages.ubuntu.com/manpages/natty/man7/pcap-filter.7.html">here</a> and try to work up a capture filter expression to put into the Wireshark capture options dialog. Then check if that's the result you're after.</p><p>Once refined you can take that capture filter and stick it on the dumpcap command line, which allows you longer term capture, if that's what you need. This has been covered in many places already.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '11, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6767" class="comments-container"></div><div id="comment-tools-6767" class="comment-tools"></div><div class="clear"></div><div id="comment-6767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

