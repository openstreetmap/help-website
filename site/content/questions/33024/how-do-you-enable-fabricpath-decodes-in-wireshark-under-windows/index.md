+++
type = "question"
title = "How do you enable fabricpath decodes in wireshark under windows?"
description = '''Running Wireshark 1.7.10 on Windows 7 and I the Help files list support for Cisco FabricPath Protocol, But when I run a packet capture from a fabricpath switch, I can See the ethertype II FRame and everything below that is just Data, No IP addresses etc because there is a fabric path header that wir...'''
date = "2014-05-23T13:04:00Z"
lastmod = "2014-05-24T02:32:00Z"
weight = 33024
keywords = [ "fabricpath" ]
aliases = [ "/questions/33024" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do you enable fabricpath decodes in wireshark under windows?](/questions/33024/how-do-you-enable-fabricpath-decodes-in-wireshark-under-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33024-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running Wireshark 1.7.10 on Windows 7 and I the Help files list support for Cisco FabricPath Protocol, But when I run a packet capture from a fabricpath switch, I can See the ethertype II FRame and everything below that is just Data, No IP addresses etc because there is a fabric path header that wireshark does not seem to understand.. How Can I enable this decode/dissector under this version of wireshark on windows</p></div><div id="question-tags" class="tags-container tags">fabricpath</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '14, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/e1dc56a93f650b5db1bfb6a38f692bd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="canetto&#39;s gravatar image" /><p>canetto<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="canetto has no accepted answers">0%</span></p></div></div><div id="comments-container-33024" class="comments-container"></div><div id="comment-tools-33024" class="comment-tools"></div><div class="clear"></div><div id="comment-33024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33029"></span>

<div id="answer-container-33029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33029-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you made a typo and you are using 1.10.7 have you enabled the dissector?</p><p><code>Edit - Preferences - Protocols - CFP - Enable dissector</code></p><p>CFP was introduced in version 1.8.0 so if you are using 1.7.1 please upgrade to the latest version.</p><p><a href="https://www.wireshark.org/docs///dfref/c/cfp.html">https://www.wireshark.org/docs///dfref/c/cfp.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '14, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-33029" class="comments-container"></div><div id="comment-tools-33029" class="comment-tools"></div><div class="clear"></div><div id="comment-33029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

