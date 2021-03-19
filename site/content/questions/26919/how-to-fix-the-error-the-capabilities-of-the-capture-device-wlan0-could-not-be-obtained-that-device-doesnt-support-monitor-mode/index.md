+++
type = "question"
title = "how to fix the error &quot;The capabilities of The capture device &quot;wlan0&quot; could not be obtained (That device doesn&#x27;t support monitor mode)&quot;"
description = '''how to fix the error &quot;The capabilities of The capture device &quot;wlan0&quot; could not be obtained (That device doesn&#x27;t support monitor mode). Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified. Try using airmon-ng, as suggested by CaptureSetu...'''
date = "2013-11-12T19:43:00Z"
lastmod = "2013-11-12T19:52:00Z"
weight = 26919
keywords = [ "monitor-mode" ]
aliases = [ "/questions/26919" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to fix the error "The capabilities of The capture device "wlan0" could not be obtained (That device doesn't support monitor mode)"](/questions/26919/how-to-fix-the-error-the-capabilities-of-the-capture-device-wlan0-could-not-be-obtained-that-device-doesnt-support-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26919-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to fix the error "The capabilities of The capture device "wlan0" could not be obtained (That device doesn't support monitor mode). Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified.</p><p>Try using airmon-ng, as suggested by CaptureSetup/WLAN in the Wireshark Wiki." I turned on interface wlan0 in monitoring mode, but did not help</p></div><div id="question-tags" class="tags-container tags">monitor-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '13, 19:43</strong></p><img src="https://secure.gravatar.com/avatar/348b58b10734f511c32ddaa3f6c15488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sokolov%20%20Andrey&#39;s gravatar image" /><p>Sokolov Andrey<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sokolov  Andrey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Nov '13, 19:54</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-26919" class="comments-container"></div><div id="comment-tools-26919" class="comment-tools"></div><div class="clear"></div><div id="comment-26919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26920"></span>

<div id="answer-container-26920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26920-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I turned on interface wlan0 in monitoring mode,</p></blockquote><p>Did you do so by using airmon-ng, as suggested by <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">CaptureSetup/WLAN in the Wireshark Wiki</a>? I.e., did you do</p><pre><code>airmon-ng start wlan0</code></pre><p>If you did try that, and it printed something such as</p><pre><code>Interface   Chipset      Driver

wlan0      {whatever}   {whatever} - [phy0]
            (monitor mode enabled on mon0)</code></pre><p>try capturing on <code>mon0</code>, <strong><em>NOT</em></strong> on <code>wlan0</code>, and <em>don't</em> check the monitor mode box (capturing on <code>mon0</code> will automatically be in monitor mode)..</p><p>If you didn't try that, try doing that and, if it prints something such as</p><pre><code>Interface   Chipset      Driver

wlan0      {whatever}   {whatever} - [phy0]
            (monitor mode enabled on mon0)</code></pre><p>try capturing on <code>mon0</code>, <strong><em>NOT</em></strong> on <code>wlan0</code>, and <em>don't</em> check the monitor mode box (capturing on <code>mon0</code> will automatically be in monitor mode).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '13, 19:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Nov '13, 19:53</p></div></div><div id="comments-container-26920" class="comments-container"><span id="26922"></span><div id="comment-26922" class="comment"><div id="post-26922-score" class="comment-score"></div><div class="comment-text"><p>I did choose the interface mon0 the same error</p></div><div id="comment-26922-info" class="comment-info"><span class="comment-age">(12 Nov '13, 20:01)</span> Sokolov Andrey</div></div></div><div id="comment-tools-26920" class="comment-tools"></div><div class="clear"></div><div id="comment-26920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

