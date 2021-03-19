+++
type = "question"
title = "Add Sequence number to WIreshark Column"
description = '''Hello, How can i add packets sequence number (BE and LE) to wireshark column? BR Kamran'''
date = "2017-04-08T10:04:00Z"
lastmod = "2017-04-08T10:09:00Z"
weight = 60670
keywords = [ "columns", "wireshark" ]
aliases = [ "/questions/60670" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Add Sequence number to WIreshark Column](/questions/60670/add-sequence-number-to-wireshark-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60670-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, How can i add packets sequence number (BE and LE) to wireshark column? BR Kamran</p></div><div id="question-tags" class="tags-container tags">columns wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '17, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/af235f77f98a216c6c1e00d88f9d52a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kamran&#39;s gravatar image" /><p>Kamran<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kamran has no accepted answers">0%</span></p></div></div><div id="comments-container-60670" class="comments-container"></div><div id="comment-tools-60670" class="comment-tools"></div><div class="clear"></div><div id="comment-60670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60671"></span>

<div id="answer-container-60671" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60671-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What number do you exactly want to add? TCP Sequence, ICMP Echo Request/Reply? In general, find the field in the decode you want to add, right click, "Add as column".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '17, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60671" class="comments-container"><span id="60673"></span><div id="comment-60673" class="comment"><div id="post-60673-score" class="comment-score"></div><div class="comment-text"><p>i was trying to add seq number in separate column for ICMP request/rsespoce. i have added icmp.seq field in filed name and it worked. thank you for your attention<br />
</p></div><div id="comment-60673-info" class="comment-info"><span class="comment-age">(09 Apr '17, 01:35)</span> Kamran</div></div><span id="60843"></span><div id="comment-60843" class="comment"><div id="post-60843-score" class="comment-score"></div><div class="comment-text"><p>i use version 2.2.4 when i create the column with icmp.ident it does not show correctly. when i add icmp.seq and icmp.sec_le ir works correctly as described in the packet</p></div><div id="comment-60843-info" class="comment-info"><span class="comment-age">(15 Apr '17, 07:08)</span> Kamran</div></div><span id="60847"></span><div id="comment-60847" class="comment"><div id="post-60847-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I'll go back and check the release notes to see when this was reworked.</p></div><div id="comment-60847-info" class="comment-info"><span class="comment-age">(15 Apr '17, 11:27)</span> bubbasnmp</div></div></div><div id="comment-tools-60671" class="comment-tools"></div><div class="clear"></div><div id="comment-60671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

