+++
type = "question"
title = "Lua behaviour has changed sometime since Wireshark 1.8.7"
description = '''I just upgraded Wireshark from 1.8.7 to the latest stable version (1.12.2) on my Windows machine. The Lua engine now behaves differently, rendering my plugin dissectors inoperative. I have three dissectors, each in a separate .lua source file, that make use of some common, global, variables that are...'''
date = "2014-12-09T09:05:00Z"
lastmod = "2014-12-12T05:51:00Z"
weight = 38497
keywords = [ "lua" ]
aliases = [ "/questions/38497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lua behaviour has changed sometime since Wireshark 1.8.7](/questions/38497/lua-behaviour-has-changed-sometime-since-wireshark-187)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38497-score" class="post-score" title="current number of votes">0</div><span id="post-38497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just upgraded Wireshark from 1.8.7 to the latest stable version (1.12.2) on my Windows machine.</p><p>The Lua engine now behaves differently, rendering my plugin dissectors inoperative. I have three dissectors, each in a separate .lua source file, that make use of some common, global, variables that are declared in a fourth .lua source file. All of these sources are placed in my %APPDATA%\Roaming\Wireshark\plugins directory.</p><p>After the Lua engine reads all these sources in, all non-local entities declared in any file USED TO BE ACCESSIBLE from any function subsequently run (even if that function were defined in a different source file to the entity's declaration).</p><p>Are individual .lua source files now treated as separate namespaces (effectively making all declarations local to their containing file)?</p><p>Is there some way to restore the ability to declare entities that can be visible from functions in other sources?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '14, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/2d11f8af3e0ab84f60eb3e8b76f8161c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tony%20Oliver&#39;s gravatar image" /><p><span>Tony Oliver</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tony Oliver has no accepted answers">0%</span></p></div></div><div id="comments-container-38497" class="comments-container"></div><div id="comment-tools-38497" class="comment-tools"></div><div class="clear"></div><div id="comment-38497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38541"></span>

<div id="answer-container-38541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38541-score" class="post-score" title="current number of votes">1</div><span id="post-38541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, a long time ago the loading of plugins was changed to be scoped to a separate environment for each plugin file, to prevent clobbering of variables if people forgot to make their variables local.</p><p>To handle your use-case, I think you have two options:</p><ol><li><p>In the file that declares your global variables, declare them explicitly as global variables by putting them in the global table. For example, like this:</p><pre><code> _G[&quot;myVariable1&quot;] = true
 _G[&quot;myVariable2&quot;] = 42
 -- or this syntax
 _G.myVariable3 = false
 _G.myVariable4 = &quot;foobar&quot;</code></pre></li><li><p>Or, have Wireshark only load the one plugin that declares the common global variables, and in that plugin use <code>dofile()</code> or load <code>file()</code> to load all the other plugins. That way they're all loaded into the same environment.</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '14, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-38541" class="comments-container"><span id="38542"></span><div id="comment-38542" class="comment"><div id="post-38542-score" class="comment-score"></div><div class="comment-text"><p>Oh, and I suppose a third option is to have the Lua plugin that declares the global variables change its environment to be the global one. Unfortunately the way this is done is different for Lua 5.1 vs. 5.2, and Wireshark supports both... so if you wanted to support both for your plugin you'd have to check the Lua version first and then do it the appropriate way - this can be done, since there is a global variable for the Lua version (<code>_VERSION</code> if I recall right); so you'd use <code>setfenv()</code> if it's 5.1, and <code>debug.setupvalue()</code> if it's 5.2 or greater.</p></div><div id="comment-38542-info" class="comment-info"><span class="comment-age">(12 Dec '14, 05:51)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-38541" class="comment-tools"></div><div class="clear"></div><div id="comment-38541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

