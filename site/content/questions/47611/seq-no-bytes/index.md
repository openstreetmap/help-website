+++
type = "question"
title = "seq no &gt; bytes"
description = '''hi, i was doing some tests and came across something that i don&#x27;t understand. I was capturing a file download from a FTP Server. When I look on the very last packet from the sender it matches the size of the downloaded file - 2 bytes (for SYN / FIN packets). The same file i was uploading on a SMB sh...'''
date = "2015-11-14T14:40:00Z"
lastmod = "2015-11-14T16:50:00Z"
weight = 47611
keywords = [ "bytes", "sequencenumber" ]
aliases = [ "/questions/47611" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [seq no &gt; bytes](/questions/47611/seq-no-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47611-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>i was doing some tests and came across something that i don't understand. I was capturing a file download from a FTP Server. When I look on the very last packet from the sender it matches the size of the downloaded file - 2 bytes (for SYN / FIN packets). The same file i was uploading on a SMB share but this time the very last packet of the sender has a higher sequence number value than the file size itself ??? Relative Seq Number are enabled, it might be something simple but I'm puzzled ...</p><p>any ideas please ?</p><p>BR</p><p>Adam</p></div><div id="question-tags" class="tags-container tags">bytes sequencenumber</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '15, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-47611" class="comments-container"></div><div id="comment-tools-47611" class="comment-tools"></div><div class="clear"></div><div id="comment-47611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47612"></span>

<div id="answer-container-47612" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47612-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's because the FTP transfer you looked at was a raw data transfer, meaning that it only transported the file content (the rest, like the get/put commands, is happening in a second session). SMB has additional protocol headers that are transported over TCP, and transfers the files in chunks (usually 64k). Look at your SMB packets and you'll see the headers - this is what takes additional bytes away from your sequence number calculation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '15, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Nov '15, 16:50</p></div></div><div id="comments-container-47612" class="comments-container"><span id="47619"></span><div id="comment-47619" class="comment"><div id="post-47619-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, thank you for your answer. I did no select the answer as the correct answer yet but the page says that i did it lol, strange.</p><p>I'm just wondering because in and older post i found the following "f you want to know only how many data bytes were transmitted, not including Ethernet, IP, or TCP headers, then make sure Wireshark's TCP preference "Relative sequence numbers" is enabled. (This is the default.) Go to the very last packet from the sender and see what the sequence number is. This is the total number of data bytes transferred."</p><p><a href="https://ask.wireshark.org/questions/42834/calculate-the-number-of-bytes-sent-in-a-tcp-session">https://ask.wireshark.org/questions/42834/calculate-the-number-of-bytes-sent-in-a-tcp-session</a></p><p>Is SMB an exception or am I still missing something ?</p><p>BR</p><p>Adam</p></div><div id="comment-47619-info" class="comment-info"><span class="comment-age">(15 Nov '15, 11:49)</span> adasko</div></div><span id="47620"></span><div id="comment-47620" class="comment"><div id="post-47620-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Is SMB an exception or am I still missing something ?<br />
</p></blockquote><p>b) is correct :-)</p><p>Think about "file contents" and "file description". As <a href="https://ask.wireshark.org/users/145/jasper">Jasper</a> wrote, ftp uses a dedicated tcp session for transferring the contents of each file (hence the tcp sequence number of the last transferred packet matches the file <strong>contents</strong> size), and uses the common control tcp session to transfer the file name(s).</p><p>SMB, in contrary, transfers both the file contents and the file description (pathname and file name at least) in a single tcp session, so the number of transferred bytes includes not only the size of the file contents but also of the additional information.</p></div><div id="comment-47620-info" class="comment-info"><span class="comment-age">(15 Nov '15, 12:04)</span> sindy</div></div><span id="47621"></span><div id="comment-47621" class="comment"><div id="post-47621-score" class="comment-score">1</div><div class="comment-text"><p>SMB is a protocol carried <strong>over</strong> TCP (i.e., all the SMP stuff, including the SMP protocol headers, is part of the TCP data bytes).</p><p>So: as indicated by Jasper, the TCP sequence numbers (i.e., TCP data bytes) for an SMB TCP payload include both SMB protocol header data and SMB file data.</p></div><div id="comment-47621-info" class="comment-info"><span class="comment-age">(15 Nov '15, 12:09)</span> Bill Meier ♦♦</div></div><span id="47625"></span><div id="comment-47625" class="comment"><div id="post-47625-score" class="comment-score"></div><div class="comment-text"><p>so to known the how many data bytes were transmitted in a SMB conversation I would have to sum the tcp length values ?</p></div><div id="comment-47625-info" class="comment-info"><span class="comment-age">(16 Nov '15, 00:15)</span> adasko</div></div><span id="47626"></span><div id="comment-47626" class="comment"><div id="post-47626-score" class="comment-score">1</div><div class="comment-text"><p>Your original question was suggesting that you were interested in the size of the contents of a single transferred file. This is possible with ftp where a dedicated tcp session is created for each individual file to be transported.</p><p>SMB, unlike FTP, uses a single TCP session to transport both the files' contents and the control communication, i.e. much more data than just the file(s) contents, like the initial login conversation, the file name and path, the timestamps of creation/last access/last write etc. So by tcp seq no, it is impossible to determine how many bytes the file contents alone has got. You would need to dive deeper into the SMB packets and sum up the SMB payload.</p></div><div id="comment-47626-info" class="comment-info"><span class="comment-age">(16 Nov '15, 01:03)</span> sindy</div></div><span id="47627"></span><div id="comment-47627" class="comment not_top_scorer"><div id="post-47627-score" class="comment-score"></div><div class="comment-text"><p>@sindy ok now i see. Ist there perhaps any query / filter I could use to sum up the SMB payload ?</p></div><div id="comment-47627-info" class="comment-info"><span class="comment-age">(16 Nov '15, 01:07)</span> adasko</div></div><span id="47628"></span><div id="comment-47628" class="comment not_top_scorer"><div id="post-47628-score" class="comment-score"></div><div class="comment-text"><p>The term "SMB payload" in usual understanding still means more than just the file contents.</p><p>But to answer what you really intended to ask, try</p><p>File -&gt; Export Objects -&gt; SMB</p><p>You should get a list of files with sizes. I don't have a SMB capture handy to verify this, however.</p></div><div id="comment-47628-info" class="comment-info"><span class="comment-age">(16 Nov '15, 01:16)</span> sindy</div></div></div><div id="comment-tools-47612" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-47612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

