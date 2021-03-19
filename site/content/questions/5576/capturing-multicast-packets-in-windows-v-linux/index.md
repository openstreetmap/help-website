+++
type = "question"
title = "Capturing multicast packets in Windows v. Linux"
description = '''I have a program on one computer that is sending multicast packets. I can see the packets in Wireshark on that same computer, and on a different computer while in Linux, but not while in Windows (it&#x27;s dual-boot). The sending computer is wired into a router. The receiving computer is wireless. I&#x27;m us...'''
date = "2011-08-08T10:00:00Z"
lastmod = "2011-08-09T13:03:00Z"
weight = 5576
keywords = [ "windows", "multicast", "linux" ]
aliases = [ "/questions/5576" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing multicast packets in Windows v. Linux](/questions/5576/capturing-multicast-packets-in-windows-v-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5576-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a program on one computer that is sending multicast packets. I can see the packets in Wireshark on that same computer, and on a different computer while in Linux, but not while in Windows (it's dual-boot).</p><p>The sending computer is wired into a router. The receiving computer is wireless. I'm using the same wireless NIC in both Linux and Windows. Any help would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags">windows multicast linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '11, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/8d89c3087cc6cb98793ab7c0f5658c56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bch36&#39;s gravatar image" /><p>bch36<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bch36 has no accepted answers">0%</span></p></div></div><div id="comments-container-5576" class="comments-container"><span id="5578"></span><div id="comment-5578" class="comment"><div id="post-5578-score" class="comment-score">1</div><div class="comment-text"><p>Is the capturing computer (Windows) wireless? If so, have you checked out <a href="http://ask.wireshark.org/questions/2702/monitor-mode-problem?page=1#2703">this answer</a>?</p></div><div id="comment-5578-info" class="comment-info"><span class="comment-age">(08 Aug '11, 10:33)</span> multipleinte...</div></div></div><div id="comment-tools-5576" class="comment-tools"></div><div class="clear"></div><div id="comment-5576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5600"></span>

<div id="answer-container-5600" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5600-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you, multipleinterfaces. That was exactly the problem.<br />
</p><p>Just for future people searching: there was actually no problem with the packets being transferred, I simply had to use Microsoft Network Monitor to see them.</p><p>The link posted by multipleinterfaces goes into more detail, but long story short, on a Windows Vista or Windows 7 machine, Wireshark cannot capture packets in monitor mode, which was apparently what I needed to do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '11, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/8d89c3087cc6cb98793ab7c0f5658c56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bch36&#39;s gravatar image" /><p>bch36<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bch36 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-5600" class="comments-container"></div><div id="comment-tools-5600" class="comment-tools"></div><div class="clear"></div><div id="comment-5600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

