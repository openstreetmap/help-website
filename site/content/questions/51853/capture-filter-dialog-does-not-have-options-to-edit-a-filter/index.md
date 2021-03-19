+++
type = "question"
title = "Capture filter dialog does not have options to edit a filter."
description = '''Capture filter dialog looks different than shown in help. There are 6 buttons on the bottom - create, remove, copy, OK Cancel Help. No way to specify a filter string or to save the filter. What is wrong?'''
date = "2016-04-21T17:17:00Z"
lastmod = "2016-04-24T17:44:00Z"
weight = 51853
keywords = [ "capture-filter" ]
aliases = [ "/questions/51853" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter dialog does not have options to edit a filter.](/questions/51853/capture-filter-dialog-does-not-have-options-to-edit-a-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51853-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Capture filter dialog looks different than shown in help. There are 6 buttons on the bottom - create, remove, copy, OK Cancel Help. No way to specify a filter string or to save the filter. What is wrong?<img src="https://osqa-ask.wireshark.org/upfiles/ScreenShot033.gif" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '16, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/1c9bd03b66f4d4b5832b8053a1479db9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bgailer&#39;s gravatar image" /><p>bgailer<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bgailer has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51853" class="comments-container"></div><div id="comment-tools-51853" class="comment-tools"></div><div class="clear"></div><div id="comment-51853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51873"></span>

<div id="answer-container-51873" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51873-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Double click the "Filter" field to edit in-line. Hit enter to save it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '16, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51873" class="comments-container"><span id="51916"></span><div id="comment-51916" class="comment"><div id="post-51916-score" class="comment-score"></div><div class="comment-text"><p>All that does is let me edit the name. The dialog shown in help (see below) lets me do other (more useful) things.<img src="https://osqa-ask.wireshark.org/upfiles/ScreenShot034.gif" alt="alt text" /></p></div><div id="comment-51916-info" class="comment-info"><span class="comment-age">(24 Apr '16, 15:52)</span> bgailer</div></div><span id="51919"></span><div id="comment-51919" class="comment"><div id="post-51919-score" class="comment-score"></div><div class="comment-text"><p>Note I said to click a "Filter" field. That's the column of entries with filter expressions in.</p><p>As @Jim Aragon noted, double clicking a Name field, i.e. the column of entries with filter names in, allows you to edit the filter name.</p><p>The thing I see missing from the Qt version of the "Display Filters" dialog is the "Expression builder" button, and that isn't present on the GTK legacy capture filter dialog which was your original question.</p><p>If there is no current item outstanding for this on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>, please raise an "enhancement" request to have it added.</p></div><div id="comment-51919-info" class="comment-info"><span class="comment-age">(25 Apr '16, 02:39)</span> grahamb ♦</div></div></div><div id="comment-tools-51873" class="comment-tools"></div><div class="clear"></div><div id="comment-51873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51917"></span>

<div id="answer-container-51917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51917-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Double-click the Name field to edit the name; double-click the Filter field to edit the filter. All the functionality of the old dialog is present in the new interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '16, 17:44</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></img></div></div><div id="comments-container-51917" class="comments-container"></div><div id="comment-tools-51917" class="comment-tools"></div><div class="clear"></div><div id="comment-51917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

