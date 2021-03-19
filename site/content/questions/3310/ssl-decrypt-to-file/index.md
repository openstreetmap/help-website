+++
type = "question"
title = "SSL Decrypt to File"
description = '''Hi, I need to decode an ssl stream from a pcap file and save the decoded stream to a new pcap file. I use http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;amp;do=view&amp;amp;target=snakeoil2_070531.tgz cap and key from http://wiki.wireshark.org/SSL for test. So with command: tshark -n -d tcp....'''
date = "2011-04-03T14:28:00Z"
lastmod = "2011-04-03T14:36:00Z"
weight = 3310
keywords = [ "ssl", "pcap", "tshark" ]
aliases = [ "/questions/3310" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decrypt to File](/questions/3310/ssl-decrypt-to-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3310-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need to decode an ssl stream from a pcap file and save the decoded stream to a new pcap file. I use http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=snakeoil2_070531.tgz cap and key from http://wiki.wireshark.org/SSL for test. So with command:</p><p>tshark -n -d tcp.port==443,http -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list: 127.0.0.1,443,http,/snakeoil2_070531/rsasnakeoil2.key" -r /snakeoil2_070531/rsasnakeoil2.cap</p><p>tshark print on screen the testual version of decoded packets in right way. Now I need to save the real packets (not text) decoded (ssl-&gt;http) to a new file.</p><p>Using -w option tshark saves the same packet dunp that it reads (rsasnakeoil2.cap) to another file (test.pcap). The two files are equal.</p><p>tshark -n -d tcp.port==443,http -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list: 127.0.0.1,443,http,/snakeoil2_070531/rsasnakeoil2.key" -r /snakeoil2_070531/rsasnakeoil2.cap -w test.cap.</p><p>I can't understand why tshark can't save the decoded ssl traffic to another file. Help Me.</p><p>Detail of my wireshark version: wireshark 1.4.4</p><p>Copyright 1998-2011 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.22.1, with GLib 2.26.1, with libpcap 1.1.1, without libz, with POSIX capabilities (Linux), without libpcre, without SMI, without c-ares, without ADNS, without Lua, without Python, with GnuTLS 2.10.4, with Gcrypt 1.4.6, with Heimdal Kerberos, without GeoIP, without PortAudio, without AirPcap.</p><p>Running on Linux 2.6.37-ARCH, with libpcap version 1.1.1, GnuTLS 2.10.5, Gcrypt 1.4.6.</p><p>Built using gcc 4.5.2 20110127 (prerelease).</p></div><div id="question-tags" class="tags-container tags">ssl pcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '11, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/8996b99a2e3f15d58091495c1afb9857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mkl&#39;s gravatar image" /><p>mkl<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mkl has no accepted answers">0%</span></p></div></div><div id="comments-container-3310" class="comments-container"></div><div id="comment-tools-3310" class="comment-tools"></div><div class="clear"></div><div id="comment-3310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3311"></span>

<div id="answer-container-3311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3311-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark and tshark can't save decrypted data back into a new pcap file.</p><p>The best thing you can do is add -V (full decodes) to your tshark command and redirect the output to a text file and supply that with the pcap file.</p><p>Please also have a look at <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3444">feature request 3444</a>, in which the same question was asked.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3311" class="comments-container"></div><div id="comment-tools-3311" class="comment-tools"></div><div class="clear"></div><div id="comment-3311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

