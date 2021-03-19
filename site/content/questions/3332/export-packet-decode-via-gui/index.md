+++
type = "question"
title = "export packet decode via GUI"
description = '''I&#x27;ve been using Tshark line like this a lot lately: tshark.exe -r somefile.pcap -R &#x27;frame.number==5&#x27; -V which gives me a nice complete plaintext decode of a single frame. I&#x27;m sure there must be a way to get the whole packet decode as plain text in the GUI after applying the display filter, but I jus...'''
date = "2011-04-04T15:50:00Z"
lastmod = "2011-04-05T07:35:00Z"
weight = 3332
keywords = [ "text", "tshark" ]
aliases = [ "/questions/3332" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [export packet decode via GUI](/questions/3332/export-packet-decode-via-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3332-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using Tshark line like this a lot lately:</p><p>tshark.exe -r somefile.pcap -R 'frame.number==5' -V</p><p>which gives me a nice complete plaintext decode of a single frame. I'm sure there must be a way to get the whole packet decode as plain text in the GUI after applying the display filter, but I just can't find it. What am I missing?</p></div><div id="question-tags" class="tags-container tags">text tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '11, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/8d955195202bfccc131e41c435bc382a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jswan&#39;s gravatar image" /><p>jswan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jswan has no accepted answers">0%</span></p></div></div><div id="comments-container-3332" class="comments-container"></div><div id="comment-tools-3332" class="comment-tools"></div><div class="clear"></div><div id="comment-3332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3333"></span>

<div id="answer-container-3333" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3333-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try this:</p><ol><li>Apply the display filter after loading the trace</li><li>Choose "File" -&gt; "Export" -&gt; "File"</li><li>Select "Save as Type" as "Plain Text"</li><li>Mark "Packet Range" radio button as "Displayed"</li><li>Set the Packet Format according to your wishes, usually only "Packet Details" -&gt; "All Expanded" or "As displayed"</li></ol><p>Is that what you were looking for?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '11, 18:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3333" class="comments-container"></div><div id="comment-tools-3333" class="comment-tools"></div><div class="clear"></div><div id="comment-3333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3343"></span>

<div id="answer-container-3343" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3343-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's it! I was missing the "as displayed" option under "Packet details".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '11, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/8d955195202bfccc131e41c435bc382a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jswan&#39;s gravatar image" /><p>jswan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jswan has no accepted answers">0%</span></p></div></div><div id="comments-container-3343" class="comments-container"></div><div id="comment-tools-3343" class="comment-tools"></div><div class="clear"></div><div id="comment-3343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

