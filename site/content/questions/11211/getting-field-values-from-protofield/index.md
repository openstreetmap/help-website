+++
type = "question"
title = "Getting field values from ProtoField"
description = '''I have a ProtoField defined as: proto.led = ProtoField.uint8(&quot;led&quot;, &quot;LED&quot;, base.HEX, LED_FLAGS, 0x1)  That bit changes a few fields in the message. Ideally, I&#x27;d be able to do something like: if (proto.led) then  -- do a else  -- do b  Is there any shortcut to grabbing the value of a field (or bit) f...'''
date = "2012-05-22T06:26:00Z"
lastmod = "2012-05-22T17:39:00Z"
weight = 11211
keywords = [ "lua" ]
aliases = [ "/questions/11211" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting field values from ProtoField](/questions/11211/getting-field-values-from-protofield)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11211-score" class="post-score" title="current number of votes">0</div><span id="post-11211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_class_ProtoField"><code>ProtoField</code></a> defined as:</p><pre><code>proto.led = ProtoField.uint8(&quot;led&quot;, &quot;LED&quot;, base.HEX, LED_FLAGS, 0x1)</code></pre><p>That bit changes a few fields in the message. Ideally, I'd be able to do something like:</p><pre><code>if (proto.led) then
   -- do a
else
   -- do b</code></pre><p>Is there any shortcut to grabbing the value of a field (or bit) from the <code>ProtoField</code> definitions? The bit field is displayed correctly in the GUI, so I know I am parsing this part right.</p><p>This would be easy in C-dissector. I'm still fumbling my way thru Lua.<br />
</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/61dd0a62d62ba6e987ac1f93ad269ebe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TalleyHo&#39;s gravatar image" /><p><span>TalleyHo</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TalleyHo has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 May '12, 07:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11211" class="comments-container"></div><div id="comment-tools-11211" class="comment-tools"></div><div class="clear"></div><div id="comment-11211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11213"></span>

<div id="answer-container-11213" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11213-score" class="post-score" title="current number of votes">1</div><span id="post-11213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TalleyHo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, that's not possible. The <code>ProtoField</code> only defines the format of the field; it isn't aware of packet buffers or offsets, both of which would be required to determine the field value.</p><p>On the other hand, <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Field.html#lua_class_Field"><code>Field</code></a> extractors can pull field values from the current packet without being given buffers/offsets (the fields would already have been parsed by a dissector). However, this is only available from a <a href="http://wiki.wireshark.org/Lua/Taps">tap</a> or <a href="http://wiki.wireshark.org/Lua/Dissectors#postdissectors">postdissector</a>, and it doesn't <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3513">work</a> for Lua-defined fields (unverified).</p><p><strong>EDIT:</strong> You might be interested in <a href="http://wiki.wireshark.org/LuaAPI/Tvb#tvbrange:bitfield.28.5Boffset.5D.2C_.5Blength.5D.29"><code>TvbRange.bitfield()</code></a> and Wireshark Lua's built-in <a href="http://bitop.luajit.org/api.html"><code>bit</code></a> library, as demonstrated below.</p><pre><code>local proto_foo = Proto(&#39;foo&#39;, &#39;Foo Protocol&#39;)
local f = proto_foo.fields

local LED_FLAGS = { [0] = &#39;off&#39;, [1] = &#39;on&#39; }
f.led = ProtoField.uint8(&#39;foo.led&#39;, &#39;LED&#39;, base.HEX, LED_FLAGS, 0x01)

local LED_BYTE_OFFSET = 0
local LED_BIT_INDEX = 7 -- rightmost bit in MSB-0 bit numbering

function proto_foo.dissector(buf, pinfo, tree)
    -- use TvbRange.bitfield(offset, length)
    local bitval = buf(LED_BYTE_OFFSET, 1):bitfield(LED_BIT_INDEX, 1)
    print(&#39;bit&#39;, bitval, LED_FLAGS[bitval] or &#39;?&#39;)

    -- or use the built-in &quot;bit&quot; library (no need to use &quot;require&quot;)
    local num = buf(LED_BYTE_OFFSET, 1):uint()
    local bitval2 = bit.band( bit.rshift(num, 7 - LED_BIT_INDEX), 1 )
    print(&#39;bit&#39;, bitval2, LED_FLAGS[bitval2] or &#39;?&#39;)

end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 May '12, 17:41</strong> </span></p></div></div><div id="comments-container-11213" class="comments-container"><span id="11214"></span><div id="comment-11214" class="comment"><div id="post-11214-score" class="comment-score"></div><div class="comment-text"><p>I could grab the buffer and parse it, but I don't see bitwise operators in Lua. However, the lua docs state that is only supported in 5.2. Unfortunately, I'm not quite there yet. Is there another way to handle this fork in the road? Right now I key off the remaining packet length, but I'm not happy with that /solution/.</p></div><div id="comment-11214-info" class="comment-info"><span class="comment-age">(22 May '12, 07:00)</span> <span class="comment-user userinfo">TalleyHo</span></div></div><span id="11215"></span><div id="comment-11215" class="comment"><div id="post-11215-score" class="comment-score"></div><div class="comment-text"><p>See updated answer. And Wireshark Lua has a built-in <code>bit</code> library, which I think is a copy of: <a href="http://bitop.luajit.org/api.html">http://bitop.luajit.org/api.html</a></p></div><div id="comment-11215-info" class="comment-info"><span class="comment-age">(22 May '12, 07:10)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="11224"></span><div id="comment-11224" class="comment"><div id="post-11224-score" class="comment-score"></div><div class="comment-text"><p>Awesome. I didn't know about the bitfield function. Although, I think the docs may be bass-ackwards. The LED bit in my case is bit 5, however, I had to use extendedMsg = buffer(offset, 1):bitfield(2, 1) which says that the start position is 2 from the LEFT and 1 bit in width. Thanks for the pointer to bitfield, that did the trick.</p></div><div id="comment-11224-info" class="comment-info"><span class="comment-age">(22 May '12, 12:56)</span> <span class="comment-user userinfo">TalleyHo</span></div></div><span id="11229"></span><div id="comment-11229" class="comment"><div id="post-11229-score" class="comment-score"></div><div class="comment-text"><p>You're right. <code>bitfield()</code> (actually, its underlying C function: <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/tvbuff.c?revision=42638&amp;view=markup#l1777"><code>_tvb_get_bits64</code></a>) uses <a href="http://en.wikipedia.org/wiki/Bit_numbering#MSB_0_bit_numbering">MSB-0 bit numbering</a>. The wiki for <code>bitfield()</code> has been corrected. Thanks.</p></div><div id="comment-11229-info" class="comment-info"><span class="comment-age">(22 May '12, 17:39)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-11213" class="comment-tools"></div><div class="clear"></div><div id="comment-11213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

