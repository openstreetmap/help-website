+++
type = "question"
title = "Wireshark 2 Configuration Persistence"
description = '''The setting in the &quot;View&quot; menu do not seem to persist when using Wireshark 2. Here are the steps I am performing:  From the View menu, deselect the Main Toolbar so it isn&#x27;t shown Close Wireshark Open Wireshark - the Main Toolbar is back to visible. I expect the setting to persist!  I looked at the &quot;...'''
date = "2016-08-09T08:25:00Z"
lastmod = "2016-08-09T08:45:00Z"
weight = 54703
keywords = [ "profile", "configuration", "wireshark-2.0", "settings" ]
aliases = [ "/questions/54703" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2 Configuration Persistence](/questions/54703/wireshark-2-configuration-persistence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54703-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The setting in the "View" menu do not seem to persist when using Wireshark 2. Here are the steps I am performing:</p><ol><li>From the View menu, deselect the Main Toolbar so it isn't shown</li><li>Close Wireshark</li><li>Open Wireshark - the Main Toolbar is back to visible. I expect the setting to persist!</li></ol><p>I looked at the "recent" file in ...\AppData\Roaming\Wireshark\, and the gui.toolbar_main_show: gets written to the proper value (according to the view menu setting) when Wireshark is closed. However, when opened again, Wireshark ignores this setting. The view menu shows the main toolbar as checked (enabled), regardless of the contents of the "recent" file when launching the app.</p><p>I have also tried creating a custom profile, and it behaves the same way; Wireshark ignores the "recent" file when launching, and consequently the settings are not persistent.</p><p>The Wireshark Legacy performs like I think it should. It respects the settings in the "recent" file when opening. Surely I am not the only one seeing this issue.</p><p>Here is the platform that I am having the issue on:</p><p>Wireshark v2.0.5 Windows 7 Enterprise</p></div><div id="question-tags" class="tags-container tags">profile configuration wireshark-2.0 settings</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '16, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/6acf3c1293dde7d08c204b9265e46764?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J_Turner&#39;s gravatar image" /><p>J_Turner<br />
<span class="score" title="71 reputation points">71</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J_Turner has no accepted answers">0%</span></p></div></div><div id="comments-container-54703" class="comments-container"></div><div id="comment-tools-54703" class="comment-tools"></div><div class="clear"></div><div id="comment-54703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54704"></span>

<div id="answer-container-54704" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54704-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This doesn't seem to be limited to the toolbar either, at least the filter and status bar items are similarly afflicted.</p><p>Anyway, the place for this if you wish to see it fixed is to raise an entry on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '16, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-54704" class="comments-container"><span id="54706"></span><div id="comment-54706" class="comment"><div id="post-54706-score" class="comment-score"></div><div class="comment-text"><p>OK. It seems like a rather common item, so I thought surely I must be doing something wrong. But, it sounds like it is indeed a bug. I'll put it on the Bug Tracker.</p></div><div id="comment-54706-info" class="comment-info"><span class="comment-age">(09 Aug '16, 09:27)</span> J_Turner</div></div></div><div id="comment-tools-54704" class="comment-tools"></div><div class="clear"></div><div id="comment-54704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

