+++
type = "question"
title = "A way to highlight disjoint bytes simultaneously through Lua?"
description = '''I&#x27;ve asked this before, but didn&#x27;t get any answers. This might be impossible to do. For my dissector, some tree items have the corresponding value stored in two, not continuous parts. For example, I have this chunk of a buffer: 1a2b3c4d. The first and last byte combined is the value I need, so 1a4d....'''
date = "2014-03-28T12:41:00Z"
lastmod = "2014-04-03T09:07:00Z"
weight = 31251
keywords = [ "lua" ]
aliases = [ "/questions/31251" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [A way to highlight disjoint bytes simultaneously through Lua?](/questions/31251/a-way-to-highlight-disjoint-bytes-simultaneously-through-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31251-score" class="post-score" title="current number of votes">0</div><span id="post-31251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've asked this before, but didn't get any answers. This might be impossible to do.</p><p>For my dissector, some tree items have the corresponding value stored in two, not continuous parts.</p><p>For example, I have this chunk of a buffer: 1a2b3c4d. The first and last byte combined is the value I need, so 1a4d. I can calculate this value and add a tree item to represent it. But I don't know how to get only the bytes 1a and 4d highlighted, and leaving the middle two bytes alone, when clicking on this tree item.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '14, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Mar '14, 16:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-31251" class="comments-container"></div><div id="comment-tools-31251" class="comment-tools"></div><div class="clear"></div><div id="comment-31251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="31255"></span>

<div id="answer-container-31255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31255-score" class="post-score" title="current number of votes">0</div><span id="post-31255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should be able to use <code>proto_tree_add_uint</code> for this, since you can already compute your value.<br />
Using your example, you'd make a header field such as this:</p><pre><code>{&amp;hf_myfield, {&quot;My Field&quot;, &quot;myproto.myfield&quot;, FT_UINT32, BASE_HEX, NULL, 0xFF0000FF, &quot;My Field&quot;, HFILL}}</code></pre>Then, in your <code>dissect_myproto</code>...<pre><code>   //...
   value = compute_myfield_value(tvb, offset); //or however you want to do this
   proto_tree_add_uint(tree, hf_myfield, tvb, offset, 4, value);
   //...</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '14, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-31255" class="comments-container"><span id="31256"></span><div id="comment-31256" class="comment"><div id="post-31256-score" class="comment-score"></div><div class="comment-text"><p>Is this a C function? I have to use Lua. Also, my value is a 64 bit int.</p></div><div id="comment-31256-info" class="comment-info"><span class="comment-age">(28 Mar '14, 14:26)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31264"></span><div id="comment-31264" class="comment"><div id="post-31264-score" class="comment-score"></div><div class="comment-text"><p>Yes, it is part of the C interface. I don't think this functionality is exposed through the Lua interface right now, but I'm not as familiar with the Lua API.</p></div><div id="comment-31264-info" class="comment-info"><span class="comment-age">(28 Mar '14, 15:17)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="31265"></span><div id="comment-31265" class="comment"><div id="post-31265-score" class="comment-score"></div><div class="comment-text"><p>According to the docs, the <strong>mask</strong> option (0xFF0000FF in the example) should be available (optional parameter)</p><blockquote><p><a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_class_ProtoField">http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_class_ProtoField</a></p></blockquote></div><div id="comment-31265-info" class="comment-info"><span class="comment-age">(28 Mar '14, 15:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31266"></span><div id="comment-31266" class="comment"><div id="post-31266-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Also, my value is a <strong>64 bit int</strong>.</p></blockquote><p>64 bit is a second story. (usable) Lua 64 bit support was only added recently. What is your Wireshark version?</p></div><div id="comment-31266-info" class="comment-info"><span class="comment-age">(28 Mar '14, 15:26)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31269"></span><div id="comment-31269" class="comment"><div id="post-31269-score" class="comment-score"></div><div class="comment-text"><p>Using masks for ProtoFields is supported, and is shown in the <code>dissector.lua</code> example script found <a href="http://wiki.wireshark.org/Lua/Examples">here</a>. Using a 64-bit mask isn't though, both because Lua itself would lose precision in such a big number, but also because the current code gets it as a 32-bit integer. I'd argue the latter is a bug, but the former requires accepting a <code>UInt64</code> mask type anyway to actually work right. So I think you should submit a bug.</p></div><div id="comment-31269-info" class="comment-info"><span class="comment-age">(28 Mar '14, 16:09)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31270"></span><div id="comment-31270" class="comment not_top_scorer"><div id="post-31270-score" class="comment-score"></div><div class="comment-text"><p>Apparently the internal C-code for fields only supports a 32-bit mask to begin with. I grep'ed the code, and sure enough not a single 64-bit field uses a mask. The one I found that should have, cheated and pretended it was a 32-bit field because only the lower 32-bits were being used. That will make this tricky to support. :(</p></div><div id="comment-31270-info" class="comment-info"><span class="comment-age">(28 Mar '14, 16:35)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-31255" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-31255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31272"></span>

<div id="answer-container-31272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31272-score" class="post-score" title="current number of votes">0</div><span id="post-31272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try "cheating": create your current 64-bit ProtoField without a mask, and also create two 32-bit ProtoField for each 32-bit portion of the 64-bit with the appropriate mask for each portion. When you add the 64-bit one to the tree use the <code>TvbRange</code> of the whole 64-bits, and save the child tree returned from the <code>tree:add()</code> call; then add the two 32-bit ones to the child tree, giving each of them the <code>TvbRange</code> half they each represents. That way the user sees the 64-bit one and if they select it the whole 64-bits are highlighted, with a expandable arrow thing to see the two 32-bit ones under it for each 32-bit half, and clicking those will show the appropriately masked portions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '14, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31272" class="comments-container"><span id="31273"></span><div id="comment-31273" class="comment"><div id="post-31273-score" class="comment-score"></div><div class="comment-text"><p>"When you add the 64-bit one to the tree use the TvbRange of the whole 64-bits"... I think this opens a new tab in the bytes pane, because it is not a TvbRange that actually exists in the stream. I don't want to have to have so many new tabs open(they don't auto close when you are done looking at them). Also, ideally, the users can see where the disjoint bytes are located in relation to each other with just open click. Oh, am I picky?</p></div><div id="comment-31273-info" class="comment-info"><span class="comment-age">(28 Mar '14, 19:28)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31275"></span><div id="comment-31275" class="comment"><div id="post-31275-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure we're using the same words. A "tab" usually means a new window pane, and no adding a tree item does not create a new window. It does create a new branch in the tree, and if you add elements under that branch (i.e., under that child node) then the user will see an expansion icon (an arrow in GTK, or a plus in windows I think) next to that tree item, which they can click to expand to view what's under it if they want to. But it doesn't usually show in expanded form automatically so it shouldn't bother them.</p><p>These things are already done all over the place and most people don't notice it. For example, if you have a capture with TCP/IPv4 traffic, you'll see the Frame, Ethernet (or wifi), IP, and TCP in the details pane. If you expand the IP one, you'll see a DSCP field, which itself can be expanded, as well as the flags field, etc. Those aren't really one field each - they're multiple fields each: a parent one that you see without expanding it, and then the child ones under it when you expand them.</p></div><div id="comment-31275-info" class="comment-info"><span class="comment-age">(28 Mar '14, 19:41)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31327"></span><div id="comment-31327" class="comment"><div id="post-31327-score" class="comment-score"></div><div class="comment-text"><p>Sorry I have to use "Your answer" instead of comment, as I have two images.<br />
</p><p>You will see what I mean by "tab" by looking at the images. Toward the very bottom, there are two tabs, one for frame (79 bytes) and another for myTvb (4 bytes). myTvb is created from disjoint bytes in the payload. Wireshark automatically created the myTvb tab to show this new buffer that does not exist in the original payload.</p><p>The code that corresponds to this is as follows:</p><p>subtree:add(buffer(0,2),"The first value: " .. buffer(0,2):uint())</p><pre><code>local allBytes = ByteArray.new()

local nextByte = buffer(3, 1):bytes()

allBytes:append(nextByte)

nextByte = buffer(4, 1):bytes()

allBytes:append(nextByte)

nextByte = buffer(9, 1):bytes()

allBytes:append(nextByte)

nextByte = buffer(10, 1):bytes()

allBytes:append(nextByte)

debug(&quot;bytes are &quot; .. tostring(allBytes))

local myTvb = ByteArray.tvb(allBytes, &quot;My Tvb&quot;)

local subtreeNext = subtree:add(myTvb(0,0),&quot;The next value:&quot;..myTvb(0,4):uint())

    subtreeNext:add(buffer(3,2), &quot;The first part location&quot; )

    subtreeNext:add(buffer(9,2), &quot;The second part location&quot; )</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-03-31_at_5.10.37_PM_1.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-03-31_at_5.11.28_PM_1.png" alt="alt text" /></p></div><div id="comment-31327-info" class="comment-info"><span class="comment-age">(31 Mar '14, 15:25)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31360"></span><div id="comment-31360" class="comment"><div id="post-31360-score" class="comment-score"></div><div class="comment-text"><p>That's because you're creating a new <code>Tvb</code>, and adding it to the tree. There's no need to do that. The idea was to use the original <code>Tvb</code> that came in the packet, and to display portions of it using the masking strategy.</p></div><div id="comment-31360-info" class="comment-info"><span class="comment-age">(01 Apr '14, 14:58)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-31272" class="comment-tools"></div><div class="clear"></div><div id="comment-31272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31338"></span>

<div id="answer-container-31338" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31338-score" class="post-score" title="current number of votes">0</div><span id="post-31338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think what you want is possible, either in Lua or C. The bytes pane highlight only does continuous ranges and the creation of a new tvb for data from discontinuous bytes creates the new tab as you have seen.</p><p>You would need to make some (possibly) extensive changes in the core Wireshark code to allow highlighting of discontinuous ranges. You can try adding an enhancement request on the Wireshark bugzilla, but I don't know if you'll get any one to take it on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '14, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></img></div></div><div id="comments-container-31338" class="comments-container"><span id="31391"></span><div id="comment-31391" class="comment"><div id="post-31391-score" class="comment-score"></div><div class="comment-text"><p>Thanks. That's what I think.</p></div><div id="comment-31391-info" class="comment-info"><span class="comment-age">(02 Apr '14, 07:34)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31403"></span><div id="comment-31403" class="comment"><div id="post-31403-score" class="comment-score"></div><div class="comment-text"><p>That's because you're creating a new Tvb, and adding it to the tree. There's no need to do that. The idea was to use the original Tvb that came in the packet, and to display portions of it using the masking strategy.</p></div><div id="comment-31403-info" class="comment-info"><span class="comment-age">(02 Apr '14, 09:41)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31404"></span><div id="comment-31404" class="comment"><div id="post-31404-score" class="comment-score"></div><div class="comment-text"><p>That doesn't fix the OP's original issue in that they want discontiguous bytes highlighted in the bytes pane.</p></div><div id="comment-31404-info" class="comment-info"><span class="comment-age">(02 Apr '14, 09:49)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="31413"></span><div id="comment-31413" class="comment"><div id="post-31413-score" class="comment-score"></div><div class="comment-text"><p>Right, but this was in the context of the "cheating" proposal I made. His response was that would create a new tab, and my point is it only creates a new tab if you create a new Tvb.</p></div><div id="comment-31413-info" class="comment-info"><span class="comment-age">(02 Apr '14, 10:53)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31414"></span><div id="comment-31414" class="comment"><div id="post-31414-score" class="comment-score"></div><div class="comment-text"><p>In your cheating advice you said, "When you add the 64-bit one to the tree use the TvbRange of the whole 64-bits". How do you get the TvbRange? Code please.</p></div><div id="comment-31414-info" class="comment-info"><span class="comment-age">(02 Apr '14, 11:31)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-31338" class="comment-tools"></div><div class="clear"></div><div id="comment-31338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31434"></span>

<div id="answer-container-31434" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31434-score" class="post-score" title="current number of votes">0</div><span id="post-31434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do something like this <em>outside</em> of the dissector function:</p><pre><code>local f_value = ProtoField.uint32(&quot;myproto.value&quot;, &quot;The value&quot;)
local f_whole = ProtoField.bytes(&quot;myproto.value.hex&quot;, &quot;The whole range&quot;)
local f_part1 = ProtoField.uint16(&quot;myproto.value.part1&quot;, &quot;The first part&quot;, base.HEX)
local f_part2 = ProtoField.uint16(&quot;myproto.value.part2&quot;, &quot;The second part&quot;, base.HEX)
-- register the above fields to your proto
myproto.fields = { f_value, f_whole, f_part1, f_part2 }</code></pre><p>Now for the part <em>inside</em> the dissector function... the following assumes "<code>buffer</code>" is the name of the <code>Tvb</code> given to the <code>dissector()</code> function, and that your bytes start at offset <code>3</code> for <code>8</code> bytes long, since that's what it looks like from your code earlier; and the following assumes "<code>myval</code>" is the true/real/parsed Lua number value of your disparate fields - there are a couple different ways to achieve that without creating a new <code>Tvb</code>, but I assume you already have a way to do that; for example using the <code>Struct</code> class. If not, let me know and I can show that too.</p><pre><code>-- add your value to the tree, without highlighting
local subtree:add(f_value, myval)
-- and add the field for the bytes next, saving the returned child tree
local subtreeNext = subtree:add(f_whole, buffer:range(3,8))
-- add the children
subtreeNext:add(f_part1, buffer:range(3,2))
subtreeNext:add(f_part2, buffer:range(9,2))</code></pre><p>Alternatively, you could do this instead, depending on what look you like:</p><pre><code>-- add your value to the tree, highlighting all the bytes
local subtreeNext = subtree:add(f_value, buffer:range(3,8), myval)
-- add the children
subtreeNext:add(f_part1, buffer:range(3,2))
subtreeNext:add(f_part2, buffer:range(9,2))</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Apr '14, 13:48</strong> </span></p></div></div><div id="comments-container-31434" class="comments-container"><span id="31488"></span><div id="comment-31488" class="comment"><div id="post-31488-score" class="comment-score"></div><div class="comment-text"><p>Thanks Hadriel.<br />
This helps, but I don't like the fact that when "The whole range" is selected, everything, including bytes that should be omitted are highlighted. Ideally I want the bytes at the two ends of the range which I actually use highlighted but the ones in the middle not highlighted. I guess that is impossible to do. Your code does help me build my tree though. Much appreciated.</p></div><div id="comment-31488-info" class="comment-info"><span class="comment-age">(03 Apr '14, 09:07)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-31434" class="comment-tools"></div><div class="clear"></div><div id="comment-31434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

