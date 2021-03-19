+++
type = "question"
title = "How can we implement exception handling using Lua?"
description = '''If we want to develop our own plugin using Lua. How we can use exception handling in that?'''
date = "2015-03-13T02:14:00Z"
lastmod = "2015-03-14T11:40:00Z"
weight = 40532
keywords = [ "lua" ]
aliases = [ "/questions/40532" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can we implement exception handling using Lua?](/questions/40532/how-can-we-implement-exception-handling-using-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40532-score" class="post-score" title="current number of votes">0</div><span id="post-40532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If we want to develop our own plugin using Lua. How we can use exception handling in that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '15, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p><span>ankit</span><br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '15, 11:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-40532" class="comments-container"></div><div id="comment-tools-40532" class="comment-tools"></div><div class="clear"></div><div id="comment-40532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40563"></span>

<div id="answer-container-40563" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40563-score" class="post-score" title="current number of votes">1</div><span id="post-40563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To catch Lua exceptions, use <a href="http://www.lua.org/manual/5.2/manual.html#pdf-pcall"><code>pcall</code></a> as described in <a href="http://www.lua.org/pil/8.4.html">Lua docs</a> (copied here):</p><pre><code>If you need to handle errors in Lua, you should use the pcall function (protected call) to encapsulate your code.

Suppose you want to run a piece of Lua code and to catch any error raised while running that code. Your first step is to encapsulate that piece of code in a function; let us call it foo:

    function foo ()
        ...
      if unexpected_condition then error() end
        ...
      print(a[i])    -- potential error: `a&#39; may not be a table
        ...
    end

Then, you call foo with pcall:

    if pcall(foo) then
      -- no errors while running `foo&#39;
      ...
    else
      -- `foo&#39; raised an error: take appropriate actions
      ...
    end

Of course, you can call pcall with an anonymous function:

    if pcall(function () ... end) then ...
    else ...

The pcall function calls its first argument in protected mode, so that it catches any errors while the function is running. If there are no errors, pcall returns true, plus any values returned by the call. Otherwise, it returns false, plus the error message.

Despite its name, the error message does not have to be a string. Any Lua value that you pass to error will be returned by pcall:

    local status, err = pcall(function () error({code=121}) end)
    print(err.code)  --&gt;  121

These mechanisms provide all we need to do exception handling in Lua. We throw an exception with error and catch it with pcall. The error message identifies the kind or error.
</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '15, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-40563" class="comments-container"></div><div id="comment-tools-40563" class="comment-tools"></div><div class="clear"></div><div id="comment-40563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

