+++
type = "question"
title = "Parsing a binary data packets file"
description = '''I have a file that contains the binary data of the packets (that came from my network interface), without any pcap header or any packet header. The file has no delimiter between each packet. Is there a way to parse this file and convert it to be readable by wireshark&#92;tshark&#92;tcpdump? Thanks!'''
date = "2016-11-17T01:09:00Z"
lastmod = "2016-11-17T02:10:00Z"
weight = 57433
keywords = [ "binary", "pcap", "tshark" ]
aliases = [ "/questions/57433" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Parsing a binary data packets file](/questions/57433/parsing-a-binary-data-packets-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57433-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a file that contains the binary data of the packets (that came from my network interface), without any pcap header or any packet header. The file has no delimiter between each packet. Is there a way to parse this file and convert it to be readable by wireshark\tshark\tcpdump?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">binary pcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '16, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/c6d8583de5b7ab80649a3713e380714a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wires-hark&#39;s gravatar image" /><p>wires-hark<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wires-hark has no accepted answers">0%</span></p></div></div><div id="comments-container-57433" class="comments-container"><span id="57434"></span><div id="comment-57434" class="comment"><div id="post-57434-score" class="comment-score"></div><div class="comment-text"><p>When you say there is no packet header, do you mean that there is nothing but the raw frame as it came from the network (starting from the six bytes of the destination MAC address) or that even the Ethernet, IP, (TCP) headers are missing and you only have the payload?</p></div><div id="comment-57434-info" class="comment-info"><span class="comment-age">(17 Nov '16, 01:26)</span> sindy</div></div><span id="57435"></span><div id="comment-57435" class="comment"><div id="post-57435-score" class="comment-score"></div><div class="comment-text"><p>can you put the file somewhere to take a look at?</p></div><div id="comment-57435-info" class="comment-info"><span class="comment-age">(17 Nov '16, 01:29)</span> Jasper ♦♦</div></div><span id="57436"></span><div id="comment-57436" class="comment"><div id="post-57436-score" class="comment-score"></div><div class="comment-text"><p>Yes, I have only the raw frames</p></div><div id="comment-57436-info" class="comment-info"><span class="comment-age">(17 Nov '16, 01:50)</span> wires-hark</div></div><span id="57438"></span><div id="comment-57438" class="comment"><div id="post-57438-score" class="comment-score"></div><div class="comment-text"><p>If there are just raw frames, and all of them contain IP packets, you should be able to recognize frame boundaries by looking for the MAC address and IP address of the interface (which you should know) and one of two Ethertype values. So you would look for the following patterns in the data (<code>mm:mm:mm:mm:mm:mm</code> is your interface's MAC address, <code>ii:ii:ii:ii</code> is your interface's IPv4 address, and bb:bb:bb:bb is your interface subnet's broadcast address):</p><p>(any six bytes):mm:mm:mm:mm:mm:mm:08:00:(any 12 bytes):ii:ii:ii:ii</p><p>this is the beginning of an IPv4 packet sent <strong>by</strong> your interface,</p><p>mm:mm:mm:mm:mm:mm:(any six bytes):08:00:(any 16 bytes):ii:ii:ii:ii</p><p>this is the beginning of an IPv4 packet sent <strong>to</strong> the individual address of your interface,</p><pre><code>ff:ff:ff:ff:ff:ff:(any six bytes):08:00:(any 16 bytes):bb:bb:bb:bb</code></pre><p>this is the beginning of an IPv4 packet sent <strong>to</strong> a broadcast address of your interface,</p><pre><code>ff:ff:ff:ff:ff:ff:(any six bytes):08:06:(any 24 bytes):ii:ii:ii:ii</code></pre><p>or</p><pre><code>mm:mm:mm:mm:m:mm:(any six bytes):08:06:(any 24 bytes):ii:ii:ii:ii</code></pre><p>these are ARP request sent to your interface,</p><pre><code>(any six bytes):mm:mm:mm:mm:mm:mm:08:06(any 14 bytes):ii:ii:ii:ii</code></pre><p>this is an ARP request sent by your interface,</p><p>etc.</p><p>The longer patterns you are able to check, the higher the chance that you can determine the frame beginnings properly.</p><p>It may not be simple to provide a full list of expressions if you use multicast, if there are some other protocols than IPv4 and ARP for IPv4, ..., so it may be quite an iterative process.</p><p>The easiest way to get the result into Wireshark is to print each frame as a line beginning with a <code>0000</code> followed by space-separated hexadecimal values of the frame bytes. A space must follow the last byte, and I think the lines should be separated from each other by an empty one.</p><p>A hex dump file formatted like this can be imported using the <code>File -&gt; Import from Hex Dump...</code> function of Wireshark, choosing "no dummy header" and "Encapsulation type: Ethernet".</p></div><div id="comment-57438-info" class="comment-info"><span class="comment-age">(17 Nov '16, 02:09)</span> sindy</div></div></div><div id="comment-tools-57433" class="comment-tools"></div><div class="clear"></div><div id="comment-57433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57439"></span>

<div id="answer-container-57439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57439-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has the ability to read hex dumps which is described at <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html">https://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html</a>. If you create a script that converts your binary data into a hex dump that looks like this:</p><pre><code>000000 00 e0 1e a7 05 6f 00 10 ........
000008 5a a0 b9 12 08 00 46 00 ........
000010 03 68 00 00 00 00 0a 2e ........
000018 ee 33 0f 19 08 7f 0f 19 ........
000020 03 80 94 04 00 00 10 01 ........
000028 16 a2 0a 00 03 50 00 0c ........
000030 01 01 0f 19 03 80 11 01 ........

000000 00 e0 1e a7 05 6f 00 10 ........
000008 5a a0 b9 12 08 00 46 00 ........
000010 03 68 00 00 00 00 0a 2e ........
000018 ee 33 0f 19 08 7f 0f 19 ........
000020 03 80 94 04 00 00 10 01 ........
000028 16 a2 0a 00 03 50 00 0c ........
000030 01 01 0f 19 03 80 11 01 ........</code></pre><p>Then you can import it by using "File -&gt; Import from hexdump..."</p><p>Whether or not it is doable to convert your binary data into the hexdump depends mostly on the complexity of the network traffic and your scripting skills.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '16, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57439" class="comments-container"><span id="57440"></span><div id="comment-57440" class="comment"><div id="post-57440-score" class="comment-score"></div><div class="comment-text"><p>There's no need to add the "ASCII" ........ part.</p></div><div id="comment-57440-info" class="comment-info"><span class="comment-age">(17 Nov '16, 03:03)</span> grahamb ♦</div></div></div><div id="comment-tools-57439" class="comment-tools"></div><div class="clear"></div><div id="comment-57439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

