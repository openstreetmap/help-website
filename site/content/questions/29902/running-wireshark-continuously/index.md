+++
type = "question"
title = "Running Wireshark continuously"
description = ''' For my project I want Wireshark to directly start saving packets as I start it.  I need packets in plain text file format ( 2. is there automatic exporting possible by doing any setting in wireshark ? ) How above two can be done ..... '''
date = "2014-02-16T01:27:00Z"
lastmod = "2014-02-16T02:26:00Z"
weight = 29902
keywords = [ "save", "export", "plain-text", "wireshark" ]
aliases = [ "/questions/29902" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Running Wireshark continuously](/questions/29902/running-wireshark-continuously)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29902-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><ol><li>For my project I want Wireshark to directly start saving packets as I start it. I need packets in plain text file format ( 2. is there automatic exporting possible by doing any setting in wireshark ? ) How above two can be done .....</li></ol></div><div id="question-tags" class="tags-container tags">save export plain-text wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '14, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/4f2e12b298828a7bdd200478480606da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WIDS&#39;s gravatar image" /><p>WIDS<br />
<span class="score" title="25 reputation points">25</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WIDS has no accepted answers">0%</span></p></div></div><div id="comments-container-29902" class="comments-container"></div><div id="comment-tools-29902" class="comment-tools"></div><div class="clear"></div><div id="comment-29902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29905"></span>

<div id="answer-container-29905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29905-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do that with Wireshark. That's what tshark is made for.</p><blockquote><p>tshark -Vxnr input.pcap</p></blockquote><p>or</p><blockquote><p>tshark -nr input.pcap -T pdml</p></blockquote><p>or even</p><blockquote><p>tshark -nr input.pcap -T fields -e frame.number -e radiotap.channel -e radiotap.radiotap.db_antsignal -e wlan.sa -e wlan.da -e ip.src -e ip.dst -E separator=; -E header=y</p></blockquote><p>List of fields:</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/r/radiotap.html">http://www.wireshark.org/docs/dfref/r/radiotap.html</a><br />
<a href="http://www.wireshark.org/docs/dfref/w/wlan.html">http://www.wireshark.org/docs/dfref/w/wlan.html</a><br />
<a href="http://www.wireshark.org/docs/dfref/">http://www.wireshark.org/docs/dfref/</a></p></blockquote><p>Then parse the output of tshark with whatever language you prefer (in your case probably Java).</p><p><strong>HINT:</strong> If you run tshark/Wireshark continuously, you will eventually get into trouble, as both tools are not designed as long term, real time monitoring tools. For both the memory usage will increase steadily, as both store state information about several things (sessions, etc.), and never release that memory, until the process ends.</p><blockquote><p><a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a><br />
</p></blockquote><p>See also some lengthy discussion on this site, regarding tshark as a long term, real time monitoring solution and the problems that can arise.</p><blockquote><p><a href="http://ask.wireshark.org/questions/25794/tshark-generate-core-dump">http://ask.wireshark.org/questions/25794/tshark-generate-core-dump</a><br />
<a href="http://ask.wireshark.org/questions/26563/smaller-tshark-for-specific-protocol">http://ask.wireshark.org/questions/26563/smaller-tshark-for-specific-protocol</a><br />
<a href="http://ask.wireshark.org/questions/28224/tshark-crashed-without-any-reason-in-output-log">http://ask.wireshark.org/questions/28224/tshark-crashed-without-any-reason-in-output-log</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '14, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '14, 03:12</p></div></div><div id="comments-container-29905" class="comments-container"></div><div id="comment-tools-29905" class="comment-tools"></div><div class="clear"></div><div id="comment-29905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

