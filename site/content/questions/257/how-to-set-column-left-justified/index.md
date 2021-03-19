+++
type = "question"
title = "How to set column left-justified"
description = '''Hello all, Wireshark Version 1.2.5: when I start &quot;Wireshark/Statistics/Service Response Time/SMB...&quot; it will open another window &quot;SMB Service Response Time statistics&quot;. All columns are left-justified inside there. Wireshark Version 1.4.0: Lately I installed the latest Version of Wireshark and the co...'''
date = "2010-09-22T02:00:00Z"
lastmod = "2017-07-26T06:56:00Z"
weight = 257
keywords = [ "justified", "configuration", "smb", "columns" ]
aliases = [ "/questions/257" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to set column left-justified](/questions/257/how-to-set-column-left-justified)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-257-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>Wireshark Version 1.2.5: when I start "Wireshark/Statistics/Service Response Time/SMB..." it will open another window "SMB Service Response Time statistics". All columns are left-justified inside there.</p><p>Wireshark Version 1.4.0: Lately I installed the latest Version of Wireshark and the column "Avg SRT" is right-justified now.</p><p>I compared all "/Wireshark / Edit / Preferences" settings of both installed Versions, but I did not find any possibilities to change anything.</p><p>How could I change this to left-justified again?</p><p>Thks a lot for some ideas.</p><p>Chris</p></div><div id="question-tags" class="tags-container tags">justified configuration smb columns</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '10, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/16c60b60b519644e28e94e0f8b142f9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wenzch&#39;s gravatar image" /><p>wenzch<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wenzch has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '10, 02:06</p></div></div><div id="comments-container-257" class="comments-container"></div><div id="comment-tools-257" class="comment-tools"></div><div class="clear"></div><div id="comment-257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="258"></span>

<div id="answer-container-258" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-258-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no option to left-justify them.</p><p>The change comes from the change in the underlying GUI element; the deprecated element used in Wireshark 1.2 was replace by a new one in 1.4. The code forces all columns right-justified, except for the Procedure column.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '10, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-258" class="comments-container"><span id="259"></span><div id="comment-259" class="comment"><div id="post-259-score" class="comment-score"></div><div class="comment-text"><p>Hello jaap,</p><p>thks for the information! I thought there is a possibility to change it by myself. :-(</p><p>chris</p></div><div id="comment-259-info" class="comment-info"><span class="comment-age">(22 Sep '10, 05:30)</span> wenzch</div></div></div><div id="comment-tools-258" class="comment-tools"></div><div class="clear"></div><div id="comment-258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63132"></span>

<div id="answer-container-63132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63132-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can solve this by change the language to be English instead of System default.</p><p>From the Edit menu, -&gt; Preferences , in the Appearance item (or Ctrl + Shift + P), the bottom droplist sets the Language . By default I think it follows the System Setting --&gt; change to English and it will be left justified</p><p>Regards, Yohai</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '17, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/2b680db6b5e1f336bafa59be9c9ae7c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yohaial&#39;s gravatar image" /><p>yohaial<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yohaial has no accepted answers">0%</span></p></div></div><div id="comments-container-63132" class="comments-container"></div><div id="comment-tools-63132" class="comment-tools"></div><div class="clear"></div><div id="comment-63132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

