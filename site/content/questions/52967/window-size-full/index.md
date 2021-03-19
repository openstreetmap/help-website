+++
type = "question"
title = "Window Size Full"
description = '''Hello, I am trying to undestand TCP receive window. I am getting a lot of tcp window full messages at client side but not tcp window zero messages when I send data from client to the server using iperf. The problem is the tcp receive window of server shows 64240 bytes in the previous frame. Can anyo...'''
date = "2016-05-26T10:10:00Z"
lastmod = "2016-05-26T14:22:00Z"
weight = 52967
keywords = [ "tcpwindowfull", "tcpwindowsize" ]
aliases = [ "/questions/52967" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Window Size Full](/questions/52967/window-size-full)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52967-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to undestand TCP receive window. I am getting a lot of tcp window full messages at client side but not tcp window zero messages when I send data from client to the server using iperf. The problem is the tcp receive window of server shows 64240 bytes in the previous frame. Can anyone help me figure out how does the receive window size drastically decrease to zero and also to measure the rate at which the receiver buffer processes the data I have added captures below:</p><p>link:<a href="https://www.dropbox.com/s/r6fbukaik0j59dj/iperf.pcapng?dl=0">Capturefile</a></p><p>PS: I HAVE DISABLED WINDOW SCALING<br />
</p></div><div id="question-tags" class="tags-container tags">tcpwindowfull tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '16, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/72d6fe43f92f9994421ed328054e242d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gravatar&#39;s gravatar image" /><p>gravatar<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gravatar has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-52967" class="comments-container"></div><div id="comment-tools-52967" class="comment-tools"></div><div class="clear"></div><div id="comment-52967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52970"></span>

<div id="answer-container-52970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52970-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The receive window value is only relevant in relation to what has been acked. So while your server window is 64k you have as many bytes in flight, meaning that the window is used by not-acknowleged data.</p><p>Simple example:</p><ol><li>server announces 64k window size</li><li>client sends 64k</li><li>server acknowledges packets worth 2k, and announces 64k window in the same packet</li></ol><p>this means that the window is only 2k, because 62k are still unacknowledged and are part of the 64k window. client sends 2k, and again the "window is full".</p><p>Also, "Window Full" is not the same as "Zero Window". Window Full means "bytes-in-flight equals advertised window size of receiver". Check the TCP layer for the bytes-in-flight value to see what I mean.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '16, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 May '16, 14:13</p></div></div><div id="comments-container-52970" class="comments-container"><span id="53017"></span><div id="comment-53017" class="comment"><div id="post-53017-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-53017-info" class="comment-info"><span class="comment-age">(27 May '16, 18:24)</span> gravatar</div></div></div><div id="comment-tools-52970" class="comment-tools"></div><div class="clear"></div><div id="comment-52970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52971"></span>

<div id="answer-container-52971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52971-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What I see in this capture is that the client is sending so much data that the number of bytes in flight (the unacknowledged bytes) reaches to reported window size (the receive window full) (frame 233). That's were the the client stops, waits until an ACK is received (frame 234), showing that the window has room again, which is immediately filled until it's full again (frame 236). Etc, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '16, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52971" class="comments-container"><span id="53018"></span><div id="comment-53018" class="comment"><div id="post-53018-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-53018-info" class="comment-info"><span class="comment-age">(27 May '16, 18:24)</span> gravatar</div></div></div><div id="comment-tools-52971" class="comment-tools"></div><div class="clear"></div><div id="comment-52971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

