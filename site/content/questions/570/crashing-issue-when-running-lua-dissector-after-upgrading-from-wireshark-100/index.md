+++
type = "question"
title = "Crashing issue when running Lua dissector after upgrading from wireshark 1.0.0"
description = '''The Lua dissector below causes a segmentation fault in Wireshark 1.2 and Wireshark 1.4.1. This works fine in Wireshark 1.0.0. It appears that the call to payload_dissector_table:try() is causing the problem, but I can&#x27;t figure out why. If I remove that call, the dissector runs fine. If I change the ...'''
date = "2010-10-20T16:11:00Z"
lastmod = "2010-10-20T16:11:00Z"
weight = 570
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/570" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Crashing issue when running Lua dissector after upgrading from wireshark 1.0.0](/questions/570/crashing-issue-when-running-lua-dissector-after-upgrading-from-wireshark-100)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The Lua dissector below causes a segmentation fault in Wireshark 1.2 and Wireshark 1.4.1. This works fine in Wireshark 1.0.0.</p><p>It appears that the call to <code>payload_dissector_table:try()</code> is causing the problem, but I can't figure out why. If I remove that call, the dissector runs fine. If I change the dissector table so that it doesn't match any packets, the dissector runs fine. If I remove everything from the <code>testProtoSubprotocol.dissector()</code> function, I get a crash. So, it doesn't look like there's anything wrong about <code>testProtoSubprotocol.dissector()</code> itself.</p><p>I'm not sure why this is happening, or where to go from here to debug it. Does anyone have any suggestions either on what the issue is, or how to debug it further?</p><p>Thanks!</p><h1 id="lua-dissector">Lua dissector</h1><pre><code>testProtoSubprotocol = Proto(&quot;testproto.test&quot;, &quot;Test Protocol Frame Type 0&quot;)

local testSubfields = testProtoSubprotocol.fields
testSubfields.number = ProtoField.uint16(&quot;testproto.test.number&quot;, &quot;Number&quot;, base.DEC)

function testProtoSubprotocol.dissector(buffer, pinfo, tree)
    local subtree = tree:add(testProtoSubprotocol, buffer())
    local number = buffer(0, 2)
    subtree:add_le(testSubfields.number, number)
    pinfo.cols.info = &quot;Number &quot;
    pinfo.cols.info:append( number:le_uint() )
end

testDissectorTable = DissectorTable.new( &quot;testproto&quot;, &quot;Test Protocol&quot; )
testDissectorTable:add( 0, testProtoSubprotocol )

testProtocol = Proto(&quot;testproto&quot;, &quot;Test Protocol&quot;)

local frametypes = {
    [0x00] = &quot;Test Frame Type&quot;,
}

local fields = testProtocol.fields
fields.frameType = ProtoField.uint8(&quot;testproto.frame_type&quot;, &quot;Frame Type&quot;, base.HEX, frametypes, 0x0F)
fields.payload = ProtoField.bytes(&quot;testproto.payload&quot;, &quot;Payload&quot;)

function testProtocol.dissector(buffer, pinfo, tree)
    pinfo.cols.protocol = testProtocol.name

    local subtree = tree:add(testProtocol, buffer())

    local frame_type = mask( buffer(0, 1):uint(), 0x0F )

    subtree:add(fields.frameType, buffer(offset, 1))

    payload = buffer(2, 60)
    local payload_dissector_table = DissectorTable.get( &quot;testproto&quot; )
    payload_dissector_table:try( frame_type, payload:tvb(), pinfo, subtree )
end

function mask( value, mask )
    return value % (mask + 1)
end

ethernet_table = DissectorTable.get(&quot;ethertype&quot;)
ethernet_table:add(0x4A46, testProtocol)</code></pre><h1 id="version-information">Version information:</h1><pre><code>wireshark 1.4.1

Copyright 1998-2010 Gerald Combs &lt;[email protected]wireshark.org&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled with GTK+ 2.20.1, (32-bit) with GLib 2.24.1, with libpcap 1.0.0, with
libz 1.2.3.3, with POSIX capabilities (Linux), without libpcre, with SMI 0.4.8,
with c-ares 1.7.0, with Lua 5.1, without Python, with GnuTLS 2.8.5, with Gcrypt
1.4.4, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Feb 18
2010 22:31:30), without AirPcap.

Running on Linux 2.6.32-24-generic, with libpcap version 1.0.0, with libz
1.2.3.3, GnuTLS 2.8.5, Gcrypt 1.4.4.

Built using gcc 4.4.3.</code></pre></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '10, 16:11</strong></p><img src="https://secure.gravatar.com/avatar/2a77db1e6976df3589b98cfb3bb27667?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacques&#39;s gravatar image" /><p>Jacques<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacques has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 May '12, 15:09</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-570" class="comments-container"><span id="11006"></span><div id="comment-11006" class="comment"><div id="post-11006-score" class="comment-score"></div><div class="comment-text"><p>asked <strong>20 Oct '10</strong>, 16:11<br />
edited <strong>25 mins</strong> ago ???</p><p>I wonder if @Jacques is still waiting for an answer :-)</p></div><div id="comment-11006-info" class="comment-info"><span class="comment-age">(15 May '12, 15:36)</span> Kurt Knochner ♦</div></div><span id="11007"></span><div id="comment-11007" class="comment"><div id="post-11007-score" class="comment-score"></div><div class="comment-text"><p>@Kurt, yes :) that would be my edit. The question was difficult to read because of the formatting, and the fix was simple. The reported problem might not be an issue any more, but it can still be answered regardless of whether @Jacques is waiting for the answer :)</p></div><div id="comment-11007-info" class="comment-info"><span class="comment-age">(15 May '12, 16:00)</span> helloworld</div></div></div><div id="comment-tools-570" class="comment-tools"></div><div class="clear"></div><div id="comment-570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

