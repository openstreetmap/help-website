+++
type = "question"
title = "transfer from Linux to Windows"
description = '''I have several pcap files that I merge together using mergecap on Linux. &quot;mergecap -w output.pcap file1 file2 ....&quot; once the file is merged I then transfer it from the Linux box to a Windows machine using SecureFX and when I try to open it it says &quot;The file X.pcap isn&#x27;t a capture file in format Wire...'''
date = "2015-07-08T08:50:00Z"
lastmod = "2015-07-08T08:50:00Z"
weight = 43965
keywords = [ "linux" ]
aliases = [ "/questions/43965" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [transfer from Linux to Windows](/questions/43965/transfer-from-linux-to-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43965-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have several pcap files that I merge together using mergecap on Linux. "mergecap -w output.pcap file1 file2 ...."</p><p>once the file is merged I then transfer it from the Linux box to a Windows machine using SecureFX and when I try to open it it says "The file X.pcap isn't a capture file in format Wireshark understands."</p></div><div id="question-tags" class="tags-container tags">linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '15, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/c2f1187b3da18669b131dbe3021a68a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrjoli021&#39;s gravatar image" /><p>mrjoli021<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrjoli021 has no accepted answers">0%</span></p></div></div><div id="comments-container-43965" class="comments-container"><span id="43966"></span><div id="comment-43966" class="comment"><div id="post-43966-score" class="comment-score"></div><div class="comment-text"><p>If I run the same command in Windows CLI using the exact same files the merge works. For the Linux box I am using CentOS 6.5.</p></div><div id="comment-43966-info" class="comment-info"><span class="comment-age">(08 Jul '15, 08:55)</span> mrjoli021</div></div><span id="43969"></span><div id="comment-43969" class="comment"><div id="post-43969-score" class="comment-score">1</div><div class="comment-text"><p>Is your SecureFX tool transferring the file in binary mode (as it should) and not text mode? There is no reason for a pcap file created by mergecap on Linux to not open on Windows, unless it is corrupted during the transfer. A way to verify this would be to compute its MD5 or SHA1 on Linux and then on Windows after transfer and confirm they match.</p></div><div id="comment-43969-info" class="comment-info"><span class="comment-age">(08 Jul '15, 09:12)</span> Pascal Quantin</div></div><span id="43985"></span><div id="comment-43985" class="comment"><div id="post-43985-score" class="comment-score"></div><div class="comment-text"><p>Yes it is doing Binary I had already checked that. Same files and same command. One ran on windows CLI and I am able to open it on Windows wireshark. the other ran on CentOs 6.5 and when I transfer the file over it doesnt work. Maybe mergecap damages the files. The command I am using is "mergecap -w file.pcap file1 file2 ....." the only difference is that on windows i need to specify mergecap.exe. This is consistent I run pcaps everyday from multiple systems and everyday I cant open the file, but again same thing in windows and i am able to open it.</p><p>MD5sum passed before and after transfer.</p></div><div id="comment-43985-info" class="comment-info"><span class="comment-age">(08 Jul '15, 13:25)</span> mrjoli021</div></div><span id="43986"></span><div id="comment-43986" class="comment"><div id="post-43986-score" class="comment-score"></div><div class="comment-text"><p>What version of mergecap do you have on each platform? Post the output of "tshark -v" or "mergecap -V" from each machine here.</p><p>Perhaps the "pcap" file on the CentOS is actually a pcapng format, and the Windows version of Wireshark is so old it can't read it?</p></div><div id="comment-43986-info" class="comment-info"><span class="comment-age">(08 Jul '15, 13:55)</span> Hadriel</div></div><span id="43987"></span><div id="comment-43987" class="comment"><div id="post-43987-score" class="comment-score"></div><div class="comment-text"><p>Windows Wireshark Version 1.8.6</p><p>CentOS: TShark 1.8.10 (SVN Rev Unknown from unknown)</p><p>I am saving the file as output.pcap should I save it as something else?</p></div><div id="comment-43987-info" class="comment-info"><span class="comment-age">(08 Jul '15, 14:23)</span> mrjoli021</div></div><span id="43989"></span><div id="comment-43989" class="comment not_top_scorer"><div id="post-43989-score" class="comment-score"></div><div class="comment-text"><p>darn lost my comment...</p><p>mergecap (and Wireshark, and tshark) don't care about the file name extension really - they don't use it for deciding things.</p><p>Force mergecap to generate a old-style cap file by going this:</p><pre><code>mergecap -F pcap -w output.pcap infile1 infile2</code></pre></div><div id="comment-43989-info" class="comment-info"><span class="comment-age">(08 Jul '15, 15:09)</span> Hadriel</div></div><span id="43990"></span><div id="comment-43990" class="comment not_top_scorer"><div id="post-43990-score" class="comment-score"></div><div class="comment-text"><p>I get this error on when running in on CentOS: mergecap: The available capture file types for the "-F" flag are:</p><pre><code>5views - InfoVista 5View capture
btsnoop - Symbian OS btsnoop
commview - TamoSoft CommView
dct2000 - Catapult DCT2000 trace (.out format)
erf - Endace ERF capture
eyesdn - EyeSDN USB S0/E1 ISDN trace format
k12text - K12 text file
lanalyzer - Novell LANalyzer
libpcap - Wireshark/tcpdump/... - libpcap
modlibpcap - Modified tcpdump - libpcap
netmon1 - Microsoft NetMon 1.x
netmon2 - Microsoft NetMon 2.x
nettl - HP-UX nettl trace
ngsniffer - NA Sniffer (DOS)
ngwsniffer_1_1 - NA Sniffer (Windows) 1.1
ngwsniffer_2_0 - NA Sniffer (Windows) 2.00x
niobserver - Network Instruments Observer
nokialibpcap - Nokia tcpdump - libpcap 
nseclibpcap - Wireshark - nanosecond libpcap
nstrace10 - NetScaler Trace (Version 1.0)
nstrace20 - NetScaler Trace (Version 2.0)
pcapng - Wireshark - pcapng
rf5 - Tektronix K12xx 32-bit .rf5 format
rh6_1libpcap - RedHat 6.1 tcpdump - libpcap
snoop - Sun snoop
suse6_3libpcap - SuSE 6.3 tcpdump - libpcap
visual - Visual Networks traffic capture</code></pre></div><div id="comment-43990-info" class="comment-info"><span class="comment-age">(08 Jul '15, 15:30)</span> mrjoli021</div></div><span id="43992"></span><div id="comment-43992" class="comment not_top_scorer"><div id="post-43992-score" class="comment-score"></div><div class="comment-text"><p>OK, so the name was different back then... try "libpcap", i.e.:</p><pre><code>mergecap -F libpcap -w output.pcap infile1 infile2</code></pre></div><div id="comment-43992-info" class="comment-info"><span class="comment-age">(08 Jul '15, 15:47)</span> Hadriel</div></div><span id="43993"></span><div id="comment-43993" class="comment not_top_scorer"><div id="post-43993-score" class="comment-score"></div><div class="comment-text"><p>By using the suggested method "mergecap -F libpcap -w output.pcap infile1 infile2" I not getting that error anymore. I am not getting a different error:</p><p>"The capture file appears to be damaged or corrupt. (pcap file has 14436269812-byte packet, bigger than maximum of 65535)"</p></div><div id="comment-43993-info" class="comment-info"><span class="comment-age">(08 Jul '15, 17:00)</span> mrjoli021</div></div><span id="43994"></span><div id="comment-43994" class="comment not_top_scorer"><div id="post-43994-score" class="comment-score"></div><div class="comment-text"><p>Well that is really weird. You're getting that error on the Windows Wireshark 1.8.6, after copying the file over from CentOS Wireshark 1.8.10? <code>14436269812</code> is bigger than a 32-bit unsigned integer - which is what the packet length field is - so how could it even come up with such a big number to print it in the error message?</p><p>Well... your options are (1) upgrade the Windows Wireshark to something more modern and not end-of-life, like 1.12.6. Or at least to something newer than 1.8.6. See if that fixes it. Or (2) post a sample merged capture file that's supposedly corrupted, to somewhere we can get at it.</p></div><div id="comment-43994-info" class="comment-info"><span class="comment-age">(08 Jul '15, 18:31)</span> Hadriel</div></div><span id="43995"></span><div id="comment-43995" class="comment not_top_scorer"><div id="post-43995-score" class="comment-score"></div><div class="comment-text"><p>What is the size, in bytes, of the file on the Linux machine, and what is the size, in bytes, of the copy of that file on the Windows machine?</p></div><div id="comment-43995-info" class="comment-info"><span class="comment-age">(08 Jul '15, 20:22)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-43965" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-43965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

