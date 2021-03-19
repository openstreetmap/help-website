+++
type = "question"
title = "editcap fails to split large trace"
description = '''I have an 88Mb trace file that is proving too large for wireshark to handle on my machine. I&#x27;ve tried splitting it up into smaller files, but editcap keeps stopping after packet 218,128. If I try to use editcap to get any packets over 218,128 I just end up with an empty trace. Any ideas what could b...'''
date = "2010-12-20T00:05:00Z"
lastmod = "2010-12-20T01:13:00Z"
weight = 1401
keywords = [ "editcap" ]
aliases = [ "/questions/1401" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [editcap fails to split large trace](/questions/1401/editcap-fails-to-split-large-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1401-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an 88Mb trace file that is proving too large for wireshark to handle on my machine.</p><p>I've tried splitting it up into smaller files, but editcap keeps stopping after packet 218,128. If I try to use editcap to get any packets over 218,128 I just end up with an empty trace.</p><p>Any ideas what could be happening?</p><p>Here's some info on the trace file:</p><pre><code>C:\Program Files\Wireshark&gt;capinfos infile.pcap
File name:           infile.pcap
File type:           Wireshark/tcpdump/... - libpcap
File encapsulation:  Ethernet
Packet size limit:   file hdr: 65535 bytes
Number of packets:   5235627
File size:           91027900 bytes
Data size:           7257844 bytes
Capture duration:    1289414770 seconds
Start time:          Thu Jan 01 08:00:00 1970
End time:            Thu Nov 11 02:46:09 2010
Data byte rate:      0.01 bytes/sec
Data bit rate:       0.05 bits/sec
Average packet size: 1.39 bytes
Average packet rate: 0.00 packets/sec
SHA1:                7423f4a61fa1eece737579edd023b3243e9715c7
RIPEMD160:           8186ff80810036a867c046e686dc5d5137c9e031
MD5:                 2e725c970a09bedcc5de9aee0bc6e8e3
Strict time order:   False</code></pre></div><div id="question-tags" class="tags-container tags">editcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '10, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/2785dbc44d3e55f545951dc32f80e737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dopplershift&#39;s gravatar image" /><p>dopplershift<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dopplershift has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Dec '10, 01:09</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-1401" class="comments-container"></div><div id="comment-tools-1401" class="comment-tools"></div><div class="clear"></div><div id="comment-1401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1402"></span>

<div id="answer-container-1402" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1402-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like your file is corrupt somehow. First of all, it has a duration of more than 40 years. But most important, the data size is smaller than the file size, which is impossible when the packet size limit is 65535.</p><p>How did you transfer this file from the capture location to your windows system? If by FTP, did you use binary mode?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '10, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1402" class="comments-container"><span id="1413"></span><div id="comment-1413" class="comment"><div id="post-1413-score" class="comment-score"></div><div class="comment-text"><p>Haha, yeah, thanks SYNbit. I noticed the timestamps and just assumed it was a mistake somehow (I'm not sure how wireshark gets this info, but I thought maybe the computer's clock had been reset while capturing?).</p><p>Unfortunately, it wasn't me who did the capture. And I'm not sure how it was transferred to our system... most likely copied and pasted via remote desktop (I'm in Perth and the site is in Melbourne). I'll try and get some answers to these questions.</p><p>In the meantime I'm just looking at the first 218,128 packets (about 15mins)... trying to find anything unusual.</p></div><div id="comment-1413-info" class="comment-info"><span class="comment-age">(20 Dec '10, 16:54)</span> dopplershift</div></div><span id="1420"></span><div id="comment-1420" class="comment"><div id="post-1420-score" class="comment-score"></div><div class="comment-text"><p>Thursday, January 1, 1970, 00:00:00 UTC was Thursday, January 1, 08:00:00 local time in Perth, and is a time_t value of 0, so the time stamp of the first packet in the capture is probably bad.</p><p>Does editcap print anything before it stops?</p><p>If not, what happens if you run tshark on the file and, if possible, send the standard output to NUL:?</p></div><div id="comment-1420-info" class="comment-info"><span class="comment-age">(20 Dec '10, 19:44)</span> Guy Harris ♦♦</div></div><span id="1421"></span><div id="comment-1421" class="comment"><div id="post-1421-score" class="comment-score"></div><div class="comment-text"><p>If I ask editcap to split the file into uniformly sized pieces, it prints out "Packet: 1","Packet: 2", up to "Packet: 218128" and then just stops.</p><p>If I ask editcap to put a range of packets into a new file it says "Add_Selected: 0-218128" then "Inclusive ... 0, 218128" and then stops.</p></div><div id="comment-1421-info" class="comment-info"><span class="comment-age">(20 Dec '10, 22:45)</span> dopplershift</div></div><span id="1422"></span><div id="comment-1422" class="comment"><div id="post-1422-score" class="comment-score"></div><div class="comment-text"><p>Running tshark (just with -r)on the file just spits out packet info from packet 1 onwards until it starts sayong "252448 -1289413907.163060 -&gt; Ethernet [Malformed Packet]" etc. I missed when this transition occurred, but presumably it was at 21,8129. It took a good 6 or 7mins to get there though.</p><p>Running tshark and sending the output to nul just hangs the cmd window for an unknown amount of time.</p><p>So, malformed packets hey? What does this mean and why does it break editcap?</p><p>Thanks again</p></div><div id="comment-1422-info" class="comment-info"><span class="comment-age">(20 Dec '10, 22:45)</span> dopplershift</div></div><span id="1423"></span><div id="comment-1423" class="comment"><div id="post-1423-score" class="comment-score"></div><div class="comment-text"><p>When you say "If I ask editcap to split the file into uniformly sized pieces, it prints out "Packet: 1","Packet: 2", up to "Packet: 218128" and then just stops.", what command-line arguments did you pass to editcap? Was it a "-c" argument?</p><p>When you say "If I ask editcap to put a range of packets into a new file it says "Add_Selected: 0-218128" then "Inclusive ... 0, 218128" and then stops.", what command-line arguments did you pass to editcap?</p></div><div id="comment-1423-info" class="comment-info"><span class="comment-age">(20 Dec '10, 23:26)</span> Guy Harris ♦♦</div></div><span id="1424"></span><div id="comment-1424" class="comment not_top_scorer"><div id="post-1424-score" class="comment-score"></div><div class="comment-text"><p>The transition in TShark occurred at packet 252,448, because it said so.</p><p>252448 != 218128, so it's not clear that editcap's problem is the same as TShark's problem. TShark's problem is reported by a packet dissector; editcap doesn't do any packet dissection.</p></div><div id="comment-1424-info" class="comment-info"><span class="comment-age">(20 Dec '10, 23:26)</span> Guy Harris ♦♦</div></div><span id="1425"></span><div id="comment-1425" class="comment not_top_scorer"><div id="post-1425-score" class="comment-score"></div><div class="comment-text"><p>Is the unknown amount of time greater than, or less than or equal to, 6-7 minutes? If it's about 6 or 7 minutes, the command window probably isn't hanging - it's probably just running TShark, which is doing the same work that it did when you didn't redirect the output. (It'd probably take less than 6-7 minutes, though, as it's sending the packet dissection to the null device rather than to the cmd.exe window.)</p></div><div id="comment-1425-info" class="comment-info"><span class="comment-age">(20 Dec '10, 23:26)</span> Guy Harris ♦♦</div></div><span id="1428"></span><div id="comment-1428" class="comment not_top_scorer"><div id="post-1428-score" class="comment-score"></div><div class="comment-text"><p>Could you post the output of:</p><p>tshark -nr &lt;file&gt; -R "frame.number&gt;=218128 and frame.number&lt;=218129" -V -x</p></div><div id="comment-1428-info" class="comment-info"><span class="comment-age">(21 Dec '10, 02:32)</span> SYN-bit ♦♦</div></div><span id="1444"></span><div id="comment-1444" class="comment not_top_scorer"><div id="post-1444-score" class="comment-score"></div><div class="comment-text"><blockquote><p>editcap -v -c 50000 infile.pcap outfile.pcap</p></blockquote><p>and</p><blockquote><p>editcap -v -r infile.pcap outfile.pcap 0-218128</p></blockquote></div><div id="comment-1444-info" class="comment-info"><span class="comment-age">(21 Dec '10, 18:06)</span> dopplershift</div></div></div><div id="comment-tools-1402" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-1402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

