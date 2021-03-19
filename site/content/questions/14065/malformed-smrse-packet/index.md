+++
type = "question"
title = "Malformed smrse packet"
description = '''Hi everyone, Getting &quot;malformed smrse packet (exception occured)&quot; errors on our Win2003 server. Anything I should be concerned about?'''
date = "2012-09-05T15:02:00Z"
lastmod = "2012-09-05T18:51:00Z"
weight = 14065
keywords = [ "smrse", "malformed" ]
aliases = [ "/questions/14065" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed smrse packet](/questions/14065/malformed-smrse-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14065-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>Getting "malformed smrse packet (exception occured)" errors on our Win2003 server. Anything I should be concerned about?</p></div><div id="question-tags" class="tags-container tags">smrse malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '12, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/e09f028a6c2cc569354f0d56c47e9292?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quickpath&#39;s gravatar image" /><p>quickpath<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quickpath has no accepted answers">0%</span></p></div></div><div id="comments-container-14065" class="comments-container"></div><div id="comment-tools-14065" class="comment-tools"></div><div class="clear"></div><div id="comment-14065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14074"></span>

<div id="answer-container-14074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14074-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please refer to the <a href="http://wiki.wireshark.org/Protocols/malformed">malformed</a> wiki page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '12, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-14074" class="comments-container"><span id="14132"></span><div id="comment-14132" class="comment"><div id="post-14132-score" class="comment-score"></div><div class="comment-text"><p>In particular, note the list on that page:</p><blockquote><p>There are three main causes:</p><ul><li>protocol data is malformed</li><li>protocol dissector is buggy</li><li>wrong protocol dissector used</li></ul></blockquote><p>Very often, the third of those is the real reason; for TCP and UDP traffic, Wireshark often has to guess the next protocol for packets based either on a port number or on the packet contents, and can guess wrong. For SMRSE, it's based on the port number; if non-SMRSE traffic goes to or from port 4321, it may be mis-dissected as SMRSE. Try disabling the SMRSE dissector.</p></div><div id="comment-14132-info" class="comment-info"><span class="comment-age">(07 Sep '12, 14:42)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-14074" class="comment-tools"></div><div class="clear"></div><div id="comment-14074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

