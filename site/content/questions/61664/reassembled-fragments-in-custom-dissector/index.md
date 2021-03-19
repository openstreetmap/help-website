+++
type = "question"
title = "Reassembled fragments in custom dissector"
description = '''hi, i have n number of packet and i have three different message. beginning message , continuation message and end message. when beginning message received i have to store the message and continuation of message alo be included and when it comes to end message i have to reassembled them. Packet 1 : ...'''
date = "2017-05-27T21:30:00Z"
lastmod = "2017-05-30T08:21:00Z"
weight = 61664
keywords = [ "reassembly", "reassembled", "dissector" ]
aliases = [ "/questions/61664" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Reassembled fragments in custom dissector](/questions/61664/reassembled-fragments-in-custom-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61664-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, i have n number of packet and i have three different message. beginning message , continuation message and end message. when beginning message received i have to store the message and continuation of message alo be included and when it comes to end message i have to reassembled them.</p><p>Packet 1 : fragmentation, beginning message(id=1)</p><p>Packet 2 : fragmentation, continuation message(id=1)</p><p>Packet 3 : fragmentation, beginning message(id=2)</p><p>Packet 4 : fragmentation, beginning message(id=3)</p><p>Packet 5 : fragmentation, continuation message(id=1)</p><p>Packet 6 : fragmentation, end message(id=1)</p><p>how can i reassemble these messages in my dissectors?</p></div><div id="question-tags" class="tags-container tags">reassembly reassembled dissector</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '17, 21:30</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p>ghader<br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '17, 08:22</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-61664" class="comments-container"><span id="61665"></span><div id="comment-61665" class="comment"><div id="post-61665-score" class="comment-score">1</div><div class="comment-text"><p>So how are those three types of message indicated? Is a non-fragmented message one that's marked as neither beginning, nor continuation, nor end? Or is it marked in some other way? What if a message has only two fragments - is one marked as beginning and the other marked as end?</p><p>And do the IDs indicate what message is fragmented, so that, with those 6 packets, only the message with an ID of 1 can be reassembled?</p></div><div id="comment-61665-info" class="comment-info"><span class="comment-age">(27 May '17, 22:17)</span> Guy Harris ♦♦</div></div><span id="61666"></span><div id="comment-61666" class="comment"><div id="post-61666-score" class="comment-score"></div><div class="comment-text"><p>in message packets, there is a flag(message type) that indicate type of message(b,c,e).some message has only two fragments - is one marked as beginning and the other marked as end.the IDs dont indicate what message is fragmented. there is a counter in each message that increase each time send a packet.</p><p>Packet 1 : fragmentation, beginning message(id=1),n=10</p><p>Packet 2 : fragmentation, continuation message(id=1),n=11</p><p>Packet 3 : fragmentation, beginning message(id=2),n=15</p><p>Packet 4 : fragmentation, beginning message(id=3),n=20</p><p>Packet 5 : fragmentation, continuation message(id=1),n=12</p><p>Packet 6 : fragmentation, end message(id=1),n=13</p></div><div id="comment-61666-info" class="comment-info"><span class="comment-age">(27 May '17, 22:55)</span> ghader</div></div><span id="61703"></span><div id="comment-61703" class="comment"><div id="post-61703-score" class="comment-score"></div><div class="comment-text"><blockquote><p>some message has only two fragments</p></blockquote><p>So <em>all</em> messages are fragmented - there's no message type that's "it's all here, no fragments"? Or is that a fourth message type?</p><p>In your example, what indicates which message packets 2 and 5 are continuations of, and what message packet 6 is the end of?</p></div><div id="comment-61703-info" class="comment-info"><span class="comment-age">(30 May '17, 20:44)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-61664" class="comment-tools"></div><div class="clear"></div><div id="comment-61664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61700"></span>

<div id="answer-container-61700" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61700-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you didn't say otherwise I'm assuming your custom dissector is in C (rather than Lua).</p><p>Fundamentally you want to use the routines in epan/reassemble.{h,c}. From the looks of it you may be able to use the <code>fragment_add()</code> method. You'll need to go through that code and/or other Wireshark code that uses the reassembly code to see how to use them (there's no README that I'm aware of).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '17, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-61700" class="comments-container"></div><div id="comment-tools-61700" class="comment-tools"></div><div class="clear"></div><div id="comment-61700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

