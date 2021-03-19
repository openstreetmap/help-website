+++
type = "question"
title = "Calling a Lua Dissector on a file"
description = '''Hi all, I&#x27;ve been using Wireshark for a while and also building LUA dissectors for some proprietary protocols. Before you can use a dissector, you need to add it to the appropriate dissector table. I would like to use the abilities from Wireshark to represent the contents of a binary file, similar t...'''
date = "2013-12-30T02:42:00Z"
lastmod = "2016-12-21T02:48:00Z"
weight = 28474
keywords = [ "eservcinreturns" ]
aliases = [ "/questions/28474" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Calling a Lua Dissector on a file](/questions/28474/calling-a-lua-dissector-on-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28474-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I've been using Wireshark for a while and also building LUA dissectors for some proprietary protocols. Before you can use a dissector, you need to add it to the appropriate dissector table. I would like to use the abilities from Wireshark to represent the contents of a binary file, similar to "ASN.1 Basic Encoding Rules(<em>.</em>)" however I do not know if it is possible to register a dissector for use as file dissector. I can understand that the dissectors are called on packets read, however this would make it very powerfull in some occasions.</p><p>Thanks and best regards,</p><p>Sjoerd</p></div><div id="question-tags" class="tags-container tags">eservcinreturns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '13, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/c843c60e3ee5619adccdc472ed64e8c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sjoerdvandoorn&#39;s gravatar image" /><p>sjoerdvandoorn<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sjoerdvandoorn has no accepted answers">0%</span></p></div></div><div id="comments-container-28474" class="comments-container"></div><div id="comment-tools-28474" class="comment-tools"></div><div class="clear"></div><div id="comment-28474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28482"></span>

<div id="answer-container-28482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28482-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>however I do not know if it is possible to register a dissector for use as file dissector.</p></blockquote><p>No, that's not possible.</p><blockquote><p>however this would make it very powerfull in some occasions.</p></blockquote><p>Yes, and that's why a similar project has already been started (TFShark - Terminal FileShark)</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9607">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9607</a></p></blockquote><p>Maybe you want to take a look at that and probably contribute ideas and/or code.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '13, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28482" class="comments-container"></div><div id="comment-tools-28482" class="comment-tools"></div><div class="clear"></div><div id="comment-28482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58271"></span>

<div id="answer-container-58271" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58271-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is possible to register a dissector for the file in Lua, but involves two steps:</p><ol><li>Register a <code>FileHandler</code> which accepts a file and provides a MIME encapsulation type.</li><li>Register a heuristics dissector for the MIME file encapsulation table and add your dissector in there.</li></ol><p>I am working on a Zip Archive file dissector for Lua, but you can probably adjust this template to your needs: <a href="https://git.lekensteyn.nl/peter/wireshark-notes/commit/?id=bad766a9ef81f7267cdb8e4f82db692a83ba2f9a">https://git.lekensteyn.nl/peter/wireshark-notes/commit/?id=bad766a9ef81f7267cdb8e4f82db692a83ba2f9a</a></p><p>Examples of usage:</p><pre><code>tshark -Xlua_script:file-zip.lua -r sample.zip
wireshark -Xlua_script:file-zip.lua -r sample.zip</code></pre><p>Other examples of a FileHandler can be found in the Wireshark source tree (<code>test/lua/acme_file.lua</code> and <code>test/lua/pcap_file.lua</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '16, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-58271" class="comments-container"></div><div id="comment-tools-58271" class="comment-tools"></div><div class="clear"></div><div id="comment-58271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

