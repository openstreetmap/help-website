+++
type = "question"
title = "Get value from protofield"
description = '''Hello,  I&#x27;m a recent convert from a C based dissector to Lua to help ease the installation for our Windows users. :)  Is it possible to get the value from a proto field that has already been defined? Or must I grab the data from the buffer? For instance... foo_proto = Proto(&quot;foo&quot;,&quot;Foo Proto&quot;) local ...'''
date = "2010-12-01T07:40:00Z"
lastmod = "2010-12-01T07:40:00Z"
weight = 1190
keywords = [ "extraction", "protofield", "append" ]
aliases = [ "/questions/1190" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get value from protofield](/questions/1190/get-value-from-protofield)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1190-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm a recent convert from a C based dissector to Lua to help ease the installation for our Windows users. :)<br />
</p><p>Is it possible to get the value from a proto field that has already been defined? Or must I grab the data from the buffer? For instance...</p><p>foo_proto = Proto("foo","Foo Proto") local foo = foo_proto.fields foo.pdu = ProtoField.uint8("foo.pdutype", "PDU Type", base.HEX, PDU_TYPES) ... subtree:add(foo.pdu, buffer(offset,1)); offset = offset + 1;</p><p>From here, I ultimately call into a more detailed parser function depending on various fields in the header. I may want to do something like pinfo.cols.append(string.format(" PDU Type: %d", foo.pdu:uint())) but I get an error.</p><p>The primary problem is that our proto has a common header field of 20 bytes that I don't necessarily want to add text to the table, but in the later, more discrete parsers I would. I have the whole buffer in my helper functions, but it sure would be nice and convenient if I could somehow use the protofield I've defined to pull/retrieve data.</p><p>Secondly, I'm a bit new to the Wireshark/Lua interface. Is there an easier way to debug your scripts and make changes? Right now I'm doing it the good ol' college way - make changes, open wireshark, see if it worked, if not, kill wireshark, make changes, recapture, repeat ad naseum. Is there a way to reload my script via dofile() on the evaluate line? I get duplicate proto errors when doing so.</p></div><div id="question-tags" class="tags-container tags">extraction protofield append</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '10, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/61dd0a62d62ba6e987ac1f93ad269ebe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TalleyHo&#39;s gravatar image" /><p>TalleyHo<br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TalleyHo has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Dec '10, 07:45</p></div></div><div id="comments-container-1190" class="comments-container"></div><div id="comment-tools-1190" class="comment-tools"></div><div class="clear"></div><div id="comment-1190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

