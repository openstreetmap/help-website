+++
type = "question"
title = "lua: little-endian ProtoField"
description = '''Is there a way to create a ProtoField and indicate that it is to be interpreted little-endian? I only find constructors for e.g. uint16, while the vtbuff does have methods to extract little-endian values (buff:le_uint16())'''
date = "2014-05-28T05:13:00Z"
lastmod = "2014-06-04T00:57:00Z"
weight = 33134
keywords = [ "protofield", "little-endian" ]
aliases = [ "/questions/33134" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [lua: little-endian ProtoField](/questions/33134/lua-little-endian-protofield)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33134-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to create a <code>ProtoField</code> and indicate that it is to be interpreted little-endian? I only find constructors for e.g. <code>uint16</code>, while the <code>vtbuff</code> <em>does</em> have methods to extract little-endian values (<code>buff:le_uint16()</code>)</p></div><div id="question-tags" class="tags-container tags">protofield little-endian</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '14, 05:13</strong></p><img src="https://secure.gravatar.com/avatar/635c3ea0c7b8c37ef45744b6e66dd263?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xtofl&#39;s gravatar image" /><p>xtofl<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xtofl has no accepted answers">0%</span></p></div></div><div id="comments-container-33134" class="comments-container"></div><div id="comment-tools-33134" class="comment-tools"></div><div class="clear"></div><div id="comment-33134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33370"></span>

<div id="answer-container-33370" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33370-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use: <code>t:add_le( proto_foo.fields.u16, buf(0,2) )</code> as mentioned in <a href="http://wiki.wireshark.org/LuaAPI/TreeItem">http://wiki.wireshark.org/LuaAPI/TreeItem</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/cc22b4404576d307a99960c5bfc8a08f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bavh&#39;s gravatar image" /><p>bavh<br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bavh has one accepted answer">50%</span></p></div></div><div id="comments-container-33370" class="comments-container"></div><div id="comment-tools-33370" class="comment-tools"></div><div class="clear"></div><div id="comment-33370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

