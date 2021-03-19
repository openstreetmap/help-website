+++
type = "question"
title = "How to change a proto_item value at dissector?"
description = '''Hey, I&#x27;m writing a dissector (wireshark-v1.99.9) for a custom protocol with the following structure:   pdu = instruction [&amp;amp; 0x20 &amp;amp; parameter]*  That means each pdu has excatly one instruction and an variable amount of parameters. At the details pane the protocol should be display like that: ...'''
date = "2015-09-18T04:13:00Z"
lastmod = "2015-09-18T05:19:00Z"
weight = 45943
keywords = [ "development", "dissector", "export", "wireshark", "plugin" ]
aliases = [ "/questions/45943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to change a proto\_item value at dissector?](/questions/45943/how-to-change-a-proto_item-value-at-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45943-score" class="post-score" title="current number of votes">0</div><span id="post-45943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I'm writing a dissector (wireshark-v1.99.9) for a custom protocol with the following structure:<br />
</p><blockquote><p>pdu = instruction [&amp; 0x20 &amp; parameter]*</p></blockquote><p>That means each pdu has excatly one instruction and an variable amount of parameters. At the details pane the protocol should be display like that:<br />
-Instructionname<br />
+"Parameters: %d", n<br />
--parameter 0<br />
--parameter 1<br />
--...<br />
--parameter n<br />
</p><p>The field/node parameters should contain an FT_UINT8 so the user can search for packets with certain amount of parameters (n). Therefore at the time parameters is constructed I don't know n. To work around this issue I could first dissect the pdu and determine n and afterwards dissect a second time to construct the proto_tree. But performance-wise this is not a good solution.</p><p>I would rather init parameters with 0, dissect the pdu and finalize n after I'm done. I checked epan/proto.h&amp;.c and README.dissector for methods I could use.<br />
<code>proto_item_set_text();</code> looked promising but it broke the filter proto.paramters==n (&gt;, &lt; kept working).<br />
The second discovery is <code>static void proto_tree_set_uint(field_info *fi, guint32 value);</code>. It suits my needs perfectly, but is not exported via proto.h.</p><p>I'm not that experienced as a programmer and a wireshark newbie, therefore <strong>my questions:</strong><br />
</p><ol><li>Is there a way I overlooked, to accomplish the desired protocol dissection?</li><li>Is there a deeper design reason behind the fact that <code>proto_tree_set_uint();</code> (and similar functions) are not exported? I tried to do it myself, added following costum functions:<br />
<strong>proto.h</strong><br />
<code>WS_DLL_PUBLIC void my_set_uint(proto_item *pi, guint32 value);</code><br />
<strong>proto.c</strong><br />
<code>void my_set_uint(proto_item *pi, guint32 value) {   proto_tree_set_uint(PITEM_FINFO(pi), value); }</code><br />
and recompiled wireshark and my plugin but it crashed right after the startup.</li></ol><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '15, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/47d39f56c989005615cd5d94372229f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grima&#39;s gravatar image" /><p><span>Grima</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grima has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '15, 04:27</strong> </span></p></div></div><div id="comments-container-45943" class="comments-container"></div><div id="comment-tools-45943" class="comment-tools"></div><div class="clear"></div><div id="comment-45943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45945"></span>

<div id="answer-container-45945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45945-score" class="post-score" title="current number of votes">0</div><span id="post-45945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not certain I follow your protocol definition, but I think you're saying it's one of those awkward protocols that doesn't have a length or count in the "header", and then repeated "parameter" records.</p><p>If that's the case, then I would add the instruction field, keeping the return value (a <code>proto_item*</code>) from <code>proto_tree_add_item()</code>, creating a sub-tree off it with <code>proto-item_add_subtree()</code>, iterate over the parameter records accumulating the count, then at the end add the count value to the sub-tree of the instruction field using the accumulated value. To finish off, call the <code>PROTO_ITEM_SET_GENERATED()</code> macro on the count field to show that it's been generated and doesn't exist in the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '15, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-45945" class="comments-container"></div><div id="comment-tools-45945" class="comment-tools"></div><div class="clear"></div><div id="comment-45945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

