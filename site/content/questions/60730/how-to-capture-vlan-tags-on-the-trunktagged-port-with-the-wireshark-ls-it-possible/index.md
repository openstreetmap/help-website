+++
type = "question"
title = "How to capture VLAN tags on the trunk/tagged port with the Wireshark. ls it possible?"
description = '''Hi All, As the title says: How to capture VLAN tags on the trunk/tagged port with the Wireshark. is it possible? Let&#x27;s say I do have a switchport configured listening on the &quot;tags&quot; 10,20,30 (trunk port really). Haker connects with PC to this port. Running Wireshark. What info will hacker able to see...'''
date = "2017-04-11T03:37:00Z"
lastmod = "2017-04-11T04:07:00Z"
weight = 60730
keywords = [ "vlan" ]
aliases = [ "/questions/60730" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture VLAN tags on the trunk/tagged port with the Wireshark. ls it possible?](/questions/60730/how-to-capture-vlan-tags-on-the-trunktagged-port-with-the-wireshark-ls-it-possible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60730-score" class="post-score" title="current number of votes">0</div><span id="post-60730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>As the title says: How to capture VLAN tags on the trunk/tagged port with the Wireshark. is it possible? Let's say I do have a switchport configured listening on the "tags" 10,20,30 (trunk port really). Haker connects with PC to this port. Running Wireshark. What info will hacker able to see?</p><p>Thank you, Mykhaylo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '17, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/bc027ad1ed53177bd22a7ef8bd4cab03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Myky&#39;s gravatar image" /><p><span>Myky</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Myky has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Apr '17, 03:38</strong> </span></p></div></div><div id="comments-container-60730" class="comments-container"></div><div id="comment-tools-60730" class="comment-tools"></div><div class="clear"></div><div id="comment-60730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60731"></span>

<div id="answer-container-60731" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60731-score" class="post-score" title="current number of votes">0</div><span id="post-60731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Myky has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the packets leaving the switch on that port have the 802.1Q tag (which they should, as you said it's a trunk port) then yes, you can see them. <strong>But</strong> since at the port resides no real traffic destination, only few packets will be sent using that port. Mostly it'll be broadcast and multicast traffic, but if you worry about VLAN tags: yes, the "hacker" can see them (assuming a compatible NIC is used for the capture).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '17, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Apr '17, 13:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-60731" class="comments-container"><span id="60733"></span><div id="comment-60733" class="comment"><div id="post-60733-score" class="comment-score"></div><div class="comment-text"><p>Hello Jasper,</p><p>Appreciate your response. So idea is to understand if I do have switch port configured for Access Point where management VLAN is also tagged by AP (apart from the different SSID VLANS). So lets say SSID1=10, SSID2=20 and MGMT VLAN=30. Switchport configured as a trunk to accept 10, 20 and 30 VLAN tags. So hacker removes the AP and plugs in his PC, fire up wireshark and all VLAN tags are visible. Is that correct?</p><p>Thank you, Mykhaylo</p></div><div id="comment-60733-info" class="comment-info"><span class="comment-age">(11 Apr '17, 04:00)</span> <span class="comment-user userinfo">Myky</span></div></div><span id="60734"></span><div id="comment-60734" class="comment"><div id="post-60734-score" class="comment-score">1</div><div class="comment-text"><p>yes, that's correct, but not really "hacking" - it's a physical security issue :-)</p></div><div id="comment-60734-info" class="comment-info"><span class="comment-age">(11 Apr '17, 04:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="60735"></span><div id="comment-60735" class="comment"><div id="post-60735-score" class="comment-score"></div><div class="comment-text"><p>Yep l do agree :0 thanks!</p></div><div id="comment-60735-info" class="comment-info"><span class="comment-age">(11 Apr '17, 04:07)</span> <span class="comment-user userinfo">Myky</span></div></div></div><div id="comment-tools-60731" class="comment-tools"></div><div class="clear"></div><div id="comment-60731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

