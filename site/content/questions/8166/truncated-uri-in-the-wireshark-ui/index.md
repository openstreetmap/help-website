+++
type = "question"
title = "Truncated URI in the Wireshark UI"
description = '''Long URIs are truncated in the Wireshark UI by default, even when the capture was run with tshark which does not limit the snaplen. I can view the full URI on the command-line using tshark and pulling out the http.request.uri. Is it possible to override whatever causes the truncation in the Wireshar...'''
date = "2011-12-29T13:36:00Z"
lastmod = "2011-12-29T16:28:00Z"
weight = 8166
keywords = [ "gui", "truncated", "ui", "truncate", "wireshark" ]
aliases = [ "/questions/8166" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Truncated URI in the Wireshark UI](/questions/8166/truncated-uri-in-the-wireshark-ui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8166-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Long URIs are truncated in the Wireshark UI by default, even when the capture was run with tshark which does not limit the snaplen. I can view the full URI on the command-line using tshark and pulling out the http.request.uri. Is it possible to override whatever causes the truncation in the Wireshark UI? None of the options I came across in the UI seemed to lend itself to making this possible. I also did a recursive search under the Wireshark installation directory and nothing stood out.</p></div><div id="question-tags" class="tags-container tags">gui truncated ui truncate wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '11, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/c72ae7a46acbddf07e3c2ba755b19a4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devrick0&#39;s gravatar image" /><p>devrick0<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devrick0 has no accepted answers">0%</span></p></div></div><div id="comments-container-8166" class="comments-container"></div><div id="comment-tools-8166" class="comment-tools"></div><div class="clear"></div><div id="comment-8166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8167"></span>

<div id="answer-container-8167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8167-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're referring to the URI being truncated in the packet details pane, then that is likely the result of the URI being longer than the maximum number of characters allowed, which is currently specified by <code>ITEM_LABEL_LENGTH</code> as <code>240</code> in <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/proto.h?revision=40306&amp;view=markup">epan/proto.h</a>.</p><p>This topic recently came up on the <a href="http://www.wireshark.org/lists/wireshark-users/201112/msg00062.html">wireshark-user</a> mailing list. You might want to <a href="https://www.wireshark.org/mailman/listinfo/wireshark-users">subscribe</a> to it if you haven't already.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '11, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8167" class="comments-container"></div><div id="comment-tools-8167" class="comment-tools"></div><div class="clear"></div><div id="comment-8167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

