+++
type = "question"
title = "Tshark problem"
description = '''Dear friends, I am trying to export output to a csv file with tshark and I would like to export Beacon Timestamp not in a Hex format but in Decimal format.  When I am using this method : -e wlan_mgt.fixed.timestamp I see hexadecimal value in my CSV file. But when I open wireshark and look at the Tim...'''
date = "2012-03-30T08:40:00Z"
lastmod = "2012-04-03T10:36:00Z"
weight = 9866
keywords = [ "tshark" ]
aliases = [ "/questions/9866" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark problem](/questions/9866/tshark-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9866-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear friends, I am trying to export output to a csv file with tshark and I would like to export Beacon Timestamp not in a Hex format but in Decimal format. When I am using this method : -e wlan_mgt.fixed.timestamp I see hexadecimal value in my CSV file. But when I open wireshark and look at the Timestamp custome column the value is in Decimal. Please help me to find out what am I doing wrong? Thank you in advance</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '12, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/559f374efd2eaeaafac5616bbec62008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AminGho&#39;s gravatar image" /><p>AminGho<br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AminGho has no accepted answers">0%</span></p></div></div><div id="comments-container-9866" class="comments-container"><span id="9909"></span><div id="comment-9909" class="comment"><div id="post-9909-score" class="comment-score"></div><div class="comment-text"><p>No one Can Help me with this?</p></div><div id="comment-9909-info" class="comment-info"><span class="comment-age">(03 Apr '12, 01:45)</span> AminGho</div></div></div><div id="comment-tools-9866" class="comment-tools"></div><div class="clear"></div><div id="comment-9866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9917"></span>

<div id="answer-container-9917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9917-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't see a way in TShark to change the format of that field from hex to decimal. If you're exporting the file, you might as well use another tool to postprocess the exported file (to rewrite that column into the desired format). I would use <code>awk</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '12, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-9917" class="comments-container"></div><div id="comment-tools-9917" class="comment-tools"></div><div class="clear"></div><div id="comment-9917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

