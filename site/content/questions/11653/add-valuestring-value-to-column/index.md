+++
type = "question"
title = "add valuestring value to column"
description = '''I&#x27;m having a problem with getting the value of a protofield to the Info column. I&#x27;ve defined the following ProtoField: f.payload = ProtoField.uint8(&quot;observation.payload&quot;,&quot;payload&quot;,base.HEX,{ [0] = &quot;Off&quot;, [1] = &quot;On&quot;},0x10)  I want add this field value (On or Off) to pinfo.col.info. How can I do it?'''
date = "2012-06-05T02:00:00Z"
lastmod = "2012-06-05T15:54:00Z"
weight = 11653
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/11653" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [add valuestring value to column](/questions/11653/add-valuestring-value-to-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11653-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having a problem with getting the value of a protofield to the Info column. I've defined the following ProtoField:</p><pre><code>f.payload = ProtoField.uint8(&quot;observation.payload&quot;,&quot;payload&quot;,base.HEX,{ [0] = &quot;Off&quot;, [1] = &quot;On&quot;},0x10)</code></pre><p>I want add this field value (On or Off) to <code>pinfo.col.info</code>. How can I do it?</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '12, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/542740772c88eb2e13de648922e897bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ekrako&#39;s gravatar image" /><p>ekrako<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ekrako has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jun '12, 16:00</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11653" class="comments-container"></div><div id="comment-tools-11653" class="comment-tools"></div><div class="clear"></div><div id="comment-11653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11694"></span>

<div id="answer-container-11694" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11694-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't extract the value from a ProtoField (see similar <a href="http://ask.wireshark.org/questions/11211/getting-field-values-from-protofield">question</a>). Instead, you have to parse the buffer, and add the value manually to the Info column, which is fairly easy to do. Try this:</p><pre><code>local VALS_ON_OFF = { [0] = &quot;Off&quot;, [1] = &quot;On&quot; }

local proto_foo = Proto(&quot;foo&quot;, &quot;Foo Protocol&quot;)
local f = proto_foo.fields
f.payload = ProtoField.uint8(&quot;observation.payload&quot;, &quot;payload&quot;, base.HEX, VALS_ON_OFF, 0x10)

function proto_foo.dissector(buf, pinfo, tree)
   local t = tree:add(proto_foo, buf())

   -- assume observation.payload is at byte 0
   t:add(f.payload, buf(0,1))

   -- 0x10 has one bit set, that&#39;s bit 3 from the left
   local bitval = buf(0,1):bitfield(3)

   -- set the Info column based on the bit value
   pinfo.cols.info = &quot;payload: &quot;..VALS_ON_OFF[bitval]
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '12, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jun '12, 16:01</p></div></div><div id="comments-container-11694" class="comments-container"></div><div id="comment-tools-11694" class="comment-tools"></div><div class="clear"></div><div id="comment-11694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

