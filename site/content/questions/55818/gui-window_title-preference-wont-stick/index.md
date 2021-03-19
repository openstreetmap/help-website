+++
type = "question"
title = "GUI window_title  preference won&#x27;t stick"
description = '''Greetings -  At some version point the window title preference stopped working correctly -  using v2.20 on Mac El Capitan, MBP, default profile.  on open, splash page shows correct title preference setting on capture, shows right after capture stop, it&#x27;s right opening prefs shows the gui.window_titl...'''
date = "2016-09-25T19:52:00Z"
lastmod = "2016-09-29T02:58:00Z"
weight = 55818
keywords = [ "window_title" ]
aliases = [ "/questions/55818" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [GUI window\_title preference won't stick](/questions/55818/gui-window_title-preference-wont-stick)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55818-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings -</p><p>At some version point the window title preference stopped working correctly - using v2.20 on Mac El Capitan, MBP, default profile.</p><ol><li>on open, splash page shows correct title preference setting</li><li>on capture, shows right</li><li>after capture stop, it's right</li><li>opening prefs shows the gui.window_title setting is correct</li><li>any opening of prefs, when closed, causes the setting to not work</li><li>open an existing file, and the title is right at first</li><li>then open prefs for anything, and it goes away</li></ol><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-09-25_at_7.50.58_PM.jpg" alt="alt text" /></p><p>Have not tested for what all things cause WS to forget - but this behavior is recent, in my observation - somewhere in the last couple versions. Any suggestions, or have I missed something?</p><p>** note - This operates similarly for the gui.prepend.window_title setting</p><p>TIA John Gonder</p></div><div id="question-tags" class="tags-container tags">window_title</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '16, 19:52</strong></p><img src="https://secure.gravatar.com/avatar/52ff5d6b59bd5798a667a6f346a52421?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetlevel&#39;s gravatar image" /><p>packetlevel<br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetlevel has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '16, 22:47</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-55818" class="comments-container"><span id="55976"></span><div id="comment-55976" class="comment"><div id="post-55976-score" class="comment-score"></div><div class="comment-text"><p>To Jaap -</p><p>Greetings,</p><p>I notice you took the time (and, surprisingly, have the access) to edit my question on the Wireshark wiki.</p><p>Although you have now added spaces and periods in some places, I take it you don’t have any other information that might answer the question.</p><p>If you do, please be so kind as to make a reply.</p><p>Thanks in advance,</p><p>Packetlevel</p><p>Best regards, John Gonder</p></div><div id="comment-55976-info" class="comment-info"><span class="comment-age">(28 Sep '16, 22:38)</span> packetlevel</div></div></div><div id="comment-tools-55818" class="comment-tools"></div><div class="clear"></div><div id="comment-55818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55981"></span>

<div id="answer-container-55981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55981-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This looks to be a bug, any loaded capture filename and title is removed when clicking OK on the preferences dialog.</p><p>Bugs should be reported at the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> in according with the <a href="https://wiki.wireshark.org/ReportingBugs">Reporting Bugs</a> guidelines.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '16, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55981" class="comments-container"><span id="55994"></span><div id="comment-55994" class="comment"><div id="post-55994-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I'll do that - I wasn't sure if I had missed something new/changed in the prefs.</p></div><div id="comment-55994-info" class="comment-info"><span class="comment-age">(29 Sep '16, 11:09)</span> packetlevel</div></div></div><div id="comment-tools-55981" class="comment-tools"></div><div class="clear"></div><div id="comment-55981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

