+++
type = "question"
title = "CFM decoder"
description = '''Is cfm packet decoder supported in Wireshark 1.6.1.If affirmative, could you please provide steps on how to activate it? Thanks very kindly'''
date = "2011-08-10T08:18:00Z"
lastmod = "2011-08-10T08:36:00Z"
weight = 5622
keywords = [ "cfm", "802.1x" ]
aliases = [ "/questions/5622" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [CFM decoder](/questions/5622/cfm-decoder)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5622-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is cfm packet decoder supported in Wireshark 1.6.1.If affirmative, could you please provide steps on how to activate it?</p><p>Thanks very kindly</p></div><div id="question-tags" class="tags-container tags">cfm 802.1x</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '11, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/654622511d57161bf7c43604d0430d13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jg2&#39;s gravatar image" /><p>jg2<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jg2 has no accepted answers">0%</span></p></div></div><div id="comments-container-5622" class="comments-container"></div><div id="comment-tools-5622" class="comment-tools"></div><div class="clear"></div><div id="comment-5622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5623"></span>

<div id="answer-container-5623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5623-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has a dissector for CFM;</p><p>From the source code:</p><pre><code>/* This code is based on the IEEE P802.1ag/D8.1 document, and on the ITU-T Y.1731
 * recommendation (05/2006,) which is not formally released at the time of this
 * dissector development.  Any updates to these documents may require additional
 * modifications to this code.
 */</code></pre><p>No special action is required to activate the dissector.</p><p>I note that support for the following was added quite recently (and thus probably is not in Wireshark 1.6.1):</p><pre><code>This patch adds support for the two-way Sythetic Loss Measurement
opcodes (SLM &amp; SLR) defined in the latest ITU-T Y.1731.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '11, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Aug '11, 08:41</p></div></div><div id="comments-container-5623" class="comments-container"></div><div id="comment-tools-5623" class="comment-tools"></div><div class="clear"></div><div id="comment-5623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

