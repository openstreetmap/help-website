+++
type = "question"
title = "How to apply a change to a Lua preference without requiring a restart of Wireshark?"
description = '''I&#x27;ve added a preference to a Lua dissector, but when the preference is changed, a restart of Wireshark is required before the change takes affect. Is it possible for the changed preference to be applied without a restart? For example, below is a simple foo.lua Lua dissector with a simple Boolean pre...'''
date = "2017-03-30T11:26:00Z"
lastmod = "2017-03-30T11:49:00Z"
weight = 60450
keywords = [ "lua", "preference" ]
aliases = [ "/questions/60450" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to apply a change to a Lua preference without requiring a restart of Wireshark?](/questions/60450/how-to-apply-a-change-to-a-lua-preference-without-requiring-a-restart-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60450-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've added a preference to a Lua dissector, but when the preference is changed, a restart of Wireshark is required before the change takes affect. Is it possible for the changed preference to be applied without a restart?</p><p>For example, below is a simple <em>foo.lua</em> Lua dissector with a simple Boolean preference. Changing the preference currently requires a Wireshark restart before the change takes affect. The <a href="https://www.cloudshark.org/captures/965bd39c6694">foo.pcapng</a> capture file hosted on cloudshark can be used to test it.</p><pre><code>-- Protocol
local p_foo = Proto(&quot;foo&quot;, &quot;FOO Protocol&quot;)

-- Preferences
local foo_settings = {
    info = true
}
p_foo.prefs.info = Pref.bool(&quot;Write to Info column&quot;, foo_settings.info,
    &quot;Whether to write information to the Info column or not&quot;)

-------------------------------------------------------------------------
function p_foo.prefs_changed()

    if foo_settings.info ~= p_foo.prefs.info then
        foo_settings.info = p_foo.prefs.info
        reload() -- This doesn&#39;t seem to help.
    end

end

-------------------------------------------------------------------------
-- Fields
local f_foo_val8 = ProtoField.uint8(&quot;foo.val8&quot;, &quot;Value 8&quot;, base.OCT)
local f_foo_val16 = ProtoField.uint16(&quot;foo.val16&quot;, &quot;Value 16&quot;, base.DEC)
local f_foo_val32 = ProtoField.uint32(&quot;foo.val32&quot;, &quot;Value 32&quot;, base.HEX)
local f_foo_ipv4 = ProtoField.ipv4(&quot;foo.ipv4&quot;, &quot;IPv4 Address&quot;)
local f_foo_ipv6 = ProtoField.ipv6(&quot;foo.ipv6&quot;, &quot;IPv6 Address&quot;)

p_foo.fields = { f_foo_val8, f_foo_val16, f_foo_val32, f_foo_ipv4, f_foo_ipv6 }

-- Dissection
function p_foo.dissector(buf, pinfo, tree)
    local foo_tree = tree:add(p_foo, buf(0,-1))

    pinfo.cols.protocol:set(&quot;FOO&quot;)
    if foo_settings.info then
        pinfo.cols.info:set(&quot;Hello World!&quot;)
    end

    foo_tree:add(f_foo_val8, buf(0, 1))
    foo_tree:add(f_foo_val16, buf(1, 2))
    foo_tree:add(f_foo_val32, buf(3, 4))
    foo_tree:add(f_foo_ipv4, buf(7, 4))
    foo_tree:add(f_foo_ipv6, buf(11, 16))
end

-- Registration
local udp_table = DissectorTable.get(&quot;udp.port&quot;)
udp_table:add(33333, p_foo)</code></pre></div><div id="question-tags" class="tags-container tags">lua preference</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '17, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-60450" class="comments-container"></div><div id="comment-tools-60450" class="comment-tools"></div><div class="clear"></div><div id="comment-60450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60451"></span>

<div id="answer-container-60451" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60451-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, this is apparently a Lua bug with the latest version, Version 2.3.0 (v2.1.0rc0-3313-geb37819), because it works as expected with Wireshark 1.12.13. I'll file a bug report.</p><p><strong>EDIT</strong>: It also works with the latest version of Wireshark Gtk, but just not with Qt. This is reflected in the bug report, which is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13536">Bug 13536</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '17, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Mar '17, 13:08</p></div></div><div id="comments-container-60451" class="comments-container"></div><div id="comment-tools-60451" class="comment-tools"></div><div class="clear"></div><div id="comment-60451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

