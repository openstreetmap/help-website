+++
type = "question"
title = "tshark - Issues with IP Defragmentation - SIP"
description = '''I have a problem reading pcap files that have fragmented packets with tshark. My expectaion is tshark will re-assemble the fragmented IP packets before it passes them to the higher layer dissectors. But this doesnt appear to happen. If I open the same file with the Wireshark GUI application it does ...'''
date = "2013-02-08T02:12:00Z"
lastmod = "2013-02-08T13:08:00Z"
weight = 18443
keywords = [ "reassembly", "fragmentation", "sip", "tshark", "reassemble" ]
aliases = [ "/questions/18443" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [tshark - Issues with IP Defragmentation - SIP](/questions/18443/tshark-issues-with-ip-defragmentation-sip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18443-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a problem reading pcap files that have fragmented packets with tshark. My expectaion is tshark will re-assemble the fragmented IP packets before it passes them to the higher layer dissectors. But this doesnt appear to happen. If I open the same file with the Wireshark GUI application it does this fine.</p><p>Should I be able to do this with tshark on the command line? I have tried various tshark versions and get the same result. 1.4x, 1.6.7 and 1.8.2. I have also tried overriding the default sip.defragment option.</p><p>As an example I am searching pcap files (dumped with tcpump) for SIP calls. But the SIP dissector doesnt recognise the packets because they are still fragmented. So if I look at the first 10 packets in the file is see:</p><p><code> $ tshark -r 218423_1.cap00 -c 10   1   0.000000 10.0.226.129 -&gt; 10.0.226.133 SIP 1251 Request: OPTIONS sip:10.0.226.133;transport=tcp   2   0.000835 10.0.226.133 -&gt; 10.0.226.129 SIP 1337 Status: 200 OK   3   5.091195 10.0.226.133 -&gt; 10.0.226.129 SIP/SDP 1025 Request: INVITE sip:[email protected];user=phone, with session description   4   5.094097 10.0.226.129 -&gt; 10.0.226.133 SIP 359 Status: 100 Trying   5   5.122237 10.0.226.129 -&gt; 10.0.226.133 IPv4 132 Fragmented IP protocol (proto=UDP 17, off=1480, ID=d618)   6   5.169126 10.0.226.129 -&gt; 10.0.226.133 IPv4 825 Fragmented IP protocol (proto=UDP 17, off=1480, ID=d619)   7   5.171658 10.0.226.133 -&gt; 10.0.226.129 SIP 840 Status: 100 Trying   8   5.176699 10.0.226.129 -&gt; 10.0.226.134 RTP 218 PT=ITU-T G.711 PCMA, SSRC=0x33B61227, Seq=1, Time=0    9   5.177610 10.0.226.129 -&gt; 10.0.226.134 RTCP 134 Receiver Report   Source description   10   5.196590 10.0.226.129 -&gt; 10.0.226.134 RTP 218 PT=ITU-T G.711 PCMA, SSRC=0x33B61227, Seq=2, Time=160 </code></p><p>As you can see #5 and 6 show as fragmented. If I try to pass this through a sip filter it wont find those packets so it doesnt appear to be re-assembling them in the same way wireshark application does.</p><p><code> $ tshark -r 218423_1.cap00 sip -c 10   1   0.000000 10.0.226.129 -&gt; 10.0.226.133 SIP 1251 Request: OPTIONS sip:10.0.226.133;transport=tcp   2   0.000835 10.0.226.133 -&gt; 10.0.226.129 SIP 1337 Status: 200 OK   3   5.091195 10.0.226.133 -&gt; 10.0.226.129 SIP/SDP 1025 Request: INVITE sip:[email protected];user=phone, with session description   4   5.094097 10.0.226.129 -&gt; 10.0.226.133 SIP 359 Status: 100 Trying   7   5.171658 10.0.226.133 -&gt; 10.0.226.129 SIP 840 Status: 100 Trying  12   5.216181 10.0.226.129 -&gt; 10.0.226.133 SIP 1026 Request: PRACK sip:[email protected]:5060  14   5.219458 10.0.226.133 -&gt; 10.0.226.129 SIP 1385 Status: 200 OK 483   8.250769 10.0.226.133 -&gt; 10.0.226.129 SIP 1498 Status: 180 Ringing 487   8.267270 10.0.226.129 -&gt; 10.0.226.133 SIP 1028 Request: PRACK sip:[email protected]:5060 488   8.270899 10.0.226.133 -&gt; 10.0.226.129 SIP 1387 Status: 200 OK</code></p><p>As can be seen packets 5 and 6 (which in this I know form an INVITE) dont get shown. I have also tried the <code>-o ip.defragment:TRUE</code> and also writing the output to file but it still doesnt change anything.</p><p>For reference I am capturing them with tcpdump using the following BPF: <code>( vlan and (port 5060 or ip[6:2] &amp; 0x1fff != 0 ))</code></p><p>Any Advice would be much appreciated</p></div><div id="question-tags" class="tags-container tags">reassembly fragmentation sip tshark reassemble</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '13, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/04f2459d8c2e3e8f9f9afc61a05fc8d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marv&#39;s gravatar image" /><p>Marv<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marv has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-18443" class="comments-container"><span id="18530"></span><div id="comment-18530" class="comment"><div id="post-18530-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guys,</p><p>I have narrowed down the issue and it appears I have made a mistake in the way the files have been captured. On closer inspection Tshark is working fine but something is causing packets with the fragmented flag set to be dropped. This may be an aggregation switch before the capture box or the box itself so will need further investigation. When supplied with a valid file tshark will re-assemble them as expected. I do still have issues with extracting SIP when fragmented packets are present but I will get the capture issues sorted first.</p><p>Thanks all for you help an comments. They have helped a great deal in improving the BPF and tracking down the issue.</p><p>Cheers Marv</p></div><div id="comment-18530-info" class="comment-info"><span class="comment-age">(12 Feb '13, 01:10)</span> Marv</div></div><span id="18531"></span><div id="comment-18531" class="comment"><div id="post-18531-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-18531-info" class="comment-info"><span class="comment-age">(12 Feb '13, 01:59)</span> grahamb ♦</div></div></div><div id="comment-tools-18443" class="comment-tools"></div><div class="clear"></div><div id="comment-18443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="18444"></span>

<div id="answer-container-18444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18444-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're missing the first part of your IP fragmented packets. That's because you drop them with your capture filter.</p><p>That filter says:</p><p><code>vlan</code></p><p>oke, your on a vlan, make sure there's a tag and compensate for it,</p><p><code>and (port 5060</code></p><p>oke, you want UDP (and TCP) port 5060, the SIP signaling port,</p><p><code>or ip[6:2] &amp; 0x1fff != 0 )</code></p><p>not oke, you don't want to have IP fragments with offsets multiple of 8.191. This includes offset 0, the start of the fragmented packets you are missing. Mind you, without reassembled IP packets, there is no UDP datagram that can be dissected to match the <code>port 5060</code> filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '13, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18444" class="comments-container"></div><div id="comment-tools-18444" class="comment-tools"></div><div class="clear"></div><div id="comment-18444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18450"></span>

<div id="answer-container-18450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18450-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like your filter is OK, it captures all frames with TCP and UDP port 5060 and all frames that have an IP fragment offset of non-zero. But this means your filter will also catch IP fragments that were not for port 5060. So the fragments that you are referring too might not be SIP at all.</p><p>Then again, you say wireshark shows the packets fine. From the output of the packet it looks like</p><ol><li><p><strong>either the first fragments of packets 5 and 6 are not in the capture file.</strong> What is the output of <code>tshark -r 218423_1.cap00 -R "ip.id==0xd618 or ip.id==0xd619"</code>? Do you see only the two fragments or also the first parts of these IP packets? I expect to see only two fragments, as there were no frames with len=1500 (20 bytes IP header and 1480 bytes IP payload) before packet 5.)</p></li><li><p><strong>or IP reassembly is not enabled in the profile that tshark uses</strong> in which case you might want to try <code>tshark -o ip.defragment:TRUE -nlr 218423_1.cap00 -R sip</code></p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '13, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18450" class="comments-container"></div><div id="comment-tools-18450" class="comment-tools"></div><div class="clear"></div><div id="comment-18450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18449"></span>

<div id="answer-container-18449" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18449-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My expectaion is tshark will re-assemble the fragmented IP packets before it passes them to the higher layer dissectors.</p></blockquote><p>Yes, it should/will do that.</p><blockquote><p>But this doesnt appear to happen. <strong>If I open the same file</strong> with the <strong>Wireshark GUI</strong> application <strong>it does this fine</strong>.</p></blockquote><p>O.K. you are saying, that for the <strong>identical</strong> file (captured with the BPF you mentioned) de-fragmentation works in Wireshark and it does not work in tshark?</p><p>If so, can you please upload the file somewhere (google docs, cloudshark.org, one-click file hoster. BEWARE the privacy issues in doing so!), so we can check ourselves?</p><p>BTW: Did you capture the whole frame (option -s0)? If you did not, you will get problems during de-fragmentation.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '13, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '13, 12:29</p></div></div><div id="comments-container-18449" class="comments-container"></div><div id="comment-tools-18449" class="comment-tools"></div><div class="clear"></div><div id="comment-18449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

