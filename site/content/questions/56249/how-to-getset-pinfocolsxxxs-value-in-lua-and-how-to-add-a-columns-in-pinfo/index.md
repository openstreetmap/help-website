+++
type = "question"
title = "how to get/set pinfo.cols.xxx&#x27;s value in lua, and how to add a columns in pinfo?"
description = '''and one more question, how to access the data beyon tvb. Such as I add a dissector in udp port 2222, but I need to access the data in network layer in the dissector, how to do this in Lua, or I have to use c to do this? Best regards'''
date = "2016-10-09T04:00:00Z"
lastmod = "2016-10-16T13:50:00Z"
weight = 56249
keywords = [ "lua", "columns", "pinfo" ]
aliases = [ "/questions/56249" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to get/set pinfo.cols.xxx's value in lua, and how to add a columns in pinfo?](/questions/56249/how-to-getset-pinfocolsxxxs-value-in-lua-and-how-to-add-a-columns-in-pinfo)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56249-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>and one more question, how to access the data beyon tvb. Such as I add a dissector in udp port 2222, but I need to access the data in network layer in the dissector, how to do this in Lua, or I have to use c to do this?</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">lua columns pinfo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '16, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/06873e10edc62e4ff547a6e2c5ef5e25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmqy&#39;s gravatar image" /><p>cmqy<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmqy has no accepted answers">0%</span></p></div></div><div id="comments-container-56249" class="comments-container"></div><div id="comment-tools-56249" class="comment-tools"></div><div class="clear"></div><div id="comment-56249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56429"></span>

<div id="answer-container-56429" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56429-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are interested in things like the destination address, have a look at fields like <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Pinfo.html#lua_class_attrib_pinfo_net_src"><code>pinfo.net_src</code></a> or <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Pinfo.html#lua_class_attrib_pinfo_src"><code>pinfo.src</code></a>. You can find more of such fields at the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Pinfo.html">pinfo reference</a>.</p><p>To access individual fields, first specify the individual packet somewhere in your packet and retrieve it like this:</p><pre><code>local myproto = Proto(&quot;myproto&quot;, &quot;My Protocol&quot;)
local ttl_field = Field.new(&quot;ip.ttl&quot;)
function myproto.dissect(tvb, pinfo, tree)
    local ttl = ttl_field()
    -- now &quot;ttl&quot; contains a FieldInfo instance
end</code></pre><p>For the available properties of the FieldInfo class instance, see the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Field.html#lua_class_FieldInfo">FieldInfo reference</a>. You are likely interested in the <code>value</code> and <code>range</code> fields.</p><p>In other cases, you can just access the contents of the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Tvb.html#lua_class_Tvb"><code>tvb</code></a> directly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '16, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56429" class="comments-container"></div><div id="comment-tools-56429" class="comment-tools"></div><div class="clear"></div><div id="comment-56429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

