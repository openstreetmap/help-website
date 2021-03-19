+++
type = "question"
title = "Tshark issue on ubuntu"
description = '''When i gave following command on ubuntu tshark -2 -F pcap -r tcpdump.pcap -R &quot;tcp and ip&quot; -w write.pcap 1) used -F pcap option i want e.pcap in old pcap format. problem/issue :- When i open write.pcap it has loosed his old time/date i.e. tcpdump.pcap in its Time column is having 26 July 2014 with so...'''
date = "2014-09-01T18:30:00Z"
lastmod = "2014-10-23T11:58:00Z"
weight = 35920
keywords = [ "tshark", "ubuntu" ]
aliases = [ "/questions/35920" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark issue on ubuntu](/questions/35920/tshark-issue-on-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35920-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When i gave following command on ubuntu</p><p>tshark -2 -F pcap -r tcpdump.pcap -R "tcp and ip" -w write.pcap</p><p>1) used -F pcap option i want e.pcap in old pcap format.</p><p>problem/issue :- When i open write.pcap it has loosed his old time/date</p><p>i.e. tcpdump.pcap in its Time column is having 26 July 2014 with some time 10.12.34 , but in write.pcap it comes to 1970-01-01 with time 00.00.00 in Time column.</p><p>If i use -w option i will give raw packet but why it is loosing Time from it. i.e. i want my Time to be intact rather that going to default time.</p><p>Is any way to correct this situation with option or anything else.</p></div><div id="question-tags" class="tags-container tags">tshark ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '14, 18:30</strong></p><img src="https://secure.gravatar.com/avatar/6e4b54399e50998763bf536748dffc64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravi1&#39;s gravatar image" /><p>Ravi1<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravi1 has no accepted answers">0%</span></p></div></div><div id="comments-container-35920" class="comments-container"><span id="35996"></span><div id="comment-35996" class="comment"><div id="post-35996-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark is this? (What does <code>tshark -v</code> print?)</p></div><div id="comment-35996-info" class="comment-info"><span class="comment-age">(04 Sep '14, 02:36)</span> Guy Harris ♦♦</div></div><span id="36270"></span><div id="comment-36270" class="comment"><div id="post-36270-score" class="comment-score"></div><div class="comment-text"><p>[email protected]:~$ tshark -v print TShark 1.10.6 (v1.10.6 from master-1.10)</p><p>Copyright 1998-2014 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GLib 2.39.91, with libpcap, with libz 1.2.8, with POSIX capabilities (Linux), without libnl, with SMI 0.4.8, with c-ares 1.10.0, with Lua 5.2, without Python, with GnuTLS 2.12.23, with Gcrypt 1.5.3, with MIT Kerberos, with GeoIP.</p><p>Running on Linux 3.13.0-32-generic, with locale en_US.UTF-8, with libpcap version 1.5.3, with libz 1.2.8. Intel(R) Core(TM) i5-3437U CPU @ 1.90GHz</p><p>Built using gcc 4.8.2. [email protected]:~$</p></div><div id="comment-36270-info" class="comment-info"><span class="comment-age">(12 Sep '14, 08:09)</span> Ravi1</div></div><span id="37304"></span><div id="comment-37304" class="comment"><div id="post-37304-score" class="comment-score"></div><div class="comment-text"><p>We'd probably need to see the original capture file to reproduce the problem. You might consider first upgrading to the latest version (currently 1.12.1) and if that doesn't help then open a bug report (it's easier to attach files there).</p></div><div id="comment-37304-info" class="comment-info"><span class="comment-age">(23 Oct '14, 02:37)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-35920" class="comment-tools"></div><div class="clear"></div><div id="comment-35920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37315"></span>

<div id="answer-container-37315" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37315-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like the same (or similar) error that was reported in another question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/28835/tshark-writing-1st-jan-1970-as-packet-time-stamps-after-writing-to-new-file-using-w-option">https://ask.wireshark.org/questions/28835/tshark-writing-1st-jan-1970-as-packet-time-stamps-after-writing-to-new-file-using-w-option</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '14, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37315" class="comments-container"></div><div id="comment-tools-37315" class="comment-tools"></div><div class="clear"></div><div id="comment-37315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

