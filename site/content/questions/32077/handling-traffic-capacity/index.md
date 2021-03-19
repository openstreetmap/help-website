+++
type = "question"
title = "handling traffic capacity"
description = '''how many traffic capacities wireshark can handle in a second?'''
date = "2014-04-22T22:54:00Z"
lastmod = "2014-04-22T23:49:00Z"
weight = 32077
keywords = [ "traffic", "capacity" ]
aliases = [ "/questions/32077" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [handling traffic capacity](/questions/32077/handling-traffic-capacity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32077-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how many traffic capacities wireshark can handle in a second?</p></div><div id="question-tags" class="tags-container tags">traffic capacity</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '14, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/885666c057a323159826c414b83eae37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fred&#39;s gravatar image" /><p>fred<br />
<span class="score" title="26 reputation points">26</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fred has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Apr '14, 01:33</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32077" class="comments-container"></div><div id="comment-tools-32077" class="comment-tools"></div><div class="clear"></div><div id="comment-32077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32081"></span>

<div id="answer-container-32081" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32081-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on the hardware wireshark is running on and the OS and version of the sport libraries. At Sharkfest '13 it was demonstrated that a windows laptop may be struggling at 100Mb/s, on a Ubuntu 13.10 with libpcap 1.5.x I managed close to 600Mb/s with dumpcap. Tcpdump did slightly better.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '14, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32081" class="comments-container"><span id="32091"></span><div id="comment-32091" class="comment"><div id="post-32091-score" class="comment-score"></div><div class="comment-text"><p>I deleted the comment by misstake... If you are doing a live capture with Wireshark I suspect it will manage less packets/s. As stated above your milage varies depending on HW, OS and SW level on that OS. To add insult to injury Wireshark will eventually run out of memory if run for a long time. Your Wireshark settings does also affect performance - like name resolution, update packets in real time, capture filters etc. So it's hard to give a straight answer.</p><p>(sport libraries, should read Support libraries, blaim T9)</p></div><div id="comment-32091-info" class="comment-info"><span class="comment-age">(23 Apr '14, 01:56)</span> Anders ♦</div></div><span id="32228"></span><div id="comment-32228" class="comment"><div id="post-32228-score" class="comment-score"></div><div class="comment-text"><p>hi,you say "on a Ubuntu 13.10 with libpcap 1.5.x I managed close to 600Mb/s with dumpcap", could you tell me your hardware list ? for example,mem size, disk size, number of interface,number of cpu core etc.</p></div><div id="comment-32228-info" class="comment-info"><span class="comment-age">(27 Apr '14, 19:02)</span> fred</div></div><span id="32244"></span><div id="comment-32244" class="comment"><div id="post-32244-score" class="comment-score"></div><div class="comment-text"><p>Now you should use Ubuntu 14.04 as that comes with libpcap 1.5.x</p><p>grep -c processor /proc/cpuinfo 12</p><p>/proc/cpuinfo processor : 0 vendor_id : GenuineIntel cpu family : 6 model : 45 model name : Intel(R) Xeon(R) CPU E5-2430 0 @ 2.20GHz stepping : 7 microcode : 0x70d cpu MHz : 2200.003 cache size : 15360 KB physical id : 0 siblings : 12 core id : 0 cpu cores : 6 apicid : 0 initial apicid : 0 fpu : yes fpu_exception : yes cpuid level : 13 wp : yes flags : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm ida arat xsaveopt pln pts dtherm tpr_shadow vnmi flexpriority ept vpid bogomips : 4400.00 clflush size : 64 cache_alignment : 64 address sizes : 46 bits physical, 48 bits virtual power management:</p><p>cat /proc/meminfo MemTotal: 24642912 kB</p></div><div id="comment-32244-info" class="comment-info"><span class="comment-age">(28 Apr '14, 03:50)</span> Anders ♦</div></div><span id="32276"></span><div id="comment-32276" class="comment"><div id="post-32276-score" class="comment-score"></div><div class="comment-text"><p>your os Ubuntu 14.04 is desktop or server? Usually i use SUSE server,especial SUSE11SP1, can SUSE have the same handling capacity as your Ubuntu 14.04?</p></div><div id="comment-32276-info" class="comment-info"><span class="comment-age">(28 Apr '14, 18:13)</span> fred</div></div><span id="32282"></span><div id="comment-32282" class="comment"><div id="post-32282-score" class="comment-score"></div><div class="comment-text"><p>If it has the same wireshark and Libpcap versions I don't see why not. Kernel version might make a difference too but not that I'm aware of. Server or desktop differences i don't know either.</p></div><div id="comment-32282-info" class="comment-info"><span class="comment-age">(28 Apr '14, 20:58)</span> Anders ♦</div></div><span id="32283"></span><div id="comment-32283" class="comment not_top_scorer"><div id="post-32283-score" class="comment-score"></div><div class="comment-text"><p>thanks,i will check it</p></div><div id="comment-32283-info" class="comment-info"><span class="comment-age">(28 Apr '14, 22:02)</span> fred</div></div></div><div id="comment-tools-32081" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-32081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

