+++
type = "question"
title = "LUA: problem using bit.bxor"
description = '''Hi, I&#x27;m struggling with a problem in a LUA script. I need to XOR a byte with the value 0xa5. The code looks like this:  tvbr = tvb:range(ptr, 1) -- set up a range  local rop_id = tvbr:bytes() -- extract the RopId   if xor_magic_set then  rop_id = bit.bxor(rop_id, 0xa5) -- error occurs here  end  The...'''
date = "2016-02-26T01:36:00Z"
lastmod = "2016-02-27T08:21:00Z"
weight = 50529
keywords = [ "lua" ]
aliases = [ "/questions/50529" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LUA: problem using bit.bxor](/questions/50529/lua-problem-using-bitbxor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50529-score" class="post-score" title="current number of votes">0</div><span id="post-50529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm struggling with a problem in a LUA script. I need to XOR a byte with the value 0xa5. The code looks like this:</p><pre><code>  tvbr = tvb:range(ptr, 1) -- set up a range
  local rop_id = tvbr:bytes() -- extract the RopId

  if xor_magic_set then
    rop_id = bit.bxor(rop_id, 0xa5) -- error occurs here
  end</code></pre><p>The line that extracts the RopId works fine, but the bit.bxor line throws an error:</p><p>Lua Error: [string "C:\Program Files\Wireshark2\plugins\msmapi.lua"]:173: bad argument #1 to 'bxor' (number expected, got userdata)</p><p>How do I convert the extracted byte (rop_id) into a value type that I can XOR? Any advice much appreciated.</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '16, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-50529" class="comments-container"></div><div id="comment-tools-50529" class="comment-tools"></div><div class="clear"></div><div id="comment-50529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50548"></span>

<div id="answer-container-50548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50548-score" class="post-score" title="current number of votes">0</div><span id="post-50548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It should help to use <code>tvbr:uint()</code> instead of <code>tvbr:bytes()</code> when extracting the RopId.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '16, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50548" class="comments-container"><span id="50561"></span><div id="comment-50561" class="comment"><div id="post-50561-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy.</p><p>What I didn't say earlier was that I actually eventually needed to apply the XOR to a block of bytes. I realised that I was mixing tvbs with byte arrays and eventually converted the block of bytes to a byte array (baIn below), which meant I could then do this:</p><pre><code>for i = 0, (baIn:len() - 1) do
  baOut:set_size(i + 1)
  baOut:set_index( i, bit.bxor(baIn:get_index(i), 0xa5) )
end</code></pre><p>Best regards...Paul</p></div><div id="comment-50561-info" class="comment-info"><span class="comment-age">(27 Feb '16, 08:21)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-50548" class="comment-tools"></div><div class="clear"></div><div id="comment-50548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

