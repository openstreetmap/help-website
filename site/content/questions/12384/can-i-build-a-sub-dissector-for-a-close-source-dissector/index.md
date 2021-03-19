+++
type = "question"
title = "Can I build a sub-dissector for a close source dissector?"
description = '''I have a plugin for a protocol which encapsulates another protocol (i.e. ASN.1 based LTE-RRC). Unfortunately I don&#x27;t have the source code for this plugin. Do I still have the chance to develop a plugin to decode the encapsulated protocol? And I also noticed LTE-RRC is already supported by wireshark,...'''
date = "2012-07-02T22:40:00Z"
lastmod = "2012-07-04T01:17:00Z"
weight = 12384
keywords = [ "sub-dissector" ]
aliases = [ "/questions/12384" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I build a sub-dissector for a close source dissector?](/questions/12384/can-i-build-a-sub-dissector-for-a-close-source-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12384-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a plugin for a protocol which encapsulates another protocol (i.e. ASN.1 based LTE-RRC). Unfortunately I don't have the source code for this plugin. Do I still have the chance to develop a plugin to decode the encapsulated protocol? And I also noticed LTE-RRC is already supported by wireshark, how to request wireshark to decode a filed of a protocol as LTE-RRC?</p></div><div id="question-tags" class="tags-container tags">sub-dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '12, 22:40</strong></p><img src="https://secure.gravatar.com/avatar/a834854423c09d2848eda66559663c17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xu%20Yun&#39;s gravatar image" /><p>Xu Yun<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xu Yun has no accepted answers">0%</span></p></div></div><div id="comments-container-12384" class="comments-container"></div><div id="comment-tools-12384" class="comment-tools"></div><div class="clear"></div><div id="comment-12384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12432"></span>

<div id="answer-container-12432" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12432-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without having the source code of this plugin(*) it's hard to tell what hooks it provides to connect your dissector to. Maybe a symbol inspection could shed some light.</p><p>As for the LTE-RRC dissector, it register enough hooks by name, so there very well could be a applicable entrypoint for you. It's hard to tell without the details.</p><p>(*) You can always get this source code. That's because Wireshark plugins are GPL licensed, hence the distributor of the plugin <em>has</em> to provide the source code. (either with the binary, or upon request, for a reasonable fee for the medium it's delivered on).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '12, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-12432" class="comments-container"></div><div id="comment-tools-12432" class="comment-tools"></div><div class="clear"></div><div id="comment-12432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

