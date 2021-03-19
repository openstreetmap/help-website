+++
type = "question"
title = "How to slice 3G trace for just &quot;tcp.port == 1234 || udp.port == 1234&quot;"
description = '''Title says it all. I have a few 2-3G traces of a bunch of nonsense from the past 6 months and the only packets I&#x27;m looking for would match the display filter: (tcp.port==1234) || (udp.port==1234) Is there anyone I can slice the traces for just these packets? Using free tools of course :D'''
date = "2014-06-23T14:09:00Z"
lastmod = "2014-06-23T20:54:00Z"
weight = 34095
keywords = [ "slicing", "me", "help", "big_trace_file" ]
aliases = [ "/questions/34095" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to slice 3G trace for just "tcp.port == 1234 || udp.port == 1234"](/questions/34095/how-to-slice-3g-trace-for-just-tcpport-1234-udpport-1234)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34095-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Title says it all. I have a few 2-3G traces of a bunch of nonsense from the past 6 months and the only packets I'm looking for would match the display filter: (tcp.port==1234) || (udp.port==1234)</p><p>Is there anyone I can slice the traces for just these packets? Using free tools of course :D</p></div><div id="question-tags" class="tags-container tags">slicing me help big_trace_file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '14, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/8988cfa4b1abc8a6990290d638bb7d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zasher&#39;s gravatar image" /><p>zasher<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zasher has no accepted answers">0%</span></p></div></div><div id="comments-container-34095" class="comments-container"><span id="34097"></span><div id="comment-34097" class="comment"><div id="post-34097-score" class="comment-score"></div><div class="comment-text"><p>What exactly do you mean by "slice"? Cut the payload at a specific offset/after a specific layer?</p></div><div id="comment-34097-info" class="comment-info"><span class="comment-age">(23 Jun '14, 15:26)</span> Jasper ♦♦</div></div></div><div id="comment-tools-34095" class="comment-tools"></div><div class="clear"></div><div id="comment-34095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34105"></span>

<div id="answer-container-34105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34105-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a few ways to interpret your question.</p><p>If you mean "How do I create a trace file with just the packets that match that port number?", the answer would be something like this in tshark (for Windows, go to your Wireshark install directory and use tshark.exe):</p><pre><code>tshark -r {2G_File.pcap} -R &quot;(tcp.port==1234)||(udp.port==1234)&quot; -w {FilteredFile.pcap}</code></pre><p>If you mean "How do I read through the noise, as these files are too big to load in Wireshark or Tshark?", the answer (or mine, at least), would be to cut them down to fixed file size or packet count with the "editcap" utility, use the above command to pass them through a filter into 1234-only files, then merge those filtered files with the 'mergecap' utility.</p><p>So, between editcap, mergecap and tshark you should be able to work with the files to get those packets out without blowing up your memory by loading a 3G trace into Wireshark. Consult the man pages or manual for more information on all those:</p><p>Tshark: <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html">http://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html</a></p><p>Editcap: <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolseditcap.html">http://www.wireshark.org/docs/wsug_html_chunked/AppToolseditcap.html</a></p><p>Mergecap: <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolsmergecap.html">http://www.wireshark.org/docs/wsug_html_chunked/AppToolsmergecap.html</a></p><p>The manual index: <a href="http://www.wireshark.org/docs/wsug_html_chunked/">http://www.wireshark.org/docs/wsug_html_chunked/</a></p><p>And finally if you mean "How do I automate a process of reading every one of those files and pulling out just these packets?", I suggest a perl script with a simple FOR loop on all those files, calling that Tshark query to read/filter/write, where you could remove the write option and just have it print to screen and leave it as a long-running script sorting through the files. Just keep in mind that would be memory intensive with tshark unless you cut the files down to size first. Also, I'd suggest "-t ad" to get the full date and time if you go with the text output method, so you can reference the exact capture file later (assuming it's timestamped) if needed.</p><p>Of my shots in the dark, I hope the answer was somewhere there. :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '14, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '14, 21:01</p></div></div><div id="comments-container-34105" class="comments-container"></div><div id="comment-tools-34105" class="comment-tools"></div><div class="clear"></div><div id="comment-34105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

