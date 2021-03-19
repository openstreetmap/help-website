+++
type = "question"
title = "10G Trace Tool"
description = '''We intend to setup a 10G/1G trace tool based on high end desktop components. The Wireshark and the Cace Pilot Software will be used. The system will be equipped with 1 TB SSD storage (PCI-e,2x 480GB) and should cover rates up to 3 Gbits/s.  Questions: Are the following Intel Network Card supported b...'''
date = "2011-09-02T03:24:00Z"
lastmod = "2011-09-02T18:04:00Z"
weight = 6059
keywords = [ "nic", "tool", "10g", "trace" ]
aliases = [ "/questions/6059" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [10G Trace Tool](/questions/6059/10g-trace-tool)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6059-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We intend to setup a 10G/1G trace tool based on high end desktop components. The Wireshark and the Cace Pilot Software will be used. The system will be equipped with 1 TB SSD storage (PCI-e,2x 480GB) and should cover rates up to 3 Gbits/s.</p><p>Questions: Are the following Intel Network Card supported by Wireshark and Cace Pilot? - 4 port - 1G Ethernet: Intel Ethernet Server Adapter I340-T4 - 1 Port - 10g Ethernet: Intel 10G Network Adapter Multimode (E10G81GF2R)</p><p>Is there any recommendations for Network NICs (1G copper and 10G Multimode)?</p><p>Our prefered OS will be a Windows7 Professional 64bit Version. Is this OS supported by Wireshark and Cace Pilot?</p><p>Best Regards, Dr. E. Grawenhof</p></div><div id="question-tags" class="tags-container tags">nic tool 10g trace</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '11, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/264149369edecff57fa39378196e9414?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grawenhof&#39;s gravatar image" /><p>Grawenhof<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grawenhof has no accepted answers">0%</span></p></div></div><div id="comments-container-6059" class="comments-container"></div><div id="comment-tools-6059" class="comment-tools"></div><div class="clear"></div><div id="comment-6059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6065"></span>

<div id="answer-container-6065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6065-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark and Pilot do not, in and of themselves, support any network adapters; on UN*X, Wireshark uses libpcap to capture traffic, and, on Windows, Wireshark uses WinPcap and I'm not sure Pilot itself captures traffic (as opposed to reading existing captures or telling Shark appliances to capture traffic).</p><p>libpcap runs atop the particular capture mechanism on the UN*X you're using, and WinPcap's driver runs atop NDIS; those mechanisms are network-adapter-independent, so they support any adapter whose driver plugs into the OS's networking stack.</p><p>So both of those Intel network adapters should work. Whether they'll offer sufficient performance is another matter. I don't have any recommendations to make in that regard.</p><p>Wireshark 1.6.x has both 32-bit and 64-bit versions for Windows, both of which should work on 64-bit Windows; the 64-bit version should be able to handle larger capture files. The "Requirements" tab on <a href="http://www.riverbed.com/us/products/cascade/cascade_pilot.php">the Cascade Pilot page</a> says it supports, among other versions of Windows, 64-bit Windows 7 Professional.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '11, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6065" class="comments-container"></div><div id="comment-tools-6065" class="comment-tools"></div><div class="clear"></div><div id="comment-6065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

