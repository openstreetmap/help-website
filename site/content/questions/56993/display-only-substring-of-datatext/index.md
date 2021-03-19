+++
type = "question"
title = "Display only substring of data.text"
description = '''Hello, I did add a column data.text and enabled it (https://ask.wireshark.org/questions/14011/customcolumn-datatext), so far the package content is displayed fine.  Now I would like to only show only certain characterfields there, for example the first ten chars, or char 5 to 8. Is this possible? I ...'''
date = "2016-11-04T12:27:00Z"
lastmod = "2016-11-07T02:16:00Z"
weight = 56993
keywords = [ "display" ]
aliases = [ "/questions/56993" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Display only substring of data.text](/questions/56993/display-only-substring-of-datatext)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56993-score" class="post-score" title="current number of votes">0</div><span id="post-56993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I did add a column data.text and enabled it (<a href="https://ask.wireshark.org/questions/14011/customcolumn-datatext),">https://ask.wireshark.org/questions/14011/customcolumn-datatext),</a> so far the package content is displayed fine.</p><p>Now I would like to only show only certain characterfields there, for example the first ten chars, or char 5 to 8. Is this possible? I tried data.text[10] but it did not work</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '16, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/45868ff9de38e8974af97d50e87948dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anothersharky&#39;s gravatar image" /><p><span>anothersharky</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anothersharky has no accepted answers">0%</span></p></div></div><div id="comments-container-56993" class="comments-container"></div><div id="comment-tools-56993" class="comment-tools"></div><div class="clear"></div><div id="comment-56993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57043"></span>

<div id="answer-container-57043" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57043-score" class="post-score" title="current number of votes">0</div><span id="post-57043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="anothersharky has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is not possible out-of-the-box. You could however use a <a href="https://wiki.wireshark.org/Lua">LUA</a> script to extract portions of a field and put the result in a new field. Or you could file an "Enhancement Request" at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> for this functionality and hope that some developer finds interest in developing this functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Nov '16, 02:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-57043" class="comments-container"></div><div id="comment-tools-57043" class="comment-tools"></div><div class="clear"></div><div id="comment-57043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

