+++
type = "question"
title = "Determine Speed of Remote Device (10 or 100 BASE-T?)"
description = '''I have a CAT5 cable that is connected between a laptop and an embedded device. I need to know if the embedded device is using 10Base-T or 100Base-T. Is the Base-T info from each device (the laptop and embedded device) passed in the ethernet packets? i.e. Can I use Wireshark to gather the Base-T info...'''
date = "2015-07-09T10:22:00Z"
lastmod = "2015-07-09T15:30:00Z"
weight = 44018
keywords = [ "capture", "speed", "10base-t" ]
aliases = [ "/questions/44018" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Determine Speed of Remote Device (10 or 100 BASE-T?)](/questions/44018/determine-speed-of-remote-device-10-or-100-base-t)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44018-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a CAT5 cable that is connected between a laptop and an embedded device. I need to know if the embedded device is using 10Base-T or 100Base-T.</p><p>Is the Base-T info from each device (the laptop and embedded device) passed in the ethernet packets? i.e. Can I use Wireshark to gather the Base-T information? If so, how?</p></div><div id="question-tags" class="tags-container tags">capture speed 10base-t</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '15, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p>KTM<br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '15, 10:46</p></div></div><div id="comments-container-44018" class="comments-container"></div><div id="comment-tools-44018" class="comment-tools"></div><div class="clear"></div><div id="comment-44018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44023"></span>

<div id="answer-container-44023" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44023-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is the Base-T info from each device (the laptop and embedded device) passed in the ethernet packets?</p></blockquote><p>Not at the level at which packet capture mechanisms supply the packets - i.e., it's not a field in an Ethernet packet - so...</p><blockquote><p>Can I use Wireshark to gather the Base-T information?</p></blockquote><p>...no.</p><p>However, if this is a point-to-point Ethernet - i.e., you just have a single Ethernet cable between the two machines, with no hub or switch in between them - you might be able to find out from the operating system on the laptop what speed it's using, which would be the same speed as the speed of the device to which it's talking. What operating system is the laptop running?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '15, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '15, 15:46</p></div></div><div id="comments-container-44023" class="comments-container"><span id="44024"></span><div id="comment-44024" class="comment"><div id="post-44024-score" class="comment-score"></div><div class="comment-text"><p>The laptop is running OS X. And, yes, I have a point-to-point connection with no hubs/switches in between the two devices.</p></div><div id="comment-44024-info" class="comment-info"><span class="comment-age">(09 Jul '15, 15:50)</span> KTM</div></div><span id="44025"></span><div id="comment-44025" class="comment"><div id="post-44025-score" class="comment-score"></div><div class="comment-text"><p>Try opening a Terminal window and doing <code>ifconfig -a</code> and see what it reports for your Ethernet interface. If it's a laptop with a built-in Ethernet, your Ethernet interface will probably be <code>en0</code>, otherwise <code>en0</code> will probably be a Wi-Fi interface and your Ethernet will be some other <code>en</code> interface.</p></div><div id="comment-44025-info" class="comment-info"><span class="comment-age">(09 Jul '15, 19:43)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-44023" class="comment-tools"></div><div class="clear"></div><div id="comment-44023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

