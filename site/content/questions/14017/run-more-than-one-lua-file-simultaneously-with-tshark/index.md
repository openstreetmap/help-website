+++
type = "question"
title = "run more than one Lua file simultaneously with tshark"
description = '''Is it possible to run more than one Lua file at the same time with tshark? Can you provide an example?'''
date = "2012-09-04T02:12:00Z"
lastmod = "2012-09-04T21:44:00Z"
weight = 14017
keywords = [ "lua" ]
aliases = [ "/questions/14017" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [run more than one Lua file simultaneously with tshark](/questions/14017/run-more-than-one-lua-file-simultaneously-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14017-score" class="post-score" title="current number of votes">0</div><span id="post-14017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to run more than one Lua file at the same time with tshark? Can you provide an example?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '12, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p><span>Leena</span><br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Sep '12, 21:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-14017" class="comments-container"><span id="14051"></span><div id="comment-14051" class="comment"><div id="post-14051-score" class="comment-score">1</div><div class="comment-text"><p>I assume you mistakenly tagged this question with <code>luainterface</code> (i.e., <a href="http://code.google.com/p/luainterface/">LuaInterface</a>), which is a Lua bridge to .NET, allowing one to instantiate CLR objects and use them in Lua.</p></div><div id="comment-14051-info" class="comment-info"><span class="comment-age">(04 Sep '12, 21:44)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-14017" class="comment-tools"></div><div class="clear"></div><div id="comment-14017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14052"></span>

<div id="answer-container-14052" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14052-score" class="post-score" title="current number of votes">1</div><span id="post-14052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leena has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, the Lua interpreter cannot run multiple Lua scripts simultaneously as it's single-threaded.</p><p>(If you explain your end goal, perhaps we can offer a better solution.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 21:44</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-14052" class="comments-container"></div><div id="comment-tools-14052" class="comment-tools"></div><div class="clear"></div><div id="comment-14052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

