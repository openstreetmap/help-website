+++
type = "question"
title = "10gbe huge frames seen in captures"
description = '''I&#x27;m capturing on a linux server using tcpdump tcpdump -i eth2 -s 1600 -w file.out When reviewing the file.out in Wireshark I see many frames that are huge (larger than 9K bytes). These ethernet frames aren&#x27;t valid on the network. I&#x27;m not using jumbo frames either and they are larger than 9K. Our the...'''
date = "2012-03-01T11:09:00Z"
lastmod = "2012-03-01T11:47:00Z"
weight = 9294
keywords = [ "10gbe", "ethernet", "frame" ]
aliases = [ "/questions/9294" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [10gbe huge frames seen in captures](/questions/9294/10gbe-huge-frames-seen-in-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9294-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm capturing on a linux server using tcpdump</p><p>tcpdump -i eth2 -s 1600 -w file.out</p><p>When reviewing the file.out in Wireshark I see many frames that are huge (larger than 9K bytes). These ethernet frames aren't valid on the network. I'm not using jumbo frames either and they are larger than 9K.</p><p>Our theory is the huge ethernet frames are not "real" but are the OS transferring to the 10Gbe nic driver.<br />
</p><p>Any thoughts or experience with these ?</p><p>thanks Tim</p></div><div id="question-tags" class="tags-container tags">10gbe ethernet frame</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '12, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/9e5b2a4b1e9c59d0b4333a628c9ae10c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timc&#39;s gravatar image" /><p>timc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timc has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-9294" class="comments-container"></div><div id="comment-tools-9294" class="comment-tools"></div><div class="clear"></div><div id="comment-9294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9295"></span>

<div id="answer-container-9295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9295-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Correct: you're probably looking at <a href="http://wiki.wireshark.org/CaptureSetup/Offloading#Segmentation_Offload">Segmentation Offload</a>.</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '12, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '12, 06:58</p></div></div><div id="comments-container-9295" class="comments-container"></div><div id="comment-tools-9295" class="comment-tools"></div><div class="clear"></div><div id="comment-9295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

