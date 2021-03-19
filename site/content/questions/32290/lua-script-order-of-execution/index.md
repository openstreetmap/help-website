+++
type = "question"
title = "Lua script order of execution"
description = '''What controls the order in which Lua scripts get executed? Scripts in the global configuration plugins directory get executed first. Scripts in the local (user) configuration plugins directory get executed next. Scripts specified from the command line (e.g. with -X lua_script:somescript.lua) get exe...'''
date = "2014-04-29T07:39:00Z"
lastmod = "2014-04-29T11:46:00Z"
weight = 32290
keywords = [ "lua", "execution", "order", "script" ]
aliases = [ "/questions/32290" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lua script order of execution](/questions/32290/lua-script-order-of-execution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32290-score" class="post-score" title="current number of votes">0</div><span id="post-32290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What controls the order in which Lua scripts get executed?</p><p>Scripts in the global configuration plugins directory get executed first.</p><p>Scripts in the local (user) configuration plugins directory get executed next.</p><p>Scripts specified from the command line (e.g. with -X lua_script:somescript.lua) get executed last. When multiple scripts are passed from the command line using -X, they are executed in the order they appear on the command line.</p><p>What controls the order of execution of scripts when multiple scripts exist in, say, the local plugins directory? With the little experimentation I've done (in Linux only) it appears to be reverse alphabetical by script file name. However, I didn't experiment to see if there is another factor (e.g. date created or modified.) And I haven't experimented on a windows platform yet. I have not searched the source code yet...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-execution" rel="tag" title="see questions tagged &#39;execution&#39;">execution</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '14, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/cc0c91c9249fabb764686944218f0fc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="needaclone&#39;s gravatar image" /><p><span>needaclone</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="needaclone has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Apr '14, 11:39</strong> </span></p></div></div><div id="comments-container-32290" class="comments-container"></div><div id="comment-tools-32290" class="comment-tools"></div><div class="clear"></div><div id="comment-32290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32295"></span>

<div id="answer-container-32295" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32295-score" class="post-score" title="current number of votes">1</div><span id="post-32295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The answer seems to be that there is no guaranteed order per se.</p><p>Under the hood, Wireshark uses the glib function g_dir_read_name() to run through all the files in a given directory, subsequently loading all the .lua scripts. Online documentation for g_dir_read_name() at developer.gnome.org says "The order of entries returned from this function is not defined, and may vary by file system or other operating-system dependent factors."</p><p>So, there's no guarantee the the order of execution will be the same across OS or filesystem types or versions.</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '14, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/cc0c91c9249fabb764686944218f0fc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="needaclone&#39;s gravatar image" /><p><span>needaclone</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="needaclone has no accepted answers">0%</span></p></div></div><div id="comments-container-32295" class="comments-container"></div><div id="comment-tools-32295" class="comment-tools"></div><div class="clear"></div><div id="comment-32295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

