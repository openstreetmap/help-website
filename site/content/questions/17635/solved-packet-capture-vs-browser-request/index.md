+++
type = "question"
title = "[Solved] Packet Capture vs Browser Request"
description = '''I&#x27;ve noticed that Wireshark isn&#x27;t able to capture certain browser GET requests. For example, TamperData (Firefox addon) shows a GET request for a URL. In Wireshark that URL is not seen as an HTTP.REQUEST.URI, rather it is found as an XML.ATTRIBUTE. I&#x27;m wondering where I am having the disconnect unde...'''
date = "2013-01-11T21:35:00Z"
lastmod = "2013-01-11T21:35:00Z"
weight = 17635
keywords = [ "browser", "request", "wireshark" ]
aliases = [ "/questions/17635" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[Solved\] Packet Capture vs Browser Request](/questions/17635/solved-packet-capture-vs-browser-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17635-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've noticed that Wireshark isn't able to capture certain browser GET requests. For example, TamperData (Firefox addon) shows a GET request for a URL. In Wireshark that URL is not seen as an HTTP.REQUEST.URI, rather it is found as an XML.ATTRIBUTE. I'm wondering where I am having the disconnect understanding this.</p><p>Thanks</p><p>Update: NGREP is able to capture the HTTP GET request.</p><p>Edit: There were some odd dynamic caching that was occurring. It wasn't showing because it had been cached.</p><p>Though this problem is solved, there's still another one that I've run into. If the traffic is SSL, Wireshark won't be able to see it, but TamperData will, since it is getting the request before it is encrypted and sent off.</p></div><div id="question-tags" class="tags-container tags">browser request wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '13, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/d4659f38a392fe3d2b0f19ac1863e7a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naisanza&#39;s gravatar image" /><p>naisanza<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naisanza has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '13, 22:12</p></div></div><div id="comments-container-17635" class="comments-container"></div><div id="comment-tools-17635" class="comment-tools"></div><div class="clear"></div><div id="comment-17635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

