+++
type = "question"
title = "USB network adaptors"
description = '''I have A usb network adaptor in a Tomtom navigation device I want to monitor from when it is plugged in, but of course if you unplug it the live capture stops and when u plug it back in data already flows before you can start capture, so need to set it up to capture as soon as it is plugged in, is t...'''
date = "2011-06-02T12:38:00Z"
lastmod = "2011-06-02T16:49:00Z"
weight = 4344
keywords = [ "usb" ]
aliases = [ "/questions/4344" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [USB network adaptors](/questions/4344/usb-network-adaptors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4344-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have A usb network adaptor in a Tomtom navigation device I want to monitor from when it is plugged in, but of course if you unplug it the live capture stops and when u plug it back in data already flows before you can start capture, so need to set it up to capture as soon as it is plugged in, is this possible ?</p></div><div id="question-tags" class="tags-container tags">usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '11, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/92dfd7012700abf4e05bb7224ffb8dea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Evan%20Berry&#39;s gravatar image" /><p>Evan Berry<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Evan Berry has no accepted answers">0%</span></p></div></div><div id="comments-container-4344" class="comments-container"></div><div id="comment-tools-4344" class="comment-tools"></div><div class="clear"></div><div id="comment-4344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4350"></span>

<div id="answer-container-4350" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4350-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are using Linux, you might be able to use <code>usbmon</code> to capture the actual USB traffic, but the results may or may not be what you want. See <a href="http://wiki.wireshark.org/CaptureSetup/USB">http://wiki.wireshark.org/CaptureSetup/USB</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4350" class="comments-container"></div><div id="comment-tools-4350" class="comment-tools"></div><div class="clear"></div><div id="comment-4350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4353"></span>

<div id="answer-container-4353" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4353-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>And if you are using Linux, you could try capturing on the "any" device, which should deliver packets from all network devices, so, if a new device is plugged in, Wireshark (or tcpdump or...) should see packets from the device as soon as it starts delivering them to the networking stack.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4353" class="comments-container"></div><div id="comment-tools-4353" class="comment-tools"></div><div class="clear"></div><div id="comment-4353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

