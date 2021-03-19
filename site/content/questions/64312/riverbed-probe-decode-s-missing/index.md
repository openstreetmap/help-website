+++
type = "question"
title = "Riverbed  Probe Decode - S+* Missing"
description = '''It appears that Wireshark 2.4.2 is now displaying &quot;S+&quot; in the Info field instead of &quot;S+*&quot; on Syn packets leaving the server side Steelhead towards the server. I believe older versions of Wireshark used &quot;S+&quot; for Syn packets from the client side Steelhead, while using &quot;S+*&quot; for Syn packets forwarded f...'''
date = "2017-10-27T17:09:00Z"
lastmod = "2017-10-29T04:01:00Z"
weight = 64312
keywords = [ "decode", "steelhead" ]
aliases = [ "/questions/64312" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Riverbed Probe Decode - S+\* Missing](/questions/64312/riverbed-probe-decode-s-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64312-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It appears that Wireshark 2.4.2 is now displaying "S+" in the Info field instead of "S+*" on Syn packets leaving the server side Steelhead towards the server. I believe older versions of Wireshark used "S+" for Syn packets from the client side Steelhead, while using "S+*" for Syn packets forwarded from other Steelheads (e.g. the server side Steelhead or other mid-stream Steelheads.</p><p>Is that intentional or an oversight?</p></div><div id="question-tags" class="tags-container tags">decode steelhead</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '17, 17:09</strong></p><img src="https://secure.gravatar.com/avatar/8f57622799be875b9759d0b39cd7829e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rick16&#39;s gravatar image" /><p>Rick16<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rick16 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Oct '17, 00:44</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-64312" class="comments-container"></div><div id="comment-tools-64312" class="comment-tools"></div><div class="clear"></div><div id="comment-64312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64326"></span>

<div id="answer-container-64326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64326-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you're right. Up to version 2.2.X these packets where flagged with S+*. With the latest stable version and developer master this is missing. Furthermore my tests captures are interpreted as malformed after the "Riverbed Probe Option" with 2.4.X</p><p>So this is a bug.</p><p>I will open a bug and check if I can fix it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '17, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-64326" class="comments-container"><span id="64327"></span><div id="comment-64327" class="comment"><div id="post-64327-score" class="comment-score"></div><div class="comment-text"><p>Reported with <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=14150">bug 14150</a></p></div><div id="comment-64327-info" class="comment-info"><span class="comment-age">(29 Oct '17, 04:14)</span> Uli</div></div></div><div id="comment-tools-64326" class="comment-tools"></div><div class="clear"></div><div id="comment-64326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

