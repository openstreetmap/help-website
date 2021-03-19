+++
type = "question"
title = "ISO 7816 Example Capture?"
description = '''I have some ISO7816 data I would like to analyze using the built-in 7816 plugin, but it doesn&#x27;t seem to recognize the data. I have this data in both raw hex dump format and captured over USB.  Does anyone have an example ISO 7816 capture or instructions on how to get my USB payload to be analyzed wi...'''
date = "2014-05-07T06:40:00Z"
lastmod = "2014-05-07T08:09:00Z"
weight = 32594
keywords = [ "iso7816", "usb" ]
aliases = [ "/questions/32594" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ISO 7816 Example Capture?](/questions/32594/iso-7816-example-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32594-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some ISO7816 data I would like to analyze using the built-in 7816 plugin, but it doesn't seem to recognize the data. I have this data in both raw hex dump format and captured over USB.</p><p>Does anyone have an example ISO 7816 capture or instructions on how to get my USB payload to be analyzed with the ISO 7816 plugin?</p></div><div id="question-tags" class="tags-container tags">iso7816 usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/bead3c1760775a7e8ae6a51d23bfe2c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testuser&#39;s gravatar image" /><p>testuser<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testuser has no accepted answers">0%</span></p></div></div><div id="comments-container-32594" class="comments-container"></div><div id="comment-tools-32594" class="comment-tools"></div><div class="clear"></div><div id="comment-32594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32603"></span>

<div id="answer-container-32603" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32603-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can find one attached to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7255">bug 7255</a>. You will probably need to change a Wireshark preference though in order for the ISO 7816 traffic to be dissected:</p><pre><code>Edit -&gt; Preferences -&gt; Protocols -&gt; USBCCID -&gt; &quot;PC -&gt; Reader Payload Type:&quot; = Generic ISO 7816 -&gt; OK</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-32603" class="comments-container"></div><div id="comment-tools-32603" class="comment-tools"></div><div class="clear"></div><div id="comment-32603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

