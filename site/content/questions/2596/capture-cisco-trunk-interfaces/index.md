+++
type = "question"
title = "Capture cisco trunk interfaces"
description = '''Hi all, I really need help with this one. I have to capture traffic betwwen trunked cisco ports (dot1Q). I have a switch in the middle with monitor session command to mirror the physical interface. monitor session 2 source interface GiX/XX monitor session 2 destination interface GY/YY monitor sessio...'''
date = "2011-03-01T03:12:00Z"
lastmod = "2011-03-01T04:12:00Z"
weight = 2596
keywords = [ "capture", "interfaces", "cisco", "trunk" ]
aliases = [ "/questions/2596" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture cisco trunk interfaces](/questions/2596/capture-cisco-trunk-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2596-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I really need help with this one. I have to capture traffic betwwen trunked cisco ports (dot1Q). I have a switch in the middle with monitor session command to mirror the physical interface. monitor session 2 source interface GiX/XX monitor session 2 destination interface GY/YY monitor session 2 filter packet-type good rx</p><p>If I ping a machine on the remote lan i only get the requests but not the replays (But the echo ping is responded)</p><p>If I ping the remote interface from the local interface no echo request and reply is recorded (but it also pings)</p><p>the cisco commands are:</p><p>Anyone knows why? Wireshark handles dot1Q? Thanks</p></div><div id="question-tags" class="tags-container tags">capture interfaces cisco trunk</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '11, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/eb4a2b31e624b49f2e99e318de19f300?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zeca_neca&#39;s gravatar image" /><p>zeca_neca<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zeca_neca has no accepted answers">0%</span></p></div></div><div id="comments-container-2596" class="comments-container"></div><div id="comment-tools-2596" class="comment-tools"></div><div class="clear"></div><div id="comment-2596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2597"></span>

<div id="answer-container-2597" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2597-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture vlan tagged frames, you need to make sure that:</p><ol><li>The NIC in the capturing device does not strip the vlan tags (see: <a href="http://wiki.wireshark.org/CaptureSetup/VLAN">http://wiki.wireshark.org/CaptureSetup/VLAN</a></li><li>The mirrored traffic has vlag tags. This is dependent on the switch brand and model</li></ol><p>You are using a cisco switch with IOS. However, you haven't said what model. Different models need different configuration of the monitor session en span port. If you are using a 2950/3560/3750, you need to use "monitor session X destination interface GiX/XX encapsulation dot1q" to make the switch copy the vlan tags to the output port. On a 65XX switch you need to configure the destination port to also be a trunk port and make sure the vlan you are interested in are in the allowed list.</p><p>And yes, wireshark handles 802.1Q vlan tagged frames :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '11, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2597" class="comments-container"><span id="2598"></span><div id="comment-2598" class="comment"><div id="post-2598-score" class="comment-score"></div><div class="comment-text"><p>IT's a WS-C4503-E thanks</p></div><div id="comment-2598-info" class="comment-info"><span class="comment-age">(01 Mar '11, 04:15)</span> zeca_neca</div></div><span id="2609"></span><div id="comment-2609" class="comment"><div id="post-2609-score" class="comment-score"></div><div class="comment-text"><p>I changed to a older PC and it worked.... thanks a lot</p><p>for me it's a closed matter</p></div><div id="comment-2609-info" class="comment-info"><span class="comment-age">(01 Mar '11, 07:56)</span> zeca_neca</div></div><span id="2619"></span><div id="comment-2619" class="comment"><div id="post-2619-score" class="comment-score"></div><div class="comment-text"><p>(converted your answer to a comment to adhere to the nature of this Q&amp;A site, please see the FAQ)</p><p>If your question has been answered, please "accept" the answer by clicking on the checkmark below the thumps-down. That way, the question will not be listed under the "unanswered" category anymore.</p></div><div id="comment-2619-info" class="comment-info"><span class="comment-age">(01 Mar '11, 14:05)</span> SYN-bit ♦♦</div></div><span id="2624"></span><div id="comment-2624" class="comment"><div id="post-2624-score" class="comment-score"></div><div class="comment-text"><p>If running the same version of Wireshark on an older PC made a difference, the reason is probably that the network adapter, or driver, on the newer PC either can't handle capturing raw VLAN tagged frames (or frames on a different VLAN) or doesn't do so by default, and the adapter or driver on the older PC handles them by default. See <a href="http://wiki.wireshark.org/CaptureSetup/VLAN">the CaptureSetup/VLAN page on the Wireshark Wiki</a> for more information on this.</p></div><div id="comment-2624-info" class="comment-info"><span class="comment-age">(01 Mar '11, 14:29)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-2597" class="comment-tools"></div><div class="clear"></div><div id="comment-2597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

