+++
type = "question"
title = "packet capture best practice"
description = '''I&#x27;m attempting to capture a poor quality VoIP session for two users on the network. I have isolated the users to their own Cisco managed PoE switch which connects back into our main switch, also a Cisco. I haven&#x27;t mirrored either of the user&#x27;s port to the port where wireshark is running on a Windows...'''
date = "2017-07-10T13:31:00Z"
lastmod = "2017-07-10T15:19:00Z"
weight = 62650
keywords = [ "capture", "practice", "packet" ]
aliases = [ "/questions/62650" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [packet capture best practice](/questions/62650/packet-capture-best-practice)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62650-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm attempting to capture a poor quality VoIP session for two users on the network. I have isolated the users to their own Cisco managed PoE switch which connects back into our main switch, also a Cisco. I haven't mirrored either of the user's port to the port where wireshark is running on a Windows 7 PC.</p><p>Was able to capture a fairly small amount of data during a time when one of the users was experiencing the clipping. Will this pcap contain the information I need to analyze or do I need to mirror one of the user ports to capture anything useful?</p><p>I have noticed that about 50% of the traffic is ARP. Is that "normal"?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">capture practice packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '17, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/03945af0d6f3e344515a513d9505bcfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TonyB&#39;s gravatar image" /><p>TonyB<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TonyB has no accepted answers">0%</span></p></div></div><div id="comments-container-62650" class="comments-container"></div><div id="comment-tools-62650" class="comment-tools"></div><div class="clear"></div><div id="comment-62650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62652"></span>

<div id="answer-container-62652" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62652-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From a best-practice point of view, you really need a tap or span port off the switch. So likely without a mirror you do not have relevant data to diagnose your issue.</p><p>50% ARP, without context, does not really mean anything. If you have a LOT of traffic, and half is ARP, then you likely have a problem. If you have almost no traffic, then 50% ARP traffic probably does not mean much. What you describe is consistent: you are not on a mirror or span port, so you are only capturing broadcast traffic from the network (maybe some multicast too, depending on specific configurations). Some ARP traffic is classically broadcast, so that makes sense as long as there is not a lot of it in packets/sec.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '17, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-62652" class="comments-container"><span id="62674"></span><div id="comment-62674" class="comment"><div id="post-62674-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Bob. I've mirrored the port and will review the data once the issue happens again. Appreciate the very clear response.</p></div><div id="comment-62674-info" class="comment-info"><span class="comment-age">(11 Jul '17, 07:50)</span> TonyB</div></div></div><div id="comment-tools-62652" class="comment-tools"></div><div class="clear"></div><div id="comment-62652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

