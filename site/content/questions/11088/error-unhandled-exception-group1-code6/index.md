+++
type = "question"
title = "Error: Unhandled Exception (group=1, code=6)"
description = '''hi, when i use tshark to sniffer, it always appear error:Unhandled Exception (group=1, code=6) My cmd is &quot;tshark -nn -i eth1 -t ad -R &#x27;(tcp.flags.syn == 1 and tcp.flags.ack == 0 and ip.dst&amp;lt;192.168.0.0 or ip.dst&amp;gt;192.168.255.255)&#x27;&quot; Firstly, i thought maybe the memory isn`t enough, but after i fr...'''
date = "2012-05-17T01:00:00Z"
lastmod = "2012-05-17T02:49:00Z"
weight = 11088
keywords = [ "tshark" ]
aliases = [ "/questions/11088" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error: Unhandled Exception (group=1, code=6)](/questions/11088/error-unhandled-exception-group1-code6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11088-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, when i use tshark to sniffer, it always appear error:Unhandled Exception (group=1, code=6)</p><p>My cmd is "tshark -nn -i eth1 -t ad -R '(tcp.flags.syn == 1 and tcp.flags.ack == 0 and ip.dst&lt;192.168.0.0 or ip.dst&gt;192.168.255.255)'"</p><p>Firstly, i thought maybe the memory isn`t enough, but after i freed memory,i found it still error and now the free memory have 4G,</p><p>Can you tell me how to solve?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '12, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/861497af4aeeedc11c382438bcaa9005?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mastertu&#39;s gravatar image" /><p>mastertu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mastertu has no accepted answers">0%</span></p></div></div><div id="comments-container-11088" class="comments-container"><span id="11089"></span><div id="comment-11089" class="comment"><div id="post-11089-score" class="comment-score"></div><div class="comment-text"><ol><li>what is your OS</li><li>what is the version of tshark</li><li>do you run the command as root</li></ol><p>Regards<br />
Kurt</p></div><div id="comment-11089-info" class="comment-info"><span class="comment-age">(17 May '12, 01:14)</span> Kurt Knochner ♦</div></div><span id="11090"></span><div id="comment-11090" class="comment"><div id="post-11090-score" class="comment-score"></div><div class="comment-text"><ol><li>my os is centos 6.2</li><li>the version of tshark is TShark 1.2.15</li><li>yes, i run the command as root.</li></ol></div><div id="comment-11090-info" class="comment-info"><span class="comment-age">(17 May '12, 01:17)</span> mastertu</div></div><span id="11091"></span><div id="comment-11091" class="comment"><div id="post-11091-score" class="comment-score"></div><div class="comment-text"><pre><code>[[email protected] ~]# tshark -v
TShark 1.2.15

Copyright 1998-2011 Gerald Combs &lt;[email protected]wireshark.org&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (32-bit) with GLib 2.22.5, with libpcap 1.0.0, with libz 1.2.3, without
POSIX capabilities, with libpcre 7.8, with SMI 0.4.8, without c-ares, without
ADNS, without Lua, with GnuTLS 2.8.5, with Gcrypt 1.4.5, with MIT Kerberos,
without GeoIP.

Running on Linux 2.6.32-220.7.1.el6.i686, with libpcap version 1.0.0, GnuTLS
2.8.5, Gcrypt 1.4.5.

Built using gcc 4.4.6 20110731 (Red Hat 4.4.6-3).</code></pre></div><div id="comment-11091-info" class="comment-info"><span class="comment-age">(17 May '12, 01:20)</span> mastertu</div></div><span id="11092"></span><div id="comment-11092" class="comment"><div id="post-11092-score" class="comment-score"></div><div class="comment-text"><p>my sniffer data is very much, wheather it caused this errror?</p></div><div id="comment-11092-info" class="comment-info"><span class="comment-age">(17 May '12, 01:32)</span> mastertu</div></div><span id="11093"></span><div id="comment-11093" class="comment"><div id="post-11093-score" class="comment-score"></div><div class="comment-text"><p>maybe. When does the error occur. Right at the beginning?</p><p>BTW: before we are looking for possible errors in an older version of tshark, can you please upgrade to tshark 1.6? As CentOS 6.2 only provides wireshark 1.2, I suggest to look for a 1.6 rpm elsewhere or compile it yourself.</p></div><div id="comment-11093-info" class="comment-info"><span class="comment-age">(17 May '12, 01:37)</span> Kurt Knochner ♦</div></div><span id="11095"></span><div id="comment-11095" class="comment not_top_scorer"><div id="post-11095-score" class="comment-score"></div><div class="comment-text"><p>not right at the beginning, it after six or seven minutes.</p><p>Ok, i will upgrade it and try again</p></div><div id="comment-11095-info" class="comment-info"><span class="comment-age">(17 May '12, 02:19)</span> mastertu</div></div></div><div id="comment-tools-11088" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-11088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11097"></span>

<div id="answer-container-11097" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11097-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>This may very well be caused by running <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out-of-memory</a>. Especially since you say you are on a high bandwidth network and using display filters instead of capture filters.</p><p>Tshark is a statefull analyzer which means it does keep state of all kinds of sessions. It also does reassembly of higher layer protocols. All of this will increase its memory footprint while capturing. So it is best to present tshark as little data as possible to reduce the memory footprint while capturing. This can be done by using capture filters.</p><p>The equivalent capture filter for your display filter would be:</p><pre><code>tcp[13]&amp;18=2 and not (dst net 192.168.0.0 mask 255.255.0.0)</code></pre><p><em>(tcp[13] points to the TCP flags in the TCP header, the SYN bit has value 2, he ACK bit has value 16, so to only select SYN packets without SYN/ACK packets anding with 16+2 should result in 2. Then your not interested in TCP SYN's to systems in 192.168.0.0/16, so exclude those destinations with the "dst net" filter)</em></p><p>So you could use the command:</p><pre><code>tshark -nn -i eth1 -t ad -f &quot;tcp[13]&amp;18=2 and not (dst net 192.168.0.0 mask 255.255.0.0)&quot;</code></pre><p>Which should make it possible to run tshark for much longer periods than with your previous command. However, it will not run forever.</p><p>Please also note that using display filters in recent versions of tshark is not possible anymore while capturing as the capture engine has been moved to a separate process for <a href="http://wiki.wireshark.org/Development/PrivilegeSeparation">privilege separation</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '12, 06:19</p></div></div><div id="comments-container-11097" class="comments-container"><span id="11101"></span><div id="comment-11101" class="comment"><div id="post-11101-score" class="comment-score"></div><div class="comment-text"><p>Yes, he's running out of memory. Unfortunately tshark didn't catch the OutOfMemory exception until r39798. (After that rev tshark will tell you what the problem is rather than just failing to catch the exception.)</p></div><div id="comment-11101-info" class="comment-info"><span class="comment-age">(17 May '12, 05:54)</span> JeffMorriss ♦</div></div><span id="11129"></span><div id="comment-11129" class="comment"><div id="post-11129-score" class="comment-score"></div><div class="comment-text"><p>when i use "tshark -nn -i eth1 -t ad -f "tcp[13]&amp;18=2 and not (dst net 192.168.0.0 mask 255.255.0.0)""<br />
I found a lot of packets didn`t caught</p></div><div id="comment-11129-info" class="comment-info"><span class="comment-age">(18 May '12, 02:33)</span> mastertu</div></div><span id="11130"></span><div id="comment-11130" class="comment"><div id="post-11130-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "caught"? This capture filter does the same as your display filter. The output on screen should be the same (which I just verified myself with some test traffic).</p><p>Which traffic do you suspect is not caught?</p></div><div id="comment-11130-info" class="comment-info"><span class="comment-age">(18 May '12, 02:50)</span> SYN-bit ♦♦</div></div><span id="11132"></span><div id="comment-11132" class="comment"><div id="post-11132-score" class="comment-score"></div><div class="comment-text"><p>Sorry,please forgive my english. I mean that when i use cmd"tshark -nn -i eth1 -t ad -R '(tcp.flags.syn == 1 and tcp.flags.ack == 0 and ip.dst&lt;192.168.0.0 or ip.dst&gt;192.168.255.255)'" The sniffer result is right. But when i use cmd"tshark -nn -i eth1 -t ad -f "tcp[13]&amp;18=2 and not (dst net 192.168.0.0 mask 255.255.0.0)" I found the result is very less. I found the reson maybe caused by this capture "tcp[13]&amp;18=2", can you tell me why? Thany you.</p></div><div id="comment-11132-info" class="comment-info"><span class="comment-age">(18 May '12, 03:01)</span> mastertu</div></div><span id="11133"></span><div id="comment-11133" class="comment"><div id="post-11133-score" class="comment-score"></div><div class="comment-text"><p>As the filters should work the same (and they seem to do on my system), I'm very curious to see how the output differs. Can you start both commands and send me the some output that is missing from my command? Please also supply the exact commands that you used in the test.</p></div><div id="comment-11133-info" class="comment-info"><span class="comment-age">(18 May '12, 03:12)</span> SYN-bit ♦♦</div></div><span id="11134"></span><div id="comment-11134" class="comment not_top_scorer"><div id="post-11134-score" class="comment-score"></div><div class="comment-text"><pre><code>[[email protected] data]# tshark -nn -i eth1 -t ad -R &#39;(tcp.flags.syn == 1 and tcp.flags.ack == 0 and ip.dst&lt;192.168.0.0 or ip.dst&gt;192.168.255.255)&#39;
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on eth1
2012-05-18 18:15:59.024477 192.168.50.111 -&gt; 1.2.3.4      TCP 28728 &gt; 82 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 TSV=3171436 TSER=0
2012-05-18 18:15:59.090329 192.168.15.15 -&gt; 119.147.113.43 TCP 57546 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:15:59.123530 192.168.0.141 -&gt; 74.125.71.157 TCP 52304 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186171229 TSER=0
2012-05-18 18:15:59.125058 192.168.0.112 -&gt; 220.181.112.34 TCP 61277 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460
2012-05-18 18:15:59.125632 192.168.0.112 -&gt; 220.181.112.34 TCP 61278 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460
2012-05-18 18:15:59.377753 192.168.0.141 -&gt; 74.125.71.157 TCP 52305 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186171485 TSER=0
2012-05-18 18:15:59.474241 192.168.0.141 -&gt; 23.21.171.71 TCP 52306 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186171576 TSER=0
2012-05-18 18:15:59.483072 192.168.0.141 -&gt; 107.22.194.172 TCP 52307 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186171584 TSER=0
2012-05-18 18:15:59.529752 192.168.13.111 -&gt; 119.147.113.117 TCP 54843 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2
2012-05-18 18:15:59.531222 192.168.0.170 -&gt; 218.30.111.182 TCP 38563 &gt; 25 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:15:59.601367 192.168.50.118 -&gt; 1.2.3.4      TCP 49536 &gt; 82 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=2
2012-05-18 18:15:59.640381 192.168.13.137 -&gt; 119.147.113.98 TCP 51584 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2
2012-05-18 18:15:59.661852 192.168.0.186 -&gt; 125.64.93.204 TCP 50175 &gt; 65532 [SYN] Seq=0 Win=14600 Len=0 MSS=1460 TSV=3053589858 TSER=0 WS=6
2012-05-18 18:15:59.779664 192.168.15.140 -&gt; 119.147.113.105 TCP 59062 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:15:59.785710 192.168.11.22 -&gt; 1.2.3.4      TCP 55089 &gt; 82 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:15:59.869167 192.168.50.111 -&gt; 119.147.113.104 TCP 28729 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2 TSV=3171520 TSER=0
2012-05-18 18:16:00.004662 192.168.50.119 -&gt; 119.147.113.104 TCP 2729 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=0
2012-05-18 18:16:00.095211 192.168.18.12 -&gt; 119.147.113.98 TCP 62265 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2
2012-05-18 18:16:00.148128 192.168.0.141 -&gt; 58.83.170.244 TCP 52308 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186172241 TSER=0
2012-05-18 18:16:00.152433 192.168.0.141 -&gt; 58.83.170.244 TCP 52309 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186172245 TSER=0
2012-05-18 18:16:00.323979 192.168.15.15 -&gt; 119.147.113.43 TCP 57547 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:16:00.375384 192.168.12.103 -&gt; 183.60.136.64 TCP 52733 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:16:00.490977 192.168.50.124 -&gt; 183.60.9.160 TCP 56100 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:16:00.508177 192.168.90.18 -&gt; 58.58.58.58  TCP 2020 &gt; 1604 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2012-05-18 18:16:00.618612 192.168.0.141 -&gt; 63.141.192.120 TCP 52310 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186172698 TSER=0
2012-05-18 18:16:00.631318 192.168.0.141 -&gt; 63.141.192.120 TCP 52311 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186172707 TSER=0
2012-05-18 18:16:00.650815 192.168.0.141 -&gt; 63.141.192.120 TCP 52312 &gt; 80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=4 TSV=186172726 TSER=0
2012-05-18 18:16:00.770647 192.168.0.232 -&gt; 121.14.110.44 TCP 47859 &gt; 80 [SYN] Seq=0 Win=5840 Len=0 MSS=1460 TSV=890135769 TSER=0 WS=6
2012-05-18 18:16:00.782544 192.168.18.14 -&gt; 119.147.113.25 TCP 57899 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2
2012-05-18 18:16:00.824439 192.168.30.142 -&gt; 220.181.111.148 TCP 60162 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:16:00.852977 192.168.15.15 -&gt; 119.147.113.43 TCP 57548 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:16:00.883222 192.168.12.113 -&gt; 183.60.58.88 TCP 56490 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2
2012-05-18 18:16:00.883225 192.168.12.113 -&gt; 183.60.58.88 TCP 56489 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2
2012-05-18 18:16:00.933774 192.168.0.78 -&gt; 221.123.176.120 TCP 4984 &gt; 80 [SYN] Seq=0 Win=16384 Len=0 MSS=1460
2012-05-18 18:16:00.962308 192.168.15.15 -&gt; 119.147.113.43 TCP 57549 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8
2012-05-18 18:16:00.982045 192.168.50.124 -&gt; 220.181.181.223 TCP 56101 &gt; 80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2

[[email protected] data]# tshark -nn -i eth1 -t ad -f &quot;tcp[13]&amp;18=2 and not (dst net 192.168.0.0 mask 255.255.0.0)&quot;
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on eth1
2012-05-18 18:17:16.180467 192.168.90.18 -&gt; 58.58.58.58  TCP 2024 &gt; 1604 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2012-05-18 18:17:17.649489 192.168.90.14 -&gt; 58.58.58.58  TCP 1073 &gt; 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2012-05-18 18:17:19.148456 192.168.90.18 -&gt; 58.58.58.58  TCP 2024 &gt; 1604 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2012-05-18 18:17:20.554775 192.168.90.14 -&gt; 58.58.58.58  TCP 1073 &gt; 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2012-05-18 18:17:25.164211 192.168.90.18 -&gt; 58.58.58.58  TCP 2024 &gt; 1604 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2012-05-18 18:17:26.570437 192.168.90.14 -&gt; 58.58.58.58  TCP 1073 &gt; 80 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2012-05-18 18:17:37.399896 192.168.90.18 -&gt; 58.58.58.58  TCP 2025 &gt; 1604 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
2012-05-18 18:17:40.257794 192.168.90.18 -&gt; 58.58.58.58  TCP 2025 &gt; 1604 [SYN] Seq=0 Win=64240 Len=0 MSS=1460</code></pre></div><div id="comment-11134-info" class="comment-info"><span class="comment-age">(18 May '12, 03:18)</span> mastertu</div></div><span id="11135"></span><div id="comment-11135" class="comment not_top_scorer"><div id="post-11135-score" class="comment-score"></div><div class="comment-text"><p>sorry,the format hasn`t tab, can you give your email? I will send to your email,thans.</p></div><div id="comment-11135-info" class="comment-info"><span class="comment-age">(18 May '12, 03:20)</span> mastertu</div></div><span id="11136"></span><div id="comment-11136" class="comment not_top_scorer"><div id="post-11136-score" class="comment-score"></div><div class="comment-text"><p>I just updated the format, no worries :-)</p><p>I think I know the problem, are there any vlan tagged frames? The capture filter only shows non-tagged frames. To include vlan-tagged frames, you can use:</p><pre><code>tshark -nn -i eth1 -t ad -f &quot;(tcp[13]&amp;18=2 and not (dst net 192.168.0.0 mask 255.255.0.0)) or (vlan and (tcp[13]&amp;18=2 and not (dst net 192.168.0.0 mask 255.255.0.0)))&quot;</code></pre></div><div id="comment-11136-info" class="comment-info"><span class="comment-age">(18 May '12, 03:25)</span> SYN-bit ♦♦</div></div><span id="11138"></span><div id="comment-11138" class="comment not_top_scorer"><div id="post-11138-score" class="comment-score"></div><div class="comment-text"><p>yes, i have solve my question, thank you very much</p></div><div id="comment-11138-info" class="comment-info"><span class="comment-age">(18 May '12, 10:11)</span> mastertu</div></div><span id="11143"></span><div id="comment-11143" class="comment not_top_scorer"><div id="post-11143-score" class="comment-score"></div><div class="comment-text"><p>hi，this time， the tshark crashed agfer 18 hours. whether the memory inns`t enough? my host has 8G memory</p></div><div id="comment-11143-info" class="comment-info"><span class="comment-age">(19 May '12, 11:26)</span> mastertu</div></div><span id="11144"></span><div id="comment-11144" class="comment not_top_scorer"><div id="post-11144-score" class="comment-score"></div><div class="comment-text"><p>Running out of memory is inevitable as <code>tshark</code> accumulates information on each packet. You should instead be using <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html"><code>dumpcap</code></a> for long-running captures...</p></div><div id="comment-11144-info" class="comment-info"><span class="comment-age">(19 May '12, 15:03)</span> helloworld</div></div><span id="11145"></span><div id="comment-11145" class="comment not_top_scorer"><div id="post-11145-score" class="comment-score"></div><div class="comment-text"><p>...as described in the <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory#Work_Around.28s.29">OutOfMemory wiki</a>:</p><blockquote><h3 id="other-tools">Other tools</h3><p><br />
If Wireshark is running out of memory, that probably means that you're letting it run for a very long time or you're analyzing very large capture files. You may find that another tool does what you want better than Wireshark. Use <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> for long term capturing, it's intended for this purpose, or see <a href="http://wiki.wireshark.org/Tools">Tools</a> for other tools which may be more suitable for the task.</p></blockquote></div><div id="comment-11145-info" class="comment-info"><span class="comment-age">(19 May '12, 15:04)</span> helloworld</div></div><span id="11165"></span><div id="comment-11165" class="comment not_top_scorer"><div id="post-11165-score" class="comment-score"></div><div class="comment-text"><p>hi,i found another question, Please see the data,between 58.58.58.58 and TCP,there is two space But between the other dstip and TCP only has one space. I want make all of them one space, can you help me? Thank you.</p></div><div id="comment-11165-info" class="comment-info"><span class="comment-age">(20 May '12, 20:30)</span> mastertu</div></div><span id="11166"></span><div id="comment-11166" class="comment not_top_scorer"><div id="post-11166-score" class="comment-score"></div><div class="comment-text"><p>i delete the space by tr -s ' '</p></div><div id="comment-11166-info" class="comment-info"><span class="comment-age">(20 May '12, 21:07)</span> mastertu</div></div></div><div id="comment-tools-11097" class="comment-tools"><span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a></div><div class="clear"></div><div id="comment-11097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

