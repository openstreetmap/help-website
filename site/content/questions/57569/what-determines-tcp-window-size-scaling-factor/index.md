+++
type = "question"
title = "What Determines TCP Window Size Scaling Factor?"
description = '''I am troubleshooting why doing a FTP GET is much slower than doing a FTP PUT. I&#x27;ve noticed in Wireshark traces, on the FTP-DATA packets, that the TCP window size scaling factor is consistently larger when doing a PUT (32) versus a GET (128). I suspect this is affecting throughput, but am not certain...'''
date = "2016-11-23T07:22:00Z"
lastmod = "2016-11-24T03:16:00Z"
weight = 57569
keywords = [ "ftp", "windowscaling" ]
aliases = [ "/questions/57569" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What Determines TCP Window Size Scaling Factor?](/questions/57569/what-determines-tcp-window-size-scaling-factor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57569-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am troubleshooting why doing a FTP GET is much slower than doing a FTP PUT. I've noticed in Wireshark traces, on the FTP-DATA packets, that the TCP window size scaling factor is consistently larger when doing a PUT (32) versus a GET (128). I suspect this is affecting throughput, but am not certain.</p><p>I also observed similar behavior with iPerf; using the -R (reverse) flag, I consistently see much worse performance. When setting the window size larger, it makes a difference on the send but not on the receive.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags">ftp windowscaling</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '16, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/bc5894d5e17283b7665fa5d468e050b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PhoenixGrad&#39;s gravatar image" /><p>PhoenixGrad<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PhoenixGrad has no accepted answers">0%</span></p></div></div><div id="comments-container-57569" class="comments-container"><span id="57570"></span><div id="comment-57570" class="comment"><div id="post-57570-score" class="comment-score"></div><div class="comment-text"><p>Could you <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">share us a trace</a>? Either ftp or iperf.</p></div><div id="comment-57570-info" class="comment-info"><span class="comment-age">(23 Nov '16, 07:43)</span> Christian_R</div></div><span id="57572"></span><div id="comment-57572" class="comment"><div id="post-57572-score" class="comment-score"></div><div class="comment-text"><p>Capture done with iPerf and WireShark.</p><p>0 - 10: Send, no window size specified. 24 - 35: Receive, no window size specified. 52 - 63: Send, 1M window size specified. 83 - 93: Receive, 1M window size specified.</p><p><a href="https://drive.google.com/file/d/0BzBe-IJh8phKUWJleHVydzBvY1U/view?usp=sharing">https://drive.google.com/file/d/0BzBe-IJh8phKUWJleHVydzBvY1U/view?usp=sharing</a></p></div><div id="comment-57572-info" class="comment-info"><span class="comment-age">(23 Nov '16, 09:13)</span> PhoenixGrad</div></div><span id="57577"></span><div id="comment-57577" class="comment"><div id="post-57577-score" class="comment-score"></div><div class="comment-text"><p>Bear in mind that both the window size itself and the window size scaling factor is chosen by each participant of the TCP session independently, depending on that participant's capabilities.</p><p>For the throughput, the window size on the receiving side is important: for PUT, the one of the remote side, for GET, the one of the local side.</p><p>You cannot affect window size at the remote side, but as you say you have issues with GET, your chances might be higher.</p><p>Window size scaling factor is a secondary thing; the primary thing is that the recipient can use a window so big that it needs to use a scaling factor to be able to express that window size using the 16-bit field available. So the best choice of a scaling factor is one which allows to express the maximum possible size of the window using a number between 32768 and 65535, as in this case, the finest possible granularity is achieved.</p></div><div id="comment-57577-info" class="comment-info"><span class="comment-age">(23 Nov '16, 11:01)</span> sindy</div></div><span id="57680"></span><div id="comment-57680" class="comment"><div id="post-57680-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Sindy, for the insights. Since setting the window size with the iPerf flag does not seem to have any effect, my guess is that the OS (Windows 2012) could be limiting the window size and/or scaling factor. Is there any way to conclusively determine that?</p></div><div id="comment-57680-info" class="comment-info"><span class="comment-age">(28 Nov '16, 06:21)</span> PhoenixGrad</div></div><span id="57682"></span><div id="comment-57682" class="comment"><div id="post-57682-score" class="comment-score"></div><div class="comment-text"><p>According to <a href="https://kb.wisc.edu/uwsysnet/page.php?id=41705">this link</a>, there seems to be no direct link between what window size you ask the iperf to use and what window the OS kernel actually uses. So you can replicate the tests done there, i.e. to observe a difference in measured throughput and see no difference in the maximum window size actually indicated in TCP, and you should see the window to shrink in TCP more often when a smaller "iperf window" is set. The TCP window reacts to behaviour of the receiving application - if the size of the receive buffer is fixed and the application doesn't pick up the data from the buffer, the window size must decrease.</p></div><div id="comment-57682-info" class="comment-info"><span class="comment-age">(28 Nov '16, 07:36)</span> sindy</div></div></div><div id="comment-tools-57569" class="comment-tools"></div><div class="clear"></div><div id="comment-57569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57580"></span>

<div id="answer-container-57580" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57580-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you have a bottle neck in the path. If your Window Size is bigger more data can be send at once and might fill the bottleneck. <a href="http://smallvoid.com/article/tcpip-rwin-size.html">http://smallvoid.com/article/tcpip-rwin-size.html</a></p><p>But if you send data you got a full window event - not a zero window. And if you receive data you deal with retransmissions and packet loss.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '16, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '16, 12:57</p></div></div><div id="comments-container-57580" class="comments-container"><span id="57678"></span><div id="comment-57678" class="comment"><div id="post-57678-score" class="comment-score"></div><div class="comment-text"><p>Although I agree with your conclusion that there is a bottleneck in the path, I don't know how to identify it. One of the mysteries about this particular issue is that when doing a "send" we consistently get two to four times the throughput of a "receive."</p></div><div id="comment-57678-info" class="comment-info"><span class="comment-age">(28 Nov '16, 06:10)</span> PhoenixGrad</div></div><span id="57679"></span><div id="comment-57679" class="comment"><div id="post-57679-score" class="comment-score"></div><div class="comment-text"><p>Maybe it is because the sender in the case of "receive" is able to send data much faster then in the other case. Easily said maybe it is because the sender in the case of receive has 10Gbit/s interfaces?</p></div><div id="comment-57679-info" class="comment-info"><span class="comment-age">(28 Nov '16, 06:20)</span> Christian_R</div></div></div><div id="comment-tools-57580" class="comment-tools"></div><div class="clear"></div><div id="comment-57580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57596"></span>

<div id="answer-container-57596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57596-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I see that the 10.x.x.x system has a IP TTL of 64 and the 192.168.x.x system seems to have an IP TTL of 128 (and is passing 10 routing hops). From this I assume that the 10.x.x.x is a linux or osx host and that the 192.168.x.x is a Windows host. Is that correct?</p><p>In the TCP streamgraph (tcptrace) of tcp.stream 7 I see that the 192.168.x.x host is throttling it's bandwidth. I assume this is done by keeping a small congestion window because of the packet loss. CAn you try a Linux-to-Linux iPerf in the same locations and see what the throughput is? What should be the bandwidth between those two nodes (in each direction) by the way?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '16, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57596" class="comments-container"><span id="57676"></span><div id="comment-57676" class="comment"><div id="post-57676-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the analysis and response. For this particular capture, both servers were Windows hosts; 10.92.x.x is Windows 2012 and 192.168.x.x is Windows 2008. I will set up a Linux to Linux iPerf test in the same locations and let you know the results.</p></div><div id="comment-57676-info" class="comment-info"><span class="comment-age">(28 Nov '16, 06:06)</span> PhoenixGrad</div></div></div><div id="comment-tools-57596" class="comment-tools"></div><div class="clear"></div><div id="comment-57596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

