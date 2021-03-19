+++
type = "question"
title = "WireShark eats up memory at an alarming rate for version after 1.6.5"
description = '''I&#x27;ve now tested 5 different version of WireShark on my Windows 2008 R2 Servers. The only version that I found to not eat up memory at an alarming rate is the 64 Bit of 1.6.5. I&#x27;ve tried 1.6.14, 1.8.2, 1.8.6 and they all are eating up memory at a crazy rate even when the packet rate is not that high....'''
date = "2013-03-26T12:39:00Z"
lastmod = "2013-03-26T13:07:00Z"
weight = 19852
keywords = [ "1.6.14", "leak", "1.8.6", "memory" ]
aliases = [ "/questions/19852" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark eats up memory at an alarming rate for version after 1.6.5](/questions/19852/wireshark-eats-up-memory-at-an-alarming-rate-for-version-after-165)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19852-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've now tested 5 different version of WireShark on my Windows 2008 R2 Servers. The only version that I found to not eat up memory at an alarming rate is the 64 Bit of 1.6.5. I've tried 1.6.14, 1.8.2, 1.8.6 and they all are eating up memory at a crazy rate even when the packet rate is not that high. Eventually Wireshark will crash which is a know bug because it is running out of memory. My issue is the rate at which the newer version are eating up memory over version 1.6.5. Can anyone explain what has changed since 1.6.5 that would account for this or is this a bug?</p></div><div id="question-tags" class="tags-container tags">1.6.14 leak 1.8.6 memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '13, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/0dfa2a10f23c2c7f0e729c267bebac0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rdoerr&#39;s gravatar image" /><p>rdoerr<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rdoerr has no accepted answers">0%</span></p></div></div><div id="comments-container-19852" class="comments-container"></div><div id="comment-tools-19852" class="comment-tools"></div><div class="clear"></div><div id="comment-19852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19853"></span>

<div id="answer-container-19853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19853-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you connecting with remote desktop to the Windows 2008 R2 server? You are likely hitting a memory leak in GTK2, the multi platform GUI toolkit used by Wireshark. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8281">bug 8281</a> for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '13, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-19853" class="comments-container"><span id="19854"></span><div id="comment-19854" class="comment"><div id="post-19854-score" class="comment-score"></div><div class="comment-text"><p>Yes, I am using Remote Desktop to connect to all of my WireShark machines. This afternoon I test all the versions of 1.6.5 up to 1.6.14 and here is what I figured out. The latest version that works without having the Memory Leak issue is 1.6.8. I was unable to test 1.6.9 since it failed to run after doing a fresh install. All version 1.6.10 through 1.6.14 all have the same Memory Leak issue. I read up on the bug 8281 that you reported above but still didn't see any fix or work around for this issue. I would think many people are using RDP on Windows 2008 R2.</p><p>Thanks</p><p>Ray</p></div><div id="comment-19854-info" class="comment-info"><span class="comment-age">(26 Mar '13, 13:55)</span> rdoerr</div></div><span id="19855"></span><div id="comment-19855" class="comment"><div id="post-19855-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately there is no fix available until we get a fixed GTK package (the 1.6.8 release is using GTK 2.24.10-20120208 while the 1.6.10 release is using version 2.24.10-2.7). In the meantime you can try using QTshark, or capture the pcap file with dumpcap/tshark and open it locally on your computer.</p></div><div id="comment-19855-info" class="comment-info"><span class="comment-age">(26 Mar '13, 14:22)</span> Pascal Quantin</div></div></div><div id="comment-tools-19853" class="comment-tools"></div><div class="clear"></div><div id="comment-19853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

