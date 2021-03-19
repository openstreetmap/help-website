+++
type = "question"
title = "Exporting all streams in a pcap as C Arrays text files with tshark"
description = '''Hey guys, I hope what I&#x27;m trying to achieve isn&#x27;t too complicated: Let&#x27;s say I have a pretty small pcap, I can go packet by packet and click &quot;Follow TCP&#92;UDP stream&quot; and save what I get as C Arrays file, and if something is saved already - not to save it again (let&#x27;s say all the files are in the same...'''
date = "2016-02-24T07:59:00Z"
lastmod = "2016-02-25T15:14:00Z"
weight = 50472
keywords = [ "follow", "stream", "streams", "tshark", "tcp" ]
aliases = [ "/questions/50472" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting all streams in a pcap as C Arrays text files with tshark](/questions/50472/exporting-all-streams-in-a-pcap-as-c-arrays-text-files-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50472-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I hope what I'm trying to achieve isn't too complicated: Let's say I have a pretty small pcap, I can go packet by packet and click "Follow TCP\UDP stream" and save what I get as C Arrays file, and if something is saved already - not to save it again (let's say all the files are in the same folder) Now I want to automate it with tshark. Every file need to have a number based on the first packet that created this stream. Assuming I got a pcap with 2 streams, the first is a UDP DNS request to google servers and the second is just some http browsing. I want to get 2 files in my folder: 0_UDP and 1_TCP. Each file will contain what it would have contained if I clicked "Follow tcp\udp stream" in the gui and saved as C Arrays.</p></div><div id="question-tags" class="tags-container tags">follow stream streams tshark tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '16, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/c71b705d6928f48abe7ba18a85e37a2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danielcp&#39;s gravatar image" /><p>danielcp<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danielcp has no accepted answers">0%</span></p></div></div><div id="comments-container-50472" class="comments-container"></div><div id="comment-tools-50472" class="comment-tools"></div><div class="clear"></div><div id="comment-50472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50519"></span>

<div id="answer-container-50519" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50519-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark has the "-z follow" option to allow automation of following TCP and UDP (and SSL) streams but this option does not have the ability to save the results as C arrays. It does have a "raw" (hexadecimal) output which wouldn't be hard to manipulate into C arrays. You could also <a href="https://bugs.wireshark.org">raise an enhancement request</a> to ask that C arrays be added as an output option.</p><p>(Using that option would also require you to call tshark multiple times, once for each stream you want to save.)</p><p>Other tools such as tcpflow might also work for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '16, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-50519" class="comments-container"></div><div id="comment-tools-50519" class="comment-tools"></div><div class="clear"></div><div id="comment-50519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

