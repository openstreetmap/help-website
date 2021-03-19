+++
type = "question"
title = "Dissection Bug (Live Capture)"
description = '''I have a custom plugin for wireshark. I found a bug, but I&#x27;m not sure what causes the bug.  During a live capture my plugin/dissector sometimes does not get called (No dissection information from my dissector), but this only happens sometimes. If I am to save the live capture and open the trace, eve...'''
date = "2015-05-28T14:42:00Z"
lastmod = "2015-05-28T14:42:00Z"
weight = 42736
keywords = [ "capture", "dissector", "bug", "plugin", "wireshark" ]
aliases = [ "/questions/42736" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissection Bug (Live Capture)](/questions/42736/dissection-bug-live-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42736-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a custom plugin for wireshark. I found a bug, but I'm not sure what causes the bug.</p><p>During a live capture my plugin/dissector sometimes does not get called (No dissection information from my dissector), but this only happens sometimes. If I am to save the live capture and open the trace, everything is dissected perfectly, so it seems to be an issue with live capture. Any pointers as to why this is happening.</p><p>Thanks</p><p><strong>Edit:</strong></p><p>Dissector is written in C.</p><p>My plugin reroutes to one of two dissectors.</p><p>I write to the info column before "if(tree)" in my dissectors.</p><p>plugin registration: dissector_add_uint("tcp.port", Y_PORT, _handle); dissector_add_uint("tcp.port", Z_PORT, _handle); heur_dissector_add("udp", dissect_X, proto_X);</p><p>I am using pinfo-&gt;fd-&gt;flags.visited</p></div><div id="question-tags" class="tags-container tags">capture dissector bug plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '15, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/42f084d62348c04d00bd67b129116cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XQW1123&#39;s gravatar image" /><p>XQW1123<br />
<span class="score" title="46 reputation points">46</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XQW1123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 May '15, 07:21</p></div></div><div id="comments-container-42736" class="comments-container"><span id="42738"></span><div id="comment-42738" class="comment"><div id="post-42738-score" class="comment-score">1</div><div class="comment-text"><p>How is your plugin called? Via UDP/TCP port registration - or? Is it written in LUA or C? Do you add stuff to the columns and tree <em>before</em> if(tree)? are you using pinfo-&gt;flags.vissited in your code? Is it a heuristic dissector?</p></div><div id="comment-42738-info" class="comment-info"><span class="comment-age">(29 May '15, 00:01)</span> Anders ♦</div></div><span id="42741"></span><div id="comment-42741" class="comment"><div id="post-42741-score" class="comment-score"></div><div class="comment-text"><p>Dissector is written in C.</p><p>My plugin reroutes to one of two dissectors.</p><p>I write to the info column before "if(tree)" in my dissectors.</p><p>plugin registration: dissector_add_uint("tcp.port", Y_PORT, _handle); dissector_add_uint("tcp.port", Z_PORT, _handle); heur_dissector_add("udp", dissect_X, proto_X);</p><p>Yes I am using pinfo-&gt;fd-&gt;flags.visited</p></div><div id="comment-42741-info" class="comment-info"><span class="comment-age">(29 May '15, 07:19)</span> XQW1123</div></div></div><div id="comment-tools-42736" class="comment-tools"></div><div class="clear"></div><div id="comment-42736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

