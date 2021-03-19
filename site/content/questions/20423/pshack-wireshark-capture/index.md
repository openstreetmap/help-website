+++
type = "question"
title = "[PSH,ACK] wireshark capture"
description = '''I am capturing a https traffic from a PC to the web application and I am seeing an ACK follow by a PSH,ACK from the source to destination and vice versa: PC [ACK] -&amp;gt; WebApp PC [PSH,ACK] -&amp;gt; WebApp WebApp [ACK] -&amp;gt; PC WebApp [PSH,ACK] -&amp;gt; PC What does it mean? Thanks'''
date = "2013-04-15T09:04:00Z"
lastmod = "2013-04-15T15:05:00Z"
weight = 20423
keywords = [ "psh" ]
aliases = [ "/questions/20423" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[PSH,ACK\] wireshark capture](/questions/20423/pshack-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20423-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am capturing a https traffic from a PC to the web application and I am seeing an ACK follow by a PSH,ACK from the source to destination and vice versa:</p><p>PC [ACK] -&gt; WebApp PC [PSH,ACK] -&gt; WebApp WebApp [ACK] -&gt; PC WebApp [PSH,ACK] -&gt; PC</p><p>What does it mean? Thanks</p></div><div id="question-tags" class="tags-container tags">psh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '13, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/4bf9a4681570406f873b404a912f2a7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="character9&#39;s gravatar image" /><p>character9<br />
<span class="score" title="16 reputation points">16</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="character9 has no accepted answers">0%</span></p></div></div><div id="comments-container-20423" class="comments-container"></div><div id="comment-tools-20423" class="comment-tools"></div><div class="clear"></div><div id="comment-20423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20437"></span>

<div id="answer-container-20437" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20437-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>ACK means that the machine sending the packet with ACK is acknowledging data that it had received from the other machine. In TCP, once the connection is established, <em>all</em> packets sent by either side will contain an ACK, even if it's just re-acknowledging data that it's already acknowledged.</p><p>PSH is an indication by the sender that, if the receiving machine's TCP implementation has not yet provided the data it's received to the code that's reading the data (program, or library used by a program), it should do so at that point. To quote <a href="http://tools.ietf.org/html/rfc793">RFC 793</a>, the official specification for TCP:</p><p>The data that flows on a connection may be thought of as a stream of octets. The sending user indicates in each SEND call whether the data in that call (and any preceeding calls) should be immediately pushed through to the receiving user by the setting of the PUSH flag.</p><p>A sending TCP is allowed to collect data from the sending user and to send that data in segments at its own convenience, until the push function is signaled, then it must send all unsent data. When a receiving TCP sees the PUSH flag, it must not wait for more data from the sending TCP before passing the data to the receiving process.</p><p>There is no necessary relationship between push functions and segment boundaries. The data in any particular segment may be the result of a single SEND call, in whole or part, or of multiple SEND calls.</p><p>The purpose of push function and the PUSH flag is to push data through from the sending user to the receiving user. It does not provide a record service.</p><p>There is a coupling between the push function and the use of buffers of data that cross the TCP/user interface. Each time a PUSH flag is associated with data placed into the receiving user's buffer, the buffer is returned to the user for processing even if the buffer is not filled. If data arrives that fills the user's buffer before a PUSH is seen, the data is passed to the user in buffer size units.</p><p>There is no special significance to PSH and ACK both being set in the conversation; PSH being set has some significance, and, once the connection is established, ACK being set has very little significance.</p><p>RST, by itself, means that the sender of the RST believes an error occurred and that the connection should be "reset". It should be sent if, for example, a packet arrives on a connection that is "apparently not intended for the current connection", to quote RFC 793. So if the connection was closed, but a packet arrives for it anyway, that should provoke an RST.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20437" class="comments-container"></div><div id="comment-tools-20437" class="comment-tools"></div><div class="clear"></div><div id="comment-20437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20424"></span>

<div id="answer-container-20424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20424-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is basic TCP communications flow. The ACK indicates that a host is acknowledging having received some data, and the PSH,ACK indicates the host is acknowledging receipt of some previous data and also transmitting some more data.</p><p>Google will let you search for more info about basic TCP communication.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-20424" class="comments-container"><span id="20430"></span><div id="comment-20430" class="comment"><div id="post-20430-score" class="comment-score"></div><div class="comment-text"><p>grahamb, How about [RST,ACK]? Does it mean that the connection was disconnected? Thx</p></div><div id="comment-20430-info" class="comment-info"><span class="comment-age">(15 Apr '13, 10:31)</span> character9</div></div></div><div id="comment-tools-20424" class="comment-tools"></div><div class="clear"></div><div id="comment-20424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

