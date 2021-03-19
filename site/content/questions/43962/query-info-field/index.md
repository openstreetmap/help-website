+++
type = "question"
title = "Query Info Field"
description = '''When I look in my capture, I see several: SMB2 Create Request File: filename.txt  SMB2 Create Response, Error: STATUS_OBJECT_NAME_NOT_FOUND How can I write a query where the word &quot;Create&quot; is present in the Info field? I can do an ip.addr == 192.168.80.10, but I only want to see the create requests o...'''
date = "2015-07-08T06:36:00Z"
lastmod = "2015-07-08T09:13:00Z"
weight = 43962
keywords = [ "query", "capture-filter", "wireshark" ]
aliases = [ "/questions/43962" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Query Info Field](/questions/43962/query-info-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43962-score" class="post-score" title="current number of votes">0</div><span id="post-43962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I look in my capture, I see several:</p><p>SMB2 Create Request File: filename.txt SMB2 Create Response, Error: STATUS_OBJECT_NAME_NOT_FOUND</p><p>How can I write a query where the word "Create" is present in the Info field? I can do an ip.addr == 192.168.80.10, but I only want to see the create requests or errors, and nothing else.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '15, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/b8872d358b1cfd72253910e0912daf3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kspinnato&#39;s gravatar image" /><p><span>kspinnato</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kspinnato has no accepted answers">0%</span></p></div></div><div id="comments-container-43962" class="comments-container"></div><div id="comment-tools-43962" class="comment-tools"></div><div class="clear"></div><div id="comment-43962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43967"></span>

<div id="answer-container-43967" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43967-score" class="post-score" title="current number of votes">0</div><span id="post-43967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kspinnato has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>smb2.cmd == 5</p><p>For your complete filter: smb2.cmd == 5 &amp;&amp; ip.addr==192.168.80.10</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '15, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-43967" class="comments-container"><span id="43970"></span><div id="comment-43970" class="comment"><div id="post-43970-score" class="comment-score"></div><div class="comment-text"><p>That works perfect! Thanks for helping me out with this filter.</p></div><div id="comment-43970-info" class="comment-info"><span class="comment-age">(08 Jul '15, 09:13)</span> <span class="comment-user userinfo">kspinnato</span></div></div></div><div id="comment-tools-43967" class="comment-tools"></div><div class="clear"></div><div id="comment-43967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

