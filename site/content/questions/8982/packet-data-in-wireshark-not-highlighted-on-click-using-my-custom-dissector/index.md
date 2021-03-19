+++
type = "question"
title = "Packet data in wireshark not highlighted on click using my custom dissector"
description = '''I am writing a dissector in Lua for a custom binary protocol. I have defined three field types: f.field1 = ProtoField.bytes(&quot;myproto.field1&quot;,&quot;Field 1&quot;,base.HEX) f.field2 = ProtoField.uint16(&quot;myproto.field2&quot;,&quot;Field 2&quot;,base.HEX) f.field3 = ProtoField.bytes(&quot;myproto.field3&quot;,&quot;Field 3&quot;,base.HEX)  These f...'''
date = "2012-02-13T13:02:00Z"
lastmod = "2012-02-13T18:12:00Z"
weight = 8982
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/8982" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Packet data in wireshark not highlighted on click using my custom dissector](/questions/8982/packet-data-in-wireshark-not-highlighted-on-click-using-my-custom-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8982-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a dissector in Lua for a custom binary protocol. I have defined three field types:</p><pre><code>f.field1 = ProtoField.bytes(&quot;myproto.field1&quot;,&quot;Field 1&quot;,base.HEX)
f.field2 = ProtoField.uint16(&quot;myproto.field2&quot;,&quot;Field 2&quot;,base.HEX)
f.field3 = ProtoField.bytes(&quot;myproto.field3&quot;,&quot;Field 3&quot;,base.HEX)</code></pre><p>These fields are added to the tree like this:</p><pre><code>subtree:add(f.field1,buf(offset,4))
offset = offset + 4
val2 = buf(offset,2):uint()

-- some logic around populating f2_description omitted
offset = offset + 2
subtree:add(f.field2, val2):append_text(&quot; (&quot; ..f2_description ..&quot;)&quot;)
subtree:add(f.field3, buf(offset,2))</code></pre><p><br />
Now, when I open Wireshark and click on "Field 1" or "Field 3" in the dissected packet's tree, I see that the selected data is highlighted in the raw packet hex view (bottom most panel):</p><p><img src="http://i.stack.imgur.com/sjeyf.png" alt="packet contents highlighted" /></p><p><br />
but it is not the case for Field2.</p><p><img src="http://i.stack.imgur.com/4Y4jq.png" alt="alt text" /></p><p><br />
What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '12, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/b70690e672a9e5968adc126d9dd0c16d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Konrads&#39;s gravatar image" /><p>Konrads<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Konrads has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '12, 17:33</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></img></div></div><div id="comments-container-8982" class="comments-container"></div><div id="comment-tools-8982" class="comment-tools"></div><div class="clear"></div><div id="comment-8982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8985"></span>

<div id="answer-container-8985" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8985-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is you're passing in <code>val2</code> (an integer) when you really want to pass in <code>buf(offset,2)</code>, which is a <a href="http://wiki.wireshark.org/LuaAPI/Tvb#TvbRange"><code>TvbRange</code></a>. <a href="http://wiki.wireshark.org/LuaAPI/TreeItem#treeitem:add.28proto_field_.5B.2Ctvbrange.5D_.5B.2Cvalue_.5B.2Ctext1_.5B.2Ctext2.5D_....5D_.5D.29"><code>TreeItem</code></a> requires the <code>TvbRange</code> in order to highlight the corresponding bytes in the <em>Packet Details Pane</em>.</p><p>Something like this would work the way you want:</p><pre><code>subtree:add(f.field1,buf(offset,4))
offset = offset + 4
val2 = buf(offset+4,2):uint()
-- some logic around populating f2_description omitted
offset = offset + 2
subtree:add(f.field2, val2 buf(offset+4,2)):append_text(&quot; (&quot; ..f2_description ..&quot;)&quot;)
subtree:add(f.field3, buf(offset+6,2))</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '12, 18:12</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '12, 19:52</p></div></div><div id="comments-container-8985" class="comments-container"><span id="8988"></span><div id="comment-8988" class="comment"><div id="post-8988-score" class="comment-score"></div><div class="comment-text"><p>Thanks! it works!</p></div><div id="comment-8988-info" class="comment-info"><span class="comment-age">(14 Feb '12, 00:07)</span> Konrads</div></div></div><div id="comment-tools-8985" class="comment-tools"></div><div class="clear"></div><div id="comment-8985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

