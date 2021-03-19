+++
type = "question"
title = "Window size full messages while uploading to the server"
description = '''I am getting a lot of tcp window full messages when I upload data to the server using SMB2. I heard that these are just messages from Wireshark expert, but somewhere I also heard that these can cause slow data transfer as the sender has to wait for ack from the receiver everytime this message is sho...'''
date = "2014-06-02T01:42:00Z"
lastmod = "2014-06-02T01:45:00Z"
weight = 33257
keywords = [ "tcpwindowfull" ]
aliases = [ "/questions/33257" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Window size full messages while uploading to the server](/questions/33257/window-size-full-messages-while-uploading-to-the-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33257-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting a lot of tcp window full messages when I upload data to the server using SMB2. I heard that these are just messages from Wireshark expert, but somewhere I also heard that these can cause slow data transfer as the sender has to wait for ack from the receiver everytime this message is shown.</p></div><div id="question-tags" class="tags-container tags">tcpwindowfull</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '14, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/4316c1946f08f682c8b02ca026a5a95e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rikki&#39;s gravatar image" /><p>Rikki<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rikki has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '15, 19:06</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-33257" class="comments-container"></div><div id="comment-tools-33257" class="comment-tools"></div><div class="clear"></div><div id="comment-33257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33258"></span>

<div id="answer-container-33258" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33258-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>TCP Window Full is a warning sign, but it may not mean that there is trouble. It all depends on how much time is lost by the full window, so you should check the time distance between the "Window Full" and the next window advertisement by the receiver. Meaning: you need to find out how long the sender has to stop and wait until it can continue. If that time adds up to significant delays you have a problem on the receiving side.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '14, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33258" class="comments-container"><span id="33262"></span><div id="comment-33262" class="comment"><div id="post-33262-score" class="comment-score"></div><div class="comment-text"><p>Your capture setup is a problem, it is quite hard to say what happens in your case with a capture that was done locally. But it looks like everything is not so bad.</p><p>I recommend you read this blog post: <a href="http://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">http://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a> to find out why local captures are a problem. In your case it is quite possible that the "window full" messages are a phantom diagnosis caused by the way the packets where recorded.</p></div><div id="comment-33262-info" class="comment-info"><span class="comment-age">(02 Jun '14, 02:03)</span> Jasper ♦♦</div></div></div><div id="comment-tools-33258" class="comment-tools"></div><div class="clear"></div><div id="comment-33258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

