+++
type = "question"
title = "why the client resend whole message to server?"
description = '''client:any browser,PC(windows os) server:firewall-&amp;gt;F5-&amp;gt;IHS-&amp;gt;WAS In my case,a http request will be hanged by WAS for 10 min.Somtimes,When WAS hang the request for about 5 min,client(PC) will resend the whole message to server.I&#x27;ve used httpwatch and fiddler to see the resent message,but can&#x27;...'''
date = "2012-09-13T23:48:00Z"
lastmod = "2012-09-14T00:53:00Z"
weight = 14257
keywords = [ "rst", "ack", "resend" ]
aliases = [ "/questions/14257" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why the client resend whole message to server?](/questions/14257/why-the-client-resend-whole-message-to-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14257-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>client:any browser,PC(windows os) server:firewall-&gt;F5-&gt;IHS-&gt;WAS In my case,a http request will be hanged by WAS for 10 min.Somtimes,When WAS hang the request for about 5 min,client(PC) will resend the whole message to server.I've used httpwatch and fiddler to see the resent message,but can't catch any resent info.And wireshark can catch the resent info. The resent time decided by the F5's idle-time settings.When the idle-time changed,the resent interval time changed.They(F5) told me the idle-time is to break off the connection between the client and the server. The info with resent message is:</p><pre><code>No.  Time        Source          Destination     Protocol Info 
  75 6.247420    36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
  76 6.247540    36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
  77 6.250121    60.208.131.87   36.0.135.56     TCP      8009 &gt; 54398 [ACK] Seq=1 Ack=1628 Win=16506 Len=0
5223 200.517228  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54388 [RST, ACK] Seq=1 Ack=1 Win=16333 Len=0
5224 200.517230  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54389 [RST, ACK] Seq=1 Ack=1 Win=15368 Len=0
5225 200.517230  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54390 [RST, ACK] Seq=1 Ack=1 Win=15487 Len=0
5226 200.517336  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54393 [RST, ACK] Seq=1 Ack=1 Win=14503 Len=0
5227 200.517337  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54394 [RST, ACK] Seq=1 Ack=1 Win=14347 Len=0
5228 200.517337  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54395 [RST, ACK] Seq=1 Ack=1 Win=14208 Len=0
5229 200.517337  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54396 [RST, ACK] Seq=1 Ack=1 Win=14455 Len=0
7044 249.113874  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54398 [RST, ACK] Seq=1 Ack=1628 Win=16506 Len=0
7078 249.119338  36.0.135.56     60.208.131.87   TCP      54530 &gt; 8009 [SYN] Seq=0 Win=8192 [TCP CHECKSUM INCORRECT] Len=0 MSS=1460 WS=2
7079 249.123288  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54530 [SYN, ACK] Seq=0 Ack=1 Win=4380 Len=0 MSS=1460 WS=0
7080 249.123401  36.0.135.56     60.208.131.87   TCP      54530 &gt; 8009 [ACK] Seq=1 Ack=1 Win=65700 [TCP CHECKSUM INCORRECT] Len=0
7081 249.123912  36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
7082 249.124121  36.0.135.56     60.208.131.87   TCP      54531 &gt; 8009 [SYN] Seq=0 Win=8192 [TCP CHECKSUM INCORRECT] Len=0 MSS=1460 WS=2
7083 249.126055  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54531 [SYN, ACK] Seq=0 Ack=1 Win=4380 Len=0 MSS=1460 WS=0
7084 249.126057  60.208.131.87   36.0.135.56     AJP13    AJP13 Error?
7085 249.126195  36.0.135.56     60.208.131.87   TCP      54531 &gt; 8009 [ACK] Seq=1 Ack=1 Win=65700 [TCP CHECKSUM INCORRECT] Len=0
7086 249.126865  36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
7087 249.127037  36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
7088 249.129194  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54530 [ACK] Seq=147 Ack=158 Win=4470 Len=0
7089 249.129195  60.208.131.87   36.0.135.56     AJP13    AJP13 Error?
7090 249.130538  36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
7094 249.134976  60.208.131.87   36.0.135.56     TCP      8009 &gt; 54531 [ACK] Seq=147 Ack=158 Win=4470 Len=0
7096 249.134977  60.208.131.87   36.0.135.56     TCP      [TCP ACKed lost segment] 8009 &gt; 54531 [ACK] Seq=147 Ack=1785 Win=6164 Len=0
7108 249.155169  60.208.131.87   36.0.135.56     TCP      [TCP segment of a reassembled PDU]
7109 249.187292  36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
7110 249.187292  36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
7111 249.192339  60.208.131.87   36.0.135.56     TCP      [TCP segment of a reassembled PDU]
7112 249.192341  60.208.131.87   36.0.135.56     TCP      [TCP segment of a reassembled PDU]
7115 249.208616  36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
7116 249.209016  36.0.135.56     60.208.131.87   AJP13    AJP13 Error?[Unreassembled Packet [incorrect TCP checksum]] 
7117 249.212176  60.208.131.87   36.0.135.56     TCP      [TCP segment of a reassembled PDU]
7118 249.212178  60.208.131.87   36.0.135.56     TCP      [TCP segment of a reassembled PDU]
7134 249.414204  36.0.135.56     60.208.131.87   TCP      54530 &gt; 8009 [ACK] Seq=1421 Ack=538 Win=65160 [TCP CHECKSUM INCORRECT] Len=0
7135 249.414210  36.0.135.56     60.208.131.87   TCP      54531 &gt; 8009 [ACK] Seq=3050 Ack=1600 Win=65700 [TCP CHECKSUM INCORRECT] Len=0</code></pre><p>In this case,F5's idle-time was 240s.The interval time between 77 and 7044 was about 240s. The top three line happened when the browser post normal.From 7044,it happend when the client resent. In my case,the WAS must hang every normal request,but the resent message happened sometimes. I found that,we can see a message like this just when the client resent: 7044 249.113874 60.208.131.87 36.0.135.56 TCP 8009 &gt; 54398 [RST, ACK] Seq=1 Ack=1628 Win=16506 Len=0</p><p>My question:Why the client resent the whole message(included the same form data) to server?</p><p>ps:I apologize for my pool English.:)</p></div><div id="question-tags" class="tags-container tags">rst ack resend</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '12, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/ca1f5da924f2a1f21cf352ab0613be22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msworder&#39;s gravatar image" /><p>msworder<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msworder has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Sep '12, 00:45</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-14257" class="comments-container"></div><div id="comment-tools-14257" class="comment-tools"></div><div class="clear"></div><div id="comment-14257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14260"></span>

<div id="answer-container-14260" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14260-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume the trace was taken on the client PC.</p><p>As the client gets no answer from the server for a long time, the F5 actively closes the connection due to it's idle timer in its tcp profile. This is why you see the "RST" packets. This closes the tcp connection on the client and the client decides to try a again by opening new connections to the server.</p><p>The interesting part would be to look at the server side of the F5 and check why there is no response to the requests. Does the WAS get the request? Does it send a response that does not arrive at the F5 or does the F5 not forward the response.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14260" class="comments-container"><span id="14261"></span><div id="comment-14261" class="comment"><div id="post-14261-score" class="comment-score"></div><div class="comment-text"><p>There are some problem in our applications.Sometimes it would take more than 5 min to deal with some <a href="http://request.So">request.So</a> F5 would get no response from WAS until our app finished it's work. If client PC took the trace,why it wasn't happened every time? We made our app sleep for 10 min with no response to F5 when it get a request,and used some PCs with diffrent windows OS and diffrent browsers to test.For each test,we sent a request after a 5 min waiting nothing was done.We found that the resent happened sometimes.</p></div><div id="comment-14261-info" class="comment-info"><span class="comment-age">(14 Sep '12, 01:53)</span> msworder</div></div><span id="14263"></span><div id="comment-14263" class="comment"><div id="post-14263-score" class="comment-score"></div><div class="comment-text"><p>Sounds to me like this needs some thorough investigation with traces being made at different points in the chain. You then need to compare the results for the different scenarios that you describe (when clients do resend the request, when clients don't resend the request, when the WAS server does respond).</p></div><div id="comment-14263-info" class="comment-info"><span class="comment-age">(14 Sep '12, 03:13)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-14260" class="comment-tools"></div><div class="clear"></div><div id="comment-14260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

