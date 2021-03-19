+++
type = "question"
title = "analyze sap gui with wireshark"
description = '''In the low part of Wireshark I see : SNCFRA ME , please advise ? is it relate to the fact that I am using sap snc (secure network connection)? '''
date = "2017-02-22T00:16:00Z"
lastmod = "2017-02-23T12:17:00Z"
weight = 59596
keywords = [ "snc1" ]
aliases = [ "/questions/59596" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [analyze sap gui with wireshark](/questions/59596/analyze-sap-gui-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59596-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the low part of Wireshark I see : SNCFRA ME , please advise ? is it relate to the fact that I am using sap snc (secure network connection)?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/SNC_WS_Capture.PNG" width="640" /></p></div><div id="question-tags" class="tags-container tags">snc1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '17, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/8666288fd5ee73bb82b5f0dae4e9d310?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hadarba63&#39;s gravatar image" /><p>hadarba63<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hadarba63 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Feb '17, 04:38</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-59596" class="comments-container"></div><div id="comment-tools-59596" class="comment-tools"></div><div class="clear"></div><div id="comment-59596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59603"></span>

<div id="answer-container-59603" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59603-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes.......</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '17, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59603" class="comments-container"></div><div id="comment-tools-59603" class="comment-tools"></div><div class="clear"></div><div id="comment-59603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59640"></span>

<div id="answer-container-59640" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59640-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello! Yes, that is the "eyecatcher" for the use of SNC. You can use the following plugin to see some SAPGUI/Diag protocol data (e.g. field "sapdiag.header.compress" for if the Diag packet is only compressed or SNC is enabled) along with the SNC Frame container:</p><p><a href="https://github.com/CoreSecurity/SAP-Dissection-plug-in-for-Wireshark">https://github.com/CoreSecurity/SAP-Dissection-plug-in-for-Wireshark</a></p><p>I'm planning to add support for more detailed dissection of SNC packets around late March (after publishing <a href="https://www.troopers.de/events/troopers17/763_intercepting_sap_snc-protected_traffic/).">https://www.troopers.de/events/troopers17/763_intercepting_sap_snc-protected_traffic/).</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '17, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/3db2b8a556c32a6fbc6e288df6d21815?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mgallo&#39;s gravatar image" /><p>mgallo<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mgallo has no accepted answers">0%</span></p></div></div><div id="comments-container-59640" class="comments-container"></div><div id="comment-tools-59640" class="comment-tools"></div><div class="clear"></div><div id="comment-59640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

