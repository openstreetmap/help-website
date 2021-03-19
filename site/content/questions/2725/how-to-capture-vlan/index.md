+++
type = "question"
title = "How to capture vlan"
description = '''I trying to capture what Vlan certain ports are configured for on my switch. Can wireshark do this? If so how do I set it up?'''
date = "2011-03-09T07:38:00Z"
lastmod = "2011-03-09T09:00:00Z"
weight = 2725
keywords = [ "capture", "setup", "vlan" ]
aliases = [ "/questions/2725" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture vlan](/questions/2725/how-to-capture-vlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2725-score" class="post-score" title="current number of votes">0</div><span id="post-2725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I trying to capture what Vlan certain ports are configured for on my switch. Can wireshark do this? If so how do I set it up?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '11, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/f08dee8edd2a99f10c183fc5a0143140?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theman&#39;s gravatar image" /><p><span>theman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theman has no accepted answers">0%</span></p></div></div><div id="comments-container-2725" class="comments-container"></div><div id="comment-tools-2725" class="comment-tools"></div><div class="clear"></div><div id="comment-2725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2733"></span>

<div id="answer-container-2733" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2733-score" class="post-score" title="current number of votes">1</div><span id="post-2733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would go for the password recovery procedure as that will give you 100% certainty. If you want to deduct the vlan configuration of the switch you might be in luck by the packets it's sending.</p><ul><li>The easiest would be to monitor the broadcast traffic on each port (especially the arp requests) and map the source ip addresses to your vlans.</li><li>If CDP or similar protocol is enabled on the switch, it will tell you the "Native Vlan ID" for the port on which the CDP packet was sent.</li><li>If Spanning-Tree is configured on the ports, depending on version of the protocol used, it may show you the vlan ID in the "Bridge System ID Extension" field.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '11, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2733" class="comments-container"></div><div id="comment-tools-2733" class="comment-tools"></div><div class="clear"></div><div id="comment-2733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2727"></span>

<div id="answer-container-2727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2727-score" class="post-score" title="current number of votes">0</div><span id="post-2727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might be able to capture VLAN tags but only if you capture on a switch trunk port by introducing a hub/tap, or by mirroring it to the analyzer port including the VLAN tags (which otherwise might be stripped).</p><p>On the other hand: if you want to have a list of which ports are configured with which VLANs you should dump a switch port statistic on the switch itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '11, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2727" class="comments-container"><span id="2728"></span><div id="comment-2728" class="comment"><div id="post-2728-score" class="comment-score"></div><div class="comment-text"><p>Ok, the problem is I can not access the switch config. The company lost the password. So I'm trying to configure a new switch for the network. It's multiple switches on the network and they are using the same vlan config. So I thought I could use wireshark to sniff the vlan config for each port. I'm very new at network sniffing</p></div><div id="comment-2728-info" class="comment-info"><span class="comment-age">(09 Mar '11, 07:51)</span> <span class="comment-user userinfo">theman</span></div></div><span id="2729"></span><div id="comment-2729" class="comment"><div id="post-2729-score" class="comment-score"></div><div class="comment-text"><p>Ok, I see. Can you access ANY of the switches, or do they all have the same password nobody knows about? Maybe you can find one where you can login and determine the VLAN config for the new switch?</p><p>What you can do is use Wireshark on each port by inserting a hub or (even better) a small switch with integrated monitor port (like the Dual-Comm DCSW-1005). That way you can see if there are any visible VLAN tags - if not you don't have a trunk port, otherwise you can see what VLANs are in use on that trunk.</p></div><div id="comment-2729-info" class="comment-info"><span class="comment-age">(09 Mar '11, 08:18)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="2731"></span><div id="comment-2731" class="comment"><div id="post-2731-score" class="comment-score"></div><div class="comment-text"><p>Ok, I will try. Also, I talked with the switch manufacture and they provided me with a back door access. Hope it work thanks Jasper</p></div><div id="comment-2731-info" class="comment-info"><span class="comment-age">(09 Mar '11, 08:43)</span> <span class="comment-user userinfo">theman</span></div></div></div><div id="comment-tools-2727" class="comment-tools"></div><div class="clear"></div><div id="comment-2727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

