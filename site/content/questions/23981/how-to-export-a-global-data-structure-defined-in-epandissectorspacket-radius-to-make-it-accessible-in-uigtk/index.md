+++
type = "question"
title = "How to export a global data structure defined in epan/dissectors/packet-radius to make it accessible in ui/gtk?"
description = '''I have defined a global data structure inside epan/dissector/packet-radius, which I am using to store some radius state handling information. I would like to display the information stored in this data structure inside the Statistics-&amp;gt;Summary dialogue window. I am not sure how to export the data ...'''
date = "2013-08-23T06:47:00Z"
lastmod = "2013-08-24T11:58:00Z"
weight = 23981
keywords = [ "export", "udp", "data", "menu", "wireshark" ]
aliases = [ "/questions/23981" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to export a global data structure defined in epan/dissectors/packet-radius to make it accessible in ui/gtk?](/questions/23981/how-to-export-a-global-data-structure-defined-in-epandissectorspacket-radius-to-make-it-accessible-in-uigtk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23981-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have defined a global data structure inside epan/dissector/packet-radius, which I am using to store some radius state handling information. I would like to display the information stored in this data structure inside the Statistics-&gt;Summary dialogue window.</p><p>I am not sure how to export the data structure defined in epan/dissector/packet-radius.c to make it available to ui/gtk/summary_dlg.c</p><p>I did this long back in Wireshark-1.0.1 using the following steps:</p><ol><li><p>Add following to epan/dissector/packet-radius.h</p><p>WS_VAR_IMPORT struct radius_call_state* radius_stathead;</p></li><li><p>Export stathead in epan/libwireshark.def</p><p>radius_stathead DATA</p></li></ol><p>But, it seems that "WS_VAR_IMPORT" and "epan/libwireshark.def" are not being used in the latest Wireshark version (1.10.1).</p><p>Any help on this is appreciated.</p></div><div id="question-tags" class="tags-container tags">export udp data menu wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '13, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/60bdd63251a0e3e8ace45fb1ec16f73a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kkg78&#39;s gravatar image" /><p>kkg78<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kkg78 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Aug '13, 06:57</p></div></div><div id="comments-container-23981" class="comments-container"></div><div id="comment-tools-23981" class="comment-tools"></div><div class="clear"></div><div id="comment-23981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24004"></span>

<div id="answer-container-24004" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24004-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd suggest doing this with a tap, instead, rather than by exporting a global data structure.</p><blockquote><p>I would like to display the information stored in this data structure inside the Statistics-&gt;Summary dialogue window.</p></blockquote><p>I'd make all protocol-specific statistics taps rather than putting them into the summary dialog.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24004" class="comments-container"></div><div id="comment-tools-24004" class="comment-tools"></div><div class="clear"></div><div id="comment-24004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

