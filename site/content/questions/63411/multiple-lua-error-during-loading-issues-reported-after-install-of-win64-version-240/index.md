+++
type = "question"
title = "Multiple &quot;Lua: Error during loading&quot; issues reported after install of Win64 version 2.4.0"
description = '''Prior to install and launch of Wireshark 2.4.0 for Windows 64, I had none of the problems described below. However, after the install, I am getting the following 2 errors reported in a dialog:   Lua: Error during loading:  [string &quot;C:&#92;Program Files&#92;Wireshark&#92;plugins&#92;2.4.0&#92;dsmc...&quot;]:40: bad argument ...'''
date = "2017-08-04T16:48:00Z"
lastmod = "2017-08-04T23:10:00Z"
weight = 63411
keywords = [ "lua", "base.hex", "ftypes.ether", "dissectors" ]
aliases = [ "/questions/63411" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple "Lua: Error during loading" issues reported after install of Win64 version 2.4.0](/questions/63411/multiple-lua-error-during-loading-issues-reported-after-install-of-win64-version-240)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63411-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Prior to install and launch of Wireshark 2.4.0 for Windows 64, I had none of the problems described below. However, after the install, I am getting the following 2 errors reported in a dialog:</p><ol><li><p>Lua: Error during loading: [string "C:\Program Files\Wireshark\plugins\2.4.0\dsmc..."]:40: bad argument #3 to 'bytes' (Display must be either base.NONE, base.DOT, base.DASH, base.COLON or base.SPACE) --</p></li><li><p>Lua: Error during loading: [string "C:\Program Files\Wireshark\plugins\2.4.0\twcs..."]:426: bad argument #3 to 'new' (ProtoField_new: Unsupported ProtoField field type) --</p></li></ol><h2 id="the-first-error">The first error</h2><p>References a dissector named dsmcc_dissector.lua, and line 40 has the following lua code:<br />
ServerInteractiveSessionRequest.fields.sessionId = ProtoField.bytes("dsmcc.sessionId", "sessionId", base.HEX, nil, nil)</p><h2 id="referencing-the-following-lua-api-link-base.hex-appears-to-be-valid">Referencing the following LUA API link, base.HEX appears to be valid:</h2><p><a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Proto.html">https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Proto.html</a></p><h2 id="the-second-error">2. The second error</h2><p>References a dissector named twcssp.lua, and line 426 has the following lua code: local pf_stb_address = ProtoField.new("Unique STB MAC Address", "dsmcc_ssp.stb_address", ftypes.ETHER)</p><h2 id="referencing-the-follwing-lua-api-link-ftypes.ether-appears-also-to-be-valid">Referencing the follwing LUA API link, ftypes.ETHER appears also to be valid:</h2><p><a href="https://wiki.wireshark.org/LuaAPI/Proto#ProtoField">https://wiki.wireshark.org/LuaAPI/Proto#ProtoField</a></p><p>Any help on how to resolve this would be greatly appreciated!</p><p>Thanks,</p><p>Mike</p></div><div id="question-tags" class="tags-container tags">lua base.hex ftypes.ether dissectors</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '17, 16:48</strong></p><img src="https://secure.gravatar.com/avatar/0e669f5129ac13bdba3262abcfbaa92b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfbaker&#39;s gravatar image" /><p>mfbaker<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfbaker has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-63411" class="comments-container"><span id="63412"></span><div id="comment-63412" class="comment"><div id="post-63412-score" class="comment-score"></div><div class="comment-text"><p>FYI, I just downgraded Win64 wireshark v2.4.0 to Win64 wireshark v2.2.8. Wireshark now launches, and there are no more "LUA: Error during loading" messages.</p></div><div id="comment-63412-info" class="comment-info"><span class="comment-age">(04 Aug '17, 17:41)</span> mfbaker</div></div></div><div id="comment-tools-63411" class="comment-tools"></div><div class="clear"></div><div id="comment-63411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63414"></span>

<div id="answer-container-63414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63414-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Referencing the following LUA API link, base.HEX appears to be valid</p></blockquote><p>The documentation needs updating; FT_BYTES fields are <em>always</em> displayed as hex, you just get to choose what separates the hex digit pairs for the bytes, if anything. Choose one of base.NONE, base.DOT, base.DASH, base.COLON or base.SPACE, depending on whether you want no separator between bytes, a "." between bytes, a "-" between bytes, a ":" between bytes, or a pace between bytes. I don't know whether any other than base.NONE will work on all versions of Wireshark, but base.NONE should work on all versions.</p><blockquote><p>Referencing the follwing LUA API link, ftypes.ETHER appears also to be valid</p></blockquote><p>That looks like a bug; please file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach your Lua script.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '17, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63414" class="comments-container"><span id="63416"></span><div id="comment-63416" class="comment"><div id="post-63416-score" class="comment-score"></div><div class="comment-text"><p>Just as a possible workaround, you use</p><p><code>ServerInteractiveSessionRequest.fields.sessionId = ProtoField.bytes("dsmcc.sessionId", "sessionId", base.HEX, nil, nil)</code></p><p>in one case, but in the other one, you use</p><p><code>local pf_stb_address = ProtoField.new("Unique STB MAC Address", "dsmcc_ssp.stb_address", ftypes.ETHER)</code> rather than <code>local pf_stb_address = ProtoField.ether("Unique STB MAC Address", "dsmcc_ssp.stb_address")</code></p><p>Maybe the latter syntax is accepted? If it is, it doesn't mean that you should not file the bug as <a href="https://ask.wireshark.org/users/79/guy-harris">@Guy Harris</a> asked you to.</p></div><div id="comment-63416-info" class="comment-info"><span class="comment-age">(04 Aug '17, 23:42)</span> sindy</div></div><span id="63422"></span><div id="comment-63422" class="comment"><div id="post-63422-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Guy! I just filed Bug 13950 - Multiple "Lua: Error during loading" issues reported after install of Win64 version 2.4.0, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13950">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13950</a></p></div><div id="comment-63422-info" class="comment-info"><span class="comment-age">(06 Aug '17, 13:43)</span> mfbaker</div></div></div><div id="comment-tools-63414" class="comment-tools"></div><div class="clear"></div><div id="comment-63414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

