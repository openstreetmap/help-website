+++
type = "question"
title = "Extract Pinfo timestamp with better than second precision from Lua?"
description = '''The documentation describes how to access the packet timestamps using pinfo.abs_ts and similar. However it is not clear as to how this time is represented. From looking at the source, it seems to be returned as epoch seconds using lua_nstime_to_sec. Is there a way of getting a more precise timestamp...'''
date = "2014-03-17T11:36:00Z"
lastmod = "2014-03-17T13:00:00Z"
weight = 30897
keywords = [ "lua", "timestamp", "nano", "pinfo" ]
aliases = [ "/questions/30897" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extract Pinfo timestamp with better than second precision from Lua?](/questions/30897/extract-pinfo-timestamp-with-better-than-second-precision-from-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30897-score" class="post-score" title="current number of votes">0</div><span id="post-30897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html">documentation</a> describes how to access the packet timestamps using <code>pinfo.abs_ts</code> and similar. However it is not clear as to how this time is represented. From looking at the <a href="https://github.com/avsej/wireshark/blob/master/epan/wslua/wslua_pinfo.c">source</a>, it seems to be returned as epoch seconds using <code>lua_nstime_to_sec</code>.</p><p>Is there a way of getting a more precise timestamp for the packet, ideally with nanosecond precision, from Lua?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-nano" rel="tag" title="see questions tagged &#39;nano&#39;">nano</span> <span class="post-tag tag-link-pinfo" rel="tag" title="see questions tagged &#39;pinfo&#39;">pinfo</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '14, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/b505e6c822ccf1eaa8d663d9fb28fedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randomphrase&#39;s gravatar image" /><p><span>randomphrase</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randomphrase has no accepted answers">0%</span></p></div></div><div id="comments-container-30897" class="comments-container"></div><div id="comment-tools-30897" class="comment-tools"></div><div class="clear"></div><div id="comment-30897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30898"></span>

<div id="answer-container-30898" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30898-score" class="post-score" title="current number of votes">0</div><span id="post-30898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="randomphrase has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I haven't tried it, but what it should be doing is returning a Lua number with the fractional part representing the nanoseconds. So if the absolute time is 123456 seconds and 789 nanoseconds, when you get <code>pinfo.abs_ts</code> you should be getting back a Lua number of 123456.000000789.</p><p>A Lua number is a double, so it has a fractional component, and <code>lua_nstime_to_sec</code> tries to take advantage of that to give the nanoseconds. (I believe a double has enough precision in the fractional part to handle that correctly, though I could be wrong)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '14, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Mar '14, 11:54</strong> </span></p></div></div><div id="comments-container-30898" class="comments-container"><span id="30899"></span><div id="comment-30899" class="comment"><div id="post-30899-score" class="comment-score"></div><div class="comment-text"><p>Ah yes of course - don't know why I missed something so obvious.</p><p>For future reference, here's what worked for me:</p><pre><code>local secs, frac = math.modf(pinfo.abs_ts)
local timestamp = NSTime(secs, math.modf(frac * 10^9))</code></pre><p>(Possibly could be made more elegant by someone more knowledgable about Lua than I!)</p></div><div id="comment-30899-info" class="comment-info"><span class="comment-age">(17 Mar '14, 12:36)</span> <span class="comment-user userinfo">randomphrase</span></div></div><span id="30901"></span><div id="comment-30901" class="comment"><div id="post-30901-score" class="comment-score"></div><div class="comment-text"><p>There's no reason to do a <code>math.modf()</code> in the second argument to <code>NSTime()</code>. <code>NSTime()</code> will ignore any fractional component in its arguments.</p><p>Really what you're doing there anyway is giving <code>NSTime()</code> three arguments: (1) the <code>secs</code>, (2) the integral number of <code>frac * 10^9</code>, and (3) the fractional number of <code>frac * 10^9</code>. Luckily <code>NSTime()</code> ignores this third argument you're passing, but this might break someday if <code>NSTime()</code> is enhanced to take a third optional argument for something.</p><p>You could also do this instead, though I think your way is clearer and easier to read:</p><pre><code>local timestamp = NSTime(pinfo.abs_ts, select(2,math.modf(pinfo.abs_ts)) * 10^9)</code></pre></div><div id="comment-30901-info" class="comment-info"><span class="comment-age">(17 Mar '14, 12:57)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30902"></span><div id="comment-30902" class="comment"><div id="post-30902-score" class="comment-score"></div><div class="comment-text"><p>But maybe what we really need is for <code>pinfo</code> to provide a way to get the NSTime object as a return value for abs_ts (and the other times). So you don't have to do this shenanigans. :)</p></div><div id="comment-30902-info" class="comment-info"><span class="comment-age">(17 Mar '14, 13:00)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-30898" class="comment-tools"></div><div class="clear"></div><div id="comment-30898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

