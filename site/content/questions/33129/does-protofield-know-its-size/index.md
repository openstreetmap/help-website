+++
type = "question"
title = "Does ProtoField know it&#x27;s size?"
description = '''I&#x27;m writing a simple dissector, and bump into a &#x27;DRY/SPOT&#x27; violation: I can declare ProtoField, but applying it to a vtbuff I still need to tell how many bytes it should use: proto = Proto(&quot;X&quot;, &quot;x&quot;) proto.fields.firstchunk = ProtoField.uint8(&quot;x.firstchunk&quot;, &quot;The First Byte&quot;) proto.fields.secondchunk...'''
date = "2014-05-28T04:04:00Z"
lastmod = "2014-05-28T04:04:00Z"
weight = 33129
keywords = [ "design", "dissector", "protofield" ]
aliases = [ "/questions/33129" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does ProtoField know it's size?](/questions/33129/does-protofield-know-its-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33129-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a simple dissector, and bump into a 'DRY/SPOT' violation: I can declare <code>ProtoField</code>, but applying it to a <code>vtbuff</code> I still need to tell how many bytes it should use:</p><pre><code>proto = Proto(&quot;X&quot;, &quot;x&quot;)
proto.fields.firstchunk  = ProtoField.uint8(&quot;x.firstchunk&quot;, &quot;The First Byte&quot;)
proto.fields.secondchunk = ProtoField.uint32(&quot;x.secondchunk&quot;, &quot;The Second Chunk&quot;)
proto.dissector(buffer, pinfo, tree)
  tree:add(proto.fields.firstchunk, buffer(0,1))
  tree:add(proto.fields.secondchunk, buffer(1,4))

  -- I really wanted to write:
  local offset = 0
  tree:add(proto.fields.firstchunk(buffer, offset))
  offset += proto.fields.firstchunk.size

  tree:add(proto.fields.secondchunk(buffer, offset))
  offset += proto.fields.secondchunk.size
  ...
end</code></pre><p>Is something like that possible?</p></div><div id="question-tags" class="tags-container tags">design dissector protofield</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '14, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/635c3ea0c7b8c37ef45744b6e66dd263?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xtofl&#39;s gravatar image" /><p>xtofl<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xtofl has no accepted answers">0%</span></p></div></div><div id="comments-container-33129" class="comments-container"></div><div id="comment-tools-33129" class="comment-tools"></div><div class="clear"></div><div id="comment-33129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

