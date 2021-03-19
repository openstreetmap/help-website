+++
type = "question"
title = "Nested LUA Dissector with CIGI"
description = '''I&#x27;m trying to write a LUA Dissector which consumes some bytes and calls the existing dissector CIGI for the rest of the package. As in Multi-Protocol-Dissector stated, i tried to get a reference to the CIGI dissector with myDissector = Dissector.get(&quot;cigi&quot;) but i&#x27;m not able to get a valid Dissector....'''
date = "2014-05-13T04:34:00Z"
lastmod = "2014-05-13T05:52:00Z"
weight = 32754
keywords = [ "cigi", "lua", "dissector" ]
aliases = [ "/questions/32754" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nested LUA Dissector with CIGI](/questions/32754/nested-lua-dissector-with-cigi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32754-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to write a LUA Dissector which consumes some bytes and calls the existing dissector CIGI for the rest of the package. As in <a href="http://ask.wireshark.org/questions/10658/how-to-use-lua-to-write-multi-protocol-dissector-plugin">Multi-Protocol-Dissector</a> stated, i tried to get a reference to the CIGI dissector with</p><p><code>myDissector = Dissector.get("cigi")</code></p><p>but i'm not able to get a valid Dissector. Even not as in <a href="http://ask.wireshark.org/questions/29841/lua-dissectorget-cant-find-an-existing-dissector">"can't find existing Dissector"</a> stated with</p><p><code>DissectorTable.get("udp.port"):get_dissector("8005") or DissectorTable.get("udp.port"):get_dissector(8005) or DissectorTable.get("udp.port"):get_dissector("cigi") or DissectorTable.get("udp.port"):get_dissector("CIGI")</code></p><p>My dissector looks like this so far:</p><pre><code>myCIGI = Proto(&quot;My CIGI&quot;, &quot;My CIGI Interface&quot;)

function myCIGI.dissector(buffer,pinfo,tree)
  local subtree = tree:add(myCIGI, buffer, &quot;My Header&quot;)
  subtree:add(buffer(0,1), &quot;Header: &quot; .. buffer(0,1):uint())
  cigi_dissector = Dissector.get(&quot;cigi&quot;)
  sub_buf = buffer(1):tvb()
  cigi_dissector:call(sub_buf,pinfo,tree)
end

upd_tabe = DissectorTable.get(&quot;udp.port&quot;)
udp_table:add(8014, myCIGI)
udp_table:add(8015, myCIGI)</code></pre><p>Because of the small protocoll extension of myCIGI a would like to avoid to write a complete new dissector in C.</p><p>Thanks for any help.</p></div><div id="question-tags" class="tags-container tags">cigi lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '14, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/20f3e6e33e15cb5b154971af8f477dd5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="athomi&#39;s gravatar image" /><p>athomi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="athomi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 May '14, 04:46</p></div></div><div id="comments-container-32754" class="comments-container"></div><div id="comment-tools-32754" class="comment-tools"></div><div class="clear"></div><div id="comment-32754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32757"></span>

<div id="answer-container-32757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32757-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>For that to work the CIGI dissector needs to register by name with</p><pre><code>new_register_dissector() or register_dissector().</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '14, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32757" class="comments-container"><span id="32758"></span><div id="comment-32758" class="comment"><div id="post-32758-score" class="comment-score"></div><div class="comment-text"><p>This means i should send a "feature request" or "bug report" to the maintainers of the cigi dissector? On the developer mailing list?</p></div><div id="comment-32758-info" class="comment-info"><span class="comment-age">(13 May '14, 06:24)</span> athomi</div></div><span id="32759"></span><div id="comment-32759" class="comment"><div id="post-32759-score" class="comment-score"></div><div class="comment-text"><p>Use the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a>.</p></div><div id="comment-32759-info" class="comment-info"><span class="comment-age">(13 May '14, 06:49)</span> grahamb ♦</div></div></div><div id="comment-tools-32757" class="comment-tools"></div><div class="clear"></div><div id="comment-32757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

