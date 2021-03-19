+++
type = "question"
title = ".pcap parse question:  &quot;len&quot; verses &quot;length&quot;?"
description = '''I am writing a Delphi (Pascal) app that will do some custom parsing of a .pcap file. The .pcap file is written by Wireshare/winpcap. I found C++ sample code for parsing the .pcap file, and I converted the C++ structs to Delphi records. And I&#x27;ve got my app mostly done. But, one thing that I&#x27;m just no...'''
date = "2012-11-19T05:45:00Z"
lastmod = "2012-11-19T05:52:00Z"
weight = 16050
keywords = [ "parse", "length", "pcap" ]
aliases = [ "/questions/16050" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [.pcap parse question: "len" verses "length"?](/questions/16050/pcap-parse-question-len-verses-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16050-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a Delphi (Pascal) app that will do some custom parsing of a .pcap file. The .pcap file is written by Wireshare/winpcap. I found C++ sample code for parsing the .pcap file, and I converted the C++ structs to Delphi records. And I've got my app mostly done. But, one thing that I'm just not getting...</p><p>The headers for the Ethernet header, IP header and TCP header comes out to 54 bytes, assuming of course the packet in question is an Ethernet TCP/IP packet. Which is all I am working with. So, if the pcap record header incl_len is, for example, 60, then, the TCP payload would be 6 bytes, no?</p><p>Well, no, or at least it seems not necessarily. In Wireshark, you can display columns of "length" and "info". And within the "info" column, it tells you things like the sequence number, the ack number, etc. And it tells you the "len". But, I'm seeing some rows with a "length" of 60 with a "len" of 6, as I would expect. But other rows of "length" of 60 may have len = 1 or 2 or 3, etc.</p><p>Moreover, it seems that the "len" value, wherever it comes from, is the correct value for the usable data in the packet. If the len seems like it should be, say, 6 (in my example of length of 60) then if len is less than 6, then the additional bytes are just garbage or superfluous. Or maybe they have some meaning that is beyond my understanding.</p><p>So, here is my question: where the heck is Wireshark getting "len" from? As far as the "length", that does seem to be the incl_len. But, for the "len", I can't find it from any of the values in the headers. As I said, I would think it would be length-54 (assuming Ethernet TCP/IP) and it often is. But it often isn't and I haven't a clue where len is coming from but I need it.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">parse length pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '12, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/88638ff5bf062cf998bc9c87e3fbe320?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulJ&#39;s gravatar image" /><p>PaulJ<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulJ has no accepted answers">0%</span></p></div></div><div id="comments-container-16050" class="comments-container"><span id="16091"></span><div id="comment-16091" class="comment"><div id="post-16091-score" class="comment-score"></div><div class="comment-text"><p>Can you not just call a C library such as libpcap/WinPcap from Delphi? That's a lot easier than trying to read pcap files yourself (and than trying to read pcap-ng files as well, given that pcap-ng is the default output format of Wireshark 1.8.0 and later).</p><p>Note, BTW, that if, in a 1000-byte TCP segment over IPv4 over Ethernet, with 14 bytes of Ethernet header, 20 bytes of IPv4 header (with no options), 20 bytes of TCP header (with no options), and 1000 bytes of data, if incl_len is 128 and orig_len is 1054 (as it should be), using incl_len would not correctly indicate the TCP payload.</p></div><div id="comment-16091-info" class="comment-info"><span class="comment-age">(19 Nov '12, 19:31)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-16050" class="comment-tools"></div><div class="clear"></div><div id="comment-16050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16051"></span>

<div id="answer-container-16051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16051-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Cool, someone else besides me using Delphi to parse trace files...</p><p>If a packet has 54 bytes (14 Ethernet header, 20 IP header, 20 TCP header) and no TCP payload it would be too short to be a valid ethernet frame, which needs to be 60 bytes plus FCS = 64 Bytes. To achieve the minimum length, the frame is padded on the ethernet layer by 6 bytes. You can deduct the TCP payload length from taking the IP total length minus the IP and TCP header length.</p><p>By the way, you only see packets with a length of 54 bytes if you're capturing on the system that is sending them, because Wireshark/Dumppcap will "pick them up" before the network card has done the padding. You can verify this by capturing on the other machine - it will show you the packets including padding. Oh, and Wireshark does not keep the FCS, which is why you'll see 60 bytes instead of 64.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '12, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '12, 05:58</p></div></div><div id="comments-container-16051" class="comments-container"><span id="16082"></span><div id="comment-16082" class="comment"><div id="post-16082-score" class="comment-score"></div><div class="comment-text"><p>Ah, so, there is padding if the packet is less than a minimum length. But, I'm not seeing in what you say as to how to find out how much the padding is. When you say to "deduct the TCP payload length from taking the IP total length minus the IP and TCP header length", well, that, so far, seems to give me the size including the padding. I need the len, the length of actual data.</p><p>I absolutely have to have this information for my app to work. I am getting data stretched across multiple frames that are being sent by Telnet. I sometimes get 1 or 2 or 3 bytes of usable data. My app needs to stitch it together. I can't stitch it if I don't know how much padding there is.</p></div><div id="comment-16082-info" class="comment-info"><span class="comment-age">(19 Nov '12, 11:54)</span> PaulJ</div></div><span id="16085"></span><div id="comment-16085" class="comment"><div id="post-16085-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a comment as that's how this site works, please read the FAQ for details.</p></div><div id="comment-16085-info" class="comment-info"><span class="comment-age">(19 Nov '12, 13:36)</span> grahamb ♦</div></div><span id="16086"></span><div id="comment-16086" class="comment"><div id="post-16086-score" class="comment-score"></div><div class="comment-text"><p>take a look at the following packet:</p><blockquote><p><code>https://www.cloudshark.org/captures/016c970ebd51</code><br />
</p></blockquote><p>The frame length is 60 byte. The IP header starts at byte 0x0e(45 00 ..). The IP total length is 43 bytes. The IP header is 20 bytes and the TCP header is 20 bytes as well.</p><p>So: 43-20-20 = 3 bytes TCP payload and 3 bytes padding (00 00 00). Telnet data is starting at position 0x36 = 0x0e (IP start) + 0x14 (20 bytes IP header) + 0x14 (20 bytes TCP header).</p></div><div id="comment-16086-info" class="comment-info"><span class="comment-age">(19 Nov '12, 13:54)</span> Kurt Knochner ♦</div></div><span id="16089"></span><div id="comment-16089" class="comment"><div id="post-16089-score" class="comment-score"></div><div class="comment-text"><p>Ah, okay. I was looking looking for something that would be, say, 57 (3 bytes payload with 54 bytes in headers) instead of 43, which doesn't include the Ethernet header. Now, I see. Thanks!</p></div><div id="comment-16089-info" class="comment-info"><span class="comment-age">(19 Nov '12, 14:27)</span> PaulJ</div></div><span id="16090"></span><div id="comment-16090" class="comment"><div id="post-16090-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p></div><div id="comment-16090-info" class="comment-info"><span class="comment-age">(19 Nov '12, 14:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16051" class="comment-tools"></div><div class="clear"></div><div id="comment-16051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

