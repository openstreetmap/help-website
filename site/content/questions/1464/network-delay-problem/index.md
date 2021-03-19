+++
type = "question"
title = "Network Delay Problem"
description = '''We found the network delay about 20 seconds.  The result is like the below.   A packet(1510 Byte) was sent by 5 fragments(Number 47215, 49041, 50848, 52765, 52785)  The delay for each segment was 5 seconds.  For this test, i didn&#x27;t set &#x27;tcp window size&#x27; and &#x27;nagle option&#x27; on Window Server 2008 R2 64...'''
date = "2010-12-22T18:28:00Z"
lastmod = "2010-12-23T01:11:00Z"
weight = 1464
keywords = [ "delay" ]
aliases = [ "/questions/1464" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Network Delay Problem](/questions/1464/network-delay-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1464-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We found the network delay about 20 seconds.</p><p>The result is like the below.</p><p><img src="http://i54.tinypic.com/2r4k5nc.gif" alt="alt text" /></p><p>A packet(1510 Byte) was sent by 5 fragments(Number 47215, 49041, 50848, 52765, 52785) The delay for each segment was 5 seconds.</p><p>For this test, i didn't set 'tcp window size' and 'nagle option' on Window Server 2008 R2 64bit.</p><p>I have two questions. 1. TCP window size on screen shot as you see is under 256. Is this normal? 2. A long packet delay was found between segments. Is this normal?</p><p>Please give me your help for solving those problems.</p></div><div id="question-tags" class="tags-container tags">delay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '10, 18:28</strong></p><img src="https://secure.gravatar.com/avatar/a38d11defaf0ba2de308980321732b9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dalma&#39;s gravatar image" /><p>dalma<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dalma has no accepted answers">0%</span></p></img></div></div><div id="comments-container-1464" class="comments-container"><span id="1467"></span><div id="comment-1467" class="comment"><div id="post-1467-score" class="comment-score"></div><div class="comment-text"><p>I have resloved both of ip adresses(192.168.0.2, 192.168.0.4). Original address was different. However, both of them are in same network.</p><p>I have filtered Tcp keep-alive Packet and tcp keep-alive ack for the test above screen shot.</p><p>The below shows only port after filtering for the test.</p><p><img src="http://i52.tinypic.com/2ijqdf9.gif" alt="alt text" /></p><p>I am curious why the packet was received after over 20 seconds, TCP window size is so small on window.</p></div><div id="comment-1467-info" class="comment-info"><span class="comment-age">(22 Dec '10, 23:52)</span> dalma</div></div><span id="1473"></span><div id="comment-1473" class="comment"><div id="post-1473-score" class="comment-score"></div><div class="comment-text"><p>Dalma, 20 seconds is an eternity in network time. Consider that in one second, I can go across the world about three times. I can't see the post pics too well so it's hard for me to tell what's going on. But one thing to consider is that nothing in the network clocks at 5 second interval. So I have some questions. What apps is this, can you post a snippet of the trace (editcap it to just headers) so people can help you?</p></div><div id="comment-1473-info" class="comment-info"><span class="comment-age">(23 Dec '10, 16:49)</span> hansangb</div></div><span id="1695"></span><div id="comment-1695" class="comment"><div id="post-1695-score" class="comment-score"></div><div class="comment-text"><p>To hansangb, May I have your mail address? Because, it is difficult to upload the capture file. Plz, Help me.</p></div><div id="comment-1695-info" class="comment-info"><span class="comment-age">(10 Jan '11, 22:59)</span> dalma</div></div></div><div id="comment-tools-1464" class="comment-tools"></div><div class="clear"></div><div id="comment-1464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1465"></span>

<div id="answer-container-1465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1465-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's on the same subnet. There's some out of order stuff going on. So basically some frames are being destroyed between the source and destination. Is there a duplex mismatch somewhere? Is anything hard coded to full?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '10, 18:55</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></img></div></div><div id="comments-container-1465" class="comments-container"></div><div id="comment-tools-1465" class="comment-tools"></div><div class="clear"></div><div id="comment-1465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1468"></span>

<div id="answer-container-1468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1468-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Regarding the Window Size: I'd say it's normal, I see sizes like that a lot, and usually for Vista/2008 and up. These OSes use the TCP window scaling option (RFC 1323), which means that the specified window size is multiplied by a certain scale factor. Vista and 2008 often use a scale factor of 8, which means that the window size is multiplied by 2^8 (256). So for example if your window is 256 you need to calculate the scaled window, which is 256*256=65536.</p><p>Wireshark can calculate the scaled window size for you if you enabled it in the TCP settings ("relative sequence numbers and window scaling"). Since the scale factor is only agreed upon within the SYN-SYN/ACK packets of a connection you need to make sure you capture them, otherwise Wireshark doesn't know what the scale factor is and can only show the base value, which I guess is what happened in your trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '10, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1468" class="comments-container"></div><div id="comment-tools-1468" class="comment-tools"></div><div class="clear"></div><div id="comment-1468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

