+++
type = "question"
title = "where to declare a pattren name in lua while writting a dissector."
description = '''for example, i used : dissector_add_string(&quot;rtp_ dyn_ payload_ type&quot;,&quot;PATTREN&quot;, xxx_handle); while writing a normal dissector in c. Now i want to write the dissector in lua .please help me with this.'''
date = "2015-04-15T04:27:00Z"
lastmod = "2015-04-15T04:27:00Z"
weight = 41448
keywords = [ "lua", "error" ]
aliases = [ "/questions/41448" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [where to declare a pattren name in lua while writting a dissector.](/questions/41448/where-to-declare-a-pattren-name-in-lua-while-writting-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41448-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>for example, i used :</p><p>dissector_add_string("rtp_ dyn_ payload_ type","PATTREN", xxx_handle);</p><p>while writing a normal dissector in c. Now i want to write the dissector in lua .please help me with this.</p></div><div id="question-tags" class="tags-container tags">lua error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '15, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/a2e29df6af5eb33f09d1ed5321ea6586?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakshmi&#39;s gravatar image" /><p>lakshmi<br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakshmi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '15, 22:41</p></div></div><div id="comments-container-41448" class="comments-container"><span id="41581"></span><div id="comment-41581" class="comment"><div id="post-41581-score" class="comment-score"></div><div class="comment-text"><p>i tried like this:</p><p>local my_dissector_table = DissectorTable.get("rtp.pt") local xxx = dissectortable:get_dissector("PATTREN") my_dissector_table:add(xxx, p_myproto)</p><p>It is showing error as:</p><p>Lua: Error during loading: C:\Program Files\Wireshark1\myproto.lua:30: bad argument #1 to 'get_dissector' (number expected, got string)</p></div><div id="comment-41581-info" class="comment-info"><span class="comment-age">(19 Apr '15, 22:28)</span> lakshmi</div></div></div><div id="comment-tools-41448" class="comment-tools"></div><div class="clear"></div><div id="comment-41448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

