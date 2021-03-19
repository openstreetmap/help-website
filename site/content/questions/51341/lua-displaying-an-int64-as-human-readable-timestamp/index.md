+++
type = "question"
title = "[LUA] Displaying an int64 as human readable timestamp"
description = '''Hi, within my protocol I have an 8 byte value, int64, which contains the number of microseconds since the epoch. What I would like to do is place this into the tree in a human readable format but I&#x27;m struggling.  This is what I use to display the value of the int64. msg_header:add(buf(12,8),&quot;Timesta...'''
date = "2016-04-01T05:27:00Z"
lastmod = "2016-04-01T08:46:00Z"
weight = 51341
keywords = [ "lua", "timestamp" ]
aliases = [ "/questions/51341" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[LUA\] Displaying an int64 as human readable timestamp](/questions/51341/lua-displaying-an-int64-as-human-readable-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51341-score" class="post-score" title="current number of votes">0</div><span id="post-51341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, within my protocol I have an 8 byte value, int64, which contains the number of microseconds since the epoch. What I would like to do is place this into the tree in a human readable format but I'm struggling.</p><p>This is what I use to display the value of the int64. msg_header:add(buf(12,8),"Timestamp: " .. buf(12,8):le_int64())</p><p>Help would be much appreciated.</p><p>Thanks, Bart</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '16, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/1d2ba9d0b40389d5081701e2a668eafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbart&#39;s gravatar image" /><p><span>sbart</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbart has no accepted answers">0%</span></p></div></div><div id="comments-container-51341" class="comments-container"></div><div id="comment-tools-51341" class="comment-tools"></div><div class="clear"></div><div id="comment-51341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51350"></span>

<div id="answer-container-51350" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51350-score" class="post-score" title="current number of votes">0</div><span id="post-51350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Found my own answer.</p><p>msg_header:add(buf(12,8),"Timestamp: " .. os.date("%x %X",(buf(12,8):le_int64()):tonumber()/1000000) .. "." .. (buf(12,8):le_int64()):tonumber()%1000000)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '16, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/1d2ba9d0b40389d5081701e2a668eafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbart&#39;s gravatar image" /><p><span>sbart</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbart has no accepted answers">0%</span></p></div></div><div id="comments-container-51350" class="comments-container"></div><div id="comment-tools-51350" class="comment-tools"></div><div class="clear"></div><div id="comment-51350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

