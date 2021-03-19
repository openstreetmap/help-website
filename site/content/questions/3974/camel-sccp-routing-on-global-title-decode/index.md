+++
type = "question"
title = "camel sccp routing on global title decode"
description = '''I am trying to decode SCTP frames that contain CAPv2 (Camel) operations however decoding stops at SCCP level. SCCP addresses contain:  - Address Indicator H&#x27;0989  - Route on GT  - GT indicator: Translation Type only  - SSN not present  - Point Code present  - Point Code  - Global Title  - Translatio...'''
date = "2011-05-06T00:58:00Z"
lastmod = "2011-05-06T06:32:00Z"
weight = 3974
keywords = [ "routing", "ssn", "sccp", "capv2", "camel" ]
aliases = [ "/questions/3974" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [camel sccp routing on global title decode](/questions/3974/camel-sccp-routing-on-global-title-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3974-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decode SCTP frames that contain CAPv2 (Camel) operations however decoding stops at SCCP level. SCCP addresses contain: - Address Indicator H'0989 - Route on GT - GT indicator: Translation Type only - SSN not present - Point Code present - Point Code - Global Title - Translation Type - Address information (digits)</p><p>The Addresses on SCCP do not contain SSN, instead routing is performed solely on global title containing Translation Type and Address Information. Is there a setting I can use to decode these messages on TCAP level including the Camel decoding?</p></div><div id="question-tags" class="tags-container tags">routing ssn sccp capv2 camel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '11, 00:58</strong></p><img src="https://secure.gravatar.com/avatar/2cfad863a818dca1bae4aaea4b18a43e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acve&#39;s gravatar image" /><p>acve<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acve has no accepted answers">0%</span></p></div></div><div id="comments-container-3974" class="comments-container"></div><div id="comment-tools-3974" class="comment-tools"></div><div class="clear"></div><div id="comment-3974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3977"></span>

<div id="answer-container-3977" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3977-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In current trunk (and 1.5.1) the SCCP dissector has a preference for a "default payload" (it was added by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3301">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3301</a> ). You'd need to set that to "tcap" to decode messages with no SSN in it as TCAP.</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '11, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '12, 07:03</p></div></div><div id="comments-container-3977" class="comments-container"><span id="4014"></span><div id="comment-4014" class="comment"><div id="post-4014-score" class="comment-score"></div><div class="comment-text"><p>Great, this worked for me. Thanks for the help</p></div><div id="comment-4014-info" class="comment-info"><span class="comment-age">(09 May '11, 04:22)</span> acve</div></div></div><div id="comment-tools-3977" class="comment-tools"></div><div class="clear"></div><div id="comment-3977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

