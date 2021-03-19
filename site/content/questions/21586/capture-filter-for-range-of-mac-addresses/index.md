+++
type = "question"
title = "Capture Filter for range of MAC addresses"
description = '''I&#x27;m attempting to create a capture filter for a range of MAC addresses. The range of addresses is: 0009fbx6 where x can be any number'''
date = "2013-05-29T19:30:00Z"
lastmod = "2013-05-29T23:59:00Z"
weight = 21586
keywords = [ "mac", "capture-filter" ]
aliases = [ "/questions/21586" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter for range of MAC addresses](/questions/21586/capture-filter-for-range-of-mac-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21586-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm attempting to create a capture filter for a range of MAC addresses.</p><p>The range of addresses is: 0009fbx6 where x can be any number</p></div><div id="question-tags" class="tags-container tags">mac capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '13, 19:30</strong></p><img src="https://secure.gravatar.com/avatar/d87d2173daa97e7292d8c556d8fafb8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mpking&#39;s gravatar image" /><p>Mpking<br />
<span class="score" title="8 reputation points">8</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mpking has no accepted answers">0%</span></p></div></div><div id="comments-container-21586" class="comments-container"></div><div id="comment-tools-21586" class="comment-tools"></div><div class="clear"></div><div id="comment-21586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21590"></span>

<div id="answer-container-21590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21590-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can create a filter that manually looks at the mac address fields in the ethernet header. Here is what the normal "ether host 11:22:33:44:55:66" looks like in BPF code:</p><pre><code>$ tcpdump -d ether host 11:22:33:44:55:66
(000) ld       [8]
(001) jeq      #0x33445566      jt 2    jf 4
(002) ldh      [6]
(003) jeq      #0x1122          jt 8    jf 4
(004) ld       [2]
(005) jeq      #0x33445566      jt 6    jf 9
(006) ldh      [0]
(007) jeq      #0x1122          jt 8    jf 9
(008) ret      #65535
(009) ret      #0
$</code></pre><p>So in your case, you want to look at the ethernet destination address, which starts at offset o in the ethernet header and you will need the first 4 octets. This can be done with <code>ether[0:4]</code>, then you need to mask all the bits in which you are not interested, this can be done with <code>ether[0:4] &amp; 0xffffff0f</code>. Then compare this with your specific address range 0x0009fb06. The same goes for the ethernet source address which can be found at offset 6. This will result in the filter:</p><pre><code> ether[0:4] &amp; 0xffffff0f = 0x0009fb06 or ether[6:4] &amp; 0xffffff0f = 0x0009fb06</code></pre><p>This filter will result in the following BPF code:</p><pre><code>$ tcpdump -d &quot;ether[0:4] &amp; 0xffffff0f = 0x0009fb06 or ether[6:4] &amp; 0xffffff0f = 0x0009fb06&quot;
(000) ld       [0]
(001) and      #0xffffff0f
(002) jeq      #0x9fb06         jt 6    jf 3
(003) ld       [6]
(004) and      #0xffffff0f
(005) jeq      #0x9fb06         jt 6    jf 7
(006) ret      #65535
(007) ret      #0
$</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '13, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21590" class="comments-container"><span id="21599"></span><div id="comment-21599" class="comment"><div id="post-21599-score" class="comment-score"></div><div class="comment-text"><p>Ok. That is very similar with I had come up with, Mine had more brackets.</p><p>I'm also trying to do the inverse. Capture all packets, except for 0009fbx6 where x can be any number.</p><p>I think my brackets have been getting in the way.</p><p>I've tried not (ether[0:4] &amp; 0xffffff0f = 0x0009fb06) or not (ether[6:4] &amp; 0xffffff0f = 0x0009fb06)</p><p>But it doesn't seem to exclude those packets.</p></div><div id="comment-21599-info" class="comment-info"><span class="comment-age">(30 May '13, 07:06)</span> Mpking</div></div><span id="21600"></span><div id="comment-21600" class="comment"><div id="post-21600-score" class="comment-score">1</div><div class="comment-text"><p>It's either:</p><pre><code>not (srcfilter or dstfilter)</code></pre><p>or</p><pre><code>not (srcfilter) and not (dstfilter)</code></pre><p>I usualy take the filter that shows me all the traffic I do not want to see and then put "not (" and ")" around it.</p><p>So in your case:</p><pre><code>not ( ether[0:4] &amp; 0xffffff0f = 0x0009fb06 or ether[6:4] &amp; 0xffffff0f = 0x0009fb06 )</code></pre></div><div id="comment-21600-info" class="comment-info"><span class="comment-age">(30 May '13, 07:10)</span> SYN-bit ♦♦</div></div><span id="21838"></span><div id="comment-21838" class="comment"><div id="post-21838-score" class="comment-score"></div><div class="comment-text"><p>Hmm... That did not appear to work for me. I'm still seeing that traffic.</p></div><div id="comment-21838-info" class="comment-info"><span class="comment-age">(08 Jun '13, 20:47)</span> Mpking</div></div><span id="21841"></span><div id="comment-21841" class="comment"><div id="post-21841-score" class="comment-score"></div><div class="comment-text"><p>Can you share a piece of the full tracefile (without the filter) on www.cloudshark.org?</p><p>If not, can you do the following:</p><ul><li>Create a capture file with 1000 packets (-c 1000) without using a cature filter</li><li>Use tcpdump to extract a file with the filter (<code>tcpdump -r full.pcap -w incl.pcap "ether[0:4] &amp; 0xffffff0f = 0x0009fb06 or ether[6:4] &amp; 0xffffff0f = 0x0009fb06"</code>)</li><li>Use tcpdump to extract a file with the exclude filter (<code>tcpdump -r full.pcap -w excl.pcap "ether[0:4] &amp; 0xffffff0f = 0x0009fb06 or ether[6:4] &amp; 0xffffff0f = 0x0009fb06"</code>)</li><li>Run <code>capinfos -Tc *</code> and show the output here.</li><li>Run <code>tshark -nlr excl.pcap -T fields -e eth.src -e eth.dst -c 5</code> and show the output here.</li></ul></div><div id="comment-21841-info" class="comment-info"><span class="comment-age">(08 Jun '13, 23:39)</span> SYN-bit ♦♦</div></div><span id="21863"></span><div id="comment-21863" class="comment"><div id="post-21863-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, I can't seem to do either. The box I'm performing the capture's on is on an isolated network, and I don't have access to getting files on or off the box. (I'm supposed to, but something is messed up with my VPN, and I can only seem to get RDP access to the box)</p><p>The box is windows, and only has wireshark (WinPCAP / tshark) on the box. I can added tcpdump for the same above reason.</p><p>Is there a way to do this with Just wireshark?<br />
</p><p>I will have a person onsite tomorrow, so there is a possibility that I can get files sneakernet'd off the box tomorrow, but that is iffy, because there supposed to be doing an install of something in a different part of the building.</p></div><div id="comment-21863-info" class="comment-info"><span class="comment-age">(09 Jun '13, 18:49)</span> Mpking</div></div><span id="21870"></span><div id="comment-21870" class="comment not_top_scorer"><div id="post-21870-score" class="comment-score"></div><div class="comment-text"><p>Using Remote Desktop you can "share" a local drive with the remote machine, and then on the remote machine copy files to that "shared" drive. Look under Options | Local Resources | Local devices and resources | More ...</p></div><div id="comment-21870-info" class="comment-info"><span class="comment-age">(10 Jun '13, 03:07)</span> grahamb ♦</div></div></div><div id="comment-tools-21590" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-21590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

