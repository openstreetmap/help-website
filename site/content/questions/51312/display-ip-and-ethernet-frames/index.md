+++
type = "question"
title = "Display IP and ETHERNET Frames"
description = '''I am trying to display a complete http conversation sequence but all I am getting are HTTP and TCP frames in the trace. I have tried a number of different iterations of the capture and display options but no luck.  Please help!!  michael'''
date = "2016-03-31T06:57:00Z"
lastmod = "2016-03-31T08:25:00Z"
weight = 51312
keywords = [ "displayip" ]
aliases = [ "/questions/51312" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Display IP and ETHERNET Frames](/questions/51312/display-ip-and-ethernet-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51312-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to display a complete http conversation sequence but all I am getting are HTTP and TCP frames in the trace. I have tried a number of different iterations of the capture and display options but no luck.<br />
</p><p>Please help!! michael</p></div><div id="question-tags" class="tags-container tags">displayip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '16, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/c4716dc2bb5be564438219b7b4c2c3e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michael325&#39;s gravatar image" /><p>michael325<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michael325 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-51312" class="comments-container"></div><div id="comment-tools-51312" class="comment-tools"></div><div class="clear"></div><div id="comment-51312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51313"></span>

<div id="answer-container-51313" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51313-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>They are all there. In the Protocol column, Wireshark displays only the highest level protocol present in the frame. Look in the Packet Details pane. HTTP is encapsulated in TCP, which is in IP, which is in Ethernet.</p><p>All your HTTP frames are also TCP, IP, and Ethernet, and all your TCP frames are also IP and Ethernet. If a packet does not have data, Wireshark identifies it as just TCP, not HTTP, even though it's running over a port recognized as HTTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '16, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51313" class="comments-container"><span id="51316"></span><div id="comment-51316" class="comment"><div id="post-51316-score" class="comment-score"></div><div class="comment-text"><p>Jim, I suspected that something like your description was the case. My confusion still is that non of the packets show "IP" in the protocol column. Would it not be the highest level protocol in some cases. Same applies to ethernet. Or by "highest" would the order be http, tcp, ip and then eternet?</p><p>Sorry to be so obtuse but I am just a rank beginner with networking. My past experience is such things as bsc and SNA. :-)</p></div><div id="comment-51316-info" class="comment-info"><span class="comment-age">(31 Mar '16, 12:05)</span> michael325</div></div><span id="51319"></span><div id="comment-51319" class="comment"><div id="post-51319-score" class="comment-score"></div><div class="comment-text"><p>Could you Provide us thaw capture file at a public accessible place like Dropbox? You can use a tool like tracewrangler to anomyze the trace</p></div><div id="comment-51319-info" class="comment-info"><span class="comment-age">(31 Mar '16, 12:14)</span> Christian_R</div></div><span id="51320"></span><div id="comment-51320" class="comment"><div id="post-51320-score" class="comment-score">1</div><div class="comment-text"><p>In this instance, HTTP is the highest layer, TCP is below that, then IP, then Ethernet. No, IP will never be the highest level. IP is used to transport something. We don't send IP packets if there's nothing to put in them. Same for Ethernet. We don't send an Ethernet frame if we don't have some higher-layer payload to put in it.</p></div><div id="comment-51320-info" class="comment-info"><span class="comment-age">(31 Mar '16, 12:19)</span> Jim Aragon</div></div><span id="51324"></span><div id="comment-51324" class="comment"><div id="post-51324-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jim.. That answers my question. Also makes this clear to me!! michael</p></div><div id="comment-51324-info" class="comment-info"><span class="comment-age">(31 Mar '16, 13:16)</span> michael325</div></div><span id="51340"></span><div id="comment-51340" class="comment"><div id="post-51340-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-51340-info" class="comment-info"><span class="comment-age">(01 Apr '16, 02:18)</span> Jaap ♦</div></div></div><div id="comment-tools-51313" class="comment-tools"></div><div class="clear"></div><div id="comment-51313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

