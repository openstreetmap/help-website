+++
type = "question"
title = "Is there any way to filter or capture packet using display filter in C language?"
description = '''Winpcap(https://www.winpcap.org/) provides lots of functions, such as pcap_setfilter/pcap_compile...,so we can write a software using C language, which can capture packets from interface card or filter packet from files using capture filter. But some times I want to capture or filter using display f...'''
date = "2016-11-12T00:15:00Z"
lastmod = "2016-11-12T03:05:00Z"
weight = 57331
keywords = [ "winpcap", "tshark", "wireshark" ]
aliases = [ "/questions/57331" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any way to filter or capture packet using display filter in C language?](/questions/57331/is-there-any-way-to-filter-or-capture-packet-using-display-filter-in-c-language)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57331-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Winpcap(<a href="https://www.winpcap.org/)">https://www.winpcap.org/)</a> provides lots of functions, such as pcap_setfilter/pcap_compile...,so we can write a software using C language, which can capture packets from interface card or filter packet from files using capture filter.</p><p>But some times I want to capture or filter using display filter in my software. How can I do this? Does wireshark provides C language functions similar to pcap_setfilter/pcap_compile/pcap_open...?</p><p>Thanks a lot</p><p>If analyse few files manualy, tshark is ok. But I want to analyse a lot of files automaticlly</p><p>For example, if I want to filter thousands of files, how can I count the matched packets number in each file? how can I write matched packets to one file or few files?</p><p>Can tshark command line help me to do? Thank you</p></div><div id="question-tags" class="tags-container tags">winpcap tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '16, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/069467bd1edc7bb03aa0fb74d7e673af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="w44524&#39;s gravatar image" /><p>w44524<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="w44524 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Nov '16, 21:50</p></div></div><div id="comments-container-57331" class="comments-container"></div><div id="comment-tools-57331" class="comment-tools"></div><div class="clear"></div><div id="comment-57331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57334"></span>

<div id="answer-container-57334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57334-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Display filtering is done by the Wireshark engine in libwireshark but this is NOT built to be used as an external library by other applications, although a few have managed to do so.</p><p>You might be better off using the command line application tshark to filter for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '16, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57334" class="comments-container"><span id="57373"></span><div id="comment-57373" class="comment"><div id="post-57373-score" class="comment-score"></div><div class="comment-text"><p>Following up your supplemental question, you'll need to supply a display filter in the call to tshark and then parse the output.</p><p>There is a <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> that list all the tshark options, you might be interested in the <code>-z &lt;statistics&gt;</code> part.</p></div><div id="comment-57373-info" class="comment-info"><span class="comment-age">(14 Nov '16, 02:25)</span> grahamb ♦</div></div></div><div id="comment-tools-57334" class="comment-tools"></div><div class="clear"></div><div id="comment-57334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

