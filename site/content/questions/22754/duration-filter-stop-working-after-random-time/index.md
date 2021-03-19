+++
type = "question"
title = "Duration filter stop working after random time"
description = '''Hi ! Sorry for bad english :/ I&#x27;m using Dumpcap in command line with different parameters... sudo nohup dumpcap -P -f &quot;((src 192.1.1.80 and port 25340) and (dst 192.1.1.20 and port 21286)) or   ((src 192.1.1.84 and port 25596) and (dst 192.1.1.20 and port 21288)) or   ((src 192.1.1.47 and port 80) a...'''
date = "2013-07-09T06:19:00Z"
lastmod = "2013-07-15T01:37:00Z"
weight = 22754
keywords = [ "duration", "buffer", "dumpcap" ]
aliases = [ "/questions/22754" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Duration filter stop working after random time](/questions/22754/duration-filter-stop-working-after-random-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22754-score" class="post-score" title="current number of votes">0</div><span id="post-22754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi !</p><p>Sorry for bad english :/ I'm using Dumpcap in command line with different parameters...</p><pre><code>sudo nohup dumpcap -P -f &quot;((src 192.1.1.80 and port 25340) and (dst 192.1.1.20 and port 21286)) or 
    ((src 192.1.1.84 and port 25596) and (dst 192.1.1.20 and port 21288)) or 
    ((src 192.1.1.47 and port 80) and (dst 192.1.1.31 and port 80)) or 
    ((src 192.1.1.31 and port 80) and (dst 192.1.1.47 and port 80)) or 
    ((src 192.1.1.47 and port 22) and (dst 192.1.1.31 and port 22)) or 
    ((src 192.1.1.31 and port 22) and (dst 192.1.1.47 and port 22))&quot; 
    -b duration:600 -i eth0 -w /mnt/hdd/tsar_files_to_proceed/REC.pcap &gt; /dev/null &amp;</code></pre><p>So, this command contains lot of filter, anyway, it's not the problem. This problem is the " -b duration:600" part.</p><p>Sometimes, dumpcap can listen the network a whole day without any bug, and the next day, it stops spliting files after few hours...</p><p>I notice that too: When dumpcap splits the file after long random period (during the "bug")... The command crash, we can see it running with "top" command but... not working anymore</p><blockquote><p>dumpcap -v Dumpcap 1.8.2</p><p>Copyright 1998-2012 Gerald Combs <span><span class="__cf_email__" data-cfemail="8ee9ebfcefe2eacef9e7fcebfde6effce5a0e1fce9">[email protected]</span></span> and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (32-bit) with GLib 2.32.4, with libpcap, with libz 1.2.7, with POSIX capabilities (Linux).</p><p>Running on Linux 3.6.11+, with locale fr_FR.UTF-8, with libpcap version 1.3.0, with libz 1.2.7.</p><p>Built using gcc 4.6.3.</p></blockquote><p>Running on Raspbian Wheezy</p><p>Thank's for helping ! Have a good day !</p><p>Vincent.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-buffer" rel="tag" title="see questions tagged &#39;buffer&#39;">buffer</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/02f48a963f183d550567946439383ef8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FriZBy76&#39;s gravatar image" /><p><span>FriZBy76</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FriZBy76 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jul '13, 06:48</strong> </span></p></div></div><div id="comments-container-22754" class="comments-container"><span id="22755"></span><div id="comment-22755" class="comment"><div id="post-22755-score" class="comment-score"></div><div class="comment-text"><p>Which version of dumpcap are you using and which OS version?</p></div><div id="comment-22755-info" class="comment-info"><span class="comment-age">(09 Jul '13, 06:44)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="22756"></span><div id="comment-22756" class="comment"><div id="post-22756-score" class="comment-score"></div><div class="comment-text"><p>dumpcap 1.8.2 running on Raspbian Wheezy ( Edited :) )</p></div><div id="comment-22756-info" class="comment-info"><span class="comment-age">(09 Jul '13, 06:48)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22759"></span><div id="comment-22759" class="comment"><div id="post-22759-score" class="comment-score"></div><div class="comment-text"><p>are you sure the filesystem is not filled up with capture files and that's the reason why it stops working?</p></div><div id="comment-22759-info" class="comment-info"><span class="comment-age">(09 Jul '13, 06:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22760"></span><div id="comment-22760" class="comment"><div id="post-22760-score" class="comment-score"></div><div class="comment-text"><p>Sure ! Files are writen on an external drive (8GB, 5,5GB Free !) and this phenomenon is tottaly random... I don't understand</p></div><div id="comment-22760-info" class="comment-info"><span class="comment-age">(09 Jul '13, 06:57)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22793"></span><div id="comment-22793" class="comment"><div id="post-22793-score" class="comment-score"></div><div class="comment-text"><p>Ok, I start a capture. Waiting the bug ^^' ...</p></div><div id="comment-22793-info" class="comment-info"><span class="comment-age">(10 Jul '13, 02:50)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22796"></span><div id="comment-22796" class="comment not_top_scorer"><div id="post-22796-score" class="comment-score"></div><div class="comment-text"><p>please let strace run for 10-30 seconds!</p><p>BTW: here is an update to the lsof command:</p><blockquote><p><code>lsof -n | grep dumpcap</code><br />
<code>lsof -n | grep wireshark</code></p></blockquote><p>BTW: Are there any messages in the output of <strong>dmesg</strong> about the mounted disk?</p></div><div id="comment-22796-info" class="comment-info"><span class="comment-age">(10 Jul '13, 03:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22894"></span><div id="comment-22894" class="comment not_top_scorer"><div id="post-22894-score" class="comment-score"></div><div class="comment-text"><p>Se my new answer...Comment are restricted, the response command is to long =)</p></div><div id="comment-22894-info" class="comment-info"><span class="comment-age">(12 Jul '13, 02:08)</span> <span class="comment-user userinfo">FriZBy76</span></div></div></div><div id="comment-tools-22754" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-22754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22761"></span>

<div id="answer-container-22761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22761-score" class="post-score" title="current number of votes">1</div><span id="post-22761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7423">bug 7423</a>, could you try the latest 1.8 (1.8.8) or 1.10 (1.10.0) release?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '13, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jul '13, 06:58</strong> </span></p></div></div><div id="comments-container-22761" class="comments-container"><span id="22763"></span><div id="comment-22763" class="comment"><div id="post-22763-score" class="comment-score"></div><div class="comment-text"><p>Trying it I'll start a capture and come back here to tell you what happen</p></div><div id="comment-22763-info" class="comment-info"><span class="comment-age">(09 Jul '13, 07:04)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22792"></span><div id="comment-22792" class="comment"><div id="post-22792-score" class="comment-score"></div><div class="comment-text"><p>I can't build Wireshark 1.10 i've got some errors... I lose my morning trying it :(</p></div><div id="comment-22792-info" class="comment-info"><span class="comment-age">(10 Jul '13, 02:49)</span> <span class="comment-user userinfo">FriZBy76</span></div></div></div><div id="comment-tools-22761" class="comment-tools"></div><div class="clear"></div><div id="comment-22761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22789"></span>

