+++
type = "question"
title = "Is there dissector for Cisco RUDP/BSM Version 1 used for ISDN/PRI  backhaul?"
description = '''Hello, team! I use Wireshark for viewing Cisco&#x27;s SLT RUDP/BSMV0 (Backhaul session Manager Version 0) used for SS7 ISUP/MTP3 management backhaul. But Cisco also uses another flavor of RUDP/SM stack called BSM V1 (version 1 versus Version 0 used for SS7). It used at place where IUA should be used name...'''
date = "2011-05-03T23:46:00Z"
lastmod = "2011-05-04T06:25:00Z"
weight = 3907
keywords = [ "pri", "rudp", "cisco", "isdn", "sm" ]
aliases = [ "/questions/3907" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there dissector for Cisco RUDP/BSM Version 1 used for ISDN/PRI backhaul?](/questions/3907/is-there-dissector-for-cisco-rudpbsm-version-1-used-for-isdnpri-backhaul)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3907-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, team! I use Wireshark for viewing Cisco's SLT RUDP/BSMV0 (Backhaul session Manager Version 0) used for SS7 ISUP/MTP3 management backhaul. But Cisco also uses another flavor of RUDP/SM stack called BSM V1 (version 1 versus Version 0 used for SS7). It used at place where IUA should be used namely for backhauling ISDN PRI from Media Gateway to Media Gateway Controller. http://en.wikipedia.org/wiki/Reliable_User_Datagram_Protocol for few details. Does anyone has idea how to cope with it? Setting decode for RUDP on that flow reveals some strange MTP3 exchange between strange OPC and DPC which is wrong here. I can see in those packets Calling and Called party numbers and Display IE (calling party name Id). Thanks in advance, Greg Shkolnik. P.S. I can provide sample captures on demand.</p></div><div id="question-tags" class="tags-container tags">pri rudp cisco isdn sm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '11, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/707cb4becf78e2192d64f5a35baa9994?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gregshk&#39;s gravatar image" /><p>Gregshk<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gregshk has no accepted answers">0%</span></p></div></div><div id="comments-container-3907" class="comments-container"><span id="10236"></span><div id="comment-10236" class="comment"><div id="post-10236-score" class="comment-score"></div><div class="comment-text"><p>Hi gays! I need BSM V1 (Cisco) dissector too.</p></div><div id="comment-10236-info" class="comment-info"><span class="comment-age">(18 Apr '12, 02:00)</span> ars</div></div></div><div id="comment-tools-3907" class="comment-tools"></div><div class="clear"></div><div id="comment-3907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3916"></span>

<div id="answer-container-3916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3916-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd suggest you open an enhancement request on https://bugs.wireshark.org providing this description and a sample capture (preferably with some details of what the bytes are supposed to be). Someone could (if they have the time) reverse engineer (if necessary) V1 and either add a preference to the RUDP dissector to choose the version or maybe figure out the version from the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-3916" class="comments-container"></div><div id="comment-tools-3916" class="comment-tools"></div><div class="clear"></div><div id="comment-3916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

