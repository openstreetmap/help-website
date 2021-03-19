+++
type = "question"
title = "ARP replies appear with delay in Wireshark output"
description = '''If I send an ICMP &quot;echo request&quot; from 10.10.10.2 to 10.10.10.1, then according to tcpdump and Wireshark, 10.10.10.1 sends ICMP &quot;echo reply&quot; before ARP reply from 10.10.10.2 is received: 02:36:14.689050 00:1a:6b:6c:0c:cc &amp;gt; ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.10...'''
date = "2012-11-10T17:34:00Z"
lastmod = "2012-11-12T17:02:00Z"
weight = 15792
keywords = [ "arp", "linux" ]
aliases = [ "/questions/15792" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [ARP replies appear with delay in Wireshark output](/questions/15792/arp-replies-appear-with-delay-in-wireshark-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15792-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I send an ICMP "echo request" from 10.10.10.2 to 10.10.10.1, then according to tcpdump and Wireshark, 10.10.10.1 sends ICMP "echo reply" before ARP reply from 10.10.10.2 is received:</p><pre><code>02:36:14.689050 00:1a:6b:6c:0c:cc &gt; ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.10.10.1 tell 10.10.10.2, length 46
02:36:14.689079 00:1d:09:f0:92:ab &gt; 00:1a:6b:6c:0c:cc, ethertype ARP (0x0806), length 42: Reply 10.10.10.1 is-at 00:1d:09:f0:92:ab, length 28
02:36:14.689320 00:1a:6b:6c:0c:cc &gt; 00:1d:09:f0:92:ab, ethertype IPv4 (0x0800), length 98: 10.10.10.2 &gt; 10.10.10.1: ICMP echo request, id 8301, seq 1, length 64
02:36:14.689344 00:1d:09:f0:92:ab &gt; 00:1a:6b:6c:0c:cc, ethertype IPv4 (0x0800), length 98: 10.10.10.1 &gt; 10.10.10.2: ICMP echo reply, id 8301, seq 1, length 64
02:36:19.688639 00:1d:09:f0:92:ab &gt; 00:1a:6b:6c:0c:cc, ethertype ARP (0x0806), length 42: Request who-has 10.10.10.2 tell 10.10.10.1, length 28
02:36:19.689815 00:1a:6b:6c:0c:cc &gt; 00:1d:09:f0:92:ab, ethertype ARP (0x0806), length 60: Reply 10.10.10.2 is-at 00:1a:6b:6c:0c:cc, length 46</code></pre><p>Wireshark output can be seen <a href="http://www.cloudshark.org/captures/e4d6ea732135">here</a>.</p><p>Of course ARP traffic should appear before the ICMP "echo reply". Why tcpdump and Wireshark show ARP traffic with a delay? I use tcpdump version 4.1.1 and Wireshark 1.2.11. Both use libpcap 1.1.1. Any ideas what might cause such behavior?</p></div><div id="question-tags" class="tags-container tags">arp linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '12, 17:34</strong></p><img src="https://secure.gravatar.com/avatar/8fc701f2803add97aa6b718e44d49a07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m4rtin&#39;s gravatar image" /><p>m4rtin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m4rtin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Nov '12, 00:00</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-15792" class="comments-container"></div><div id="comment-tools-15792" class="comment-tools"></div><div class="clear"></div><div id="comment-15792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="15797"></span>

<div id="answer-container-15797" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15797-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>I find the timing of exactly 5 seconds too precise for a coincidence.</p><p>Several IP stacks verify the content of the ARP cache to identify stale entries. The details are usually implementation-specific.</p><p>The payload of the echo requests posted on cloudshark suggest that 10.10.10.1 is a Linux / Unix system. You might want to check the stale time defined in net/ipv4/neigh/$DEV/gc_stale_time</p><p>Still, absolutely normal operation and nothing to worry.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '12, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-15797" class="comments-container"><span id="15798"></span><div id="comment-15798" class="comment"><div id="post-15798-score" class="comment-score"></div><div class="comment-text"><p><strong>Kurt</strong>, <strong>packethunter</strong>: thank you for replies! Both hosts are Debian machines with 2.6.32-5-amd64 kernel. Content of the /proc/sys/net/ipv4/neigh/eth0/gc_stale_time is following:</p><pre><code>[email protected]:~# cat /proc/sys/net/ipv4/neigh/eth0/gc_stale_time
60
[email protected]:~#</code></pre><p>I tested this several times and 10.10.10.1 always sent ARP request 5s later. One example where I waited about 8min before and after the ICMP "echo request":</p><pre><code>[email protected]:~# time tcpdump -nei eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
13:53:05.823491 00:1a:6b:6c:0c:cc &gt; ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.10.10.1 tell 10.10.10.2, length 46
13:53:05.823529 00:1d:09:f0:92:ab &gt; 00:1a:6b:6c:0c:cc, ethertype ARP (0x0806), length 42: Reply 10.10.10.1 is-at 00:1d:09:f0:92:ab, length 28
13:53:05.823746 00:1a:6b:6c:0c:cc &gt; 00:1d:09:f0:92:ab, ethertype IPv4 (0x0800), length 98: 10.10.10.2 &gt; 10.10.10.1: ICMP echo request, id 9357, seq 1, length 64
13:53:05.823769 00:1d:09:f0:92:ab &gt; 00:1a:6b:6c:0c:cc, ethertype IPv4 (0x0800), length 98: 10.10.10.1 &gt; 10.10.10.2: ICMP echo reply, id 9357, seq 1, length 64
13:53:10.821636 00:1d:09:f0:92:ab &gt; 00:1a:6b:6c:0c:cc, ethertype ARP (0x0806), length 42: Request who-has 10.10.10.2 tell 10.10.10.1, length 28
13:53:10.830231 00:1a:6b:6c:0c:cc &gt; 00:1d:09:f0:92:ab, ethertype ARP (0x0806), length 60: Reply 10.10.10.2 is-at 00:1a:6b:6c:0c:cc, length 46
^C
6 packets captured
6 packets received by filter
0 packets dropped by kernel

real    16m58.812s
user    0m0.008s
sys 0m0.008s
[email protected]:~#</code></pre><p>Wireshark output can be seen <a href="http://www.cloudshark.org/captures/0440c57321c9">here</a>.</p><p>Maybe it is some sort of default behavior of Linux IP stack to check the accuracy of ARP table if the ARP table entry was built not by the ARP reply packet but some other unicast packet(ICMP "echo request" in this case)? In addition, is it possible to configure Linux kernel to use broadcast messages for building up ARP table?</p></div><div id="comment-15798-info" class="comment-info"><span class="comment-age">(11 Nov '12, 04:23)</span> m4rtin</div></div><span id="15800"></span><div id="comment-15800" class="comment"><div id="post-15800-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I find the timing of exactly 5 seconds too precise for a coincidence.</p></blockquote><p>well, hard to say, based on a single incident. But nevertheless, the idea about arp cache stale checking is a good idea.</p><blockquote><p>I tested this several times and 10.10.10.1 always sent ARP request 5s later.</p></blockquote><p>O.K. <strong>now</strong> it's clear, that it is not coincidental. So, it looks like a feature of the IP stack and the mentioned stale check is a good candidate.</p><p>@m4rtin: can you please retry and post the output of the following command before and after the ping. Run the command on 10.10.10.1.</p><blockquote><p><code>ip neighbor show 10.10.10.2</code><br />
</p></blockquote><p>It will show, if the ARP entry is stale.</p></div><div id="comment-15800-info" class="comment-info"><span class="comment-age">(11 Nov '12, 06:36)</span> Kurt Knochner ♦</div></div><span id="15814"></span><div id="comment-15814" class="comment"><div id="post-15814-score" class="comment-score"></div><div class="comment-text"><p>Does anybody find it curious that 10.10.10.1 is answering the ping without ARPing for a MAC address?</p><p>@m4rtin, I am assuming that you cleared the ARP cache on both systems?</p></div><div id="comment-15814-info" class="comment-info"><span class="comment-age">(12 Nov '12, 00:37)</span> packethunter</div></div></div><div id="comment-tools-15797" class="comment-tools"></div><div class="clear"></div><div id="comment-15797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15794"></span>

<div id="answer-container-15794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15794-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you can see:</p><p>Frame #1: ARP request from 10.10.10.2, as it needs the MAC address of 10.10.10.1<br />
Frame #2: ARP reply from 10.10.10.1 with it's MAC address<br />
Frame #3: Echo request from 10.10.10.2<br />
Frame #4: Echo reply from 10.10.10.1. Now, there is <strong>no</strong> need for 10.10.10.1 to send an ARP request as it learned the MAC address of 10.10.10.2 either from the Echo request packet, or because it already knew it (ARP cache). Otherwise it would be unable to send the Echo response packet.<br />
</p><p>Frame #5: ARP request from 10.l0.10.1 is <strong>just coincidental</strong> as the entry in the ARP cache of 10.10.10.1 timed out. This ARP request (5 seconds later!!) is not related to the ICMP echo response.</p><p>So, to me it looks like normal operation ...</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '12, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Nov '12, 01:16</p></div></div><div id="comments-container-15794" class="comments-container"><span id="15802"></span><div id="comment-15802" class="comment"><div id="post-15802-score" class="comment-score"></div><div class="comment-text"><p><strong>Kurt</strong>, this seems to work in a way that after 10.10.10.1 has sent ICMP "echo reply" the ARP table entry is in the "DELAY" state(I started with empty ARP table):</p><pre><code>10.10.10.2 dev eth0 lladdr 00:1a:6b:6c:0c:cc DELAY</code></pre><p>..and exactly 5s later 10.10.10.1 sends ARP request and once it has received a reply from 10.10.10.2, ARP table entry will go to "REACHABLE" state:</p><pre><code>10.10.10.2 dev eth0 lladdr 00:1a:6b:6c:0c:cc REACHABLE</code></pre><p>ARP table entry will stay in "REACHABLE" state for dozens of seconds. After this it changes state to "STALE".</p><p>Even if I ping 10.10.10.1 from 10.10.10.2 with 1s interval, it still marks the ARP table entry as "DELAY" if 30-60s has passed, waits 5s and sends ARP request. Once the reply is receiver, ARP table entry will go to "REACHABLE" state.</p><p>Why ARP request messages are sent despite the fact that there is constantly traffic between the hosts?</p></div><div id="comment-15802-info" class="comment-info"><span class="comment-age">(11 Nov '12, 14:46)</span> m4rtin</div></div><span id="15808"></span><div id="comment-15808" class="comment"><div id="post-15808-score" class="comment-score">1</div><div class="comment-text"><p>@m4rtin, I can confirm your result. I did the same tests with Ubuntu 12.04. Same result.</p><p>I guess that's the implementation of the Linux kernel to find stale ARP cache entries. If you want to know <strong>why</strong> it was implemented that way, you would have ask that question on the linux kernel mailing list.</p></div><div id="comment-15808-info" class="comment-info"><span class="comment-age">(11 Nov '12, 18:42)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15794" class="comment-tools"></div><div class="clear"></div><div id="comment-15794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15836"></span>

<div id="answer-container-15836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15836-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. I admit that this is a rather long post, but if you are willing to wade through it, you may (or may not ;-)) learn something new about the arp subsystem of the linux kernel, as I did during my 'research/tests'.</p><p>As @packethunter mentioned, there is the parameter <strong>delay_first_probe_time</strong> and its default value of <strong>5 seconds</strong> matches the observed delay, however the description in the man pages does not really match the observed behavior and there is actually a difference in behavior between ICMP and TCP (see my tests below).</p><p>I did some tests with Win XP SP3 (client - 192.168.158.139) and Ubuntu 12.04, Kernel 3.2.0-32 (server - 192.168.158.154). Here is what I observed.</p><p><strong>RFC</strong> RFC1122 defines how to handle validation of ARP cache entries.</p><blockquote><p><a href="http://tools.ietf.org/html/rfc1122#page-22">2.3.2.1 ARP Cache Validation</a><br />
</p></blockquote><p>That chapter defines four methods to flush out-of-date cache entries (please read the RFC). One of the methods is "Unicast Poll", which periodically sends ARP requests to verify ARP cache entries. The proposed interval is ~ 1 minute.</p><p><strong>arp man page</strong></p><blockquote><p><code>http://www.kernel.org/doc/man-pages/online/pages/man7/arp.7.html</code><br />
</p></blockquote><pre><code>       When there is no positive feedback for an existing mapping after some time
       (see the /proc interfaces below), a neighbor cache entry is considered stale.
       Positive feedback can be gotten from a higher layer; for example from a
       successful TCP ACK.  Other protocols can signal forward progress using the
       MSG_CONFIRM flag to sendmsg(2).  When there is no forward progress, ARP tries
       to reprobe.</code></pre><p>O.K. So, if a higher level protocol signals the arp subsystem, that the ARP entry is still good, it will not probe (for some time), otherwise it will probe. The example mentions just TCP ACK and that's where I started my tests.</p><p><strong>=================================================</strong><br />
<strong>== TEST #1:</strong> ping from windows -&gt; linux<br />
<strong>=================================================</strong><br />
</p><p>I cleared all arp caches and then I captured the traffic on linux with tcpdump and this filter: 'icmp or arp'.</p><p>I ran that command in background (shell). The output went to STDOUT and thus the output of tcpdump and the output of the loop command (see below) were merged. In the foreground I queried the arp cache with a loop.</p><blockquote><p><code>[email protected]:~# while true; do date; ip neigh show; sleep 1; done</code><br />
</p></blockquote><p>Result: As you can see below (TEST #1: Data), there is no ARP entry on linux until I started ping on windows, which triggered an ARP request from windows. Immediately after the ARP reply there is an entry in the linux arp cache, that is marked with <strong>DELAY</strong></p><blockquote><p><code>192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY</code><br />
</p></blockquote><p>So, linux obviously knows the MAC address of the windows box (from the ARP request). However, the entry is marked <strong>DELAY</strong> instead of <strong>REACHABLE</strong> (although a higher layer protocol could have given positive feedback - in this case ICMP).</p><p>Then, after 5 seconds, there is an arp request to verify the entry. After a valid answer, the entry is marked as <strong>REACHABLE</strong>. It remains in that state for 46 seconds. Then it's marked as <strong>STALE</strong></p><p>So, how does that match the definition in the arp man page?</p><blockquote><p>Cite: Positive feedback can be gotten from a higher layer ... When there is no forward progress, ARP tries to reprobe.</p></blockquote><p>So, apparently ICMP does <strong>not give positive feedback</strong> to the arp subsystem, otherwise there would have been no probe (this is different for TCP, see below).</p><p>Now, let's look at the time until the probe is sent (according to the capture files: 5 seconds). There is the following definition in the arp man page:</p><pre><code>delay_first_probe_time (since Linux 2.2)
              Delay before first probe after it has been decided that a neighbor is
              stale.  Defaults to 5 seconds.</code></pre><p>The default value is 5 seconds, but the description does not match the observed behavior. The entry was not <strong>STALE</strong> (as described in the man page). It was in the state <strong>DELAY</strong>.</p><p>So, how can we explain this discrepancy?</p><ul><li>it could be an error in the man page</li><li>the value could be used to probe <strong>DELAY</strong> entries as well</li><li>the value is unrelated to the probe sent for the <strong>DELAY</strong> entries, but then which value is used and where is that one defined (also 5 seconds)?</li></ul><p>I had not yet time to check the kernel source to find an answer to that question.</p><p>Finally: How long is an entry considered to be <strong>REACHABLE</strong> before it changes to <strong>STALE</strong>. From the arp man page.</p><pre><code>       base_reachable_time (since Linux 2.2)
              Once a neighbor has been found, the entry is considered to be valid for
              at least a random value between base_reachable_time/2 and
              3*base_reachable_time/2.  An entry&#39;s validity will be extended if it
              receives positive feedback from higher level protocols.  Defaults to 30
              seconds.  This file is now obsolete in favor of base_reachable_time_ms.

       base_reachable_time_ms (since Linux 2.6.12)
              As for base_reachable_time, but measures time in milliseconds.
              Defaults to 30000 milliseconds.</code></pre><p>So, the enrty is <strong>REACHABLE</strong> for a random amount of seconds in the range of <strong>base_reachable_time/2</strong> and <strong>3*base_reachable_time/2</strong>. The observed 46 seconds do fall into that range and if you repeat the test, you will get different values.</p><p><strong>=================================================</strong><br />
<strong>== TEST #1:</strong> Data<br />
<strong>=================================================</strong><br />
</p><pre><code>Sun Nov 11 21:42:07 CET 2012
Sun Nov 11 21:42:08 CET 2012
Sun Nov 11 21:42:09 CET 2012
Sun Nov 11 21:42:10 CET 2012
Sun Nov 11 21:42:11 CET 2012
Sun Nov 11 21:42:12 CET 2012
21:42:12.473391 ARP, Request who-has 192.168.158.154 tell 192.168.158.139, length 46
21:42:12.473434 ARP, Reply 192.168.158.154 is-at 00:0c:29:c5:f6:9b, length 28
21:42:12.473572 IP 192.168.158.139 &gt; 192.168.158.154: ICMP echo request, id 512, seq 4096, length 40
21:42:12.473656 IP 192.168.158.154 &gt; 192.168.158.139: ICMP echo reply, id 512, seq 4096, length 40
Sun Nov 11 21:42:13 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:42:14 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:42:15 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:42:16 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:42:17 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
21:42:17.481965 ARP, Request who-has 192.168.158.139 tell 192.168.158.154, length 28
21:42:17.482126 ARP, Reply 192.168.158.139 is-at 00:0c:29:34:0b:de, length 46
Sun Nov 11 21:42:18 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:42:19 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:42:20 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:42:21 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:42:22 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:42:23 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:42:24 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:42:25 CET 2012
...
Sun Nov 11 21:43:00 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:43:01 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:43:02 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE
Sun Nov 11 21:43:03 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE
Sun Nov 11 21:43:04 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE
Sun Nov 11 21:43:05 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE
Sun Nov 11 21:43:06 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE</code></pre><p><strong>=================================================</strong><br />
<strong>== TEST #2:</strong> tcp connect from windows -&gt; linux:22<br />
<strong>=================================================</strong><br />
</p><p>I cleared all arp caches and then I captured the traffic on linux with tcpdump and this filter: 'icmp or arp or tcp[13]&amp;2 ==2'.</p><p>I ran that command in background (shell). In the foreground I queried the arp cache with this command:</p><blockquote><p><code>[email protected]:~# while true; do date; ip neigh show; sleep 1; done</code><br />
</p></blockquote><p>Result: As you can see below, there is no ARP entry on linux until I connected to port 22 of the linux box, which triggered an ARP request from the windows system. Immediately after the ARP reply there is an entry in the linux arp cache, that is marked with <strong>DELAY</strong></p><blockquote><p><code>192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY</code><br />
</p></blockquote><p>So, linux obviously knows the MAC address of the windows box (from the ARP request). The entry is marked with <strong>DELAY</strong>.</p><p><strong>HOWEVER</strong>, this time there is <strong>no arp probe after 5 seconds</strong>. The entry changes from <strong>DELAY</strong> to <strong>REACHABLE</strong> automatically after 5 seconds (again that value!). So, this looks like a 'positive feedback from a higher layer', as described in the arp man page.</p><p><strong>=================================================</strong><br />
<strong>== TEST #2:</strong> Data<br />
<strong>=================================================</strong><br />
</p><pre><code>[email protected]:~# while true; do date; ip neigh show; sleep 1; done
Sun Nov 11 21:51:08 CET 2012
Sun Nov 11 21:51:09 CET 2012
Sun Nov 11 21:51:10 CET 2012
Sun Nov 11 21:51:11 CET 2012
Sun Nov 11 21:51:12 CET 2012
21:51:12.986592 ARP, Request who-has 192.168.158.154 tell 192.168.158.139, length 46
21:51:12.986638 ARP, Reply 192.168.158.154 is-at 00:0c:29:c5:f6:9b, length 28
21:51:12.986720 IP 192.168.158.139.3393 &gt; 192.168.158.154.22: Flags [S], seq 1430831265, win 64240, options [mss 1460,nop,nop,sackOK], length 0
21:51:12.986742 IP 192.168.158.154.22 &gt; 192.168.158.139.3393: Flags [S.], seq 1752069330, ack 1430831266, win 14600, options [mss 1460,nop,nop,sackOK], length 0
Sun Nov 11 21:51:13 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:51:14 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:51:15 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:51:16 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:51:17 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de DELAY
Sun Nov 11 21:51:18 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:19 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:20 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:21 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:22 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:23 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:24 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:25 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:26 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:27 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:28 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:29 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:30 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:31 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:32 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:33 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:34 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:35 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:36 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:37 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:38 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:39 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:40 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:41 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:42 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:43 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:44 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de REACHABLE
Sun Nov 11 21:51:45 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE
Sun Nov 11 21:51:46 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE
Sun Nov 11 21:51:47 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE
Sun Nov 11 21:51:48 CET 2012
192.168.158.139 dev eth0 lladdr 00:0c:29:34:0b:de STALE</code></pre><p><strong>CONCLUSION:</strong> One needs to check the kernel source code to fully understand why the linux kernel behaves in the observed way. If one want's to know why it was <strong>implemented</strong> that way (the difference between icmp and tcp), I suggest to post a question on the kernel developer list and prepare to get some friendly rant ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Nov '12, 23:47</p></div></div><div id="comments-container-15836" class="comments-container"></div><div id="comment-tools-15836" class="comment-tools"></div><div class="clear"></div><div id="comment-15836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15821"></span>

<div id="answer-container-15821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15821-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The riddle is solved on <a href="http://www.kernel.org/doc/man-pages/online/pages/man7/arp.7.html">http://www.kernel.org/doc/man-pages/online/pages/man7/arp.7.html</a></p><p>I don't want to quote the whole page, but the following abstract explains the behavior observed by m4rtin:</p><pre><code>ARP supports a range of /proc interfaces to configure parameters on a global or per-interface basis.  [...]</code></pre><p>One of the parameters is "delay_first_probe_time"</p><pre><code>   **delay_first_probe_time** (since Linux 2.2)
          Delay before first probe after it has been decided that a neighbor is
          stale.  Defaults to 5 seconds.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span> </br></br></p></div></div><div id="comments-container-15821" class="comments-container"></div><div id="comment-tools-15821" class="comment-tools"></div><div class="clear"></div><div id="comment-15821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

