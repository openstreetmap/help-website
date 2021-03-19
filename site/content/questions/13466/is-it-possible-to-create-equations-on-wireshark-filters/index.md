+++
type = "question"
title = "IS it possible to create equations on wireshark filters"
description = '''I&#x27;d like if it is possible to use wireshark filter to do equations.  For example. If I have two fields with timestamps on a frame. Can I gete the difference between then, or add on to another? something like that?  thanks in advance. '''
date = "2012-08-08T05:41:00Z"
lastmod = "2012-08-08T06:24:00Z"
weight = 13466
keywords = [ "filter", "equation", "wireshark" ]
aliases = [ "/questions/13466" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IS it possible to create equations on wireshark filters](/questions/13466/is-it-possible-to-create-equations-on-wireshark-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13466-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like if it is possible to use wireshark filter to do equations. For example. If I have two fields with timestamps on a frame. Can I gete the difference between then, or add on to another? something like that? thanks in advance.</p></div><div id="question-tags" class="tags-container tags">filter equation wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '12, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/bfdf3a1cf8df2e1bf4988beaf588d9d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="higorsilvacomh&#39;s gravatar image" /><p>higorsilvacomh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="higorsilvacomh has no accepted answers">0%</span></p></div></div><div id="comments-container-13466" class="comments-container"></div><div id="comment-tools-13466" class="comment-tools"></div><div class="clear"></div><div id="comment-13466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13468"></span>

<div id="answer-container-13468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13468-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filters are used to either:</p><ol><li>Select if a frame from the selected interface(s) is written to the capture output sink. These are called <strong>capture</strong> filters.</li><li>Select if a frame from the capture file is displayed in the Wireshark GUI. These are called <strong>display</strong> filters.</li></ol><p>In both these cases the filter expressions return a yes/no that indicates if the frame passes the filter and should be captured/displayed as appropriate and do not return any other useful value in that respect.</p><p>If you wish to calculate inter-frame differences you'll have to resort to a tap or scripting the output of tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '12, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13468" class="comments-container"></div><div id="comment-tools-13468" class="comment-tools"></div><div class="clear"></div><div id="comment-13468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

