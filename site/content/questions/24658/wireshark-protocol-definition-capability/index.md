+++
type = "question"
title = "Wireshark protocol definition capability"
description = '''Subject: Wireshark protocol definition capability I have a question about using Wireshark to capture/decode what I would call application packets inside of TCP or UDP packets. I am working on an enterprise messaging protocol standard that would use the TCP or UDP data payload to transport structured...'''
date = "2013-09-13T14:00:00Z"
lastmod = "2013-09-13T16:01:00Z"
weight = 24658
keywords = [ "definition", "protocol" ]
aliases = [ "/questions/24658" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark protocol definition capability](/questions/24658/wireshark-protocol-definition-capability)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24658-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Subject: Wireshark protocol definition capability I have a question about using Wireshark to capture/decode what I would call application packets inside of TCP or UDP packets. I am working on an enterprise messaging protocol standard that would use the TCP or UDP data payload to transport structured messages between any number of servers. I'm anticipating that if Wireshark can support filter captures of this kind of enterprise messaging that enterprise conversations might be able to be captured and decoded. By decoded, I am making an assumption that there is a facility within Wireshark to define the structured data protocol and on display after capture to have it decoded in terms of what named data fields have for data content.</p><p>Can you define structured data packets like I know Wireshark must have definitions of encapsulaed headers for different Internet protocols, etc?</p><p>Appreciate any reply and pointers to guide me in the right direction. Thanks.</p><p>Don Johnston University of Illinois</p></div><div id="question-tags" class="tags-container tags">definition protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '13, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/7cd43aa57b215b1bca13d9364fcf3b62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dljohnst&#39;s gravatar image" /><p>dljohnst<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dljohnst has no accepted answers">0%</span></p></div></div><div id="comments-container-24658" class="comments-container"></div><div id="comment-tools-24658" class="comment-tools"></div><div class="clear"></div><div id="comment-24658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24659"></span>

<div id="answer-container-24659" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24659-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you are describing sounds to me like you're interested in writing a Wireshark dissector. You might want to start with the Wireshark <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">Developer's Guide</a>.</p><p>And be sure to also read the various <code>README</code> files in the top-level and <code>doc/</code> directories, particularly <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer?revision=51739&amp;view=markup">doc/README.developer</a> and <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.dissector?revision=50557&amp;view=markup">doc/README.dissector</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24659" class="comments-container"></div><div id="comment-tools-24659" class="comment-tools"></div><div class="clear"></div><div id="comment-24659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24661"></span>

<div id="answer-container-24661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24661-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As the answer from @cmaynard states, you are looking at creating a dissector for your protocol. There are a few options for doing this:</p><ol><li>Using a text description of your protocol with <a href="http://wsgd.free.fr/">WSGD</a>.</li><li>Using a scripting language built-in to Wireshark, e.g. Lua.</li><li>Writing a C dissector, possibly as a plug-in.</li></ol><p>All three options were discussed in my presentation at SharkFest '13, <a href="http://sharkfest.wireshark.org/sharkfest.13/presentations/PA-10_Writing-a-Wireshark-Dissector_Graham-Bloice.zip">Writing a Wireshark Dissector</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24661" class="comments-container"><span id="24697"></span><div id="comment-24697" class="comment"><div id="post-24697-score" class="comment-score"></div><div class="comment-text"><p>Should the developer's guide be updated to mention WSGD, Lua and even the ptvcursor API? And then there's <a href="http://wiki.wireshark.org/Mate">MATE</a>. And <a href="https://code.google.com/p/pyreshark/">pyreshark</a>.</p></div><div id="comment-24697-info" class="comment-info"><span class="comment-age">(14 Sep '13, 16:10)</span> cmaynard ♦♦</div></div><span id="24710"></span><div id="comment-24710" class="comment"><div id="post-24710-score" class="comment-score"></div><div class="comment-text"><p>All good candidates for listing somewhere. Maybe a wiki page as well.</p></div><div id="comment-24710-info" class="comment-info"><span class="comment-age">(15 Sep '13, 01:15)</span> grahamb ♦</div></div></div><div id="comment-tools-24661" class="comment-tools"></div><div class="clear"></div><div id="comment-24661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

