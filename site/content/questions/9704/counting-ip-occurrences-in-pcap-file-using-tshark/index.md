+++
type = "question"
title = "Counting IP occurrences in PCAP file using tshark"
description = '''Hi I&#x27;m looking for TSHARK syntax to count:  how many times IP address is present in the PCAP file as source ip. how many times IP address is present in the PCAP file as destination ip. how many times TCP Port is present in the PCAP file as destination port.  This needs to be OS-independent, so pipes...'''
date = "2012-03-22T12:31:00Z"
lastmod = "2012-03-26T03:35:00Z"
weight = 9704
keywords = [ "filter", "ip", "tshark", "port", "count" ]
aliases = [ "/questions/9704" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Counting IP occurrences in PCAP file using tshark](/questions/9704/counting-ip-occurrences-in-pcap-file-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9704-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm looking for TSHARK syntax to count:</p><ol><li>how many times IP address is present in the PCAP file as source ip.</li><li>how many times IP address is present in the PCAP file as destination ip.</li><li>how many times TCP Port is present in the PCAP file as destination port.</li></ol><p>This needs to be OS-independent, so pipes and OS-specific commands can't be used...</p><p>Thanks a lot for any help</p></div><div id="question-tags" class="tags-container tags">filter ip tshark port count</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '12, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/9459f9b8c4c4c6291729d6ee81cc8a59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aleksandrc&#39;s gravatar image" /><p>Aleksandrc<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aleksandrc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '12, 16:26</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-9704" class="comments-container"></div><div id="comment-tools-9704" class="comment-tools"></div><div class="clear"></div><div id="comment-9704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9759"></span>

<div id="answer-container-9759" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9759-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Simply use I/O stasistics for that:</p><p>c:\tshark -r tracefile.pcap -qz io,stat,0,ip.src==1.2.3.4,ip.dst==1.2.3.4,tcp.dstport==80</p><p><code>=================================================================== IO Statistics Column #0: ip.src==1.2.3.4 Column #1: ip.dst==1.2.3.4 Column #2: tcp.dstport==80                 |   Column #0    |   Column #1    |   Column #2 Time            |frames|  bytes  |frames|  bytes  |frames|  bytes 000.000-            725     52048    663    340474     28      2494 ===================================================================</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '12, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Mar '12, 03:37</p></div></div><div id="comments-container-9759" class="comments-container"></div><div id="comment-tools-9759" class="comment-tools"></div><div class="clear"></div><div id="comment-9759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9709"></span>

<div id="answer-container-9709" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9709-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>How OS independent does it need to be? If you need *nix AND Windows then you'll be struggling as it will need some scripting and the native script environments are wildly different.</p><p>The <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark manual</a> page lists all the options for tshark, you'll probably want to look at the '-T fields' with some '-e' options, e.g. '-T fields -e ip.src' to get a list of the source ip's, '-T fields -e ip.dst' for destination IP's and '-T fields -e tcp.dstport' for the destination port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9709" class="comments-container"></div><div id="comment-tools-9709" class="comment-tools"></div><div class="clear"></div><div id="comment-9709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

