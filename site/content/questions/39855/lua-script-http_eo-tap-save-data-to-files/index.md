+++
type = "question"
title = "Lua Script HTTP_EO TAP  Save Data to Files"
description = '''Hi, I am new bee to Lua scripting. I am trying to use http_eo tap to download all files extracted from http to a folder. Following is what I tried and I have no idea how to move further. tap_http_eo = Listener.new(&quot;http_eo&quot;) function tap_http_eo.packet(pinfo,tvb)  local text = &quot;packet &quot; .. pinfo.num...'''
date = "2015-02-13T09:22:00Z"
lastmod = "2015-02-13T09:22:00Z"
weight = 39855
keywords = [ "export-http", "lua", "tshark" ]
aliases = [ "/questions/39855" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua Script HTTP\_EO TAP Save Data to Files](/questions/39855/lua-script-http_eo-tap-save-data-to-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39855-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am new bee to Lua scripting. I am trying to use http_eo tap to download all files extracted from http to a folder. Following is what I tried and I have no idea how to move further.</p><p>tap_http_eo = Listener.new("http_eo") function tap_http_eo.packet(pinfo,tvb) local text = "packet " .. pinfo.number -- debug("packet " .. pinfo.number, tvb)</p><p>end</p><p>Kindly help me and give me pointers, how can I use tvb to save files in folder.</p></div><div id="question-tags" class="tags-container tags">export-http lua tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '15, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/a332cff93fdb53320465b8dadef03ad3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MZR&#39;s gravatar image" /><p>MZR<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MZR has no accepted answers">0%</span></p></div></div><div id="comments-container-39855" class="comments-container"></div><div id="comment-tools-39855" class="comment-tools"></div><div class="clear"></div><div id="comment-39855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

