+++
type = "question"
title = "After capturing traffic for 5 minutes how to calculate total income and outgoing data for that period of time?"
description = '''hello, I want to calculate the total incoming and outgoing traffic for an hour. After capturing data for a certain period of time. As I want to calculate how the traffic is increasing or decreasing after an hour for a day. This is important for me as I have to predict the traffic as a part of a coll...'''
date = "2017-02-01T04:32:00Z"
lastmod = "2017-02-05T01:20:00Z"
weight = 59212
keywords = [ "traffic", "prediction" ]
aliases = [ "/questions/59212" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [After capturing traffic for 5 minutes how to calculate total income and outgoing data for that period of time?](/questions/59212/after-capturing-traffic-for-5-minutes-how-to-calculate-total-income-and-outgoing-data-for-that-period-of-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, I want to calculate the total incoming and outgoing traffic for an hour. After capturing data for a certain period of time. As I want to calculate how the traffic is increasing or decreasing after an hour for a day. This is important for me as I have to predict the traffic as a part of a college assaignment please help me.</p></div><div id="question-tags" class="tags-container tags">traffic prediction</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '17, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/2db98c9767028d68be23866d7a9fd15d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Junaid388&#39;s gravatar image" /><p>Junaid388<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Junaid388 has no accepted answers">0%</span></p></div></div><div id="comments-container-59212" class="comments-container"></div><div id="comment-tools-59212" class="comment-tools"></div><div class="clear"></div><div id="comment-59212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="59219"></span>

<div id="answer-container-59219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59219-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could go spelunkng in the Statistics menu, but I would suggest using more suitable software for this, eg <a href="http://www.ntop.org">ntop-ng</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '17, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59219" class="comments-container"><span id="59235"></span><div id="comment-59235" class="comment"><div id="post-59235-score" class="comment-score"></div><div class="comment-text"><p>Thank you for replying me. I am using wireshark 2.2.3 on windows. In Statistics menu I cannot find the option spelunkng. Hw can I find it.</p></div><div id="comment-59235-info" class="comment-info"><span class="comment-age">(01 Feb '17, 20:01)</span> Junaid388</div></div><span id="59241"></span><div id="comment-59241" class="comment"><div id="post-59241-score" class="comment-score"></div><div class="comment-text"><p>Oh, that was not to be taken literally, 'go spelunking' is a figure of speech for 'go search and discover in the depth of this menu'. You can find the term <a href="https://www.wireshark.org/download.html#spelunking">here</a> as well.</p></div><div id="comment-59241-info" class="comment-info"><span class="comment-age">(02 Feb '17, 02:25)</span> Jaap ♦</div></div></div><div id="comment-tools-59219" class="comment-tools"></div><div class="clear"></div><div id="comment-59219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59252"></span>

<div id="answer-container-59252" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59252-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One way to do it is use the I/O Graph. So for example,</p><ul><li>Go to Statistics IO Graph</li><li>Add a new plot</li><li>Set the filter to select data by MAC or IP Destination address</li><li>Choose Y-Axis of Sum(Y-field)</li><li>Set Y Field to the value you want to sum e.g. frame.len</li><li>Set the Interval to 10 mins</li></ul><p>The height of the plot is the sum of ghe value. You can use Zoom to increase the precision.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '17, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Feb '17, 01:19</p></div></div><div id="comments-container-59252" class="comments-container"></div><div id="comment-tools-59252" class="comment-tools"></div><div class="clear"></div><div id="comment-59252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59255"></span>

<div id="answer-container-59255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59255-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>An alternative method is to add frame.len as a Packet List column, export the packet list to CSV and then use Excel to do the maths.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '17, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-59255" class="comments-container"></div><div id="comment-tools-59255" class="comment-tools"></div><div class="clear"></div><div id="comment-59255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

