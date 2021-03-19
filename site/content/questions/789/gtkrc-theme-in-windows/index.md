+++
type = "question"
title = "gtkrc theme in Windows"
description = '''While this question is a bit off topic of net sniffing, I am hoping someone might help. I am writing a Windows app using gtk. I see that Wireshark is a gtk app with a gtkrc file. My app works fine with the theme stuff on the developer PC but it doesn&#x27;t when I try to redistribute. Certainly the Wires...'''
date = "2010-11-03T04:13:00Z"
lastmod = "2012-09-22T19:17:00Z"
weight = 789
keywords = [ "gtkrc", "windows" ]
aliases = [ "/questions/789" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [gtkrc theme in Windows](/questions/789/gtkrc-theme-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-789-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While this question is a bit off topic of net sniffing, I am hoping someone might help. I am writing a Windows app using gtk. I see that Wireshark is a gtk app with a gtkrc file. My app works fine with the theme stuff on the developer PC but it doesn't when I try to redistribute. Certainly the Wireshark developers have figured out how to redistribute their app and still have the gtk theme work. Would any of the developers be willing to tell me what they had to do to get the gtk theme stuff to work on windows?</p></div><div id="question-tags" class="tags-container tags">gtkrc windows</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '10, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/38703683661e9a855f79520eea332293?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="damon_register&#39;s gravatar image" /><p>damon_register<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="damon_register has no accepted answers">0%</span></p></div></div><div id="comments-container-789" class="comments-container"></div><div id="comment-tools-789" class="comment-tools"></div><div class="clear"></div><div id="comment-789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="803"></span>

<div id="answer-container-803" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-803-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The best answer is probably to dive into the source code itself...</p><p>You can browse the Wireshark source code at http://anonsvn.wireshark.org/viewvc/ - the "releases" view will let you drill down on a particular version.<br />
</p><p>You can find the GTK-specific code for the latest version at: http://anonsvn.wireshark.org/viewvc/releases/wireshark-1.4.1/gtk/</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '10, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Nov '10, 20:08</p></div></div><div id="comments-container-803" class="comments-container"></div><div id="comment-tools-803" class="comment-tools"></div><div class="clear"></div><div id="comment-803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14454"></span>

<div id="answer-container-14454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14454-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>An old question, but I just happened upon it now while searching for something else ...</p><p>In a nutshell, Wireshark distributes the MS-Windows themed <code>gtkrc</code> file with the Wireshark installer, so that when the user installs Wireshark, [s]he gets a <code>gtkrc</code> file appropriate for the Windows environment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '12, 19:17</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-14454" class="comments-container"></div><div id="comment-tools-14454" class="comment-tools"></div><div class="clear"></div><div id="comment-14454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

