+++
type = "question"
title = "Is there a way to group ProtoFields In Lua?"
description = '''Given: local foo_proto = Proto(,)  local foo_fields = foo_proto.fields  foo_fields is a ProtoField[] (at least that is how I think of it) Is there a way to define foo_proto.messages where messages is a Message[] And for each Message have Message.ProtoField[] fields In other words I would like to str...'''
date = "2013-11-25T02:12:00Z"
lastmod = "2014-03-07T17:12:00Z"
weight = 27334
keywords = [ "lua", "dissector", "protofield" ]
aliases = [ "/questions/27334" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to group ProtoFields In Lua?](/questions/27334/is-there-a-way-to-group-protofields-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27334-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Given:</p><pre><code>local foo_proto = Proto(,)

local foo_fields = foo_proto.fields</code></pre><p><code>foo_fields</code> is a <code>ProtoField[]</code> (at least that is how I think of it)</p><p>Is there a way to define</p><p><code>foo_proto.messages</code> where <code>messages</code> is a <code>Message[]</code></p><p>And for each <code>Message</code> have <code>Message.ProtoField[] fields</code></p><p>In other words I would like to structure field definitions, instead of having a flat/linear <code>ProtoField</code> definition</p></div><div id="question-tags" class="tags-container tags">lua dissector protofield</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/10ba80b2d73f068e916ba35852a8a436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lews%20Therin&#39;s gravatar image" /><p>Lews Therin<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lews Therin has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 07 Mar '14, 16:45</p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-27334" class="comments-container"></div><div id="comment-tools-27334" class="comment-tools"></div><div class="clear"></div><div id="comment-27334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30589"></span>

<div id="answer-container-30589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30589-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe, depending on how you mean the question.</p><p>Basically the <code>foo_proto.fields</code> member is a Lua table array of ProtoFields, as you said; but it's real purpose is to bind the internal wireshark representation of protocol fields to Lua. When you set the ProtoFields into the <code>foo_proto.fields</code> member, which you don't show in your example but is presumably being done, then internally wireshark remembers those fields, and once your script is loaded, they're each registered internally for your protocol. That internal structure isn't changeable by Lua code. You can certainly store those fields in other tables/variables in your Lua script, but it won't change how wireshark processes them.</p><p>So, for example, you could do this:</p><pre><code>-- my new proto
local foo_proto = Proto(...)
-- create some protofields
local field1 = ProtoField.new(...)
local field2 = ProtoField.new(...)
local field3 = ProtoField.new(...)
-- sets the protofields to the proto
foo_proto.fields = { field1, field2 }
-- have a nicer way of getting my protofields
local myfoo = { message = {header = field1, data = field2}, keepalive = field3 }

function foo_proto.dissector(tvbuf,pktinfo,root)
    ...
    tree:add(myfoo.message.data, tvbuf:range(2,2))
    ...
end</code></pre><p>You can do that, but it's not like Wireshark is going to know that <code>field2</code> or <code>myfoo.message.data</code> is at that buffer range/offset or anything. All you're doing is creating a Lua table, with member variables that happen to point to the same <code>ProtoField</code> userdata objects that you set into the <code>Proto.field</code> member. I.e., since userdata objects are handled as pointers and copied by reference, the above works; wireshark knows nothing about it... as far as wireshark knows, your <code>myfoo.message.data</code> is identical to using <code>field2</code>.</p><p>What you <strong>cannot</strong> do, is do that type of thing using <code>foo_proto.messages</code>, because <code>foo_proto</code> represents a wirshark object, and that class type has no member variable named <code>messages</code> which you could be getting/setting from/to. In the past I think it might have silently allowed you to it but not actually done the action; but more recent versions will error if you try setting a member that doesn't exist like that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '14, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30589" class="comments-container"></div><div id="comment-tools-30589" class="comment-tools"></div><div class="clear"></div><div id="comment-30589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

