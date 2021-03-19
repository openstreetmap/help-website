+++
type = "question"
title = "Getting Tshark up to wire speed for NFS packet captures"
description = '''I am trying to use tshark for reassembling and extracting NFS payloads. Because of the large amount of data I am processing (and some security concerns) I can not do this processing offline so I am trying to get tshark to run at or as close to wire speed as possible. I initially tried using tshark t...'''
date = "2012-12-05T14:11:00Z"
lastmod = "2012-12-05T16:09:00Z"
weight = 16613
keywords = [ "performance" ]
aliases = [ "/questions/16613" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting Tshark up to wire speed for NFS packet captures](/questions/16613/getting-tshark-up-to-wire-speed-for-nfs-packet-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16613-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use tshark for reassembling and extracting NFS payloads. Because of the large amount of data I am processing (and some security concerns) I can not do this processing offline so I am trying to get tshark to run at or as close to wire speed as possible. I initially tried using tshark to do the packet capture but it was dropping too many packets so I am using another pcap based tool to do the packet capture (and successfully capturing and writing packets at wire speed) and then I am piping the output of tshark to another process that does processing on the payloads. So the whole setup looks something like this:</p><p>pcap-packet-capture-tool | tshark -i - -n -T fields -e nfs.data | my_program</p><p>In my experiments, I have seen that tshark significantly lags wire speed (1 Gb/s). It's actual rate is roughly 25 MB/s and this lag manifests itself by tshark taking extra time after the packet capture is complete to finish at roughly the rate of 1 to 1 ie. if I do a packet capture for 30 minutes, it will take tshark a total of an hour to finish.</p><p>I have looked into trying to speed it up myself by not converting the data into hex representations and just printing the binary but the improvements were marginal. For more significant performance improvements I would either need a better understanding of the code (to know what to adjust/strip off) or perhaps I am missing some crucial parameters that will significantly speed tshark up. Please let me know if you have any suggestions on either front. I would also be happy to provide any extra information if this is not enough to troubleshoot the issue.</p><p>I should add, this is running in a virtualized linux environment with a relatively modern/ powerful server and I have already disabled host look up (as I know that can significantly slow down packet captures).<br />
</p><p>Thanks you!</p><p>UPDATE: Thank you for the quick responses. Below are some clarifications.</p><ol><li>The testing that I've done to find the speed of tshark were not in the full setup. I am writing the pcap to tshark with dd and letting tshark write it's output to /dev/null so there are no external limiting factors. The note above about tshark going at 25 MB/s is from the isolated tests, not the full setup. I just added those details in case there is some slowdown when capturing on the stdin interface or writing to stdout.<br />
</li><li>The pcap tool is tcpdump with pfring.</li><li>I have looked at top and vmstat while it runs. It uses up to 1 GB of ram and 100% cpu. tshark is single threaded so it's only taking up 1 of the 4 cores.</li><li>I do run tshark with -n, I just omitted it above. I am re-adding it now.</li></ol><p>Update 2: I added my own benchmarks in an answer.</p><p>Update 3: I have used the tshark that gets installed with apt-get and I have built the latest myself. apt-get gives you 1.8.2 and the one I built is 1.8.4. The results from both are similar. I am running it in Ubuntu 12.10 VM running in VMWare fusion on OS X Mountain Lion. It's a macbook air with i7 processor, 8 GB of ram. The VM has 3GB of ram and 4 vCPUs.<br />
</p><pre><code>$ ./tshark -v
TShark 1.8.4 (SVN Rev Unknown from unknown)

Copyright 1998-2012 Gerald Combs &lt;[email protected]wireshark.org&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GLib 2.34.0, with libpcap, with libz 1.2.7, without POSIX
capabilities, without SMI, without c-ares, without ADNS, without Lua, without
Python, without GnuTLS, without Gcrypt, without Kerberos, without GeoIP.

Running on Linux 3.5.0-19-generic, with locale en_US.UTF-8, with libpcap version
1.3.0, with libz 1.2.7.

Built using gcc 4.7.2.

$ tshark -v
TShark 1.8.2

Copyright 1998-2012 Gerald Combs &lt;[email protected]wireshark.org&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GLib 2.34.0, with libpcap, with libz 1.2.7, with POSIX
capabilities (Linux), with SMI 0.4.8, with c-ares 1.9.1, with Lua 5.1, without
Python, with GnuTLS 2.12.14, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP.

Running on Linux 3.5.0-19-generic, with locale en_US.UTF-8, with libpcap version
1.3.0, with libz 1.2.7.

Built using gcc 4.7.2.

$ uname -a
Linux ubuntu 3.5.0-19-generic #30-Ubuntu SMP Tue Nov 13 17:48:01 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux</code></pre></div><div id="question-tags" class="tags-container tags">performance</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/08f0b2e3262cfb486306c28a042948f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="notorious-pcaper&#39;s gravatar image" /><p>notorious-pc...<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="notorious-pcaper has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Dec '12, 10:05</p></div></div><div id="comments-container-16613" class="comments-container"><span id="16648"></span><div id="comment-16648" class="comment"><div id="post-16648-score" class="comment-score"></div><div class="comment-text"><p>If you are building from source you are better off building from trunk, checking out from svn. In that way you get access to the latest improvments if any. Building a profiling build might help(I don't know how to do that) finding out where the bottleneck is.</p></div><div id="comment-16648-info" class="comment-info"><span class="comment-age">(06 Dec '12, 11:14)</span> Anders ♦</div></div></div><div id="comment-tools-16613" class="comment-tools"></div><div class="clear"></div><div id="comment-16613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16618"></span>

<div id="answer-container-16618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16618-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Some questions/suggestions:</p><ul><li>What is your pcap-packet-capture-tool?</li><li>How do you know that this tool is not the limiting factor? Did you measure it's performance with cpipe?</li></ul><blockquote><p><code>pcap-packet-capture-tool | cpipe -vt &gt; /dev/null</code><br />
</p></blockquote><ul><li>decoding the whole traffic will take a lot of resources. Did you check the resource usage of tshark while it is running? (top, vmstat, atop, etc.)</li><li>How do you know that your program (my_program) is not the limiting factor? What happens if you run this:</li></ul><blockquote><p><code>pcap-packet-capture-tool | tshark -i - -T fields -e nfs.data &gt; /dev/null</code><br />
</p></blockquote><ul><li>the pipe buffer size is limited. If one process fills it up fast and the other is not reading fast enough, the first process might block.</li></ul><blockquote><p>and I have already disabled host look up</p></blockquote><p>You did not use the option <code>-n</code> with tshark (at least not in your example above). Please try that.</p><p><strong>UPDATE</strong></p><p>replying to your update in the question.</p><p>I did some test with dd and the buffer size and that is a crucial factor.</p><p>dd with default buffer size (you did not mention your buffer size for dd!!)</p><pre><code>dd if=http_250.cap | cpipe -b 1024 -vt &gt; /dev/null 
thru: 320.396ms at    3.1MB/s (   3.1MB/s avg) 1024.0kB
thru: 302.170ms at    3.3MB/s (   3.2MB/s avg)    2.0MB
thru: 304.235ms at    3.3MB/s (   3.2MB/s avg)    3.0MB
thru: 300.765ms at    3.3MB/s (   3.3MB/s avg)    4.0MB</code></pre><p>That's pretty slow! The buffer of dd is to small.</p><p>Now cat.</p><pre><code>cat http_250.cap | cpipe -b 1024 -vt &gt; /dev/null 
thru:   5.004ms at  199.8MB/s ( 199.8MB/s avg) 1024.0kB
thru:   5.092ms at  196.4MB/s ( 196.9MB/s avg)    2.0MB
thru:   5.027ms at  198.9MB/s ( 197.3MB/s avg)    3.0MB
thru:   5.188ms at  192.8MB/s ( 195.8MB/s avg)    4.0MB</code></pre><p>That's much better.</p><p>Now dd with a decent buffer size.</p><pre><code>dd bs=512000 if=http_250.cap | cpipe -b 1024 -vt &gt; /dev/null 
thru:   2.006ms at  498.5MB/s ( 498.5MB/s avg) 1024.0kB
thru:   0.743ms at    1.3GB/s ( 714.5MB/s avg)    2.0MB
thru:   0.759ms at    1.3GB/s ( 813.0MB/s avg)    3.0MB
thru:   0.708ms at    1.4GB/s ( 897.1MB/s avg)    4.0MB
thru:   0.717ms at    1.4GB/s ( 955.7MB/s avg)    5.0MB
thru:   0.725ms at    1.3GB/s ( 995.2MB/s avg)    6.0MB
thru:   0.723ms at    1.4GB/s (   1.0GB/s avg)    7.0MB
thru:   0.739ms at    1.3GB/s (   1.0GB/s avg)    8.0MB</code></pre><p>nearly 1 GByte/s (avg). That's not bad :-)</p><p><strong>HINT</strong>: This is <strong>obviously</strong> using the filesystem cache of Linux. My SSD is only capable of reading with at max. speed of 400-500 MByte/s (specs and measured).</p><p>now, let's bring in tshark.</p><pre><code>dd bs=512000 if=http_250.cap | cpipe -b 1024 -vt | tshark -ni - &gt; /dev/null 
Capturing on Standard input
thru:   4.809ms at  207.9MB/s (  90.7MB/s avg)   41.0MB
thru:   5.187ms at  192.8MB/s (  91.8MB/s avg)   42.0MB
thru:   5.586ms at  179.0MB/s (  92.9MB/s avg)   43.0MB
thru:   5.552ms at  180.1MB/s (  93.9MB/s avg)   44.0MB
thru:   9.280ms at  107.8MB/s (  94.1MB/s avg)   45.0MB
thru:  17.993ms at   55.6MB/s (  92.7MB/s avg)   46.0MB</code></pre><p>O.K. that's odd. Only 10% of the input stream, but still fast enough for a 1 GBit/s link, as the output of cpipe is in Byte/s, so it's ~90 MByte/s.</p><p>Now tshark filtering on only some fields:</p><pre><code>dd bs=512000 if=http_250.cap | cpipe -b 1024 -vt | tshark -ni - -T fields -e tcp.port &gt; /dev/null 
Capturing on Standard input
thru:   5.584ms at  179.1MB/s ( 109.4MB/s avg)  125.0MB
thru:   5.746ms at  174.0MB/s ( 109.7MB/s avg)  126.0MB
thru:   7.830ms at  127.7MB/s ( 109.8MB/s avg)  127.0MB
thru:   6.039ms at  165.6MB/s ( 110.1MB/s avg)  128.0MB
thru:   5.836ms at  171.4MB/s ( 110.4MB/s avg)  129.0MB
thru:   7.159ms at  139.7MB/s ( 110.6MB/s avg)  130.0MB
thru: 193.072ms at    5.2MB/s (  95.7MB/s avg)  131.0MB
thru:   5.408ms at  184.9MB/s (  96.0MB/s avg)  132.0MB
thru:   5.573ms at  179.4MB/s (  96.4MB/s avg)  133.0MB
thru:   5.702ms at  175.4MB/s (  96.7MB/s avg)  134.0MB
thru:   6.357ms at  157.3MB/s (  97.0MB/s avg)  135.0MB
thru:   6.004ms at  166.6MB/s (  97.3MB/s avg)  136.0MB</code></pre><p>O.K, a bit better, with a (avg) peak up to 110 MByte/s.</p><p>So, why is your tshark not that fast? I did my test in a VMware on a laptop. The file is on a real fast SSD (400 MByte/s). HOWEVER, I used just <strong>http</strong> traffic.</p><p>There is a pretty good chance, that the NFS dissector consumes much more resources, and thus it is so much slower. As I don't have a large NFS capture file, I cannot test it. However, you can test your environment with a large http capture file (easy to create). Then compare your results with mine. If tshark is still much slower, then it's related to your system (CPU, I/O, etc.) or to the tshark version (mine: 1.8.3 on Ubuntu 12.04). If your system is much faster with http, then it's the NFS dissector and there is probably nothing you can do, except speeding up the dissector by improving the code or by using an even faster system (CPU) ;-)</p><p>BTW: If you run tshark for a long time at a high data rate, it will build up internal state (hash tables, lists, etc.) and it will become slower over time, as it takes longer to add/extract data to those data structures!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 16:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16618" class="comments-container"><span id="16638"></span><div id="comment-16638" class="comment"><div id="post-16638-score" class="comment-score"></div><div class="comment-text"><p>So I did your set of tests to see how I compare. I have them below. In short, it seems my system's capabilities are similar to yours but when I add in tshark it's much slower. I think my pcap is a bit smaller (50MB) but I don't think that should make a this huge of a difference.</p><p>Writing with dd with no block size specified is quite faster for me.</p><pre><code>$ dd if=../../pcap/http-50MB.pcap | cpipe -b 1024 -vt &gt; /dev/null 
thru:   9.865ms at  101.4MB/s ( 101.4MB/s avg) 1024.0kB
thru:   4.987ms at  200.5MB/s ( 133.8MB/s avg)    2.0MB
thru:   2.256ms at  443.3MB/s ( 173.5MB/s avg)    3.0MB
thru:  22.243ms at   45.0MB/s ( 100.9MB/s avg)    4.0MB
thru:  22.767ms at   43.9MB/s (  80.0MB/s avg)    5.0MB
thru:  15.571ms at   64.2MB/s (  76.4MB/s avg)    6.0MB
thru:  16.805ms at   59.5MB/s (  73.4MB/s avg)    7.0MB
thru:  10.056ms at   99.4MB/s (  75.8MB/s avg)    8.0MB
thru:  10.396ms at   96.2MB/s (  77.5MB/s avg)    9.0MB
thru:  21.253ms at   47.1MB/s (  72.8MB/s avg)   10.0MB</code></pre><p>Using a bigger block size anyway:</p><pre><code>$ dd bs=512k if=../../pcap/http-50MB.pcap | cpipe -b 1024 -vt  &gt; /dev/null
thru:   3.327ms at  300.6MB/s ( 300.6MB/s avg) 1024.0kB
thru:   2.213ms at  451.9MB/s ( 350.1MB/s avg)    2.0MB
thru:   2.240ms at  446.4MB/s ( 369.9MB/s avg)    3.0MB
thru:   3.805ms at  262.8MB/s ( 330.7MB/s avg)    4.0MB
thru:   2.395ms at  417.5MB/s ( 343.1MB/s avg)    5.0MB
thru:   2.467ms at  405.4MB/s ( 347.7MB/s avg)    6.0MB
thru:   1.602ms at  624.2MB/s ( 370.2MB/s avg)    7.0MB
thru:   1.528ms at  654.5MB/s ( 388.9MB/s avg)    8.0MB
thru:   1.135ms at  881.1MB/s ( 412.3MB/s avg)    9.0MB
thru:   1.065ms at  939.0MB/s ( 435.3MB/s avg)   10.0MB</code></pre><p>Ok, that's pretty slow, but still above wire speed. Also, looking later in the process (MB 38 and on)</p><pre><code>thru:   0.931ms at    1.0GB/s ( 694.1MB/s avg)   38.0MB
thru:   0.798ms at    1.2GB/s ( 701.6MB/s avg)   39.0MB
thru:   0.933ms at    1.0GB/s ( 707.1MB/s avg)   40.0MB
thru:   0.822ms at    1.2GB/s ( 714.0MB/s avg)   41.0MB
thru:   0.587ms at    1.7GB/s ( 723.6MB/s avg)   42.0MB
thru:   0.636ms at    1.5GB/s ( 732.5MB/s avg)   43.0MB
thru:   0.755ms at    1.3GB/s ( 739.8MB/s avg)   44.0MB
thru:   0.758ms at    1.3GB/s ( 746.7MB/s avg)   45.0MB
thru:   0.667ms at    1.5GB/s ( 754.5MB/s avg)   46.0MB
thru:   0.745ms at    1.3GB/s ( 761.2MB/s avg)   47.0MB
thru:   0.832ms at    1.2GB/s ( 766.7MB/s avg)   48.0MB</code></pre><p>That's pretty comprable to your results. Here comes tshark:</p><pre><code>$ dd bs=512k if=../../pcap/http-50MB.pcap | cpipe -b 1024 -vt | ./tshark -ni - &gt; /dev/null
Capturing on Standard input
thru: 222.728ms at    4.5MB/s (   4.5MB/s avg) 1024.0kB
thru:  16.554ms at   60.4MB/s (   8.4MB/s avg)    2.0MB
thru:  12.820ms at   78.0MB/s (  11.9MB/s avg)    3.0MB
thru:  19.805ms at   50.5MB/s (  14.7MB/s avg)    4.0MB
thru:  14.044ms at   71.2MB/s (  17.5MB/s avg)    5.0MB
thru:  14.296ms at   69.9MB/s (  19.9MB/s avg)    6.0MB
thru:  16.266ms at   61.5MB/s (  22.1MB/s avg)    7.0MB
thru:  10.686ms at   93.6MB/s (  24.4MB/s avg)    8.0MB
thru:   9.888ms at  101.1MB/s (  26.6MB/s avg)    9.0MB
thru:  19.367ms at   51.6MB/s (  28.0MB/s avg)   10.0MB
thru:  19.538ms at   51.2MB/s (  29.2MB/s avg)   11.0MB
thru:  19.455ms at   51.4MB/s (  30.3MB/s avg)   12.0MB
thru:  12.148ms at   82.3MB/s (  31.8MB/s avg)   13.0MB
thru:  15.142ms at   66.0MB/s (  33.0MB/s avg)   14.0MB
...
thru:  19.875ms at   50.3MB/s (  44.0MB/s avg)   37.0MB
thru:  18.174ms at   55.0MB/s (  44.2MB/s avg)   38.0MB
thru:  42.073ms at   23.8MB/s (  43.3MB/s avg)   39.0MB
thru:  27.417ms at   36.5MB/s (  43.1MB/s avg)   40.0MB
thru:  33.191ms at   30.1MB/s (  42.6MB/s avg)   41.0MB
thru:   9.252ms at  108.1MB/s (  43.3MB/s avg)   42.0MB
thru:  15.505ms at   64.5MB/s (  43.6MB/s avg)   43.0MB
thru:   8.617ms at  116.0MB/s (  44.2MB/s avg)   44.0MB
thru:  11.868ms at   84.3MB/s (  44.7MB/s avg)   45.0MB
thru:  34.991ms at   28.6MB/s (  44.1MB/s avg)   46.0MB
thru:  18.417ms at   54.3MB/s (  44.3MB/s avg)   47.0MB
thru:  28.615ms at   34.9MB/s (  44.1MB/s avg)   48.0MB</code></pre><p>Similar situation with the fields:</p><pre><code>$ dd bs=512k if=../../pcap/http-50MB.pcap | cpipe -b 1024 -vt | ./tshark -ni - -T fields -e tcp.port&gt; /dev/null
Capturing on Standard input
thru: 205.944ms at    4.9MB/s (   4.9MB/s avg) 1024.0kB
thru:  10.363ms at   96.5MB/s (   9.2MB/s avg)    2.0MB
thru:  12.774ms at   78.3MB/s (  13.1MB/s avg)    3.0MB
thru:  10.068ms at   99.3MB/s (  16.7MB/s avg)    4.0MB
thru:   7.983ms at  125.3MB/s (  20.2MB/s avg)    5.0MB
thru:   8.106ms at  123.4MB/s (  23.4MB/s avg)    6.0MB
thru:   9.250ms at  108.1MB/s (  26.4MB/s avg)    7.0MB
thru:   8.799ms at  113.6MB/s (  29.2MB/s avg)    8.0MB
thru:   9.492ms at  105.4MB/s (  31.7MB/s avg)    9.0MB
thru:  13.729ms at   72.8MB/s (  33.6MB/s avg)   10.0MB
thru:  21.893ms at   45.7MB/s (  34.4MB/s avg)   11.0MB
thru:   8.379ms at  119.3MB/s (  36.6MB/s avg)   12.0MB
thru:  11.659ms at   85.8MB/s (  38.3MB/s avg)   13.0MB
thru:  17.193ms at   58.2MB/s (  39.2MB/s avg)   14.0MB
thru:  13.114ms at   76.3MB/s (  40.5MB/s avg)   15.0MB
...
thru:  17.869ms at   56.0MB/s (  51.3MB/s avg)   36.0MB
thru:  11.028ms at   90.7MB/s (  51.9MB/s avg)   37.0MB
thru:  10.326ms at   96.8MB/s (  52.6MB/s avg)   38.0MB
thru:  13.916ms at   71.9MB/s (  52.9MB/s avg)   39.0MB
thru:   8.701ms at  114.9MB/s (  53.6MB/s avg)   40.0MB
thru:   8.585ms at  116.5MB/s (  54.4MB/s avg)   41.0MB
thru:  15.419ms at   64.9MB/s (  54.6MB/s avg)   42.0MB
thru:  24.169ms at   41.4MB/s (  54.2MB/s avg)   43.0MB
thru:  24.658ms at   40.6MB/s (  53.7MB/s avg)   44.0MB
thru:  19.379ms at   51.6MB/s (  53.7MB/s avg)   45.0MB
thru:  19.207ms at   52.1MB/s (  53.7MB/s avg)   46.0MB
thru:  16.235ms at   61.6MB/s (  53.8MB/s avg)   47.0MB
thru:  13.310ms at   75.1MB/s (  54.1MB/s avg)   48.0MB</code></pre><p>Interestingly, it goes the same speed for NFS reassembly so it seems that whatever is making my tshark slow should also help with the NFS case. Do you have any thoughts on what might cause this (about 2x) slowdown? Do you need more explicit details about my system/ setup to have a better idea of where to start looking?</p><p>Thanks again.</p></div><div id="comment-16638-info" class="comment-info"><span class="comment-age">(06 Dec '12, 08:26)</span> notorious-pc...</div></div><span id="16640"></span><div id="comment-16640" class="comment"><div id="post-16640-score" class="comment-score"></div><div class="comment-text"><p>what is your tshark version? Please post the output of.</p><blockquote><p><code>tshark -v</code><br />
</p></blockquote><p>What is your OS version?</p><blockquote><p>Do you need more explicit details about my system/ setup to have a better idea of where to start looking?</p></blockquote><p>Yes, every detail you can give (e.g. VMware Version, Host OS version, virtual OS version, etc.) may help.</p><p>BTW: I converted your answer to a comment, as that's how this site works.</p></div><div id="comment-16640-info" class="comment-info"><span class="comment-age">(06 Dec '12, 09:14)</span> Kurt Knochner ♦</div></div><span id="16651"></span><div id="comment-16651" class="comment"><div id="post-16651-score" class="comment-score"></div><div class="comment-text"><p>Upon some further investigation I was able to get tshark to read in data up to 200 MB/s with a VM with 32 GB of RAM. This showed that the throughput measurement is not accurate because tshark will continue to run after it has read everything and finish reassembly much later. For example, I fed tshark a 1GB pcap which it consumed in 5 seconds (probably buffering most of it) but tshark actually runs for 3 minutes so if you average that 1GB over 180 seconds it's actually more like 5MB/s.</p></div><div id="comment-16651-info" class="comment-info"><span class="comment-age">(06 Dec '12, 11:23)</span> notorious-pc...</div></div></div><div id="comment-tools-16618" class="comment-tools"></div><div class="clear"></div><div id="comment-16618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

