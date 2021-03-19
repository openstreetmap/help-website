+++
type = "question"
title = "Lua Dissector - Access other dissectors&#x27; fields"
description = '''I wrote a custom dissector to dissect TCP payloads. I would like to access the wlan.sa field from within my dissector. How can I access data (fields) from &quot;lower layer&quot; dissectors, like the 802.11 dissector. '''
date = "2016-07-29T10:04:00Z"
lastmod = "2016-07-29T12:42:00Z"
weight = 54444
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/54444" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Lua Dissector - Access other dissectors' fields](/questions/54444/lua-dissector-access-other-dissectors-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54444-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a custom dissector to dissect TCP payloads. I would like to access the wlan.sa field from within my dissector. How can I access data (fields) from "lower layer" dissectors, like the 802.11 dissector.</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '16, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/6acf3c1293dde7d08c204b9265e46764?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J_Turner&#39;s gravatar image" /><p>J_Turner<br />
<span class="score" title="71 reputation points">71</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J_Turner has no accepted answers">0%</span></p></div></div><div id="comments-container-54444" class="comments-container"></div><div id="comment-tools-54444" class="comment-tools"></div><div class="clear"></div><div id="comment-54444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54445"></span>

<div id="answer-container-54445" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54445-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've provided many Lua-related links in my answer to <a href="https://ask.wireshark.org/questions/53802/how-dissect-two-segments-of-one-protocol-in-the-same-packet-in-the-same-tcp-segment-lua">this</a> question. The documentation explains how to do this and there are many example scripts that show you exactly how to do it as well. One such example is the "<a href="https://wiki.wireshark.org/Lua/Dissectors#postdissectors">postdissectors</a>" example, where it shows things like:</p><pre><code> 5 tcp_src_f = Field.new(&quot;tcp.srcport&quot;)

18     local tcp_src = tcp_src_f()</code></pre><p>Refer to the documentation for <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Field.html#lua_class_Field"><code>Field.new</code></a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '16, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54445" class="comments-container"><span id="54478"></span><div id="comment-54478" class="comment"><div id="post-54478-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the answer. I know it's annoying when people post questions that have obvious answers in the docs. I did wander through all that documentation for a day before I posted the question, but as a noob, I just didn't put it all together. However, I got it to work quickly with your brief guidance. All this just to say: thanks for being patient and not blowing off the obvious questions.</p></div><div id="comment-54478-info" class="comment-info"><span class="comment-age">(01 Aug '16, 06:08)</span> J_Turner</div></div><span id="54488"></span><div id="comment-54488" class="comment"><div id="post-54488-score" class="comment-score"></div><div class="comment-text"><p>For the record, I was not annoyed and I apologize if my answer came across if I was. My answer wasn't meant to infer that you hadn't looked at the documentation either, but linking to the documentation, examples, manual, etc. may help you (and others) with similar Lua-related questions in the future.</p></div><div id="comment-54488-info" class="comment-info"><span class="comment-age">(01 Aug '16, 17:12)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-54445" class="comment-tools"></div><div class="clear"></div><div id="comment-54445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

