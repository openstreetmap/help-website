+++
type = "question"
title = "Enable bluetooth interface in wireshark"
description = '''I am trying to capture bluetooth packets using wireshark , I connected my bluetooth dongle to ubuntu PC and started wireshark but i am able to see ethernet and wireless interface but not able to see bluetooth interface like bluetooth0 or bluetooth1.  Can anyone help me how to enable bluetooth interf...'''
date = "2014-03-17T06:49:00Z"
lastmod = "2014-03-19T00:16:00Z"
weight = 30884
keywords = [ "wireshark" ]
aliases = [ "/questions/30884" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Enable bluetooth interface in wireshark](/questions/30884/enable-bluetooth-interface-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30884-score" class="post-score" title="current number of votes">0</div><span id="post-30884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture bluetooth packets using wireshark , I connected my bluetooth dongle to ubuntu PC and started wireshark but i am able to see ethernet and wireless interface but not able to see bluetooth interface like bluetooth0 or bluetooth1.</p><p>Can anyone help me how to enable bluetooth interface in wireshark??????</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '14, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/a68b056ce997d8a9dc1e16f765cf1619?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sreeram1443&#39;s gravatar image" /><p><span>sreeram1443</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sreeram1443 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Mar '14, 23:18</strong> </span></p></div></div><div id="comments-container-30884" class="comments-container"><span id="30912"></span><div id="comment-30912" class="comment"><div id="post-30912-score" class="comment-score"></div><div class="comment-text"><p>Anyone anyhelp ??</p></div><div id="comment-30912-info" class="comment-info"><span class="comment-age">(17 Mar '14, 22:01)</span> <span class="comment-user userinfo">sreeram1443</span></div></div><span id="30916"></span><div id="comment-30916" class="comment"><div id="post-30916-score" class="comment-score"></div><div class="comment-text"><p>If you select the "About Wireshark" menu item under "Help", what does Wireshark display - in particular, what does it show for "with libpcap" in the "Running on" section?</p></div><div id="comment-30916-info" class="comment-info"><span class="comment-age">(18 Mar '14, 01:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="30925"></span><div id="comment-30925" class="comment"><div id="post-30925-score" class="comment-score"></div><div class="comment-text"><p>0</p><p>It contains following information.....</p><p>Running on Linux 3.5.0-46-generic, with locale en_IN, with libpcap version 1.3.0, with libz 1.2.7, GnuTLS 2.12.14, Gcrypt 1.5.0, without AirPcap.</p></div><div id="comment-30925-info" class="comment-info"><span class="comment-age">(18 Mar '14, 04:00)</span> <span class="comment-user userinfo">sreeram1443</span></div></div><span id="30934"></span><div id="comment-30934" class="comment"><div id="post-30934-score" class="comment-score"></div><div class="comment-text"><p>What's printed if you run the command <code>sudo tcpdump -D</code>?</p></div><div id="comment-30934-info" class="comment-info"><span class="comment-age">(18 Mar '14, 11:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="30940"></span><div id="comment-30940" class="comment"><div id="post-30940-score" class="comment-score"></div><div class="comment-text"><p>Here:</p><pre><code>[email protected]:/home/igx# tcpdump -D
1.eth0
2.wlan0
3.pan1
4.any (Pseudo-device that captures on all interfaces)
5.lo</code></pre><p>In this pan1 is printing while runnig bluetooth-manager other wise pan1 is not printing.This pan1 is not showing bluetooth packets.</p></div><div id="comment-30940-info" class="comment-info"><span class="comment-age">(18 Mar '14, 21:45)</span> <span class="comment-user userinfo">sreeram1443</span></div></div><span id="30941"></span><div id="comment-30941" class="comment not_top_scorer"><div id="post-30941-score" class="comment-score"></div><div class="comment-text"><p>Do you want to capture Bluetooth frames or IP frames transmitted over your Bluetooth interface?</p></div><div id="comment-30941-info" class="comment-info"><span class="comment-age">(18 Mar '14, 23:02)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-30884" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-30884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30942"></span>

<div id="answer-container-30942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30942-score" class="post-score" title="current number of votes">0</div><span id="post-30942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That appears to be a libpcap problem, not a Wireshark problem (Wireshark uses libpcap for capturing); the libpcap you're using was not built with Bluetooth support.</p><p>You will have to ask Canonical about this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '14, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-30942" class="comments-container"></div><div id="comment-tools-30942" class="comment-tools"></div><div class="clear"></div><div id="comment-30942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

