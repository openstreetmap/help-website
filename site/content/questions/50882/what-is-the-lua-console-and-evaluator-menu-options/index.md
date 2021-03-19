+++
type = "question"
title = "what is the LUA console and evaluator menu options?"
description = '''i believe these are new features added in wireshark 2, but i don&#x27;t know how to use them exactly i was hoping the console would at least print out any messages i use with print function in a dissector , but it does not. '''
date = "2016-03-14T02:38:00Z"
lastmod = "2016-03-15T11:15:00Z"
weight = 50882
keywords = [ "lua", "evaluator", "console" ]
aliases = [ "/questions/50882" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [what is the LUA console and evaluator menu options?](/questions/50882/what-is-the-lua-console-and-evaluator-menu-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50882-score" class="post-score" title="current number of votes">1</div><span id="post-50882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i believe these are new features added in wireshark 2, but i don't know how to use them exactly i was hoping the console would at least print out any messages i use with print function in a dissector , but it does not.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-evaluator" rel="tag" title="see questions tagged &#39;evaluator&#39;">evaluator</span> <span class="post-tag tag-link-console" rel="tag" title="see questions tagged &#39;console&#39;">console</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '16, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/a862f54e9cb5d1cc5dc2b83084555ebd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EXM1110b&#39;s gravatar image" /><p><span>EXM1110b</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EXM1110b has no accepted answers">0%</span></p></div></div><div id="comments-container-50882" class="comments-container"></div><div id="comment-tools-50882" class="comment-tools"></div><div class="clear"></div><div id="comment-50882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50937"></span>

<div id="answer-container-50937" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50937-score" class="post-score" title="current number of votes">1</div><span id="post-50937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm guessing that you're on Windows?</p><p>From the <a href="https://wiki.wireshark.org/Lua">Wireshark Lua wiki page</a>:</p><p><em>Please note: On Windows, you may not see any output when running Lua scripts in Wireshark. If the console window is enabled it will be opened <strong>after</strong> the lua engine is loaded. This does not affect TShark, since it is a console program.</em></p><p>That said, if you open the <code>Lua -&gt; Console</code> and the <code>Lua -&gt; Evaluate</code> dialogs, you can force your dissector to be loaded by typing the following and then clicking on <code>Evaluate</code>:</p><pre><code>dofile(&quot;path/to/file.lua&quot;)</code></pre><p>You should then see your output in the Lua console. Note that you will almost certainly need to keep your Lua dissector in a directory other than <code>%APPDATA%\Wireshark\plugins\</code> until you're done testing it to avoid having Wireshark automatically load it when it starts up, because in almost all but the simplest of cases can it be loaded/run more than once - something like the <code>hello.lua</code> example being one that can be loaded more than once without a problem.</p><p>The Qt Wireshark version allows reloading of Lua dissectors via <code>Analyze -&gt; Reload Lua Plugins</code>; however, that affects <em>all</em> plugins and the Qt version is missing the <code>Tools -&gt; Lua</code> sub-menu altogether, so I don't know how you could achieve this with the Qt version.</p><p>Final note: Initially I was able to get Lua debug printed to the Lua Console, but after a bit of testing, it stopped for some unknown reason. I was at least able to open a console via <code>Edit -&gt; Preferences -&gt; Open a console window -&gt; Always (debugging)</code> and obtain the Lua debug output that way instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '16, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-50937" class="comments-container"></div><div id="comment-tools-50937" class="comment-tools"></div><div class="clear"></div><div id="comment-50937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

