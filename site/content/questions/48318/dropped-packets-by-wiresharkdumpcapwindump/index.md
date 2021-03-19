+++
type = "question"
title = "Dropped packets  by Wireshark/Dumpcap/WinDump"
description = '''Hello, We are trying to record some iSCSI traffic using Wireshark, and was consistently seeing dropped packets. We are running with a 1G buffer size, and rotating 5 files with 1G file size as well. The data is being saved to a RAMDisk, and the TEMP environment variables have also been changed to use...'''
date = "2015-12-06T23:51:00Z"
lastmod = "2015-12-08T13:27:00Z"
weight = 48318
keywords = [ "wireshark", "windump", "tcpdump", "dumpcap", "dropped" ]
aliases = [ "/questions/48318" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dropped packets by Wireshark/Dumpcap/WinDump](/questions/48318/dropped-packets-by-wiresharkdumpcapwindump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48318-score" class="post-score" title="current number of votes">0</div><span id="post-48318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, We are trying to record some iSCSI traffic using Wireshark, and was consistently seeing dropped packets. We are running with a 1G buffer size, and rotating 5 files with 1G file size as well. The data is being saved to a RAMDisk, and the TEMP environment variables have also been changed to use the Ramdisk.</p><p>Switched to using dumpcap straight, and with larger buffer sizes like wireshark. Same with winDump.</p><p>The machine is a 2.4GHz, 12 core, machine, and CPU usage when these numbers were recorded is about 14% max, including the dumppcap. The machine has about 72G of memory, 40 of which is being used for the Ramdisk, and about 20 is unused when these numbers were recorded.</p><p>I am positive we are doing something wrong here, or missing something really obvious. Can someone please point us in the right direction?</p><p>Here is the dumpcap output</p><pre><code>C:\Program Files\Wireshark&gt;dumpcap.exe -i 2 -i 3 -B 1024 -b files:5 -w F:\Trace\2.pcap
dumpcap: Ring buffer requested, but no maximum capture file size or duration were specified.
Capturing on 2 interfaces
File: F:\Trace\2_00001_20151207074008.pcap
Packets captured: 537560
Packets received/dropped on interface \Device\NPF_{42D93B77-D5B2-4FAD-8901-E7C54D63ECAD}: 421222/722498 (36.8%)
Packets received/dropped on interface \Device\NPF_{B0462921-3F8D-44A0-B828-7FDF0FD0AB9B}: 653570/556621 (54.0%)</code></pre><p>F:\ is the RAMDisk.</p><p>The current output on the machines is about 1.5 Gbps on each interface being captured. We see the same behavior even when we try to use a single interface</p><pre><code>C:\Program Files\Wireshark&gt;dumpcap.exe -i 2 -B 1024 -b files:5 -w F:\Trace\2.pcap
dumpcap: Ring buffer requested, but no maximum capture file size or duration were specified.
Capturing on \Device\NPF_{42D93B77-D5B2-4FAD-8901-E7C54D63ECAD}
File: F:\Trace\2_00001_20151207074218.pcap
Packets captured: 419766
Packets received/dropped on interface \Device\NPF_{42D93B77-D5B2-4FAD-8901-E7C54D63ECAD}: 419766/587700 (41.7%)</code></pre><p>With Windump, this is what we see:</p><pre><code>F:\WinDump&gt;WinDump.exe -n -i \Device\NPF_{42D93B77-D5B2-4FAD-8901-E7C54D63ECAD} -s0 -C 1024 -W 5 -B 2048576 -w capture.pcap -p -U
WinDump.exe: listening on \Device\NPF_{42D93B77-D5B2-4FAD-8901-E7C54D63ECAD}

2980237 packets captured
4512223 packets received by filter
1449839 packets dropped by kernel</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-windump" rel="tag" title="see questions tagged &#39;windump&#39;">windump</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-dropped" rel="tag" title="see questions tagged &#39;dropped&#39;">dropped</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '15, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/b2eb254debb093a83e03d472bfd6246b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manish%20Sharma&#39;s gravatar image" /><p><span>Manish Sharma</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manish Sharma has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Dec '15, 00:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48318" class="comments-container"></div><div id="comment-tools-48318" class="comment-tools"></div><div class="clear"></div><div id="comment-48318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48319"></span>

<div id="answer-container-48319" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48319-score" class="post-score" title="current number of votes">0</div><span id="post-48319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try to lower the capture frame size to figure out if the buffer is filling up too fast or if there is another problem. Start with 1024, 512, 256, 128, etc.</p><blockquote><p>dumpcap -i 2 -B 1024 -b files:5 -w F:\Trace\2.pca p dumpcap -s 512</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '15, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-48319" class="comments-container"><span id="48328"></span><div id="comment-48328" class="comment"><div id="post-48328-score" class="comment-score"></div><div class="comment-text"><p>We need the entire packet unfortunately, this is iSCSI, so we can have multiple PDUs in a single packet. With such a fast disk, and a big buffer, why is it that even tcpdump cannot keep up?</p></div><div id="comment-48328-info" class="comment-info"><span class="comment-age">(07 Dec '15, 08:31)</span> <span class="comment-user userinfo">Manish Sharma</span></div></div><span id="48334"></span><div id="comment-48334" class="comment"><div id="post-48334-score" class="comment-score"></div><div class="comment-text"><p>I understood <span>@Kurt Knochner</span>'s recommendation not as a solution but as a diagnostic step, allowing you to better localize the root cause of the issue.</p></div><div id="comment-48334-info" class="comment-info"><span class="comment-age">(07 Dec '15, 11:22)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48352"></span><div id="comment-48352" class="comment"><div id="post-48352-score" class="comment-score"></div><div class="comment-text"><p>Not much of a difference at different packet sizes also. Its really bugging me now..Even tried changing the default socket buffer recieve size. Not sure what the issue is at this point. Any other thoughts?</p></div><div id="comment-48352-info" class="comment-info"><span class="comment-age">(08 Dec '15, 08:17)</span> <span class="comment-user userinfo">Manish Sharma</span></div></div><span id="48365"></span><div id="comment-48365" class="comment"><div id="post-48365-score" class="comment-score"></div><div class="comment-text"><p>Then it'a most certainly what <span>@Jasper</span> wrote. If the network card is not optimized for capturing, you might loose frames. Just one hint: If the network card (in worst case) creates an interrupt for every single frame, you would simply overwhelm the CPU. So, those special cards (as well as some regular cards) usually have a buffer and they will only create an interrupt if that internal buffer is about to get full. This will speed up the capture process. There are other things the optimize together with drivers.</p><p>Furthermore Windows and Winpcap are probably not the best platforms to capture in high speed networks. Please try Linux and compare the results.</p></div><div id="comment-48365-info" class="comment-info"><span class="comment-age">(08 Dec '15, 13:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-48319" class="comment-tools"></div><div class="clear"></div><div id="comment-48319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48320"></span>

