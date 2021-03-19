+++
type = "question"
title = "Bluetooth - How to capture network performances statistic (such as signal strength) using Wireshark"
description = '''Hi, I need to capture wireless network performances statistic of Bluetooth(such as signal strength, throughput, etc) using Wireshark and Windows 7x64. May i know how to setup Wireshark to do this? Please help.'''
date = "2014-06-17T12:43:00Z"
lastmod = "2014-06-17T12:56:00Z"
weight = 33906
keywords = [ "wireless", "signal", "strength", "setup", "bluetooth" ]
aliases = [ "/questions/33906" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bluetooth - How to capture network performances statistic (such as signal strength) using Wireshark](/questions/33906/bluetooth-how-to-capture-network-performances-statistic-such-as-signal-strength-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33906-score" class="post-score" title="current number of votes">0</div><span id="post-33906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I need to capture wireless network performances statistic of Bluetooth(such as signal strength, throughput, etc) using Wireshark and Windows 7x64. May i know how to setup Wireshark to do this? Please help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-signal" rel="tag" title="see questions tagged &#39;signal&#39;">signal</span> <span class="post-tag tag-link-strength" rel="tag" title="see questions tagged &#39;strength&#39;">strength</span> <span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-bluetooth" rel="tag" title="see questions tagged &#39;bluetooth&#39;">bluetooth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '14, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/287024c5a663404a19410f0e8a7df8e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kohck&#39;s gravatar image" /><p><span>kohck</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kohck has no accepted answers">0%</span></p></div></div><div id="comments-container-33906" class="comments-container"></div><div id="comment-tools-33906" class="comment-tools"></div><div class="clear"></div><div id="comment-33906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33908"></span>

<div id="answer-container-33908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33908-score" class="post-score" title="current number of votes">0</div><span id="post-33908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do that with Wireshark on Windows directly, as WinPcap does not offer Bluetooth support!</p><p>You can capture bluetooth traffic on Linux.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Bluetooth">http://wiki.wireshark.org/CaptureSetup/Bluetooth</a><br />
</p></blockquote><p>See also my answer to a similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/22715/capturing-bluetooth-on-windows-7">http://ask.wireshark.org/questions/22715/capturing-bluetooth-on-windows-7</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '14, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-33908" class="comments-container"></div><div id="comment-tools-33908" class="comment-tools"></div><div class="clear"></div><div id="comment-33908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

