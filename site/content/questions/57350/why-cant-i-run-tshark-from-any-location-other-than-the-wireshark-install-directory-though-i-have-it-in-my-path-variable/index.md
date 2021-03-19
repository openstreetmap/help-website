+++
type = "question"
title = "Why can&#x27;t I run tshark from any location other than the Wireshark install directory, though I have it in my PATH variable."
description = '''I am running Windows 7 64-bit. I have installed Version 2.2.1 of Wireshark. This is how my PATH system-environment variable starts: C:&#92;Program Files&#92;Wireshark&#92;tshark.exe;....other paths  But when I try to run tshark -help from anywhere other than the Wireshark install directory (which contains tshar...'''
date = "2016-11-12T21:51:00Z"
lastmod = "2016-11-12T21:55:00Z"
weight = 57350
keywords = [ "windows7", "tshark" ]
aliases = [ "/questions/57350" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I run tshark from any location other than the Wireshark install directory, though I have it in my PATH variable.](/questions/57350/why-cant-i-run-tshark-from-any-location-other-than-the-wireshark-install-directory-though-i-have-it-in-my-path-variable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57350-score" class="post-score" title="current number of votes">0</div><span id="post-57350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Windows 7 64-bit. I have installed Version 2.2.1 of Wireshark. This is how my PATH system-environment variable starts:</p><pre><code>C:\Program Files\Wireshark\tshark.exe;....other paths</code></pre><p>But when I try to run <code>tshark -help</code> from anywhere other than the Wireshark install directory (which contains <code>tshark.exe</code>), I get</p><pre><code>C:\Windows\System32&gt;tshark.exe
&#39;tshark.exe&#39; is not recognized as an internal or external command,
operable program or batch file.</code></pre><p>All other programs are running fine in my Windows.</p><p><strong>The question is WHY, and how do I resolve this issue?</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '16, 21:51</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p><span>Jesss</span><br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '16, 01:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-57350" class="comments-container"></div><div id="comment-tools-57350" class="comment-tools"></div><div class="clear"></div><div id="comment-57350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57351"></span>

<div id="answer-container-57351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57351-score" class="post-score" title="current number of votes">2</div><span id="post-57351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You don't put executable files on the path; you put the directories where the executable files are located on the path.</p><p>Instead of C:\Program Files\Wireshark\tshark.exe it should be C:\Program Files\Wireshark</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '16, 21:55</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-57351" class="comments-container"></div><div id="comment-tools-57351" class="comment-tools"></div><div class="clear"></div><div id="comment-57351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

