+++
type = "question"
title = "How to measure throughput with tshark ?"
description = '''Hello, I&#x27;m trying to measure the throughput for PCAP files. any idea about how to do it ?'''
date = "2015-07-16T06:26:00Z"
lastmod = "2015-07-16T06:47:00Z"
weight = 44209
keywords = [ "pcap", "throughput", "tshark" ]
aliases = [ "/questions/44209" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to measure throughput with tshark ?](/questions/44209/how-to-measure-throughput-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44209-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to measure the throughput for PCAP files. any idea about how to do it ?</p></div><div id="question-tags" class="tags-container tags">pcap throughput tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '15, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/0df72a5f5db5a2c33c8f966dd7262b66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alessio77&#39;s gravatar image" /><p>alessio77<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alessio77 has no accepted answers">0%</span></p></div></div><div id="comments-container-44209" class="comments-container"></div><div id="comment-tools-44209" class="comment-tools"></div><div class="clear"></div><div id="comment-44209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44210"></span>

<div id="answer-container-44210" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44210-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use the command line tool capinfos from the Wireshark suite, sample output:</p><pre><code>C:\temp&gt; &#39;C:\Program Files\Wireshark\capinfos.exe&#39; test.pcapng
File name:           test.pcapng
File type:           Wireshark/... - pcapng                    
File encapsulation:  Ethernet                                  
Packet size limit:   file hdr: (not set)                       
Number of packets:   13 k                                      
File size:           1957 kB                                   
Data size:           1517 kB                                   
Capture duration:    28 seconds                                
First packet time:   2015-05-31 16:20:24                       
Last packet time:    2015-05-31 16:20:52                       
Data byte rate:      55 kBps                                   
Data bit rate:       440 kbps                                  
Average packet size: 114.41 bytes                              
Average packet rate: 480 packets/s                             
SHA1:                96131ed5b7f8ae4583cd7b82bbf6e294435704a6  
RIPEMD160:           75cd6e0ae3da1041bb3914fac70abd482fe8e15b  
MD5:                 95d7eb35fdcb2a27e1afa580a754f39e          
Strict time order:   True</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '15, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44210" class="comments-container"><span id="44412"></span><div id="comment-44412" class="comment"><div id="post-44412-score" class="comment-score"></div><div class="comment-text"><p>Thanks, then how can i use it for calculating throughput ?</p></div><div id="comment-44412-info" class="comment-info"><span class="comment-age">(23 Jul '15, 04:20)</span> alessio77</div></div><span id="44415"></span><div id="comment-44415" class="comment"><div id="post-44415-score" class="comment-score">1</div><div class="comment-text"><p>What do you mean by "throughput". The capinfos output has stats such as Data byte rate, Data bit rate, Average packet rate.</p></div><div id="comment-44415-info" class="comment-info"><span class="comment-age">(23 Jul '15, 04:40)</span> grahamb ♦</div></div><span id="44761"></span><div id="comment-44761" class="comment"><div id="post-44761-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply, I mean, I wanna find a way to calculate the throughput of a PCAP file , So, need a command-line based tool , like this one or tshark , ... if i think right :</p><p>Bit rate (simplified) is the number of bits per second required to produce a given level of quality for a given media codec.</p><p>Throughput is the rate of transfer one is able to sustain over a data link (which could be between two remote locations through the internet or a data bus internally in a computer).</p></div><div id="comment-44761-info" class="comment-info"><span class="comment-age">(03 Aug '15, 03:43)</span> alessio77</div></div><span id="44763"></span><div id="comment-44763" class="comment"><div id="post-44763-score" class="comment-score">1</div><div class="comment-text"><p>A pcap file will only tell you what has happened, it can't predict what the maximum rate will be for a given codec.</p><p>It sounds as though you are looking for end-to-end connectivity and performance tools, which isn't what Wireshark and the rest of the suite do. The can give you some statistics on what you have captured, but that only relates to the actual traffic captured.</p></div><div id="comment-44763-info" class="comment-info"><span class="comment-age">(03 Aug '15, 04:04)</span> grahamb ♦</div></div><span id="44774"></span><div id="comment-44774" class="comment not_top_scorer"><div id="post-44774-score" class="comment-score"></div><div class="comment-text"><p>Dear Graham, So you think there is no solution in this manner ? the pcap file are buch of packets that came from a public addreses to my source. and the public address for each pcap is different. Do you think it would be possible to just care about data transffered and time duration ? because i think i should just care about pure data not other packets like header and hanshake and ....</p><p>thanks for your support :)</p></div><div id="comment-44774-info" class="comment-info"><span class="comment-age">(03 Aug '15, 06:44)</span> alessio77</div></div><span id="44779"></span><div id="comment-44779" class="comment not_top_scorer"><div id="post-44779-score" class="comment-score"></div><div class="comment-text"><p>Tshark does have the <code>-z, ...</code> statistics options that might be more help to you. Have you looked at the tshark <a href="https://www.wireshark.org/docs/man-pages/tshark.html">man</a> page?</p></div><div id="comment-44779-info" class="comment-info"><span class="comment-age">(03 Aug '15, 06:49)</span> grahamb ♦</div></div><span id="44818"></span><div id="comment-44818" class="comment not_top_scorer"><div id="post-44818-score" class="comment-score"></div><div class="comment-text"><p>Yes, i used it alot for other metrics, but seems throughput is not that much straight. The point is i should care about the amount of data that has been transfered in a period of time. but the file is has more packets like handshake, payload,... and also find out the exact time for data transition. the i can use these two for calculating throughput (If i think right...). It seems t shark will not give me this kind of info or a method for calculation of throughput of a PCAP file. what do you think sir ?</p></div><div id="comment-44818-info" class="comment-info"><span class="comment-age">(04 Aug '15, 05:31)</span> alessio77</div></div><span id="44819"></span><div id="comment-44819" class="comment"><div id="post-44819-score" class="comment-score">1</div><div class="comment-text"><p>As you still haven't really defined what you mean by "throughput" it's a bit difficult to help you any further.</p><p>It seems you are interested in the payload of certain protocols rather than just the total bytes transferred over the length of the pcap file. Can you list which protocols those are?</p></div><div id="comment-44819-info" class="comment-info"><span class="comment-age">(04 Aug '15, 06:25)</span> grahamb ♦</div></div><span id="44855"></span><div id="comment-44855" class="comment not_top_scorer"><div id="post-44855-score" class="comment-score"></div><div class="comment-text"><p>Dear Graham, I have bunch of PCAP file , and wanna analyse them based on several metrics , i do no have problem with RTT, packet loss, ... But, for throughput it's a bit complicate for me. Yes, you right... I wanna care about the total amount of "DATA" that transferred in unit of time to find out throughput, and probably for accurate measure just should care about data size, not other annoying packets if i right ... i need to extract these info woth command-line because wanna apply it to all the pcap files with a script. The protocol here is TCP.</p></div><div id="comment-44855-info" class="comment-info"><span class="comment-age">(05 Aug '15, 01:04)</span> alessio77</div></div></div><div id="comment-tools-44210" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-44210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

