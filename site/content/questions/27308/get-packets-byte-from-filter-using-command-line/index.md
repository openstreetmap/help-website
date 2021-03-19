+++
type = "question"
title = "Get packets byte from filter using command line"
description = '''I looking for command that after search for specific filter for example: tcp.port==80 the output will be the packet in byte. until now i am using this command : tshark.exe -Y tcp.port==80 -n -r file.pcap and the output is only the packet details: packet number 28.853596 192.0.16.37 -&amp;gt; 66.196.114....'''
date = "2013-11-24T04:13:00Z"
lastmod = "2013-11-24T11:47:00Z"
weight = 27308
keywords = [ "tshark" ]
aliases = [ "/questions/27308" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get packets byte from filter using command line](/questions/27308/get-packets-byte-from-filter-using-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27308-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I looking for command that after search for specific filter for example: <code>tcp.port==80</code> the output will be the packet in byte.</p><p>until now i am using this command : <code>tshark.exe -Y tcp.port==80 -n -r file.pcap</code> and the output is only the packet details:</p><pre><code>packet number  28.853596  192.0.16.37 -&gt; 66.196.114.114 TCP 66 50580 &gt; 5050 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1</code></pre></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '13, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/af2a4a3dfd1933fb52e65e2cfd4efc69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="falukky&#39;s gravatar image" /><p>falukky<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="falukky has no accepted answers">0%</span></p></div></div><div id="comments-container-27308" class="comments-container"></div><div id="comment-tools-27308" class="comment-tools"></div><div class="clear"></div><div id="comment-27308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27320"></span>

<div id="answer-container-27320" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27320-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe the <code>-x</code> option is what you're looking for? Did you try:</p><pre><code>tshark.exe -Y tcp.port==80 -n -r file.pcap -x</code></pre><p>For more information on <code>tshark</code> usage, refer to the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '13, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27320" class="comments-container"></div><div id="comment-tools-27320" class="comment-tools"></div><div class="clear"></div><div id="comment-27320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

