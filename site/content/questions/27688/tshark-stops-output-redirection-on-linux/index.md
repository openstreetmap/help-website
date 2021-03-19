+++
type = "question"
title = "Tshark stops output redirection on Linux"
description = '''Hello! I&#x27;m trying to capture traffic with applying tshark filters in realtime. #Capturing command is the following: tshark -i eth6 -i eth7 -R &#x27;(tcp.analysis.retransmission or tcp.analysis.fast_retransmission or tcp.analysis.duplicate_ack_frame)&#x27; -Tfields -Eseparator=&quot;|&quot; -Eoccurrence=l -e frame.time ...'''
date = "2013-12-02T23:03:00Z"
lastmod = "2013-12-03T11:08:00Z"
weight = 27688
keywords = [ "redirection", "tshark", "filters", "linux" ]
aliases = [ "/questions/27688" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark stops output redirection on Linux](/questions/27688/tshark-stops-output-redirection-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27688-score" class="post-score" title="current number of votes">0</div><span id="post-27688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I'm trying to capture traffic with applying tshark filters in realtime.</p><pre><code>#Capturing command is the following:
tshark -i eth6 -i eth7 -R &#39;(tcp.analysis.retransmission or tcp.analysis.fast_retransmission or tcp.analysis.duplicate_ack_frame)&#39; -Tfields -Eseparator=&quot;|&quot; -Eoccurrence=l -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e expert | sed &quot;...&quot; &gt; /tmp/retransmissions.txt</code></pre><p>After the some time odd situation occurs: file /tmp/retransmissions.txt stop grows, but wireshark temporary file still grows (looks like everything is fine and that traffic still captures). If I will start additional tshark process with the same filters (without redirection to file), I will see that retransmissions are present, but 1st process of the tshark will not redirect to output these packets.</p><p>So the situation looks like redirection unexpectedly stops its work. Every necessary process runs in this time:</p><pre><code># ps aux |grep tshark
root     21992  4.2  1.0 493688 304092 pts/1   S    09:56   1:39 /usr/bin/tshark -i eth6 -i eth7 -R (tcp.analysis.retransmission or tcp.analysis.duplicate_ack_frame) -Tfields -Eseparator | -Eoccurrence l -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e expert

# ps aux |grep dumpcap
root     22008  3.0  0.0 202288 26428 pts/1    Sl   09:56   1:48 /usr/bin/dumpcap -t -n -i eth6 -i eth7 -Z none

# free
             total       used       free     shared    buffers     cached
Mem:      28729376    3672100   25057276          0     192384    1397272
-/+ buffers/cache:    2082444   26646932
Swap:      6143992          0    6143992

# tshark -v
TShark 1.10.3 (SVN Rev Unknown from unknown)

# cat /etc/redhat-release
CentOS release 6.5 (Final)</code></pre><p>Do you have any ideas why this situation may occurs and how to resolve it?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-redirection" rel="tag" title="see questions tagged &#39;redirection&#39;">redirection</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '13, 23:03</strong></p><img src="https://secure.gravatar.com/avatar/00fc9b7ddbee4ec657351cff07ace3ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrav&#39;s gravatar image" /><p><span>mrav</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrav has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Dec '13, 05:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-27688" class="comments-container"></div><div id="comment-tools-27688" class="comment-tools"></div><div class="clear"></div><div id="comment-27688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27691"></span>

<div id="answer-container-27691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27691-score" class="post-score" title="current number of votes">2</div><span id="post-27691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tshark output is buffered. Please try tshark option -l and check if that helps. Same for sed, option -u.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Dec '13, 01:49</strong> </span></p></div></div><div id="comments-container-27691" class="comments-container"><span id="27693"></span><div id="comment-27693" class="comment"><div id="post-27693-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>I have tried this solution, unfortunately problem has occurred again.</p></div><div id="comment-27693-info" class="comment-info"><span class="comment-age">(03 Dec '13, 02:59)</span> <span class="comment-user userinfo">mrav</span></div></div><span id="27695"></span><div id="comment-27695" class="comment"><div id="post-27695-score" class="comment-score"></div><div class="comment-text"><p>O.K. then please do the following:</p><p>As soon as the output stalls, run the following commands</p><pre><code>strace -r -tt -T -s 1024 -p &lt;pid of tshark&gt; -f -o /tmp/tshark.strace    
strace -r -tt -T -s 1024 -p  &lt;pid of sed&gt; -f -o /tmp/sed.strace</code></pre><p>Then post the output files</p></div><div id="comment-27695-info" class="comment-info"><span class="comment-age">(03 Dec '13, 03:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27701"></span><div id="comment-27701" class="comment"><div id="post-27701-score" class="comment-score"></div><div class="comment-text"><h1 id="cat-tshark.strace">cat tshark.strace</h1><pre><code>27203      0.000000 write(2, &quot;\r128413 &quot;, 8 &lt;unfinished ...&gt;
27203    835.667210 +++ killed by SIGKILL +++</code></pre><h1 id="cat-sed.starce">cat sed.starce</h1><pre><code>27204      0.000000 read(0, &quot;&quot;, 4096)   = 0 &lt;799.749215&gt;
27204    799.749351 close(0)            = 0 &lt;0.000040&gt;
27204      0.000118 munmap(0x7f4405f52000, 4096) = 0 &lt;0.000024&gt;
27204      0.000081 close(1)            = 0 &lt;0.000048&gt;
27204      0.000113 munmap(0x7f4405f4e000, 4096) = 0 &lt;0.000065&gt;
27204      0.000122 close(2)            = 0 &lt;0.000013&gt;
27204      0.000087 exit_group(0)       = ?</code></pre><p>SIGKILL and close (0) has appeared in strace files after I have stopped the capturing script.</p></div><div id="comment-27701-info" class="comment-info"><span class="comment-age">(03 Dec '13, 05:11)</span> <span class="comment-user userinfo">mrav</span></div></div><span id="27706"></span><div id="comment-27706" class="comment"><div id="post-27706-score" class="comment-score"></div><div class="comment-text"><blockquote><p>27203 0.000000 write(2, "\r128413 ", 8 &lt;unfinished ...=""&gt; 27203 835.667210 +++ killed by SIGKILL +++</p></blockquote><p>is that the only line in tshark.trace?</p><p>BTW: What is the output of the following commands, while the output stalls</p><blockquote><p>df -h<br />
lsof -n | egrep '(tshark|dumpcap)'</p></blockquote></div><div id="comment-27706-info" class="comment-info"><span class="comment-age">(03 Dec '13, 05:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27708"></span><div id="comment-27708" class="comment"><div id="post-27708-score" class="comment-score"></div><div class="comment-text"><p>Correct, only this line, which is not gave us any useful information..unfortunately.</p><p>Will try additionally to run strace from the beginning, when tshark works correctly .Maybe this will give additional information.</p><p>Disk space is present, while the output stalls. Anyway will try again to reproduce an issue and check the command output.</p><p>Many thanks for your help!</p></div><div id="comment-27708-info" class="comment-info"><span class="comment-age">(03 Dec '13, 05:57)</span> <span class="comment-user userinfo">mrav</span></div></div><span id="27713"></span><div id="comment-27713" class="comment not_top_scorer"><div id="post-27713-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Will try additionally to run strace from the beginning, when tshark works correctly .Maybe this will give additional information.</p></blockquote><p>that will generate way too much data....</p><p>Please run strace on dumpcap while the output stalls.</p></div><div id="comment-27713-info" class="comment-info"><span class="comment-age">(03 Dec '13, 06:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27728"></span><div id="comment-27728" class="comment not_top_scorer"><div id="post-27728-score" class="comment-score"></div><div class="comment-text"><p>Output of commands is the following:</p><h1 id="lsof--n-egrep-tsharkdumpcap">lsof -n |egrep '(tshark|dumpcap)'</h1><pre><code>tail       2984      root    3r      REG                8,5 1061880053         18 /tmp/tshark.strace
tshark    28443      root  cwd       DIR                8,2       4096     524289 /root
tshark    28443      root  rtd       DIR                8,2       4096          2 /
tshark    28443      root  txt       REG                8,2    1227674    1709133 /usr/bin/tshark
tshark    28443      root  mem       REG                8,2      12504    1704720     /usr/lib64/gconv/IBM437.so
tshark    28443      root  mem       REG                8,2      26060    1704864 /usr/lib64/gconv/gconv-modules.cache
tshark    28443      root  mem       REG                8,2   99158576    1716876 /usr/lib/locale/locale-archive
tshark    28443      root  mem       REG                8,2      65928     655653 /lib64/libnss_files-2.12.so
tshark    28443      root  mem       REG                8,2     178014    1709122 /usr/lib/wireshark/plugins/1.10.3/gryphon.so
tshark    28443      root  mem       REG                8,2    1035851    1709127 /usr/lib/wireshark/plugins/1.10.3/profinet.so
tshark    28443      root  mem       REG                8,2     186948    1709119 /usr/lib/wireshark/plugins/1.10.3/asn1.so
tshark    28443      root  mem       REG                8,2     260738    1709125 /usr/lib/wireshark/plugins/1.10.3/mate.so
tshark    28443      root  mem       REG                8,2      34247    1709128 /usr/lib/wireshark/plugins/1.10.3/stats_tree.so
tshark    28443      root  mem       REG                8,2     167035    1709131 /usr/lib/wireshark/plugins/1.10.3/wimaxasncp.so
tshark    28443      root  mem       REG                8,2      57183    1709124 /usr/lib/wireshark/plugins/1.10.3/m2m.so
tshark    28443      root  mem       REG                8,2     141459    1709123 /usr/lib/wireshark/plugins/1.10.3/irda.so
tshark    28443      root  mem       REG                8,2    1001620    1709120 /usr/lib/wireshark/plugins/1.10.3/docsis.so
tshark    28443      root  mem       REG                8,2     178299    1709132 /usr/lib/wireshark/plugins/1.10.3/wimaxmacphy.so
tshark    28443      root  mem       REG                8,2    1709096    1709130 /usr/lib/wireshark/plugins/1.10.3/wimax.so
tshark    28443      root  mem       REG                8,2     635758    1709126 /usr/lib/wireshark/plugins/1.10.3/opcua.so
tshark    28443      root  mem       REG                8,2     252218    1709129 /usr/lib/wireshark/plugins/1.10.3/unistim.so
tshark    28443      root  mem       REG                8,2     335925    1709121 /usr/lib/wireshark/plugins/1.10.3/ethercat.so
tshark    28443      root  mem       REG                8,2      19536     655643 /lib64/libdl-2.12.so
tshark    28443      root  mem       REG                8,2      11816     655711 /lib64/libgmodule-2.0.so.0.2600.1
tshark    28443      root  mem       REG                8,2      43832     655665 /lib64/librt-2.12.so
tshark    28443      root  mem       REG                8,2      17536     655715 /lib64/libgthread-2.0.so.0.2600.1
tshark    28443      root  mem       REG                8,2    1921216     655637 /lib64/libc-2.12.so
tshark    28443      root  mem       REG                8,2     142640     655661 /lib64/libpthread-2.12.so
tshark    28443      root  mem       REG                8,2      88600     655688 /lib64/libz.so.1.2.3
tshark    28443      root  mem       REG                8,2     655691    1716807 /usr/lib/libpcap.so.1.4.0
tshark    28443      root  mem       REG                8,2     596264     655645 /lib64/libm-2.12.so
tshark    28443      root  mem       REG                8,2    1066448     655709 /lib64/libglib-2.0.so.0.2600.1
tshark    28443      root  mem       REG                8,2      58574    1708933 /usr/lib/libwsutil.so.3.0.0
tshark    28443      root  mem       REG                8,2  133618918    1709118 /usr/lib/libwireshark.so.3.1.3
tshark    28443      root  mem       REG                8,2    1291175    1708940 /usr/lib/libwiretap.so.3.0.3
tshark    28443      root  mem       REG                8,2     154520     655363 /lib64/ld-2.12.so
tshark    28443      root    0u      CHR             136,11        0t0         14 /dev/pts/11
tshark    28443      root    1w     FIFO                0,8        0t0    1727249 pipe
tshark    28443      root    2u      CHR             136,11        0t0         14 /dev/pts/11
tshark    28443      root    3r     FIFO                0,8        0t0    1727311 pipe
tshark    28443      root    4r      REG                8,5 1288595548         12 /tmp/wireshark_2_interfaces_20131203175838_Fs5DKR
dumpcap   28451      root  cwd       DIR                8,2       4096     524289 /root
dumpcap   28451      root  rtd       DIR                8,2       4096          2 /
dumpcap   28451      root  txt       REG                8,2     233105    1709134 /usr/bin/dumpcap
dumpcap   28451      root  mem       REG                8,2      65928     655653 /lib64/libnss_files-2.12.so
dumpcap   28451      root  mem       REG                0,6               1727315 socket:[1727315] (stat: No such file or directory)
dumpcap   28451      root  mem       REG                0,6               1727314 socket:[1727314] (stat: No such file or directory)
dumpcap   28451      root  mem       REG                8,2      19536     655643 /lib64/libdl-2.12.so
dumpcap   28451      root  mem       REG                8,2      11816     655711 /lib64/libgmodule-2.0.so.0.2600.1
dumpcap   28451      root  mem       REG                8,2      43832     655665 /lib64/librt-2.12.so
dumpcap   28451      root  mem       REG                8,2    1921216     655637 /lib64/libc-2.12.so
dumpcap   28451      root  mem       REG                8,2     142640     655661 /lib64/libpthread-2.12.so
dumpcap   28451      root  mem       REG                8,2      88600     655688 /lib64/libz.so.1.2.3
dumpcap   28451      root  mem       REG                8,2     655691    1716807 /usr/lib/libpcap.so.1.4.0
dumpcap   28451      root  mem       REG                8,2    1066448     655709 /lib64/libglib-2.0.so.0.2600.1
dumpcap   28451      root  mem       REG                8,2      17536     655715 /lib64/libgthread-2.0.so.0.2600.1
dumpcap   28451      root  mem       REG                8,2      58574    1708933 /usr/lib/libwsutil.so.3.0.0
dumpcap   28451      root  mem       REG                8,2     154520     655363 /lib64/ld-2.12.so
dumpcap   28451      root    0u      CHR             136,11        0t0         14 /dev/pts/11
dumpcap   28451      root    1w     FIFO                0,8        0t0    1727249 pipe
dumpcap   28451      root    2w     FIFO                0,8        0t0    1727311 pipe
dumpcap   28451      root    3u     pack            1727314        0t0        ALL type=SOCK_RAW
dumpcap   28451      root    4w     FIFO                0,8        0t0    1727311 pipe
dumpcap   28451      root    5u     pack            1727315        0t0        ALL type=SOCK_RAW
dumpcap   28451      root    6u      REG                8,5 1288595548         12 /tmp/wireshark_2_interfaces_20131203175838_Fs5DKR
strace    28847      root    3w      REG                8,5 1061880053         18 /tmp/tshark.strace</code></pre><h1 id="df--h">df -h</h1><pre><code>Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2        32G   21G  9.8G  68% /
tmpfs            14G     0   14G   0% /dev/shm
/dev/sda1       194M   76M  108M  42% /boot
/dev/sda5        97G  2.5G   90G   3% /tmp</code></pre><h1 id="strace">strace</h1><pre><code>28443      0.004057 read(4, &quot;D\36\241ZA4\0\17S\fI|\10\0E\0\0t\372\[email protected]\[email protected]\6N\226\n\1n\204\n\1n\202N  \[email protected]\237,\304\241\5\366\256m\200\30\0\201\304q\0\0\1\1\10\n\240\265ax9\231l[\0\30\34L\0\0\0f\0\0\0,\0\0\0,\0\0\0\0LISTENER[2]APP[10100]#[email protected]\0\0\0\244\0\0\0\6\0\0\0d\0\0\0\0\0\0\0\242\354\4\0\7\211\311aB\0\0\0B\0\0\0\0\17S\fI|D\36\241ZA4\10\0E\0\[email protected]\[email protected]\6%Q\n\1n\202\n\1n\204\[email protected] \5\366\256m\237,\304\341\200\20\1&gt;\247~\0\0\1\1\10\n9\231l^\240\265ax\0\0d\0\0\0\6\0\0\0d\0\0\0\1\0\0\0\242\354\4\0\355\225\311aB\0\0\0B\0\0\0D\36\241ZA4\0\17S\fI|\10\0E\0\0004\233\[email protected]\[email protected]\6\256\20\n\1n\204\n\1n\202N\&quot;\271+u\223\347\365\333E\330\2\200\20\1d\304\4\0\0\1\1\10\n\240\265a|9\231la\0\0d\0\0\0\6\0\0\0x\0\0\0\0\0\0\0\242\354\4\0\365\225\311aV\0\0\0V\0\0\0\0\17S\fI|D\36\241ZA4\10\0E\0\0H\[email protected]\[email protected]\6\265\203\n\1n\202\n\1n\204\271+N\&quot;\333E\327\356u\223\347\365\200\30\1\365Q,\0\0\1\1\10\n9\231la\240\265a\v\0\0\0\0\0\0\0e\0\0\0\0\0\0\0\0\0Ir\2\0\0x\0\0\0\6\0\0\0\244\0\0\0\1\0\0\0\242\354\4\0\322\325\311a\202\0\0\0\202\0\0\0D\36\241Z1\350\0\17S\fI|\10\0E\0\0t\33\[email protected]\[email protected]\6-\260\n\1n\204\n\1n\203N \262\232\237}\352:T\36\370x\200\30\0.\314\231\0\0\1\1\10\n\240\265a\214\32\366\340\234\0\30\34L\0\0\0f\0\0\0,\0\0\0,\0\0\0\0LISTENER[2]APP[10100]#[email protected]\0\0\0\244\0\0\0\6\0\0\0d\0\0\0\0\0\0\0\242\354\4\0\27\326\311aB\0\0\0B\0\0\0\0\17S\fI|D\36\241Z1\350\10\0E\0\[email protected]\[email protected]\6\364\212\n\1n\203\n\1n\204\262\232N T\36\370x\237}\352z\200\20\0.\257\365\0\0\1\1\10\n\32\366\341\r\240\265a\214\0\0d\0\0\0\6\0\0\0\244\0\0\0\1\0\0\0\242\354\4\0\304\335\311a\202\0\0\0\202\0\0\0D\36\241Z1\350\0\17S\fI|\10\0E\0\0t\210\[email protected]\[email protected]\6\300\322\n\1n\204\n\1n\203N\&quot;\332\212u\213\271D*\r\245\371\200\30\1t\277\2\0\0\1\1\10\n\240\265a\216\32\366\340V\0\n\326t\0\0\0f\0\0\0,\0\0\0,\0\0\0\0LISTENER[1]APP[10102]#[email protected]\0\0\0\244\0\0\0\6\0\0\0|\0\0\0\0\0\0\0\242\354\4\0\366\335\311a\\\0\0\0\\\0\0\0\377\377\377\377\377\377\234\216\231\36\371|\10\0E\0\0N\21\355\0\0\200\02178\n\1ny\n\1n\377\0\211\0\211\0:\320\262\236\276\1\20\0\1\0\0\0\0\0\0 FHEJEOCNEIDCDBEMEMDIEDDDDFEFECAA\0\0 \0\1|\0\0\0\6\0\0\0d\0\0\0\0\0\0\0\242\354\4\0&quot;..., 4096) = 3808 &lt;0.000121&gt;
28443      0.000568 read(4, &quot;&quot;, 288)    = 0 &lt;0.000111&gt;
28443      0.003445 write(2, &quot;\r257636 &quot;, 8 &lt;unfinished ...&gt;</code></pre></div><div id="comment-27728-info" class="comment-info"><span class="comment-age">(03 Dec '13, 11:08)</span> <span class="comment-user userinfo">mrav</span></div></div></div><div id="comment-tools-27691" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-27691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

