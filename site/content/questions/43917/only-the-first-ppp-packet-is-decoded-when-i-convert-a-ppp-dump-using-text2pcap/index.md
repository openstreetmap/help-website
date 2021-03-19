+++
type = "question"
title = "Only the first ppp packet is decoded when I convert a ppp dump using text2pcap"
description = '''I have a ppp stream over a serial port. Each ppp packet contains an IP datagram, with an ICMP message (ping). I have removed the HDLC headers (7E FF 03) from the stream, and I have also corrected the characters escaped with 0x7D. I convert this ppp dump using text2pcap -l 9 (DLT_PPP protocol), but i...'''
date = "2015-07-07T01:38:00Z"
lastmod = "2015-07-09T06:37:00Z"
weight = 43917
keywords = [ "text2pcap", "ppp", "hdlc", "wireshark" ]
aliases = [ "/questions/43917" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Only the first ppp packet is decoded when I convert a ppp dump using text2pcap](/questions/43917/only-the-first-ppp-packet-is-decoded-when-i-convert-a-ppp-dump-using-text2pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43917-score" class="post-score" title="current number of votes">0</div><span id="post-43917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a ppp stream over a serial port. Each ppp packet contains an IP datagram, with an ICMP message (ping). I have removed the HDLC headers (7E FF 03) from the stream, and I have also corrected the characters escaped with 0x7D.</p><p>I convert this ppp dump using text2pcap -l 9 (DLT_PPP protocol), but in the resulting pcap file, only the first ppp packet is decoded, as you can see in the following image:</p><p><img src="http://oi58.tinypic.com/6fsfph.jpg" alt="capture" /></p><p>I have checked the IP length, and it is right. I have also compared my capture with "ppp-dialup-munged.pcap" in <a href="https://wiki.wireshark.org/PPP">https://wiki.wireshark.org/PPP</a> and, in both captures, packets have a two-byte FCS after the IP datagram, just before the next packet.</p><p>Why in my case the next packet is not decoded? Should I signal in the raw file where the next packet begins?</p><p>The raw file I convert with text2pcap is:</p><pre><code>000000 00 21 45 00 00 3C 6E 5D 00 00 80 01 E9 01 C0 A8 
000010 0E 21 08 00 0C 99 00 00 52 5C 02 00 01 00 61 62 
000020 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 
000030 73 74 75 76 77 61 62 63 64 65 66 67 68 69 CD 94 
000040 00 21 45 00 00 3C 6E 5E 00 00 80 01 E9 00 C0 A8 
000050 0E 21 08 00 0C 99 00 00 51 5C 02 00 02 00 61 62 
000060 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 
000070 73 74 75 76 77 61 62 63 64 65 66 67 68 69 5D 14 
000080 00 21 45 00 00 3C 6E 5F 00 00 80 01 E8 FF C0 A8 
000090 0E 21 08 00 0C 99 00 00 50 5C 02 00 03 00 61 62 
0000A0 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 
0000B0 73 74 75 76 77 61 62 63 64 65 66 67 68 69 A1 3C 
0000C0 00 21 45 00 00 3C 6E 60 00 00 80 01 E8 FE C0 A8 
0000D0 0E 21 08 00 0C 99 00 00 4F 5C 02 00 04 00 61 62 
0000E0 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 
0000F0 73 74 75 76 77 61 62 63 64 65 66 67 68 69 75 1C 
000100</code></pre><p>New packets should start in 0x000000, 0x000040, 0x000080 and 0x0000C0 (the begining is 00 21, IP protocol). Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span> <span class="post-tag tag-link-ppp" rel="tag" title="see questions tagged &#39;ppp&#39;">ppp</span> <span class="post-tag tag-link-hdlc" rel="tag" title="see questions tagged &#39;hdlc&#39;">hdlc</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '15, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/650d241a03ae63cf616b958ffe420fab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcibar&#39;s gravatar image" /><p><span>jcibar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcibar has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jul '15, 01:42</strong> </span></p></div></div><div id="comments-container-43917" class="comments-container"></div><div id="comment-tools-43917" class="comment-tools"></div><div class="clear"></div><div id="comment-43917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43919"></span>

<div id="answer-container-43919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43919-score" class="post-score" title="current number of votes">1</div><span id="post-43919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are 4 64 bytes PPP frames in the data so you must add the max packet length parameter to text2pcap of <code>-m 64</code>.</p><p>When viewing the capture in Wireshark you should also set the PPP protocol preference "PPP Frame Checksum Type" to "16-Bit".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '15, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-43919" class="comments-container"></div><div id="comment-tools-43919" class="comment-tools"></div><div class="clear"></div><div id="comment-43919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44007"></span>

<div id="answer-container-44007" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44007-score" class="post-score" title="current number of votes">0</div><span id="post-44007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Finally, I solved the issue restarting the byte count digits when a new packet starts (that is, the new packet starts with 000000):</p><pre><code>000000 00 21 45 00 00 3C 6E 5D 00 00 80 01 E9 01 C0 A8 
000010 0E 21 08 00 0C 99 00 00 52 5C 02 00 01 00 61 62 
000020 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 
000030 73 74 75 76 77 61 62 63 64 65 66 67 68 69 CD 94 
000040    
000000 00 21 45 00 00 3C 6E 5E 00 00 80 01 E9 00 C0 A8 
000010 0E 21 08 00 0C 99 00 00 51 5C 02 00 02 00 61 62 
000020 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 
000030 73 74 75 76 77 61 62 63 64 65 66 67 68 69 5D 14 
000040    
000000 00 21 45 00 00 3C 6E 5F 00 00 80 01 E8 FF C0 A8 
000010 0E 21 08 00 0C 99 00 00 50 5C 02 00 03 00 61 62 
000020 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 
000030 73 74 75 76 77 61 62 63 64 65 66 67 68 69 A1 3C 
000040
000000 00 21 45 00 00 3C 6E 60 00 00 80 01 E8 FE C0 A8 
000010 0E 21 08 00 0C 99 00 00 4F 5C 02 00 04 00 61 62 
000020 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 
000030 73 74 75 76 77 61 62 63 64 65 66 67 68 69 75 1C 
000040</code></pre><p>Thanks for your help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '15, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/650d241a03ae63cf616b958ffe420fab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcibar&#39;s gravatar image" /><p><span>jcibar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcibar has no accepted answers">0%</span></p></div></div><div id="comments-container-44007" class="comments-container"></div><div id="comment-tools-44007" class="comment-tools"></div><div class="clear"></div><div id="comment-44007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

