+++
type = "question"
title = "Query : How to decode MTP3 Message Over TCP using TALI??"
description = '''I want to know how can I decode MTP3 messages encapsulated in TCP using TALI header (rfc 3094) in WireShark?? TALI is enabled in &quot;Enabled Protocol&quot; list on WireShark. But there is no option &quot;Decode as -&amp;gt; TALI&quot; on WireShark. I am using WireShark version 1.8.3 on Windows. TALI PCAP file uploaded on...'''
date = "2013-04-16T08:48:00Z"
lastmod = "2013-04-18T07:14:00Z"
weight = 20472
keywords = [ "tali", "mtp3", "tcp" ]
aliases = [ "/questions/20472" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Query : How to decode MTP3 Message Over TCP using TALI??](/questions/20472/query-how-to-decode-mtp3-message-over-tcp-using-tali)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20472-score" class="post-score" title="current number of votes">0</div><span id="post-20472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know how can I decode MTP3 messages encapsulated in TCP using TALI header (rfc 3094) in WireShark??</p><p>TALI is enabled in "Enabled Protocol" list on WireShark. But there is no option "Decode as -&gt; TALI" on WireShark. I am using WireShark version 1.8.3 on Windows.</p><p>TALI PCAP file uploaded on cloudshark.org</p><p><a href="http://cloudshark.org/captures/cf084e5e7a74">http://cloudshark.org/captures/cf084e5e7a74</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tali" rel="tag" title="see questions tagged &#39;tali&#39;">tali</span> <span class="post-tag tag-link-mtp3" rel="tag" title="see questions tagged &#39;mtp3&#39;">mtp3</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/a273217076451fb71206e452cf39243e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="friends&#39;s gravatar image" /><p><span>friends</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="friends has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '13, 23:25</strong> </span></p></div></div><div id="comments-container-20472" class="comments-container"></div><div id="comment-tools-20472" class="comment-tools"></div><div class="clear"></div><div id="comment-20472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20474"></span>

<div id="answer-container-20474" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20474-score" class="post-score" title="current number of votes">1</div><span id="post-20474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="friends has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's TALI dissector is heuristic, meaning that it attempts to automatically identify TALI packets and decode them--regardless of the TCP ports being used. Once the packets are decoded as TALI then they should automatically be decoded as MTP3.</p><p>What does Wireshark say is the highest-level protocol in the frame? TCP or TALI?</p><p>Are you sure the traffic is TALI? Looks like the first 4 bytes of each message need to be the ASCII string "TALI". A sample capture (which you could upload to cloudshark.org) might help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-20474" class="comments-container"><span id="20495"></span><div id="comment-20495" class="comment"><div id="post-20495-score" class="comment-score"></div><div class="comment-text"><p>Traffic is in TALI. First four bytes is "TALI" and next four bytes are"mtp3".</p><pre><code>0000   00 00 00 00 00 00 02 bf 0a 00 00 79 08 00 45 00
0010   00 b1 00 00 00 00 0a 06 00 00 0a 00 00 79 00 00
0020   00 00 01 00 83 05 00 00 00 36 00 00 00 36 50 18
0030   ff ff 00 00 00 00 ***54 41 4c 49 6d 74 70 33*** 00 7f
0040   83 ea 54 ae 15 09 81 03 0e 19 0b 12 08 00 12 04
0050   94 89 41 10 32 54 0b 12 08 00 12 04 94 27 09 00
0060   00 11 5c 62 5a 48 04 ff 5c 49 19 6b 1e 28 1c 06
0070   07 00 11 86 05 01 01 01 a0 11 60 0f 80 02 07 80
0080   a1 09 06 07 04 00 00 01 00 15 02 6c 32 a1 30 02
0090   01 ec 02 01 2e 30 28 84 07 91 94 89 41 10 32 54
00a0   82 07 91 94 88 88 88 88 88 04 14 11 29 0c 91 94
00b0   99 99 99 99 99 00 00 a7 06 c8 32 9b fd 06 01</code></pre><p>TALI PCAP file uploaded on cloudshark.org</p><p><a href="http://cloudshark.org/captures/cf084e5e7a74">http://cloudshark.org/captures/cf084e5e7a74</a></p><p>I am receiving MTP3 packet from network and I am converting it into TCP packet using TALI. TALI, TCP, IP, Ethernet are dummy header added to MTP3 PDU.</p></div><div id="comment-20495-info" class="comment-info"><span class="comment-age">(16 Apr '13, 20:57)</span> <span class="comment-user userinfo">friends</span></div></div></div><div id="comment-tools-20474" class="comment-tools"></div><div class="clear"></div><div id="comment-20474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20511"></span>

