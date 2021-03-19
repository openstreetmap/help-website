+++
type = "question"
title = "ZeroWindowProbe data in saved raw file"
description = '''I captured a TCP session that was throttled by the receiver using TCP ZeroWindow. Subsequently the sender probed two times, using ZeroWindowProbe including the next data byte. When the receiver finally opened the window, transmission resumed as usual. During the probing, ACK and SEQ numbers did not ...'''
date = "2017-07-14T11:47:00Z"
lastmod = "2017-07-14T14:18:00Z"
weight = 62785
keywords = [ "zerowindowprobe" ]
aliases = [ "/questions/62785" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ZeroWindowProbe data in saved raw file](/questions/62785/zerowindowprobe-data-in-saved-raw-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62785-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured a TCP session that was throttled by the receiver using TCP ZeroWindow. Subsequently the sender probed two times, using ZeroWindowProbe including the next data byte. When the receiver finally opened the window, transmission resumed as usual. During the probing, ACK and SEQ numbers did not increment, as expected.</p><p>In wireshark when I "Follow TCP stream" and then save the stream as raw, one of the two probing data bytes are included in the file. Why is that? Shouldn't they be omitted like re-transmitted data? And if not, why would there only be one of the two additional bytes?</p><p>Here is a sanitized capture demonstrating the issue:</p><p><a href="https://www.dropbox.com/s/b8qubwtdi5nucqx/zwin2_anon.pcapng?dl=0">https://www.dropbox.com/s/b8qubwtdi5nucqx/zwin2_anon.pcapng?dl=0</a></p><p>After saving the stream, you can find the duplicated byte by searching for "0x50 0x50".</p></div><div id="question-tags" class="tags-container tags">zerowindowprobe</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '17, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/528f6fec8c573b8542103eadd64f9f65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="namnamreg&#39;s gravatar image" /><p>namnamreg<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="namnamreg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '17, 08:52</p></div></div><div id="comments-container-62785" class="comments-container"></div><div id="comment-tools-62785" class="comment-tools"></div><div class="clear"></div><div id="comment-62785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62786"></span>

<div id="answer-container-62786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62786-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Zero Window is the receiving system saying that it's receive buffer is full and it has no room for incoming data. Naturally, this stops the data transfer. When the receiving system has space in its receive buffer again, it will send a Window Update. It's possible that, due to packet loss, the sending system might not get the window update, so the sending system will send Zero Window Probes periodically, just to check if the receiver's buffer is still full. It's asking the receiver "Are you still out of space, or can I resume sending?" Zero window probes contain the next one byte of data.</p><p>If the receiving system now has space in its receive buffer, it will accept that byte of data, increment the ACK by one, and put its current window size in the window size field.</p><p>If the receiving system is still out of space, it will not have room for that byte of data, so it will send back an acknowledgment but the ACK number will not increase, indicating that it did not accept the byte of data, and again putting zero in the window size field.</p><p>The ACK did not increase because the two data bytes were not accepted. When the communication resumed, you only saw one of the two bytes because both of the zero window probes contained the <em>same</em> byte of data. It was not accepted either time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '17, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-62786" class="comments-container"><span id="62792"></span><div id="comment-62792" class="comment"><div id="post-62792-score" class="comment-score"></div><div class="comment-text"><p>Maybe I wasn't clear, the actual data byte in question is sent three times: First and second time with the probes (ACK does not increment, like you pointed out), and then again when the window opens, as first byte of the next full data packet. So, on the receiving end's application layer I only see that byte once, as expected. However when I save the captured stream in wireshark, I see it twice. So my conclusion is that one of the two probe bytes is being interpreted as data when the stream gets reassembled, but it shouldn't.</p></div><div id="comment-62792-info" class="comment-info"><span class="comment-age">(14 Jul '17, 21:17)</span> namnamreg</div></div><span id="62807"></span><div id="comment-62807" class="comment"><div id="post-62807-score" class="comment-score"></div><div class="comment-text"><p>That sounds like a bug. I suggest you submit a bug report at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a></p></div><div id="comment-62807-info" class="comment-info"><span class="comment-age">(15 Jul '17, 10:48)</span> Jim Aragon</div></div><span id="62808"></span><div id="comment-62808" class="comment"><div id="post-62808-score" class="comment-score"></div><div class="comment-text"><p>Or you can share us the example <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-62808-info" class="comment-info"><span class="comment-age">(15 Jul '17, 11:14)</span> Christian_R</div></div><span id="62826"></span><div id="comment-62826" class="comment"><div id="post-62826-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I wasn't aware of that great tool! I edited the question and added a link to a sample.</p></div><div id="comment-62826-info" class="comment-info"><span class="comment-age">(17 Jul '17, 08:55)</span> namnamreg</div></div><span id="62828"></span><div id="comment-62828" class="comment"><div id="post-62828-score" class="comment-score"></div><div class="comment-text"><p>It seems that Wireshark is getting confused. The Zero Window Probes are in packets 20 and 22. If you follow the stream and then switch the display to "C Arrays" you will see each packet listed with a note in the form "/ <em>Packet n</em> /", where "n" is the packet number. Packet 22, the second Zero Window Probe, is missing. Every other packet is listed, whether it has data or not. This looks like a bug to me, and I assume that the same bug is responsible both for the missing packet in the Follow Stream C Arrays display, and for the fact that one of the Zero Window Probes is saved as data.</p></div><div id="comment-62828-info" class="comment-info"><span class="comment-age">(17 Jul '17, 11:32)</span> Jim Aragon</div></div></div><div id="comment-tools-62786" class="comment-tools"></div><div class="clear"></div><div id="comment-62786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

