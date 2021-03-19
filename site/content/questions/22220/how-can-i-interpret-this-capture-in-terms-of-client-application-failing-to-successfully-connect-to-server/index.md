+++
type = "question"
title = "How can I interpret this capture in terms of client application failing to successfully connect to server?"
description = '''Hi everyone. I&#x27;m an application administrator but my TCP knowledge is minimal. I have done some research trying to work this out on my own but feel like I&#x27;m going to need help to make any real progress.  So... here goes. I have one particular customer site from which nobody can successfully connect ...'''
date = "2013-06-21T06:15:00Z"
lastmod = "2013-06-21T09:56:00Z"
weight = 22220
keywords = [ "capture" ]
aliases = [ "/questions/22220" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I interpret this capture in terms of client application failing to successfully connect to server?](/questions/22220/how-can-i-interpret-this-capture-in-terms-of-client-application-failing-to-successfully-connect-to-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22220-score" class="post-score" title="current number of votes">0</div><span id="post-22220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone. I'm an application administrator but my TCP knowledge is minimal. I have done some research trying to work this out on my own but feel like I'm going to need help to make any real progress.<br />
</p><p>So... here goes. I have one particular customer site from which nobody can successfully connect to our server. They are able to telnet to the correct port. I have over 100 other users from various sites logged in daily who are all working fine. This leads me to believe that the app and networking on my side are ok. The customer is maintaining that there is no problem on their side. They have provided me with the capture below taken from their firewall (x is the client machine, y our server). Please let me know if there's any other information I can provide. And thanks!!</p><pre><code>  1 0.000000    x.x.x.x            y.y.y.y         TCP      66     56951 &gt; dnp [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
  2 0.048124    y.y.y.y         x.x.x.x            TCP      66     dnp &gt; 56951 [SYN, ACK] Seq=0 Ack=1 Win=64240 Len=0 MSS=1380 WS=1 SACK_PERM=1
  3 0.048459    x.x.x.x            y.y.y.y         TCP      54     56951 &gt; dnp [ACK] Seq=1 Ack=1 Win=131072 Len=0
  4 0.048841    x.x.x.x            y.y.y.y         TCP      218    56951 &gt; dnp [PSH, ACK] Seq=1 Ack=1 Win=131072 Len=164
  5 0.096858    y.y.y.y         x.x.x.x            TCP      582    dnp &gt; 56951 [PSH, ACK] Seq=1 Ack=165 Win=64076 Len=528
  6 0.348782    x.x.x.x            y.y.y.y         TCP      218    [TCP Retransmission] 56951 &gt; dnp [PSH, ACK] Seq=1 Ack=1 Win=131072 Len=164
  7 0.394633    y.y.y.y         x.x.x.x            TCP      54     [TCP Dup ACK 5#1] dnp &gt; 56951 [ACK] Seq=529 Ack=165 Win=64076 Len=0
  8 0.950533    x.x.x.x            y.y.y.y         TCP      218    [TCP Retransmission] 56951 &gt; dnp [PSH, ACK] Seq=1 Ack=1 Win=131072 Len=164
  9 0.962175    x.x.x.x            y.y.y.y         TCP      66     56952 &gt; dnp [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
 10 0.997604    y.y.y.y         x.x.x.x            TCP      54     [TCP Dup ACK 5#2] dnp &gt; 56951 [ACK] Seq=529 Ack=165 Win=64076 Len=0
 11 0.997818    x.x.x.x            y.y.y.y         TCP      54     56951 &gt; dnp [RST] Seq=165 Win=0 Len=0
 12 1.009475    y.y.y.y         x.x.x.x            TCP      66     dnp &gt; 56952 [SYN, ACK] Seq=0 Ack=1 Win=64240 Len=0 MSS=1380 WS=1 SACK_PERM=1
 13 1.009887    x.x.x.x            y.y.y.y         TCP      54     56952 &gt; dnp [ACK] Seq=1 Ack=1 Win=131072 Len=0
 14 1.010024    x.x.x.x            y.y.y.y         TCP      218    56952 &gt; dnp [PSH, ACK] Seq=1 Ack=1 Win=131072 Len=164
 15 1.059002    y.y.y.y         x.x.x.x            TCP      582    dnp &gt; 56952 [PSH, ACK] Seq=1 Ack=165 Win=64076 Len=528
 16 1.059155    x.x.x.x            y.y.y.y         TCP      54     56952 &gt; dnp [RST] Seq=165 Win=0 Len=0
 17 1.357846    x.x.x.x            y.y.y.y         TCP      66     56953 &gt; dnp [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
 18 1.405527    y.y.y.y         x.x.x.x            TCP      66     dnp &gt; 56953 [SYN, ACK] Seq=0 Ack=1 Win=64240 Len=0 MSS=1380 WS=1 SACK_PERM=1
 19 1.405893    x.x.x.x            y.y.y.y         TCP      54     56953 &gt; dnp [ACK] Seq=1 Ack=1 Win=131072 Len=0
 20 1.406046    x.x.x.x            y.y.y.y         TCP      430    56953 &gt; dnp [PSH, ACK] Seq=1 Ack=1 Win=131072 Len=376
 21 1.453000    y.y.y.y         x.x.x.x            TCP      378    dnp &gt; 56953 [PSH, ACK] Seq=1 Ack=377 Win=63864 Len=324
 22 1.453199    x.x.x.x            y.y.y.y         TCP      54     56953 &gt; dnp [RST] Seq=377 Win=0 Len=0
 23 1.453931    x.x.x.x            y.y.y.y         TCP      66     56954 &gt; dnp [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
 24 1.501033    y.y.y.y         x.x.x.x            TCP      66     dnp &gt; 56954 [SYN, ACK] Seq=0 Ack=1 Win=64240 Len=0 MSS=1380 WS=1 SACK_PERM=1
 25 1.501399    x.x.x.x            y.y.y.y         TCP      54     56954 &gt; dnp [ACK] Seq=1 Ack=1 Win=131072 Len=0
 26 1.501536    x.x.x.x            y.y.y.y         TCP      430    56954 &gt; dnp [PSH, ACK] Seq=1 Ack=1 Win=131072 Len=376
 27 1.549034    y.y.y.y         x.x.x.x            TCP      378    dnp &gt; 56954 [PSH, ACK] Seq=1 Ack=377 Win=63864 Len=324
 28 1.549141    x.x.x.x            y.y.y.y         TCP      54     56954 &gt; dnp [RST] Seq=377 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '13, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/be3b42cbadc428acf9766608b1ee61f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="colby&#39;s gravatar image" /><p><span>colby</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="colby has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-22220" class="comments-container"></div><div id="comment-tools-22220" class="comment-tools"></div><div class="clear"></div><div id="comment-22220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22226"></span>

<div id="answer-container-22226" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22226-score" class="post-score" title="current number of votes">1</div><span id="post-22226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For the first connection on port 56951 the client sends a request (frame 4), the server acks and responds with data (5) and the client doesn't seem to receive the response as it retransmits the request (6), the server acks again (7), the client retransmits the request again (8) then the client appears to give up on that connection and opens another to port 56952 (9), the server again acks the original request (10) and then the client resets that original connection (11) without actually closing it (no FIN).</p><p>For the 3 subsequent connection attempts the client sends a reset as soon as the server responds.</p><p>Something odd is going on on the client side, the server is behaving correctly. Even if the application data response was incorrect, the client should at least ack it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22226" class="comments-container"></div><div id="comment-tools-22226" class="comment-tools"></div><div class="clear"></div><div id="comment-22226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

