+++
type = "question"
title = "how to split a .pcap file"
description = '''there is a merge option in wireshark, but is there anything like to split a file into 2 parts which can be read using wireshark ?'''
date = "2017-05-12T11:04:00Z"
lastmod = "2017-05-12T14:37:00Z"
weight = 61371
keywords = [ "a", "split", "file", ".pcap" ]
aliases = [ "/questions/61371" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to split a .pcap file](/questions/61371/how-to-split-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61371-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>there is a merge option in wireshark, but is there anything like to split a file into 2 parts which can be read using wireshark ?</p></div><div id="question-tags" class="tags-container tags">a split file .pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '17, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/4debf4d644c7320e639547bd1b13c1b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="w_keyboard&#39;s gravatar image" /><p>w_keyboard<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="w_keyboard has no accepted answers">0%</span></p></div></div><div id="comments-container-61371" class="comments-container"></div><div id="comment-tools-61371" class="comment-tools"></div><div class="clear"></div><div id="comment-61371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61372"></span>

<div id="answer-container-61372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61372-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Editcap might do what you need: <a href="https://www.wireshark.org/docs/man-pages/editcap.html">https://www.wireshark.org/docs/man-pages/editcap.html</a></p><p>Editcap is a program that reads some or all of the captured packets from the infile, optionally converts them in various ways and writes the resulting packets to the capture outfile (or outfiles).</p><p>By default, it reads all packets from the infile and writes them to the outfile in pcap file format.</p><p>An optional list of packet numbers can be specified on the command tail; individual packet numbers separated by whitespace and/or ranges of packet numbers can be specified as start-end, referring to all packets from start to end. By default the selected packets with those numbers will not be written to the capture file. If the -r flag is specified, the whole packet selection is reversed; in that case only the selected packets will be written to the capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '17, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-61372" class="comments-container"></div><div id="comment-tools-61372" class="comment-tools"></div><div class="clear"></div><div id="comment-61372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61376"></span>

<div id="answer-container-61376" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61376-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Aside from the 'editcap' command line utility, the 'File &gt; Export Specified Packets' GUI in Wireshark is pretty flexible, and gives you some options for saving a capture file containing only part of an existing capture file.</p><p>For example, if I wanted to save "half" of the file, I might select the first packet, hit ctrl+m (to mark it), then do the same to the "middle" packet, and export the "first to last marked".</p><p>As another example, I might apply a display filter to show me just one protocol, or just one source/destination IP address, and export "all displayed". Then I could save "everything else" with a "!" added to the front of that filter if I wanted.</p><p>Since the "export specified packets" GUI lets you base it on display filters or markings, there's little you can't do there in terms of carving up a capture file.</p><p>Having said that, 'editcap' is efficient and can cut up files based on timestamps or frame numbers quite nicely. As always it really depends on your particular use case, and what specifically you want to do when you say you want to "split" the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '17, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-61376" class="comments-container"></div><div id="comment-tools-61376" class="comment-tools"></div><div class="clear"></div><div id="comment-61376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

