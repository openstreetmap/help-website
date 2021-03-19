+++
type = "question"
title = "10gbps network capturing"
description = '''Hello I was wondering if the wiredhark can properly capture 10gbps network trafic without losses of data. If the issue has been tested it would realy help. There is no hw limitation because ssd drive is used with xeon 2637v3 dual cpu and ddr4 32GB of ram. Wireshark 1.12.3 64bit version is used'''
date = "2015-02-17T02:32:00Z"
lastmod = "2015-02-17T04:01:00Z"
weight = 39907
keywords = [ "10g" ]
aliases = [ "/questions/39907" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [10gbps network capturing](/questions/39907/10gbps-network-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39907-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I was wondering if the wiredhark can properly capture 10gbps network trafic without losses of data. If the issue has been tested it would realy help. There is no hw limitation because ssd drive is used with xeon 2637v3 dual cpu and ddr4 32GB of ram. Wireshark 1.12.3 64bit version is used</p></div><div id="question-tags" class="tags-container tags">10g</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '15, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/353a2ff67b3cf198e82f93399b74f097?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dima&#39;s gravatar image" /><p>Dima<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dima has no accepted answers">0%</span></p></div></div><div id="comments-container-39907" class="comments-container"><span id="39910"></span><div id="comment-39910" class="comment"><div id="post-39910-score" class="comment-score"></div><div class="comment-text"><p>There was a great talk at Sharkfest 14 by Andrew Brown covering this topic.</p><p>You can find his presentation at <a href="http://sharkfest.wireshark.org/assets/presentations/I3:%20Sharkfest_2014_ABrown%20-%20Copy.pdf">http://sharkfest.wireshark.org/assets/presentations/I3:%20Sharkfest_2014_ABrown%20-%20Copy.pdf</a> or <a href="http://sharkfest.wireshark.org/assets/presentations/I3.pptx">http://sharkfest.wireshark.org/assets/presentations/I3.pptx</a></p></div><div id="comment-39910-info" class="comment-info"><span class="comment-age">(17 Feb '15, 03:49)</span> Uli</div></div></div><div id="comment-tools-39907" class="comment-tools"></div><div class="clear"></div><div id="comment-39907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39911"></span>

<div id="answer-container-39911" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39911-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you aware of the fact that Wireshark doesn't capture data? For this task it spawns dumpcap, which, using libpcap/winpcap, captures the data, and hands it over to Wireshark.</p><p>So you have to look into equipment that can handle the wirespeed, writing that to storage and offer Wireshark the option to open the capture files for detailed analysis. You should look into some dedicated capture hardware (nice platform details you listed, but what about the capture hardware??), to handle this deluge of data. A quick internet search shows there enough options. And have a look at what Riverbed has on offer, being the home of Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '15, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39911" class="comments-container"></div><div id="comment-tools-39911" class="comment-tools"></div><div class="clear"></div><div id="comment-39911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

