+++
type = "question"
title = "Implementing a &quot;next capture in directory&quot; feature"
description = '''I&#x27;m not a coder, but I use Wireshark daily as I work at a networking company. I often have to go through hundreds of captures one-by-one, and right now I close each Wireshark instance and then open the next file (opening the next one in Wireshark itself is a pain because it jumps to the top of the d...'''
date = "2012-01-10T09:21:00Z"
lastmod = "2012-01-10T13:44:00Z"
weight = 8304
keywords = [ "efficiency", "open", "batch", "capture" ]
aliases = [ "/questions/8304" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Implementing a "next capture in directory" feature](/questions/8304/implementing-a-next-capture-in-directory-feature)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8304-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm not a coder, but I use Wireshark daily as I work at a networking company. I often have to go through hundreds of captures one-by-one, and right now I close each Wireshark instance and then open the next file (opening the next one in Wireshark itself is a pain because it jumps to the top of the directory each time). Perhaps it might be nice to be able to go forward and backward in a directory of capture files (like an "open" shortcut).</p><p>If such a function already exists, let me know. Thanks.</p></div><div id="question-tags" class="tags-container tags">efficiency open batch capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '12, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/4bd87cd218657feabb638ddc636084df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred%20Meissner&#39;s gravatar image" /><p>Fred Meissner<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred Meissner has no accepted answers">0%</span></p></div></div><div id="comments-container-8304" class="comments-container"></div><div id="comment-tools-8304" class="comment-tools"></div><div class="clear"></div><div id="comment-8304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8310"></span>

<div id="answer-container-8310" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8310-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Note sure if this helps, but did you find the "File Set -&gt; "List Files" menu item in the "File" menu? It will give you a list of files that belong together, usually after doing a ring buffer capture, and you can jump back and forth. Doesn't help with files that do not have the naming scheme of a ring buffer capture though - at least last time I checked it didn't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '12, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8310" class="comments-container"><span id="8352"></span><div id="comment-8352" class="comment"><div id="post-8352-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, but that doesn't work so well since the captures must be named with the test number first, so they don't follow the same prefix.</p></div><div id="comment-8352-info" class="comment-info"><span class="comment-age">(12 Jan '12, 11:36)</span> Fred Meissner</div></div></div><div id="comment-tools-8310" class="comment-tools"></div><div class="clear"></div><div id="comment-8310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

