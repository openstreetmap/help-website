+++
type = "question"
title = "how do I capture on a Wi-Fi network on Windows?"
description = '''Hi guys, I&#x27;m in my home and I want to monitor all wi-fi devices but I only see my computer called &quot;Ethernet&quot; in the main page of wireshark, I already run it as administrator etc but can&#x27;t see new interfaces please help me.'''
date = "2017-06-15T11:19:00Z"
lastmod = "2017-06-16T12:36:00Z"
weight = 62048
keywords = [ "windows", "wi-fi" ]
aliases = [ "/questions/62048" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how do I capture on a Wi-Fi network on Windows?](/questions/62048/how-do-i-capture-on-a-wi-fi-network-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62048-score" class="post-score" title="current number of votes">0</div><span id="post-62048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I'm in my home and I want to monitor all wi-fi devices but I only see my computer called "Ethernet" in the main page of wireshark, I already run it as administrator etc but can't see new interfaces please help me.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-wi-fi" rel="tag" title="see questions tagged &#39;wi-fi&#39;">wi-fi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '17, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/554fb6c86c55bd20dd50ad5519cfe336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Artor1as&#39;s gravatar image" /><p><span>Artor1as</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Artor1as has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jun '17, 12:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-62048" class="comments-container"></div><div id="comment-tools-62048" class="comment-tools"></div><div class="clear"></div><div id="comment-62048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62060"></span>

<div id="answer-container-62060" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62060-score" class="post-score" title="current number of votes">0</div><span id="post-62060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Artor1as has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your smartphone isn't a network interface, it's a network host.</p><p>Your computer isn't called "Ethernet", your computer's Ethernet interface is called "Ethernet".</p><p>Network hosts and network interfaces are different. A given network interface may be on a network with <em>more than one</em> other host on it.</p><p>If you want to capture on Wi-Fi, you need to capture on a Wi-Fi interface.</p><p>I infer from "as administrator" that this is Windows. Capturing on a Wi-Fi interface on Windows is a bit difficult; you will probably either need to have Npcap, rather than WinPcap, or buy an AirPcap device. See <a href="https://wiki.wireshark.org/CaptureSetup/WLAN#Windows">the "Windows" section of the Wireshark Wiki page on Wi-Fi capturing</a> for more details.</p><p>Note also that IEEE 802.11 was <em>deliberately designed</em> to make it hard to sniff; most Wi-Fi networks encrypt the packets, and most current Wi-Fi networks encrypt it in a fashion that requires some special effort when capturing. See <a href="https://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki page on Wi-Fi decrypting</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '17, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62060" class="comments-container"></div><div id="comment-tools-62060" class="comment-tools"></div><div class="clear"></div><div id="comment-62060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

