+++
type = "question"
title = "pls point example source file of dual heuristic/normal dissector"
description = '''I want an example where dual heuristic/normal dissector is used in /epan/dissectors/'''
date = "2012-06-05T17:47:00Z"
lastmod = "2012-06-05T23:32:00Z"
weight = 11698
keywords = [ "plugin", "wireshark" ]
aliases = [ "/questions/11698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pls point example source file of dual heuristic/normal dissector](/questions/11698/pls-point-example-source-file-of-dual-heuristicnormal-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11698-score" class="post-score" title="current number of votes">0</div><span id="post-11698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want an example where dual heuristic/normal dissector is used in /epan/dissectors/</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '12, 17:47</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p><span>yogeshg</span><br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11698" class="comments-container"></div><div id="comment-tools-11698" class="comment-tools"></div><div class="clear"></div><div id="comment-11698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11699"></span>

<div id="answer-container-11699" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11699-score" class="post-score" title="current number of votes">0</div><span id="post-11699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here are a couple of examples:</p><ul><li><a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-ppp.c?revision=42989&amp;view=markup">packet-ppp.c</a></li><li><a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-wol.c?revision=42632&amp;view=markup">packet-wol.c</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '12, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11699" class="comments-container"><span id="11705"></span><div id="comment-11705" class="comment"><div id="post-11705-score" class="comment-score"></div><div class="comment-text"><p>I want my dissector to get called if my src mac or dest mac is of some specific pattern , for that i am using heuristic dissector for eth but then tvb will point to eth payload i suppose and instead i want dissection of http payload , so for this i need to use these dual dissectors right ? , just confirm</p></div><div id="comment-11705-info" class="comment-info"><span class="comment-age">(05 Jun '12, 23:32)</span> <span class="comment-user userinfo">yogeshg</span></div></div></div><div id="comment-tools-11699" class="comment-tools"></div><div class="clear"></div><div id="comment-11699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

