+++
type = "question"
title = "Retrieving information inside the dissection tree?"
description = '''I need the uncompressed text of a http response, however with lua it&#x27;s a little tricky to process the compressed data. I think I can use the existing data within the dissection tree, because there is already a dissector done that. But the documentation doesn&#x27;t seem to provide that function. Is this ...'''
date = "2013-12-08T13:33:00Z"
lastmod = "2013-12-08T22:48:00Z"
weight = 27926
keywords = [ "dissector" ]
aliases = [ "/questions/27926" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Retrieving information inside the dissection tree?](/questions/27926/retrieving-information-inside-the-dissection-tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27926-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need the uncompressed text of a http response, however with lua it's a little tricky to process the compressed data. I think I can use the existing data within the dissection tree, because there is already a dissector done that. But the documentation doesn't seem to provide that function. Is this potentially possible?</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '13, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/39442a32c6ceb159821eeb2123154ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacul&#39;s gravatar image" /><p>Jacul<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacul has no accepted answers">0%</span></p></div></div><div id="comments-container-27926" class="comments-container"></div><div id="comment-tools-27926" class="comment-tools"></div><div class="clear"></div><div id="comment-27926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27942"></span>

<div id="answer-container-27942" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27942-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I need the uncompressed text of a http response</p></blockquote><p>Does that HTTP response have a particular MIME media-type value?</p><p>If so, register your dissector in the "media_type" dissector table with the MIME media-type string.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '13, 22:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27942" class="comments-container"><span id="27954"></span><div id="comment-27954" class="comment"><div id="post-27954-score" class="comment-score"></div><div class="comment-text"><p>I think the content type is "text/html". Will the text content be included in the bytebuffer after registering the media type?</p></div><div id="comment-27954-info" class="comment-info"><span class="comment-age">(09 Dec '13, 09:06)</span> Jacul</div></div><span id="27959"></span><div id="comment-27959" class="comment"><div id="post-27959-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I think the content type is "text/html"</p></blockquote><p>You can't register your dissector for that, as there's already a dissector for it (for obvious reasons).</p><p>This means that you will have to look at <strong><em>ALL</em></strong> entity-bodies to see if they happen to correspond to your protocol, before they're handed to media-type-based dissectors.</p><p>This means you'll need to write a heuristic dissector and register it in the "http" heuristic dissector table. See the doc/README.heuristic file in the source for the version of Wireshark you're using. Note that you will have to write this dissector in C, as there is currently no support for heuristic Lua dissectors.</p></div><div id="comment-27959-info" class="comment-info"><span class="comment-age">(09 Dec '13, 11:19)</span> Guy Harris ♦♦</div></div><span id="27960"></span><div id="comment-27960" class="comment"><div id="post-27960-score" class="comment-score"></div><div class="comment-text"><p>Thank you, at least I know where to start now. I think you are the same guy who commented my question in stackoverflow. If you don't mind, can you post a answer there so I can accept it?</p></div><div id="comment-27960-info" class="comment-info"><span class="comment-age">(09 Dec '13, 13:18)</span> Jacul</div></div><span id="27961"></span><div id="comment-27961" class="comment"><div id="post-27961-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I think you are the same guy who commented my question in stackoverflow.</p></blockquote><p>And I thought you were the same guy who asked on Stack Overflow, which is why I put in the note about C and Lua.</p><p>You might want to file a bug on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a> suggesting that support for heuristic Lua dissectors be added.</p><blockquote><p>If you don't mind, can you post a answer there so I can accept it?</p></blockquote><p>OK.</p></div><div id="comment-27961-info" class="comment-info"><span class="comment-age">(09 Dec '13, 14:07)</span> Guy Harris ♦♦</div></div><span id="27965"></span><div id="comment-27965" class="comment"><div id="post-27965-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, that won't work, as there's already a text/html dissector, and that'll get called for all entity-bodies with a Content-Type of text/html; the media-type dissectors are checked before the heuristic ones are called.</p><p>You <em>might</em> be able to hack the epan/dissectors/packet-text-media.c dissector to look for your protocol, or might add a separate heuristic dissector table to it and then register your dissector in <em>that</em> table.</p></div><div id="comment-27965-info" class="comment-info"><span class="comment-age">(09 Dec '13, 17:34)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-27942" class="comment-tools"></div><div class="clear"></div><div id="comment-27942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

