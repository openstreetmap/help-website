+++
type = "question"
title = "Server sending RST Message"
description = '''I am developing a server, and client messages are sent through a handset. Server and handset are connected through Wifi.  Client sends a HTTP Post message to server, and server is supposed to reply with a 200 ok. It works in most systems, but in some systems, after the server receives the POST Messa...'''
date = "2013-09-30T06:46:00Z"
lastmod = "2013-10-01T01:53:00Z"
weight = 25374
keywords = [ "ack", "brokentcp", "tcp", "rst" ]
aliases = [ "/questions/25374" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Server sending RST Message](/questions/25374/server-sending-rst-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25374-score" class="post-score" title="current number of votes">1</div><span id="post-25374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing a server, and client messages are sent through a handset. Server and handset are connected through Wifi.</p><p>Client sends a HTTP Post message to server, and server is supposed to reply with a 200 ok. It works in most systems, but in some systems, after the server receives the POST Message, it replies with a TCP RST.</p><p>Server IP is: 192.168.1.2 and Client IP is : 192.168.1.9. This is the flow when it does not work.</p><pre><code>|Time     | 192.168.1.9                           |
|         |                   | 192.168.1.2       |                   
|103.313276|         49988 &gt; 5901 [SYN]            |TCP: 49988 &gt; 5901 [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=306973 TSecr=0 WS=64
|         |(49988)  ------------------&gt;  (5901)   |
|103.313469|         5901 &gt; 49988 [SYN,            |TCP: 5901 &gt; 49988 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=8 TSval=0 TSecr=0 SACK_PERM=1
|         |(49988)  &lt;------------------  (5901)   |
|106.281619|         5901 &gt; 49988 [SYN,            |TCP: 5901 &gt; 49988 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=8 TSval=0 TSecr=0 SACK_PERM=1
|         |(49988)  &lt;------------------  (5901)   |
|112.316765|         5901 &gt; 49988 [SYN,            |TCP: 5901 &gt; 49988 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=8 TSval=0 TSecr=0 SACK_PERM=1
|         |(49988)  &lt;------------------  (5901)   |
|124.381196|         POST 192.168.1.2:59           |HTTP: POST 192.168.1.2:5901/ftcontentserver.rcs.mnc.mcc.pub.3gppnetwork.org HTTP/1.1 
|         |(49988)  ------------------&gt;  (5901)   |
|124.381300|         5901 &gt; 49988 [RST]            |TCP: 5901 &gt; 49988 [RST] Seq=1 Win=0 Len=0
|         |(49988)  &lt;------------------  (5901)   |</code></pre><p>This is the case where it works:</p><pre><code>|Time     | 192.168.1.3                           | 192.168.1.2                           |
|         |                   | 192.168.1.9       |                   
|117.828732|         42956 &gt; 5901 [SYN]            |                   |TCP: 42956 &gt; 5901 [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=2994458 TSecr=0 WS=64
|         |(42956)  ------------------&gt;  (5901)   |                   |
|117.828828|         5901 &gt; 42956 [SYN,            |                   |TCP: 5901 &gt; 42956 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=8 TSval=0 TSecr=0 SACK_PERM=1
|         |(42956)  &lt;------------------  (5901)   |                   |
|117.930471|         42956 &gt; 5901 [ACK]            |                   |TCP: 42956 &gt; 5901 [ACK] Seq=1 Ack=1 Win=14656 Len=0 TSval=2994490 TSecr=0
|         |(42956)  ------------------&gt;  (5901)   |                   |
|117.930932|         [TCP Window Update]           |                   |TCP: [TCP Window Update] 5901 &gt; 42956 [ACK] Seq=1 Ack=1 Win=262800 Len=0 TSval=75822 TSecr=2994490
|         |(42956)  &lt;------------------  (5901)   |                   |
|117.941444|         POST 192.168.1.9:59           |                   |HTTP: POST 192.168.1.9:5901/ftcontentserver.rcs.mnc.mcc.pub.3gppnetwork.org HTTP/1.1 
|         |(42956)  ------------------&gt;  (5901)   |                   |
|117.964006|         HTTP/1.1 204 No Con           |                   |HTTP: HTTP/1.1 204 No Content 
|         |(42956)  &lt;------------------  (5901)   |                   |</code></pre><p>This is the error I get in the first case: Expert Info (Warn/Protocol): Acknowledgment number: Broken TCP. The acknowledge field is nonzero while the ACK flag is not set</p><p>Can someone suggest what could be possibly going wrong?</p><p><strong>UPDATE</strong> Here is the wireshark dump</p><pre><code>No.     Time        Source                Destination           Protocol Length Info
      1 0.000000    192.168.1.9           192.168.1.2           TCP      74     49988 &gt; 5901 [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=306973 TSecr=0 WS=64

Frame 1: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: Lge_4c:96:28 (5c:17:d3:4c:96:28), Dst: IntelCor_d4:8d:40 (00:23:14:d4:8d:40)
Internet Protocol Version 4, Src: 192.168.1.9 (192.168.1.9), Dst: 192.168.1.2 (192.168.1.2)
Transmission Control Protocol, Src Port: 49988 (49988), Dst Port: 5901 (5901), Seq: 0, Len: 0

No.     Time        Source                Destination           Protocol Length Info
      2 0.000193    192.168.1.2           192.168.1.9           TCP      78     5901 &gt; 49988 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=8 TSval=0 TSecr=0 SACK_PERM=1

Frame 2: 78 bytes on wire (624 bits), 78 bytes captured (624 bits)
Ethernet II, Src: IntelCor_d4:8d:40 (00:23:14:d4:8d:40), Dst: Lge_4c:96:28 (5c:17:d3:4c:96:28)
Internet Protocol Version 4, Src: 192.168.1.2 (192.168.1.2), Dst: 192.168.1.9 (192.168.1.9)
Transmission Control Protocol, Src Port: 5901 (5901), Dst Port: 49988 (49988), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
      3 2.968343    192.168.1.2           192.168.1.9           TCP      78     5901 &gt; 49988 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=8 TSval=0 TSecr=0 SACK_PERM=1

Frame 3: 78 bytes on wire (624 bits), 78 bytes captured (624 bits)
Ethernet II, Src: IntelCor_d4:8d:40 (00:23:14:d4:8d:40), Dst: Lge_4c:96:28 (5c:17:d3:4c:96:28)
Internet Protocol Version 4, Src: 192.168.1.2 (192.168.1.2), Dst: 192.168.1.9 (192.168.1.9)
Transmission Control Protocol, Src Port: 5901 (5901), Dst Port: 49988 (49988), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
      4 9.003489    192.168.1.2           192.168.1.9           TCP      78     5901 &gt; 49988 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460 WS=8 TSval=0 TSecr=0 SACK_PERM=1

Frame 4: 78 bytes on wire (624 bits), 78 bytes captured (624 bits)
Ethernet II, Src: IntelCor_d4:8d:40 (00:23:14:d4:8d:40), Dst: Lge_4c:96:28 (5c:17:d3:4c:96:28)
Internet Protocol Version 4, Src: 192.168.1.2 (192.168.1.2), Dst: 192.168.1.9 (192.168.1.9)
Transmission Control Protocol, Src Port: 5901 (5901), Dst Port: 49988 (49988), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
      5 21.067920   192.168.1.9           192.168.1.2           HTTP     148    POST 192.168.1.2:5901/ftcontentserver.rcs.mnc.mcc.pub.3gppnetwork.org HTTP/1.1

Frame 5: 148 bytes on wire (1184 bits), 148 bytes captured (1184 bits)
Ethernet II, Src: Lge_4c:96:28 (5c:17:d3:4c:96:28), Dst: IntelCor_d4:8d:40 (00:23:14:d4:8d:40)
Internet Protocol Version 4, Src: 192.168.1.9 (192.168.1.9), Dst: 192.168.1.2 (192.168.1.2)
Transmission Control Protocol, Src Port: 49988 (49988), Dst Port: 5901 (5901), Seq: 1, Ack: 1, Len: 82
Hypertext Transfer Protocol

No.     Time        Source                Destination           Protocol Length Info
      6 21.068024   192.168.1.2           192.168.1.9           TCP      54     5901 &gt; 49988 [RST] Seq=1 Win=0 Len=0

Frame 6: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: IntelCor_d4:8d:40 (00:23:14:d4:8d:40), Dst: Lge_4c:96:28 (5c:17:d3:4c:96:28)
Internet Protocol Version 4, Src: 192.168.1.2 (192.168.1.2), Dst: 192.168.1.9 (192.168.1.9)
Transmission Control Protocol, Src Port: 5901 (5901), Dst Port: 49988 (49988), Seq: 1, Len: 0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-brokentcp" rel="tag" title="see questions tagged &#39;brokentcp&#39;">brokentcp</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '13, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/2429f8b6661800a7b2aa8e21cc8292d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="networker&#39;s gravatar image" /><p><span>networker</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="networker has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '13, 20:29</strong> </span></p></div></div><div id="comments-container-25374" class="comments-container"></div><div id="comment-tools-25374" class="comment-tools"></div><div class="clear"></div><div id="comment-25374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25377"></span>

<div id="answer-container-25377" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25377-score" class="post-score" title="current number of votes">1</div><span id="post-25377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Probably the server does not like the POST request. There is a clear difference</p><p><strong>BAD</strong> - Client: <strong>192.168.1.9</strong></p><blockquote><p>POST 192.168.1.2:59 |HTTP: POST <strong>192.168.1.2</strong>:5901/ftcontentserver.rcs.mnc.mcc.pub.3gppnetwork.org HTTP/1.1</p></blockquote><p><strong>GOOD:</strong> - Client: <strong>192.168.1.3</strong></p><blockquote><p>POST 192.168.1.9:59 |HTTP: POST <strong>192.168.1.9</strong>:5901/ftcontentserver.rcs.mnc.mcc.pub.3gppnetwork.org HTTP/1.1</p></blockquote><p>How comes, the POST request in the <strong>GOOD</strong> case contains the IP address of the client in the <strong>BAD</strong> case (192.168.1.9) and not the server (192.168.1.2)?</p><p>Is this intended or part of the problem?</p><p><strong>++ UPDATE ++</strong></p><p>O.K. with a little reformatting of the text, one can see that there are 3 SYN,ACK from the server to the client, but no ACK from the client. And then 'all of a sudden' the client sends a POST request, although the connection is not yet established from the servers point of view. As a result, the server sends a RST.</p><p>Why the client behaves like that, or if the packet got lost on the way is hard to tell.</p><p>Can you please add some details about your environment.</p><ul><li>OS involved (client)</li><li>software involved (Browser)</li><li>where did you capture and how</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '13, 10:17</strong> </span></p></div></div><div id="comments-container-25377" class="comments-container"><span id="25394"></span><div id="comment-25394" class="comment"><div id="post-25394-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt Knochner</span> That is not the problem, The server was just running on a different IP when it ran correctly. I had restarted my system, so server took new IP.</p></div><div id="comment-25394-info" class="comment-info"><span class="comment-age">(30 Sep '13, 08:39)</span> <span class="comment-user userinfo">networker</span></div></div><span id="25399"></span><div id="comment-25399" class="comment"><div id="post-25399-score" class="comment-score">1</div><div class="comment-text"><p>well, then it is impossible to compare those two capture files, especially as you just printed the summaries.</p><p>Please repeat your test <strong>with the same server IP address</strong> and then post both capture files somewhere.</p><p>I still believe the server does not like the POST request for some reason. Without a chance to look at the data, I cannot give any meaningful advice.</p></div><div id="comment-25399-info" class="comment-info"><span class="comment-age">(30 Sep '13, 10:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="25402"></span><div id="comment-25402" class="comment"><div id="post-25402-score" class="comment-score"></div><div class="comment-text"><p>see the <strong>UPDATE</strong> in my answer.</p></div><div id="comment-25402-info" class="comment-info"><span class="comment-age">(30 Sep '13, 10:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="25403"></span><div id="comment-25403" class="comment"><div id="post-25403-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Kurt Knochner</span> : OS of server is windows XP (coded in C), Client is android phone. The ere is a client application, which sends HTTP message to a HTTP server. I have taken logs of the Server through wireshark</p></div><div id="comment-25403-info" class="comment-info"><span class="comment-age">(30 Sep '13, 10:20)</span> <span class="comment-user userinfo">networker</span></div></div><span id="25404"></span><div id="comment-25404" class="comment"><div id="post-25404-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt Knochner</span> : Client sends ACK through the POST Message( this I noticed when I expand the message in wireshark). But in the case it works, it is a distinct ACK as it can be seen</p></div><div id="comment-25404-info" class="comment-info"><span class="comment-age">(30 Sep '13, 10:21)</span> <span class="comment-user userinfo">networker</span></div></div><span id="25419"></span><div id="comment-25419" class="comment not_top_scorer"><div id="post-25419-score" class="comment-score"></div><div class="comment-text"><blockquote><p>OS of server is windows XP (coded in C), Client is android phone.</p></blockquote><p>O.K. on the android phone, I guess you are simply using the browser or your own app. In both cases it will use a system call (possibly connect()) to open the TCP connection and then the OS will handle to TCP 3-way handshake, so there should be no reason for the behavior shown above, especially if another device works just fine with the same browser or the same app.</p><p>After the SYN the client does not react for 11 seconds and I believe it does not receive the SYN-ACK.</p><p>How is the android device connected to the 'server'? I assume a wireless connection and possibly you are having a problem with packet loss there.</p><p>Why the server sends a RST after the POST of the client, depends on how your C application is structured. As <span>@SYN-bit</span> mentioned, the capture files might help to dig a bit deeper into this.</p></div><div id="comment-25419-info" class="comment-info"><span class="comment-age">(30 Sep '13, 14:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="25435"></span><div id="comment-25435" class="comment not_top_scorer"><div id="post-25435-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt Knochner</span> I have updated the question. I have shown the wireshark dump</p></div><div id="comment-25435-info" class="comment-info"><span class="comment-age">(30 Sep '13, 20:30)</span> <span class="comment-user userinfo">networker</span></div></div><span id="25443"></span><div id="comment-25443" class="comment not_top_scorer"><div id="post-25443-score" class="comment-score"></div><div class="comment-text"><p>Can you please post a full capture file somewhere (google drive/docs, dropbox, cloudshark)? It's hard to look at text formatted output, especially if that output does not contain everything.</p></div><div id="comment-25443-info" class="comment-info"><span class="comment-age">(01 Oct '13, 01:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25377" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-25377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25412"></span>

<div id="answer-container-25412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25412-score" class="post-score" title="current number of votes">0</div><span id="post-25412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK it is allowed to send data straight after the SYN, SYN/ACK, however, the sequence number need to be 1 higher than the initial sequence number in the SYN. Also the ACK needs to be one higher than the sequence number in the SYN/ACK. Can you confirm these values (or netter, post the two tracefiles on www.cloudshark.org for further inspection)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25412" class="comments-container"><span id="25434"></span><div id="comment-25434" class="comment"><div id="post-25434-score" class="comment-score"></div><div class="comment-text"><p><span>@SYN-bit</span> I have updated the question. I have shown the wireshark dump</p></div><div id="comment-25434-info" class="comment-info"><span class="comment-age">(30 Sep '13, 20:30)</span> <span class="comment-user userinfo">networker</span></div></div></div><div id="comment-tools-25412" class="comment-tools"></div><div class="clear"></div><div id="comment-25412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

