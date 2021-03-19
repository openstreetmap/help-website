+++
type = "question"
title = "Wireshark vs tcpstat: Packet count differences"
description = '''Hey there, I downloaded some of sample capture files from the wireshark store, and ran a test to see if there is any difference in packet counting between wireshark and tcpstat. And the answer is totally yes! Why is that so? I did the test with this file: http://wiki.wireshark.org/SampleCaptures?act...'''
date = "2014-06-09T00:53:00Z"
lastmod = "2014-06-09T03:37:00Z"
weight = 33566
keywords = [ "tcpstat", "count", "different", "difference", "packetcount" ]
aliases = [ "/questions/33566" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark vs tcpstat: Packet count differences](/questions/33566/wireshark-vs-tcpstat-packet-count-differences)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there, I downloaded some of sample capture files from the wireshark store, and ran a test to see if there is any difference in packet counting between wireshark and tcpstat. And the answer is totally yes! Why is that so? I did the test with this file: <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=pgsql-jdbc.pcap.gz">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=pgsql-jdbc.pcap.gz</a></p><p>The display filter for wireshark I used, is "pgsql" and it gave me 9698 packets. But tcpstat with the same file and display filter "port postgres" gave me 12453 packets. Both of them counted the total packets 18472.</p><p>Why is that so?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">tcpstat count different difference packetcount</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '14, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/07da332d5eb4e9d3e3c205c281a4d003?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abd&#39;s gravatar image" /><p>abd<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abd has no accepted answers">0%</span></p></div></div><div id="comments-container-33566" class="comments-container"></div><div id="comment-tools-33566" class="comment-tools"></div><div class="clear"></div><div id="comment-33566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33567"></span>

<div id="answer-container-33567" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33567-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably because you used "pgsql", which filters on the application protocol, which will leave out all TCP management packets (Three Way Handshake, empty ACK-Packets, Session Teardown). Try filtering on "tcp.port==5432" and you should get the correct number of packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '14, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33567" class="comments-container"><span id="33571"></span><div id="comment-33571" class="comment"><div id="post-33571-score" class="comment-score"></div><div class="comment-text"><p>Soooo ture. Thank you veeery much. Then, according to the way the 2 do(Wireshark and bpf based tools) it, it seems wireshark would be a bit slower in large amounts, right?</p><p>Thanks</p></div><div id="comment-33571-info" class="comment-info"><span class="comment-age">(09 Jun '14, 04:15)</span> abd</div></div><span id="33572"></span><div id="comment-33572" class="comment"><div id="post-33572-score" class="comment-score">1</div><div class="comment-text"><p>I'm pretty sure Wireshark does way more processing on packets than tcpstat does while reading a file, and it keeps more data in memory about what it saw in previous packets. That would make it slower, yes.</p></div><div id="comment-33572-info" class="comment-info"><span class="comment-age">(09 Jun '14, 04:22)</span> Jasper ♦♦</div></div></div><div id="comment-tools-33567" class="comment-tools"></div><div class="clear"></div><div id="comment-33567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

