+++
type = "question"
title = "Dynamically create protofields"
description = '''I would like to add protofields to my dissector so it is easier to filter on. However, the data for the dissector is contained in multiple lua files (as tables). I have the following code: t = myproto.fields for i in ipairs(tablename) do  t.i = protofield.string(blahblah) end  But this is not workin...'''
date = "2014-11-24T07:12:00Z"
lastmod = "2014-12-23T09:35:00Z"
weight = 38101
keywords = [ "lua" ]
aliases = [ "/questions/38101" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dynamically create protofields](/questions/38101/dynamically-create-protofields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38101-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to add protofields to my dissector so it is easier to filter on. However, the data for the dissector is contained in multiple lua files (as tables). I have the following code:</p><pre><code>t = myproto.fields
for i in ipairs(tablename) do
   t.i = protofield.string(blahblah)
end</code></pre><p>But this is not working. I've tried concatenating the i variable in a number of ways (t..i, t[i], etc) but it is not working. Is it possible to create dynamic variable names in lua like this?</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '14, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/40aae7ab1a30c4c2d4bbece83599857a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hls&#39;s gravatar image" /><p>hls<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hls has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Dec '14, 01:20</p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-38101" class="comments-container"></div><div id="comment-tools-38101" class="comment-tools"></div><div class="clear"></div><div id="comment-38101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38686"></span>

<div id="answer-container-38686" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38686-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to get my code working, doing a combination of trial and error, as well as global tables.</p><pre><code>tbl = string.upper(string.sub(file, 1, -5))
    _G[&quot;t&quot;..tbl] = {}</code></pre><p>I was then able to use that global variable to add a protofield string</p><pre><code>_G[&quot;t&quot;..tbl][i] = ProtoField.string(blahblah)</code></pre><p>and finally, use that table to add to the fields table.</p><pre><code>table.insert(myproto.fields,i,_G[&quot;t&quot;..tbl][i])</code></pre><p>Not the prettiest code, but it's currently working</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '14, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/40aae7ab1a30c4c2d4bbece83599857a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hls&#39;s gravatar image" /><p>hls<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hls has one accepted answer">100%</span></p></div></div><div id="comments-container-38686" class="comments-container"></div><div id="comment-tools-38686" class="comment-tools"></div><div class="clear"></div><div id="comment-38686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38676"></span>

<div id="answer-container-38676" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38676-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What exact error message(s) are you getting?</p><p>Lua does indeed support variables for table indexes/keys, and the correct syntax would be:</p><pre><code>t[i] = ProtoField.string(blahblah)</code></pre><p>...<em>but</em> it's <strong>not</strong> going to work unless you did other stuff you're not showing in your question's Lua snippet. For example, "<code>t = myproto.fields</code>" won't return a table unless you've previously set <code>myproto.fields</code> to a table I believe; so using <code>"t[i]</code>" won't work because <code>t</code> isn't a Lua table.</p><p>You probably want to do this instead:</p><pre><code>local t = {}
for i in ipairs(tablename) do
    t[i] = ProtoField.string(blahblah)
end
myproto.fields = t</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '14, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-38676" class="comments-container"></div><div id="comment-tools-38676" class="comment-tools"></div><div class="clear"></div><div id="comment-38676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

