+++
type = "question"
title = "why wireshark displays TCP payload as telnet?"
description = '''I write an application to dump &quot;0123456789&quot; as payload of TCP to a PCAP file. (based on https://github.com/shadow/shadow/blob/master/src/support/shd-pcap-writer.c). After loading the generated PCAP with wireshark, it shows the payload as telnet data. Question&amp;gt; How to fix the problem so that the p...'''
date = "2017-05-05T12:28:00Z"
lastmod = "2017-05-05T12:45:00Z"
weight = 61256
keywords = [ "pcap" ]
aliases = [ "/questions/61256" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [why wireshark displays TCP payload as telnet?](/questions/61256/why-wireshark-displays-tcp-payload-as-telnet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61256-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I write an application to dump "0123456789" as payload of TCP to a PCAP file. (based on <a href="https://github.com/shadow/shadow/blob/master/src/support/shd-pcap-writer.c).">https://github.com/shadow/shadow/blob/master/src/support/shd-pcap-writer.c).</a></p><p>After loading the generated PCAP with wireshark, it shows the payload as telnet data.</p><p>Question&gt; How to fix the problem so that the payload is shown as Data instead of telnet. Thank you</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_zTPnplv.PNG" alt="alt text" /></p><p>For example, A correctly display payload is as follows:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark-tcp-data.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '17, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/ec5ada4e8208a8fa410847ae421bf229?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="q0987&#39;s gravatar image" /><p>q0987<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="q0987 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '17, 12:29</p></div></div><div id="comments-container-61256" class="comments-container"></div><div id="comment-tools-61256" class="comment-tools"></div><div class="clear"></div><div id="comment-61256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61258"></span>

<div id="answer-container-61258" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61258-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark displays the payload as Telnet because the well-known TCP port for <a href="https://wiki.wireshark.org/Telnet">Telnet</a> is port 23.</p><p>See also <a href="https://tools.ietf.org/html/rfc854">RFC854</a>, IANA's <a href="https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt">Service Name and Transport Protocol Port Number Registry</a>, and Wireshark's <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-telnet.c;h=59a73f4682d8bdc7f694d9d6f22bc54b303ddd20;hb=HEAD#l156">Telnet dissector source code</a>, where it <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-telnet.c;h=59a73f4682d8bdc7f694d9d6f22bc54b303ddd20;hb=HEAD#l2193">registers on that port</a>.</p><p>Basically, don't use port 23.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '17, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></img></div></div><div id="comments-container-61258" class="comments-container"></div><div id="comment-tools-61258" class="comment-tools"></div><div class="clear"></div><div id="comment-61258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61257"></span>

<div id="answer-container-61257" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61257-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your connection is using the TCP port 23. Therefore the data gets dissected as Telnet.</p><p>To work around this, go to 'Analyze' -&gt; 'Enable Protocols' -&gt; search for 'TELNET' and disable it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '17, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-61257" class="comments-container"></div><div id="comment-tools-61257" class="comment-tools"></div><div class="clear"></div><div id="comment-61257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

