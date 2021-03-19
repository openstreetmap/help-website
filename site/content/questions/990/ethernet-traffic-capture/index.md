+++
type = "question"
title = "Ethernet traffic capture"
description = '''Can I capture all traffic in my LAN? not only my pc traffic. I want to get the packets from other¡s pc&#x27;s in the same workgroup. For example: I want to be able to know wich pages is other people visiting. assuming that I have ip 172.17.223.15 and I want to see the traffic of 172.17.223.16 Is it that ...'''
date = "2010-11-17T10:28:00Z"
lastmod = "2010-11-18T04:25:00Z"
weight = 990
keywords = [ "ethernet", "capture" ]
aliases = [ "/questions/990" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Ethernet traffic capture](/questions/990/ethernet-traffic-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-990-score" class="post-score" title="current number of votes">0</div><span id="post-990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I capture all traffic in my LAN? not only my pc traffic.</p><p>I want to get the packets from other¡s pc's in the same workgroup.</p><p>For example: I want to be able to know wich pages is other people visiting. assuming that I have ip 172.17.223.15 and I want to see the traffic of 172.17.223.16</p><p>Is it that possible?¿ PD:Sorry for my bad english.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '10, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/6a6ea63da438eab511f9e8724e685e37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umbertix&#39;s gravatar image" /><p><span>umbertix</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umbertix has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Nov '10, 10:40</strong> </span></p></div></div><div id="comments-container-990" class="comments-container"></div><div id="comment-tools-990" class="comment-tools"></div><div class="clear"></div><div id="comment-990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="997"></span>

<div id="answer-container-997" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-997-score" class="post-score" title="current number of votes">1</div><span id="post-997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="umbertix has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This depends on your network. If you have a central Hub (not a Switch) you can see all data passing by, but it is highly unlikely that you're not using a Switch (because hubs are slooooooow). On a switch, you can only receive broadcasts and other single packets that are flooded to all ports because of an unknown destination MAC address, but you will not see complete communication flows of others. The switch will hide it from you because it is connecting stations directly without broadcasting the data to all other stations.</p><p>One way to get around this problem of not seeing the packets you want is to use a SPAN session (a.k.a mirror port, monitor port etc.), but that requires the switch in use to be manageable. Some better SOHO switches can do that, usually via web interface. If your switch is "dumb" and cannot be managed you're out of luck, unless you try to leverage some hacking techniques like ARP cache poisoning on the network. Or you can get one of the fancy Dualcomm switches with built-in monitor ports and replace your switch with it :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '10, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-997" class="comments-container"><span id="1000"></span><div id="comment-1000" class="comment"><div id="post-1000-score" class="comment-score"></div><div class="comment-text"><p>See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">the Wireshark Wiki page on Ethernet capture setup</a> for more information on Ethernet captures and switches; it also refers you to <a href="http://wiki.wireshark.org/SwitchReference">the Wireshark Wiki switch reference pages</a> for information on SPAN sessions/mirror ports/etc. for various brands of switches.</p></div><div id="comment-1000-info" class="comment-info"><span class="comment-age">(17 Nov '10, 18:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="1004"></span><div id="comment-1004" class="comment"><div id="post-1004-score" class="comment-score"></div><div class="comment-text"><p>Thx for quick answering.</p><p>Thats a good comunity</p></div><div id="comment-1004-info" class="comment-info"><span class="comment-age">(18 Nov '10, 04:25)</span> <span class="comment-user userinfo">umbertix</span></div></div></div><div id="comment-tools-997" class="comment-tools"></div><div class="clear"></div><div id="comment-997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

