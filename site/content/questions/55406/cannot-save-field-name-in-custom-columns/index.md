+++
type = "question"
title = "Cannot save Field Name in custom Columns"
description = '''I have created a Host column. I right-click on the column &amp;gt; Select Column Preferences &amp;gt; Select Columns &amp;gt; Add a new Column &amp;gt; Title == Host &amp;gt; Type == Custom &amp;gt; Field Name == http.host The Field Name is not saved. As soon as I click out of the window the entry http.host is not saved. P...'''
date = "2016-09-08T19:50:00Z"
lastmod = "2016-09-10T09:52:00Z"
weight = 55406
keywords = [ "field", "name", "columns", "custom" ]
aliases = [ "/questions/55406" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot save Field Name in custom Columns](/questions/55406/cannot-save-field-name-in-custom-columns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55406-score" class="post-score" title="current number of votes">0</div><span id="post-55406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have created a Host column. I right-click on the column &gt; Select Column Preferences &gt; Select Columns &gt; Add a new Column &gt; Title == Host &gt; Type == Custom &gt; Field Name == http.host</p><p>The Field Name is not saved. As soon as I click out of the window the entry http.host is not saved. Please help!</p><p>Wireshark macOS 10.6 and later Intel 64-bit .dmg Version 2.2.0 (v2.2.0-0-g5368c50 from master-2.2)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '16, 19:50</strong></p><img src="https://secure.gravatar.com/avatar/283bf8b826363521879a48cbc7f9f812?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="duncan_testlio&#39;s gravatar image" /><p><span>duncan_testlio</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="duncan_testlio has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Sep '16, 23:19</strong> </span></p></div></div><div id="comments-container-55406" class="comments-container"><span id="55411"></span><div id="comment-55411" class="comment"><div id="post-55411-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark is this? Please edit your question adding the contents of Help -&gt; About Wireshark.</p></div><div id="comment-55411-info" class="comment-info"><span class="comment-age">(08 Sep '16, 23:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="55457"></span><div id="comment-55457" class="comment"><div id="post-55457-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb, I have updated the question to contain the information regarding my platform and what version I am on. Thank you very much for helping me to narrow this issue down</p></div><div id="comment-55457-info" class="comment-info"><span class="comment-age">(09 Sep '16, 23:20)</span> <span class="comment-user userinfo">duncan_testlio</span></div></div></div><div id="comment-tools-55406" class="comment-tools"></div><div class="clear"></div><div id="comment-55406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55461"></span>

<div id="answer-container-55461" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55461-score" class="post-score" title="current number of votes">2</div><span id="post-55461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="duncan_testlio has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Om Windows if I complete the field by typing the complete entry or by selecting the context menu entry and then either hitting "Enter" or "TAB" then the field contents are as expected.</p><p>If neither of these work on macOS, then please raise an entry at the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '16, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55461" class="comments-container"><span id="55464"></span><div id="comment-55464" class="comment"><div id="post-55464-score" class="comment-score"></div><div class="comment-text"><p>Thank you Grahamb! Tabbing out of the field saved my entry as expected. Previously I was clicking out of the field which resulted in the issue listed in the question above</p></div><div id="comment-55464-info" class="comment-info"><span class="comment-age">(10 Sep '16, 09:52)</span> <span class="comment-user userinfo">duncan_testlio</span></div></div></div><div id="comment-tools-55461" class="comment-tools"></div><div class="clear"></div><div id="comment-55461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

