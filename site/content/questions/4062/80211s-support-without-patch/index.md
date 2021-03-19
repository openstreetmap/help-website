+++
type = "question"
title = "802.11s support without patch"
description = '''Hi, Is there a version of wireshark source code that supports 802.11s (mesh) protocol and does not require a patch. Thank you very much.'''
date = "2011-05-12T22:08:00Z"
lastmod = "2011-05-13T06:00:00Z"
weight = 4062
keywords = [ "802.11s", "mesh" ]
aliases = [ "/questions/4062" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11s support without patch](/questions/4062/80211s-support-without-patch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4062-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Is there a version of wireshark source code that supports 802.11s (mesh) protocol and does not require a patch.</p><p>Thank you very much.</p></div><div id="question-tags" class="tags-container tags">802.11s mesh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '11, 22:08</strong></p><img src="https://secure.gravatar.com/avatar/5e8388d49cbd970492ac855ab25e179d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bthapa&#39;s gravatar image" /><p>bthapa<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bthapa has no accepted answers">0%</span></p></div></div><div id="comments-container-4062" class="comments-container"></div><div id="comment-tools-4062" class="comment-tools"></div><div class="clear"></div><div id="comment-4062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4063"></span>

<div id="answer-container-4063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4063-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Initial support for the Hybrid Wireless Mesh Protocol was added to the 802.11 dissector on May 25, 2010 in <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=32955">r32955</a> and was backported to the 1.4.x branch but not the 1.2.x branch.</p><p>So, if you download the latest sources for either the trunk or the trunk-1.4 branch, you will have a version of wireshark source code that supports 802.11s that does not require a patch. See <a href="http://www.wireshark.org/develop.html">http://www.wireshark.org/develop.html</a> for information on how to obtain the source code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '11, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4063" class="comments-container"><span id="4071"></span><div id="comment-4071" class="comment"><div id="post-4071-score" class="comment-score"></div><div class="comment-text"><p>Chris, I compiled and installed the latest source from trunk. Then I tried to open http://o11s.org/files/mesh_traffic.cap. It didn't parse the Mesh parameters in the IEEE 802.11 Management Frame field :(. I am trying the latest stable wireshark version now..1.4.6. I will update you soon with a success story or a failure.</p></div><div id="comment-4071-info" class="comment-info"><span class="comment-age">(13 May '11, 12:38)</span> bthapa</div></div><span id="4073"></span><div id="comment-4073" class="comment"><div id="post-4073-score" class="comment-score">1</div><div class="comment-text"><p>Well, I am mistaken. Support was added but not enabled as MESH_OVERRIDES was left undefined. I'm not sure why that was, perhaps because it's still in draft? In any case, there is no current version of Wireshark available that will dissect 802.11s without a patch. I was going to check in a change to support it, but I noticed some redefintions taking place as a result, and I don't know enough or have the time to look at the implications. I would suggest filing a bugzilla bug report asking to have it enabled. If there are conflicts, perhaps an IEEE802.11 preference could be added instead.</p></div><div id="comment-4073-info" class="comment-info"><span class="comment-age">(13 May '11, 13:10)</span> cmaynard ♦♦</div></div><span id="4075"></span><div id="comment-4075" class="comment"><div id="post-4075-score" class="comment-score">1</div><div class="comment-text"><p>As I recall, MESH_OVERRIDES was undefined because some of the tag IDs conflict with pre-existing code.</p></div><div id="comment-4075-info" class="comment-info"><span class="comment-age">(13 May '11, 13:36)</span> Gerald Combs ♦♦</div></div><span id="4079"></span><div id="comment-4079" class="comment"><div id="post-4079-score" class="comment-score"></div><div class="comment-text"><p>Ok. I even reverted back to svn r32955. Compiled/Installed and even that could not parse the mesh_traffic.cap from http://o11s.org/files/mesh_traffic.cap. Do you have any suggestion for me?</p><p>Is there any specific wireshark source version that you know works and recommend me using which has a patch known to work. I have tried wireshark-1.2.* version with patch wireshark-1.2.3-mesh-support from http://o11s.org/patches/wireshark/wireshark-1.2.3-mesh-support.patch</p><p>and that does not work either</p><p>Thank you Chris and Gerald.</p></div><div id="comment-4079-info" class="comment-info"><span class="comment-age">(13 May '11, 14:25)</span> bthapa</div></div><span id="4080"></span><div id="comment-4080" class="comment"><div id="post-4080-score" class="comment-score"></div><div class="comment-text"><p>As I mentioned above, I would suggest filing a Wireshark bug report at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a> asking to have 802.11s support completed. I'd also recommend attaching the capture file to the bug report.</p></div><div id="comment-4080-info" class="comment-info"><span class="comment-age">(13 May '11, 14:53)</span> cmaynard ♦♦</div></div><span id="4082"></span><div id="comment-4082" class="comment not_top_scorer"><div id="post-4082-score" class="comment-score"></div><div class="comment-text"><p>Looking at the code, tags 52, 55, and 69 conflict with 802.11r-2008.</p></div><div id="comment-4082-info" class="comment-info"><span class="comment-age">(13 May '11, 15:33)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-4063" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-4063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

