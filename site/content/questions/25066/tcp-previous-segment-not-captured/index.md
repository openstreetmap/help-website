+++
type = "question"
title = "TCP previous segment not captured, ..."
description = '''Hi  I have a scenario where vlan traffic is going through gateway SVI and some specific traffic is routed through Route-map to Cisco ASA placed in the same VLAN, Now using VMware View client when traffic is routed through route-map Vmware View does not work after authentication saying &quot;TCP previous ...'''
date = "2013-09-21T08:25:00Z"
lastmod = "2013-09-22T22:59:00Z"
weight = 25066
keywords = [ "ir" ]
aliases = [ "/questions/25066" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP previous segment not captured, ...](/questions/25066/tcp-previous-segment-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25066-score" class="post-score" title="current number of votes">0</div><span id="post-25066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have a scenario where vlan traffic is going through gateway SVI and some specific traffic is routed through Route-map to Cisco ASA placed in the same VLAN, Now using VMware View client when traffic is routed through route-map Vmware View does not work after authentication saying "TCP previous segment not captured" , but when i manually add gateway as ASA, Application works perfectly, i am assuming that some packets are missing within this routing.Getting confused need expert opinion. Here are the capture <a href="http://cloudshark.org/captures/8b0542a4523f">http://cloudshark.org/captures/8b0542a4523f</a> Failed attempt <a href="http://cloudshark.org/captures/b5a9187cb96b">http://cloudshark.org/captures/b5a9187cb96b</a> Successful attempt</p><p>Ir</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ir" rel="tag" title="see questions tagged &#39;ir&#39;">ir</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '13, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/0822b856a5ac48f5b03ded3357b99af2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="imrans&#39;s gravatar image" /><p><span>imrans</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="imrans has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Sep '13, 08:25</strong> </span></p></div></div><div id="comments-container-25066" class="comments-container"></div><div id="comment-tools-25066" class="comment-tools"></div><div class="clear"></div><div id="comment-25066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25070"></span>

<div id="answer-container-25070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25070-score" class="post-score" title="current number of votes">0</div><span id="post-25070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Vmware View does not work after authentication saying "TCP previous segment not captured"</p></blockquote><p>So the VMmare_View client is failing after authentication but I suppose the "TCP previous segment not captured" is what you saw in the wireshark trace file, not what VMware was 'telling' you.</p><p>These messages generated because the packets arrive out of order at your workstation.<br />
In <code>tcp.stream eq 0</code> this causes the FIN packet (ip.id==0x3ed5) to arrive before the Close-Notify (ip.id==0x3ed4) at the client which is getting a reset as the socket in your client is already gone. <img src="https://osqa-ask.wireshark.org/upfiles/VMWare_Client.png" alt="alt text" /> However the tcp.stream eq 0 in the 'successful' scenario shows the packets arriving in order but still the Close_Notify gets a RST, so from the VMWare client's perspective there is no real difference.</p><p>Also, in both traces remote MAC address is the same Cisco router so I'm wondering if you really provided two different scenarios in cloudshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '13, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-25070" class="comments-container"><span id="25095"></span><div id="comment-25095" class="comment"><div id="post-25095-score" class="comment-score"></div><div class="comment-text"><p>Thanks Yes!!! Traffic is going through the same Firewall but in successful case Firewall is default gateway of the host and in failed case traffic is going to SVI( default gateway) which is re-routing to the same Firewall using route-map.</p><p>Ir</p></div><div id="comment-25095-info" class="comment-info"><span class="comment-age">(22 Sep '13, 22:59)</span> <span class="comment-user userinfo">imrans</span></div></div></div><div id="comment-tools-25070" class="comment-tools"></div><div class="clear"></div><div id="comment-25070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

