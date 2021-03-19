+++
type = "question"
title = "Packet timestamps with capinfos/tshark (lauched from cygwin) are off by several hours"
description = '''I have a cap file captured with tcpdump on a Linux system. The first paket is known to be dated Thu Dec 06 11:47:00. This is what I see when I run capinfos -a or tcpdump -r on Linux, and also when I open the file in Wireshark on Windows.  When I run capinfos -m on Windows, I am told the time of the ...'''
date = "2012-12-13T12:31:00Z"
lastmod = "2012-12-17T08:09:00Z"
weight = 16846
keywords = [ "timestamp", "cygwin" ]
aliases = [ "/questions/16846" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Packet timestamps with capinfos/tshark (lauched from cygwin) are off by several hours](/questions/16846/packet-timestamps-with-capinfostshark-lauched-from-cygwin-are-off-by-several-hours)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16846-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a cap file captured with tcpdump on a Linux system. The first paket is known to be dated <code>Thu Dec 06 11:47:00</code>. This is what I see when I run <code>capinfos -a</code> or <code>tcpdump -r</code> on Linux, and also when I open the file in Wireshark on Windows.</p><p>When I run <code>capinfos -m</code> on Windows, I am told the time of the first packet is <code>Thu Dec 06 16:47:00 2012</code>. Tshark will display the same if I run it with <code>-T fields -e frame.time</code>.</p><p>If I run tshark on Windows with <code>-T fields -e frame.time_epoch</code> and convert it with <code>date -d '@1354812420.853205000'</code>, I will get the time I want. But I'd rather not do the conversion myself.</p><p>So my question is: what is going on with my timestamps? Both machines I am using are in the same timezone and clocks are set correctly. Can I have tshark display the time I want without doing any conversions myself?</p><p><strong>EDIT: How to reproduce</strong></p><p>It is actually simple to reproduce. I simply captured a telnet attempt with tcpdump and ran capinfos on it.</p><p>What really bothers me is tshark and wireshark not displaying the same thing. If I play with the timestamps with editcap, they won't show up correctly in wireshark anymore.</p><p>If I capture with tshark I won't have such problem. Maybe its time to start capturing directly with tshark. I have been capturing with tcpdump out of habit (and analysing with wireshark on windows).</p><p>RHEL 5.7 (tcpdump-3.9.4-15, wireshark-1.0.15-1)</p><pre><code>File name: cap
File type: Wireshark/tcpdump/... - libpcap
File encapsulation: Ethernet
Number of packets: 5
File size: 450 bytes
Data size: 346 bytes
Capture duration: 3.117839 seconds
Start time: Mon Dec 17 10:17:44 2012
End time: Mon Dec 17 10:17:47 2012
Data rate: 110.97 bytes/s
Data rate: 887.79 bits/s
Average packet size: 69.20 bytes</code></pre><p>On Windows (Wireshark Version 1.8.4 (SVN Rev 46250 from /trunk-1.8, cygwin)</p><pre><code>File name:           cap
File type:           Wireshark/tcpdump/... - libpcap
File encapsulation:  Ethernet
Packet size limit:   file hdr: 96 bytes
Number of packets:   5
File size:           450 bytes
Data size:           346 bytes
Capture duration:    3 seconds
Start time:          Mon Dec 17 15:17:44 2012
End time:            Mon Dec 17 15:17:47 2012
Data byte rate:      110.97 bytes/sec
Data bit rate:       887.79 bits/sec
Average packet size: 69.20 bytes
Average packet rate: 1.60 packets/sec
SHA1:                93e5fbf5bf7a6df1f6da066977335890c50e74e8
RIPEMD160:           c866a969118d29e58f65adf1a91faf1726430965
MD5:                 35870c270f932cecfb838b091afe7797
Strict time order:   True</code></pre><p><strong>EDIT 2</strong></p><p>The timezone is identical on both systems. The simplest way to see it:</p><pre><code># RHEL
date -R
Mon, 17 Dec 2012 11:56:34 -0500

# CYGWIN
LANG=en date -R
Mon, 17 Dec 2012 11:56:00 -0500</code></pre><p>On Linux TZ is not set. /etc/timezone does not exist on RHEL. But here's what I have in /etc/sysconfig/clock:</p><pre><code>ZONE=&quot;America/Montreal&quot;
UTC=true
ARC=false</code></pre><p>On Windows, TZ is not set. But the date gui shows the right zone as well as regedit:</p><pre><code> standardname        REG_SZ  Eastern Standard Time</code></pre><p>This whole problem seems to revolve around UTC. The dates I see in capinfos and tshark are UTC.</p></div><div id="question-tags" class="tags-container tags">timestamp cygwin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '12, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/49a7ee5012c5ee27f94f16be6cd13d1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PhilippeA&#39;s gravatar image" /><p>PhilippeA<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PhilippeA has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Mar '16, 16:01</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16846" class="comments-container"><span id="16889"></span><div id="comment-16889" class="comment"><div id="post-16889-score" class="comment-score"></div><div class="comment-text"><p>can you post that file somewhere (<a href="http://cloudshark.org">cloudshark.org</a>)?</p></div><div id="comment-16889-info" class="comment-info"><span class="comment-age">(14 Dec '12, 07:48)</span> Kurt Knochner ♦</div></div><span id="16977"></span><div id="comment-16977" class="comment"><div id="post-16977-score" class="comment-score"></div><div class="comment-text"><p>See <a href="http://cloudshark.org/captures/50cca25994ec.">http://cloudshark.org/captures/50cca25994ec.</a> The timestamp in cloudshark shows correctly (10:17:44). But it should not with tshark/capinfos. Please also see my question edit. Thanks.</p></div><div id="comment-16977-info" class="comment-info"><span class="comment-age">(17 Dec '12, 07:55)</span> PhilippeA</div></div><span id="16979"></span><div id="comment-16979" class="comment"><div id="post-16979-score" class="comment-score"></div><div class="comment-text"><p>Did you look at my answer below? Can you show the output of <code>set TZ</code> from the command prompt where you call capinfos\tshark?</p></div><div id="comment-16979-info" class="comment-info"><span class="comment-age">(17 Dec '12, 08:13)</span> grahamb ♦</div></div><span id="16983"></span><div id="comment-16983" class="comment"><div id="post-16983-score" class="comment-score"></div><div class="comment-text"><p>Eastern Standard Time == GMT - 5, so it looks like your windows system shows GMT time (5 hours difference).</p></div><div id="comment-16983-info" class="comment-info"><span class="comment-age">(17 Dec '12, 10:30)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16846" class="comment-tools"></div><div class="clear"></div><div id="comment-16846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16895"></span>

<div id="answer-container-16895" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16895-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>By default, Wireshark and associated programs follow the timezone setting of the user, and display times in the users local timezone.</p><p>I would guess that the timezone setting for the command prompt on the windows systems where you are running the errant capinfos and tshark have a timezone that is set 5 hours earlier than the linux system.</p><p><strong>Edit:</strong></p><p>After your edit 2 about the timezone settings I'm a bit confused. On Windows are you running a Windows version or a Linux version run with Cygwin? If you are using a Windows version then try running it under a normal Windows Cmd Prompt or PowerShell rather than Cygwin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '12, 09:34</p></div></div><div id="comments-container-16895" class="comments-container"><span id="16984"></span><div id="comment-16984" class="comment"><div id="post-16984-score" class="comment-score"></div><div class="comment-text"><p>The date command output is from Cygwin. I checked the rest in cmd. The bottom line remains the same: my clocks and timezones are consistent.</p></div><div id="comment-16984-info" class="comment-info"><span class="comment-age">(17 Dec '12, 11:02)</span> PhilippeA</div></div><span id="16985"></span><div id="comment-16985" class="comment"><div id="post-16985-score" class="comment-score"></div><div class="comment-text"><p>what happens if you run capinfos from <strong>outside</strong> of cygwin?</p></div><div id="comment-16985-info" class="comment-info"><span class="comment-age">(17 Dec '12, 11:06)</span> Kurt Knochner ♦</div></div><span id="16991"></span><div id="comment-16991" class="comment"><div id="post-16991-score" class="comment-score"></div><div class="comment-text"><p>Cygwin was the culprit. The TZ is set in cygwin. I don't understand why, but disabling it solves my issue.</p></div><div id="comment-16991-info" class="comment-info"><span class="comment-age">(17 Dec '12, 12:01)</span> PhilippeA</div></div><span id="16993"></span><div id="comment-16993" class="comment"><div id="post-16993-score" class="comment-score"></div><div class="comment-text"><p>Good! Please accept the answer of @grahamb for the benefit of other users.</p></div><div id="comment-16993-info" class="comment-info"><span class="comment-age">(17 Dec '12, 12:07)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16895" class="comment-tools"></div><div class="clear"></div><div id="comment-16895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16978"></span>

<div id="answer-container-16978" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16978-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>it shows the <strong>same</strong> timestamp on my Ubuntu 12.04 and my Win XP system (see below), but a different time than on your system, which is due to a different time zone (here: CET). So I guess, it's a timezone problem, as already mentioned by @grahamb.</p><p>What is the output of these commands on your systems?</p><blockquote><p><code>Windows: reg query HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\TimeZoneInformation /v standardname | FIND "REG_SZ"</code><br />
</p><p><code>Windows: set | find "TZ"</code><br />
</p><p><code>Linux: cat /etc/timezone</code><br />
</p><p><code>Linux: echo $TZ</code><br />
</p></blockquote><p><strong>Windows XP</strong></p><pre><code>Z:\ask.wireshark.org&gt;capinfos timestamp.cap
File name:           timestamp.cap
File type:           Wireshark/tcpdump/... - libpcap
File encapsulation:  Ethernet
Packet size limit:   file hdr: 96 bytes
Number of packets:   5
File size:           450 bytes
Data size:           346 bytes
Capture duration:    3 seconds
Start time:          Mon Dec 17 16:17:44 2012
End time:            Mon Dec 17 16:17:47 2012
Data byte rate:      110.97 bytes/sec
Data bit rate:       887.79 bits/sec
Average packet size: 69.20 bytes
Average packet rate: 1.60 packets/sec
SHA1:                93e5fbf5bf7a6df1f6da066977335890c50e74e8
RIPEMD160:           c866a969118d29e58f65adf1a91faf1726430965
MD5:                 35870c270f932cecfb838b091afe7797
Strict time order:   True

Z:\ask.wireshark.org\&gt;tshark -nr timestamp.cap -T fields -e frame.time
Dec 17, 2012 16:17:44.234821000
Dec 17, 2012 16:17:44.234822000
Dec 17, 2012 16:17:44.234835000
Dec 17, 2012 16:17:47.352494000
Dec 17, 2012 16:17:47.352660000</code></pre><p><strong>Ubuntu 12.04</strong></p><pre><code>[email protected]:/$ capinfos timestamp.cap 
File name:           timestamp.cap
File type:           Wireshark/tcpdump/... - libpcap
File encapsulation:  Ethernet
Packet size limit:   file hdr: 96 bytes
Number of packets:   5
File size:           450 bytes
Data size:           346 bytes
Capture duration:    3 seconds
Start time:          Mon Dec 17 16:17:44 2012
End time:            Mon Dec 17 16:17:47 2012
Data byte rate:      110.97 bytes/sec
Data bit rate:       887.79 bits/sec
Average packet size: 69.20 bytes
Average packet rate: 1.60 packets/sec
SHA1:                93e5fbf5bf7a6df1f6da066977335890c50e74e8
RIPEMD160:           c866a969118d29e58f65adf1a91faf1726430965
MD5:                 35870c270f932cecfb838b091afe7797
Strict time order:   True

[email protected]:$ tshark -nr timestamp.cap  -T fields -e frame.time
Dec 17, 2012 16:17:44.234821000
Dec 17, 2012 16:17:44.234822000
Dec 17, 2012 16:17:44.234835000
Dec 17, 2012 16:17:47.352494000
Dec 17, 2012 16:17:47.352660000

[email protected]:$ tcpdump -nr /tmp/timestamp.cap
reading from file /tmp/timestamp.cap, link-type EN10MB (Ethernet)
16:17:44.234821 IP 127.0.0.1.25533 &gt; 127.0.0.1.18009: Flags [S], seq 4185924599, win 32792, options [mss 16396,sackOK,TS val 3539423714 ecr 0,nop,wscale 7], length 0
16:17:44.234822 IP 127.0.0.1.18009 &gt; 127.0.0.1.25533: Flags [S.], seq 4191217688, ack 4185924600, win 32768, options [mss 16396,sackOK,TS val 3539423714 ecr 3539423714,nop,wscale 7], length 0
16:17:44.234835 IP 127.0.0.1.25533 &gt; 127.0.0.1.18009: Flags [.], ack 1, win 257, options [nop,nop,TS val 3539423714 ecr 3539423714], length 0
16:17:47.352494 IP 127.0.0.1.25533 &gt; 127.0.0.1.18009: Flags [F.], seq 1, ack 1, win 257, options [nop,nop,TS val 3539426832 ecr 3539423714], length 0
16:17:47.352660 IP 127.0.0.1.18009 &gt; 127.0.0.1.25533: Flags [R.], seq 1, ack 2, win 256, options [nop,nop,TS val 3539426832 ecr 3539426832], length 0</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '12, 08:21</p></div></div><div id="comments-container-16978" class="comments-container"></div><div id="comment-tools-16978" class="comment-tools"></div><div class="clear"></div><div id="comment-16978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

