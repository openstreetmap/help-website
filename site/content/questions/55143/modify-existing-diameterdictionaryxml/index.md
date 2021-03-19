+++
type = "question"
title = "Modify existing diameter/dictionary.xml"
description = '''If I modify dictionary.xml in the diameter folder to add another AVP or parse out more detail within an existing AVP do I need to rebuild? If yes what do I need to do on Windows7?'''
date = "2016-08-27T22:55:00Z"
lastmod = "2016-08-27T23:07:00Z"
weight = 55143
keywords = [ "diameter" ]
aliases = [ "/questions/55143" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Modify existing diameter/dictionary.xml](/questions/55143/modify-existing-diameterdictionaryxml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55143-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I modify dictionary.xml in the diameter folder to add another AVP or parse out more detail within an existing AVP do I need to rebuild? If yes what do I need to do on Windows7?</p></div><div id="question-tags" class="tags-container tags">diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '16, 22:55</strong></p><img src="https://secure.gravatar.com/avatar/00e21f3840a9bb6488f254f9ec0a1bf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_BR&#39;s gravatar image" /><p>_BR<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_BR has no accepted answers">0%</span></p></div></div><div id="comments-container-55143" class="comments-container"></div><div id="comment-tools-55143" class="comment-tools"></div><div class="clear"></div><div id="comment-55143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55144"></span>

<div id="answer-container-55144" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55144-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To add a new AVP you just need to add it to the existing files and restart wireshark. To add more detail you have to modify the dissector e.g write c code and recompile see packet-diameter_3gpp.c ad an example. It might be possible in Lua too. If you are adding standard AVPs please send us a patch so it can be included in the next release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '16, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-55144" class="comments-container"><span id="55167"></span><div id="comment-55167" class="comment"><div id="post-55167-score" class="comment-score"></div><div class="comment-text"><p>thank you. follow up question. I would like to have additional decoding for AVP 2516 (EUTRAN-Positioning-Data). It is in 3gpp 29.172. So I still need to modify packet-diameter_3gpp.c?<br />
</p></div><div id="comment-55167-info" class="comment-info"><span class="comment-age">(29 Aug '16, 08:29)</span> _BR</div></div><span id="55168"></span><div id="comment-55168" class="comment"><div id="post-55168-score" class="comment-score"></div><div class="comment-text"><p>That may recently have been added to trunk, I don't have easy access to the sources currently. Try a development build.</p></div><div id="comment-55168-info" class="comment-info"><span class="comment-age">(29 Aug '16, 09:03)</span> Anders ♦</div></div></div><div id="comment-tools-55144" class="comment-tools"></div><div class="clear"></div><div id="comment-55144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

