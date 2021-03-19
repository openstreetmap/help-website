+++
type = "question"
title = "How to chose a capture-filter in version 1.8.0 as previous in the capture-options menu of version 1.6"
description = '''Hello wireshark community With version 1.6 I can choose/select a capture-filter in the capture-options dialog menue. In version 1.8 this option has disappeared in the capture-options dialog menue. How to select a capture-filter in version 1.8 by GUI? Perhaps only now with the -f parameter when I sta...'''
date = "2012-06-26T21:11:00Z"
lastmod = "2012-06-26T21:55:00Z"
weight = 12221
keywords = [ "capture-options", "capture-filter", "1.8.0" ]
aliases = [ "/questions/12221" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to chose a capture-filter in version 1.8.0 as previous in the capture-options menu of version 1.6](/questions/12221/how-to-chose-a-capture-filter-in-version-180-as-previous-in-the-capture-options-menu-of-version-16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12221-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello wireshark community</p><p>With version 1.6 I can choose/select a capture-filter in the capture-options dialog menue. In version 1.8 this option has disappeared in the capture-options dialog menue. How to select a capture-filter in version 1.8 by GUI? Perhaps only now with the -f parameter when I start wireshark?</p><p>I am not a very expirienced user of wireshark yet, but very impressed. Looked and searched in the documentation for my question but didn't find hints for a solution.</p><p>Thank you for your time and for your helpful answers.</p></div><div id="question-tags" class="tags-container tags">capture-options capture-filter 1.8.0</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/ab20caa0f95788cd0ae90a0045543206?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="georg49&#39;s gravatar image" /><p>georg49<br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="georg49 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Aug '12, 11:54</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-12221" class="comments-container"></div><div id="comment-tools-12221" class="comment-tools"></div><div class="clear"></div><div id="comment-12221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12222"></span>

<div id="answer-container-12222" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12222-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark 1.8 now allows capturing on multiple interfaces, and each interface can have its own capture filter, so the capture filter input field has been moved to the interface settings.</p><p>From the Capture Options dialog, double-click on the interface for which you want to set the capture filter. This will take you to the "Edit Interface Settings" dialog, and you will see the capture filter input field.</p><p>Note that the capture filter for each interface is actually shown in the Capture Options dialog, but it's to the far right and you have to scroll the display to make it visible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 21:55</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-12222" class="comments-container"><span id="12224"></span><div id="comment-12224" class="comment"><div id="post-12224-score" class="comment-score"></div><div class="comment-text"><p>Hello Jim</p><p>Thank you very much for your helpful answer. You made me happy cause I almost desperately searched about 2 hours for the solution. Prmanentely thinking that it should/must be there/anywehre but where?! Never doubleclicked on the interface to see that and didn't recognice the column titel in the interface window - so crazy. Thanks a lot again and have a good time.</p><p>Georg</p></div><div id="comment-12224-info" class="comment-info"><span class="comment-age">(26 Jun '12, 22:21)</span> georg49</div></div><span id="12225"></span><div id="comment-12225" class="comment"><div id="post-12225-score" class="comment-score"></div><div class="comment-text"><p>answer accepted</p></div><div id="comment-12225-info" class="comment-info"><span class="comment-age">(26 Jun '12, 22:43)</span> georg49</div></div></div><div id="comment-tools-12222" class="comment-tools"></div><div class="clear"></div><div id="comment-12222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

