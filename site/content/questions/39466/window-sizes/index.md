+++
type = "question"
title = "Window Sizes"
description = '''Im troubleshooting an issue where we are receiving slow transfer speeds when going to one server and not the other. i.e  Client A - Server A (UK) 1MBps Client A - Server B (Germany) 10MBps  The RTT is the same for both i.e around 60ms. Client A advertises his window in the SYN ACK as 40880 (i.e wind...'''
date = "2015-01-29T00:12:00Z"
lastmod = "2015-01-29T03:05:00Z"
weight = 39466
keywords = [ "tcpwindowsize" ]
aliases = [ "/questions/39466" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Window Sizes](/questions/39466/window-sizes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39466-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im troubleshooting an issue where we are receiving slow transfer speeds when going to one server and not the other. i.e</p><ul><li>Client A - Server A (UK) 1MBps</li><li>Client A - Server B (Germany) 10MBps</li></ul><p>The RTT is the same for both i.e around 60ms.</p><p>Client A advertises his window in the SYN ACK as 40880 (i.e window size 5840 * Window Scale of 7) However for the transfer for client A I see the window size go no higher then 191488 (??) Also can the window go higher then what is announced by the receiver ?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '15, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p>bart80<br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '15, 00:13</p></div></div><div id="comments-container-39466" class="comments-container"></div><div id="comment-tools-39466" class="comment-tools"></div><div class="clear"></div><div id="comment-39466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39472"></span>

<div id="answer-container-39472" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39472-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure your Client A has a Window of 40880 in the SYN ACK? I doubt it, and here's why:</p><p>1) while there is a scale factor of 7, it does not mean that you multiply the actual window size with 7. It means that you multiply the actual window size with 2^7, which is 128. That would be a scaled window of 747520.</p><p>2) the scaling does not apply to packets with SYN flags, because the connection setup isn't complete yet. What your SYN ACK basically says is "hey, my window size is 5840 right now. I would like to do window scaling with a scale factor of 7 for all further packets, if you know what that means". You can usually see that - as soon as both nodes tell each other that they know how window scaling works, and thus can use it - they reduce the actual window size value in the TCP header to a much smaller window and pull it up slowly while sending data.</p><p>Regarding the maximum window size you see - it's up to the stack to advertise a window that it can live with. Since the client sort of "guarantees" that it can receive and buffer that many bytes, it may have reasons for saving memory and not advertise crazy window sizes. Also, you rarely see stacks using the full maximum size for their scaled window (which is different from unscaled window sizes, which often stay very close to the maximum of 64k).</p><p>If your Client A keeps a certain scaled window maximum size it means either it doesn't have more resources to go higher (which is very uncommon), or it just thinks it doesn't <strong>need</strong> to go higher.</p><p>What you should do is find out if the window size is a problem by determining if the communication could go faster if the Client would just advertise an even bigger window. For that you could look for delays caused by full windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '15, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '15, 03:06</p></div></div><div id="comments-container-39472" class="comments-container"></div><div id="comment-tools-39472" class="comment-tools"></div><div class="clear"></div><div id="comment-39472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

