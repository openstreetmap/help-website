+++
type = "question"
title = "LUA dissector: update treeitem in earlier packet"
description = '''Hi, I&#x27;ve written a post-dissector to add some additional info into the tree for TCP packets. I&#x27;d like to do something like the http.response_in field but for TCP, or put another way, provide the inverse of the tcp.analysis.acks_frame - rather than saying this is an ACK to the earlier segment in fram...'''
date = "2017-02-02T02:07:00Z"
lastmod = "2017-02-04T03:12:00Z"
weight = 59240
keywords = [ "lua", "dissector", "postdissector" ]
aliases = [ "/questions/59240" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [LUA dissector: update treeitem in earlier packet](/questions/59240/lua-dissector-update-treeitem-in-earlier-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've written a post-dissector to add some additional info into the tree for TCP packets. I'd like to do something like the <code>http.response_in</code> field but for TCP, or put another way, provide the inverse of the <code>tcp.analysis.acks_frame</code> - rather than saying <em>this is an ACK to the earlier segment in frame x</em> say <em>this segment is ACKed later in frame y</em>.</p><p>It seems like this would require saving state and then updating an already dissected packet. Is this even possible with LUA, and if so could someone provide a few hints or point to similar code?</p><p>thanks a bundle,</p><p>chris</p></div><div id="question-tags" class="tags-container tags">lua dissector postdissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '17, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/0957869882dd5a286cc5208905077d98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaddman&#39;s gravatar image" /><p>gaddman<br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaddman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '17, 13:42</p></div></div><div id="comments-container-59240" class="comments-container"></div><div id="comment-tools-59240" class="comment-tools"></div><div class="clear"></div><div id="comment-59240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59250"></span>

<div id="answer-container-59250" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59250-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I faced the same issue when I wrote the TRANSUM LUA. Guy corrected me the other day regarding Wireshark scanning so my following description is a bit loose, and I'm doing this from memory.</p><p>Your dissector will be called at least twice for each packet; once on an initial scan with pinfo.visited false and a second (and further times) with pinfo.visited true. You can generate the new values on the first scan and add the data to the protocol tree on the second (and later) scans.</p><p>You might want to take a look at the TRANSUM LUA code which you can download from TribeLab.com.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '17, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-59250" class="comments-container"><span id="59261"></span><div id="comment-59261" class="comment"><div id="post-59261-score" class="comment-score"></div><div class="comment-text"><p>Paul, that's even better than what I'd hoped for. I've had a look through your TRANSUM code and realised it was actually a small change to my code. Updated my dissector here: <a href="https://github.com/gaddman/wireshark-tcpextend">https://github.com/gaddman/wireshark-tcpextend</a></p></div><div id="comment-59261-info" class="comment-info"><span class="comment-age">(08 Feb '17, 13:35)</span> gaddman</div></div></div><div id="comment-tools-59250" class="comment-tools"></div><div class="clear"></div><div id="comment-59250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59242"></span>

<div id="answer-container-59242" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59242-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I doubt this can be done in a post dissector, let alone LUA. I think this has to be done in the TCP dissector itself. The concept however is possible. Other dissector do have the feature where 'requests' and 'responses' are matched both ways. There is a README on this (request response tracking) in the doc directory of the source tree to give you some insight in how this is achieved.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '17, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59242" class="comments-container"><span id="59262"></span><div id="comment-59262" class="comment"><div id="post-59262-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the pointer, I read the source docs and there's a good outline of how to write a dissector in C: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.request_response_tracking;hb=HEAD">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.request_response_tracking;hb=HEAD</a></p></div><div id="comment-59262-info" class="comment-info"><span class="comment-age">(08 Feb '17, 13:36)</span> gaddman</div></div></div><div id="comment-tools-59242" class="comment-tools"></div><div class="clear"></div><div id="comment-59242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

