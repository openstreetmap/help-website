+++
type = "question"
title = "analyzing packets"
description = '''I am new to wireshark, and am trying to learn as much as possible, and wasn&#x27;t sure where to start. I heard somewhere from doing research online that the books can&#x27;t teach/show you everything, so a good place to get started is to look around, use it, and to get familiar with it. I noticed on the wire...'''
date = "2012-11-27T15:34:00Z"
lastmod = "2012-11-27T16:37:00Z"
weight = 16356
keywords = [ "packets" ]
aliases = [ "/questions/16356" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [analyzing packets](/questions/16356/analyzing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16356-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark, and am trying to learn as much as possible, and wasn't sure where to start. I heard somewhere from doing research online that the books can't teach/show you everything, so a good place to get started is to look around, use it, and to get familiar with it. I noticed on the wireshark site that they have some captures. i thought it would be interesting to see what a virus/trojan looked like. I downloaded the slammer.pcap, and am trying to figure out the main things that would pop out warning the administrator that it is a malicious packet?</p></div><div id="question-tags" class="tags-container tags">packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '12, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/3962b2c1048cf6eda0cdbe8ad3434562?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="droidus&#39;s gravatar image" /><p>droidus<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="droidus has no accepted answers">0%</span></p></div></div><div id="comments-container-16356" class="comments-container"></div><div id="comment-tools-16356" class="comment-tools"></div><div class="clear"></div><div id="comment-16356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16362"></span>

<div id="answer-container-16362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16362-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and am trying to figure out the main things that would pop out warning the administrator that it is a malicious packet?</p></blockquote><p>Wireshark is a network analyzer, so it helps to detect problems within the network and/or with networked applications. Wireshark is <strong>unable</strong> to detect "malicious" content in a packet as it has no functionality for that. You can however do that manually, if you know what to look for.</p><p>There is an extension for Wireshark, called <a href="http://honeynet.org/node/790">WireShnork</a>, which combines the functionality of Wireshark with the detection capabilities of Snort. With that plugin, you will be able to detect malicious "actions/content" in a packet (or data stream), if there is a pattern for that specific attack. However, that's more a snort question than a Wireshark question.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '12, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Nov '12, 16:49</p></div></div><div id="comments-container-16362" class="comments-container"><span id="16364"></span><div id="comment-16364" class="comment"><div id="post-16364-score" class="comment-score"></div><div class="comment-text"><p>I could only see directions for linux commands. am i missing something for windows? also, there is no way to just look at this data, like the content, to tell if it is malicious?</p></div><div id="comment-16364-info" class="comment-info"><span class="comment-age">(27 Nov '12, 19:24)</span> droidus</div></div><span id="16376"></span><div id="comment-16376" class="comment"><div id="post-16376-score" class="comment-score"></div><div class="comment-text"><p>Well, if you need WireShnork for Windows, you need the following:</p><ul><li>snort version for Windows, which is available</li><li>you would have to compile the plugin yourself on Windows (follow the plugin developer guide).</li><li>you would have o extend the plugin code to work on windows (calling the snort binary).</li><li>download the plugin code</li></ul><p>Unfortunately, the code is currently not available, as the mentioned GIT server refuses the GIT connection !?!</p><blockquote><p>also, there is no way to just look at this data, like the content, to tell if it is malicious?</p></blockquote><p>Sure there is. As I mentioned, you can look into the packet content manually (that's the main usage of wireshark) and try to identifiy malicious code/activities. But then you need to know exactly what to look for.</p><p>In the case of <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=slammer.pcap">slammer.pcap</a> you can view the packet bytes in Wireshark.</p><blockquote><p><code>http://www.wireshark.org/docs/wsug_html_chunked/ChapterWork.html</code><br />
</p></blockquote><p>As the MS-SQL protocol is a binary protocol, you will only see the HEX representation of the packet bytes. If you can identify the attack in that packet, depends on your knowledge of how slammer works.</p></div><div id="comment-16376-info" class="comment-info"><span class="comment-age">(28 Nov '12, 03:52)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16362" class="comment-tools"></div><div class="clear"></div><div id="comment-16362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

