+++
type = "question"
title = "View Lua dissector&#x27;s console output on Windows 10"
description = '''This is kind of a newbie question: I am writing a custom dissector with Lua. For debugging, I need to print to the console using Lua&#x27;s print() function. Under Linux, I can see this output on the console if I start Wireshark from the console. How can I see that output when developing on Windows 10 an...'''
date = "2016-11-18T07:50:00Z"
lastmod = "2017-03-08T05:46:00Z"
weight = 57448
keywords = [ "debug", "lua", "dissector", "console" ]
aliases = [ "/questions/57448" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [View Lua dissector's console output on Windows 10](/questions/57448/view-lua-dissectors-console-output-on-windows-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57448-score" class="post-score" title="current number of votes">0</div><span id="post-57448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is kind of a newbie question: I am writing a custom dissector with Lua. For debugging, I need to print to the console using Lua's print() function. Under Linux, I can see this output on the console if I start Wireshark from the console. How can I see that output when developing on Windows 10 and launching Wireshark from a cmd shell?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-console" rel="tag" title="see questions tagged &#39;console&#39;">console</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '16, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/00a96bd28fd02417186122229a517000?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_oppermann&#39;s gravatar image" /><p><span>patrick_oppe...</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_oppermann has no accepted answers">0%</span></p></div></div><div id="comments-container-57448" class="comments-container"></div><div id="comment-tools-57448" class="comment-tools"></div><div class="clear"></div><div id="comment-57448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57449"></span>

<div id="answer-container-57449" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57449-score" class="post-score" title="current number of votes">1</div><span id="post-57449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="patrick_oppermann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure if this works for Lua, but in general, Preferences -&gt; Advanced -&gt; gui.console_open. Modify the setting to be other than NEVER.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '16, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57449" class="comments-container"><span id="59924"></span><div id="comment-59924" class="comment"><div id="post-59924-score" class="comment-score"></div><div class="comment-text"><p>Cool, thank you for this hint, however, the GUI console does not display any of my log output. I ended up using the Lua console (Tools -&gt; Lua -&gt; Console) that I can write to using the info() and warn() functions.</p></div><div id="comment-59924-info" class="comment-info"><span class="comment-age">(08 Mar '17, 05:46)</span> <span class="comment-user userinfo">patrick_oppe...</span></div></div></div><div id="comment-tools-57449" class="comment-tools"></div><div class="clear"></div><div id="comment-57449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

