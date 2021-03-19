+++
type = "question"
title = "copying Preferences from Windows to Linux"
description = '''I can open Wireshark fine on my newly minted Linux box, capture, analyze, looks good. When I exit Wireshark, copy my .preferences directory from Windows to Linux, and then load Wireshark once more ... things most look good: The title bar: The Wireshark Network Analyzer [Wireshark 1.10.2 (SVN Rev Unk...'''
date = "2013-11-14T10:14:00Z"
lastmod = "2013-11-14T21:56:00Z"
weight = 27013
keywords = [ "windows", "gui", "moving", "preferences", "linux" ]
aliases = [ "/questions/27013" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [copying Preferences from Windows to Linux](/questions/27013/copying-preferences-from-windows-to-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can open Wireshark fine on my newly minted Linux box, capture, analyze, looks good.</p><p>When I exit Wireshark, copy my .preferences directory from Windows to Linux, and then load Wireshark once more ... things most look good: The title bar: The Wireshark Network Analyzer [Wireshark 1.10.2 (SVN Rev Unknown from unknown)] The menu bar: File Edit View Go Capture Statistics Telephony Tools Internals Help And the various panels, in brilliant color ... all looks good ... although I notice that the status bar at the bottom is empty ... no way to change Profile, for example ...</p><p>If I select an interface and Start capture ... the screen goes mostly blank: The Title and Menu bars remains ... but everything else turns a light grey. I can still stop capture, using the Capture ... Stop ... and save using File ... Save ... and open using File... Open ... but none of this fixes the display: just grey, no packets, no status bar.</p><p>If I exit Wireshark, nuke ~/.wireshark, and restart, the GUI returns to full functionality.</p><p>So, sounds like some line preferences or preferences_common ... or perhaps in profiles/ ... confuses the GUI.</p><p>I can of course start commenting out preferences ... before I walk that path, any suggestions?</p><p>Ubuntu 12.04.3 LTS</p><p>--sk</p></div><div id="question-tags" class="tags-container tags">windows gui moving preferences linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '13, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/18ae5b8bfddad49931ec557b9342075a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skendric&#39;s gravatar image" /><p>skendric<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skendric has no accepted answers">0%</span></p></div></div><div id="comments-container-27013" class="comments-container"></div><div id="comment-tools-27013" class="comment-tools"></div><div class="clear"></div><div id="comment-27013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27024"></span>

<div id="answer-container-27024" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27024-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to run <code>dos2unix-o *</code> to convert the files</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-27024" class="comments-container"><span id="27034"></span><div id="comment-27034" class="comment"><div id="post-27034-score" class="comment-score"></div><div class="comment-text"><p>Ah, that fixes it, thanx --sk</p></div><div id="comment-27034-info" class="comment-info"><span class="comment-age">(15 Nov '13, 08:23)</span> skendric</div></div><span id="27035"></span><div id="comment-27035" class="comment"><div id="post-27035-score" class="comment-score"></div><div class="comment-text"><p>Good to hear, would you please 'accept' the answer then to close it out.. Thanks</p></div><div id="comment-27035-info" class="comment-info"><span class="comment-age">(15 Nov '13, 08:31)</span> mrEEde</div></div><span id="27043"></span><div id="comment-27043" class="comment"><div id="post-27043-score" class="comment-score"></div><div class="comment-text"><p>I accepted the answer, as the proposed solution fixed the problem.</p><p>Regards<br />
Kurt</p></div><div id="comment-27043-info" class="comment-info"><span class="comment-age">(15 Nov '13, 13:14)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27024" class="comment-tools"></div><div class="clear"></div><div id="comment-27024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

