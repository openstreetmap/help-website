+++
type = "question"
title = "identify packet"
description = '''I need some assistance getting started with WireShark and identifying the data it is capturing.  The source computer is Windows XP and the destination is Windows Server 2008. Below are a few lines from one packet of a capture. The send computer is IP address 192.10.11.227 (in hex c0 a0 0b e3) and th...'''
date = "2011-11-24T20:24:00Z"
lastmod = "2011-11-26T19:27:00Z"
weight = 7621
keywords = [ "packet", "format" ]
aliases = [ "/questions/7621" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [identify packet](/questions/7621/identify-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7621-score" class="post-score" title="current number of votes">0</div><span id="post-7621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need some assistance getting started with WireShark and identifying the data it is capturing. The source computer is Windows XP and the destination is Windows Server 2008.</p><p>Below are a few lines from one packet of a capture. The send computer is IP address 192.10.11.227 (in hex c0 a0 0b e3) and the destination is 192.10.11.222 (in hex c0 a0 0b de) . I think that the sender has the server role while the receiver is client.<br />
</p><p>Contrary to my book the source address is in byte number 001A, not in the first byte. So what are bytes 0000 through 0019?</p><p>Starting with byte 0034 I can identify the payload as the data sent from the application. I take that as meaning the last four bytes of the header are 0030 through 0033. Is that correct?</p><p>Please post a link to a web page that provides this information. I did some searches and was unable to find a match.</p><p>Edit: after original post, I edited off the text display on the right side to make the post more readable.</p><pre><code>No. Time      Source        Destination   Protocol  Info
26  61.060962 192.10.11.227 192.10.11.222 TCP       49000 &gt; 55344 [ACK] Seq=1

0000 00 10 18 4f 8e 80 00 10 6f 0f 20 26 08 00 45 00
0010 05 de 21 5d 40 00 80 06 3b e9 c0 0a 0b e3 c0 0a
0020 0b de bf 68 d8 30 91 da 9b 27 7a 56 75 59 50 10
0030 ff ff d5 ee 00 00 14 06 00 00 00 00 00 00 00 00
0040 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0050 00 00 00 00 00 00 01 00 00 00 04 00 00 00 17 01
0060 00 00 02 00 00 00 04 00 00 00 ec 88 38 2a 03 00
0070 00 00 04 00 00 00 00 00 00 00 05 00 00 00 04 00
0080 00 00 00 00 00 00 04 00 00 00 c8 05 00 00 00 00</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '11, 20:24</strong></p><img src="https://secure.gravatar.com/avatar/68c6ec7e9c6a5614e85d20345c5597e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bkelly&#39;s gravatar image" /><p><span>bkelly</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bkelly has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '11, 15:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7621" class="comments-container"></div><div id="comment-tools-7621" class="comment-tools"></div><div class="clear"></div><div id="comment-7621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7640"></span>

<div id="answer-container-7640" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7640-score" class="post-score" title="current number of votes">3</div><span id="post-7640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bkelly has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>0000 00 10 18 4f 8e 80</code></pre><p>Destination Ethernet address</p><pre><code>                        00 10 6f 0f 20 26</code></pre><p>Source Ethernet address</p><pre><code>                                          08 00</code></pre><p>Ethernet type field = 0x0800 means IPv4</p><pre><code>                                                45</code></pre><p>IPv4 version and header length field - version 4, 5 32-bit words or 20 bytes</p><pre><code>                                                   00</code></pre><p>IPv4 Type of Service/whatever it's called code point; 0 means "ordinary boring packet"</p><pre><code>0010 05 de</code></pre><p>Total length of the IPv4 datagram; 0x05d3 = 1491 bytes</p><pre><code>           21 5d</code></pre><p>Identification - 0x215d</p><pre><code>                 40 00</code></pre><p>Flags and fragment offset - Don't Fragment and fragment offset of 0, meaning "not fragmented"</p><pre><code>                       80</code></pre><p>Time to live; 0x80 = 128</p><pre><code>                          06</code></pre><p>Protocol; 0x06 = 6 = TCP</p><pre><code>                             3b e9</code></pre><p>Header checksum = 0x3be9</p><pre><code>                                    c0 0a 0b e3</code></pre><p>Source IP address = 0xc0 0c0a 0x0b 0xe3 = 192.10.11.227</p><pre><code>                                                 c0 0a

0020 0b de</code></pre><p>Destination IP address = 0xc0 0x0a 0x0b 0xd3 = 192.10.11.222</p><pre><code>           bf 68</code></pre><p>TCP source port; 0xbf68 = 49000</p><pre><code>                 d8 30</code></pre><p>TCP destination port; 0xd830 = 55344</p><pre><code>                       91 da 9b 27</code></pre><p>Sequence number; 0x91da9b27 = 2447022887</p><pre><code>                                   7a 56 75 59</code></pre><p>Acknowledgment number; 0x7a567559 = 2052486489</p><pre><code>                                               50</code></pre><p>Data offset; 0x5 = 5 32-bit words = 20 bytes</p><pre><code>                                                  10</code></pre><p>Flags; 0x10 = ACK</p><pre><code>0030 ff ff</code></pre><p>Window; 0xffff = 65535</p><pre><code>           d5 ee</code></pre><p>Checksum; 0xd5ee</p><pre><code>                 00 00</code></pre><p>Urgent pointer; 0x0000 = 0</p><pre><code>                       14 06 00 00 00 00 00 00 00 00
0040 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0050 00 00 00 00 00 00 01 00 00 00 04 00 00 00 17 01
0060 00 00 02 00 00 00 04 00 00 00 ec 88 38 2a 03 00
0070 00 00 04 00 00 00 00 00 00 00 05 00 00 00 04 00
0080 00 00 00 00 00 00 04 00 00 00 c8 05 00 00 00 00</code></pre><p>That's all TCP payload. It starts at 0x0036, not 0x0034; it's preceded by 14 bytes of Ethernet header and 20 bytes of IP header and 20 bytes of TCP header, so it's at an offset of decimal 54 = 0x36.</p><p>Bytes 0000 through 0019 are the Ethernet header and the IPv4 header up to and including the first byte of the IP header checksum. The IP source address starts at 001B.</p><p>For a description of the Ethernet header, see <a href="http://en.wikipedia.org/wiki/Ethernet_frame">the Wikipedia page for the Ethernet frame</a>. Note that the preamble and start-of-frame delimiter are <em>NOT</em> part of the capture.</p><p>For a description of the IPv4 header, see <a href="http://en.wikipedia.org/wiki/IPv4#Packet_structure">the "Packet structure" section of the Wikipedia page for IPv4</a>. For a description of the TCP header, see <a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure">the "TCP segment structure" section for the Wikipedia page for TCP</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '11, 15:19</strong> </span></p></div></div><div id="comments-container-7640" class="comments-container"><span id="7641"></span><div id="comment-7641" class="comment"><div id="post-7641-score" class="comment-score"></div><div class="comment-text"><p>And like Jaap said: This is wireshark is for, to do this analysis for you, instead of doing it yourself :-)</p></div><div id="comment-7641-info" class="comment-info"><span class="comment-age">(25 Nov '11, 15:16)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="7643"></span><div id="comment-7643" class="comment"><div id="post-7643-score" class="comment-score"></div><div class="comment-text"><p>Ha, the man is a machine. Leaving tools at home and Stevens on the bookshelf. We're such n00bs. ;)</p></div><div id="comment-7643-info" class="comment-info"><span class="comment-age">(25 Nov '11, 20:26)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="7656"></span><div id="comment-7656" class="comment"><div id="post-7656-score" class="comment-score"></div><div class="comment-text"><p>The preamble threw me for a bit. I need to read more about that offset and what it means. I would like to let wireshark analyze everything, but there is something wrong with my code as detected by the receiving program not accepting my data. I need to check all the fields for correctness, and I think I found a problem. But that is in my code and not suitable for a question here.</p><p>Guy, Thank you for taking the time to write that all out.</p></div><div id="comment-7656-info" class="comment-info"><span class="comment-age">(26 Nov '11, 19:27)</span> <span class="comment-user userinfo">bkelly</span></div></div></div><div id="comment-tools-7640" class="comment-tools"></div><div class="clear"></div><div id="comment-7640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7624"></span>

<div id="answer-container-7624" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7624-score" class="post-score" title="current number of votes">0</div><span id="post-7624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm thinking your analysis is flawed. The raw bytes as you see them are the complete Ehternet frame. So they start with the 6 byte destination MAC address (a Broadcom device) and source MAC address (a Trenton Technology device). The rest I didn't figure out. but from the first line it seems that Wireshark did, so why not look at the packet details?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7624" class="comments-container"></div><div id="comment-tools-7624" class="comment-tools"></div><div class="clear"></div><div id="comment-7624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

