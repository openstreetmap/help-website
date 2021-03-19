+++
type = "question"
title = "Lua dissector organization"
description = '''In the &quot;Enabled Protocols&quot; dialog some protocols have trees of sub-protocols. How is this organization defined, specifically when writing a protocol dissector in Lua? For example, I have dissectors defined in this way in %APPDATA%&#92;Wireshark&#92;plugins:  myproto.lua: MyProto myprotomsg1.lua: MyProtoMsg1...'''
date = "2016-02-04T13:34:00Z"
lastmod = "2016-02-04T13:34:00Z"
weight = 49867
keywords = [ "lua", "subdissector" ]
aliases = [ "/questions/49867" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua dissector organization](/questions/49867/lua-dissector-organization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49867-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the "Enabled Protocols" dialog some protocols have trees of sub-protocols. How is this organization defined, specifically when writing a protocol dissector in Lua?</p><p>For example, I have dissectors defined in this way in %APPDATA%\Wireshark\plugins:</p><ul><li>myproto.lua: MyProto</li><li>myprotomsg1.lua: MyProtoMsg1</li><li>myprotomsg2.lua: MyProtoMsg2</li></ul><p>MyProto adds itself in to wtap_encap in USER0 and creates a DissectorTable "myprotomsgs", and each subdissector adds itself to that table.</p><p>When I go to the Enabled Protocols dialog, I see:</p><ul><li>MyProto</li><li>MyProtoMsg1</li><li>MyProtoMsg2</li></ul><p>when I expect to see</p><ul><li>MyProto</li><li>     MyProtoMsg1</li><li>     MyProtoMsg2</li></ul><p>Is this possible using Lua?</p></div><div id="question-tags" class="tags-container tags">lua subdissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/5f457dffca32545365536f44c75d51ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmaranski&#39;s gravatar image" /><p>mmaranski<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmaranski has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Feb '16, 08:09</p></div></div><div id="comments-container-49867" class="comments-container"></div><div id="comment-tools-49867" class="comment-tools"></div><div class="clear"></div><div id="comment-49867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

