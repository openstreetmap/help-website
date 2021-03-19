+++
type = "question"
title = "TCP window keeps decreasing on PSH,ACKs"
description = '''Hi, Quick Description: I am observing a client/server application that maintains a persistence TCP socket. When the TCP session is established, the server side sets a 64k receive window and the client sets an 8k receive window. During times of no &#x27;big&#x27; application traffic the application appears to ...'''
date = "2014-03-21T06:59:00Z"
lastmod = "2014-03-21T10:12:00Z"
weight = 31048
keywords = [ "psh", "window", "tcp", "size" ]
aliases = [ "/questions/31048" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP window keeps decreasing on PSH,ACKs](/questions/31048/tcp-window-keeps-decreasing-on-pshacks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31048-score" class="post-score" title="current number of votes">0</div><span id="post-31048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p><strong>Quick Description:</strong><br />
I am observing a client/server application that maintains a persistence TCP socket. When the TCP session is established, the server side sets a 64k receive window and the client sets an 8k receive window. During times of no 'big' application traffic the application appears to maintain persistence within the application by using an 11byte payload; 11bytes PSH,ACK to server, then 11bytes PSH,ACK back to client, finally zero byte ack to server. Then, this process happens again a minute later.</p><p><strong>Question:</strong><br />
Why would the TCP window continue to decrease by the 11 bytes when the 11byte PSH,ACK is received? My understanding is that a PSH tells the receiver "don't buffer this". Even if that meant "only buffer this until you send an ACK", I still see the window continuously dropping.</p><p><strong>Example:</strong><br />
</p><pre><code>TCP 65  35112 &gt; 3333 [PSH, ACK] Seq=56 Ack=56 Win=7225 Len=11
TCP 65  3333 &gt; 35112 [PSH, ACK] Seq=56 Ack=67 Win=65008 Len=11
TCP 54  35112 &gt; 3333 [ACK] Seq=67 Ack=67 Win=7214 Len=0
TCP 65  35112 &gt; 3333 [PSH, ACK] Seq=67 Ack=67 Win=7214 Len=11
TCP 65  3333 &gt; 35112 [PSH, ACK] Seq=67 Ack=78 Win=64997 Len=11
TCP 54  35112 &gt; 3333 [ACK] Seq=78 Ack=78 Win=7203 Len=0</code></pre><p><strong>(this happens for a ~30 minutes until the buffer returns to max and starts dropping again).</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-psh" rel="tag" title="see questions tagged &#39;psh&#39;">psh</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '14, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/038dfc9228d5b4d00e246f8bedbf0e5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blablabla&#39;s gravatar image" /><p><span>blablabla</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blablabla has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Mar '14, 07:36</strong> </span></p></div></div><div id="comments-container-31048" class="comments-container"></div><div id="comment-tools-31048" class="comment-tools"></div><div class="clear"></div><div id="comment-31048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31060"></span>

<div id="answer-container-31060" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31060-score" class="post-score" title="current number of votes">0</div><span id="post-31060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>PSH does not mean "don't buffer this", it means "don't buffer this and wait for more before sending the buffer content to the applicatiuon layer". The TCP needs to put the incoming bytes somewhere before passing it on to the application, but when the push flag is set the stack is not allowed to wait for more data before it passes it on. So I guess it is normal that you have a 11 byte drop in the Window size. It should go up again in the next ACK though, but maybe the stack doesn't see the need as long as it has a lot of window bytes left for buffering more. It may be saying "I'll raise my window later, why bother now" :-)</p><p>The important thing is</p><p>a) the incoming bytes needs to be buffered to be able to pass them on; there is no direct pipeline that bypasses buffering (at least as far as I know)</p><p>b) Window size is not a problem unless it slows down the receiving of more incoming data, which in your case doesn't seem to be the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '14, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Mar '14, 10:13</strong> </span></p></div></div><div id="comments-container-31060" class="comments-container"></div><div id="comment-tools-31060" class="comment-tools"></div><div class="clear"></div><div id="comment-31060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

