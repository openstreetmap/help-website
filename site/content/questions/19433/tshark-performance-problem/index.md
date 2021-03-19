+++
type = "question"
title = "Tshark performance problem"
description = '''I execute tshark command. Process is too slow. Sometimes take more than 6-7 seconds. Pcap file is really small (~500bytes). Actually strange thing is that re-execute same command consequently, process duration is decreasing dramatically (about 1 second). After wait for a while (without execution com...'''
date = "2013-03-13T02:32:00Z"
lastmod = "2013-03-13T06:06:00Z"
weight = 19433
keywords = [ "performance", "tshark" ]
aliases = [ "/questions/19433" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark performance problem](/questions/19433/tshark-performance-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19433-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I execute tshark command. Process is too slow. Sometimes take more than 6-7 seconds. Pcap file is really small (~500bytes). Actually strange thing is that re-execute same command consequently, process duration is decreasing dramatically (about 1 second). After wait for a while (without execution command), re-run same command and process completion duration increase again. Why process behave like that? How to solve this problem?</p><p>Command :</p><pre><code>tshark -ta -r test.pcap</code></pre><p>OS Details :</p><pre><code>SunOS er 5.10 Generic_147441-01 i86pc i386 i86pc</code></pre><p>Thanks</p></div><div id="question-tags" class="tags-container tags">performance tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '13, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/ffe99b05b3063ba35b43aeca99292479?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erdinc&#39;s gravatar image" /><p>erdinc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erdinc has no accepted answers">0%</span></p></div></div><div id="comments-container-19433" class="comments-container"></div><div id="comment-tools-19433" class="comment-tools"></div><div class="clear"></div><div id="comment-19433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19440"></span>

<div id="answer-container-19440" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19440-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Actually strange thing is that re-execute same command consequently, process duration is decreasing dramatically (about 1 second)</p></blockquote><p>That's most certainly due to DNS resolving. The seconds time it runs faster due to DNS caching. Please use option '-n' and tshark should run faster.</p><blockquote><p><code>tshark -ta -n -r test.pcap</code></p></blockquote><p>If that does not help try this:</p><blockquote><p><code>tshark -ta -r test.pcap -o name_resolve:FALSE</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '13, 04:31</p></div></div><div id="comments-container-19440" class="comments-container"><span id="19442"></span><div id="comment-19442" class="comment"><div id="post-19442-score" class="comment-score"></div><div class="comment-text"><p>Both of options does not solve my problem. Tshark behaviour is not changed.</p></div><div id="comment-19442-info" class="comment-info"><span class="comment-age">(13 Mar '13, 04:56)</span> erdinc</div></div><span id="19483"></span><div id="comment-19483" class="comment"><div id="post-19483-score" class="comment-score"></div><div class="comment-text"><p>what is you tshark version (tshark -v)?</p><p>Can you please add the output of the following command for the first call (long run time) and the second call (short run time)?</p><p>Case #1:<br />
</p><blockquote><p><code>truss -a -d -e -f -o /var/tmp/tshark_case1.out tshark -ta -r test.pcap</code><br />
</p></blockquote><p>Case #2:<br />
</p><blockquote><p><code>truss -a -d -e -f -o /var/tmp/tshark_case2.out tshark -ta -r test.pcap</code><br />
</p></blockquote><p>Please post the content of the files tshark_case1.out and tshark_case2.out somewhere.</p></div><div id="comment-19483-info" class="comment-info"><span class="comment-age">(13 Mar '13, 16:49)</span> Kurt Knochner ♦</div></div><span id="19925"></span><div id="comment-19925" class="comment"><div id="post-19925-score" class="comment-score"></div><div class="comment-text"><p>I did your test, Biggest differences is at brk function. brk function consume lots of time. Output files link is below. <a href="http://www.speedyshare.com/AwzRh/tshark.rar">http://www.speedyshare.com/AwzRh/tshark.rar</a> What is wrong about memory (brk), why brk need to time, how to resolve it?</p></div><div id="comment-19925-info" class="comment-info"><span class="comment-age">(29 Mar '13, 01:55)</span> erdinc</div></div><span id="20024"></span><div id="comment-20024" class="comment"><div id="post-20024-score" class="comment-score"></div><div class="comment-text"><p>As far as I know, brk() is used my malloc() to expand the programs heap. However, I have no idea why it takes that much longer in case #1 (first load) than in case #3 (second load).</p><p>Can you please post the output of the command 'limit' or 'ulimit -a' (whatever works)?</p></div><div id="comment-20024-info" class="comment-info"><span class="comment-age">(02 Apr '13, 10:08)</span> Kurt Knochner ♦</div></div><span id="20041"></span><div id="comment-20041" class="comment"><div id="post-20041-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ulimit -a<br />
<br />
core file size (blocks, -c) unlimited<br />
data seg size (kbytes, -d) unlimited<br />
file size (blocks, -f) unlimited<br />
open files (-n) 256<br />
pipe size (512 bytes, -p) 10<br />
stack size (kbytes, -s) 10240<br />
cpu time (seconds, -t) unlimited<br />
max user processes (-u) 27493<br />
virtual memory (kbytes, -v) unlimited<br />
</p></blockquote></div><div id="comment-20041-info" class="comment-info"><span class="comment-age">(03 Apr '13, 03:02)</span> erdinc</div></div><span id="20046"></span><div id="comment-20046" class="comment not_top_scorer"><div id="post-20046-score" class="comment-score"></div><div class="comment-text"><p>can you please try to increase the stack size (ulimit -s) and see if that changes anything?</p></div><div id="comment-20046-info" class="comment-info"><span class="comment-age">(03 Apr '13, 03:28)</span> Kurt Knochner ♦</div></div><span id="20051"></span><div id="comment-20051" class="comment not_top_scorer"><div id="post-20051-score" class="comment-score"></div><div class="comment-text"><p>I set stack size to 100.000 (increase 10 times), result is same.</p></div><div id="comment-20051-info" class="comment-info"><span class="comment-age">(03 Apr '13, 06:27)</span> erdinc</div></div><span id="20053"></span><div id="comment-20053" class="comment not_top_scorer"><div id="post-20053-score" class="comment-score"></div><div class="comment-text"><p>Hm.. looks like there is 'something' on your system that makes memory reallocation slow for the first time (brk calls) and faster for consecutive calls. Could be a specific behavior of the solaris memory management or just a specific behavior of your installation, like a large memory consumption on the system and thus swapping. Are there any processes that consume large amounts of memory (output of 'top' and 'swapon -s')?</p><p>I googled for slow brk() calls, but was unable to find something interesting. Can you please check my assumption about memory usage (above).</p></div><div id="comment-20053-info" class="comment-info"><span class="comment-age">(03 Apr '13, 07:02)</span> Kurt Knochner ♦</div></div><span id="20064"></span><div id="comment-20064" class="comment not_top_scorer"><div id="post-20064-score" class="comment-score"></div><div class="comment-text"><p>Yes, system use most of memory. 12 GB memory is installed. Top command says %63 percentage is used. Only one process is about half of total memory consuming. I observe similar behaviour at windows machine, I guess differences is not as big as at solaris</p></div><div id="comment-20064-info" class="comment-info"><span class="comment-age">(03 Apr '13, 10:11)</span> erdinc</div></div></div><div id="comment-tools-19440" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-19440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19445"></span>

<div id="answer-container-19445" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19445-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How much time a process takes is dependent on a lot of things. It looks like your initial tshark execution is taking more time because of disk IO. The second time you run tshark it will be faster since it will have cached things in memory. When you run tshark for the 3rd time after waiting a while, the cache will have flushed your data from cache and will need to re-read it from disk (or the network in case of NFS, iSCSI, etc).</p><p>You can check this by using the "time" utility, although I'm not sure what options you have with it on solaris. But on my OSX I get the following:</p><pre><code>$ /usr/bin/time -l tshark -ta -r bug4716.cap 
  1 14:41:28.843078     10.0.0.1 -&gt; 10.0.0.1     TCP 62 swrmi &gt; EtherNet-IP-1 [SYN] Seq=0 Win=65535 [TCP CHECKSUM INCORRECT] Len=0 MSS=1460 SACK_PERM=1
  2 14:41:29.169626     10.0.0.1 -&gt; 10.0.0.1     TCP 60 swrmi &gt; EtherNet-IP-1 [ACK] Seq=1 Ack=1 Win=65535 [TCP CHECKSUM INCORRECT] Len=0
  3 14:41:29.712539     10.0.0.1 -&gt; 10.0.0.1     TCP 93 swrmi &gt; EtherNet-IP-1 [PSH, ACK] Seq=1 Ack=1 Win=65535 [TCP CHECKSUM INCORRECT] Len=39
  4 14:41:30.203991     10.0.0.1 -&gt; 10.0.0.1     TCP 119 swrmi &gt; EtherNet-IP-1 [PSH, ACK] Seq=40 Ack=1 Win=65535 [TCP CHECKSUM INCORRECT] Len=65
  5 14:41:32.235725     10.0.0.1 -&gt; 10.0.0.1     TCP 60 swrmi &gt; EtherNet-IP-1 [PSH, ACK] Seq=105 Ack=2 Win=65534 [TCP CHECKSUM INCORRECT] Len=1
        1.21 real         0.22 user         0.20 sys
  88346624  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
     22420  page reclaims
         0  page faults
         0  swaps
        55  block input operations
        34  block output operations
         0  messages sent
         0  messages received
         0  signals received
       161  voluntary context switches
        21  involuntary context switches
$ /usr/bin/time -l tshark -ta -r bug4716.cap 
  1 14:41:28.843078     10.0.0.1 -&gt; 10.0.0.1     TCP 62 swrmi &gt; EtherNet-IP-1 [SYN] Seq=0 Win=65535 [TCP CHECKSUM INCORRECT] Len=0 MSS=1460 SACK_PERM=1
  2 14:41:29.169626     10.0.0.1 -&gt; 10.0.0.1     TCP 60 swrmi &gt; EtherNet-IP-1 [ACK] Seq=1 Ack=1 Win=65535 [TCP CHECKSUM INCORRECT] Len=0
  3 14:41:29.712539     10.0.0.1 -&gt; 10.0.0.1     TCP 93 swrmi &gt; EtherNet-IP-1 [PSH, ACK] Seq=1 Ack=1 Win=65535 [TCP CHECKSUM INCORRECT] Len=39
  4 14:41:30.203991     10.0.0.1 -&gt; 10.0.0.1     TCP 119 swrmi &gt; EtherNet-IP-1 [PSH, ACK] Seq=40 Ack=1 Win=65535 [TCP CHECKSUM INCORRECT] Len=65
  5 14:41:32.235725     10.0.0.1 -&gt; 10.0.0.1     TCP 60 swrmi &gt; EtherNet-IP-1 [PSH, ACK] Seq=105 Ack=2 Win=65534 [TCP CHECKSUM INCORRECT] Len=1
        0.56 real         0.22 user         0.19 sys
  88346624  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
     22420  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         2  block output operations
         0  messages sent
         0  messages received
         0  signals received
       106  voluntary context switches
       338  involuntary context switches
$</code></pre><p>Please note the block input/output operations and also the "involuntary context switches" which are caused by other processes (and which could contribute to extra load time if the system is heavily loaded).</p><p>As you can see, the sys and user time are about the same for both executions, but the real time differs because of time spent waiting on the disk and/or other processes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-19445" class="comments-container"><span id="19447"></span><div id="comment-19447" class="comment"><div id="post-19447-score" class="comment-score"></div><div class="comment-text"><p>I execute commands with time, my result is below. I can inference that slowness is not about tshark, because of slowness of computer. Is this assumption true? Another question (but not primarely important) Involuntary context switches can cause "real" time is big but waiting disc IO operations should be in "sys" time? real 2.6 user 0.1 sys 0.0</p></div><div id="comment-19447-info" class="comment-info"><span class="comment-age">(13 Mar '13, 06:43)</span> erdinc</div></div><span id="19453"></span><div id="comment-19453" class="comment"><div id="post-19453-score" class="comment-score"></div><div class="comment-text"><p>user and sys time only refer to time spent on the CPU, not time waiting on disk.</p><p>Have a look at <a href="http://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1">http://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1</a></p></div><div id="comment-19453-info" class="comment-info"><span class="comment-age">(13 Mar '13, 07:53)</span> SYN-bit ♦♦</div></div><span id="19456"></span><div id="comment-19456" class="comment"><div id="post-19456-score" class="comment-score"></div><div class="comment-text"><p>I checked with DTrace script that calculate system call duration (below link).Total sys call duration is less than 0.1 second but all process is completed in 5 seconds. If I am correct, this dtrace script accumulate all context swiches and I/O operation durations. There should be another reason why tshark is completed &gt;4 seconds.</p><p><a href="http://www.brendangregg.com/DTrace/procsystime">http://www.brendangregg.com/DTrace/procsystime</a></p></div><div id="comment-19456-info" class="comment-info"><span class="comment-age">(13 Mar '13, 08:25)</span> erdinc</div></div><span id="19482"></span><div id="comment-19482" class="comment"><div id="post-19482-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Pcap file is really small (~500bytes).</p></blockquote><p>disk I/O and context switches as problem source for a <strong>500 byte</strong> file? No way .. ;-))</p><p>There must be another reason, apparently some caching (DNS, filesystem, etc.)</p><p>@erdinc: Do you start tshark from an NFS mounted filesystem (@SYN-bit mentioned it)?</p></div><div id="comment-19482-info" class="comment-info"><span class="comment-age">(13 Mar '13, 16:39)</span> Kurt Knochner ♦</div></div><span id="19495"></span><div id="comment-19495" class="comment"><div id="post-19495-score" class="comment-score"></div><div class="comment-text"><p>There is no any NFS mounting point on my system. If it helps to identify problem, mysql server is running and heavily used disc. iostat tells that %b around %50.</p></div><div id="comment-19495-info" class="comment-info"><span class="comment-age">(14 Mar '13, 05:09)</span> erdinc</div></div><span id="19497"></span><div id="comment-19497" class="comment not_top_scorer"><div id="post-19497-score" class="comment-score"></div><div class="comment-text"><blockquote><p>disk I/O and context switches as problem source for a 500 byte file? No way .. ;-))</p></blockquote><p>Well, I was not worried about the 500 byte file :-), but was thinking about the tshark executable and access to all the supporting files...</p><p>That the disk is 50% busy seems OK, but how about the "wait" and "%w" columns?</p></div><div id="comment-19497-info" class="comment-info"><span class="comment-age">(14 Mar '13, 05:23)</span> SYN-bit ♦♦</div></div><span id="19501"></span><div id="comment-19501" class="comment not_top_scorer"><div id="post-19501-score" class="comment-score"></div><div class="comment-text"><p>wait("w") is always zero.</p></div><div id="comment-19501-info" class="comment-info"><span class="comment-age">(14 Mar '13, 06:05)</span> erdinc</div></div><span id="19692"></span><div id="comment-19692" class="comment not_top_scorer"><div id="post-19692-score" class="comment-score"></div><div class="comment-text"><p>can you please add the truss output? (see the comment in my answer)...</p></div><div id="comment-19692-info" class="comment-info"><span class="comment-age">(20 Mar '13, 11:13)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-19445" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-19445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

