+++
type = "question"
title = "LUA: hex-highlighting for self made fields"
description = '''How do I make it that if I click on a self made protocol field in the packet detail window  that the hex data in the Packet Bytes window get highlighted?'''
date = "2011-05-18T01:01:00Z"
lastmod = "2011-05-18T08:09:00Z"
weight = 4116
keywords = [ "lua", "highlighting" ]
aliases = [ "/questions/4116" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA: hex-highlighting for self made fields](/questions/4116/lua-hex-highlighting-for-self-made-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4116-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I make it that if I click on a self made protocol field in the packet detail window that the hex data in the Packet Bytes window get highlighted?</p></div><div id="question-tags" class="tags-container tags">lua highlighting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '11, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/e51dc160a8e2668b26a868c6c996cd7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chill&#39;s gravatar image" /><p>chill<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chill has no accepted answers">0%</span></p></div></div><div id="comments-container-4116" class="comments-container"></div><div id="comment-tools-4116" class="comment-tools"></div><div class="clear"></div><div id="comment-4116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4121"></span>

<div id="answer-container-4121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4121-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a couple ways: add a <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_class_ProtoField">ProtoField</a> (which must include a buffer), or add a buffer with a label.</p><pre><code>proto_foo = Proto(&quot;foo&quot;, &quot;Foo Protocol&quot;)
proto_foo.fields.bar = ProtoField.uint32(&quot;foo.bar&quot;, &quot;Bar field&quot;)

function proto_foo.dissector(buf, pinfo, tree)
    -- we need at least 5 bytes...
    if buf:len() &lt; 5 then return end

    -- Add the first 4 bytes as an unsigned integer.
    -- Bytes 0 through 3 will be highlighted when the
    -- bar field is selected in the packet details.
    tree:add( proto_foo.fields.bar, buf(0, 4) )

    -- Add the next byte ad hoc. Byte 4 will be highlighted
    -- when this ad-hoc field is selected in the packet
    -- details.
    tree:add( buf(4, 1), &quot;Ad-hoc byte&quot; )
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '11, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-4121" class="comments-container"><span id="4134"></span><div id="comment-4134" class="comment"><div id="post-4134-score" class="comment-score"></div><div class="comment-text"><p>at first thx for the hint with the buffer(x,y) thats nice. So my code is working now but It look a bit redundancy.</p><p>My Code: local F_md5 = ProtoField.string("http.my.md5", "MD5: ") local subtreeitem = treeitem:add(http_my_proto, tvbuffer) subtreeitem:set_text("http post decoded") subtreeitem:add(F_md5, tvbuffer(1,32), s_info['md5']):set_text("MD5: " .. s_info['md5'])</p><p>if I write it that way:</p><p>My Code: local F_md5 = ProtoField.string("http.my.md5", "MD5: ") local subtreeitem = treeitem:add(http_my_proto, tvbuffer) subtreeitem:set_text("http post decoded") subtreeitem:add(F_md5, tvbuffer(1,32), s_info['md5']</p><p>then the n in the s_info['md5'] is not translated.</p><p>btw: how do I mark code as code?</p></div><div id="comment-4134-info" class="comment-info"><span class="comment-age">(19 May '11, 01:30)</span> chill</div></div><span id="4154"></span><div id="comment-4154" class="comment"><div id="post-4154-score" class="comment-score"></div><div class="comment-text"><p>First, you don't need to add a colon to the <code>ProtoField</code> description because that's already done internally. That should be <code>ProtoField.string("http.my.md5", "MD5")</code>. In your 1st example, there's no point in using the ProtoField's <code>label</code> arg since you're just going to overwrite the entire tree-item text with <code>set_text</code>. The two examples should produce the same results, assuming <code>s_info['md5']</code> is a string. What does <code>s_info['md5']</code> return?</p></div><div id="comment-4154-info" class="comment-info"><span class="comment-age">(19 May '11, 14:46)</span> bstn</div></div><span id="4155"></span><div id="comment-4155" class="comment"><div id="post-4155-score" class="comment-score"></div><div class="comment-text"><p>Three ways to mark text as code:</p><ol><li>Surround the text with backticks (`); This is the only way to do it for comments (afaik).</li><li>Select the text and click the "Code Sample button" in the answer toolbar (the button that shows as 101010); This can only be done for answers.</li><li>Select the text and press <strong><em>Ctrl+K</em></strong>; This can only be done for answers.</li></ol></div><div id="comment-4155-info" class="comment-info"><span class="comment-age">(19 May '11, 14:52)</span> bstn</div></div></div><div id="comment-tools-4121" class="comment-tools"></div><div class="clear"></div><div id="comment-4121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

