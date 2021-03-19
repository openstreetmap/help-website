+++
type = "question"
title = "Lack of MAC resolution in tshark on Raspberry Pi"
description = '''So from checking here it seems that the current build of tshark that runs on RasPi does not support the wlan.sa_resolved field for MAC name resolution. Is there any way around this? A manual install version that will run on a Raspberry Pi perhaps?'''
date = "2015-03-22T03:05:00Z"
lastmod = "2015-03-25T09:33:00Z"
weight = 40764
keywords = [ "raspberry", "tshark", "debian" ]
aliases = [ "/questions/40764" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lack of MAC resolution in tshark on Raspberry Pi](/questions/40764/lack-of-mac-resolution-in-tshark-on-raspberry-pi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40764-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So from checking here it seems that the current build of tshark that runs on RasPi does not support the wlan.sa_resolved field for MAC name resolution. Is there any way around this? A manual install version that will run on a Raspberry Pi perhaps?</p></div><div id="question-tags" class="tags-container tags">raspberry tshark debian</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '15, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/6ad9c485468672305ea947f0acdebd32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="youcloudsofddom&#39;s gravatar image" /><p>youcloudsofddom<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="youcloudsofddom has no accepted answers">0%</span></p></div></div><div id="comments-container-40764" class="comments-container"><span id="40784"></span><div id="comment-40784" class="comment"><div id="post-40784-score" class="comment-score"></div><div class="comment-text"><p>what is you tshark version on the Pi (tshark -v)?</p></div><div id="comment-40784-info" class="comment-info"><span class="comment-age">(23 Mar '15, 09:58)</span> Kurt Knochner ♦</div></div><span id="40789"></span><div id="comment-40789" class="comment"><div id="post-40789-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner It's 1.8.2</p></div><div id="comment-40789-info" class="comment-info"><span class="comment-age">(23 Mar '15, 15:52)</span> youcloudsofddom</div></div></div><div id="comment-tools-40764" class="comment-tools"></div><div class="clear"></div><div id="comment-40764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40820"></span>

<div id="answer-container-40820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40820-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like the maintainer of the Raspberry Pi package for tshark did not include the manufacturers file (maybe to keep the package small). Perhaps it is enough to copy the "manuf" file from your mac to the Raspberry Pi to the global preferences directory (search for the cfilters, dfilters and colorfilters files if you're not sure which directory contains the global preferences).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40820" class="comments-container"><span id="40845"></span><div id="comment-40845" class="comment"><div id="post-40845-score" class="comment-score"></div><div class="comment-text"><p>manuf is right there, from libwireshark-data, in /usr/share/wireshark/. The problem is that the dissector of his version of tshark doesn't have that field.</p></div><div id="comment-40845-info" class="comment-info"><span class="comment-age">(25 Mar '15, 09:30)</span> Jaap ♦</div></div><span id="40854"></span><div id="comment-40854" class="comment"><div id="post-40854-score" class="comment-score"></div><div class="comment-text"><p>Oops, you're right. I did not bother to check <a href="https://www.wireshark.org/docs/dfref/w/wlan.html">https://www.wireshark.org/docs/dfref/w/wlan.html</a></p></div><div id="comment-40854-info" class="comment-info"><span class="comment-age">(25 Mar '15, 12:05)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-40820" class="comment-tools"></div><div class="clear"></div><div id="comment-40820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40846"></span>

<div id="answer-container-40846" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40846-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I check the Raspbian repository I see that they have a package for Wireshark 1.12.1 (including tshark), of which the wireless LAN dissector has this field. What would be needed, with respect to required other packages, I do not know. I may require a more extensive upgrade (to jessie/testing maybe). That is depending on the distribution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '15, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40846" class="comments-container"></div><div id="comment-tools-40846" class="comment-tools"></div><div class="clear"></div><div id="comment-40846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

