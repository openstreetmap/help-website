+++
type = "question"
title = "When will Wireshark support remote packet capture in Macbook?"
description = '''Guys, As of my knowledge (I have a Macbook Pro) Wireshark does not support remote packet capture in MacOS. Is there any workaround or a plan to include this feature in newer versions? Thanksl'''
date = "2016-09-06T13:54:00Z"
lastmod = "2016-09-07T06:23:00Z"
weight = 55358
keywords = [ "remote-capture", "macosx" ]
aliases = [ "/questions/55358" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [When will Wireshark support remote packet capture in Macbook?](/questions/55358/when-will-wireshark-support-remote-packet-capture-in-macbook)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55358-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Guys,</p><p>As of my knowledge (I have a Macbook Pro) Wireshark does not support remote packet capture in MacOS. Is there any workaround or a plan to include this feature in newer versions?</p><p>Thanksl</p></div><div id="question-tags" class="tags-container tags">remote-capture macosx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '16, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/ddacc770b7955273148a9a77eb71c762?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Victor%20Tort&#39;s gravatar image" /><p>Victor Tort<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Victor Tort has no accepted answers">0%</span></p></div></div><div id="comments-container-55358" class="comments-container"></div><div id="comment-tools-55358" class="comment-tools"></div><div class="clear"></div><div id="comment-55358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55371"></span>

<div id="answer-container-55371" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55371-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The upcoming Wireshark 2.2 release will support that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '16, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55371" class="comments-container"><span id="55386"></span><div id="comment-55386" class="comment"><div id="post-55386-score" class="comment-score"></div><div class="comment-text"><p>I just downloaded version 2.2 and it is still not supported.</p></div><div id="comment-55386-info" class="comment-info"><span class="comment-age">(07 Sep '16, 17:18)</span> Victor Tort</div></div><span id="55390"></span><div id="comment-55390" class="comment"><div id="post-55390-score" class="comment-score"></div><div class="comment-text"><p>It does, via SSH remote capture, an extcap feature. It's at the bottom of your capture interfaces list.</p></div><div id="comment-55390-info" class="comment-info"><span class="comment-age">(08 Sep '16, 05:08)</span> Jaap ♦</div></div><span id="55398"></span><div id="comment-55398" class="comment"><div id="post-55398-score" class="comment-score"></div><div class="comment-text"><p>If by "remote packet capture" you mean "the remote packet capture mechanism available on Windows", rather than "the ability to capture remotely by some mechanism, not necessarily the one available on Windows", then to support it in Wireshark, either 1) Wireshark needs to be built with a version of libpcap that supports it (the version in OS X doesn't currently support it) or 2) there needs to be an extcap module to support it (there is currently no such module).</p><p>At some point in the future the standard libpcap release should support it; hopefully, Apple will pick up that version once it's released.</p></div><div id="comment-55398-info" class="comment-info"><span class="comment-age">(08 Sep '16, 10:22)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-55371" class="comment-tools"></div><div class="clear"></div><div id="comment-55371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

