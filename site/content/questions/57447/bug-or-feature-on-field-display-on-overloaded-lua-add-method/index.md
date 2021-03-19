+++
type = "question"
title = "Bug or feature on field display on overloaded lua add() method"
description = '''I am generating display methods for some fields in lua scripts. The example in the documentation at https://wiki.wireshark.org/LuaAPI/TreeItem: local t = tree:add( proto_foo, buf() ) t:add_le( proto_foo.fields.u16, buf(1,2), 100, nil, &quot;(&quot;, nil, &quot;little&quot;, 999, nil, &quot;endian&quot;, nil, &quot;)&quot; )  suggests that...'''
date = "2016-11-18T07:47:00Z"
lastmod = "2016-11-18T07:47:00Z"
weight = 57447
keywords = [ "lua", "add", "dissector", "display" ]
aliases = [ "/questions/57447" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bug or feature on field display on overloaded lua add() method](/questions/57447/bug-or-feature-on-field-display-on-overloaded-lua-add-method)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57447-score" class="post-score" title="current number of votes">0</div><span id="post-57447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am generating display methods for some fields in lua scripts. The example in the documentation at <a href="https://wiki.wireshark.org/LuaAPI/TreeItem:">https://wiki.wireshark.org/LuaAPI/TreeItem:</a></p><pre><code>local t = tree:add( proto_foo, buf() )
t:add_le( proto_foo.fields.u16, buf(1,2), 100, nil, &quot;(&quot;, nil, &quot;little&quot;, 999, nil, &quot;endian&quot;, nil, &quot;)&quot; )</code></pre><p>suggests that the display will be:</p><pre><code>&quot;Unsigned short: 0x6400 ( little endian )&quot;</code></pre><p>When I imitate this code with:</p><pre><code>proto.fields.packet_type = ProtoField.new(&quot;Type&quot;, &quot;type&quot;, ftypes.UINT8)
function display_type(value)
  if value == 0 then
    return &quot;Heartbeat&quot;
  end
  if value == 1 then
    return &quot; Start Of Session&quot;
  end
  if value == 2 then
    return &quot;End Of Session&quot;
  end
  if value == 3 then
    return &quot;Application Message&quot;
  end
  return &quot;&quot;
end

function dissect_packet_type(buffer, offset, packet, parent)
  local size = 1
  local range = buffer(offset, size)
  local value = range:le_int()
  local display = display_type(value)
  parent:add(proto.fields.type, range, value, display)
  return offset + size
end</code></pre><p>With the display method I see:</p><pre><code>&quot;Heartbeat&quot;</code></pre><p>I want it to print like the standard fields so instead I generate the display function as:</p><pre><code>function display_type(value)
  if value == 0 then
    return &quot;Type: Heartbeat (0)&quot;  
  end
  if value == 1 then
    return &quot;Type: Start Of Session (1)&quot;
  end
  if value == 2 then
    return &quot;Type: End Of Session (2)&quot;
  end
  if value == 3 then
    return &quot;Type: Application Message (3)&quot;
  end
  return &quot;&quot;
end</code></pre><p>Is my function invalid? Does the documentation need to be updated? Or is this a bug?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-add" rel="tag" title="see questions tagged &#39;add&#39;">add</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '16, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/d03ce1682e2a9e3bd9ed3be60088d031?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="william&#39;s gravatar image" /><p><span>william</span><br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="william has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Nov '16, 07:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-57447" class="comments-container"></div><div id="comment-tools-57447" class="comment-tools"></div><div class="clear"></div><div id="comment-57447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

