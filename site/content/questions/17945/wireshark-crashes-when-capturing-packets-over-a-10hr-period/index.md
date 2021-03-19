+++
type = "question"
title = "Wireshark crashes when capturing packets over a 10hr period"
description = '''Hi, I have a need to capture packets continuously (with a filter) in a ring buffer with each file size set to 300Mb and maximum of 4 files. This is all done to capture a particular rare instance of a packet failure. I left my wireshark capture running overnight and then when I came back to look the ...'''
date = "2013-01-24T16:46:00Z"
lastmod = "2013-01-25T02:01:00Z"
weight = 17945
keywords = [ "crashed", "wireshark" ]
aliases = [ "/questions/17945" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark crashes when capturing packets over a 10hr period](/questions/17945/wireshark-crashes-when-capturing-packets-over-a-10hr-period)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17945-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a need to capture packets continuously (with a filter) in a ring buffer with each file size set to 300Mb and maximum of 4 files. This is all done to capture a particular rare instance of a packet failure.</p><p>I left my wireshark capture running overnight and then when I came back to look the following morning, the wireshark had crashed and had popped up a Visual Studio 2005 debug dialog to debug the crash. I have v1.8.4 installed in my case.</p><p>Has anyone experienced this before? What can we do to get around this?</p></div><div id="question-tags" class="tags-container tags">crashed wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '13, 16:46</strong></p><img src="https://secure.gravatar.com/avatar/841a1ecf56de099ad9476e2acefeb21a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kasun&#39;s gravatar image" /><p>Kasun<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kasun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '13, 17:32</p></div></div><div id="comments-container-17945" class="comments-container"></div><div id="comment-tools-17945" class="comment-tools"></div><div class="clear"></div><div id="comment-17945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17954"></span>

<div id="answer-container-17954" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17954-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is likely to be the known bug of an <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory error</a>. For any long term capture you should use dumpcap instead of Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '13, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-17954" class="comments-container"><span id="17959"></span><div id="comment-17959" class="comment"><div id="post-17959-score" class="comment-score">1</div><div class="comment-text"><p>I agree that the crash is almost certainly due to running out of memory; however, I would categorize it as expected behavior rather than as a known bug.</p></div><div id="comment-17959-info" class="comment-info"><span class="comment-age">(25 Jan '13, 21:15)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-17954" class="comment-tools"></div><div class="clear"></div><div id="comment-17954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

