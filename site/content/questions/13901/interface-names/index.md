+++
type = "question"
title = "Interface names"
description = '''I am using Wireshark on both Windows XP Pro and Windows 7 Pro. In both cases I have multiple interfaces so I&#x27;ve given them friendly names like:  - Internet Switch Mirror  - LAN Switch Mirror  - LAN In the XP system, these assigned names show up in Wireshark. In the Win 7 system, the manufacturer and...'''
date = "2012-08-26T22:07:00Z"
lastmod = "2012-08-27T08:25:00Z"
weight = 13901
keywords = [ "interface", "windows", "names" ]
aliases = [ "/questions/13901" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Interface names](/questions/13901/interface-names)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13901-score" class="post-score" title="current number of votes">0</div><span id="post-13901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark on both Windows XP Pro and Windows 7 Pro. In both cases I have multiple interfaces so I've given them friendly names like: - Internet Switch Mirror - LAN Switch Mirror - LAN</p><p>In the XP system, these assigned names show up in Wireshark. In the Win 7 system, the manufacturer and model of the NIC shows up.</p><p>How can I fix the Windows 7 system NIC names in Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '12, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/fd5d1ff7667a61c33047863454522a9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fred3&#39;s gravatar image" /><p><span>fred3</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fred3 has no accepted answers">0%</span></p></div></div><div id="comments-container-13901" class="comments-container"></div><div id="comment-tools-13901" class="comment-tools"></div><div class="clear"></div><div id="comment-13901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13902"></span>

<div id="answer-container-13902" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13902-score" class="post-score" title="current number of votes">0</div><span id="post-13902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fred3 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By either:</p><ol><li>contributing code to WinPcap to modify it to use the "friendly name" in Windows (that's Microsoft's term for it) as the interface description, and get it accepted by the WinPcap people (or use it in your private version of WinPcap);</li><li>contributing code to Wireshark to fetch the "friendly name" and use it on Windows;</li><li>going to Edit -&gt; Preferences, selecting "Capture" in the dialog, clicking the "Edit" button next to "Interfaces:", and, for each interface whose name you want to change, clicking on it, editing the "Comment:" box, and, when you're done, click "OK".</li></ol><p>1) is probably technically the "best" choice, except that <em>Pcap should arguably supply</em> both* names, if available (as they are on at least some versions of Windows), but that would require a new API. It's also the choice that would take the most work and time to develop and get accepted.</p><p>2) is probably the best shorter-term workaround - if and when the new *Pcap APIs show up, Wireshark should use them if available and otherwise use the workaround.</p><p>3) is the "easiest" solution for a user - no code to write, and it works with standard Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '12, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-13902" class="comments-container"><span id="13915"></span><div id="comment-13915" class="comment"><div id="post-13915-score" class="comment-score"></div><div class="comment-text"><h1 id="does-it.-thank-you">3 does it. Thank you!</h1></div><div id="comment-13915-info" class="comment-info"><span class="comment-age">(27 Aug '12, 08:25)</span> <span class="comment-user userinfo">fred3</span></div></div></div><div id="comment-tools-13902" class="comment-tools"></div><div class="clear"></div><div id="comment-13902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

