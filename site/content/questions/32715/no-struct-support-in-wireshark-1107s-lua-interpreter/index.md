+++
type = "question"
title = "No struct support in wireshark 1.10.7&#x27;s lua interpreter?"
description = '''I don&#x27;t seem to be able to use Struct.pack and Struct.unpack in the lua interpreter for the latest OSX version of 1.10.7. I got an &quot;attempt to index global &#x27;Struct&#x27; (a nil value)&quot; error even though Wireshark appears to have Struct support at least in the documentation section and one of the check-in...'''
date = "2014-05-11T15:41:00Z"
lastmod = "2014-05-11T22:51:00Z"
weight = 32715
keywords = [ "lua", "struct.unpack", "wireshark" ]
aliases = [ "/questions/32715" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [No struct support in wireshark 1.10.7's lua interpreter?](/questions/32715/no-struct-support-in-wireshark-1107s-lua-interpreter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I don't seem to be able to use Struct.pack and Struct.unpack in the lua interpreter for the latest OSX version of 1.10.7.</p><p>I got an "attempt to index global 'Struct' (a nil value)" error even though Wireshark appears to have Struct support at least in the documentation section and one of the check-in messages.</p><p><a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Struct.html#lua_class_Struct">http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Struct.html#lua_class_Struct</a></p><p><a href="http://www.wireshark.org/lists/wireshark-commits/201402/msg00189.html">http://www.wireshark.org/lists/wireshark-commits/201402/msg00189.html</a></p></div><div id="question-tags" class="tags-container tags">lua struct.unpack wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '14, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/a62363ccc3a8c07a89c2a5e21bb57b01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="software%20engineer&#39;s gravatar image" /><p>software eng...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="software engineer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 May '14, 15:41</p></div></div><div id="comments-container-32715" class="comments-container"></div><div id="comment-tools-32715" class="comment-tools"></div><div class="clear"></div><div id="comment-32715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32718"></span>

<div id="answer-container-32718" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32718-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This commit was done in the development (master) branch and not in the stable (master-1.10) branch. You should use the Wireshark 1.11.3 release found on the website or a later development snapshot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '14, 22:51</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-32718" class="comments-container"><span id="32720"></span><div id="comment-32720" class="comment"><div id="post-32720-score" class="comment-score"></div><div class="comment-text"><p>Thanks. It wasnt obvious from the commit link which version it went into.</p></div><div id="comment-32720-info" class="comment-info"><span class="comment-age">(11 May '14, 23:14)</span> software eng...</div></div><span id="32733"></span><div id="comment-32733" class="comment"><div id="post-32733-score" class="comment-score"></div><div class="comment-text"><p>The API doc should say it's "Since 1.11.3" for Struct, as it does for the other new things... but does not do for Struct. I'll fix it when I get some free time this week.</p></div><div id="comment-32733-info" class="comment-info"><span class="comment-age">(12 May '14, 09:09)</span> Hadriel</div></div></div><div id="comment-tools-32718" class="comment-tools"></div><div class="clear"></div><div id="comment-32718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

