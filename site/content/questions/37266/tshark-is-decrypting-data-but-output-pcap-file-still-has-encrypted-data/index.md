+++
type = "question"
title = "tshark is decrypting data but output pcap file still has encrypted data"
description = '''I want to have pcap file with decrypted SSL data in it. I am running tshark like this-  tshark -o &quot;ssl.desegment_ssl_records: TRUE&quot; -o &quot;ssl.desegment_ssl_application_data: TRUE&quot; -o &quot;ssl.keys_list:192.168.56.101,443,http,/etc/nginx/cert.key&quot; -o &quot;ssl.debug_file:/tmp/ssl.log&quot; tcp port 443 -w /tmp/ssl.p...'''
date = "2014-10-22T03:03:00Z"
lastmod = "2014-10-22T05:11:00Z"
weight = 37266
keywords = [ "ssl", "pcap", "tshark", "ssl_decrypt" ]
aliases = [ "/questions/37266" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [tshark is decrypting data but output pcap file still has encrypted data](/questions/37266/tshark-is-decrypting-data-but-output-pcap-file-still-has-encrypted-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37266-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to have pcap file with decrypted SSL data in it. I am running tshark like this-</p><pre><code>tshark -o &quot;ssl.desegment_ssl_records: TRUE&quot; -o &quot;ssl.desegment_ssl_application_data: TRUE&quot; -o &quot;ssl.keys_list:192.168.56.101,443,http,/etc/nginx/cert.key&quot; -o &quot;ssl.debug_file:/tmp/ssl.log&quot; tcp port 443 -w /tmp/ssl.pcap</code></pre><p>When I review <code>/tmp/ssl.log</code> file I can see decryption is happening just fine. I can see plaintext data in it(ssl.log) but when I open /tmp/ssl.pcap in WireShark I observe that tshark is not putting plaintext data in it.</p><p>Is this expected behaviour? If so, how do I go about getting plaintext data directly in pcap file</p><p><strong>Version info</strong></p><p>Linux Kernel - Linux debian1 3.2.0-4-amd64</p><p>Distribution - Debian Stable</p><p>TShark version - 1.8.2</p></div><div id="question-tags" class="tags-container tags">ssl pcap tshark ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '14, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/cc8c7b7305415e6eddfb4ba1fab236ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gauravphoenix&#39;s gravatar image" /><p>gauravphoenix<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gauravphoenix has no accepted answers">0%</span></p></div></div><div id="comments-container-37266" class="comments-container"></div><div id="comment-tools-37266" class="comment-tools"></div><div class="clear"></div><div id="comment-37266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37267"></span>

<div id="answer-container-37267" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37267-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yep, that's expected, the data is only decrypted for display purposes, the packets written to the output file are those from the input that have passed any supplied filters.</p><p>Think about what you're asking for, the protocols in your capture were originally something like ethernet -&gt; ip -&gt; tcp -&gt; ssl -&gt; payload, and you now want to "remove" the ssl layer and end up with ethernet -&gt; ip -&gt; tcp -&gt; payload, so all the headers of the protocols underlying the ssl payload would need to be adjusted for lengths, checksums, sequence numbers etc.</p><p>You could use tshark to output the decrypted text and then use some other application to stuff that back into a pcap to give you the required info, but I don't know what the "other application" is.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37267" class="comments-container"><span id="37268"></span><div id="comment-37268" class="comment"><div id="post-37268-score" class="comment-score"></div><div class="comment-text"><p>Thanks for detailed answer. What is the most elegant way for saving plaintext data from tshark?</p></div><div id="comment-37268-info" class="comment-info"><span class="comment-age">(22 Oct '14, 03:29)</span> gauravphoenix</div></div><span id="37269"></span><div id="comment-37269" class="comment"><div id="post-37269-score" class="comment-score"></div><div class="comment-text"><p>Depends on how you want to process it, you can use plain text, csv, psml, pdml or postscript, and probably hex as well.</p><p>You could also limit the output to just the payload protocol.</p></div><div id="comment-37269-info" class="comment-info"><span class="comment-age">(22 Oct '14, 03:57)</span> grahamb ♦</div></div><span id="37270"></span><div id="comment-37270" class="comment"><div id="post-37270-score" class="comment-score"></div><div class="comment-text"><p>Wiresharks Export PDU function can export the decrypted layer above SSL to a pcap file retaining meta information of the packets like src/dst IP of original frame etc. But it's not available fom tshark yet.</p></div><div id="comment-37270-info" class="comment-info"><span class="comment-age">(22 Oct '14, 05:04)</span> Anders ♦</div></div></div><div id="comment-tools-37267" class="comment-tools"></div><div class="clear"></div><div id="comment-37267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37273"></span>

<div id="answer-container-37273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37273-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As Graham said, this is expected.</p><p>But if you can use the GUI then you have access to the "Export PDUs to file" function (under the File menu) which allows you to export decrypted packets into a new PCAP file.</p><p>(Note, though, that new PCAP file will probably only be readable by Wireshark; other programs using the PCAP format probably won't understand Wireshark's special "exported PDUs" DLT value.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37273" class="comments-container"></div><div id="comment-tools-37273" class="comment-tools"></div><div class="clear"></div><div id="comment-37273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

