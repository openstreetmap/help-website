+++
type = "question"
title = "wireshark bug"
description = '''hi i have built my own dissector and i am getting the following error when i click on one of the fields. (wireshark:3672): Gtk-CRITICAL **: gtk_menu_attach_to_widget: assertion `GTK_IS_MENU (menu)&#x27; failed Any help regarding this issue is appreciated'''
date = "2011-03-22T04:38:00Z"
lastmod = "2011-03-27T11:09:00Z"
weight = 3016
keywords = [ "gtk", "bug", "wireshark" ]
aliases = [ "/questions/3016" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark bug](/questions/3016/wireshark-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi i have built my own dissector and i am getting the following error when i click on one of the fields.</p><p>(wireshark:3672): Gtk-CRITICAL **: gtk_menu_attach_to_widget: assertion `GTK_IS_MENU (menu)' failed</p><p>Any help regarding this issue is appreciated</p></div><div id="question-tags" class="tags-container tags">gtk bug wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '11, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p>niks3089<br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '11, 07:12</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-3016" class="comments-container"><span id="3021"></span><div id="comment-3021" class="comment"><div id="post-3021-score" class="comment-score"></div><div class="comment-text"><p>Wireshark version? Does your dissector have GTK code ?(?!)</p></div><div id="comment-3021-info" class="comment-info"><span class="comment-age">(22 Mar '11, 07:13)</span> Jaap ♦</div></div></div><div id="comment-tools-3016" class="comment-tools"></div><div class="clear"></div><div id="comment-3016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3156"></span>

<div id="answer-container-3156" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3156-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not allow dissector plug ins to add GUI. So this is not a Wireshark bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '11, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/585595b6a24df9b742ebc186788e9a8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harper&#39;s gravatar image" /><p>harper<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harper has no accepted answers">0%</span></p></div></div><div id="comments-container-3156" class="comments-container"><span id="3160"></span><div id="comment-3160" class="comment"><div id="post-3160-score" class="comment-score"></div><div class="comment-text"><p>Well, the question Jaap Keuter asked is whether the dissector does, in fact, include GUI code; that question hasn't been answered. It could be that their dissector includes GUI code (which it shouldn't), or it could be that they're doing something that provokes a bug in Wireshark itself.</p><p>At this point, the right thing to do would be for them to ask in the wireshark-dev mailing list; they might have to show us the code.</p></div><div id="comment-3160-info" class="comment-info"><span class="comment-age">(27 Mar '11, 14:29)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-3156" class="comment-tools"></div><div class="clear"></div><div id="comment-3156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

