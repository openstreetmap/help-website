+++
type = "question"
title = "Capture Interfaces window"
description = '''I am using version 2.05, on an HP laptop running Windows 7. When I open the Capture Interfaces window (Capture-Options), I do not see the same screen as is shown in the UG (4.4. The “Capture Interfaces” dialog box – Figure 4.1) On my version, the Traffic column only shows a graph of the traffic flow...'''
date = "2016-08-24T12:42:00Z"
lastmod = "2016-08-24T15:16:00Z"
weight = 55097
keywords = [ "capture", "interfaces" ]
aliases = [ "/questions/55097" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Interfaces window](/questions/55097/capture-interfaces-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55097-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using version 2.05, on an HP laptop running Windows 7. When I open the Capture Interfaces window (Capture-Options), I do not see the same screen as is shown in the UG (4.4. The “Capture Interfaces” dialog box – Figure 4.1)</p><p>On my version, the Traffic column only shows a graph of the traffic flow.</p><p>Specifically, I am looking for the two columns on the right of the window shown in the UG: Packets and Packets/s</p></div><div id="question-tags" class="tags-container tags">capture interfaces</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '16, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/c7c839478e46a5bdf0a4201dfd47cb7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PHeat&#39;s gravatar image" /><p>PHeat<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PHeat has no accepted answers">0%</span></p></div></div><div id="comments-container-55097" class="comments-container"></div><div id="comment-tools-55097" class="comment-tools"></div><div class="clear"></div><div id="comment-55097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55101"></span>

<div id="answer-container-55101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55101-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Despite the text in the User Guide stating that Capture -&gt; Options displayed the Capture Interfaces dialog, it is actually the Capture -&gt; Interfaces menu item that does so.</p><p>The menu item and dialog is in the legacy (GTK) version and has not been carried over to the new Qt version with the redesign of the presentation of capture interfaces using sparklines to show activity.</p><p>The documentation does need some updates though, thanks for pointing that out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '16, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55101" class="comments-container"><span id="55104"></span><div id="comment-55104" class="comment"><div id="post-55104-score" class="comment-score"></div><div class="comment-text"><p>grahamb,</p><p>Thanks for the explanation.</p><p>NOTE: I cannot find the Capture-&gt;Interfaces menu selection. On the version I have installed (v2.05), the selections under the Capture drop down menu are: Options Start Stop Restart Capture Filters ... Refresh Interfaces</p></div><div id="comment-55104-info" class="comment-info"><span class="comment-age">(24 Aug '16, 23:09)</span> PHeat</div></div><span id="55106"></span><div id="comment-55106" class="comment"><div id="post-55106-score" class="comment-score"></div><div class="comment-text"><p>Yes, the item Interfaces under the Capture menu has been removed in the 2.x Qt version, along with the associated Capture Interfaces dialog (or more accurately never implemented) as it was replaced by the graphical sparklines indicting interface traffic.</p><p>If you really want the old menu and dialog, then you'll have to run the legacy GTK version.</p></div><div id="comment-55106-info" class="comment-info"><span class="comment-age">(25 Aug '16, 01:35)</span> grahamb ♦</div></div></div><div id="comment-tools-55101" class="comment-tools"></div><div class="clear"></div><div id="comment-55101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

