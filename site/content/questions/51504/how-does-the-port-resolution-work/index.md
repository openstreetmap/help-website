+++
type = "question"
title = "How does the port resolution work"
description = '''The section on port name resolution states that  Wireshark will ask the operating system to convert a TCP or UDP port to its well known name (e.g. 80 → http).  This is from the output of tshark -nr file.pcap 5 0.027049000 1.2.3.4 -&amp;gt; 5.6.7.8 TCP 66 33214 &amp;gt; 7777 [ACK] Seq=1 Ack=1 Win=251 Len=0 T...'''
date = "2016-04-08T05:08:00Z"
lastmod = "2016-04-08T05:26:00Z"
weight = 51504
keywords = [ "resolution", "port" ]
aliases = [ "/questions/51504" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How does the port resolution work](/questions/51504/how-does-the-port-resolution-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51504-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAdvNameResolutionSection.html#_tcp_udp_port_name_resolution_transport_layer">The section on port name resolution</a> states that</p><blockquote><p>Wireshark will ask the operating system to convert a TCP or UDP port to its well known name (e.g. 80 → http).</p></blockquote><p>This is from the output of <code>tshark -nr file.pcap</code></p><p>5 0.027049000 1.2.3.4 -&gt; 5.6.7.8 TCP 66 33214 &gt; 7777 [ACK] Seq=1 Ack=1 Win=251 Len=0 TSval=1736678907 TSecr=332227645</p><p>This from <code>tshark -r file.pcap</code></p><p>5 0.027049000 1.2.3.4 -&gt; 5.6.7.8 TCP 66 33214 &gt; cbt [ACK] Seq=1 Ack=1 Win=251 Len=0 TSval=1736678907 TSecr=332227645</p><p>Port 7777 got mapped to the "cbt" protocol (in tshark). Neither the port nor the string "cbt" appear in <code>/etc/services</code>, so it seems there is some other source.</p><p>Could someone explain this?</p></div><div id="question-tags" class="tags-container tags">resolution port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '16, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/0f479a594deab60e820a84e87409f955?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user1234&#39;s gravatar image" /><p>user1234<br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user1234 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Apr '16, 05:16</p></div></div><div id="comments-container-51504" class="comments-container"></div><div id="comment-tools-51504" class="comment-tools"></div><div class="clear"></div><div id="comment-51504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51505"></span>

<div id="answer-container-51505" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51505-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has its own copy of <code>services</code>, not sure where it ends up on systems other than Windows where it's placed alongside the binaries. The copy is generated from IANA's <a href="http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv">list</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '16, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51505" class="comments-container"><span id="51506"></span><div id="comment-51506" class="comment"><div id="post-51506-score" class="comment-score">1</div><div class="comment-text"><p>Should be in the users home directory; the About dialog has a tab that tells where it is exactly.</p></div><div id="comment-51506-info" class="comment-info"><span class="comment-age">(08 Apr '16, 05:28)</span> Jasper ♦♦</div></div><span id="51507"></span><div id="comment-51507" class="comment"><div id="post-51507-score" class="comment-score"></div><div class="comment-text"><p>Thank you. In debian-based systems, it's at <code>/usr/share/wireshark/services</code>. It was installed via the <code>libwireshark-data</code> package.</p></div><div id="comment-51507-info" class="comment-info"><span class="comment-age">(08 Apr '16, 05:51)</span> user1234</div></div></div><div id="comment-tools-51505" class="comment-tools"></div><div class="clear"></div><div id="comment-51505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

