+++
type = "question"
title = "How to detect a broken pipe using wireshark packet traces?"
description = '''I am getting a broken pipe socket error, most probably the other end is not closing the connection because the other end timeout later when it does not receive any packets. How can I find this by looking at packet trace. In case if the other end(destination) is closing the connection, should I see r...'''
date = "2012-09-13T11:44:00Z"
lastmod = "2012-09-17T13:33:00Z"
weight = 14248
keywords = [ "pipe", "broken", "wireshark" ]
aliases = [ "/questions/14248" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to detect a broken pipe using wireshark packet traces?](/questions/14248/how-to-detect-a-broken-pipe-using-wireshark-packet-traces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14248-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting a broken pipe socket error, most probably the other end is not closing the connection because the other end timeout later when it does not receive any packets. How can I find this by looking at packet trace. In case if the other end(destination) is closing the connection, should I see rst message at point of failure. If a firewall is causing broken pipe, How to identify that in packet traces. If something is causing a broken pipe. How to identify the cause?</p><p>I am very new to using wireshark. I am not looking for exact solution to this problem. I will be glad to receive any suggestion which might help me to inch closer to solving this issue.</p></div><div id="question-tags" class="tags-container tags">pipe broken wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '12, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/c1a0adc42ffdbf7562852ebd8cea1e51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark_shisya&#39;s gravatar image" /><p>wireshark_sh...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark_shisya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Sep '12, 13:39</p></div></div><div id="comments-container-14248" class="comments-container"><span id="14332"></span><div id="comment-14332" class="comment"><div id="post-14332-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am getting a broken pipe socket error,</p></blockquote><p>where do you get that error message?</p></div><div id="comment-14332-info" class="comment-info"><span class="comment-age">(17 Sep '12, 13:03)</span> Kurt Knochner ♦</div></div><span id="14333"></span><div id="comment-14333" class="comment"><div id="post-14333-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, write system call returns -1 and when I read the errno, I see 32 (broken pipe).</p></div><div id="comment-14333-info" class="comment-info"><span class="comment-age">(17 Sep '12, 13:17)</span> wireshark_sh...</div></div></div><div id="comment-tools-14248" class="comment-tools"></div><div class="clear"></div><div id="comment-14248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14334"></span>

<div id="answer-container-14334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14334-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Hi Kurt, write system call returns -1 and when I read the errno, I see 32 (broken pipe).</p></blockquote><p>O.K. that could mean, you're trying to write to a local socket that has been closed. So now, you need to figure out why the socket was closed. There are several reasons:</p><ol><li>the remote end closed it with a RST or FIN</li><li>the OS closed it due to some timeout</li><li>your code closed it, due to a bug</li><li>the OS closed it due to resource exhaustion (rather unlikely)</li></ol><p>Cause 1.:<br />
You should see a FIN or RST in the network capture, coming from the remote end.</p><p>Cause 2.:<br />
You should should see a FIN or RST, coming from your local machine (depends on the OS settings). Is there a longer period of inactivity when you try to write to the socket?</p><p>Cause 3.:<br />
Well, start a debugger ;-)</p><p>Cause 4.:<br />
Even harder to detect. If you're lucky, you'll see a FIN or RST in the network capture.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '12, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14334" class="comments-container"><span id="14335"></span><div id="comment-14335" class="comment"><div id="post-14335-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt, Thanks for responding. In cause 4, why do you say if lucky, I will see a FIN or RST in the network capture.</p></div><div id="comment-14335-info" class="comment-info"><span class="comment-age">(17 Sep '12, 13:37)</span> wireshark_sh...</div></div><span id="14338"></span><div id="comment-14338" class="comment"><div id="post-14338-score" class="comment-score"></div><div class="comment-text"><p>because if the OS runs into a resource exhaustion, you never know how it reacts, unless you study the source code of that specific OS ;-)</p></div><div id="comment-14338-info" class="comment-info"><span class="comment-age">(17 Sep '12, 13:49)</span> Kurt Knochner ♦</div></div><span id="41323"></span><div id="comment-41323" class="comment"><div id="post-41323-score" class="comment-score"></div><div class="comment-text"><p>plus some staff to Case1</p><p>if see sever RSF or FIN to client, we need to found the reason it case closing..</p><p>Today I found a case that client send or connect too slow, so server side timeout, then FIN/RST to client...</p><p>Then we see <code>broken pipe</code>, it's maybe helpful to others ^ ^</p></div><div id="comment-41323-info" class="comment-info"><span class="comment-age">(09 Apr '15, 06:52)</span> robi</div></div></div><div id="comment-tools-14334" class="comment-tools"></div><div class="clear"></div><div id="comment-14334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

