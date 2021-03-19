+++
type = "question"
title = "Howto setup the UDT Dissector &amp; &quot;Follow&quot; UDT stream"
description = '''Hi,  I&#x27;m using windows-hosted Version 1.10.8 (v1.10.8-2-g52a5244 from master-1.10) and I expected to see support for the UDT protocol under the &quot;Dissector tables&quot; or &quot;Supported Protocols&quot; under internals.  As such, a need a HOWTO for enabling the UDT disscetor and &quot;following&quot; the capture. Can I plea...'''
date = "2014-07-02T15:13:00Z"
lastmod = "2014-07-02T16:08:00Z"
weight = 34364
keywords = [ "follow", "dissector", "udt" ]
aliases = [ "/questions/34364" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Howto setup the UDT Dissector & "Follow" UDT stream](/questions/34364/howto-setup-the-udt-dissector-follow-udt-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34364-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm using windows-hosted Version 1.10.8 (v1.10.8-2-g52a5244 from master-1.10) and I expected to see support for the UDT protocol under the "Dissector tables" or "Supported Protocols" under internals.</p><p>As such, a need a HOWTO for enabling the UDT disscetor and "following" the capture.</p><p>Can I please get a pointer on how to do this?</p><p>I see that the UDT dissector code is available and may have been submitted into the release process.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">follow dissector udt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '14, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/fbdf37ccc1f323b8ee9f75fc75934358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IP%20Services&#39;s gravatar image" /><p>IP Services<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IP Services has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '14, 15:14</p></div></div><div id="comments-container-34364" class="comments-container"></div><div id="comment-tools-34364" class="comment-tools"></div><div class="clear"></div><div id="comment-34364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34369"></span>

<div id="answer-container-34369" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34369-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the UDT protocol you're referring to is the one whose dissector was submitted in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8741">bug 8741</a>, then the HOWTO is a simple one-step process:</p><ul><li>use Wireshark 1.12.0rc2 or later.</li></ul><p>It was submitted to the release process, but was not added to 1.10.x, so you shouldn't expect to see support for it in 1.10.8.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '14, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34369" class="comments-container"><span id="36863"></span><div id="comment-36863" class="comment"><div id="post-36863-score" class="comment-score"></div><div class="comment-text"><p>Did the trick, thank you.</p></div><div id="comment-36863-info" class="comment-info"><span class="comment-age">(05 Oct '14, 17:05)</span> IP Services</div></div></div><div id="comment-tools-34369" class="comment-tools"></div><div class="clear"></div><div id="comment-34369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

