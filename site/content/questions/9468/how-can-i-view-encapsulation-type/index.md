+++
type = "question"
title = "How can I view encapsulation type?"
description = '''I have a Wireshark capture file, and I&#x27;d like to see what encapsulations it has in one of its packages. How can I do this?'''
date = "2012-03-11T05:17:00Z"
lastmod = "2012-03-11T07:57:00Z"
weight = 9468
keywords = [ "encapsulation" ]
aliases = [ "/questions/9468" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I view encapsulation type?](/questions/9468/how-can-i-view-encapsulation-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9468-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Wireshark capture file, and I'd like to see what encapsulations it has in one of its packages. How can I do this?</p></div><div id="question-tags" class="tags-container tags">encapsulation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '12, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/e9f52ba2b79362235b07e49483f85d8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skorzeny8814&#39;s gravatar image" /><p>Skorzeny8814<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skorzeny8814 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Mar '12, 12:29</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-9468" class="comments-container"></div><div id="comment-tools-9468" class="comment-tools"></div><div class="clear"></div><div id="comment-9468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9470"></span>

<div id="answer-container-9470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9470-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what you mean by "encapsulations it has in one of its packages". Encapsulation, defined simply, is the "top-level" format of each frame in the file and can be "per file" or "per packet".</p><p>Examples:</p><pre><code>dvbci - DVB-CI (Common Interface)
enc - OpenBSD enc(4) encapsulating interface
erf - Endace Record File
ether - Ethernet
ether-nettl - Ethernet with nettl headers</code></pre><p>(Do you mean "protocols in a frame" ?)</p><p>The encapsulation (or possibly the list of encapsulations) for a capture file can be determined by using <code>capinfos</code> (one of the tools provided by the Wireshark suite).</p><p>Example::</p><pre><code>$capinfos _tmp_v6-http.cap
File name:           _tmp_v6-http.cap
File type:           Wireshark/tcpdump/... - libpcap
File encapsulation:  Ethernet
Packet size limit:   file hdr: 65535 bytes
Number of packets:   55
File size:           9159 bytes
Data size:           8255 bytes
Capture duration:    325 seconds
Start time:          Sun Aug 05 15:11:19 2007
End time:            Sun Aug 05 15:16:44 2007
Data byte rate:      25.40 bytes/sec
Data bit rate:       203.16 bits/sec
Average packet size: 150.09 bytes
Average packet rate: 0.17 packets/sec
SHA1:                7fd9486dea4cd77ae58cefab62fe3adf28f50cad
RIPEMD160:           decfdd7e46f540674bb1c3c796fd97af8c639e1a
MD5:                 803acd7573a6bd87baa777fedb432364
Strict time order:   True</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '12, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Mar '12, 12:59</p></div></div><div id="comments-container-9470" class="comments-container"><span id="9474"></span><div id="comment-9474" class="comment"><div id="post-9474-score" class="comment-score"></div><div class="comment-text"><p>And if you <em>do</em> mean "protocols in a frame" - or even those protocols sometimes thought of as "encapsulations", for example, GRE - the only way to do <em>that</em> would be to read the file with Wireshark or TShark and look at the frame's contents.</p></div><div id="comment-9474-info" class="comment-info"><span class="comment-age">(11 Mar '12, 12:29)</span> Guy Harris ♦♦</div></div><span id="21538"></span><div id="comment-21538" class="comment"><div id="post-21538-score" class="comment-score"></div><div class="comment-text"><p>Thank you for pointing to capinfos.exe - I was able to check if my file format ended up in something that scapy would throw an exception on (e.g. a file type of pcapng). I then used the editcap with the -F libpcap flag to convert my pcap to libpcap (which scapy did not throw an exception on).</p></div><div id="comment-21538-info" class="comment-info"><span class="comment-age">(28 May '13, 13:07)</span> vincent</div></div><span id="21539"></span><div id="comment-21539" class="comment"><div id="post-21539-score" class="comment-score"></div><div class="comment-text"><p>Yes, scapy has its own capture-file-reading code, rather than using one of the Python wrappers for libpcap, so it wouldn't magically pick up libpcap 1.1's ability to read some pcap-ng files.</p></div><div id="comment-21539-info" class="comment-info"><span class="comment-age">(28 May '13, 13:34)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9470" class="comment-tools"></div><div class="clear"></div><div id="comment-9470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

