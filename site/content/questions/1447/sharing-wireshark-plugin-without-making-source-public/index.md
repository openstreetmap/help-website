+++
type = "question"
title = "Sharing wireshark plugin without making source public"
description = '''Can I share wireshark plugin in the form of a DLL or .so to a customer without making the source code public for debugging activity? Please note that I am not billing the customer for this.'''
date = "2010-12-21T20:58:00Z"
lastmod = "2010-12-31T09:08:00Z"
weight = 1447
keywords = [ "license" ]
aliases = [ "/questions/1447" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Sharing wireshark plugin without making source public](/questions/1447/sharing-wireshark-plugin-without-making-source-public)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1447-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I share wireshark plugin in the form of a DLL or .so to a customer without making the source code public for debugging activity? Please note that I am <em>not</em> billing the customer for this.</p></div><div id="question-tags" class="tags-container tags">license</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '10, 20:58</strong></p><img src="https://secure.gravatar.com/avatar/08f32793008d238220f2637b313479a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neeraj&#39;s gravatar image" /><p>neeraj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neeraj has no accepted answers">0%</span></p></div></div><div id="comments-container-1447" class="comments-container"></div><div id="comment-tools-1447" class="comment-tools"></div><div class="clear"></div><div id="comment-1447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1449"></span>

<div id="answer-container-1449" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1449-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can share the plugin with the customer, but you'll be required to provide the source code if so requested. You cannot limit what the customer does with the plugin and/or source code, as per <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">GPLv2</a> which is applicable to your Wireshark dissector plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '10, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1449" class="comments-container"></div><div id="comment-tools-1449" class="comment-tools"></div><div class="clear"></div><div id="comment-1449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1560"></span>

<div id="answer-container-1560" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1560-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may also want to note that the plugin will not necessarily be portable to the next version of Wireshark, so if your customer ever wishes to use a different version of Wireshark, they may not be able to do so and use your provided .dll or .so plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '10, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p>beroset<br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span></p></div></div><div id="comments-container-1560" class="comments-container"></div><div id="comment-tools-1560" class="comment-tools"></div><div class="clear"></div><div id="comment-1560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

