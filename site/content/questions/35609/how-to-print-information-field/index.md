+++
type = "question"
title = "how to print &quot;Information&quot; field?"
description = '''Hi, I&#x27;m trying to look at real time capturing through tshark. The requirement is that I only see some specific fields. For example, if I want to quickly identify if there were dupAck or retransmission, I can only print out the &quot;Information&quot; field as shown up in wireshark GUI. I did -T -e but it does...'''
date = "2014-08-20T02:42:00Z"
lastmod = "2014-08-20T06:41:00Z"
weight = 35609
keywords = [ "tshark" ]
aliases = [ "/questions/35609" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to print "Information" field?](/questions/35609/how-to-print-information-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35609-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to look at real time capturing through tshark. The requirement is that I only see some specific fields. For example, if I want to quickly identify if there were dupAck or retransmission, I can only print out the "Information" field as shown up in wireshark GUI. I did -T -e but it doesn't help. I know that information is not a TCP field, but a wireshark function. How to achieve my goal for real time monitoring for such sensitive information?</p><p>thanks a lot!</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '14, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '14, 03:23</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-35609" class="comments-container"></div><div id="comment-tools-35609" class="comment-tools"></div><div class="clear"></div><div id="comment-35609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35614"></span>

<div id="answer-container-35614" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35614-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on your definition of "real time", tshark may not qualify as a real time application as it does take some time for packets to be processed.</p><p>Given the above qualification, you can print out the state of the tcp.analysis.xxx flags, e.g.</p><p><code>tshark -i xxx -T fields -e frame.number -e tcp.analysis.spurious_retransmission</code></p><p>You can see a list of all the tcp.analysis flags using <code>tshark -G fields</code> and then searching the output for "tcp.analysis" using your preferred method, e.g. grep.</p><p>Note that if you're running tshark for any length of time it's likely to run out of memory and crash. See the wiki page <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">Out of Memory</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35614" class="comments-container"></div><div id="comment-tools-35614" class="comment-tools"></div><div class="clear"></div><div id="comment-35614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35623"></span>

<div id="answer-container-35623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35623-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the answers to these questions for 2 possible solutions:</p><ul><li><a href="https://ask.wireshark.org/questions/32522/tshark-info-field">https://ask.wireshark.org/questions/32522/tshark-info-field</a></li><li><a href="https://ask.wireshark.org/questions/32574/tshark-column-fields">https://ask.wireshark.org/questions/32574/tshark-column-fields</a></li></ul><p><strong>Note</strong>: With version 1.12, use <code>-e _ws.col.Info</code>, whereas previous versions (1.8 and 1.10 only, I believe), you would need to use <code>-e col.Info</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35623" class="comments-container"></div><div id="comment-tools-35623" class="comment-tools"></div><div class="clear"></div><div id="comment-35623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