<div id="answer-container-20511" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20511-score" class="post-score" title="current number of votes">0</div><span id="post-20511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's something wrong with the sending host. It uses 0.0.0.0 as destination, but more importantly it send weird overlapping segments of stream data. These are not passed on to subdissectors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '13, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-20511" class="comments-container"><span id="20516"></span><div id="comment-20516" class="comment"><div id="post-20516-score" class="comment-score"></div><div class="comment-text"><p>I tried to changing the destination address to a correct address value (192.168.1.2), still wireshark is not decoding TALI PDU.</p><p>I am receiving MTP3 packet from network and I am converting it into TCP packet using TALI. TALI, TCP, IP, Ethernet are dummy header added to MTP3 PDU. TCP layer is not decoding the TALI header, that's why it is displaying it as segmented data.</p></div><div id="comment-20516-info" class="comment-info"><span class="comment-age">(17 Apr '13, 05:13)</span> <span class="comment-user userinfo">friends</span></div></div><span id="20521"></span><div id="comment-20521" class="comment"><div id="post-20521-score" class="comment-score"></div><div class="comment-text"><p>Then your TCP dummy headers are wrong. These form overlapping segments which never present a valid TVB to the TALI dissector.</p></div><div id="comment-20521-info" class="comment-info"><span class="comment-age">(17 Apr '13, 07:43)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="20524"></span><div id="comment-20524" class="comment"><div id="post-20524-score" class="comment-score">1</div><div class="comment-text"><p>The capture shows as all the packets being segments of a reassembled PDU. That makes me think that there's a length problem somewhere.</p><p>Disabling the TALI dissector's "Reassemble TALI messages..." preference shows the packets as TALI but they are malformed at the higher layer. I didn't look further into why that is.</p><p>Looks like the length problem (which is preventing the packets from decoding as TALI normally) is that the TALI length is 32512 (which is way too big). Looks like an endianism problem.</p></div><div id="comment-20524-info" class="comment-info"><span class="comment-age">(17 Apr '13, 08:00)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="20525"></span><div id="comment-20525" class="comment"><div id="post-20525-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. This works for me.</p></div><div id="comment-20525-info" class="comment-info"><span class="comment-age">(17 Apr '13, 09:02)</span> <span class="comment-user userinfo">friends</span></div></div><span id="20544"></span><div id="comment-20544" class="comment"><div id="post-20544-score" class="comment-score">1</div><div class="comment-text"><p>If your tool is Writing a libpcap file adding the dummy headers you are better off Writing MTP3 directly into the file using a DLT of 141 which is MTP3.</p></div><div id="comment-20544-info" class="comment-info"><span class="comment-age">(17 Apr '13, 22:23)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="20549"></span><div id="comment-20549" class="comment not_top_scorer"><div id="post-20549-score" class="comment-score"></div><div class="comment-text"><p>I am getting both M3UA and MTP3 PDUs. And I am writing both into one pcap file.</p><p>If I use DLT_MTP3 then wireshark will complain for M3UA PDUs.</p></div><div id="comment-20549-info" class="comment-info"><span class="comment-age">(18 Apr '13, 00:25)</span> <span class="comment-user userinfo">friends</span></div></div><span id="20550"></span><div id="comment-20550" class="comment not_top_scorer"><div id="post-20550-score" class="comment-score"></div><div class="comment-text"><p>Sorry I don't quite get that is Wireshark complaining that it expects M3UA or ´that it gets M3UA? According to <a href="http://www.tcpdump.org/linktypes.html">http://www.tcpdump.org/linktypes.html</a> LINKTYPE_MTP3</p><p>141</p><p>DLT_MTP3</p><p>Signaling System 7 Message Transfer Part Level 3, as specified by ITU-T Recommendation Q.704, with no MTP2 header preceding the MTP3 packet.</p><p>I would expect that plain MTP3 would work, is that what you have?</p></div><div id="comment-20550-info" class="comment-info"><span class="comment-age">(18 Apr '13, 00:45)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="20571"></span><div id="comment-20571" class="comment not_top_scorer"><div id="post-20571-score" class="comment-score"></div><div class="comment-text"><p>I think what <span>@friends</span> means is that s/he's getting both MTP3 and M3UA packets and trying to put them in a single PCAP file. For that purpose, using an Ethernet PCAP file (with MTP3 embedded in TALI/TCP/IP and M3UA in SCTP/IP) is probably the easiest.</p><p>Another solution with less ugliness would be to write a PCAP-NG file and put MTP3 natively with LINKTYPE_MTP3 and M3UA with LINKTYPE_Ethernet (or whatever). But that file format's probably harder to hand build.</p></div><div id="comment-20571-info" class="comment-info"><span class="comment-age">(18 Apr '13, 07:14)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-20511" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-20511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

