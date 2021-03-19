+++
type = "question"
title = "How to remove Acrylic NDIS driver from Wireshark?"
description = '''Hi guys, maybe you can help me out with this: I recently installed the Acrylic NDIS driver which comes with their free WiFi scanner in order to find out whether my NIC is capable of capturing in promiscuous mode. Unfortunately it wasn&#x27;t and so I uninstalled the software again. Virtually unaffected W...'''
date = "2015-05-18T23:43:00Z"
lastmod = "2015-05-19T08:15:00Z"
weight = 42526
keywords = [ "acrylic", "airpcap", "driver", "ndis", "uninstall" ]
aliases = [ "/questions/42526" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to remove Acrylic NDIS driver from Wireshark?](/questions/42526/how-to-remove-acrylic-ndis-driver-from-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42526-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>maybe you can help me out with this: I recently installed the Acrylic NDIS driver which comes with their free WiFi scanner in order to find out whether my NIC is capable of capturing in promiscuous mode. Unfortunately it wasn't and so I uninstalled the software again. Virtually unaffected Wireshark keeps displaying a warning after starting saying "Failed to open Airpcap adapters". I already re-installed Wireshark but it seems like there is still something left on my system which misleads Wireshark to have an Airpcap NIC attached.</p><p>Any idea how to solve this apart from a fresh Windows install? ;)</p><p>Cheers, Simon</p></div><div id="question-tags" class="tags-container tags">acrylic airpcap driver ndis uninstall</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '15, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/1000c880be2c3f58380d7dd0794cffa9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonL&#39;s gravatar image" /><p>SimonL<br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonL has no accepted answers">0%</span></p></div></div><div id="comments-container-42526" class="comments-container"><span id="42530"></span><div id="comment-42530" class="comment"><div id="post-42530-score" class="comment-score"></div><div class="comment-text"><p>have you installed the newest version of the software again with deselection all adapter related options? By the way it worked correct for me only on Win7 32bit with the Netgear AC6200.</p></div><div id="comment-42530-info" class="comment-info"><span class="comment-age">(19 May '15, 01:06)</span> Christian_R</div></div><span id="42544"></span><div id="comment-42544" class="comment"><div id="post-42544-score" class="comment-score"></div><div class="comment-text"><p>Hi Christian,</p><p>unfortunately it doesn't work for me :( Wireshark keeps complaining about a missing Airpcap adapter...</p></div><div id="comment-42544-info" class="comment-info"><span class="comment-age">(19 May '15, 08:10)</span> SimonL</div></div></div><div id="comment-tools-42526" class="comment-tools"></div><div class="clear"></div><div id="comment-42526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42546"></span>

<div id="answer-container-42546" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42546-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I did install it to try it out, and saw the same error messages, but I can't remember what I did to fix the issue. I certainly didn't reinstall my OS.</p><p>Try looking for airpcap.dll on your system.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '15, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-42546" class="comments-container"><span id="42556"></span><div id="comment-42556" class="comment"><div id="post-42556-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.acrylicwifi.com/en/blog/10-advanced-things-acrylic-wifi-free/">https://www.acrylicwifi.com/en/blog/10-advanced-things-acrylic-wifi-free/</a></p><p>Cite: "Wireshark support: <strong>The Acrylic driver installs a library</strong> called <strong>airpcap.dll on the folder system32</strong>. With this file you can emulate that tools like Wireshark believe that any WiFi card is an Airpcap, and from this moment on we can capture WiFi traffic on Windows with Wireshark. The only requirement is to start Wireshark as manager."</p></div><div id="comment-42556-info" class="comment-info"><span class="comment-age">(19 May '15, 12:07)</span> Kurt Knochner ♦</div></div><span id="42597"></span><div id="comment-42597" class="comment"><div id="post-42597-score" class="comment-score"></div><div class="comment-text"><p>Thank you guys, must have missed that section :)</p></div><div id="comment-42597-info" class="comment-info"><span class="comment-age">(20 May '15, 23:37)</span> SimonL</div></div></div><div id="comment-tools-42546" class="comment-tools"></div><div class="clear"></div><div id="comment-42546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

