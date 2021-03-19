+++
type = "question"
title = "Adding tree items according to bitmask"
description = '''I have got a working dissector up and running using Lua, and it is working well. It does everything I need it to do and I am getting the information I need - no problems. However, I would like to make a rather large improvement. Currently, our packets are sent with a 24-bit mask in each header, info...'''
date = "2015-03-22T20:54:00Z"
lastmod = "2015-06-27T21:36:00Z"
weight = 40772
keywords = [ "lua", "dissector", "tree", "mask", "flags" ]
aliases = [ "/questions/40772" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Adding tree items according to bitmask](/questions/40772/adding-tree-items-according-to-bitmask)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40772-score" class="post-score" title="current number of votes">0</div><span id="post-40772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have got a working dissector up and running using Lua, and it is working well. It does everything I need it to do and I am getting the information I need - no problems. However, I would like to make a rather large improvement. Currently, our packets are sent with a 24-bit mask in each header, informing the client which fields in the packet are valid. If the field is not valid, it is normally just padded with nulls (0x00).</p><p>Currently, I am adding all fields to my tree, without checking the mask, so I get a lot of useless tree items, and I have to manually check the flags to see which fields with 0s are valid or invalid...</p><p>My question is: How do I only add items to the tree if the mask in the header <strong><code>BITWISE AND</code></strong>s with the field mask?</p><p>e.g. currently: <code>fds.myfield = ProtoField.new("My field", "my_proto.my_field", ftypes.UINT32, nil, base.DEC)</code></p><p>then in my dissector: <code>twig:add_le(fds.myfield, buff(28,4))</code></p><p>Do I have to wrap an if statement around each and every <code>tree:add</code>?? *gasp</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-mask" rel="tag" title="see questions tagged &#39;mask&#39;">mask</span> <span class="post-tag tag-link-flags" rel="tag" title="see questions tagged &#39;flags&#39;">flags</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '15, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/33446b713282cb77d176fc09465801aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fidelius&#39;s gravatar image" /><p><span>Fidelius</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fidelius has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '15, 20:56</strong> </span></p></div></div><div id="comments-container-40772" class="comments-container"></div><div id="comment-tools-40772" class="comment-tools"></div><div class="clear"></div><div id="comment-40772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43621"></span>

<div id="answer-container-43621" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43621-score" class="post-score" title="current number of votes">1</div><span id="post-43621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Fidelius has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Do I have to wrap an if statement around each and every tree:add??</p></blockquote><p>Nope, you do <em>not</em> have to wrap each and every <code>tree:add</code> call (or in your case, <code>tree:add_le</code>).</p><p>Really, a statement like <code>tree:add(foo)</code> is Lua short-hand for <code>TreeItem.add(tree, foo)</code>, which is short-hand for "in a table named 'TreeItem', get the entry of index 'add', and call its value as a function, passing it the arguments 'tree' and 'foo'".</p><p>So what you can do is create a proxy function that will decide whether to actually call <code>TreeItem.add()</code> or not, based on your bit mask value. For example:</p><pre><code>local myproto = Proto(&quot;myproto&quot;,&quot;My Protocol&quot;)

-- my protocol&#39;s fields
local fds =
{
    bitmask = 
    {
        -- this field doesn&#39;t have a match entry, since it&#39;s the bitmask
        -- field in the packet that decides matches
        pfield = ProtoField.new(&quot;The bitmask for fields&quot;, &quot;my_proto.bitmask&quot;,
                                ftypes.UINT24, nil, base.HEX)
    }
    myfield =
    {
        match = 0x000001, -- the bit in the bitmask that represents this field
        pfield = ProtoField.new(&quot;My field&quot;, &quot;my_proto.my_field&quot;,
                                ftypes.UINT32, nil, base.DEC)
    },
    myotherfield =
    {
        match = 0x000010,
        pfield = ProtoField.new(&quot;My other field&quot;, &quot;my_proto.my_other_field&quot;,
                                ftypes.UINT16, nil, base.DEC)
    },
    -- more fields here
}

-- a flat table to hold the above but only as ProtoFields
local flat_fds = {}
-- fill that flat table
for _,v in pairs(fds) do
    flat_fds[#flat_fds + 1] = v.pfield
end
-- register all the fields using the flat table
myproto.fields = flat_fds

-- a proxy function that decides when to add a ProtField to the tree or not
local function addMaskedField(tree, mask, field, ...)
    -- only add it if it&#39;s set in the passed-in mask
    if bit.band(mask, field.match) == field.match then
        TreeItem.add_le(tree, field.pfield, ...)
    end
end

function myproto.dissector(buf,pinfo,root)
    -- add my protocol to the tree root
    local tree = root:add(myproto, buf(0, buf:len()))

    -- add the bitmask to the tree, at byte 0 for 3 bytes
    tree:add_le(fds.bitmask.pfield, buf(0, 3))

    -- now get the 24-bit value into Lua so we can use it
    local mask = buf(0, 3):le_uint()

    addMaskedField(tree, mask, fds.myfield, buf(3, 4))
    addMaskedField(tree, mask, fds.myotherfield, buf(7, 2))

    -- etc., etc.
end</code></pre><p>Note that the above is just an example - I haven't tried it or even verified it was well-formed code. But it should give you the general idea.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '15, 21:36</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43621" class="comments-container"></div><div id="comment-tools-43621" class="comment-tools"></div><div class="clear"></div><div id="comment-43621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42045"></span>

<div id="answer-container-42045" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42045-score" class="post-score" title="current number of votes">0</div><span id="post-42045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to document each dissected byte, even if it is not used, then you can use the <code>ti.set_hidden()</code> function on a <code>TreeItem</code> to hide it (you cannot undo this!). Note that if the fields are completely rubbish, then you might want to introduce a dummy field for it such as <code>my_proto.unused</code>).</p><p>Alternatively, do not add the field at all since it is unlikely of interest to the user. Yes, you need to check this yourself, but some structured code should help here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '15, 16:05</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-42045" class="comments-container"></div><div id="comment-tools-42045" class="comment-tools"></div><div class="clear"></div><div id="comment-42045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

