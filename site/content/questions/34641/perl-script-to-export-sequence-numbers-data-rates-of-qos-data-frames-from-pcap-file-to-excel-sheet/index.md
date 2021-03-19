+++
type = "question"
title = "Perl script to export  Sequence numbers &amp; data rates of QoS Data frames from pcap file to excel sheet?"
description = '''Hi I am new to perl scripting &amp;amp; wireshark usage. Can any one please please help me exporting the sequence numbers &amp;amp; data rates of QoS data frames from a pcap file to excel sheet. Thanks in Advance, Srinivas'''
date = "2014-07-14T22:05:00Z"
lastmod = "2014-07-15T00:50:00Z"
weight = 34641
keywords = [ "pcap", "wireshark", "qos", "excel", "perl" ]
aliases = [ "/questions/34641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Perl script to export Sequence numbers & data rates of QoS Data frames from pcap file to excel sheet?](/questions/34641/perl-script-to-export-sequence-numbers-data-rates-of-qos-data-frames-from-pcap-file-to-excel-sheet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34641-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am new to perl scripting &amp; wireshark usage. Can any one please please help me <strong>exporting the sequence numbers &amp; data rates of QoS data frames from a pcap file to excel sheet</strong>.</p><p>Thanks in Advance, Srinivas</p></div><div id="question-tags" class="tags-container tags">pcap wireshark qos excel perl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '14, 22:05</strong></p><img src="https://secure.gravatar.com/avatar/18a85e15deb17ed6b21762162680ba76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinivas&#39;s gravatar image" /><p>srinivas<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinivas has no accepted answers">0%</span></p></div></div><div id="comments-container-34641" class="comments-container"></div><div id="comment-tools-34641" class="comment-tools"></div><div class="clear"></div><div id="comment-34641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34644"></span>

<div id="answer-container-34644" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34644-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p>tshark -nr input.pcap -T fields -e frame.number -e ip.src -e ip.dst -e tcp.seq -E header=yes -E separator=; &gt; output.csv</p></blockquote><p>Furthermore, you need a display filter for 'QoS' frames. As you did not specify what kind of QoS frames you are talking, I can only tell you how it works in general.</p><blockquote><p>tshark -nr input.pcap -Y 'tcp.port eq 80' -T fields -e frame.number -e ip.src -e ip.dst -e tcp.seq -E header=yes -E separator=; &gt; output.csv</p></blockquote><p>Please replace <strong>tcp.port eq 80</strong> with your filter for 'QoS' traffic.</p><p>BTW: Please also define what you mean by: 'data rates' of QoS data frames.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 00:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34644" class="comments-container"></div><div id="comment-tools-34644" class="comment-tools"></div><div class="clear"></div><div id="comment-34644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