<div id="answer-container-48320" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48320-score" class="post-score" title="current number of votes">0</div><span id="post-48320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is that you're not using a high speed capture card with specialized capture drivers for this. The rest of the machine specs are impressive, but "normal" network cards are not fast enough to deal with high loads of packets (not even on 1GBit/s links, and certainly not on 10G or higher). I guess you need to look at FPGA based capture cards to do this, e.g. <a href="http://www.napatech.com">Napatech</a>, <a href="http://accoladetechnology.com/">Accolade Technology</a>, <a href="http://www.fiberblaze.com/">Fiberblaze</a> etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '15, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-48320" class="comments-container"><span id="48329"></span><div id="comment-48329" class="comment"><div id="post-48329-score" class="comment-score"></div><div class="comment-text"><p>Its not a normal network card, its emulex 10G which is usually used specifically in SAN environments..Why is it that the capability to capture with such fast memory and CPU is a problem? I am having a hard time trying to understand where the bottleneck could be.</p><p>Is there something in the NIC card that can be changed?</p></div><div id="comment-48329-info" class="comment-info"><span class="comment-age">(07 Dec '15, 08:33)</span> <span class="comment-user userinfo">Manish Sharma</span></div></div><span id="48331"></span><div id="comment-48331" class="comment"><div id="post-48331-score" class="comment-score"></div><div class="comment-text"><p>You cod try NPCAP <a href="https://github.com/nmap/npcap">https://github.com/nmap/npcap</a> I'm guessing that the single CPU core that's doing the capturing is at 100%</p></div><div id="comment-48331-info" class="comment-info"><span class="comment-age">(07 Dec '15, 08:59)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-48320" class="comment-tools"></div><div class="clear"></div><div id="comment-48320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

