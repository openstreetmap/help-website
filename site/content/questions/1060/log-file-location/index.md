+++
type = "question"
title = "Log File Location"
description = '''I&#x27;m trying to catch an intermitant problem we think may be a broadcast storm. My first task is finding the log file. Where does wireshark put it?  My next task is to automatically delete before it gets to big and then start the log again. Is there anything premade for something like that? Network of...'''
date = "2010-11-22T07:18:00Z"
lastmod = "2010-11-22T07:25:00Z"
weight = 1060
keywords = [ "log", "automatically" ]
aliases = [ "/questions/1060" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Log File Location](/questions/1060/log-file-location)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1060-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to catch an intermitant problem we think may be a broadcast storm. My first task is finding the log file. Where does wireshark put it?<br />
</p><p>My next task is to automatically delete before it gets to big and then start the log again. Is there anything premade for something like that?</p><p>Network of 80 machines, random network lockup anywhere from 1-30 sec for all machines at the same time. I was planning to keep 10 minutes chunks of wireshark logs, and when a lock up occurs have some one in the lab grab the log and note the time so we can have a look see. Does that sound like a good plan?<br />
</p><p>Are there scripts already for this?<br />
</p><p>Is there anywhere I can share mine if I make one?</p><p>Thank you, rd42</p></div><div id="question-tags" class="tags-container tags">log automatically</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '10, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/81ad4fd84d21cc5d4ce51f615f32668c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rd42&#39;s gravatar image" /><p>rd42<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rd42 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-1060" class="comments-container"></div><div id="comment-tools-1060" class="comment-tools"></div><div class="clear"></div><div id="comment-1060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1061"></span>

<div id="answer-container-1061" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1061-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>All machines lock up for 1-30 seconds? Sounds like a Spanning Tree / loop problem to me.</p><p>The plan is good, but I guess "log file" is what is usually called a "trace file", which is a file containing captured network data. The idea is good to capture chunks, and to do that you should open the capture options dialog, second button on the left of the toolbar. Set capture to file, specify a good capture size (8-16MB) and let it write either in a large ring buffer or write continuously. Then wait for the problem and look at the according file.</p><p>I bet you'll see tons of duplicate packets created by a layer 2 loop, which means you have to enable/redesign your spanning tree.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '10, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-1061" class="comments-container"><span id="1064"></span><div id="comment-1064" class="comment"><div id="post-1064-score" class="comment-score"></div><div class="comment-text"><p>You might also want to look at using the Wireshark dumpcap program with ring buffers.</p><p>Dumpcap just captures and saves; It doesn't do any analysis (which requires saving state as the capture progresses).</p><p>When you encounter a problem you can then stop dumpcap and then use Wireshark to look at the capture(s).</p><p>See: http://www.wireshark.org/docs/man-pages/dumpcap.html</p></div><div id="comment-1064-info" class="comment-info"><span class="comment-age">(22 Nov '10, 07:44)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-1061" class="comment-tools"></div><div class="clear"></div><div id="comment-1061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

