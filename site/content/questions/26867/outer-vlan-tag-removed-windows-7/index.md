+++
type = "question"
title = "Outer vlan tag removed (Windows 7)"
description = '''Hello, When I capture VLAN-tagged packets with wireshark, I don&#x27;t see VLAN tags. My OS is Windows 7 and my ethernet card is TP-LINK TG-3468 (I installed the last driver and I disabled &quot;VLAN &amp;amp; priority function&quot; in the properies in the Ethernet card driver). With Unbuntu, I can see VLAN tags with...'''
date = "2013-11-12T00:28:00Z"
lastmod = "2013-11-14T05:47:00Z"
weight = 26867
keywords = [ "removed", "vlan", "tag", "windows7" ]
aliases = [ "/questions/26867" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Outer vlan tag removed (Windows 7)](/questions/26867/outer-vlan-tag-removed-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26867-score" class="post-score" title="current number of votes">0</div><span id="post-26867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, When I capture VLAN-tagged packets with wireshark, I don't see VLAN tags. My OS is Windows 7 and my ethernet card is TP-LINK TG-3468 (I installed the last driver and I disabled "VLAN &amp; priority function" in the properies in the Ethernet card driver). With Unbuntu, I can see VLAN tags with wireshark. How can I do to capture VLAN tags ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-removed" rel="tag" title="see questions tagged &#39;removed&#39;">removed</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '13, 00:28</strong></p><img src="https://secure.gravatar.com/avatar/91493dfcf80c3f657ce0017a8b948206?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark_user&#39;s gravatar image" /><p><span>wireshark_user</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark_user has no accepted answers">0%</span></p></div></div><div id="comments-container-26867" class="comments-container"></div><div id="comment-tools-26867" class="comment-tools"></div><div class="clear"></div><div id="comment-26867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26994"></span>

<div id="answer-container-26994" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26994-score" class="post-score" title="current number of votes">0</div><span id="post-26994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I do to capture VLAN tags ?</p></blockquote><p><strong>HINT</strong>: Are you sure the VLAN tagged frames are really sent to your system? Your switch might strip them due to its own configuration.</p><p>If you are sure about the switch: I suggest to boot the system with a Linux distribution (Ubuntu, Kali Linux) from a CDROM or a USB drive and capture the VLAN tagged traffic there, as your Windows driver might not support capturing of VLAN tags, as it seems to remove them in any case, regardless of config options you chose.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26994" class="comments-container"><span id="26998"></span><div id="comment-26998" class="comment"><div id="post-26998-score" class="comment-score"></div><div class="comment-text"><p>I'm sure there are VLAN because with Ubuntu, I can capture VLAN tags (to see my first message)</p></div><div id="comment-26998-info" class="comment-info"><span class="comment-age">(14 Nov '13, 05:22)</span> <span class="comment-user userinfo">wireshark_user</span></div></div><span id="27001"></span><div id="comment-27001" class="comment"><div id="post-27001-score" class="comment-score"></div><div class="comment-text"><p>Ah, I did not see the comment about Ubuntu.</p><p>Well, then you already have a solution, right? ;-))</p><p>If it does not work on Windows, it's (most certainly) a driver problem and there is nothing the Wireshark community can do to change that. It's rather an issue for the TP-Link support.</p></div><div id="comment-27001-info" class="comment-info"><span class="comment-age">(14 Nov '13, 05:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26994" class="comment-tools"></div><div class="clear"></div><div id="comment-26994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