<div id="answer-container-22789" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22789-score" class="post-score" title="current number of votes">0</div><span id="post-22789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can you please run these commands, while the problem occurs, and then post the output here?</p><blockquote><p>lsof -ni | grep -i dumpcap<br />
lsof -ni | grep -i wireshark</p></blockquote><p>Also this:</p><blockquote><p>The command crash, we can see it running with "top" command but... not working anymore</p></blockquote><p>If the system is in this state, please get the PID of dumpcap and wireshark and run strace on both.</p><blockquote><p>strace -r -tt -v -s 1024 -f -o /var/tmp/dumpcap.trace -p PID_OF_DUMPCAP</p></blockquote><p>Then post the files /var/tmp/*.trace here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jul '13, 03:09</strong> </span></p></div></div><div id="comments-container-22789" class="comments-container"><span id="22895"></span><div id="comment-22895" class="comment"><div id="post-22895-score" class="comment-score"></div><div class="comment-text"><p>So :</p><pre><code>lsof -n | grep dumpcap</code></pre><blockquote><p>dumpcap 19259 root cwd DIR 179,2 4096 131224 /var/www/command/tshark dumpcap<br />
19259 root rtd DIR<br />
179,2 4096 2 / dumpcap<br />
19259 root txt REG<br />
179,2 71168 67417 /usr/bin/dumpcap dumpcap 19259<br />
root mem REG 0,6<br />
41184 socket:[41184] (stat: No such file or directory) dumpcap 19259<br />
root mem REG 179,2<br />
9812 1893 /lib/arm-linux-gnueabihf/libdl-2.13.so dumpcap 19259 root mem<br />
REG 179,2 17904 1819 /lib/arm-linux-gnueabihf/libattr.so.1.1.0 dumpcap 19259 root mem<br />
REG 179,2 131372 1247 /lib/arm-linux-gnueabihf/libgcc_s.so.1 dumpcap 19259 root mem<br />
REG 179,2 233000 10657 /lib/arm-linux-gnueabihf/libpcre.so.3.13.1 dumpcap 19259 root mem<br />
REG 179,2 26632 1892 /lib/arm-linux-gnueabihf/librt-2.13.so dumpcap 19259 root mem<br />
REG 179,2 13828 76593 /usr/lib/arm-linux-gnueabihf/libgmodule-2.0.so.0.3200.4 dumpcap 19259 root mem<br />
REG 179,2 5484 76592 /usr/lib/arm-linux-gnueabihf/libgthread-2.0.so.0.3200.4 dumpcap 19259 root mem<br />
REG 179,2 1196144 1891 /lib/arm-linux-gnueabihf/libc-2.13.so dumpcap 19259 root mem<br />
REG 179,2 116462 1888 /lib/arm-linux-gnueabihf/libpthread-2.13.so dumpcap 19259 root mem<br />
REG 179,2 87792 5150 /lib/arm-linux-gnueabihf/libz.so.1.2.7 dumpcap 19259 root mem<br />
REG 179,2 13072 29019 /lib/arm-linux-gnueabihf/libcap.so.2.22 dumpcap 19259 root mem<br />
REG 179,2 207132 66638 /usr/lib/arm-linux-gnueabihf/libpcap.so.1.3.0 dumpcap 19259 root mem<br />
REG 179,2 904384 76594 /lib/arm-linux-gnueabihf/libglib-2.0.so.0.3200.4 dumpcap 19259 root mem<br />
REG 179,2 21848 67377 /usr/lib/libwsutil.so.2.0.0 dumpcap<br />
19259 root mem REG<br />
179,2 6636 30910 /usr/lib/arm-linux-gnueabihf/libcofi_rpi.so dumpcap 19259 root mem<br />
REG 179,2 126236 1885 /lib/arm-linux-gnueabihf/ld-2.13.so dumpcap 19259 root 0r CHR 1,3 0t0 18 /dev/null dumpcap 19259<br />
root 1w CHR 1,3<br />
0t0 18 /dev/null dumpcap<br />
19259 root 2u CHR<br />
1,3 0t0 18 /dev/null dumpcap 19259 root 3u pack 41184 0t0 ALL type=SOCK_RAW dumpcap 19259<br />
root 4u REG 8,1 169290163 3145731 /mnt/hdd/tsar_files_to_proceed/REC_00082_20130712092043.pcap</p></blockquote><p>I'll execute strace soon</p></div><div id="comment-22895-info" class="comment-info"><span class="comment-age">(12 Jul '13, 02:10)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22896"></span><div id="comment-22896" class="comment"><div id="post-22896-score" class="comment-score"></div><div class="comment-text"><p>Does the file <code>/mnt/hdd/tsar_files_to_proceed/REC_00082_20130712092043.pcap</code> still grow? What is its size?</p></div><div id="comment-22896-info" class="comment-info"><span class="comment-age">(12 Jul '13, 02:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22897"></span><div id="comment-22897" class="comment"><div id="post-22897-score" class="comment-score"></div><div class="comment-text"><p>Still growing up... is now 181.4 Mio</p></div><div id="comment-22897-info" class="comment-info"><span class="comment-age">(12 Jul '13, 02:15)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22898"></span><div id="comment-22898" class="comment"><div id="post-22898-score" class="comment-score"></div><div class="comment-text"><p>Strace result :</p><pre><code>19259 select(4, [3], NULL, NULL, {0, 222299}) = 1 (in [3], left {0, 222273})
19259 gettimeofday({1373620307, 717390}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620307, 718166}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620307, 718913}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 88822})
19259 gettimeofday({1373620307, 881004}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620308, 132071}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620308, 383234}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 169517})
19259 gettimeofday({1373620308, 498239}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 gettimeofday({1373620308, 561709}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620308, 869494}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 41176})
19259 gettimeofday({1373620309, 100579}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620309, 101461}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 78816})
19259 gettimeofday({1373620309, 307420}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 write(4, &quot;\0\0S\310\337Q\372S\5\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 328064}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620309, 328895}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;rong&gt;&lt;br /&gt;\n&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;n&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 330183}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620309, 330976}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620309, 337532}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 219591})
19259 gettimeofday({1373620309, 369802}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620309, 370889}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;               Format : &lt;strong&gt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 377821}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620309, 378658}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620309, 379471}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;n: right;\&quot;&gt;&lt;a class=\&quot;badge badge&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 380765}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620309, 387336}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 write(4, &quot;://192.1.1.47/tmp_file/2013-07-1&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 388712}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620309, 389666}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620309, 390471}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620309, 397006}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 write(4, &quot;f=\&quot;#\&quot; class=\&quot;badge badge-importa&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 398416}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620309, 399298}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620309, 400107}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;con-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; &quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 407202}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620309, 408034}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 228982})
19259 gettimeofday({1373620309, 430010}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 247019})
19259 gettimeofday({1373620309, 434146}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 write(4, &quot;\0P\344\335M\225\2\346[\27\3\326P\20\2\224\210\37\0\0\&quot; frizb-path&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 435813}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620309, 436716}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620309, 440270}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;right;\&quot;&gt;&lt;a class=\&quot;badge badge-su&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 441652}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620309, 442458}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620309, 443269}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;92.1.1.47/tmp_file/2013-07-11/RE&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 447598}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620309, 448431}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620309, 449233}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 write(4, &quot;1554.pcap\&quot;&gt;&lt;i class=\&quot;icon-downlo&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 450527}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620309, 456034}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620309, 457039}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badg&quot;..., 4096) = 4096
19259 gettimeofday({1373620309, 458397}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620309, 459203}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620309, 459997}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 102320})
19259 gettimeofday({1373620309, 615493}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 49261})
19259 gettimeofday({1373620309, 817236}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620310, 68329}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620310, 320264}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620310, 575188}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620310, 826282}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620311, 77557}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 229573})
19259 gettimeofday({1373620311, 107513}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620311, 108508}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 172619})
19259 gettimeofday({1373620311, 188018}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 write(4, &quot;e\&quot; frizb-path=\&quot;/var/www/tmp_file&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 197348}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620311, 198274}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 write(4, &quot;&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\23s\300\1\1/\300\1\1\37\0P\344\335M&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 199801}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620311, 200696}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 gettimeofday({1373620311, 207623}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;javascript: delete_file($(this))&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 209118}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620311, 210025}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620311, 210924}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 write(4, &quot;remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 218183}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620311, 219077}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620311, 219968}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;ss=\&quot;maClass maClass0\&quot; style=\&quot;dis&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 221509}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620311, 227789}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620311, 228690}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620311, 229670}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 198776})
19259 gettimeofday({1373620311, 302466}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 write(4, &quot;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 436724}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 gettimeofday({1373620311, 496728}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 write(4, &quot;-briefcase icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 581163}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620311, 640787}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620311, 655801}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;ascript: delete_file($(this));\&quot;&gt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 657222}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620311, 657996}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620311, 658763}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620311, 663736}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;ve icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 665149}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620311, 665926}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot; class=\&quot;icon-remove icon-white\&quot;&gt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620311, 672223}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620311, 673021}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 gettimeofday({1373620311, 673794}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 gettimeofday({1373620311, 674549}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 71114})
19259 gettimeofday({1373620311, 854350}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620312, 105433}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620313, 708088}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 write(4, &quot;t: 50px;\&quot;&gt;20130711_00011&lt;/td&gt;\r\n\t&quot;..., 4096) = 4096
19259 gettimeofday({1373620313, 721085}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620313, 721910}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620313, 722717}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620313, 723525}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 write(4, &quot;/537.36 (KHTML, like Gecko) Chro&quot;..., 4096) = 4096
19259 gettimeofday({1373620313, 728224}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620313, 729053}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620313, 729860}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;ile/2013-07-12/REC_00077_2013071&quot;..., 4096) = 4096
19259 gettimeofday({1373620313, 731165}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620313, 737692}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;ss=\&quot;icon-download-alt icon-white&quot;..., 4096) = 4096
19259 gettimeofday({1373620313, 739051}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620313, 739873}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620313, 740679}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620313, 747281}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 write(4, &quot;w/tmp_file/2013-07-12/REC_00062_&quot;..., 4096) = 4096
19259 gettimeofday({1373620313, 748656}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620313, 749584}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 47065})
19259 gettimeofday({1373620313, 953785}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 write(4, &quot;eFile\&quot; frizb-path=\&quot;/var/www/tmp_&quot;..., 4096) = 4096
19259 gettimeofday({1373620313, 955331}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620313, 956231}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 write(4, &quot;72.73%&lt;/strong&gt;&lt;br /&gt;\nCPU Load A&quot;..., 4096) = 4096
19259 gettimeofday({1373620313, 959160}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620313, 960130}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620313, 960992}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620314, 212118}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620314, 463263}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620314, 714473}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620314, 965693}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 118554})
19259 gettimeofday({1373620315, 135056}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620315, 155215}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 193198})
19259 gettimeofday({1373620315, 213103}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 write(4, &quot;ng&gt;&lt;br /&gt;\r\n                     &quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 214942}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620315, 215847}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620315, 227337}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;none\&quot;&gt;&lt;td style=\&quot;padding-left: 5&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 228843}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620315, 229845}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620315, 230741}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 write(4, &quot;&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.4 MB&lt;/td&gt;\r\n\t\t\t&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 238259}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620315, 239166}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;lign: right;\&quot;&gt;&lt;a class=\&quot;badge ba&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 240613}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620315, 242457}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620315, 243414}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 gettimeofday({1373620315, 247603}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;&lt;i class=\&quot;icon-download-alt icon&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 249086}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620315, 249996}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620315, 250875}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 226337})
19259 gettimeofday({1373620315, 281363}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246701})
19259 gettimeofday({1373620315, 286012}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 write(4, &quot;_20130712005043.pcap\&quot;&gt;&lt;i class=\&quot;&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 287617}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620315, 291407}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 write(4, &quot;i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 293019}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620315, 294049}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620315, 294930}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620315, 303880}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 write(4, &quot;d&gt;\r\n\t\t\t\t&lt;td&gt;265.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 305373}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620315, 306280}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620315, 307322}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 write(4, &quot;0px;\&quot;&gt;20130711_00024&lt;/td&gt;\r\n\t\t\t\t&lt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 318321}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620315, 319211}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620315, 320101}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;le=\&quot;text-align: right;\&quot;&gt;&lt;a class&quot;..., 4096) = 4096
19259 gettimeofday({1373620315, 326996}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620315, 327976}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 97350})
19259 gettimeofday({1373620315, 481626}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 58953})
19259 gettimeofday({1373620315, 673625}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620315, 924765}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620316, 175959}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620316, 427141}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620316, 678320}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620316, 929476}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 81091})
19259 gettimeofday({1373620317, 136719}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 gettimeofday({1373620317, 196766}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 212542})
19259 write(4, &quot;s\&quot; href=\&quot;http://192.1.1.47/tmp_f&quot;..., 4096) = 4096
19259 gettimeofday({1373620317, 356720}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 gettimeofday({1373620317, 417921}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 gettimeofday({1373620317, 418854}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;&#39;192.1.1.47&#39;);\&quot;&gt;&lt;i class=\&quot;icon-b&quot;..., 4096) = 4096
19259 gettimeofday({1373620317, 426984}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 gettimeofday({1373620317, 427963}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/v&quot;..., 4096) = 4096
19259 gettimeofday({1373620317, 429532}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620317, 430462}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620317, 432546}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 write(4, &quot;le($(this));\&quot;&gt;&lt;i class=\&quot;icon-rem&quot;..., 4096) = 4096
19259 gettimeofday({1373620317, 434120}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620317, 508694}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 gettimeofday({1373620317, 551837}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 gettimeofday({1373620317, 614328}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 write(4, &quot;i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=&quot;..., 4096) = 4096
19259 gettimeofday({1373620317, 736768}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 gettimeofday({1373620317, 748519}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620317, 749900}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620317, 750670}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620317, 751443}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 60532})
19259 gettimeofday({1373620317, 941904}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620318, 193015}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620318, 444158}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 229730})
19259 gettimeofday({1373620318, 498272}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620318, 509258}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 27470})
19259 gettimeofday({1373620318, 734104}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;&gt;20130711_00044&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22&quot;..., 4096) = 4096
19259 gettimeofday({1373620318, 735544}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620318, 736399}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620318, 737395}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620318, 738221}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620318, 745517}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620319, 482}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 153151})
19259 write(4, &quot;\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; s&quot;..., 4096) = 4096
19259 gettimeofday({1373620319, 160576}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620319, 216715}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246587})
19259 gettimeofday({1373620319, 286709}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 gettimeofday({1373620319, 361806}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 write(4, &quot;iffer.php\r\nAccept-Encoding: gzip&quot;..., 4096) = 4096
19259 gettimeofday({1373620319, 410641}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620319, 411488}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620319, 412308}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;tmp_file/2013-07-12/REC_00077_20&quot;..., 4096) = 4096
19259 gettimeofday({1373620319, 413698}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620319, 417423}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 write(4, &quot;nclick=\&quot;javascript: delete_file(&quot;..., 4096) = 4096
19259 gettimeofday({1373620319, 418790}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620319, 419610}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620319, 420422}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620319, 426959}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 write(4, &quot;maClass0\&quot; style=\&quot;display: none\&quot;&gt;&quot;..., 4096) = 4096
19259 gettimeofday({1373620319, 428363}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620319, 429190}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620319, 430097}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClas&quot;..., 4096) = 4096
19259 gettimeofday({1373620319, 437194}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249944})
19259 gettimeofday({1373620319, 438123}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620319, 438934}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 141957})
19259 gettimeofday({1373620319, 547947}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 242977})
19259 gettimeofday({1373620319, 555919}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 51132})
19259 gettimeofday({1373620319, 755921}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620320, 7077}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620320, 258239}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620320, 509411}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 22158})
19259 write(4, &quot;\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;&quot;..., 4096) = 4096
19259 gettimeofday({1373620320, 747471}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620320, 748267}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 gettimeofday({1373620320, 749026}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 gettimeofday({1373620320, 749873}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620320, 750639}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 239374})
19259 gettimeofday({1373620320, 762307}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 129486})
19259 gettimeofday({1373620320, 883805}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620320, 884618}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620320, 885410}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 38735})
19259 gettimeofday({1373620321, 142046}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 gettimeofday({1373620321, 217693}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 203385})
19259 write(4, &quot;\330\266k\20\322\316\275\377&amp;P_(k:7i\341\300\312\3661\327\27&gt;!\350\[email protected]\26\267\345Q&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 311175}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620321, 312025}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620321, 327471}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;over table-condensed\&quot;&gt;&lt;tr&gt;\r\n\t\t&lt;t&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 328824}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620321, 329657}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;\314i\10\0E\0\5\334w\[email protected]\[email protected]\6:\362\300\1\1/\300\1\1\37\0P\344\336\302\340\314\374&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 337204}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620321, 338055}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620321, 338883}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;2_00067&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.2 MB&lt;/t&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 340256}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620321, 356660}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620321, 357620}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;b&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 359061}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620321, 359880}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 gettimeofday({1373620321, 376660}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;uca\310\337Q\337\267\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 378225}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 214460})
19259 gettimeofday({1373620321, 414828}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 247014})
19259 gettimeofday({1373620321, 418975}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620321, 420079}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;5_20130712000543.pcap\&quot;&gt;&lt;i class=&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 437009}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620321, 437952}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;ne\&quot;&gt;&lt;td style=\&quot;padding-left: 50p&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 439327}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620321, 440153}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620321, 447268}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620321, 448119}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;\&quot;badge badge-success\&quot; href=\&quot;hta\310&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 449494}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620321, 450322}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620321, 452283}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 write(4, &quot; right;\&quot;&gt;&lt;a class=\&quot;badge badge-s&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 453746}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620321, 467261}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620321, 468089}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 write(4, &quot;1.47/tmp_file/2013-07-11/REC_000&quot;..., 4096) = 4096
19259 gettimeofday({1373620321, 469445}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620321, 470336}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 148440})
19259 gettimeofday({1373620321, 619528}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 167364})
19259 gettimeofday({1373620321, 755034}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 gettimeofday({1373620321, 816424}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620321, 817406}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 63210})
19259 gettimeofday({1373620322, 5118}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620322, 256204}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620322, 522129}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620322, 773319}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620323, 24489}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 177760})
19259 gettimeofday({1373620323, 138873}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 gettimeofday({1373620323, 206581}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 227370})
19259 write(4, &quot;.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-a&quot;..., 4096) = 4096
19259 gettimeofday({1373620323, 348877}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620323, 423044}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 gettimeofday({1373620323, 505378}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 write(4, &quot;t: 50px;\&quot;&gt;20130712_00081&lt;/td&gt;\r\n\t&quot;..., 4096) = 4096
19259 gettimeofday({1373620323, 596718}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620323, 636746}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 gettimeofday({1373620323, 746725}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 write(4, &quot;\n\t\t\t\t&lt;td style=\&quot;text-align: righ&quot;..., 4096) = 4096
19259 gettimeofday({1373620323, 779770}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620323, 780599}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;e badge-success\&quot; href=\&quot;http://19&quot;..., 4096) = 4096
19259 gettimeofday({1373620323, 781986}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620323, 787590}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620323, 788397}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620323, 789205}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot;&quot;..., 4096) = 4096
19259 gettimeofday({1373620323, 790650}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620323, 792464}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620323, 793369}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620323, 797652}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620323, 798557}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot; class=\&quot;icon-download-alt icon-w&quot;..., 4096) = 4096
19259 gettimeofday({1373620323, 799893}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620323, 800706}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 126602})
19259 gettimeofday({1373620323, 931213}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 215345})
19259 gettimeofday({1373620323, 967265}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620323, 968122}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;/\344\336\0Ps\276\321\261\302\342\v2P\20&gt;\303\366\f\0\0\0\0\0\0\0\0c\310\337Q&amp;&quot;..., 4096) = 4096
19259 gettimeofday({1373620323, 969522}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620323, 970342}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620323, 972263}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620323, 973086}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620324, 224201}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620324, 475355}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620324, 730844}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620324, 982086}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 135429})
19259 gettimeofday({1373620325, 107302}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620325, 108117}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 182244})
19259 write(4, &quot;dstats well\&quot;&gt;\r\n\t&lt;h3&gt;&lt;img src=\&quot;./&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 178865}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620325, 179950}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620325, 180758}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;0%\&quot;&gt;Record.&lt;/th&gt;\r\n\t\t&lt;th&gt;Size&lt;/th&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 187663}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620325, 188498}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;s maClass0\&quot; style=\&quot;display: none&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 189811}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620325, 190730}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620325, 197271}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 write(4, &quot;=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 198714}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620325, 199543}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620325, 200341}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620325, 206943}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;s\&quot; href=\&quot;http://192.1.1.47/tmp_f&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 208344}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620325, 209167}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620325, 209983}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620325, 210783}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 229014})
19259 gettimeofday({1373620325, 238615}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246999})
19259 write(4, &quot;\1\1/\344\337\0P\206\0\207\356+|Q\326P\[email protected])|\351\0\0\0\0\0\0\0\0e\310\337&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 243635}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620325, 244465}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620325, 245270}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 write(4, &quot;43.pcap\&quot;&gt;&lt;i class=\&quot;icon-download&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 249393}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620325, 250230}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge b&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 251546}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620325, 252356}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620325, 257724}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620325, 258537}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;160054.pcap\&quot; onclick=\&quot;javascript&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 259884}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620325, 260709}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 gettimeofday({1373620325, 264653}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;REC_00018_20130711140054.pcap\&quot; o&quot;..., 4096) = 4096
19259 gettimeofday({1373620325, 266014}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620325, 266946}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620325, 267758}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 81393})
19259 gettimeofday({1373620325, 438371}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 62940})
19259 gettimeofday({1373620325, 626366}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620325, 877532}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620326, 128661}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620326, 379808}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620326, 630971}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620326, 882141}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 35220})
19259 gettimeofday({1373620327, 122594}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 gettimeofday({1373620327, 170207}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 161948})
19259 write(4, &quot;file($(this));\&quot;&gt;&lt;i class=\&quot;icon-r&quot;..., 4096) = 4096
19259 gettimeofday({1373620327, 356989}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620327, 426737}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 write(4, &quot;\335\203\270&#39;\353\317\314i\10\0E\0\5\334j\[email protected]\[email protected]\6H\22\300\1\1/\300\1\1\37\0P&quot;..., 4096) = 4096
19259 gettimeofday({1373620327, 548671}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249813})
19259 gettimeofday({1373620327, 624546}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 gettimeofday({1373620327, 686709}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 write(4, &quot;30712_00076&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 M&quot;..., 4096) = 4096
19259 gettimeofday({1373620327, 724455}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620327, 725271}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620327, 726040}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 write(4, &quot;e=\&quot;text-align: right;\&quot;&gt;&lt;a class=&quot;..., 4096) = 4096
19259 gettimeofday({1373620327, 730734}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620327, 731526}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620327, 732269}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;\0\0\&quot; href=\&quot;http://192.1.1.47/tmp_&quot;..., 4096) = 4096
19259 gettimeofday({1373620327, 737196}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620327, 738000}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620327, 738764}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;-12/REC_00053_20130712020543.pca&quot;..., 4096) = 4096
19259 gettimeofday({1373620327, 740036}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620327, 740808}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620327, 741559}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 77513})
19259 gettimeofday({1373620327, 916475}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620328, 167616}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620328, 418778}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 201547})
19259 gettimeofday({1373620328, 477811}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249941})
19259 gettimeofday({1373620328, 478809}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620328, 776720}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 118385})
19259 gettimeofday({1373620328, 942008}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 write(4, &quot;-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a hre&quot;..., 4096) = 4096
19259 gettimeofday({1373620328, 943471}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620328, 944258}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;g&gt;2.17&lt;/strong&gt;&lt;br /&gt;\n&amp;nbsp;&amp;nbs&quot;..., 4096) = 4096
19259 gettimeofday({1373620328, 945503}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620328, 951643}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620328, 952416}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 105320})
19259 gettimeofday({1373620329, 133600}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620329, 200333}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620329, 272492}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620329, 346700}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620329, 416715}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 write(4, &quot;                         Format &quot;..., 4096) = 4096
19259 gettimeofday({1373620329, 449147}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620329, 449968}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620329, 450766}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;ma&quot;..., 4096) = 4096
19259 gettimeofday({1373620329, 452055}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620329, 457554}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620329, 458381}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;e=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;pad&quot;..., 4096) = 4096
19259 gettimeofday({1373620329, 459718}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620329, 460540}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;20130712_00063&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.&quot;..., 4096) = 4096
19259 gettimeofday({1373620329, 467573}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620329, 468389}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620329, 469199}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620329, 470003}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;//192.1.1.47/tmp_file/2013-07-12&quot;..., 4096) = 4096
19259 gettimeofday({1373620329, 477858}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620329, 478775}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 155327})
19259 gettimeofday({1373620329, 574486}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 43823})
19259 gettimeofday({1373620329, 781647}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620330, 32771}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620330, 283966}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620330, 535139}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620330, 786258}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620331, 37512}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 189972})
19259 gettimeofday({1373620331, 136754}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620331, 181710}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620331, 236742}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249965})
19259 gettimeofday({1373620331, 272318}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620331, 287627}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 write(4, &quot;e-success\&quot; href=\&quot;http://192.1.1.&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 289136}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620331, 290040}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 write(4, &quot;0&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;37.9 MB&lt;/td&gt;\r\n\t\t&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 291486}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620331, 297794}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620331, 298687}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 write(4, &quot;p_file/2013-07-12/REC_00072_2013&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 300182}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620331, 301073}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620331, 307799}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;i class=\&quot;icon-download-alt icon-&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 309290}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620331, 310184}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620331, 311192}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 write(4, &quot; href=\&quot;#\&quot; class=\&quot;badge badge-imp&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 318336}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620331, 319325}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620331, 320204}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 227685})
19259 gettimeofday({1373620331, 343556}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246513})
19259 write(4, &quot;leteFile\&quot; frizb-path=\&quot;/var/www/t&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 348956}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620331, 349874}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620331, 353633}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 write(4, &quot;e badge-success\&quot; href=\&quot;http://19&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 355178}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620331, 356084}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620331, 357089}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;13-07-11/REC_00036_2013071121504&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 366698}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620331, 367662}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620331, 368544}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;s=\&quot;icon-download-alt icon-white\&quot;&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 377271}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620331, 378197}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620331, 379098}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;s=\&quot;badge badge-important\&quot; id=\&quot;de&quot;..., 4096) = 4096
19259 gettimeofday({1373620331, 380589}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620331, 387362}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620331, 388263}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 1927})
19259 gettimeofday({1373620331, 638473}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 55682})
19259 gettimeofday({1373620331, 833799}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620332, 84876}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620332, 335949}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620332, 602001}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620332, 853951}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 7224})
19259 gettimeofday({1373620333, 131535}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249963})
19259 write(4, &quot;www/tmp_file/2013-07-11/REC_0001&quot;..., 4096) = 4096
19259 gettimeofday({1373620333, 222429}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 247641})
19259 gettimeofday({1373620333, 305315}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620333, 394674}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;\0006\0\0\0006\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0([email protected]\[email protected]&quot;..., 4096) = 4096
19259 gettimeofday({1373620333, 404471}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620333, 405295}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620333, 406109}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot; class=\&quot;maClass maClass0\&quot; style=&quot;..., 4096) = 4096
19259 gettimeofday({1373620333, 428591}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620333, 507052}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 write(4, &quot;style=\&quot;padding-left: 50px;\&quot;&gt;2013&quot;..., 4096) = 4096
19259 gettimeofday({1373620333, 582073}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249947})
19259 gettimeofday({1373620333, 583173}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620333, 583993}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620333, 584796}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;e badge-successm\310\337Q\177\r\4\0\352\5\0\0\352\5\0\0p&quot;..., 4096) = 4096
19259 gettimeofday({1373620333, 588027}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620333, 588848}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620333, 589656}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 write(4, &quot;gn: right;\&quot;&gt;&lt;a class=\&quot;badge badg&quot;..., 4096) = 4096
19259 gettimeofday({1373620333, 598243}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620333, 599159}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620333, 599960}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620333, 600762}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620333, 607655}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620333, 608461}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620333, 609259}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 201272})
19259 gettimeofday({1373620333, 658951}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 50881})
19259 gettimeofday({1373620333, 859039}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620334, 110146}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 33727})
19259 write(4, &quot;2.1.1.47/tmp_file/2013-07-12/REC&quot;..., 4096) = 4096
19259 gettimeofday({1373620334, 332036}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620334, 333297}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620334, 334148}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;####\r\n&lt;div class=\&quot;span4 trcc_cpu&quot;..., 4096) = 4096
19259 gettimeofday({1373620334, 354860}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620334, 355718}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620334, 356540}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620334, 607826}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620334, 859603}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 11414})
19259 gettimeofday({1373620335, 107494}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 gettimeofday({1373620335, 108392}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 171826})
19259 gettimeofday({1373620335, 188060}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249771})
19259 write(4, &quot;style=\&quot;background: #FFF\&quot;&gt;\r\n     &quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 191092}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620335, 192023}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620335, 197343}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 write(4, &quot;tant\&quot; id=\&quot;deleteFile\&quot; frizb-path&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 198937}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620335, 199847}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620335, 200740}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;2013-07-12/REC_00071_20130712063&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 207926}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620335, 208844}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;\&quot;javascript: delete_file($(this)&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 210280}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620335, 211239}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 gettimeofday({1373620335, 217777}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620335, 218674}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620335, 219572}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td sty&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 221044}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259 gettimeofday({1373620335, 291545}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 gettimeofday({1373620335, 363282}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249964})
19259 write(4, &quot;le($(this));\&quot;&gt;&lt;i class=\&quot;icon-rem&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 417750}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620335, 418674}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620335, 419569}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;t\&quot; id=\&quot;deleteFile\&quot; frizb-path=o\310&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 421011}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620335, 427616}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620335, 428522}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620335, 429405}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;3-07-11/REC_00035_20130711213543&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 430972}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620335, 437581}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;=\&quot;/var/www/tmp_file/2013-07-11/R&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 439145}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620335, 440050}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620335, 440934}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 write(4, &quot;con-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/t&quot;..., 4096) = 4096
19259 gettimeofday({1373620335, 444535}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620335, 445441}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 142140})
19259 gettimeofday({1373620335, 554342}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 51208})
19259 gettimeofday({1373620335, 754157}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620336, 5317}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620336, 257012}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620336, 508081}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620336, 759244}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620337, 10463}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 162743})
19259 gettimeofday({1373620337, 136286}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249965})
19259 gettimeofday({1373620337, 182755}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 179494})
19259 write(4, &quot;ss1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td s&quot;..., 4096) = 4096
19259 gettimeofday({1373620337, 360972}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620337, 377556}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620337, 378329}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot;&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align:&quot;..., 4096) = 4096
19259 gettimeofday({1373620337, 379605}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620337, 380391}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 write(4, &quot; href=\&quot;http://192.1.1.47/tmp_fil&quot;..., 4096) = 4096
19259 gettimeofday({1373620337, 446734}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620337, 517137}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 gettimeofday({1373620337, 572851}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 write(4, &quot;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge ba&quot;..., 4096) = 4096
19259 gettimeofday({1373620338, 281833}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620338, 282707}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620338, 283827}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620338, 286227}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 write(4, &quot;\&quot;deleteFile\&quot; frizb-path=\&quot;/var/ww&quot;..., 4096) = 4096
19259 gettimeofday({1373620338, 293167}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259 gettimeofday({1373620338, 294049}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;badge badge-important\&quot; id=\&quot;delet&quot;..., 4096) = 4096
19259 gettimeofday({1373620338, 295547}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620338, 296393}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620338, 297341}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620338, 298179}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 81331})
19259 gettimeofday({1373620338, 477706}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620338, 478605}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 25443})
19259 gettimeofday({1373620340, 59582}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259 write(4, &quot;: delete_file($(this));\&quot;&gt;&lt;i clas&quot;..., 4096) = 4096
19259 gettimeofday({1373620340, 62082}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 gettimeofday({1373620340, 63382}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620340, 64195}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620340, 65073}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620340, 65840}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 write(4, &quot;sp;&lt;/span&gt; Cache : &lt;strong&gt;253 M&quot;..., 4096) = 4096
19259 gettimeofday({1373620340, 67271}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620340, 68119}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620340, 68862}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620340, 69611}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259 gettimeofday({1373620340, 70367}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620340, 71196}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;ppleWebKit/537.36 (KHTML, like G&quot;..., 4096) = 4096
19259 gettimeofday({1373620340, 72447}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620340, 73217}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259 gettimeofday({1373620340, 73984}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620340, 324993}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620340, 576060}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620340, 827224}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620341, 78403}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 230091})
19259 write(4, &quot;0130712_00077&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.3&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 107882}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620341, 108790}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620341, 109666}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620341, 110533}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 170710})
19259 gettimeofday({1373620341, 191168}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620341, 192348}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(\&quot;\[email protected]\0\200\6U\333\300\1&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 193887}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259 gettimeofday({1373620341, 197794}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 write(4, &quot;p_file/2013-07-12/REC_00078_2013&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 199360}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620341, 200274}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620341, 201168}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 write(4, &quot;ite\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 208391}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620341, 209286}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 gettimeofday({1373620341, 210172}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 gettimeofday({1373620341, 211034}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 write(4, &quot;Class0\&quot; style=\&quot;display: none\&quot;&gt;&lt;t&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 218362}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620341, 219264}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 write(4, &quot;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 220773}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620341, 227319}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620341, 228210}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 220542})
19259 gettimeofday({1373620341, 258715}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246683})
19259 gettimeofday({1373620341, 263325}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259 write(4, &quot;td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: &quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 264900}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620341, 265810}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249965})
19259 gettimeofday({1373620341, 269745}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259 write(4, &quot;ile/2013-07-11/REC_00041_2013071&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 271322}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259 gettimeofday({1373620341, 272232}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 gettimeofday({1373620341, 273105}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 write(4, &quot;ck=\&quot;javascript: delete_file($(th&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 278366}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259 gettimeofday({1373620341, 279344}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259 gettimeofday({1373620341, 280245}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259 write(4, &quot;on-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 286061}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259 gettimeofday({1373620341, 287240}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620341, 288162}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259 write(4, &quot;maClass maClass1\&quot; style=\&quot;display&quot;..., 4096) = 4096
19259 gettimeofday({1373620341, 289645}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259 gettimeofday({1373620341, 297340}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259 gettimeofday({1373620341, 298238}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 75400})
19259 gettimeofday({1373620341, 473881}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 41471})
19259 gettimeofday({1373620341, 683467}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620341, 934662}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620342, 185822}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259 gettimeofday({1373620342, 436985}, NULL) = 0
19259 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)</code></pre></div><div id="comment-22898-info" class="comment-info"><span class="comment-age">(12 Jul '13, 02:17)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22900"></span><div id="comment-22900" class="comment"><div id="post-22900-score" class="comment-score"></div><div class="comment-text"><p>if this the strace of dumpcap? If so, I wonder why these paths are in the strace output !?! Do they make any sense to you?</p><pre><code>19259 write(4, &quot;://192.1.1.47/tmp_file/2013-07-1&quot;..., 4096) = 4096
19259 write(4, &quot;www/tmp_file/2013-07-11/REC_0001&quot;..., 4096) = 4096
19259 write(4, &quot;2.1.1.47/tmp_file/2013-07-12/REC&quot;..., 4096) = 409619259 
19259 write(4, &quot;92.1.1.47/tmp_file/2013-07-11/RE&quot;..., 4096) = 409
19259 write(4, &quot;e\&quot; frizb-path=\&quot;/var/www/tmp_file&quot;..., 4096) = 4096
</code></pre><p>Are you sure you traced the dumpcap process PID?</p><p>If you run the strace command again, please use these parameters.</p><blockquote><p>strace -r -tt -v -s 1024 -f -o /var/tmp/dumpcap.trace -p PID_OF_DUMPCAP</p></blockquote></div><div id="comment-22900-info" class="comment-info"><span class="comment-age">(12 Jul '13, 02:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22902"></span><div id="comment-22902" class="comment not_top_scorer"><div id="post-22902-score" class="comment-score"></div><div class="comment-text"><p>I made this command : strace -f -o /var/tmp/19259.trace -p 19259</p><p>19259 is the PID of dumpcap</p><p>Paths you mention are paths I use with my Web application to download the pcap files.</p><p>I'll make a new strace. Coming back in a few minute</p></div><div id="comment-22902-info" class="comment-info"><span class="comment-age">(12 Jul '13, 03:46)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22904"></span><div id="comment-22904" class="comment not_top_scorer"><div id="post-22904-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Paths you mention are paths I use with my Web application for download the pcap files.</p></blockquote><p>Hm.. are you sure PID 19259 is just dumpcap, and not a script that starts dumpcap? Looks kind of strange.</p><p>How does your web application work (start of dumpcap, download of files, etc.)?</p></div><div id="comment-22904-info" class="comment-info"><span class="comment-age">(12 Jul '13, 03:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22905"></span><div id="comment-22905" class="comment not_top_scorer"><div id="post-22905-score" class="comment-score"></div><div class="comment-text"><p>Trace file with the new command you mentioned :</p><pre><code>19259      0.000000 select(4, [3], NULL, NULL, {0, 182963}) = 1 (in [3], left {0, 182932})
19259      0.000992 gettimeofday({1373626001, 646426}, NULL) = 0
19259      0.000432 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000562 gettimeofday({1373626001, 647414}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000520 gettimeofday({1373626001, 648274}, NULL) = 0
19259      0.005766 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250932 gettimeofday({1373626001, 904971}, NULL) = 0
19259      0.000344 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250936 gettimeofday({1373626002, 156249}, NULL) = 0
19259      0.000341 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250950 gettimeofday({1373626002, 407550}, NULL) = 0
19259      0.000353 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250863 gettimeofday({1373626002, 658757}, NULL) = 0
19259      0.000335 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250835 gettimeofday({1373626002, 909919}, NULL) = 0
19259      0.000306 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250778 gettimeofday({1373626003, 161000}, NULL) = 0
19259      0.000305 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250947 gettimeofday({1373626003, 412266}, NULL) = 0
19259      0.000348 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250878 gettimeofday({1373626003, 663491}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250873 gettimeofday({1373626003, 914706}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250874 gettimeofday({1373626004, 165922}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250886 gettimeofday({1373626004, 417150}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      2.256679 gettimeofday({1373626006, 696770}, NULL) = 0
19259      0.042738 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.036186 gettimeofday({1373626006, 757466}, NULL) = 0
19259      0.024644 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.029160 gettimeofday({1373626006, 811233}, NULL) = 0
19259      0.020065 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000646 gettimeofday({1373626006, 827618}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000576 gettimeofday({1373626006, 828521}, NULL) = 0
19259      0.000323 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000493 gettimeofday({1373626006, 829339}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000482 gettimeofday({1373626006, 830144}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.006811 gettimeofday({1373626006, 837287}, NULL) = 0
19259      0.000338 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000510 gettimeofday({1373626006, 838131}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000493 gettimeofday({1373626006, 838952}, NULL) = 0
19259      0.000331 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000494 gettimeofday({1373626006, 839773}, NULL) = 0
19259      0.000326 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000491 gettimeofday({1373626006, 840592}, NULL) = 0
19259      0.001619 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000552 gettimeofday({1373626006, 842765}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.003117 gettimeofday({1373626006, 847176}, NULL) = 0
19259      0.010952 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000560 gettimeofday({1373626006, 857726}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000497 gettimeofday({1373626006, 858552}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000446 write(4, &quot;E\0\0(+\[email protected]\0\200\6L\276\300\1\1\37\300\1\1/\[email protected]\0\26F\7\331\200\305t\343\315P\20\0\376\222d\0\0\0\0\0\0\0\0\215\336\337Q\235\23\n\0j\0\0\0j\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0\\+\[email protected]\0\200\6L\203\300\1\1\37\300\1\1/\[email protected]\0\26F\7\331\200\305t\343\315P\30\0\376J\336\0\0\374\323\311\211\350\300\376\306\231v\247W\0\3\235\245&#39;UF\302x\\\37\351\375\367c\374M%\37\377\373\254\223\231B\n\253I\237H\363\314\314\327\r\302\341\371\0314\215\336\337Q\205\31\n\0j\0\0\0j\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\20\0\\G\[email protected]\[email protected]\6pX\300\1\1/\300\1\1\37\0\26\[email protected]\305t\343\315F\7\331\264P\30\4\272\202\237\0\0PN.D\326\301\365\261\350\263\245)\253\265\372!\265\305\330\30\334k\6X\345\252\370\227\7f\331\235p\312\263\\\207\333E \31\251~\4\347\244\224\26\271n\334I\215\336\337Q\224\310\n\0j\0\0\0j\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0\\+\[email protected]\0\200\6L\202\300\1\1\37\300\1\1/\[email protected]\0\26F\7\331\264\305t\344\1P\30\0\376\275\0\0\0\314\361oG\357\362\262\37\211j\35J\364\300\361j\34\323\203\f\276\361\200\320\370E&amp;\36\231P\352\317\0276\2621\3,\203\310\301\7]\246\261)\274!\341U)\301\215\336\337Q\235\316\n\0j\0\0\0j\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\20\0\\G\[email protected]\[email protected]\6pW\300\1\1/\300\1\1\37\0\26\[email protected]\305t\344\1F\7\331\350P\30\4\272\202\237\0\0\315\207%I\355\205F\266\300\313\3673\277\337\2321\251~\260\306\264\214|\23262\300\307\265\356\317:\271\232\346\247d\3403\372\220lf%\357\343\223?\330\241\333y\215\336\337Q\5\341\r\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(+\[email protected]\0\200\6L\264\300\1\1\37\300\1\1/\[email protected]\0\26F\7\331\350\305t\3445P\20\0\376\221\224\0\0\0\0\0\0\0\0\216\336\337QRY\0\0j\0\0\0j\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0\\+\[email protected]\0\200\6L\177\300\1\1\37\300\1\1/\[email protected]\0\26F\7\331\350\305t\3445P\30\0\376\35\212\0\0/\323\210\311\rX\304\357\264\371J\v\374\302\246\t\246\&quot;\265\342\262\241Xzp!+\354\324\313}L\327\327\226\234X\1`\213\216W\234z\343\363\0\213\361\220\311\355\216\336\337Q9_\0\0j\0\0\0j\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\20\0\\G\[email protected]\[email protected]\6pV\300\1\1/\300\1\1\37\0\26\[email protected]\305t\3445F\7\332\34P\30\4\272\202\237\0\0\360C95p\33\206\265\313\335\313\3\340,&lt;\260Zr\313/@3\331!\5QE_\357\276)\216\262\201?\217\20O\262P\16\22\\bwW\2576\241\r\345\302\216\336\337Q\234\257\2\0j\0\0\0j\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0\\+\[email protected]\0\200\6L}\300\1\1\37\300\1\1/\[email protected]\0\26F\7\332\34\305t\344iP\30\0\376\r\306\0\0e\360\352\230\350o\314\311\214D\272\24p\224\342\337\370\273\6\213\223\300*G\333\26\35\364&gt;\305*Z\371\324n\30+L\367\261?)&lt;&gt;-\&quot;\244\242/\370\274\20\216\336\337Qa\266\2\0j\0\0\0j\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\20\0\\G\[email protected]\[email protected]\6pU\300\1\1/\300\1&quot;..., 4096) = 4096
19259      0.007895 gettimeofday({1373626006, 867226}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000533 gettimeofday({1373626006, 868144}, NULL) = 0
19259      0.000417 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000462 write(4, &quot; 12 Jul 2013 10:46:46 GMT\r\nServer: lighttpd/1.4.31\r\n\r\n5008\r\n                       Up Time : 03:13:28####SEPARATOR####\r\n20130712_00082(Size : 307.8 MB)&lt;br /&gt;\n&lt;hr /&gt;&lt;table class=\&quot;table table-striped table-hover table-condensed\&quot;&gt;&lt;tr&gt;\r\n\t\t&lt;th style=\&quot;width: 50%\&quot;&gt;Record.&lt;/th&gt;\r\n\t\t&lt;th&gt;Size&lt;/th&gt;\r\n\t\t&lt;th&gt;Action&lt;/th&gt;\r\n\t&lt;/tr&gt;&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;javacript: $(&#39;.myHidden&#39;).val(&#39;maClass0&#39;);\&quot;&gt;2013-07-12&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;td&gt;1.1 GB&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-info\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: compressDownload($(this), &#39;192.1.1.47&#39;);\&quot;&gt;&lt;i class=\&quot;icon-briefcase icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a class=\&quot;badge badge-important\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: deleteWholeDay($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00081&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-succes&quot;..., 4096) = 4096
19259      0.008219 gettimeofday({1373626006, 877200}, NULL) = 0
19259      0.000344 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000531 gettimeofday({1373626006, 878071}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000501 gettimeofday({1373626006, 878900}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000451 write(4, &quot;ath=\&quot;/var/www/tmp_file/2013-07-12/REC_00076_20130712075043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;m\226\336\337Q\207\344\f\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\264S\300\1\1/\300\1\1\37\0P\355{\334\315\372\206\[email protected]\20\1\22\210\37\0\0aClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00074&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;31 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00073&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_0&quot;..., 4096) = 4096
19259      0.007526 gettimeofday({1373626006, 887211}, NULL) = 0
19259      0.000346 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000531 gettimeofday({1373626006, 888085}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000510 gettimeofday({1373626006, 888922}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000455 write(4, &quot;055043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00067&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\226\336\337Q\321\345\f\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\264P\300\1\1/\300\1\1\37\0P\355{\334\316\v\242\[email protected]\20\1\22\210\37\0\0\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00066&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00066_20130712052043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-&quot;..., 4096) = 4096
19259      0.007492 gettimeofday({1373626006, 897202}, NULL) = 0
19259      0.000341 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000603 gettimeofday({1373626006, 898141}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000498 gettimeofday({1373626006, 898965}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000454 write(4, &quot;is));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00060&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;29.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00060_20130712035043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00060_20130712035043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00059&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00059_20130712033543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07&quot;..., 4096) = 4096
19259      0.007453 gettimeofday({1373626006, 907203}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000529 gettimeofday({1373626006, 908110}, NULL) = 0
19259      0.000423 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 243732})
19259      0.006902 gettimeofday({1373626006, 915400}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246829})
19259      0.003841 gettimeofday({1373626006, 919793}, NULL) = 0
19259      0.000577 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000471 write(4, &quot;&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00052&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;26.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-suc\226\336\337Qo\352\f\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\376\[email protected]\[email protected]\6\264K\300\1\1/\300\1\1\37\0P\355{\334\316(&amp;\[email protected]\20\1\22\210\37\0\0cess\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00052_20130712015043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00052_20130712015043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00051&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;25.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00051_20130712013543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=&quot;..., 4096) = 4096
19259      0.004426 gettimeofday({1373626006, 925057}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000536 gettimeofday({1373626006, 925932}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000588 gettimeofday({1373626006, 926874}, NULL) = 0
19259      0.000355 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000448 write(4, &quot;te\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00040&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00040_20130711225043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00040_20130711225043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00039&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.1 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;htt\226\336\337Q\362\375\r\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\376\[email protected]\[email protected]\6\264D\300\1\1/\300\1\1\37\0P\355{\334\316F\23\[email protected]\20\1\22\210\37\0\0p://192.1.1.47/tmp_file/2013-07-11/REC_00039_20130711223543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; friz&quot;..., 4096) = 4096
19259      0.009244 gettimeofday({1373626006, 936931}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000525 gettimeofday({1373626006, 937800}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000511 gettimeofday({1373626006, 938640}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000456 write(4, &quot;ass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00033&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;18 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00033_20130711174554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00033_20130711174554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00032&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;17.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00032_20130711173054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00032_20130711173054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;i&quot;..., 4096) = 4096
19259      0.007784 gettimeofday({1373626006, 947221}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000528 gettimeofday({1373626006, 948125}, NULL) = 0
19259      0.000407 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000521 gettimeofday({1373626006, 949014}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000451 write(4, &quot;: 50px;\&quot;&gt;20130711_00023&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00023_20130711151554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;\226\336\337Q\215\0\16\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\376\[email protected]\[email protected]\6\264?\300\1\1/\300\1\1\37\0P\355{\334\316b\227\[email protected]\20\1\22\210\37\0\0/var/www/tmp_file/2013-07-11/REC_00023_20130711151554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00021&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00021_20130711144554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00021_20130711144554.pcap\&quot; onclick=\&quot;javascript: delete_file($(t&quot;..., 4096) = 4096
19259      0.007436 gettimeofday({1373626006, 957236}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000520 gettimeofday({1373626006, 958094}, NULL) = 0
19259      0.000331 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000511 gettimeofday({1373626006, 958935}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000507 gettimeofday({1373626006, 959769}, NULL) = 0
19259      0.000331 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.001901 write(4, &quot;d style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00015_20130711131554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00015_20130711131554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00014&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00014_20130711130054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/w\226\336\337Q\35\2\16\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(,\[email protected]\0\200\6K\255\300\1\1\37\300\1\1/\355{\0P\[email protected]\334\316\\\343P\[email protected])\2422\0\0\0\0\0\0\0\0\226\336\337Q\270\2\16\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\376\[email protected]\[email protected]\6\264&lt;\300\1\1/\300\1\1\37\0P\355{\334\316s\263\[email protected]\20\1\22\210\37\0\0ww/tmp_file/2013-07-11/REC_00014_20130711130054.pcap\&quot; onclick=\&quot;javascript&quot;..., 4096) = 4096
19259      0.004898 gettimeofday({1373626006, 966970}, NULL) = 0
19259      0.000429 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000540 gettimeofday({1373626006, 967870}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 99978})
19259      0.150672 gettimeofday({1373626007, 118874}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 183750})
19259      0.068339 gettimeofday({1373626007, 187626}, NULL) = 0
19259      0.000433 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000560 write(4, &quot;.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00008_20130711113054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00008_20130711113054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00007&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00007_20130711111554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00007_20130711111554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;displa&quot;..., 4096) = 4096
19259      0.008663 gettimeofday({1373626007, 197215}, NULL) = 0
19259      0.000423 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000532 gettimeofday({1373626007, 198164}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000508 gettimeofday({1373626007, 199002}, NULL) = 0
19259      0.000546 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000473 write(4, &quot;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00079&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;50.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00078&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;55.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href\227\336\337Q:\320\2\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334A\[email protected]\[email protected]\6q\266\300&quot;..., 4096) = 4096
19259      0.007200 gettimeofday({1373626007, 207226}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000538 gettimeofday({1373626007, 208103}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000458 write(4, &quot;wl\333_{\241\350P\20\1\22\210\37\0\0b-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00072_20130712065043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00071&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00070&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00070_20130712062043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-&quot;..., 4096) = 4096
19259      0.008315 gettimeofday({1373626007, 217215}, NULL) = 0
19259      0.000344 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000536 gettimeofday({1373626007, 218089}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000508 gettimeofday({1373626007, 218925}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000451 write(4, &quot;is));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00064&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.1 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; \227\336\337Q\270\322\2\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334A\[email protected]\[email protected]\6q\261\300\1\1/\300\1\1\37\0P\355|\tw}\367_{\241\350P\20\1\22\210\37\0\0frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00063&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00063_20130712043543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge &quot;..., 4096) = 4096
19259      0.027201 gettimeofday({1373626007, 258134}, NULL) = 0
19259      0.033574 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259      0.018839 gettimeofday({1373626007, 301239}, NULL) = 0
19259      0.022647 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.044961 gettimeofday({1373626007, 371623}, NULL) = 0
19259      0.029982 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.008313 gettimeofday({1373626007, 405228}, NULL) = 0
19259      0.000341 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000451 write(4, &quot;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00057&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00056&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00056_20130712025043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFi\227\336\337Q\215\325\2\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(,\[email protected]\0\200\6K\243\300\1\1\37\300\1\1/\355|\0P_{\241\350\tw\203\253P\[email protected])q\7\0\0\0\0\0\0\0\0\227\336\337QM\327\2\0\352\5\0\0\352\5\0&quot;..., 4096) = 4096
19259      0.011214 gettimeofday({1373626007, 417234}, NULL) = 0
19259      0.000348 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000518 gettimeofday({1373626007, 418093}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000497 gettimeofday({1373626007, 418916}, NULL) = 0
19259      0.000326 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000496 gettimeofday({1373626007, 419737}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.001094 gettimeofday({1373626007, 421515}, NULL) = 0
19259      0.000754 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000479 write(4, &quot;i\10\0E\0\5\334A\[email protected]\[email protected]\6q\254\300\1\1/\300\1\1\37\0P\355|\tw\232{_{\241\350P\20\1\22\210\37\0\0class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00049&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00048&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00048_20130712005043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00048_20130712005043&quot;..., 4096) = 4096
19259      0.003383 gettimeofday({1373626007, 428752}, NULL) = 0
19259      0.003462 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000561 gettimeofday({1373626007, 429799}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000503 gettimeofday({1373626007, 430629}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000442 write(4, &quot; style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00040&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00040_20130711225043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00040_20130711225043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00039&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.1 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;htt\227\336\337Q\2664\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334A%@\[email protected]\6q\246\300\1\1/\300\1\1\37\0P\355|\tw\262\264_{\241\350P\20\1\22\210\37\0\0p://192.1.1.47/tmp_file/2013-07-11/REC_00039_20130711223543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00039_20130711223543.pcap\&quot; onclick=\&quot;javas&quot;..., 4096) = 4096
19259      0.005835 gettimeofday({1373626007, 437242}, NULL) = 0
19259      0.000344 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000517 gettimeofday({1373626007, 438094}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000510 gettimeofday({1373626007, 438928}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259      0.000461 write(4, &quot;\t\t\t&lt;td&gt;18 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00033_20130711174554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00033_20130711174554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00032&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;17.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00032_20130711173054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00032_20130711173054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=&quot;..., 4096) = 4096
19259      0.005140 gettimeofday({1373626007, 444869}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000515 gettimeofday({1373626007, 445718}, NULL) = 0
19259      0.000397 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 157461})
19259      0.093195 gettimeofday({1373626007, 539493}, NULL) = 0
19259      0.000543 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 43160})
19259      0.237054 gettimeofday({1373626007, 786713}, NULL) = 0
19259      0.039997 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.259249 gettimeofday({1373626008, 76180}, NULL) = 0
19259      0.000390 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 198733})
19259      0.054797 gettimeofday({1373626008, 131336}, NULL) = 0
19259      0.000315 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000478 gettimeofday({1373626008, 132117}, NULL) = 0
19259      0.000380 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 65851})
19259      0.184816 gettimeofday({1373626008, 317335}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000464 write(4, &quot;t;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00023_20130711151554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;\227\336\337Q,\313\4\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(,\[email protected]\0\200\6K\231\300\1\1\37\300\1\1/\355{\0P\[email protected]\334\316\222\vP\20?\255m\206\0\0\0\0\0\0\0\0\227\336\337Ql6\10\0&amp;\2\0\0&amp;\2\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\2\[email protected]\[email protected]\6u]\300\1\1/\300\1\1\37\0P\355|\tw\374\274_{\241\350P\30\1\22\204[\0\0002\r\n&gt;\n\r\n1dd\r\n&lt;/table&gt;####SEPARATOR####\r\n&lt;strong&gt;Current file since :&lt;/strong&gt;&lt;div style=&#39;text-align: center&#39;&gt;\n0 d. 03:26:04&lt;/div&gt;\n&lt;strong&gt;Current capture since :&lt;/strong&gt;&lt;div style=&#39;text-align: center&#39;&gt;\n1 d. 03:00:53&lt;/div&gt;&lt;hr /&gt;\n&lt;strong&gt;Instant Write Speed :&lt;/strong&gt; 24.9 KB/s&lt;br /&gt;\n&lt;strong&gt;Instant Remaining Time :&lt;/strong&gt;&lt;br /&gt;&lt;div style=&#39;text-align: center&#39;&gt;210 d. 07:40:27&lt;/div&gt;&lt;hr /&gt;\n&lt;strong&gt;Estimated Time Remaining (1h)&lt;/strong&gt;&lt;div style=&#39;text-align:center&#39;&gt;139 d. 18:11:46&lt;/div&gt;\n\r\n0\r\n\r\n\227\336\337Q\r4\v\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(,\[email protected]\0\200\6K\204\300\1\1\37\300\1\1/\355|\0P_{\241\350\tw\376\254P\20?\255\366\201\0\0\0\0\0\0\0\0\230\336\337Q1\362\1\0!\2\0\0!\2\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\2\23-\[email protected]\0\200\6I\220\300\1\1\37\300\1\1/\355|\0P_{\241\350\tw\376\254P\30?\255\204t\0\0POST /a&quot;..., 4096) = 4096
19259      0.003146 gettimeofday({1373626008, 321292}, NULL) = 0
19259      0.000350 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000538 gettimeofday({1373626008, 322171}, NULL) = 0
19259      0.005226 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000587 gettimeofday({1373626008, 327990}, NULL) = 0
19259      0.000338 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000497 gettimeofday({1373626008, 328821}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000486 gettimeofday({1373626008, 329631}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 182609})
19259      0.067979 write(4, &quot; /&gt;&lt;span class=\&quot;badge\&quot;&gt;&amp;nbsp;&lt;/span&gt; Total : &lt;strong&gt;485 MB&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 17%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-warning\&quot; style=\&quot;width: 4%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-danger\&quot; style=\&quot;width: 73%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-success\&quot; style=\&quot;width: 6%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t&lt;/div&gt;&lt;/div&gt;\r\n&lt;div class=\&quot;span4 trcc_network well\&quot;&gt;\r\n\t&lt;h3&gt;&lt;img src=\&quot;./img/network.png\&quot; width=\&quot;32px\&quot;/&gt; Network&lt;/h3&gt;\r\n\t&lt;h5&gt;Ethernet&lt;/h5&gt;IP : &lt;strong&gt;192.1.1.47&lt;/strong&gt;&lt;br /&gt;MAC : &lt;stron\230\336\337Q\266\267\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\372\[email protected]\[email protected]\6\267\377\300\1\1/\300\1\1\37\0P\355~uI\3719C\304\261\265P\20\1\22\210\37\0\0g&gt;b8:27:eb:cf:cc:69\n&lt;/strong&gt;&lt;br /&gt;&lt;img src=\&quot;./img/upload.png\&quot; width=\&quot;16px\&quot; /&gt; Upload : &lt;strong&gt;2.4 GB&lt;/strong&gt;&lt;br /&gt;&lt;img src=\&quot;./img/download.png\&quot; width=\&quot;16px\&quot; /&gt; Download : &lt;strong&gt;106.5 MB&lt;/strong&gt;&lt;br /&gt;Total : &lt;strong&gt;2.3 GB&lt;/strong&gt;&lt;br /&gt;&lt;/div&gt;\r\n####SEPARATOR####\r\n&lt;div class=\&quot;span12 trcc_hddstats well\&quot;&gt;\r\n\t&lt;h3&gt;&lt;img src=\&quot;./img/sd.png\&quot; width=\&quot;32px\&quot;/&gt; HDD&lt;/h3&gt;\r\n    &lt;div class=\&quot;row-fluid\&quot;&gt;&lt;div class=\&quot;span3 wel&quot;..., 4096) = 4096
19259      0.002046 gettimeofday({1373626008, 399989}, NULL) = 0
19259      0.006914 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000666 gettimeofday({1373626008, 407567}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000459 write(4, &quot;g: chunked\r\nDate: Fri, 12 Jul 2013 10:46:48 GMT\r\nServer: lighttpd/1.4.31\r\n\r\n5008\r\n                       Up Time : 03:13:30####SEPARATOR####\r\n20130712_00082(Size : 307.9 MB)&lt;br /&gt;\n&lt;hr /&gt;&lt;table class=\&quot;table table-striped table-hover table-condensed\&quot;&gt;&lt;tr&gt;\r\n\t\t&lt;th style=\&quot;width: 50%\&quot;&gt;Record.&lt;/th&gt;\r\n\t\t&lt;th&gt;Size&lt;/th&gt;\r\n\t\t&lt;th&gt;Action&lt;/th&gt;\r\n\t&lt;/tr&gt;&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;javacript: $(&#39;.myHidden&#39;).val(&#39;maClass0&#39;);\&quot;&gt;2013-07-12&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;td&gt;1.1 GB&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-info\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: compressDownload($(this), &#39;192.1.1.47&#39;);\&quot;&gt;&lt;i class=\&quot;icon-briefcase icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a class=\&quot;badge badge-important\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: deleteWholeDay($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00081&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a cla&quot;..., 4096) = 4096
19259      0.001628 gettimeofday({1373626008, 409984}, NULL) = 0
19259      0.006908 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000652 gettimeofday({1373626008, 417547}, NULL) = 0
19259      0.000336 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000514 gettimeofday({1373626008, 418393}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000453 write(4, &quot;d=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00076_20130712075043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;m\230\336\337Q\374\7\6\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\21Q\300\1\1/\300\1\1\37\0P\355\177\321c\307\213\246\254I\201P\20\1\22\210\37\0\0aClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00074&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;31 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00073&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp&quot;..., 4096) = 4096
19259      0.008026 gettimeofday({1373626008, 427210}, NULL) = 0
19259      0.000347 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000532 gettimeofday({1373626008, 428085}, NULL) = 0
19259      0.000412 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000522 gettimeofday({1373626008, 429018}, NULL) = 0
19259      0.000331 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000523 write(4, &quot;-12/REC_00068_20130712055043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00067&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\230\336\337Qw\t\6\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241}@\[email protected]\6\21N\300\1\1/\300\1\1\37\0P\355\177\321c\330\247\246\254I\201P\20\1\22\210\37\0\0\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00066&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00066_20130712052043.pcap\&quot;&gt;&lt;i&quot;..., 4096) = 4096
19259      0.007342 gettimeofday({1373626008, 437218}, NULL) = 0
19259      0.000344 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000534 gettimeofday({1373626008, 438091}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000495 gettimeofday({1373626008, 438916}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000454 write(4, &quot;ript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00060&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;29.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00060_20130712035043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00060_20130712035043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00059&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00059_20130712033543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/va&quot;..., 4096) = 4096
19259      0.007495 gettimeofday({1373626008, 447195}, NULL) = 0
19259      0.000338 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000527 gettimeofday({1373626008, 448053}, NULL) = 0
19259      0.000326 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000507 gettimeofday({1373626008, 448887}, NULL) = 0
19259      0.000326 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000447 write(4, &quot;remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00052&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;26.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-suc\230\336\337Q\260\r\6\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21I\300\1\1/\300\1\1\37\0P\355\177\321c\365+\246\254I\201P\20\1\22\210\37\0\0cess\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00052_20130712015043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00052_20130712015043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00051&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;25.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00051_20130712013543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;d&quot;..., 4096) = 4096
19259      0.007539 gettimeofday({1373626008, 457207}, NULL) = 0
19259      0.000344 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 241878})
19259      0.008758 gettimeofday({1373626008, 466305}, NULL) = 0
19259      0.000338 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 247071})
19259      0.003867 gettimeofday({1373626008, 470512}, NULL) = 0
19259      0.000346 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000520 gettimeofday({1373626008, 471374}, NULL) = 0
19259      0.000331 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000451 write(4, &quot;ass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00045&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00045_20130712000543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00045_20130712000543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00044&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; hr\230\336\337Q-\32\7\0&lt;\0\0\0&lt;\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0.\241\[email protected]\[email protected]\6\26\363\300\1\1/\300\1\1\37\0P\355\177\321d\7\252\246\254I\201P\30\1\22\202q\0\0001\r\n\n\r\n\230\336\337Qb\&quot;\7\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21D\300\1\1/\300\1\1\37\0P\355\177\321d\7\260\246\254I\201P\20\1\22\210\37\0\0005568\r\n&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;javacript: $(&#39;.myHidden&#39;).val(&#39;maClass1&#39;);\&quot;&gt;2013-07-11&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;td&gt;738.3 MB&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align: ri&quot;..., 4096) = 4096
19259      0.004539 gettimeofday({1373626008, 476792}, NULL) = 0
19259      0.000443 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000539 gettimeofday({1373626008, 477682}, NULL) = 0
19259      0.000337 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000457 write(4, &quot;File\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00039_20130711223543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00038&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;20.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00038_20130711222043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00038_20130711222043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00037&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;20 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00037_20130711220543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt ico&quot;..., 4096) = 4096
19259      0.008748 gettimeofday({1373626008, 487301}, NULL) = 0
19259      0.000429 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000522 gettimeofday({1373626008, 488170}, NULL) = 0
19259      0.000331 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000510 gettimeofday({1373626008, 489010}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000514 gettimeofday({1373626008, 489852}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000654 write(4, &quot;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00031&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;16.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;ht\230\336\337Q\r%\7\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6Kv\300\1\1\37\300\1\1/\355\177\0P\246\254I\201\321d\rdP\[email protected])0\224\0\0\0\0\0\0\0\0\230\336\337Qj%\7\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21?\300\1\1/\300\1\1\37\0P\355\177\321d$4\246\254I\201P\20\1\22\210\37\0\0tp://192.1.1.47/tmp_file/2013-07-11/REC_00031_20130711171554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00031_20130711171554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00028&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;16.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00028_20130711163054.pcap\&quot;&gt;&lt;i cla&quot;..., 4096) = 4096
19259      0.006387 gettimeofday({1373626008, 497231}, NULL) = 0
19259      0.000341 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000530 gettimeofday({1373626008, 498094}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000500 gettimeofday({1373626008, 498923}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000443 write(4, &quot;e_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00020&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00020_20130711143054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00020_20130711143054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00019&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://\230\336\337Q\226&amp;\7\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21&lt;\300\1\1/\300\1\1\37\0P\355\177\321d5P\246\254I\201P\20\1\22\210\37\0\000192.1.1.47/tmp_file/2013-07-11/REC_00019_20130711141554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; clas&quot;..., 4096) = 4096
19259      0.007540 gettimeofday({1373626008, 507241}, NULL) = 0
19259      0.000347 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000533 gettimeofday({1373626008, 508114}, NULL) = 0
19259      0.000414 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000467 write(4, &quot;&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00013&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00013_20130711124554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00013_20130711124554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00012&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00012_20130711123054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00012_20130711123054.pcap\&quot; onclick=\&quot;javasc&quot;..., 4096) = 4096
19259      0.008216 gettimeofday({1373626008, 517214}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000532 gettimeofday({1373626008, 518086}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 92945})
19259      0.193667 gettimeofday({1373626008, 722423}, NULL) = 0
19259      0.024872 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.020220 gettimeofday({1373626008, 764513}, NULL) = 0
19259      0.039750 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 236986})
19259      0.030014 gettimeofday({1373626008, 827013}, NULL) = 0
19259      0.000424 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000477 write(4, &quot;&lt;td&gt;7.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00006_20130711110054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www\230\336\337Q\20)\7\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\0217\300\1\1/\300\1\1\37\0P\355\177\321dQ\324\246\254I\201P\20\1\22\210\37\0\0/tmp_file/2013-07-11/REC_00006_20130711110054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00005&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;5.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00005_20130711104554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00005_20130711104554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon&quot;..., 4096) = 4096
19259      0.001865 gettimeofday({1373626008, 829707}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.007260 gettimeofday({1373626008, 837301}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000468 write(4, &quot;00081_20130712090543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00080&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;37.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00079&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;50.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-&quot;..., 4096) = 4096
19259      0.001673 gettimeofday({1373626008, 839780}, NULL) = 0
19259      0.007113 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000653 gettimeofday({1373626008, 847546}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000505 gettimeofday({1373626008, 848384}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000441 write(4, &quot;\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00072&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;31.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00072_20130712065043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; friz\230\336\337Q\307~\f\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334y\[email protected]\[email protected]\0068\324\300\1\1/\300\1\1\37\0P\355x.\34.9zM\360*P\20\[email protected]\210\37\0\0b-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00072_20130712065043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00071&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_&quot;..., 4096) = 4096
19259      0.008052 gettimeofday({1373626008, 857211}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000526 gettimeofday({1373626008, 858078}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000509 gettimeofday({1373626008, 858917}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000446 write(4, &quot;: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00065&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00065_20130712050543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00065_20130712050543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00064&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.1 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; \230\336\337Q\20\200\f\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334y\[email protected]\[email protected]\0068\321\300\1\1/\300\1\1\37\0P\355x.\34?UzM\360*P\20\[email protected]\210\37\0\0frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot; onc&quot;..., 4096) = 4096
19259      0.007502 gettimeofday({1373626008, 867201}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000516 gettimeofday({1373626008, 868051}, NULL) = 0
19259      0.000483 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000539 gettimeofday({1373626008, 869080}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000452 write(4, &quot;0058&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00058_20130712032043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00058_20130712032043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00057&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass ma&quot;..., 4096) = 4096
19259      0.007338 gettimeofday({1373626008, 877418}, NULL) = 0
19259      0.000612 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000551 gettimeofday({1373626008, 878364}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000514 gettimeofday({1373626008, 879209}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000487 gettimeofday({1373626008, 880025}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.006922 gettimeofday({1373626008, 887278}, NULL) = 0
19259      0.000336 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 248492})
19259      0.002150 gettimeofday({1373626008, 889767}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 247044})
19259      0.003696 write(4, &quot;=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00050_20130712012043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00050_20130712012043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr \230\336\337Q&gt;\204\f\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334y\[email protected]\[email protected]\0068\314\300\1\1/\300\1\1\37\0P\355x.\34[\331zM\360*P\20\[email protected]\210\37\0\0class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00049&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;&quot;..., 4096) = 4096
19259      0.004629 gettimeofday({1373626008, 898432}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000531 gettimeofday({1373626008, 899298}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000456 write(4, &quot; icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a class=\&quot;badge badge-important\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-11\&quot; onclick=\&quot;javascript: deleteWholeDay($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00043&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00043_20130711233543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00043_20130711233543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00042&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00042_20130711232043.pcap\&quot;&gt;&lt;i clas&quot;..., 4096) = 4096
19259      0.007142 gettimeofday({1373626008, 907232}, NULL) = 0
19259      0.000348 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000533 gettimeofday({1373626008, 908106}, NULL) = 0
19259      0.000415 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000523 gettimeofday({1373626008, 909043}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000504 gettimeofday({1373626008, 909874}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.002425 write(4, &quot;elete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass \230\336\337Q\316\231\r\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334z\[email protected]\[email protected]\0068\305\300\1\1/\300\1\1\37\0P\355x.\34y\306zM\360*P\20\[email protected]\210\37\0\0maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00036&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;19.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00036_20130711215043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00036_20130711215043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00035&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;18.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00035_20130711213543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#&quot;..., 4096) = 4096
19259      0.001827 gettimeofday({1373626008, 914455}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000527 gettimeofday({1373626008, 915309}, NULL) = 0
19259      0.011861 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000567 gettimeofday({1373626008, 927739}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000451 write(4, &quot;p\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00026&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;16 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00026_20130711160054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00026_20130711160054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass\230\336\337Q\201\233\r\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334z\[email protected]\[email protected]\0068\302\300\1\1/\300\1\1\37\0P\355x.\34\212\342zM\360*P\20\[email protected]\210\37\0\0 maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00025&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;15.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00025_20130711154554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-whi&quot;..., 4096) = 4096
19259      0.008763 gettimeofday({1373626008, 937294}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000534 gettimeofday({1373626008, 938164}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000500 gettimeofday({1373626008, 938990}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000452 write(4, &quot;on-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00018&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00018_20130711140054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00018_20130711140054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00017&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00017_20130711134554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00017_2013071&quot;..., 4096) = 4096
19259      0.007411 gettimeofday({1373626008, 947189}, NULL) = 0
19259      0.000335 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000526 gettimeofday({1373626008, 948043}, NULL) = 0
19259      0.000398 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000526 gettimeofday({1373626008, 948969}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 162604})
19259      0.107586 gettimeofday({1373626009, 66739}, NULL) = 0
19259      0.040009 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.039990 gettimeofday({1373626009, 146718}, NULL) = 0
19259      0.050040 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.040026 write(4, &quot;ss=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00011&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.\230\336\337Qi\236\r\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334z\[email protected]\[email protected]\0068\275\300\1\1/\300\1\1\37\0P\355x.\34\247fzM\360*P\20\[email protected]\210\37\0\0001.47/tmp_file/2013-07-11/REC_00011_20130711121554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00011_20130711121554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00010&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00010_20130711120054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/&quot;..., 4096) = 4096
19259      0.049943 gettimeofday({1373626009, 287548}, NULL) = 0
19259      0.032669 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246950})
19259      0.027768 gettimeofday({1373626009, 345130}, NULL) = 0
19259      0.039567 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.040003 gettimeofday({1373626009, 422580}, NULL) = 0
19259      0.020035 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.030071 write(4, &quot;ong&gt;Current capture since :&lt;/strong&gt;&lt;div style=&#39;text-align: center&#39;&gt;\n1 d. 03:00:55&lt;/div&gt;&lt;hr /&gt;\n&lt;strong&gt;Instant Write Speed :&lt;/strong&gt; 24.9 KB/s&lt;br /&gt;\n&lt;strong&gt;Instant Remaining Time :&lt;/strong&gt;&lt;br /&gt;&lt;div style=&#39;text-align: center&#39;&gt;210 d. 07:00:45&lt;/div&gt;&lt;hr /&gt;\n&lt;strong&gt;Estimated Time Remaining (1h)&lt;/strong&gt;&lt;div style=&#39;text-align:center&#39;&gt;139 d. 18:11:44&lt;/div&gt;\n\r\n0\r\n\r\n\231\336\337Q\323\320\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\[email protected]\[email protected]\6q\227\300\1\1/\300\1\1\37\0P\355|\tw\376\254_{\243\323P\20\[email protected]\210\37\0\0HTTP/1.1 200 OK\r\nX-Powered-By: PHP/5.4.4-14\r\nExpires: Thu, 19 Nov 1981 08:52:00 GMT\r\nCache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0\r\nPragma: no-cache\r\nContent-type: text/html\r\nTransfer-Encoding: chunked\r\nDate: Fri, 12 Jul 2013 10:46:49 GMT\r\nServer: lighttpd/1.4.31\r\n\r\n5000\r\n                       Up Time : 03:13:30####SEPARATOR####\r\n20130712_00082(Size : 308 MB)&lt;br /&gt;\n&lt;hr /&gt;&lt;table class=\&quot;table table-striped table-hover table-condensed\&quot;&gt;&lt;tr&gt;\r\n\t\t&lt;th style=\&quot;width: 50%\&quot;&gt;Record.&lt;/th&gt;\r\n\t\t&lt;th&gt;Size&lt;/th&gt;\r\n\t\t&lt;th&gt;Action&lt;/th&gt;\r\n\t&lt;/tr&gt;&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;&quot;..., 4096) = 4096
19259      0.060167 gettimeofday({1373626009, 536059}, NULL) = 0
19259      0.028547 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.030944 gettimeofday({1373626009, 594786}, NULL) = 0
19259      0.030407 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.040116 gettimeofday({1373626009, 666756}, NULL) = 0
19259      2.040005 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249946})
19259      0.039731 write(4, &quot;2080543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00077_20130712080543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00076&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00076_20130712075043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00076_20130712075043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maC\231\336\337Q5\322\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\[email protected]\[email protected]\6q\224\300\1\1/\300\1\1\37\0P\355|\tx\17\310_{\243\323P\20\[email protected]\210\37\0\0lass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00074&lt;/td&gt;\r\n\t\t\t\t&lt;td&quot;..., 4096) = 4096
19259      0.027556 gettimeofday({1373626011, 776733}, NULL) = 0
19259      0.045110 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249965})
19259      0.043732 gettimeofday({1373626011, 853961}, NULL) = 0
19259      0.003959 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000553 write(4, &quot;\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00069_20130712060543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00068&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00068_20130712055043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00068_20130712055043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00067&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-&quot;..., 4096) = 4096
19259      0.002015 gettimeofday({1373626011, 859858}, NULL) = 0
19259      0.005140 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000706 gettimeofday({1373626011, 865704}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000565 gettimeofday({1373626011, 866727}, NULL) = 0
19259      0.000496 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000563 gettimeofday({1373626011, 867688}, NULL) = 0
19259      0.000356 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000532 write(4, &quot;20130712042043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00061&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; \231\336\337Q3\325\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334A&lt;@\[email protected]\6q\217\300\1\1/\300\1\1\37\0P\355|\tx,L_{\243\323P\20\[email protected]\210\37\0\0href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00061_20130712040543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00061_20130712040543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00060&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;29.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00060_20130712035043.pcap\&quot;&gt;&lt;i class=\&quot;icon-d&quot;..., 4096) = 4096
19259      0.008699 gettimeofday({1373626011, 877284}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000586 gettimeofday({1373626011, 878238}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000559 gettimeofday({1373626011, 879157}, NULL) = 0
19259      0.000359 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000491 write(4, &quot;file/2013-07-12/REC_00054_20130712022043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00053&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00053_20130712020543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00053_20130712020543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00052&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;26.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-succe\231\336\337QA\327\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\[email protected]\[email protected]\6q\214\300\1\1/\300\1\1\37\0P\355|\tx=h_{\243\323P\20\[email protected]\210\37\0\0ss\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00052_20130712015&quot;..., 4096) = 4096
19259      0.007261 gettimeofday({1373626011, 887277}, NULL) = 0
19259      0.000379 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000572 gettimeofday({1373626011, 888220}, NULL) = 0
19259      0.000363 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000558 gettimeofday({1373626011, 889141}, NULL) = 0
19259      0.000360 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000546 gettimeofday({1373626011, 890047}, NULL) = 0
19259      0.000359 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.006913 gettimeofday({1373626011, 897329}, NULL) = 0
19259      0.000379 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000565 gettimeofday({1373626011, 898262}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 239959})
19259      0.010745 gettimeofday({1373626011, 909378}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 129676})
19259      0.120990 write(4, &quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00046&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00046_20130712002043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00046_20130712002043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00045&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00045_20130712000543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/&quot;..., 4096) = 4096
19259      0.003456 gettimeofday({1373626012, 34255}, NULL) = 0
19259      0.000451 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000603 gettimeofday({1373626012, 35250}, NULL) = 0
19259      0.000367 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.011678 write(4, &quot;10:46:51 GMT\r\nServer: lighttpd/1.4.31\r\n\r\n15cf\r\nUp Time : 03:13:28####SEPARATOR####\r\n&lt;div class=\&quot;span4 well\&quot;&gt;\r\n    &lt;h3&gt;&lt;img src=\&quot;./img/info.png\&quot; width=\&quot;32px\&quot;/&gt; Info&lt;/h3&gt;\r\n    Hostname : &lt;strong&gt;raspberrypi\n&lt;/strong&gt;&lt;br /&gt;\nDistribution : &lt;strong&gt;Debian GNU/Linux 7.0 (wheezy)&lt;/strong&gt;&lt;br /&gt;\nKernel Version : &lt;strong&gt;3.6.11+\n&lt;/strong&gt;&lt;br /&gt;\nControl Center Daemon : &lt;span class=&#39;badge badge-success&#39;&gt;On&lt;/span&gt;&lt;br /&gt;\nFile Analyzer Daemon : &lt;span class=&#39;badge badge-success&#39;&gt;On&lt;/span&gt;&lt;br /&gt;\n&lt;a href=&#39;./controlCenterHystory.php&#39;&gt;View graphical hystory&lt;/a&gt;\n&lt;/div&gt;\r\n&lt;div class=\&quot;span4 well\&quot;&gt;\r\n    &lt;h3&gt;&lt;img src=\&quot;./img/cpu_temp.png\&quot; width=\&quot;32px\&quot;/&gt; Temperature&lt;/h3&gt;\r\n    Temperature (\302\260C) : &lt;strong&gt;56.2\302\260&lt;/strong&gt;&lt;br /&gt;Temperature Max (\302\260C) : &lt;strong&gt;85\302\260&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-success progress-striped\&quot;&gt;\r\n\t\t\t\t\t&lt;div class=\&quot;bar\&quot; style=\&quot;width: 66%\&quot;&gt;66%&lt;/div&gt;\r\n\t\t\t\t&lt;/div&gt;&lt;/div&gt;\r\n&lt;div class=\&quot;span4 trcc_time well\&quot;&gt;\r\n    &lt;h3&gt;&lt;img src=\&quot;./img/clock.png\&quot; width=\&quot;32px\&quot;/&gt; Server Time&lt;/h3&gt;\r\n    Date : &lt;strong&gt;12/07/201&quot;..., 4096) = 4096
19259      0.001986 gettimeofday({1373626012, 49277}, NULL) = 0
19259      0.000424 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.005634 gettimeofday({1373626012, 55409}, NULL) = 0
19259      0.000464 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000602 gettimeofday({1373626012, 56400}, NULL) = 0
19259      0.000456 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000591 gettimeofday({1373626012, 57454}, NULL) = 0
19259      0.000368 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000546 gettimeofday({1373626012, 58363}, NULL) = 0
19259      0.000358 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.007903 gettimeofday({1373626012, 66715}, NULL) = 0
19259      0.000490 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000581 gettimeofday({1373626012, 67692}, NULL) = 0
19259      0.000357 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000589 gettimeofday({1373626012, 68681}, NULL) = 0
19259      0.000400 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 192890})
19259      0.058138 gettimeofday({1373626012, 127226}, NULL) = 0
19259      0.000428 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.001330 write(4, &quot;                           Free : &lt;strong&gt;643.9 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Format : &lt;strong&gt;ext4&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress\234\336\337Q\23q\0\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\0210\300\1\1/\300\1\1\37\0P\355\177\321dp,\246\254KkP\20\[email protected]\210\37\0\0-striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 77.2%\&quot; title=\&quot;2798520 KBytes\&quot;&gt;77.2%&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-success\&quot; style=\&quot;width: 22.8%\&quot; title=\&quot;643872 KBytes\&quot;&gt;22.8%&lt;/div&gt;\r\n\t\t\t&lt;/div&gt;&lt;/div&gt;&lt;div class=\&quot;span3 well\&quot; style=\&quot;background: #FFF\&quot;&gt;\r\n                            &lt;h4&gt;Mounted : &lt;span style=\&quot;color: blue\&quot;&gt;/boot&lt;/span&gt;&lt;/h4&gt;\r\n                            Total : &lt;strong&gt;57.3 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Used : &lt;strong&gt;19 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Free : &lt;strong&gt;38.3 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Format : &lt;strong&gt;vfat&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 33.1%\&quot; title=\&quot;18960 KBytes\&quot;&gt;33.1%&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-success\&quot; style=\&quot;width: 66.9&quot;..., 4096) = 4096
19259      0.011790 gettimeofday({1373626012, 140781}, NULL) = 0
19259      0.000434 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000591 gettimeofday({1373626012, 141751}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000507 write(4, &quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00079&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;50.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding&quot;..., 4096) = 4096
19259      0.014626 gettimeofday({1373626012, 157257}, NULL) = 0
19259      0.000463 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000596 gettimeofday({1373626012, 158310}, NULL) = 0
19259      0.000365 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000564 gettimeofday({1373626012, 159239}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000498 write(4, &quot;ap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-\234\336\337Q\r\346\1\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334z\[email protected]\[email protected]\0068\263\300\1\1/\300\1\1\37\0P\355x.\34\326\332zM\362\25P\20\1m\210\37\0\0path=\&quot;/var/www/tmp_file/2013-07-12/REC_00072_20130712065043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00071&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00070&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.4 MB&lt;/&quot;..., 4096) = 4096
19259      0.007144 gettimeofday({1373626012, 167247}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000581 gettimeofday({1373626012, 168198}, NULL) = 0
19259      0.000359 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000552 gettimeofday({1373626012, 169108}, NULL) = 0
19259      0.000352 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000491 write(4, &quot;a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00065_20130712050543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00064&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.1 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; fr\234\336\337Q^\347\1\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334z\[email protected]\[email protected]\0068\260\300\1\1/\300\1\1\37\0P\355x.\34\347\366zM\362\25P\20\1m\210\37\0\0izb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00063&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;&quot;..., 4096) = 4096
19259      0.007296 gettimeofday({1373626012, 177256}, NULL) = 0
19259      0.000382 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000575 gettimeofday({1373626012, 178204}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000559 gettimeofday({1373626012, 179125}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000504 write(4, &quot;eleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00058_20130712032043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00057&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00056&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00056_20130712025043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-&quot;..., 4096) = 4096
19259      0.008118 gettimeofday({1373626012, 188174}, NULL) = 0
19259      0.000494 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.000693 gettimeofday({1373626012, 189298}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000563 gettimeofday({1373626012, 190224}, NULL) = 0
19259      0.000366 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000545 gettimeofday({1373626012, 191130}, NULL) = 0
19259      0.006055 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 239233})
19259      0.011491 gettimeofday({1373626012, 208685}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246728})
19259      0.003977 write(4, &quot;07-12/REC_00050_20130712012043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr cl\234\336\337QI\352\1\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334z @\[email protected]\0068\253\300\1\1/\300\1\1\37\0P\355x.\35\4zzM\362\25P\20\1m\210\37\0\0ass=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00049&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00048&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00048_20130712005043.pcap\&quot;&gt;&lt;i&quot;..., 4096) = 4096
19259      0.005294 gettimeofday({1373626012, 218333}, NULL) = 0
19259      0.000372 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000580 gettimeofday({1373626012, 219278}, NULL) = 0
19259      0.000359 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000556 gettimeofday({1373626012, 220194}, NULL) = 0
19259      0.000409 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000546 write(4, &quot;yle=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00043_20130711233543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00043_20130711233543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00042&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00042_20130711232043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\234\336\337Q\3574\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334z%@\[email protected]\0068\246\300\1\1/\300\1\1\37\0P\355x.\35\26\375zM\362\25P\20\1m\210\37\0\0\&quot;/var/www/tmp_file/2013-07-11/REC_00042_20130711232043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&quot;..., 4096) = 4096
19259      0.006143 gettimeofday({1373626012, 227298}, NULL) = 0
19259      0.000378 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000568 gettimeofday({1373626012, 228236}, NULL) = 0
19259      0.000412 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000612 gettimeofday({1373626012, 229261}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000504 write(4, &quot;ss\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00036_20130711215043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00036_20130711215043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00035&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;18.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00035_20130711213543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00035_20130711213543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00034&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;265.&quot;..., 4096) = 4096
19259      0.006127 gettimeofday({1373626012, 236262}, NULL) = 0
19259      0.000452 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000718 gettimeofday({1373626012, 237433}, NULL) = 0
19259      0.000375 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000565 gettimeofday({1373626012, 238366}, NULL) = 0
19259      0.000363 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000496 write(4, &quot;/REC_00026_20130711160054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00026_20130711160054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass\234\336\337QT7\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334z*@\[email protected]\0068\241\300\1\1/\300\1\1\37\0P\355x.\0353\201zM\362\25P\20\1m\210\37\0\0 maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00025&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;15.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00025_20130711154554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00025_20130711154554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_0&quot;..., 4096) = 4096
19259      0.008047 gettimeofday({1373626012, 247282}, NULL) = 0
19259      0.000382 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000588 gettimeofday({1373626012, 248244}, NULL) = 0
19259      0.000448 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000563 gettimeofday({1373626012, 249253}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000555 gettimeofday({1373626012, 250167}, NULL) = 0
19259      0.000355 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.026499 write(4, &quot;t icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00018_20130711140054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00017&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00017_20130711134554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00017_20130711134554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maCl\234\336\337Q\f9\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\[email protected]\[email protected]\0068\236\300\1\1/\300\1\1\37\0P\355x.\35D\235zM\362\25P\20\1m\210\37\0\0ass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00016&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: &quot;..., 4096) = 4096
19259      0.039896 gettimeofday({1373626012, 326714}, NULL) = 0
19259      0.030032 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.026004 gettimeofday({1373626012, 381149}, NULL) = 0
19259      0.020455 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 138420})
19259      0.115591 gettimeofday({1373626012, 508998}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 183170})
19259      0.068387 write(4, &quot;\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00011_20130711121554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00010&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00010_20130711120054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00010_20130711120054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00009&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;24.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://&quot;..., 4096) = 4096
19259      0.009487 gettimeofday({1373626012, 587212}, NULL) = 0
19259      0.000346 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000537 gettimeofday({1373626012, 588089}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000601 gettimeofday({1373626012, 589025}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000446 write(4, &quot;th&gt;Action&lt;/th&gt;\r\n\t&lt;/tr&gt;&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;javacript: $(&#39;.myHidden&#39;).val(&#39;maClass0&#39;);\&quot;&gt;2013-07-12&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;td&gt;1.1 GB&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-info\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: compressDownload($(this), &#39;192.1.1.47&#39;);\&quot;&gt;&lt;i class=\&quot;icon-briefcase icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a class=\&quot;badge badge-important\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: deleteWholeDay($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00081&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00081_20130712090543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-pa\234\336\337Q\27\306\10\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21,\300\1\1/\300\1\1\37\0P\355\177\321d{\313\246\254MVP\20\1m\210\37\0\0th=\&quot;/var/www/tmp_file/2013-07&quot;..., 4096) = 4096
19259      0.007406 gettimeofday({1373626012, 597214}, NULL) = 0
19259      0.000347 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000537 gettimeofday({1373626012, 598095}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000454 write(4, &quot;style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00074&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;31 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00073&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00073_20130712070543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00073_20130712070543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;&quot;..., 4096) = 4096
19259      0.008322 gettimeofday({1373626012, 607205}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000535 gettimeofday({1373626012, 608077}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000509 gettimeofday({1373626012, 608920}, NULL) = 0
19259      0.000334 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000451 write(4, &quot;badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;m\234\336\337QF\310\10\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21&#39;\300\1\1/\300\1\1\37\0P\355\177\321d\230O\246\254MVP\20\1m\210\37\0\0aClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00066&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00066_20130712052043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00066_20130712052043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=&quot;..., 4096) = 4096
19259      0.007634 gettimeofday({1373626012, 617343}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000535 gettimeofday({1373626012, 618214}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000487 gettimeofday({1373626012, 619024}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000503 gettimeofday({1373626012, 619853}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000484 write(4, &quot;13-07-12/REC_00060_20130712035043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00060_20130712035043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00059&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00059_20130712033543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00059_20130712033543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr clas\234\336\337Q\202\311\10\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21$\300\1\1/\300\1\1\37\0P\355\177\321d\251k\246\254MVP\20\1m\210\37\0\0s=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20&quot;..., 4096) = 4096
19259      0.006550 gettimeofday({1373626012, 627219}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000535 gettimeofday({1373626012, 628093}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000546 write(4, &quot;p://192.1.1.47/tmp_file/2013-07-12/REC_00052_20130712015043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00052_20130712015043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00051&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;25.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00051_20130712013543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00051_20130712013543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00050&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;&quot;..., 4096) = 4096
19259      0.008324 gettimeofday({1373626012, 637297}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 229330})
19259      0.049692 gettimeofday({1373626012, 696804}, NULL) = 0
19259      0.039596 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.049988 gettimeofday({1373626012, 796716}, NULL) = 0
19259      0.060006 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.050163 gettimeofday({1373626012, 896381}, NULL) = 0
19259      0.030374 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.039883 write(4, &quot;ss=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00045_20130712000543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00044&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href\234\336\337Q,\366\t\0B\0\0\0B\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0004\241\[email protected]\[email protected]\6\26\306\300\1\1/\300\1\1\37\0P\355\177\321d\307J\246\254MVP\30\1m\202w\0\0007\r\n\t&lt;/tr&gt;\n\r\n\234\336\337Q\366\16\n\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21\35\300\1\1/\300\1\1\37\0P\355\177\321d\307V\246\254MVP\20\1m\210\37\0\0005568\r\n&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;javacript: $(&#39;.myHidden&#39;).val(&#39;maClass1&#39;);\&quot;&gt;2013-07-11&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;td&gt;738.3 MB&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-info\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-11\&quot; onclick=\&quot;javascript: compressDownload($(this), &#39;192.1.1.47&#39;);\&quot;&gt;&lt;i class=\&quot;icon-briefcase icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a class=\&quot;badge badge-important\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-11\&quot; onclick=\&quot;javascript: deleteWhole&quot;..., 4096) = 4096
19259      0.032132 gettimeofday({1373626012, 990697}, NULL) = 0
19259      0.005177 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000624 gettimeofday({1373626012, 995260}, NULL) = 0
19259      0.000318 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000485 gettimeofday({1373626012, 996059}, NULL) = 0
19259      0.000310 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000719 write(4, &quot;\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00038_20130711222043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00038_20130711222043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00037&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;20 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00037_20130711220543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00037_20130711220543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass \234\336\337Qy\20\n\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]&quot;..., 4096) = 4096
19259      0.001694 gettimeofday({1373626012, 998786}, NULL) = 0
19259      0.000315 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000484 gettimeofday({1373626012, 999580}, NULL) = 0
19259      0.000305 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000476 gettimeofday({1373626013, 361}, NULL) = 0
19259      0.000304 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.005296 write(4, &quot;\37\0P\355\177\321d\343\332\246\254MVP\20\1m\210\37\0\0tp://192.1.1.47/tmp_file/2013-07-11/REC_00031_20130711171554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00031_20130711171554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00028&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;16.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00028_20130711163054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00028_20130711163054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00026&lt;/td&gt;\r\n\t\t\t&quot;..., 4096) = 4096
19259      0.003142 gettimeofday({1373626013, 9108}, NULL) = 0
19259      0.000318 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000501 gettimeofday({1373626013, 9924}, NULL) = 0
19259      0.000312 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000481 gettimeofday({1373626013, 10716}, NULL) = 0
19259      0.000308 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000422 write(4, &quot;7-11/REC_00020_20130711143054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00020_20130711143054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00019&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://\234\336\337Q\341\22\n\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21\25\300\1\1/\300\1\1\37\0P\355\177\321d\364\366\246\254MVP\20\1m\210\37\0\000192.1.1.47/tmp_file/2013-07-11/REC_00019_20130711141554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00019_20130711141554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;2013071&quot;..., 4096) = 4096
19259      0.005768 gettimeofday({1373626013, 17221}, NULL) = 0
19259      0.000320 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000508 gettimeofday({1373626013, 18043}, NULL) = 0
19259      0.000310 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000483 gettimeofday({1373626013, 18834}, NULL) = 0
19259      0.000305 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000416 write(4, &quot;-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00013_20130711124554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00012&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00012_20130711123054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00012_20130711123054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00011&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.\234\336\337Q\222\24\n\0\352&quot;..., 4096) = 4096
19259      0.003096 gettimeofday({1373626013, 22657}, NULL) = 0
19259      0.000320 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000491 gettimeofday({1373626013, 23459}, NULL) = 0
19259      0.000303 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000562 gettimeofday({1373626013, 24329}, NULL) = 0
19259      0.005731 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 91391})
19259      0.159431 gettimeofday({1373626013, 189494}, NULL) = 0
19259      0.001339 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250875 gettimeofday({1373626013, 441715}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250860 gettimeofday({1373626013, 692903}, NULL) = 0
19259      0.000333 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250837 gettimeofday({1373626013, 944067}, NULL) = 0
19259      0.000339 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 162214})
19259      0.102947 gettimeofday({1373626014, 47376}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000564 gettimeofday({1373626014, 48307}, NULL) = 0
19259      0.000365 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000547 gettimeofday({1373626014, 49220}, NULL) = 0
19259      0.007718 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249962})
19259      0.020009 gettimeofday({1373626014, 82811}, NULL) = 0
19259      0.035569 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 236747})
19259      0.034874 gettimeofday({1373626014, 156045}, NULL) = 0
19259      0.023365 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.027799 gettimeofday({1373626014, 207208}, NULL) = 0
19259      0.038432 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.039961 gettimeofday({1373626014, 286720}, NULL) = 0
19259      0.038518 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.008602 gettimeofday({1373626014, 330561}, NULL) = 0
19259      0.032891 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 85158})
19259      0.197180 gettimeofday({1373626014, 566717}, NULL) = 0
19259      0.032802 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.039980 write(4, &quot;ipT\3220\335\203\10\0E\0\0([email protected]\0\200\6K-\300\1\1\37\300\1\1/\355x\0PzM\362\25.\35h\251P\20?\255\374\343\0\0\0\0\0\0\0\0\234\336\337Q\1A\r\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0([email protected]\0\200\6K(\300\1\1\37\300\1\1/\355\177\0P\246\254MV\321e\34\306P\20&gt;\303\36\302\0\0\0\0\0\0\0\0\234\336\337Q\33\23\17\0&amp;\2\0\0&amp;\2\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\2\30\241\[email protected]\[email protected]\6\24\322\300\1\1/\300\1\1\37\0P\355\177\321e\34\306\246\254MVP\30\1m\204[\0\0002\r\n&gt;\n\r\n1dd\r\n&lt;/table&gt;####SEPARATOR####\r\n&lt;strong&gt;Current file since :&lt;/strong&gt;&lt;div style=&#39;text-align: center&#39;&gt;\n0 d. 03:26:09&lt;/div&gt;\n&lt;strong&gt;Current capture since :&lt;/strong&gt;&lt;div style=&#39;text-align: center&#39;&gt;\n1 d. 03:00:58&lt;/div&gt;&lt;hr /&gt;\n&lt;strong&gt;Instant Write Speed :&lt;/strong&gt; 24.9 KB/s&lt;br /&gt;\n&lt;strong&gt;Instant Remaining Time :&lt;/strong&gt;&lt;br /&gt;&lt;div style=&#39;text-align: center&#39;&gt;210 d. 06:37:30&lt;/div&gt;&lt;hr /&gt;\n&lt;strong&gt;Estimated Time Remaining (1h)&lt;/strong&gt;&lt;div style=&#39;text-align:center&#39;&gt;139 d. 18:11:41&lt;/div&gt;\n\r\n0\r\n\r\n\235\336\337Q\335\340\2\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0([email protected]\0\200\6K%\300\1\1\37\300\1\1/\355\177\0P\246\254MV\321e\36\266P\[email protected])\33l\0\0\0\0\0\0\0\0\236\336\337Q\361|\0\0 \2\0\0 \2\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\2\22-`@\0\200\6I5\300\1\1\37\300\1\1/\355\177\0P\246\254MV\321e\36\266P\[email protected])J\3\0\0POST /ajax/update.php HTTP/1.1\r\nHost: 192.1.1.47\r\nConnection: keep-alive\r\nContent-Length: 12\r\nOrigin: http://192.1.1.47\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/&quot;..., 4096) = 4096
19259      0.040006 gettimeofday({1373626014, 671728}, NULL) = 0
19259      2.020277 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259      0.034630 gettimeofday({1373626016, 726712}, NULL) = 0
19259      0.035496 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.039624 write(4, &quot;r /&gt;\n&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;5mn : &lt;strong&gt;2.22&lt;/strong&gt;&lt;br /&gt;\n&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;15mn : &lt;strong&gt;2.21&lt;/strong&gt;&lt;br /&gt;\nRunning Processes : &lt;strong&gt;94&lt;/strong&gt;&lt;br /&gt;\nCurrent Freq (MHz) : &lt;strong&gt;900MHz&lt;/strong&gt;&lt;br /&gt;\nMax Freq (MHz) : &lt;strong&gt;900MHz&lt;/strong&gt;&lt;br /&gt;\nGovernor : &lt;strong&gt;ondemand&lt;/strong&gt;&lt;br /&gt;\n&lt;/div&gt;\r\n&lt;div class=\&quot;span4 trcc_ramload well\&quot;&gt;\r\n\t&lt;h3&gt;&lt;img src=\&quot;./img/memory.png\&quot; width=\&quot;32px\&quot;/&gt; RAM&lt;/h3&gt;\r\n\t&lt;span class=\&quot;badge badge-success\&quot;&gt;&amp;nbsp;&lt;/span&gt; Free : &lt;strong&gt;16 MB&lt;/strong&gt;&lt;br /&gt;&lt;span class=\&quot;badge badge-info\&quot;&gt;&amp;nbsp;&lt;/span&gt; Used : &lt;strong&gt;469 MB&lt;/strong&gt;&lt;br /&gt;&lt;span class=\&quot;badge badge-warning\&quot;&gt;&amp;nbsp;&lt;/span&gt; Buffer : &lt;strong&gt;24 MB&lt;/strong&gt;&lt;br /&gt;&lt;span class=\&quot;badge badge-important\&quot;&gt;&amp;nbsp;&lt;/span&gt; Cache : &lt;strong&gt;359 MB&lt;/strong&gt;&lt;br /&gt;&lt;span class=\&quot;badge\&quot;&gt;&amp;nbsp;&lt;/span&gt; Total : &lt;strong&gt;485 MB&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 17%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-warning\&quot; style=\&quot;width: 4%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-danger\&quot; style=\&quot;&quot;..., 4096) = 4096
19259      0.029966 gettimeofday({1373626016, 832631}, NULL) = 0
19259      0.023009 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000693 gettimeofday({1373626016, 850624}, NULL) = 0
19259      0.000366 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000543 gettimeofday({1373626016, 851530}, NULL) = 0
19259      0.000360 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000559 gettimeofday({1373626016, 852449}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.001152 gettimeofday({1373626016, 854009}, NULL) = 0
19259      0.012978 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000643 write(4, &quot;      Format : &lt;strong&gt;ext4&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 0.8%\&quot; title=\&quot;3771268 KBytes\&quot;&gt;0.8%&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-success\&quot; style=\&quot;width: 99.2%\&quot; title=\&quot;452500976 KBytes\&quot;&gt;9\236\336\337Q\244\376\7\0m\0\0\0m\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0_\241\[email protected]\[email protected]\6\26\205\300\1\1/\300\1\1\37\0P\355\177\321e5\206\246\[email protected]\30\1\233\202\242\0\0009.2%&lt;/div&gt;\r\n\t\t\t&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;\t&lt;/div&gt;\r\n&lt;/div&gt;\r\n0\r\n\r\n\236\336\337Q\365\2\10\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0([email protected]\0\200\6K\26\300\1\1\37\300\1\1/\355\177\0P\246\[email protected]\321e5\275P\[email protected])\2{\0\0\0\0\0\0\0\0\236\336\337Q\320\32\n\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\[email protected]\[email protected]\0068\226\300\1\1/\300\1\1\37\0P\355x.\35h\251zM\364\0P\20\1\233\210\37\0\0HTTP/1.1 200 OK\r\nX-Powered-By: PHP/5.4.4-14\r\nExpires: Thu, 19 Nov 1981 08:52:00 GMT\r\nCache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0\r\nPragma: no-cache\r\nContent-type: text/html\r\nTransfer-Encoding: chunked\r\nDate: Fri, 12 Jul 2013 10:46:54 GMT\r\nServer: lighttpd/1.4.31\r\n\r\n5008\r\n                       Up Time : 03:13:36####SEPARATOR####\r\n20130712_00082(Size : 308.1 MB)&lt;br /&gt;\n&lt;hr /&gt;&lt;table class=\&quot;table table-striped table-hover table-condensed\&quot;&gt;&lt;tr&gt;\r\n\t\t&lt;th style=\&quot;width: 5&quot;..., 4096) = 4096
19259      0.009379 gettimeofday({1373626016, 877071}, NULL) = 0
19259      0.000497 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000610 gettimeofday({1373626016, 878072}, NULL) = 0
19259      0.000366 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000564 gettimeofday({1373626016, 878999}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000492 write(4, &quot;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00077_20130712080543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00077_20130712080543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00076&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00076_20130712075043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00076_20130712075043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;m\236\336\337Qf\34\n\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\[email protected]\[email protected]\0068\223\300\1\1/\300\1\1\37\0P\355x.\35y\305zM\364\0P\20\1\233\210\37\0\0aClas&quot;..., 4096) = 4096
19259      0.007411 gettimeofday({1373626016, 887272}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000578 gettimeofday({1373626016, 888218}, NULL) = 0
19259      0.000358 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000498 write(4, &quot;1.47/tmp_file/2013-07-12/REC_00069_20130712060543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00069_20130712060543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00068&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00068_20130712055043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00068_20130712055043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00067&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style&quot;..., 4096) = 4096
19259      0.008177 gettimeofday({1373626016, 897259}, NULL) = 0
19259      0.000380 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000583 gettimeofday({1373626016, 898219}, NULL) = 0
19259      0.000368 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000564 gettimeofday({1373626016, 899145}, NULL) = 0
19259      0.000359 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000546 gettimeofday({1373626016, 900051}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.006840 write(4, &quot;ss=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00062_20130712042043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00061&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\236\336\337Q\221\36\n\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\[email protected]\[email protected]\0068\216\300\1\1/\300\1\1\37\0P\355x.\35\226IzM\364\0P\20\1\233\210\37\0\0\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00061_20130712040543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00061_20130712040543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00060&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;29.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-succes&quot;..., 4096) = 4096
19259      0.002251 gettimeofday({1373626016, 909508}, NULL) = 0
19259      0.000371 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.007597 gettimeofday({1373626016, 917480}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000578 gettimeofday({1373626016, 918427}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000493 write(4, &quot; style=\&quot;width: 50%\&quot;&gt;Record.&lt;/th&gt;\r\n\t\t&lt;th&gt;Size&lt;/th&gt;\r\n\t\t&lt;th&gt;Action&lt;/th&gt;\r\n\t&lt;/tr&gt;&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;javacript: $(&#39;.myHidden&#39;).val(&#39;maClass0&#39;);\&quot;&gt;2013-07-12&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;td&gt;1.1 GB&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-info\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: compressDownload($(this), &#39;192.1.1.47&#39;);\&quot;&gt;&lt;i class=\&quot;icon-briefcase icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a class=\&quot;badge badge-important\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: deleteWholeDay($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00081&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00081_20130712090543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-\240\336\337Q\341\n\r\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\21\5\300\1\1/\300&quot;..., 4096) = 4096
19259      0.007974 gettimeofday({1373626016, 927261}, NULL) = 0
19259      0.000375 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000585 gettimeofday({1373626016, 928216}, NULL) = 0
19259      0.000365 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000502 write(4, &quot;\254Q+P\20\1\311\210\37\0\0aClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00074&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;31 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00073&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00073_20130712070543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00073_20130712070543.pcap\&quot; onclick=\&quot;javascript: delete_file(&quot;..., 4096) = 4096
19259      0.005955 gettimeofday({1373626016, 935046}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000570 gettimeofday({1373626016, 935986}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000751 gettimeofday({1373626016, 937124}, NULL) = 0
19259      0.000397 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246879})
19259      0.004057 gettimeofday({1373626016, 941761}, NULL) = 0
19259      0.003494 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.000624 gettimeofday({1373626016, 945671}, NULL) = 0
19259      0.000444 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000508 write(4, &quot;&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\240\336\337Q\340x\r\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6K\0\300\1\1\37\300\1\1/\355x\0PzM\364\0.\36\21JP\20?\255RW\0\0\0\0\0\0\0\0\240\336\337QsA\16\0&lt;\0\0\0&lt;\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0.\241\[email protected]\[email protected]\6\26\245\300\1\1/\300\1\1\37\0P\355\177\321e\206\370\246\254Q+P\30\1\311\202q\0\0001\r\n\n\r\n\240\336\337Q\243Q\16\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\366\300\1\1/\300\1\1\37\0P\355\177\321e\206\376\246\254Q+P\20\1\311\210\37\0\0005568\r\n&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;javacript: $(&#39;.myHidden&#39;).val(&#39;maClass1&#39;);\&quot;&gt;2013-07-11&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;td&gt;738.3 MB&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-info\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-11\&quot; onclick=\&quot;javascript: compressDownload($(this), &#39;192.1.1.47&#39;);\&quot;&gt;&lt;i class=\&quot;icon-briefcase icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a class=\&quot;badge badg&quot;..., 4096) = 4096
19259      0.010531 gettimeofday({1373626016, 957180}, NULL) = 0
19259      0.000398 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000585 gettimeofday({1373626016, 958137}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000509 write(4, &quot;le=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00038&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;20.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00038_20130711222043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00038_20130711222043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00037&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;20 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00037_20130711220543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00037_20130711220543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remov&quot;..., 4096) = 4096
19259      0.008264 gettimeofday({1373626016, 967280}, NULL) = 0
19259      0.000379 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000570 gettimeofday({1373626016, 968221}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000563 gettimeofday({1373626016, 969147}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000558 gettimeofday({1373626016, 970069}, NULL) = 0
19259      0.000370 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.006854 write(4, &quot;ght;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;ht\240\336\337QVT\16\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\377\300\1\1\37\300\1\1/\355\177\0P\246\254Q+\321e\214\262P\[email protected])\251\232\0\0\0\0\0\0\0\0\240\336\337Q\353T\16\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\361\300\1\1/\300\1\1\37\0P\355\177\321e\243\202\246\254Q+P\20\1\311\210\37\0\0tp://192.1.1.47/tmp_file/2013-07-11/REC_00031_20130711171554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00031_20130711171554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00028&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;16.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00028_20130711163054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00028_20130711163054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this&quot;..., 4096) = 4096
19259      0.002309 gettimeofday({1373626016, 979604}, NULL) = 0
19259      0.007326 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000713 gettimeofday({1373626016, 987643}, NULL) = 0
19259      0.000367 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000556 gettimeofday({1373626016, 988560}, NULL) = 0
19259      0.000409 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000541 write(4, &quot;le=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00020_20130711143054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00020_20130711143054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00019&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://\240\336\337Q5V\16\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\356\300\1\1/\300\1\1\37\0P\355\177\321e\264\236\246\254Q+P\20\1\311\210\37\0\000192.1.1.47/tmp_file/2013-07-11/REC_00019_20130711141554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00019_20130711141554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/&quot;..., 4096) = 4096
19259      0.003579 gettimeofday({1373626016, 993097}, NULL) = 0
19259      0.000375 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.003482 gettimeofday({1373626016, 997043}, NULL) = 0
19259      0.000486 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000604 gettimeofday({1373626016, 998040}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000509 write(4, &quot;=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00013_20130711124554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00013_20130711124554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00012&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00012_20130711123054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00012_20130711123054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00011&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.7 MB&lt;/td&gt;\r\n&quot;..., 4096) = 4096
19259      0.008325 gettimeofday({1373626017, 7239}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000567 gettimeofday({1373626017, 8178}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 103380})
19259      0.147328 gettimeofday({1373626017, 156165}, NULL) = 0
19259      0.000694 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000767 gettimeofday({1373626017, 157329}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000544 gettimeofday({1373626017, 158235}, NULL) = 0
19259      0.001438 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 56716})
19259      0.194067 gettimeofday({1373626017, 353731}, NULL) = 0
19259      0.000346 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250906 gettimeofday({1373626017, 605012}, NULL) = 0
19259      0.000383 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250861 gettimeofday({1373626017, 856221}, NULL) = 0
19259      0.000339 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250870 gettimeofday({1373626018, 107421}, NULL) = 0
19259      0.000308 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 228098})
19259      0.029698 gettimeofday({1373626018, 137448}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000509 gettimeofday({1373626018, 138290}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000496 gettimeofday({1373626018, 139115}, NULL) = 0
19259      0.000326 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000490 gettimeofday({1373626018, 139928}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 181113})
19259      0.070394 gettimeofday({1373626018, 210664}, NULL) = 0
19259      0.000375 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000723 write(4, &quot;_20130711110054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www\240\336\337QP^\16\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\374\300\1\1\37\300\1\1/\355\177\0P\246\254Q+\321e\334nP\[email protected])Y\336\0\0\0\0\0\0\0\0\241\336\337Q\245[\2\0&amp;\2\0\0&amp;\2\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\2\30\241\[email protected]\[email protected]\6\24\253\300\1\1/\300\1\1\37\0P\355\177\321e\334n\246\254Q+P\30\1\311\204[\0\0002\r\n&gt;\n\r\n1dd\r\n&lt;/table&gt;####SEPARATOR####\r\n&lt;strong&gt;Current file since :&lt;/strong&gt;&lt;div style=&#39;text-align: center&#39;&gt;\n0 d. 03:26:14&lt;/div&gt;\n&lt;strong&gt;Current capture since :&lt;/strong&gt;&lt;div style=&#39;text-align: center&#39;&gt;\n1 d. 03:01:03&lt;/div&gt;&lt;hr /&gt;\n&lt;strong&gt;Instant Write Speed :&lt;/strong&gt; 24.9 KB/s&lt;br /&gt;\n&lt;strong&gt;Instant Remaining Time :&lt;/strong&gt;&lt;br /&gt;&lt;div style=&#39;text-align: center&#39;&gt;210 d. 07:27:22&lt;/div&gt;&lt;hr /&gt;\n&lt;strong&gt;Estimated Time Remaining (1h)&lt;/strong&gt;&lt;div style=&#39;text-align:center&#39;&gt;139 d. 18:11:39&lt;/div&gt;\n\r\n0\r\n\r\n\241\336\337QU]\2\0006\0\0\0006\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0([email protected]\[email protected]\6w+\300\1\1/\300\1\1\37\0P\355|\tx\247K_{\243\323P\21\[email protected]\202k\0\0\241\336\337Q\343`\2\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\371\300\1\1\37\300\1\1/\355|\0P_{\243\323\tx\247LP\[email protected])Kz\0\0\0\0\0\0\0\0\241\336\337Q\236b\5\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\370\300\1\1\37\300\1\1/\355\177\0P\246\254Q+\321e\336^P\20?\255Xj\0\0\0\0\0\0\0\0\242\336\337Q\371\363\1\0&lt;\0\0&quot;..., 4096) = 4096
19259      0.005468 gettimeofday({1373626018, 217224}, NULL) = 0
19259      0.000344 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000537 gettimeofday({1373626018, 218097}, NULL) = 0
19259      0.000408 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000523 gettimeofday({1373626018, 219029}, NULL) = 0
19259      0.000331 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.007529 write(4, &quot;\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00079&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;50.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00078&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;55.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href\242\336\337Q\356,\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\343\300\1\1/\300\1\1\37\0P\355\177\321e\351\306\246\254S\26P\20\1\366\210\37\0\0=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00078_20130712082043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/t&quot;..., 4096) = 4096
19259      0.001853 gettimeofday({1373626018, 228748}, NULL) = 0
19259      0.000421 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000543 gettimeofday({1373626018, 229706}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000459 write(4, &quot;y: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00071&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00070&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00070_20130712062043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00070_20130712062043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-w&quot;..., 4096) = 4096
19259      0.006779 gettimeofday({1373626018, 237282}, NULL) = 0
19259      0.000349 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000534 gettimeofday({1373626018, 238157}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000507 gettimeofday({1373626018, 238994}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000451 write(4, &quot;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; \242\336\337Q6/\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\336\300\1\1/\300\1\1\37\0P\355\177\321f\6J\246\254S\26P\20\1\366\210\37\0\0frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00063&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00063_20130712043543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00063_20130712043543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass m&quot;..., 4096) = 4096
19259      0.007434 gettimeofday({1373626018, 247211}, NULL) = 0
19259      0.000339 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000524 gettimeofday({1373626018, 248069}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000513 gettimeofday({1373626018, 248910}, NULL) = 0
19259      0.000329 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000515 gettimeofday({1373626018, 249757}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.007076 write(4, &quot;.47/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00056&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00056_20130712025043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFi\242\336\337Q\3271\3\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\361\300\1\1\37\300\1\1/\355\177\0P\246\254S\26\321f\v\376P\[email protected])(c\0\0\0\0\0\0\0\0\242\336\337Q^2\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\333\300\1\1/\300\1\1\37\0P\355\177\321f\27f\246\254S\26P\20\1\366\210\37\0\0le\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00056_20130712025043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&quot;..., 4096) = 4096
19259      0.001956 gettimeofday({1373626018, 259119}, NULL) = 0
19259      0.000339 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000536 gettimeofday({1373626018, 259991}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000501 gettimeofday({1373626018, 260823}, NULL) = 0
19259      0.000412 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 233857})
19259      0.016800 gettimeofday({1373626018, 278038}, NULL) = 0
19259      0.000336 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 247047})
19259      0.003736 write(4, &quot;\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00048&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00048_20130712005043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00048_20130712005043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00047&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;&quot;..., 4096) = 4096
19259      0.004297 gettimeofday({1373626018, 286471}, NULL) = 0
19259      0.000512 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000583 gettimeofday({1373626018, 287499}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000514 gettimeofday({1373626018, 288346}, NULL) = 0
19259      0.000326 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000447 write(4, &quot;\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00042&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00042_20130711232043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\242\336\337QjC\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\324\300\1\1/\300\1\1\37\0P\355\177\321f5S\246\254S\26P\20\1\366\210\37\0\0\&quot;/var/www/tmp_file/2013-07-11/REC_00042_20130711232043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00041&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00041_20130711230543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_&quot;..., 4096) = 4096
19259      0.008099 gettimeofday({1373626018, 297224}, NULL) = 0
19259      0.000346 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000535 gettimeofday({1373626018, 298099}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000511 gettimeofday({1373626018, 298937}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000490 gettimeofday({1373626018, 299754}, NULL) = 0
19259      0.000324 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249981})
19259      0.001604 write(4, &quot;none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00035&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;18.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00035_20130711213543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00035_20130711213543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00034&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;265.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00034_20130711180054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-pa\242\336\337Q\252D\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\321\300\1\1/\300\1\1\37\0P\355\177\321fFo\246\254S\26P\20\1\366\210\37\0\0th=\&quot;/var/www/tmp_file/2013-07-11/REC_00034_20130711180054.pcap\&quot; oncl&quot;..., 4096) = 4096
19259      0.005726 gettimeofday({1373626018, 307418}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000528 gettimeofday({1373626018, 308284}, NULL) = 0
19259      0.000409 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000546 write(4, &quot;lass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00025&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;15.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00025_20130711154554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00025_20130711154554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00024&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00024_20130711153054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00024_20130711153054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;i&quot;..., 4096) = 4096
19259      0.008057 gettimeofday({1373626018, 317305}, NULL) = 0
19259      0.000350 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000538 gettimeofday({1373626018, 318184}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000508 gettimeofday({1373626018, 319020}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000448 write(4, &quot;: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00017_20130711134554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00017_20130711134554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maCl\242\336\337QRG\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\241\[email protected]\[email protected]\6\20\314\300\1\1/\300\1\1\37\0P\355\177\321fb\363\246\254S\26P\20\1\366\210\37\0\0ass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00016&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00016_20130711133054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00016_20130711133054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=&quot;..., 4096) = 4096
19259      0.007471 gettimeofday({1373626018, 327274}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000532 gettimeofday({1373626018, 328144}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000494 gettimeofday({1373626018, 328962}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 91020})
19259      0.159646 gettimeofday({1373626018, 488945}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000503 gettimeofday({1373626018, 489779}, NULL) = 0
19259      0.000322 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 51976})
19259      0.198661 gettimeofday({1373626018, 688758}, NULL) = 0
19259      0.000314 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250838 gettimeofday({1373626018, 939910}, NULL) = 0
19259      0.000336 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 157702})
19259      0.146706 gettimeofday({1373626019, 94198}, NULL) = 0
19259      0.025539 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259      0.024426 gettimeofday({1373626019, 146745}, NULL) = 0
19259      0.030582 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.288927 gettimeofday({1373626019, 461479}, NULL) = 0
19259      0.020587 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 200796})
19259      0.054344 write(4, &quot;.1.47/tmp_file/2013-07-11/REC_00010_20130711120054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00010_20130711120054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00009&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;24.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00009_20130711114554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00009_20130711114554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot;\242\336\337Q\364H\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\242\[email protected]\[email protected]\6\20\311\300\1\1/\300\1\1\37\0P\355\177\321ft\17\246\254S\26P\20\1\366\210\37\0\0 style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;paddin&quot;..., 4096) = 4096
19259      0.001909 gettimeofday({1373626019, 533272}, NULL) = 0
19259      0.000325 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000505 gettimeofday({1373626019, 534094}, NULL) = 0
19259      0.000314 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000436 write(4, &quot;ck=0\r\nPragma: no-cache\r\nContent-type: text/html\r\nTransfer-Encoding: chunked\r\nDate: Fri, 12 Jul 2013 10:46:59 GMT\r\nServer: lighttpd/1.4.31\r\n\r\n15ce\r\nUp Time : 03:13:38####SEPARATOR####\r\n&lt;div class=\&quot;span4 well\&quot;&gt;\r\n    &lt;h3&gt;&lt;img src=\&quot;./img/info.png\&quot; width=\&quot;32px\&quot;/&gt; Info&lt;/h3&gt;\r\n    Hostname : &lt;strong&gt;raspberrypi\n&lt;/strong&gt;&lt;br /&gt;\nDistribution : &lt;strong&gt;Debian GNU/Linux 7.0 (wheezy)&lt;/strong&gt;&lt;br /&gt;\nKernel Version : &lt;strong&gt;3.6.11+\n&lt;/strong&gt;&lt;br /&gt;\nControl Center Daemon : &lt;span class=&#39;badge badge-success&#39;&gt;On&lt;/span&gt;&lt;br /&gt;\nFile Analyzer Daemon : &lt;span class=&#39;badge badge-success&#39;&gt;On&lt;/span&gt;&lt;br /&gt;\n&lt;a href=&#39;./controlCenterHystory.php&#39;&gt;View graphical hystory&lt;/a&gt;\n&lt;/div&gt;\r\n&lt;div class=\&quot;span4 well\&quot;&gt;\r\n    &lt;h3&gt;&lt;img src=\&quot;./img/cpu_temp.png\&quot; width=\&quot;32px\&quot;/&gt; Temperature&lt;/h3&gt;\r\n    Temperature (\302\260C) : &lt;strong&gt;55.7\302\260&lt;/strong&gt;&lt;br /&gt;Temperature Max (\302\260C) : &lt;strong&gt;85\302\260&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-success progress-striped\&quot;&gt;\r\n\t\t\t\t\t&lt;div class=\&quot;bar\&quot; style=\&quot;width: 66%\&quot;&gt;66%&lt;/div&gt;\r\n\t\t\t\t&lt;/div&gt;&lt;/div&gt;\r\n&lt;div class=\&quot;span4 trcc_time well&quot;..., 4096) = 4096
19259      0.009404 gettimeofday({1373626019, 544291}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.003433 gettimeofday({1373626019, 548062}, NULL) = 0
19259      0.000321 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000490 gettimeofday({1373626019, 548866}, NULL) = 0
19259      0.000395 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000489 gettimeofday({1373626019, 549749}, NULL) = 0
19259      0.000310 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      2.258548 gettimeofday({1373626021, 808695}, NULL) = 0
19259      0.000445 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.002850 gettimeofday({1373626021, 811917}, NULL) = 0
19259      0.000346 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000774 gettimeofday({1373626021, 813056}, NULL) = 0
19259      0.000551 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000513 write(4, &quot; &lt;strong&gt;3.6 GB&lt;/strong&gt;&lt;br /&gt;\r\n                            Used : &lt;strong&gt;2.8 GB&lt;/strong&gt;&lt;br /&gt;\r\n                            Free : &lt;strong&gt;643.8 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Format : &lt;strong&gt;ext4&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-\243\336\337QQ\372\7\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\242\[email protected]\[email protected]\6\20\301\300\1\1/\300\1\1\37\0P\355\177\321f\230\33\246\254U\0P\20\2$\210\37\0\0striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 77.2%\&quot; title=\&quot;2798636 KBytes\&quot;&gt;77.2%&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-success\&quot; style=\&quot;width: 22.8%\&quot; title=\&quot;643756 KBytes\&quot;&gt;22.8%&lt;/div&gt;\r\n\t\t\t&lt;/div&gt;&lt;/div&gt;&lt;div class=\&quot;span3 well\&quot; style=\&quot;background: #FFF\&quot;&gt;\r\n                            &lt;h4&gt;Mounted : &lt;span style=\&quot;color: blue\&quot;&gt;/boot&lt;/span&gt;&lt;/h4&gt;\r\n                            Total : &lt;strong&gt;57.3 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Used : &lt;strong&gt;19 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Free : &lt;strong&gt;38.3 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Format : &lt;strong&gt;vfat&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;&quot;..., 4096) = 4096
19259      0.007498 gettimeofday({1373626021, 821602}, NULL) = 0
19259      0.000360 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000561 gettimeofday({1373626021, 822517}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000539 gettimeofday({1373626021, 823397}, NULL) = 0
19259      0.000338 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000479 write(4, &quot;href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-\244\336\337Q\256A\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\242\[email protected]\[email protected]\6\20\275\300\1\1/\300\1\1\37\0P\355\177\321f\243\271\246\254V\353P\20\2R\210\37\0\0path=\&quot;/var/www/tmp_file/2013-07-12/REC_00081_20130712090543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00080&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;37.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00079&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;50.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge &quot;..., 4096) = 4096
19259      0.002039 gettimeofday({1373626021, 826251}, NULL) = 0
19259      0.006135 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000600 gettimeofday({1373626021, 832994}, NULL) = 0
19259      0.000350 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000540 gettimeofday({1373626021, 833876}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000468 write(4, &quot;e\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00073_20130712070543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00072&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;31.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00072_20130712065043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; friz\244\336\337Q3C\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\242\[email protected]\[email protected]\6\20\272\300\1\1/\300\1\1\37\0P\355\177\321f\264\325\246\254V\353P\20\2R\210\37\0\0b-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00072_20130712065043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00071&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013&quot;..., 4096) = 4096
19259      0.002204 gettimeofday({1373626021, 836915}, NULL) = 0
19259      0.000423 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.010035 gettimeofday({1373626021, 847356}, NULL) = 0
19259      0.000355 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000501 write(4, &quot;066_20130712052043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00065&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00065_20130712050543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00065_20130712050543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00064&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.1 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-im&quot;..., 4096) = 4096
19259      0.001927 gettimeofday({1373626021, 850129}, NULL) = 0
19259      0.000345 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000544 gettimeofday({1373626021, 851018}, NULL) = 0
19259      0.000339 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000520 gettimeofday({1373626021, 851878}, NULL) = 0
19259      0.000337 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000528 gettimeofday({1373626021, 852743}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000570 write(4, &quot;\t&lt;/tr&gt;\n&lt;tr cl\244\336\337Q\215E\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\242\[email protected]\[email protected]\6\20\265\300\1\1/\300\1\1\37\0P\355\177\321f\321Y\246\254V\353P\20\2R\210\37\0\0ass=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00058&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00058_20130712032043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00058_20130712032043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00057&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_&quot;..., 4096) = 4096
19259      0.002038 gettimeofday({1373626021, 855754}, NULL) = 0
19259      0.000414 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 98733})
19259      0.151960 gettimeofday({1373626022, 8072}, NULL) = 0
19259      0.000348 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 121687})
19259      0.129024 gettimeofday({1373626022, 137458}, NULL) = 0
19259      0.000373 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000558 gettimeofday({1373626022, 138381}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000545 gettimeofday({1373626022, 139287}, NULL) = 0
19259      0.000357 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000543 gettimeofday({1373626022, 140187}, NULL) = 0
19259      0.007028 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 176625})
19259      0.074383 gettimeofday({1373626022, 221807}, NULL) = 0
19259      0.000626 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000532 write(4, &quot;n-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00050&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00050_20130712012043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00050_20130712012043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr \246\336\337QS\34\0\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\322\300\1\1\37\300\1\1/\355\177\0P\246\254V\353\321gF\246P\[email protected])\351\344\0\0\0\0\0\0\0\0\246\336\337Q\317\361\1\0!\2\0\0!\2\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\2\23-\[email protected]\0\200\6H\345\300\1\1\37\300\1\1/\355\177\0P\246\254V\353\321gF\246P\[email protected])w\327\0\0POST /ajax/tshark/update.php HTTP/1.1\r\nHost: 192.1.1.47\r\nConnection: keep-alive\r\nContent-Length: 12\r\nOrigin: http://192.1.1.47\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36\r\nContent-type: application/x-www-form-urlenco&quot;..., 4096) = 4096
19259      0.014542 gettimeofday({1373626022, 237342}, NULL) = 0
19259      0.000418 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000589 gettimeofday({1373626022, 238308}, NULL) = 0
19259      0.000359 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000564 gettimeofday({1373626022, 239230}, NULL) = 0
19259      0.000357 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000493 write(4, &quot;ge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00078&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;55.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href\246\336\337Q\213V\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20\233\300\1\1/\300\1\1\37\0P\355\177\321gR\16\246\254X\326P\20\2\177\210\37\0\0=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00078_20130712082043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00078_20130712082043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00077&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http&quot;..., 4096) = 4096
19259      0.007170 gettimeofday({1373626022, 247257}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000587 gettimeofday({1373626022, 248215}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000563 gettimeofday({1373626022, 249138}, NULL) = 0
19259      0.000363 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000491 write(4, &quot;mp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00070&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00070_20130712062043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00070_20130712062043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00069&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;35.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; hr\246\336\337Q$X\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20\230\300\1\1/\300\1\1\37\0P\355\177\321gc*\246\254X\326P\20\2\177\210\37\0\0ef=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00069_20130712&quot;..., 4096) = 4096
19259      0.007559 gettimeofday({1373626022, 257562}, NULL) = 0
19259      0.000380 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000587 gettimeofday({1373626022, 258520}, NULL) = 0
19259      0.000360 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000497 write(4, &quot;onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00063&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00063_20130712043543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00063_20130712043543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00062&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00062_20130712042043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; &quot;..., 4096) = 4096
19259      0.007874 gettimeofday({1373626022, 267255}, NULL) = 0
19259      0.000375 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000576 gettimeofday({1373626022, 268201}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000565 gettimeofday({1373626022, 269172}, NULL) = 0
19259      0.000457 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000577 gettimeofday({1373626022, 270160}, NULL) = 0
19259      0.000358 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.006843 write(4, &quot; maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00056&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00056_20130712025043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFi\246\336\337Q{[\3\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\316\300\1\1\37\300\1\1/\355\177\0P\246\254X\326\321gtFP\[email protected])\272Y\0\0\0\0\0\0\0\0\246\336\337Q\0\\\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20\223\300\1\1/\300\1\1\37\0P\355\177\321g\177\256\246\254X\326P\20\2\177\210\37\0\0le\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00056_20130712025043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00054&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00054_20130712022043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-i&quot;..., 4096) = 4096
19259      0.002318 gettimeofday({1373626022, 279682}, NULL) = 0
19259      0.007233 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000717 gettimeofday({1373626022, 287632}, NULL) = 0
19259      0.000369 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000548 gettimeofday({1373626022, 288547}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 240976})
19259      0.009735 gettimeofday({1373626022, 298653}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246679})
19259      0.003967 write(4, &quot;tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00048&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00048_20130712005043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00048_20130712005043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00047&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00047_20130712003543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\246\336\337Q\35]\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\242;@\[email protected]\6\20\220\300\1\1/\300\1\1\37\0P\355\177\321g\220\312\246\254X\326P\20\2\177\210\37\0\0\&quot; frizb-path=\&quot;/var/www/tmp_file/&quot;..., 4096) = 4096
19259      0.004501 gettimeofday({1373626022, 307496}, NULL) = 0
19259      0.000379 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000593 gettimeofday({1373626022, 308463}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000640 gettimeofday({1373626022, 309472}, NULL) = 0
19259      0.001588 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000538 write(4, &quot;important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\246\336\337Q\37\224\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20\214\300\1\1/\300\1\1\37\0P\355\177\321g\235\233\246\254X\326P\20\2\177\210\37\0\0\&quot;/var/www/tmp_file/2013-07-11/REC_00042_20130711232043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00041&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00041_20130711230543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00041_20130711230543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00040&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://&quot;..., 4096) = 4096
19259      0.005723 gettimeofday({1373626022, 317356}, NULL) = 0
19259      0.000419 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000600 gettimeofday({1373626022, 318333}, NULL) = 0
19259      0.000365 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000563 gettimeofday({1373626022, 319261}, NULL) = 0
19259      0.000363 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000546 gettimeofday({1373626022, 320166}, NULL) = 0
19259      0.004971 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000697 write(4, &quot;file/2013-07-11/REC_00035_20130711213543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00034&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;265.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00034_20130711180054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-pa\246\336\337Q\270\225\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20\211\300\1\1/\300\1\1\37\0P\355\177\321g\256\267\246\254X\326P\20\2\177\210\37\0\0th=\&quot;/var/www/tmp_file/2013-07-11/REC_00034_20130711180054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00033&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;18 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00033_201307111745&quot;..., 4096) = 4096
19259      0.002208 gettimeofday({1373626022, 328049}, NULL) = 0
19259      0.010778 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249965})
19259      0.018113 gettimeofday({1373626022, 362633}, NULL) = 0
19259      0.039997 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259      0.040013 write(4, &quot;izb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00025_20130711154554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00024&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00024_20130711153054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00024_20130711153054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00023&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00023_20130711151554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;&quot;..., 4096) = 4096
19259      0.040009 gettimeofday({1373626022, 486695}, NULL) = 0
19259      0.029979 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259      0.020027 gettimeofday({1373626022, 527039}, NULL) = 0
19259      0.000462 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000606 gettimeofday({1373626022, 528030}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000496 write(4, &quot;remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maCl\246\336\337Q\275\230\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20\204\300\1\1/\300\1\1\37\0P\355\177\321g\313;\246\254X\326P\20\2\177\210\37\0\0ass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00016&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00016_20130711133054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00016_20130711133054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00015&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00015_20130711131554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;del&quot;..., 4096) = 4096
19259      0.003886 gettimeofday({1373626022, 532791}, NULL) = 0
19259      0.000391 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000688 gettimeofday({1373626022, 533855}, NULL) = 0
19259      0.000369 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.002931 gettimeofday({1373626022, 537328}, NULL) = 0
19259      0.000590 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 169693})
19259      0.081030 gettimeofday({1373626022, 618777}, NULL) = 0
19259      0.000370 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 50762})
19259      0.199932 gettimeofday({1373626022, 819065}, NULL) = 0
19259      0.000349 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250869 gettimeofday({1373626023, 70277}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250859 gettimeofday({1373626023, 321489}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250860 gettimeofday({1373626023, 572709}, NULL) = 0
19259      0.000363 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250847 gettimeofday({1373626023, 823909}, NULL) = 0
19259      0.000347 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 41244})
19259      0.242662 gettimeofday({1373626024, 76726}, NULL) = 0
19259      0.033912 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.036814 gettimeofday({1373626024, 147180}, NULL) = 0
19259      0.039321 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259      0.039979 gettimeofday({1373626024, 224289}, NULL) = 0
19259      0.040272 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.020191 gettimeofday({1373626024, 286813}, NULL) = 0
19259      0.036817 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249965})
19259      0.042697 gettimeofday({1373626024, 366745}, NULL) = 0
19259      0.039991 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249965})
19259      0.041525 gettimeofday({1373626024, 447230}, NULL) = 0
19259      0.024186 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259      0.031206 gettimeofday({1373626024, 501437}, NULL) = 0
19259      0.043668 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249966})
19259      0.026451 write(4, &quot;ss maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00009&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;24.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00009_20130711114554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00009_20130711114554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot;\246\336\337Qa\232\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20\201\300\1\1/\300\1\1\37\0P\355\177\321g\334W\246\254X\326P\20\2\177\210\37\0\0 style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00008&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;6.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00008_20130711113054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_0000&quot;..., 4096) = 4096
19259      0.043000 gettimeofday({1373626024, 616847}, NULL) = 0
19259      0.039969 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.036423 gettimeofday({1373626024, 691876}, NULL) = 0
19259      0.043549 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.040002 gettimeofday({1373626024, 776730}, NULL) = 0
19259      0.040022 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249965})
19259      3.210004 gettimeofday({1373626028, 26728}, NULL) = 0
19259      0.044166 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.035909 write(4, &quot; like Gecko) Chrome/27.0.1453.116 Safari/537.36\r\nContent-type: application/x-www-form-urlencoded\r\nAccept: */*\r\nReferer: http://192.1.1.47/sniffer.php\r\nAccept-Encoding: gzip,deflate,sdch\r\nAccept-Language: en-US,en;q=0.8,fr;q=0.6\r\nCookie: PHPSESSID=vg1btqljvlh8rk4q80mk82pe44\r\n\r\nrefresh=2000\250\336\337Q\31\367\1\0006\0\0\0006\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0(\221\[email protected]\[email protected]\6&#39;r\300\1\1/\300\1\1\37\0P\355\210\\D\217+s\235\352AP\20\1\22\202k\0\0\250\336\337Q\24\27\10\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20|\300\1\1/\300\1\1\37\0P\355\177\321g\357G\246\254Z\300P\20\2\224\210\37\0\0HTTP/1.1 200 OK\r\nX-Powered-By: PHP/5.4.4-14\r\nExpires: Thu, 19 Nov 1981 08:52:00 GMT\r\nCache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0\r\nPragma: no-cache\r\nContent-type: text/html\r\nTransfer-Encoding: chunked\r\nDate: Fri, 12 Jul 2013 10:47:04 GMT\r\nServer: lighttpd/1.4.31\r\n\r\n15ce\r\nUp Time : 03:13:44####SEPARATOR####\r\n&lt;div class=\&quot;span4 well\&quot;&gt;\r\n    &lt;h3&gt;&lt;img src=\&quot;./img/info.png\&quot; width=\&quot;32px\&quot;/&gt; Info&lt;/h3&gt;\r\n    Hostname : &lt;strong&gt;raspberrypi\n&lt;/strong&gt;&lt;br /&gt;\nDistribution : &lt;strong&gt;Debian GNU/Linux 7.0 (wheezy)&lt;/strong&gt;&lt;br /&gt;\nKernel Version : &lt;strong&gt;3.6.11+\n&lt;/strong&gt;&lt;br /&gt;&quot;..., 4096) = 4096
19259      0.035930 gettimeofday({1373626028, 136721}, NULL) = 0
19259      0.034062 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000804 gettimeofday({1373626028, 167803}, NULL) = 0
19259      0.000363 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000548 gettimeofday({1373626028, 168713}, NULL) = 0
19259      0.000365 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000543 gettimeofday({1373626028, 169622}, NULL) = 0
19259      0.000357 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000505 write(4, &quot;              Used : &lt;strong&gt;1K-blocksB&lt;/strong&gt;&lt;br /&gt;\r\n                            Free : &lt;strong&gt;Util.B&lt;/strong&gt;&lt;br /&gt;\r\n                            Format : &lt;strong&gt;fich.&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 0%\&quot; title=\&quot;1K-blocks KBytes\&quot;&gt;0%&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-success\&quot; style=\&quot;width: 100%\&quot; title=\&quot;Util. KBytes\&quot;&gt;100%&lt;/div&gt;\r\n\t\t\t&lt;/div&gt;&lt;/div&gt;&lt;div class=\&quot;span3 well\&quot; style=\&quot;background: #FFF\&quot;&gt;\r\n                            &lt;h4&gt;Mounted : &lt;span style=\&quot;color: blue\&quot;&gt;/&lt;/span&gt;&lt;/h4&gt;\r\n                            Total : &lt;strong&gt;3.6 GB&lt;/strong&gt;&lt;br /&gt;\r\n                            Used : &lt;strong&gt;2.8 GB&lt;/strong&gt;&lt;br /&gt;\r\n                            Free : &lt;strong&gt;643.7 MB&lt;/strong&gt;&lt;br /&gt;\r\n                            Format : &lt;strong&gt;ext4&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-\250\336\337Q\223\30\10\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20y\300\1\1/\300\1\1\37\0P\355\177\321h\0c\246\254Z\300P\20\2\224\210\37\0\0striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 77.2%\&quot; title=\&quot;2798700 KBytes\&quot;&gt;77.2%&lt;/div&gt;\r\n\t\t\t&quot;..., 4096) = 4096
19259      0.004404 gettimeofday({1373626028, 174894}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.003785 gettimeofday({1373626028, 179305}, NULL) = 0
19259      0.008168 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.000627 gettimeofday({1373626028, 187850}, NULL) = 0
19259      0.000374 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000504 write(4, &quot;eleteFile\&quot; frizb-\250\336\337Q\235\222\n\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\221\[email protected]\[email protected]\6!\274\300\1\1/\300\1\1\37\0P\355\210\\D\224\337s\235\352AP\20\1\22\210\37\0\0path=\&quot;/var/www/tmp_file/2013-07-12/REC_00081_20130712090543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00080&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;37.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00080_20130712085043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00079&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;50.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_f&quot;..., 4096) = 4096
19259      0.008539 gettimeofday({1373626028, 197268}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000675 gettimeofday({1373626028, 198315}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000558 gettimeofday({1373626028, 199232}, NULL) = 0
19259      0.000360 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000490 write(4, &quot;REC_00073_20130712070543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00072&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;31.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00072_20130712065043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; friz\250\336\337QS\224\n\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\221\[email protected]\[email protected]\6!\271\300\1\1/\300\1\1\37\0P\355\210\\D\245\373s\235\352AP\20\1\22\210\37\0\0b-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00072_20130712065043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00071&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot;&gt;&lt;i cla&quot;..., 4096) = 4096
19259      0.007171 gettimeofday({1373626028, 207259}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000584 gettimeofday({1373626028, 208217}, NULL) = 0
19259      0.000368 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000562 gettimeofday({1373626028, 209144}, NULL) = 0
19259      0.000364 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000487 write(4, &quot;: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00065&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00065_20130712050543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00065_20130712050543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00064&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.1 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; \250\336\337Q~\225\n\0\352\5\0\0\352\5\0\0pT\322&quot;..., 4096) = 4096
19259      0.007240 gettimeofday({1373626028, 217240}, NULL) = 0
19259      0.000375 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000574 gettimeofday({1373626028, 218184}, NULL) = 0
19259      0.000360 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000567 gettimeofday({1373626028, 219111}, NULL) = 0
19259      0.000365 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000559 gettimeofday({1373626028, 220032}, NULL) = 0
19259      0.000358 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.006875 write(4, &quot;\0\0.\221\[email protected]\[email protected]\6&#39;\\\300\1\1/\300\1\1\37\0P\355\210\\D\340fs\235\352AP\30\1\22\202q\0\0001\r\n\n\r\n\254\336\337Q?\370\1\0!\2\0\0!\2\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\2\23-\[email protected]\0\200\6H\274\300\1\1\37\300\1\1/\355\210\0Ps\235\352A\\E7\314P\[email protected])\233\203\0\0POST /ajax/tshark/update.php HTTP/1.1\r\nHost: 192.1.1.47\r\nConnection: keep-alive\r\nContent-Length: 12\r\nOrigin: http://192.1.1.47\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36\r\nContent-type: application/x-www-form-urlencoded\r\nAccept: */*\r\nReferer: http://192.1.1.47/sniffer.php\r\nAccept-Encoding: gzip,deflate,sdch\r\nAccept-Language: en-US,en;q=0.8,fr;q=0.6\r\nCookie: PHPSESSID=vg1btqljvlh8rk4q80mk82pe44\r\n\r\nrefresh=2000\254\336\337Q\256\262\2\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20v\300\1\1/\300\1\1\37\0P\355\177\321h\6M\246\254\\\253P\20\2\224\210\37\0\0HTTP/1.1 200 OK\r\nX-Powered-By: PHP/5.4.4-14\r\nExpires: Thu, 19 Nov 1981 08:52:00 GMT\r\nCache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0\r\nPragma: no-cache\r\nContent-type: text/html\r\nTransfer-Encoding: chunked\r\nDate: Fri, 12 Jul 2013 10:47:08 GMT\r\nServer: lighttpd/1.4.31\r\n\r\n5008\r\n                       Up Time : 03:13:49##&quot;..., 4096) = 4096
19259      0.002291 gettimeofday({1373626028, 229608}, NULL) = 0
19259      0.007365 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000715 gettimeofday({1373626028, 237721}, NULL) = 0
19259      0.000456 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000519 write(4, &quot;s=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00077&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00077_20130712080543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00077_20130712080543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00076&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00076_20130712075043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00076_20130712075043.pcap\&quot; onclick=\&quot;javascript: delete_file($(thi&quot;..., 4096) = 4096
19259      0.008633 gettimeofday({1373626028, 247254}, NULL) = 0
19259      0.000379 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000583 gettimeofday({1373626028, 248210}, NULL) = 0
19259      0.000359 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 243761})
19259      0.006928 gettimeofday({1373626028, 255503}, NULL) = 0
19259      0.000373 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 246304})
19259      0.004667 gettimeofday({1373626028, 260549}, NULL) = 0
19259      0.000382 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000515 write(4, &quot;&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; hr\254\336\337QU\265\2\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20q\300\1\1/\300\1\1\37\0P\355\177\321h\&quot;\321\246\254\\\253P\20\2\224\210\37\0\0ef=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00069_20130712060543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00069_20130712060543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00068&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00068_20130712055043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00068_20130712055043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&quot;..., 4096) = 4096
19259      0.005025 gettimeofday({1373626028, 266466}, NULL) = 0
19259      0.000466 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000615 gettimeofday({1373626028, 267540}, NULL) = 0
19259      0.000360 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000557 gettimeofday({1373626028, 268457}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.008465 write(4, &quot;5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00040_20130711225043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00040_20130711225043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00039&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.1 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;htt\254\336\337Q\265\354\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20d\300\1\1/\300\1\1\37\0P\355\177\321hb\366\246\254\\\253P\20\2\224\210\37\0\0p://192.1.1.47/tmp_file/2013-07-11/REC_00039_20130711223543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00039_20130711223543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-whit&quot;..., 4096) = 4096
19259      0.002264 gettimeofday({1373626028, 279553}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.007430 gettimeofday({1373626028, 287360}, NULL) = 0
19259      0.000376 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.000578 gettimeofday({1373626028, 288307}, NULL) = 0
19259      0.000363 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000503 write(4, &quot;s=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00033_20130711174554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00033_20130711174554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00032&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;17.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00032_20130711173054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00032_20130711173054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_0003&quot;..., 4096) = 4096
19259      0.008109 gettimeofday({1373626028, 297289}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000576 gettimeofday({1373626028, 298236}, NULL) = 0
19259      0.000361 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000554 gettimeofday({1373626028, 299149}, NULL) = 0
19259      0.000357 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000491 write(4, &quot;p_file/2013-07-11/REC_00023_20130711151554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;\254\336\337Q\262\357\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20_\300\1\1/\300\1\1\37\0P\355\177\321h\177z\246\254\\\253P\20\2\224\210\37\0\0/var/www/tmp_file/2013-07-11/REC_00023_20130711151554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00021&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00021_20130711144554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00021_20130711144554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 5&quot;..., 4096) = 4096
19259      0.004022 gettimeofday({1373626028, 304026}, NULL) = 0
19259      0.000377 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.003092 gettimeofday({1373626028, 307497}, NULL) = 0
19259      0.000375 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000565 gettimeofday({1373626028, 308427}, NULL) = 0
19259      0.000360 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000562 gettimeofday({1373626028, 309350}, NULL) = 0
19259      0.000408 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000542 write(4, &quot;=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00015_20130711131554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00014&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00014_20130711130054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/w\254\336\337Q\336\360\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6\20\\\300\1\1/\300\1\1\37\0P\355\177\321h\220\226\246\254\\\253P\20\2\224\210\37\0\0ww/tmp_file/2013-07-11/REC_00014_20130711130054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00013&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;2.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td sty&quot;..., 4096) = 4096
19259      0.006951 gettimeofday({1373626028, 317256}, NULL) = 0
19259      0.000373 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 89371})
19259      0.161404 gettimeofday({1373626028, 479025}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 183140})
19259      0.068431 gettimeofday({1373626028, 547798}, NULL) = 0
19259      0.000530 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000509 write(4, &quot;054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00008_20130711113054.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00007&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00007_20130711111554.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00007_20130711111554.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00006&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;7.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-suc&quot;..., 4096) = 4096
19259      0.008192 gettimeofday({1373626028, 557045}, NULL) = 0
19259      0.000362 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000610 gettimeofday({1373626028, 557999}, NULL) = 0
19259      0.000338 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000512 gettimeofday({1373626028, 558843}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000526 write(4, &quot;a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00079&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;50.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00079_20130712083543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00078&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;55.5 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href\254\336\337QcQ\10\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6!\232\300\1\1/\300\1\1\37\0P\355\210\\EC4s\235\354,P\20\[email protected]\210\37\0\0=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00078_20130712082043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/v&quot;..., 4096) = 4096
19259      0.017224 gettimeofday({1373626028, 582066}, NULL) = 0
19259      0.030083 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.032958 gettimeofday({1373626028, 640585}, NULL) = 0
19259      0.016958 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.019998 write(4, &quot;=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00071&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00071_20130712063543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00070&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.4 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00070_20130712062043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00070_20130712062043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remov&quot;..., 4096) = 4096
19259      0.040027 gettimeofday({1373626028, 726711}, NULL) = 0
19259      0.023253 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000625 gettimeofday({1373626028, 740828}, NULL) = 0
19259      0.000334 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000509 gettimeofday({1373626028, 741748}, NULL) = 0
19259      0.000417 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000457 write(4, &quot;ight;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; \254\336\337Q\272S\10\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6!\225\300\1\1/\300\1\1\37\0P\355\210\\E_\270s\235\354,P\20\[email protected]\210\37\0\0frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00064_20130712045043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00063&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00063_20130712043543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00063_20130712043543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;m&quot;..., 4096) = 4096
19259      0.004688 gettimeofday({1373626028, 747236}, NULL) = 0
19259      0.000340 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000513 gettimeofday({1373626028, 748081}, NULL) = 0
19259      0.000326 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000505 gettimeofday({1373626028, 748911}, NULL) = 0
19259      0.000323 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000548 gettimeofday({1373626028, 749817}, NULL) = 0
19259      0.000363 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.007032 write(4, &quot;/192.1.1.47/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00057_20130712030543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00056&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00056_20130712025043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFi\254\336\337QeV\10\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\237\300\1\1\37\300\1\1/\355\210\0Ps\235\354,\\E_\270P\[email protected])\343\271\0\0\0\0\0\0\0\0\254\336\337Q\337V\10\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6!\222\300\1\1/\300\1\1\37\0P\355\210\\Ep\324s\235\354,P\20\[email protected]\210\37\0\0le\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00056_20130712025043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/&quot;..., 4096) = 4096
19259      0.002033 gettimeofday({1373626028, 759218}, NULL) = 0
19259      0.000338 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000530 gettimeofday({1373626028, 760082}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000489 gettimeofday({1373626028, 760900}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000493 gettimeofday({1373626028, 761722}, NULL) = 0
19259      0.000327 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.004845 write(4, &quot;-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00049_20130712010543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00048&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00048_20130712005043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00048_20130712005043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00047&lt;/td&gt;\r\n\t\t\t\t&lt;t&quot;..., 4096) = 4096
19259      0.001754 gettimeofday({1373626028, 768651}, NULL) = 0
19259      0.000334 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000530 gettimeofday({1373626028, 769511}, NULL) = 0
19259      0.000330 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000508 gettimeofday({1373626028, 770350}, NULL) = 0
19259      0.000328 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000451 write(4, &quot;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00042&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00042_20130711232043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\254\336\337Q\323\311\t\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]@\[email protected]\6!\213\300\1\1/\300\1\1\37\0P\355\210\\E\216\301s\235\354,P\20\[email protected]\210\37\0\0\&quot;/var/www/tmp_file/2013-07-11/REC_00042_20130711232043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00041&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;21.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00041_20130711230543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/&quot;..., 4096) = 4096
19259      0.006067 gettimeofday({1373626028, 777198}, NULL) = 0
19259      0.000339 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 153576})
19259      0.097085 gettimeofday({1373626028, 874625}, NULL) = 0
19259      0.000341 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 90541})
19259      0.183825 gettimeofday({1373626029, 66781}, NULL) = 0
19259      0.035131 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.042664 gettimeofday({1373626029, 146722}, NULL) = 0
19259      0.020250 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.277459 gettimeofday({1373626029, 442866}, NULL) = 0
19259      0.021350 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000625 gettimeofday({1373626029, 456255}, NULL) = 0
19259      0.000314 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000572 write(4, &quot;isplay: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00035&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;18.9 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00035_20130711213543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-11/REC_00035_20130711213543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass1\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130711_00034&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;265.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-11/REC_00034_20130711180054.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-pa\254\336\337Q\222T\r\0&amp;\2\0\0&amp;\2\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\2\30\[email protected]\[email protected]\6%A\300\1\1/\300\1\1\37\0P\355\210\\E\336}s\235\354,P\30\[email protected]\204[\0\0002\r\n&gt;\n\r\n1dd\r\n&lt;/table&gt;####SEPARATOR####\r\n&lt;strong&gt;Current file &quot;..., 4096) = 4096
19259      0.001731 gettimeofday({1373626029, 458872}, NULL) = 0
19259      0.000317 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249975})
19259      0.000893 gettimeofday({1373626029, 460174}, NULL) = 0
19259      0.005193 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000480 write(4, &quot;strong&gt;900MHz&lt;/strong&gt;&lt;br /&gt;\nGovernor : &lt;strong&gt;ondemand&lt;/strong&gt;&lt;br /&gt;\n&lt;/div&gt;\r\n&lt;div class=\&quot;span4 trcc_ramload well\&quot;&gt;\r\n\t&lt;h3&gt;&lt;img src=\&quot;./img/memory.png\&quot; width=\&quot;32px\&quot;/&gt; RAM&lt;/h3&gt;\r\n\t&lt;span class=\&quot;badge badge-success\&quot;&gt;&amp;nbsp;&lt;/span&gt; Free : &lt;strong&gt;15 MB&lt;/strong&gt;&lt;br /&gt;&lt;span class=\&quot;badge badge-info\&quot;&gt;&amp;nbsp;&lt;/span&gt; Used : &lt;strong&gt;470 MB&lt;/strong&gt;&lt;br /&gt;&lt;span class=\&quot;badge badge-warning\&quot;&gt;&amp;nbsp;&lt;/span&gt; Buffer : &lt;strong&gt;24 MB&lt;/strong&gt;&lt;br /&gt;&lt;span class=\&quot;badge badge-important\&quot;&gt;&amp;nbsp;&lt;/span&gt; Cache : &lt;strong&gt;359 MB&lt;/strong&gt;&lt;br /&gt;&lt;span class=\&quot;badge\&quot;&gt;&amp;nbsp;&lt;/span&gt; Total : &lt;strong&gt;485 MB&lt;/strong&gt;&lt;br /&gt;&lt;br /&gt;&lt;div class=\&quot;progress progress-striped\&quot;&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-info\&quot; style=\&quot;width: 17%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-warning\&quot; style=\&quot;width: 4%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-danger\&quot; style=\&quot;width: 74%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t\t&lt;div class=\&quot;bar bar-success\&quot; style=\&quot;width: 5%\&quot;&gt;&lt;/div&gt;\r\n\t\t\t&lt;/div&gt;&lt;/div&gt;\r\n&lt;div class=\&quot;span4 trcc_network well\&quot;&gt;\r\n\t&lt;h3&gt;&lt;img src=\&quot;./img/network.png\&quot; width=\&quot;32px\&quot;/&gt; Network&lt;/h3&gt;\r\n\t&lt;h5&gt;Ethernet&lt;/h5&gt;IP : &lt;strong&gt;192.1.1.&quot;..., 4096) = 4096
19259      0.006539 gettimeofday({1373626029, 472347}, NULL) = 0
19259      0.000392 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249969})
19259      0.000524 gettimeofday({1373626029, 473207}, NULL) = 0
19259      0.000310 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000479 gettimeofday({1373626029, 473993}, NULL) = 0
19259      0.000305 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250797 gettimeofday({1373626029, 725095}, NULL) = 0
19259      0.000313 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.924978 gettimeofday({1373626030, 652666}, NULL) = 0
19259      0.002783 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000530 gettimeofday({1373626030, 653700}, NULL) = 0
19259      0.000384 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000490 gettimeofday({1373626030, 654574}, NULL) = 0
19259      0.000306 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000479 gettimeofday({1373626030, 655361}, NULL) = 0
19259      0.000307 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000487 gettimeofday({1373626030, 656153}, NULL) = 0
19259      0.000305 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.003388 write(4, &quot;2500812 KBytes\&quot;&gt;99\255\336\337Q(\336\6\0l\0\0\0l\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0^\[email protected]\[email protected]\6&amp;\365\300\1\1/\300\1\1\37\0P\355\210\\E\367=s\235\356\26P\30\1m\202\241\0\0.2%&lt;/div&gt;\r\n\t\t\t&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;\t&lt;/div&gt;\r\n&lt;/div&gt;\r\n0\r\n\r\n\255\336\337Q\373\341\6\0&lt;\0\0\0&lt;\0\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\0(-\[email protected]\0\200\6J\224\300\1\1\37\300\1\1/\355\210\0Ps\235\356\26\\E\367sP\[email protected])J\24\0\0\0\0\0\0\0\0\256\336\337Q\210\370\1\0!\2\0\0!\2\0\0\270&#39;\353\317\314ipT\3220\335\203\10\0E\0\2\23-\[email protected]\0\200\6H\247\300\1\1\37\300\1\1/\355\210\0Ps\235\356\26\\E\367sP\[email protected])\330\6\0\0POST /ajax/tshark/update.php HTTP/1.1\r\nHost: 192.1.1.47\r\nConnection: keep-alive\r\nContent-Length: 12\r\nOrigin: http://192.1.1.47\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36\r\nContent-type: application/x-www-form-urlencoded\r\nAccept: */*\r\nReferer: http://192.1.1.47/sniffer.php\r\nAccept-Encoding: gzip,deflate,sdch\r\nAccept-Language: en-US,en;q=0.8,fr;q=0.6\r\nCookie: PHPSESSID=vg1btqljvlh8rk4q80mk82pe44\r\n\r\nrefresh=2000\256\336\337Q&amp;\371\1\0006\0\0\0006\0\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\0(\[email protected]\[email protected]\6&#39;*\300\1\1/\300\1\1\37\0P\355\210\\E\367ss\235\360\1P\20\1\233\202k\0\0\256\336\337Q&gt;\343\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6!u\300\1\1/\300\1\1\37\0P\355\210\\E\367ss\235\360\1P\20\1\233\210\37\0\0HTTP/1.1 200 OK\r\nX-Powered-By: PHP/5.4.4-14\r\nExpires: Thu, 19 Nov 1981 08:52:00 GMT\r\nCache-Control: no-st&quot;..., 4096) = 4096
19259      0.007051 gettimeofday({1373626030, 666972}, NULL) = 0
19259      0.000404 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000528 gettimeofday({1373626030, 667834}, NULL) = 0
19259      0.000313 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000432 write(4, &quot;a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00078_20130712082043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00077&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00077_20130712080543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00077_20130712080543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00076&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_0&quot;..., 4096) = 4096
19259      0.001678 gettimeofday({1373626030, 670257}, NULL) = 0
19259      0.000316 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249976})
19259      0.000491 gettimeofday({1373626030, 671062}, NULL) = 0
19259      0.000315 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000482 gettimeofday({1373626030, 671857}, NULL) = 0
19259      0.000307 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000429 write(4, &quot;2043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00069&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;35.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; hr\256\336\337Q\352\345\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\221[@\[email protected]\6!p\300\1\1/\300\1\1\37\0P\355\210\\F\23\367s\235\360\1P\20\1\233\210\37\0\0ef=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00069_20130712060543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00069_20130712060543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00068&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00068_20130712055043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-al&quot;..., 4096) = 4096
19259      0.006628 gettimeofday({1373626030, 679230}, NULL) = 0
19259      0.000323 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000511 gettimeofday({1373626030, 680055}, NULL) = 0
19259      0.000306 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249980})
19259      0.000487 gettimeofday({1373626030, 680852}, NULL) = 0
19259      0.000316 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.005220 gettimeofday({1373626030, 686440}, NULL) = 0
19259      0.000473 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000478 write(4, &quot;));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00062&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00062_20130712042043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00062_20130712042043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00061&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;30.7 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\256\336\337Qj\347\3\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\221^@\[email protected]\6!m\300\1\1/\300\1\1\37\0P\355\210\\F%\23s\235\360\1P\20\1\233\210\37\0\0\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00061_20130712040543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge ba&quot;..., 4096) = 4096
19259      0.001796 gettimeofday({1373626030, 689134}, NULL) = 0
19259      0.000312 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000493 gettimeofday({1373626030, 689938}, NULL) = 0
19259      0.000313 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 90314})
19259      0.160313 gettimeofday({1373626030, 850568}, NULL) = 0
19259      0.000315 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250790 gettimeofday({1373626031, 101666}, NULL) = 0
19259      0.000382 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250824 gettimeofday({1373626031, 352876}, NULL) = 0
19259      0.000336 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250860 gettimeofday({1373626031, 604076}, NULL) = 0
19259      0.000336 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250852 gettimeofday({1373626031, 855266}, NULL) = 0
19259      0.000341 select(4, [3], NULL, NULL, {0, 250000}) = 0 (Timeout)
19259      0.250876 gettimeofday({1373626032, 106482}, NULL) = 0
19259      0.000469 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 227491})
19259      0.039971 gettimeofday({1373626032, 156741}, NULL) = 0
19259      0.039988 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249963})
19259      0.030038 gettimeofday({1373626032, 223368}, NULL) = 0
19259      0.019996 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 186974})
19259      0.089974 write(4, &quot;script: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00054&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00054_20130712022043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00054_20130712022043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00053&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;27.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00053_20130712020543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/&quot;..., 4096) = 4096
19259      0.029971 gettimeofday({1373626032, 366719}, NULL) = 0
19259      0.037303 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.017490 gettimeofday({1373626032, 411683}, NULL) = 0
19259      0.000323 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249968})
19259      0.001770 write(4, &quot;ass=\&quot;table table-striped table-hover table-condensed\&quot;&gt;&lt;tr&gt;\r\n\t\t&lt;th style=\&quot;width: 50%\&quot;&gt;Record.&lt;/th&gt;\r\n\t\t&lt;th&gt;Size&lt;/th&gt;\r\n\t\t&lt;th&gt;Action&lt;/th&gt;\r\n\t&lt;/tr&gt;&lt;tr&gt;\r\n\t\t\t&lt;td&gt;&lt;a href=\&quot;#\&quot; onclick=\&quot;javacript: $(&#39;.myHidden&#39;).val(&#39;maClass0&#39;);\&quot;&gt;2013-07-12&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;td&gt;1.1 GB&lt;/td&gt;\r\n\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-info\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: compressDownload($(this), &#39;192.1.1.47&#39;);\&quot;&gt;&lt;i class=\&quot;icon-briefcase icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a class=\&quot;badge badge-important\&quot; href=\&quot;#\&quot; id=\&quot;compressDay\&quot; frizb-day=\&quot;2013-07-12\&quot; onclick=\&quot;javascript: deleteWholeDay($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00081&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;22.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00081_20130712090543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;&quot;..., 4096) = 4096
19259      0.001736 gettimeofday({1373626032, 415506}, NULL) = 0
19259      0.000317 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.021074 gettimeofday({1373626032, 443693}, NULL) = 0
19259      0.033417 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249967})
19259      0.017506 gettimeofday({1373626032, 487837}, NULL) = 0
19259      0.000343 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249974})
19259      0.000456 write(4, &quot;ass=\&quot;m\260\336\337Q\2\244\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\[email protected]\[email protected]\6!Q\300\1\1/\300\1\1\37\0P\355\210\\F\2610s\235\361\354P\20\1\311\210\37\0\0aClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00074&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;31 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00074_20130712072043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00073&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;32.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00073_20130712070543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12&quot;..., 4096) = 4096
19259      0.001750 gettimeofday({1373626032, 490379}, NULL) = 0
19259      0.006538 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249973})
19259      0.000645 gettimeofday({1373626032, 497564}, NULL) = 0
19259      0.000334 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249978})
19259      0.000512 gettimeofday({1373626032, 498409}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000453 write(4, &quot;le=\&quot;padding-left: 50px;\&quot;&gt;20130712_00067&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;34.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00067_20130712053543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\260\336\337Q_\245\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\221}@\[email protected]\6!N\300\1\1/\300\1\1\37\0P\355\210\\F\302Ls\235\361\354P\20\1\311\210\37\0\0\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00066&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;33.2 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00066_20130712052043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00066_20130712052043.pcap\&quot; onclick=\&quot;javascrip&quot;..., 4096) = 4096
19259      0.008029 gettimeofday({1373626032, 507228}, NULL) = 0
19259      0.000346 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249971})
19259      0.000534 gettimeofday({1373626032, 508104}, NULL) = 0
19259      0.000335 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000499 gettimeofday({1373626032, 508937}, NULL) = 0
19259      0.000332 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000458 write(4, &quot;&lt;td&gt;29.3 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00060_20130712035043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00060_20130712035043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00059&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;28.8 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00059_20130712033543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00059_20130712033543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr cl\260\336\337Q\351\246\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0&quot;..., 4096) = 4096
19259      0.007465 gettimeofday({1373626032, 517194}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249970})
19259      0.000611 gettimeofday({1373626032, 518153}, NULL) = 0
19259      0.000344 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249977})
19259      0.000513 gettimeofday({1373626032, 519004}, NULL) = 0
19259      0.000334 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249979})
19259      0.000451 write(4, &quot; right;\&quot;&gt;&lt;a class=\&quot;badge badge-suc\260\336\337Q\203\251\4\0\352\5\0\0\352\5\0\0pT\3220\335\203\270&#39;\353\317\314i\10\0E\0\5\334\221\[email protected]\[email protected]\6!I\300\1\1/\300\1\1\37\0P\355\210\\F\336\320s\235\361\354P\20\1\311\210\37\0\0cess\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00052_20130712015043.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00052_20130712015043.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=\&quot;maClass maClass0\&quot; style=\&quot;display: none\&quot;&gt;&lt;td style=\&quot;padding-left: 50px;\&quot;&gt;20130712_00051&lt;/td&gt;\r\n\t\t\t\t&lt;td&gt;25.6 MB&lt;/td&gt;\r\n\t\t\t\t&lt;td style=\&quot;text-align: right;\&quot;&gt;&lt;a class=\&quot;badge badge-success\&quot; href=\&quot;http://192.1.1.47/tmp_file/2013-07-12/REC_00051_20130712013543.pcap\&quot;&gt;&lt;i class=\&quot;icon-download-alt icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt; &lt;a href=\&quot;#\&quot; class=\&quot;badge badge-important\&quot; id=\&quot;deleteFile\&quot; frizb-path=\&quot;/var/www/tmp_file/2013-07-12/REC_00051_20130712013543.pcap\&quot; onclick=\&quot;javascript: delete_file($(this));\&quot;&gt;&lt;i class=\&quot;icon-remove icon-white\&quot;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;\r\n\t\t\t&lt;/tr&gt;\n&lt;tr class=&quot;..., 4096) = 4096
19259      0.007412 gettimeofday({1373626032, 527203}, NULL) = 0
19259      0.000342 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 249972})
19259      0.000518 gettimeofday({1373626032, 528126}, NULL) = 0
19259      0.000408 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 149352})
19259      0.101307 gettimeofday({1373626032, 629779}, NULL) = 0
19259      0.000421 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 51090})
19259      1.356752 gettimeofday({1373626033, 987009}, NULL) = 0
19259      0.000461 select(4, [3], NULL, NULL, {0, 250000}) = 1 (in [3], left {0, 201663})
19259      0.049090 gettimeofday({1373626034, 36520}, NULL) = 0</code></pre></div><div id="comment-22905-info" class="comment-info"><span class="comment-age">(12 Jul '13, 03:50)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22906"></span><div id="comment-22906" class="comment not_top_scorer"><div id="post-22906-score" class="comment-score"></div><div class="comment-text"><p>There is HTML code in the output of strace.</p><p>I don't see how this could be the strace output of the dumpcap process, although the PID (19259) is the same as in the lsof output, which itself looks O.K. !??!</p><p>Could you please post the output of</p><ul><li>ps auxww | grep -i dumpcap</li><li>ps auxww | grep -i tshark</li><li>pstree -p -s 19259</li><li>file /usr/bin/dumpcap</li><li>file /var/www/command/tshark</li></ul><p>So, again: How do you call dumpcap in your application (what is /var/www/command/tshark)? Maybe that's the reason for the problem.</p></div><div id="comment-22906-info" class="comment-info"><span class="comment-age">(12 Jul '13, 03:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22907"></span><div id="comment-22907" class="comment not_top_scorer"><div id="post-22907-score" class="comment-score"></div><div class="comment-text"><p>There is HTML in because I'm listening 80 port (for testing). And what you see is just a dirt Ajax response :)</p><p>In this case, Dumpcap was started by PHP-CGI with shell_exec(sudo nohup dumpcap -P -f [parameters] -i eth0 -w /mnt/hdd/tsar_files_to_proceed/REC.pcap &gt; /dev/null &amp;)</p><p>PHP-CGI, LIHTTPD and DUMPCAP have 3 differents PIDs. So I'm pretty sure 19259 is the good one (corresponding to dumpcap in TOP)</p><p>So, to download a file, I've just put a symbolic link into WWW folder wich one point to the /mnt/hdd/tsar_data/ folder.</p><p>(Sorry for new response, the site consider me like a BOT :o )</p></div><div id="comment-22907-info" class="comment-info"><span class="comment-age">(12 Jul '13, 04:04)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22908"></span><div id="comment-22908" class="comment not_top_scorer"><div id="post-22908-score" class="comment-score"></div><div class="comment-text"><p>auxww command :</p><pre><code>root     16708  0.0  0.1   3556   848 pts/0    S+   13:07   0:00 grep -i dumpcap
root     19253  0.0  0.3   3752  1568 ?        S    juil.11   0:00 sudo nohup dumpcap -P -f (src 192.1.1.47 and port 80) or (dst 192.1.1.31 and port 80) or (src 192.1.1.31 and port 80) or (dst 192.1.1.47 and port 80) or (src 192.1.1.47 and port 22) or (dst 192.1.1.31 and port 22) or (src 192.1.1.31 and port 22) or (dst 192.1.1.47 and port 22) -b duration:900 -i eth0 -w /mnt/hdd/tsar_files_to_proceed/REC.pcap
root     19259  0.4  0.5   5900  2960 ?        R    juil.11   7:32 dumpcap -P -f (src 192.1.1.47 and port 80) or (dst 192.1.1.31 and port 80) or (src 192.1.1.31 and port 80) or (dst 192.1.1.47 and port 80) or (src 192.1.1.47 and port 22) or (dst 192.1.1.31 and port 22) or (src 192.1.1.31 and port 22) or (dst 192.1.1.47 and port 22) -b duration:900 -i eth0 -w /mnt/hdd/tsar_files_to_proceed/REC.pcap</code></pre><p>dumpcap :</p><pre><code>/usr/bin/dumpcap: ELF 32-bit LSB shared object, ARM, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.26, BuildID[sha1]=0x88c054d275bb687e2950b976a7ff2c4a136ec1dc, stripped</code></pre></div><div id="comment-22908-info" class="comment-info"><span class="comment-age">(12 Jul '13, 04:11)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22909"></span><div id="comment-22909" class="comment not_top_scorer"><div id="post-22909-score" class="comment-score"></div><div class="comment-text"><blockquote><p>There is HTML in because I'm listening 80 port (for testing). And what you see is just a dirt Ajax response :)</p></blockquote><p>Ah, of course. That makes sense!</p><blockquote><p>So I'm pretty sure 19259 is the good one (corresponding to dumpcap in TOP)</p></blockquote><p>O.K. I also think it's the correct PID now (see my comment about lsof). Sorry for the confusion!!</p></div><div id="comment-22909-info" class="comment-info"><span class="comment-age">(12 Jul '13, 04:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22910"></span><div id="comment-22910" class="comment not_top_scorer"><div id="post-22910-score" class="comment-score"></div><div class="comment-text"><p>tshark is not used anymore in our app, we use dumpcap.</p><p>pstree :</p><pre><code>init(1)---sudo(19253)---dumpcap(19259)</code></pre><p>So, /var/www/command/tshark is a folder with different files in to configure and launch dumpcap command from the web interface. The one you look for is /var/www/command/tshark/sniff.php</p><pre><code>    $filter_data = array(
        &quot;ip-1&quot; =&gt; array(&quot;src&quot; =&gt; &quot;192.1.1.80:25340&quot;, &quot;dst&quot; =&gt; &quot;192.1.1.20:21286&quot;),
        &quot;ip-2&quot; =&gt; array(&quot;src&quot; =&gt; &quot;192.1.1.84:25596&quot;, &quot;dst&quot; =&gt; &quot;192.1.1.20:21288&quot;),
        &quot;ip1-1&quot; =&gt; array(&quot;src&quot; =&gt; &quot;192.1.1.32:25340&quot;, &quot;dst&quot; =&gt; &quot;192.1.1.20:21282&quot;),
        &quot;ip1-2&quot; =&gt; array(&quot;src&quot; =&gt; &quot;192.1.1.36:25596&quot;, &quot;dst&quot; =&gt; &quot;192.1.1.20:21284&quot;),
        &quot;ip2&quot; =&gt; array(&quot;src&quot; =&gt; &quot;147.196.5.100:7000&quot;, &quot;dst&quot; =&gt; &quot;147.196.5.79:20990&quot;)
        //, &quot;&gt;HTTP&quot; =&gt; array(&quot;src&quot; =&gt; &quot;192.1.1.31:80&quot;, &quot;dst&quot; =&gt; &quot;192.1.1.47:80&quot;)
        //, &quot;HTTP&gt;&quot; =&gt; array(&quot;src&quot; =&gt; &quot;192.1.1.47:80&quot;, &quot;dst&quot; =&gt; &quot;192.1.1.31:80&quot;)
        //, &quot;&gt;SSH&quot; =&gt; array(&quot;src&quot; =&gt; &quot;192.1.1.31:22&quot;, &quot;dst&quot; =&gt; &quot;192.1.1.47:22&quot;)
        //, &quot;SSH&gt;&quot; =&gt; array(&quot;src&quot; =&gt; &quot;192.1.1.47:22&quot;, &quot;dst&quot; =&gt; &quot;192.1.1.31:22&quot;)
    );
    if(isset($_POST[&#39;action&#39;]))
    {
        switch($_POST[&#39;action&#39;])
        {
            case &quot;start&quot;:
                $test = shell_exec(&quot;ps cax | grep dumpcap&quot;);
                if($test == &quot;&quot;)
                {
                    $ntp = shell_exec(&quot;sudo ntpq -p | grep \&quot;*\&quot; | cut -c1&quot;);
                    if(preg_match(&quot;#\*#&quot;, $ntp))
                    {
                        $t_interface = isset($_POST[&#39;interface&#39;]);
                        $t_time = isset($_POST[&#39;time&#39;]);
                        $t_srcIp = isset($_POST[&#39;srcip&#39;]);
                        $t_srcPorts = isset($_POST[&#39;srcports&#39;]);
                        $t_dstIp = isset($_POST[&#39;dstip&#39;]);
                        $t_dstPorts = isset($_POST[&#39;dstports&#39;]);

                        if($t_interface &amp;&amp; $t_time &amp;&amp; $t_srcIp &amp;&amp; $t_srcPorts &amp;&amp; $t_dstIp &amp;&amp; $t_dstPorts)
                        {
                            $finterface = $_POST[&#39;interface&#39;];
                            $ftime = intval($_POST[&#39;time&#39;]) * 60;
                            $srcIp = explode(&#39;,&#39;, $_POST[&#39;srcip&#39;]);
                            $srcPort = explode(&#39;,&#39;, $_POST[&#39;srcports&#39;]);
                            $dstIp = explode(&#39;,&#39;, $_POST[&#39;dstip&#39;]);
                            $dstPort = explode(&#39;,&#39;, $_POST[&#39;dstports&#39;]);
                            $fport = &quot;&quot;;

                            $i = 1;
                            foreach($filter_data as $filter)
                            {
                                if(in_array($i, explode(&#39;,&#39;, $_POST[&#39;ports&#39;])))
                                {
                                    $src_ip = explode(&#39;:&#39;,$filter[&#39;src&#39;])[0];
                                    $src_port = explode(&#39;:&#39;,$filter[&#39;src&#39;])[1];
                                    $dst_ip = explode(&#39;:&#39;,$filter[&#39;dst&#39;])[0];
                                    $dst_port = explode(&#39;:&#39;,$filter[&#39;dst&#39;])[1];
                                    $fport .= &#39;(src &#39;. $src_ip .&#39; and port &#39;. $src_port .&#39;) or (dst &#39;.$dst_ip.&#39; and port &#39;.$dst_port.&#39;) or &#39;;
                                }
                                $i++;
                            }

                            if(!empty($srcIp[0]))
                            {
                                for($i = 0; $i &lt; count($srcIp); $i++)
                                {
                                    $fport .= &#39;(src &#39;. $srcIp[$i] .&#39; and port &#39;. $srcPort[$i] .&#39;) or (dst &#39;.$dstIp[$i].&#39; and port &#39;.$dstPort[$i].&#39;) or &#39;;
                                }
                            }
                            $fport = substr($fport, 0, -4);
                            $finterface = $_POST[&#39;interface&#39;];
                            $ftime = intval($_POST[&#39;time&#39;]) * 60;
                            shell_exec(&#39;sudo echo `date &quot;+%s&quot;` &gt; /var/piStats/current.cap&#39;);
                            passthru(&quot;sudo nohup dumpcap -P -f \&quot;&quot;.$fport.&quot;\&quot; -b duration:&quot;.$ftime.&quot; -i &quot;.$finterface.&quot; -w /mnt/hdd/tsar_files_to_proceed/REC.pcap &gt; /dev/null &amp;&quot;);
                            //echo &quot;sudo nohup dumpcap -P -f \&quot;&quot;.$fport.&quot;\&quot; -b duration:&quot;.$ftime.&quot; -i &quot;.$finterface.&quot; -w /mnt/hdd/tsar_files_to_proceed/REC.pcap &gt; /dev/null &amp;\n&quot;;
                            echo &quot;Starting capture...&quot;;
                        }
                        else
                        {
                            echo &quot;Empty parameter&quot;;
                        }
                    }
                    else
                    {
                        echo &quot;NTP not synchronized...&quot;;
                    }
                }
                else
                {
                    echo &quot;Dumpcap already running...&quot;;
                }
            break;
            case &quot;stop&quot;:
                passthru(&#39;sudo killall dumpcap&#39;);
                //passthru(&#39;sudo killall thaleslibpcapanalyzer&#39;);
            break;
        }
    }
    ?&gt;</code></pre></div><div id="comment-22910-info" class="comment-info"><span class="comment-age">(12 Jul '13, 04:32)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22911"></span><div id="comment-22911" class="comment not_top_scorer"><div id="post-22911-score" class="comment-score"></div><div class="comment-text"><p>O.K. now we have this:</p><ul><li>dumpcap is still running</li><li>the file is still growing</li><li>lsof show the file descriptor of the capture file to be <strong>4</strong>: <code>root 4u REG 8,1 169290163 3145731 /mnt/hdd/tsar_files_to_proceed/REC_00082_20130712092043.pcap</code></li><li>dumpcap is still writing to that file descriptor: <code>19259      0.000451 write(4, " right;\"&gt;&lt;a class=\"badge badge-suc\260</code></li></ul><p>So, now let's go back to the original problem.</p><p>You say:</p><blockquote><p>a whole day without any bug, and the next day, <strong>it stops spliting files</strong> after few hours...</p><p>I notice that too: When dumpcap splits the file after long random period (during the "bug")... The command crash, we can see it running with "top" command but... not working anymore</p></blockquote><p>I would say, the dumpcap command is still doing something, but it (probably) does <strong>not</strong> create new files after 600 seconds, for a yet unknown reason. I don't think it is bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7423">7423</a>, as the proposed code changes have no impact on dumpcap itself (as far as I can see). So, there must be some other reason.</p><p>As the file rotation is based on time, please check if 'something' (like a broken NTP server) changes your system time in an inappropriate way and thus brakes the file rotation.</p><p>You can also use the <strong>option -b filesize:50000 (50 MByte)</strong> instead of <strong>-b duration:600</strong> (just for a test).</p></div><div id="comment-22911-info" class="comment-info"><span class="comment-age">(12 Jul '13, 04:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22912"></span><div id="comment-22912" class="comment not_top_scorer"><div id="post-22912-score" class="comment-score"></div><div class="comment-text"><blockquote><p>sudo killall thaleslibpcapanalyzer</p></blockquote><p>what is sudo <strong>thaleslibpcapanalyzer</strong> (just interested)?</p></div><div id="comment-22912-info" class="comment-info"><span class="comment-age">(12 Jul '13, 05:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22913"></span><div id="comment-22913" class="comment not_top_scorer"><div id="post-22913-score" class="comment-score"></div><div class="comment-text"><p>Yes I can, but, I'll run this test on another raspberry (just in case of we have to make new command on this one already running :) )</p><p>thaleslibpcapanalyzer look every 30 seconds if the dumpcap file was modified in the last minute in order to analyze it and move it in another folder. During the capture, if file is growing up, this jar do nothing.</p><p>We already think about NTP changing system time making dumpcap "bypass" the rotation... But time is just desynchronyzed about few miliseconds.</p></div><div id="comment-22913-info" class="comment-info"><span class="comment-age">(12 Jul '13, 05:23)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22914"></span><div id="comment-22914" class="comment not_top_scorer"><div id="post-22914-score" class="comment-score"></div><div class="comment-text"><blockquote><p><strong>thaleslibpcapanalyzer</strong> look every 30 seconds if the dumpcap file was modified</p></blockquote><p>is that an open source project?</p><blockquote><p>We already think about NTP changing system time making dumpcap "bypass" the rotation... But time is <strong>just desynchronyzed about few miliseconds</strong>.</p></blockquote><p>O.K. that's not enough to cause problems, as dumpcap uses the C library function time() to get the current system time.</p><p>Strange. Please try <strong>-b filesize:50000</strong> and report back if that causes any problems.</p><p>If you are able to build your own version of dumpcap, you could add some statements to the function dumpcap.c:do_file_switch_or_stop() to see if it gets called at all.</p></div><div id="comment-22914-info" class="comment-info"><span class="comment-age">(12 Jul '13, 05:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22915"></span><div id="comment-22915" class="comment not_top_scorer"><div id="post-22915-score" class="comment-score"></div><div class="comment-text"><p>No, it's a software developed by a collegue in my company.</p><p>We're trying -b filesize... Report back if any problem. I tried to build wireshark 1.10... It failed because of some C files... When I see it I just stop trying the build.</p></div><div id="comment-22915-info" class="comment-info"><span class="comment-age">(12 Jul '13, 05:54)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22916"></span><div id="comment-22916" class="comment not_top_scorer"><div id="post-22916-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I tried to build wireshark 1.10... It failed because of some C files.</p></blockquote><p>what about the latest 1.8. release?</p></div><div id="comment-22916-info" class="comment-info"><span class="comment-age">(12 Jul '13, 06:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22917"></span><div id="comment-22917" class="comment not_top_scorer"><div id="post-22917-score" class="comment-score"></div><div class="comment-text"><p>I'll try it next week... I need to "release" this version of our project. I need to stop the current capture too, I launch another dumpcap with my other test platform. It will run for the entier weekend. I come back here on monday with new information... Thanks a lot. I think we progress and hope we can find the source of the problem ! :) Have good weekend !</p></div><div id="comment-22917-info" class="comment-info"><span class="comment-age">(12 Jul '13, 06:34)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22918"></span><div id="comment-22918" class="comment not_top_scorer"><div id="post-22918-score" class="comment-score"></div><div class="comment-text"><p>Dumpcap go on ! It split the file after a long time (434 Mio instead of around 20Mio). It doesn't crash. :)</p></div><div id="comment-22918-info" class="comment-info"><span class="comment-age">(12 Jul '13, 06:36)</span> <span class="comment-user userinfo">FriZBy76</span></div></div><span id="22919"></span><div id="comment-22919" class="comment not_top_scorer"><div id="post-22919-score" class="comment-score"></div><div class="comment-text"><p>O.K., so I guess it's (somehow) related to the system time !?! We will see.... Good luck!</p></div><div id="comment-22919-info" class="comment-info"><span class="comment-age">(12 Jul '13, 07:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22967"></span><div id="comment-22967" class="comment not_top_scorer"><div id="post-22967-score" class="comment-score"></div><div class="comment-text"><p>Hi ! We started 2 captures friday. One "normal" and one with -b filesize: 50000</p><p>The first one crashed. The last file is about 1 day and 15 hours... It makes the Raspberry Pi crashed...</p><p>The second one, had the both conditions time and size. He stop splitting files too... The last file is around 150Mio ... But both dumpcap are stoped because of RPi crashes</p></div><div id="comment-22967-info" class="comment-info"><span class="comment-age">(15 Jul '13, 01:37)</span> <span class="comment-user userinfo">FriZBy76</span></div></div></div><div id="comment-tools-22789" class="comment-tools"><span class="comments-showing"> showing 5 of 23 </span> <a href="#" class="show-all-comments-link">show 18 more comments</a></div><div class="clear"></div><div id="comment-22789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

