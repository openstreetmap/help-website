+++
type = "question"
title = "Live TCP stream capture to a file"
description = '''Is there a way to have wireshark capture a live tcp stream and send that stream to a file when the stream is closed? Im fairly new to Wireshark and have not been able to accomplish this task.'''
date = "2013-03-26T17:47:00Z"
lastmod = "2013-03-26T19:44:00Z"
weight = 19857
keywords = [ "tcp" ]
aliases = [ "/questions/19857" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Live TCP stream capture to a file](/questions/19857/live-tcp-stream-capture-to-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19857-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to have wireshark capture a live tcp stream and send that stream to a file when the stream is closed? Im fairly new to Wireshark and have not been able to accomplish this task.</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '13, 17:47</strong></p><img src="https://secure.gravatar.com/avatar/edd91ee242b7c3b7d95e865b852214c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pgfdbug&#39;s gravatar image" /><p>pgfdbug<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pgfdbug has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Mar '13, 17:49</p></div></div><div id="comments-container-19857" class="comments-container"></div><div id="comment-tools-19857" class="comment-tools"></div><div class="clear"></div><div id="comment-19857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19859"></span>

<div id="answer-container-19859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19859-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark always captures to file until you stop the capture. If you know what IP and ports the TCP connection is using you could create a capture filter to only capture that communication to file.</p><p>If this is not helping you you should probably edit your question to make it more specific. What "stream" do you need to capture and what do you want to accomplish?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '13, 19:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19859" class="comments-container"><span id="19885"></span><div id="comment-19885" class="comment"><div id="post-19885-score" class="comment-score"></div><div class="comment-text"><p>I am looking to have wireshark monitor a designated port and ip. When new traffic is detected I want to write that info to a file until the end of file is detected. I want a new file created every time new traffic is detected. Is this possible with wireshark.</p></div><div id="comment-19885-info" class="comment-info"><span class="comment-age">(27 Mar '13, 13:23)</span> pgfdbug</div></div><span id="19886"></span><div id="comment-19886" class="comment"><div id="post-19886-score" class="comment-score"></div><div class="comment-text"><p>That would require some trigger based capture mechanism, and Wireshark doesn't have that kind of thing. You need to have a capture running to extract data from afterwards. Unfortunately you can't create single files based on events.</p></div><div id="comment-19886-info" class="comment-info"><span class="comment-age">(27 Mar '13, 13:35)</span> Jasper ♦♦</div></div><span id="19912"></span><div id="comment-19912" class="comment"><div id="post-19912-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer.</p></div><div id="comment-19912-info" class="comment-info"><span class="comment-age">(28 Mar '13, 11:56)</span> pgfdbug</div></div></div><div id="comment-tools-19859" class="comment-tools"></div><div class="clear"></div><div id="comment-19859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

