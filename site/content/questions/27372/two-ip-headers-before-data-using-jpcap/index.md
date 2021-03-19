+++
type = "question"
title = "Two IP headers before data -- using jpcap"
description = '''I am creating IP packets and sending them over ethernet. I am using jpcap library for it. When I analyze the packet using wireshark, it shows the protocol as eth:ip:ip, i.e. two IP headers followed by the data. So some of my data following the 1st IP header is treated as header itself!! This is crea...'''
date = "2013-11-26T00:13:00Z"
lastmod = "2013-11-26T03:43:00Z"
weight = 27372
keywords = [ "ip", "jpcap", "wireshark" ]
aliases = [ "/questions/27372" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Two IP headers before data -- using jpcap](/questions/27372/two-ip-headers-before-data-using-jpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27372-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am creating IP packets and sending them over ethernet. I am using jpcap library for it. When I analyze the packet using wireshark, it shows the protocol as eth:ip:ip, i.e. two IP headers followed by the data. So some of my data following the 1st IP header is treated as header itself!! This is creating a lot of trouble. This is bizzare, and I am not able to understand the reason behind it. Does it have to do anything with wireshark setting, or the jpcap library??</p></div><div id="question-tags" class="tags-container tags">ip jpcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/24af0b45730f0aeb823e25cd0c541bc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mohit93&#39;s gravatar image" /><p>mohit93<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mohit93 has no accepted answers">0%</span></p></div></div><div id="comments-container-27372" class="comments-container"><span id="27396"></span><div id="comment-27396" class="comment"><div id="post-27396-score" class="comment-score"></div><div class="comment-text"><p>Please post a sample capture file somewhere (Google drive, dropbox,cloudshark.org, mega.co.nz)</p></div><div id="comment-27396-info" class="comment-info"><span class="comment-age">(26 Nov '13, 02:51)</span> Kurt Knochner ♦</div></div><span id="27402"></span><div id="comment-27402" class="comment"><div id="post-27402-score" class="comment-score"></div><div class="comment-text"><p>This is the link for the wireshark capture. Notice the top line: Protocols in frame[eth:ip:ip] <a href="https://drive.google.com/file/d/0BzzMYblB9rVPajNhbGRIcTlxdFE/edit?usp=sharing">https://drive.google.com/file/d/0BzzMYblB9rVPajNhbGRIcTlxdFE/edit?usp=sharing</a></p></div><div id="comment-27402-info" class="comment-info"><span class="comment-age">(26 Nov '13, 03:36)</span> mohit93</div></div></div><div id="comment-tools-27372" class="comment-tools"></div><div class="clear"></div><div id="comment-27372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27403"></span>

<div id="answer-container-27403" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27403-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>This is the link for the wireshark capture. Notice the top line: Protocols in frame[eth:ip:ip] <a href="https://drive.google.com/file/d/0BzzMYblB9rVPajNhbGRIcTlxdFE/edit?usp=sharing">https://drive.google.com/file/d/0BzzMYblB9rVPajNhbGRIcTlxdFE/edit?usp=sharing</a></p></blockquote><p>If you look at the line below the marked one (blue), you will see that the IP protocol type is 'IP in IP'. That's the reason why Wireshark shows two IP headers. If that was not your intention, why did you choose protocol type 0x04 (IP in IP)? If you want TCP (protocol 0x06) or UDP (protocol 0x11) then please choose the right protocol in your IP header.</p><blockquote><p><a href="http://en.wikipedia.org/wiki/IPv4_header#Header">http://en.wikipedia.org/wiki/IPv4_header#Header</a></p></blockquote><p>Maybe you just misinterpreted that field as IP protocol <strong>version</strong> and thus you chose the value of 4.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '13, 04:04</p></div></div><div id="comments-container-27403" class="comments-container"><span id="27407"></span><div id="comment-27407" class="comment"><div id="post-27407-score" class="comment-score"></div><div class="comment-text"><p>@Kurt: Thanks for pointing that out. So, the protocol field decides which higher-level protocol uses this IP header. But I just want to send this IP packet over ethernet. No other protocol should encapsulate it. So, What should I set my protocol number as??</p></div><div id="comment-27407-info" class="comment-info"><span class="comment-age">(26 Nov '13, 03:53)</span> mohit93</div></div><span id="27410"></span><div id="comment-27410" class="comment"><div id="post-27410-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So, the protocol field decides which higher-level protocol uses this IP header.</p></blockquote><p>yes.</p><blockquote><p>But I just want to send this IP packet over ethernet. No other protocol should encapsulate it. So, What should I set my protocol number as??</p></blockquote><p>Try 255, as that value is officially reserved and I <strong>guess</strong> Wireshark will not dissect it in any way.</p><blockquote><p><a href="http://en.wikipedia.org/wiki/List_of_IP_protocol_numbers">http://en.wikipedia.org/wiki/List_of_IP_protocol_numbers</a></p></blockquote><p>If that does not work, try other values from the link above, like 253 or 254 (for testing and experimenting) or any value from the range (143-252 -&gt; UNASSIGNED).</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p><p>Regards<br />
Kurt</p></div><div id="comment-27410-info" class="comment-info"><span class="comment-age">(26 Nov '13, 04:02)</span> Kurt Knochner ♦</div></div><span id="27413"></span><div id="comment-27413" class="comment"><div id="post-27413-score" class="comment-score"></div><div class="comment-text"><p>@Kurt: Thanks for the great help. With 255, Wireshark is not dissecting it, so I can see my data alright. Just one more doubt: This reserved protocol number won't affect its transmission over Ethernet, and I can read the packet as it is on the other end? Do all the packets in the network need to have one of these standard protocol numbers? Aren't there any simple IP packets in the network, which are not used by any other layer?</p></div><div id="comment-27413-info" class="comment-info"><span class="comment-age">(26 Nov '13, 04:18)</span> mohit93</div></div><span id="27414"></span><div id="comment-27414" class="comment"><div id="post-27414-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ust one more doubt: This reserved protocol number won't affect its transmission over Ethernet,</p></blockquote><p>well, I cannot guarantee that, as it obviously depends on the device that handles your IP packet. A switch will not care, neither will a router. <strong>However</strong> a firewall might decide to drop the frame for several reasons (firmware, configuration, etc.).</p><blockquote><p>Do all the packets in the network need to have <strong>one of these standard protocol numbers</strong>?</p></blockquote><p>No, you don't have to choose one of the <strong>standard protocol numbers</strong>. You are free to choose whatever is appropriate for your protocol. However: firewalls will certainly only allow what they know and that's mostly the <strong>standard protocols</strong>, while most of the firewalls I know of, can be configured to allow whatever you want.</p><blockquote><p>Aren't there any simple IP packets in the network, which are not used by any other layer?</p></blockquote><p>Not that I know of, because the idea of IP is to be a transport mechanism (routing) for the payload (data) of higher layer protocols.</p><p>Please work through the TCP/IP guide. It will explain some of those TCP/IP basics.</p><blockquote><p><a href="http://www.tcpipguide.com/">http://www.tcpipguide.com/</a></p></blockquote><p>or read the classic book, <strong>TCP/IP Illustrated Volume 1</strong></p><blockquote><p><a href="https://www.google.com/?q=amazon+TCP%2FIP+Illustrated%2C+Volume+1">https://www.google.com/?q=amazon+TCP%2FIP+Illustrated%2C+Volume+1</a></p></blockquote></div><div id="comment-27414-info" class="comment-info"><span class="comment-age">(26 Nov '13, 04:29)</span> Kurt Knochner ♦</div></div><span id="27415"></span><div id="comment-27415" class="comment"><div id="post-27415-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the great help! It is a FPGA on the other side, so I don't think there will be any firewall issues! Thanks again!</p></div><div id="comment-27415-info" class="comment-info"><span class="comment-age">(26 Nov '13, 04:38)</span> mohit93</div></div></div><div id="comment-tools-27403" class="comment-tools"></div><div class="clear"></div><div id="comment-27403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27380"></span>

<div id="answer-container-27380" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27380-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't make things up (it may annotate captures with such things as sequence analysis), it shows what has been captured.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-27380" class="comments-container"></div><div id="comment-tools-27380" class="comment-tools"></div><div class="clear"></div><div id="comment-27380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

