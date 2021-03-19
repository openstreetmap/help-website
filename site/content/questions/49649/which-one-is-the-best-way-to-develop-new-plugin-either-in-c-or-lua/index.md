+++
type = "question"
title = "Which one is the best way to develop new plugin either in C or LUA."
description = '''I want to develop my new plugin. But I am in ambiguity either to use C or lua. Because what I have seen in past, If i choose C, It will increase my performance but it is little bit hectic to write whole plugin in C. On the other way around. If I choose LUA. It is easy to write whole plugin in LUA. b...'''
date = "2016-01-30T23:07:00Z"
lastmod = "2016-01-31T19:33:00Z"
weight = 49649
keywords = [ "lua", "c", "wireshark", "plugin" ]
aliases = [ "/questions/49649" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Which one is the best way to develop new plugin either in C or LUA.](/questions/49649/which-one-is-the-best-way-to-develop-new-plugin-either-in-c-or-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49649-score" class="post-score" title="current number of votes">0</div><span id="post-49649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to develop my new plugin. But I am in ambiguity either to use C or lua. Because what I have seen in past, If i choose C, It will increase my performance but it is little bit hectic to write whole plugin in C. On the other way around. If I choose LUA. It is easy to write whole plugin in LUA. but it has major performance issues. So my question is like which one is the best way to make new plugin in very effective manner???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-c" rel="tag" title="see questions tagged &#39;c&#39;">c</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '16, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p><span>ankit</span><br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-49649" class="comments-container"></div><div id="comment-tools-49649" class="comment-tools"></div><div class="clear"></div><div id="comment-49649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49653"></span>

<div id="answer-container-49653" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49653-score" class="post-score" title="current number of votes">1</div><span id="post-49653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ankit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's the tradeoff between development effort and subsequent use afterwards. Generally you'll develop a dissector once, with a little subsequent maintenance, but it will be used many times, possibly by many people, so improving performance by using C will be an effort multiplier.</p><p>It's also easier to distribute a C dissector, just create a new package installer, and also easier to contribute back to the Wireshark project as we don't really have a distribution mechanism for lua dissectors.</p><p>So, my advice would be that if you have the capabilities to develop in C, then use that. If you do use C, and you can release the code to the Wireshark project, then do so as it will then be maintained and distributed by the project itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '16, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49653" class="comments-container"><span id="49673"></span><div id="comment-49673" class="comment"><div id="post-49673-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@grahamb</span>. I got your point.</p></div><div id="comment-49673-info" class="comment-info"><span class="comment-age">(31 Jan '16, 19:33)</span> <span class="comment-user userinfo">ankit</span></div></div></div><div id="comment-tools-49653" class="comment-tools"></div><div class="clear"></div><div id="comment-49653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

