+++
type = "question"
title = "Syn packet and Sequence Number"
description = '''I&#x27;m looking at a pcap, with the 3-way handshake already done. After an initial file is sent, the sequence number is 4887. The client sends another TCP packet with the SYN flag, which prompts another 3-way handshake. This resets the sequence numbers back to 1, as seen in the packet capture file. Howe...'''
date = "2014-08-20T15:00:00Z"
lastmod = "2014-08-20T15:03:00Z"
weight = 35642
keywords = [ "number", "syn", "sequence" ]
aliases = [ "/questions/35642" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Syn packet and Sequence Number](/questions/35642/syn-packet-and-sequence-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35642-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking at a pcap, with the 3-way handshake already done. After an initial file is sent, the sequence number is 4887. The client sends another TCP packet with the SYN flag, which prompts another 3-way handshake. This resets the sequence numbers back to 1, as seen in the packet capture file. However, immediately after when the client asks for another file, the sequence number goes back to what it started as before, plus a few more, to 5321.</p><p>Why does the sequence number shoot back up to 5321, when it was reset back to 1?</p></div><div id="question-tags" class="tags-container tags">number syn sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '14, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/2b398529553da221a724f1ea4a2e0663?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FireShark&#39;s gravatar image" /><p>FireShark<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FireShark has no accepted answers">0%</span></p></div></div><div id="comments-container-35642" class="comments-container"></div><div id="comment-tools-35642" class="comment-tools"></div><div class="clear"></div><div id="comment-35642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35643"></span>

<div id="answer-container-35643" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35643-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to isolate TCP connections to track sequence numbers. You cannot compare them across multiple connections. Use the pop up menu to select conversation filters -&gt; TCP on a packet to isolate the connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35643" class="comments-container"><span id="35645"></span><div id="comment-35645" class="comment"><div id="post-35645-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I didn't notice that although it was the same IP address, a different connection was being made on a new port.</p></div><div id="comment-35645-info" class="comment-info"><span class="comment-age">(20 Aug '14, 16:10)</span> FireShark</div></div><span id="35648"></span><div id="comment-35648" class="comment"><div id="post-35648-score" class="comment-score">1</div><div class="comment-text"><p>One minor comment on this - Wireshark by default uses relative sequence numbers starting from 0 for each TCP session, for easy human readability and math. The reality is that the sequence number in the packet is probably much greater than 0 in both cases, so it's not "dropping back" to 0, but rather analyzing that it's a second TCP session with a new set of sequence numbers which Wireshark will assign new relative numbers for, starting at 0.</p></div><div id="comment-35648-info" class="comment-info"><span class="comment-age">(20 Aug '14, 19:23)</span> Quadratic</div></div></div><div id="comment-tools-35643" class="comment-tools"></div><div class="clear"></div><div id="comment-35643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

