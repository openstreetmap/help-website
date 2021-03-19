+++
type = "question"
title = "Dissect data using Lua post-dissector"
description = '''I have an existing dissector that ends up leaving some of the payload of the packet undissected. The remaining bytes are handled by the generic &quot;data&quot; dissector, and are in a field simply called &quot;data.data&quot;. I would like to use Lua to play around with dissecting these bytes. Reading around, it would...'''
date = "2013-10-21T06:32:00Z"
lastmod = "2013-10-22T08:21:00Z"
weight = 26247
keywords = [ "lua", "postdissector" ]
aliases = [ "/questions/26247" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissect data using Lua post-dissector](/questions/26247/dissect-data-using-lua-post-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26247-score" class="post-score" title="current number of votes">0</div><span id="post-26247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an existing dissector that ends up leaving some of the payload of the packet undissected. The remaining bytes are handled by the generic "data" dissector, and are in a field simply called "data.data". I would like to use Lua to play around with dissecting these bytes. Reading around, it would appear that writing a post-dissector is the easiest way to achieve this. I am relatively new to Lua, but have copied some of the post-dissector examples.</p><p>I think I need to get the bytes from the data.data field as a TVB, then start processing them from there. However, the following code causes Wireshark (nightly, from last week) to crash:</p><pre><code>-- test
local TestDissector = Proto(&quot;testdissect&quot;, &quot;Test LUA dissector&quot;)
register_postdissector(TestDissector)

-- fields to be read
data_f = Field.new(&quot;data.data&quot;)
function TestDissector.dissector(tvb, pinfo, tree)
  local data = data_f()
  local datatvb
  if data then
    datatvb = data.range
    -- dissect bytes in datatvb here
  end
end</code></pre><p>Removing the line where datatvb is used caused Wireshark to stop crashing (but the dissector does nothing). Is this the right way to access the bytes in the data.data field? Is the crashing a bug in Wireshark or my post-dissector?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '13, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/5102bde49a023c2cdbbdffc06ffefbb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan&#39;s gravatar image" /><p><span>Alan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan has no accepted answers">0%</span></p></div></div><div id="comments-container-26247" class="comments-container"></div><div id="comment-tools-26247" class="comment-tools"></div><div class="clear"></div><div id="comment-26247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26250"></span>

<div id="answer-container-26250" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26250-score" class="post-score" title="current number of votes">0</div><span id="post-26250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think a post dissector will help here, as the data has already been processed by the 'data' dissector.</p><p>I think a chained dissector is what you need. First you register the Lua dissector for the same protocol/port, then you call the original dissector (the one that leaves a few bytes). What is left undissected, can then be handled in your Lua dissector.</p><p>There is a simple example of a chained dissector here: <code>http://delog.wordpress.com/2010/09/27/create-a-wireshark-dissector-in-lua/</code></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Oct '13, 06:46</strong> </span></p></div></div><div id="comments-container-26250" class="comments-container"><span id="26287"></span><div id="comment-26287" class="comment"><div id="post-26287-score" class="comment-score">1</div><div class="comment-text"><p>Thanks for the suggestion. However, while I was glancing in the source code for the dissector in question to work out how a chained dissector might might, I discovered that there is a dissector table that it uses to decide how to process the payload bytes. In my specific case, hooking into the dissector table seems to be the right way - in the general case, it looks like a chained dissector might be right.</p></div><div id="comment-26287-info" class="comment-info"><span class="comment-age">(22 Oct '13, 08:21)</span> <span class="comment-user userinfo">Alan</span></div></div></div><div id="comment-tools-26250" class="comment-tools"></div><div class="clear"></div><div id="comment-26250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

