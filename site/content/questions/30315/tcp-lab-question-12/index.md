+++
type = "question"
title = "TCP Lab question 12?"
description = '''Hey guys, trying to do question 12 here, but I&#x27;m a bit stumped.  12 . What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value. The Computer Networking book states that the increase of w happens when a loss event occurs (which doesn&#x27;t in ...'''
date = "2014-03-01T18:35:00Z"
lastmod = "2014-03-02T07:37:00Z"
weight = 30315
keywords = [ "rtt", "throughput", "w", "tcp" ]
aliases = [ "/questions/30315" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Lab question 12?](/questions/30315/tcp-lab-question-12)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30315-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, trying to do question 12 here, but I'm a bit stumped.</p><p>12 . What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value.</p><p>The Computer Networking book states that the increase of w happens when a loss event occurs (which doesn't in the provided TCP trace, so that can be ignored (I think?)) Is the final formula:</p><p>w/RTT ?</p><p>If it is, then how do I find what w and RTT are. Are these the differences between the first TCP and last ACK?</p></div><div id="question-tags" class="tags-container tags">rtt throughput w tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '14, 18:35</strong></p><img src="https://secure.gravatar.com/avatar/a5349cd64cc3375ba6c9e54801127b2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rainman&#39;s gravatar image" /><p>rainman<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rainman has no accepted answers">0%</span></p></div></div><div id="comments-container-30315" class="comments-container"><span id="30317"></span><div id="comment-30317" class="comment"><div id="post-30317-score" class="comment-score"></div><div class="comment-text"><p>What Lab are you referring to? What is the "Computing Networking book"?</p></div><div id="comment-30317-info" class="comment-info"><span class="comment-age">(02 Mar '14, 01:44)</span> Jasper ♦♦</div></div><span id="30320"></span><div id="comment-30320" class="comment"><div id="post-30320-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.amazon.co.uk/Computer-Networking-A-Top-down-Approach/dp/0273768964/ref=sr_1_fkmr0_1?ie=UTF8&amp;qid=1393771457&amp;sr=8-1-fkmr0&amp;keywords=computer+networking+kurose+rose">http://www.amazon.co.uk/Computer-Networking-A-Top-down-Approach/dp/0273768964/ref=sr_1_fkmr0_1?ie=UTF8&amp;qid=1393771457&amp;sr=8-1-fkmr0&amp;keywords=computer+networking+kurose+rose</a></p><p>The lab is called TCP Lab from the book above^</p></div><div id="comment-30320-info" class="comment-info"><span class="comment-age">(02 Mar '14, 06:44)</span> rainman</div></div></div><div id="comment-tools-30315" class="comment-tools"></div><div class="clear"></div><div id="comment-30315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30321"></span>

<div id="answer-container-30321" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30321-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Some hints and some questions....</p><p>Hint #1: RTT calculation</p><p>If you draw a picture of the TCP 3-way handshake (client --&gt; router --&gt; router --&gt; server), what could the RTT (round trip time) be, if you look at the SYN and SYN-ACK frames? How can you use that knowledge to calculate the RTT in a capture file, if the trace was taken on (or near) the client? What changes if you've taken the trace on (or near) the server?</p><p>Question(s) #1: w?</p><p>How is <strong>w</strong> defined in the book? In some papers I've read, w is the congestion window. Is it the same in the book? If so, did you find a definition of the congestion window in the book or with the help of Mr. search engine? If no, please search it. Then: How would you describe it in your own words?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '14, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Mar '14, 07:37</p></div></div><div id="comments-container-30321" class="comments-container"></div><div id="comment-tools-30321" class="comment-tools"></div><div class="clear"></div><div id="comment-30321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

