+++
type = "question"
title = "Coloring Rules &quot;OK&quot; Button Grayed Out After Update to Wireshark 2.2.0"
description = '''Dear Wireshark, After upgrading to Wireshark 2.2.0 from 2.0.6, I do not seem to be able to modify my Coloring Rules. Specifically, the Coloring Rules &quot;OK&quot; button appears to remain grayed out no matter what I do. I completely uninstalled Wireshark, manually downloaded 2.2.0, and re-installed Wireshar...'''
date = "2016-09-26T06:36:00Z"
lastmod = "2016-09-26T12:04:00Z"
weight = 55840
keywords = [ "color-rules", "wireshark-2.2.0", "coloring", "update" ]
aliases = [ "/questions/55840" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Coloring Rules "OK" Button Grayed Out After Update to Wireshark 2.2.0](/questions/55840/coloring-rules-ok-button-grayed-out-after-update-to-wireshark-220)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55840-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Wireshark,</p><p>After upgrading to Wireshark 2.2.0 from 2.0.6, I do not seem to be able to modify my Coloring Rules. Specifically, the Coloring Rules "OK" button appears to remain grayed out no matter what I do.</p><p>I completely uninstalled Wireshark, manually downloaded 2.2.0, and re-installed Wireshark 2.2.0. Nonetheless, this issue remained.</p><p>I uninstalled Wireshark 2.2.0 and re-installed Wireshark 2.0.4. In Wireshark 2.0.4 I can modify my Coloring Rules and the "OK" button works as expected. Re-installed Wireshark 2.2.0 once again, but Coloring Rules "OK" button remains grayed out.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">color-rules wireshark-2.2.0 coloring update</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '16, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/b1275762c4b34496165a83319ed829bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsizemore&#39;s gravatar image" /><p>jsizemore<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsizemore has no accepted answers">0%</span></p></div></div><div id="comments-container-55840" class="comments-container"></div><div id="comment-tools-55840" class="comment-tools"></div><div class="clear"></div><div id="comment-55840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55871"></span>

<div id="answer-container-55871" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55871-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There was a change in v2.2 with regards to the syntax of the display filters for bad checksums. This change makes the old default "Checksum Errors" coloring rule invalid which is why it shows up as not enabled in v2.2.</p><p>But it seems that it also prevents you from clicking Ok.</p><p>To work around the problem you can delete (or correct the syntax of) the "Checksum Errors" coloring rule. The new rule should be:</p><pre><code>eth.fcs.status==&quot;Bad&quot; || ip.checksum.status==&quot;Bad&quot; || tcp.checksum.status==&quot;Bad&quot; || udp.checksum.status==&quot;Bad&quot; || sctp.checksum.status==&quot;Bad&quot; || mstp.checksum.status==&quot;Bad&quot; || cdp.checksum.status==&quot;Bad&quot; || edp.checksum.status==&quot;Bad&quot; || wlan.fcs.status==&quot;Bad&quot; || stt.checksum.status==&quot;Bad&quot;</code></pre><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12814">Bug 12814</a> was recently opened to fix this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '16, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-55871" class="comments-container"><span id="57536"></span><div id="comment-57536" class="comment"><div id="post-57536-score" class="comment-score"></div><div class="comment-text"><p>I ran into the same problem, After upgrading to Wireshark 2.2.0 from 2.0.6, I do not seem to be able to modify my Coloring Rules. Specifically, the Coloring Rules "OK" button appears to remain grayed out no matter what I do.</p><p>Maybe the colorfilters file is read only? If this could be the case, what is the location of that file on Linux Debian?</p><p>Thanks you</p></div><div id="comment-57536-info" class="comment-info"><span class="comment-age">(21 Nov '16, 12:19)</span> toloop</div></div><span id="57538"></span><div id="comment-57538" class="comment"><div id="post-57538-score" class="comment-score"></div><div class="comment-text"><p>(I converted your Answer to a Question--this is a Q&amp;A site, not a forum, see the FAQ.)</p><p>Did you fix the syntax of the "Checksum Errors" coloring rule as described in the answer?</p><p>I don't think that the permissions on the colorfilters file will have an effect. That file, should you want to check on it, should be in <code>~/.wireshark/</code></p></div><div id="comment-57538-info" class="comment-info"><span class="comment-age">(21 Nov '16, 12:47)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-55871" class="comment-tools"></div><div class="clear"></div><div id="comment-55871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

