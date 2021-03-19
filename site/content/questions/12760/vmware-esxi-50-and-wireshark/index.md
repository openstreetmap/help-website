+++
type = "question"
title = "VMWare ESXi 5.0 and Wireshark"
description = '''What I&#x27;m trying to do: Use vmnic1 in a Windows 2008 R2 in EXSi 5.0 as a dedicated wireshark port. I need to be able to set a port mirror on my Avaya ERS5650 and have vmnic1 capture this data.  Physical Server = ESXi 5.0 Server with 2 Physical NICs. Physical Data Switch = Avaya ERS5650 ESXi vmnic0 = ...'''
date = "2012-07-16T07:10:00Z"
lastmod = "2012-07-18T17:56:00Z"
weight = 12760
keywords = [ "mirroring", "vmware", "mirror" ]
aliases = [ "/questions/12760" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [VMWare ESXi 5.0 and Wireshark](/questions/12760/vmware-esxi-50-and-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12760-score" class="post-score" title="current number of votes">0</div><span id="post-12760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What I'm trying to do: Use vmnic1 in a Windows 2008 R2 in EXSi 5.0 as a dedicated wireshark port. I need to be able to set a port mirror on my Avaya ERS5650 and have vmnic1 capture this data.<br />
</p><p>Physical Server = ESXi 5.0 Server with 2 Physical NICs.</p><p>Physical Data Switch = Avaya ERS5650</p><p>ESXi vmnic0 = vSwitch0, standard network traffic for all VM's</p><p>ESXi vmnic1 = vSwitch1 set to promiscuous mode, Avaya ERS port 1/10, Use as dedicated port for wireshark, configured as Port Mirror destination on Avaya ERS5650 mirrored port</p><p>When I turn it on, I see very little traffic, I see only LLDP, NDP, no other traffic. What am I missing in the config of VMWare or Wireshark or is this scenario not possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mirroring" rel="tag" title="see questions tagged &#39;mirroring&#39;">mirroring</span> <span class="post-tag tag-link-vmware" rel="tag" title="see questions tagged &#39;vmware&#39;">vmware</span> <span class="post-tag tag-link-mirror" rel="tag" title="see questions tagged &#39;mirror&#39;">mirror</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/6b5b8510760a35baf9eeba434aef618e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="byris&#39;s gravatar image" /><p><span>byris</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="byris has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12760" class="comments-container"><span id="12838"></span><div id="comment-12838" class="comment"><div id="post-12838-score" class="comment-score"></div><div class="comment-text"><p>I am having the same problem with the same setup, except diffrent network equipment (i am using Extreme Switches) is there any resolution for this yet?</p></div><div id="comment-12838-info" class="comment-info"><span class="comment-age">(18 Jul '12, 14:59)</span> <span class="comment-user userinfo">chad_spack</span></div></div></div><div id="comment-tools-12760" class="comment-tools"></div><div class="clear"></div><div id="comment-12760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12768"></span>

<div id="answer-container-12768" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12768-score" class="post-score" title="current number of votes">0</div><span id="post-12768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your setup is a little like on of those crazy machines, but right now I don't see why it shouldn't work. Correct me if I'm wrong:</p><ol><li>You have a Avaya switch that mirrors data to port 1/10.</li><li>connected to that port is vmnic1 of the ESXi</li><li>vmnic1 is connected to vSwitch1, with the whole vSwitch set to promiscuous mode</li><li>on the virtual side the Windows 2k8r2 machine is running, with Wireshark capturing data</li></ol><p>It basically means that your mirror port is sending data to vSwitch1 which doesn't have a valid target and floods it anyway - and even if it wouldn't, it would because it is in promiscuous mode. So yes, you should see traffic from the mirror port.</p><p>Maybe - and I would have to verify this - the vSwitch is "intelligent" enough to know that the destinations MACs are invalid since the ESXi has an inventory of existing virtual MACs and discards the frames that do not match any of them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jul '12, 08:48</strong> </span></p></div></div><div id="comments-container-12768" class="comments-container"><span id="12771"></span><div id="comment-12771" class="comment"><div id="post-12771-score" class="comment-score"></div><div class="comment-text"><p>That's Exactly what I'm trying to do, but I'm just not seeing the intended traffic, basically no ICMP, TCP, UDP etc. but I do see LLDP &amp; NDP</p><p>I've already tested the mirroring functionality on a standalone PC plugged into Avaya Switch Port 1/10 and I see the expected results. But when 1/10 is plugged into a vmnic1 I do not see the intended traffic.</p><p>Once again I already have vSwitch1 &amp; the VMXNet3 Adapter set to promiscuous mode.</p><p>I wonder if I should set it to adapter type E1000 or VMXNet2 to see if that would make a difference.</p></div><div id="comment-12771-info" class="comment-info"><span class="comment-age">(16 Jul '12, 09:42)</span> <span class="comment-user userinfo">byris</span></div></div><span id="12772"></span><div id="comment-12772" class="comment"><div id="post-12772-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment to keep the flow going.</p><p>You can try to use E1000 or VMXNet2 but I doubt it will help. I guess the VMkernel is dropping the frames as undeliverable since it knows it doesn't have the destination MACs anywhere. Unfortunately I cannot verify this behaviour at the moment since I can't access a test environment right now.</p></div><div id="comment-12772-info" class="comment-info"><span class="comment-age">(16 Jul '12, 09:48)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="12773"></span><div id="comment-12773" class="comment"><div id="post-12773-score" class="comment-score"></div><div class="comment-text"><p>Should I make the MAC address of the vmnic1 = physical eth1?</p></div><div id="comment-12773-info" class="comment-info"><span class="comment-age">(16 Jul '12, 10:12)</span> <span class="comment-user userinfo">byris</span></div></div><span id="12774"></span><div id="comment-12774" class="comment"><div id="post-12774-score" class="comment-score"></div><div class="comment-text"><p>The mirrored frames will have neither the destination MAC of the physical eth1 nor of a virtual nic, so I don't think it will help. But as always, you can still try...</p></div><div id="comment-12774-info" class="comment-info"><span class="comment-age">(16 Jul '12, 10:55)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-12768" class="comment-tools"></div><div class="clear"></div><div id="comment-12768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12839"></span>

<div id="answer-container-12839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12839-score" class="post-score" title="current number of votes">0</div><span id="post-12839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Found the solution it is in windows 2008 r2 driver - go to the interface &gt; Advanced &gt; Priority &amp; Vlan &gt; Disable Priority &amp; Vlan. Then try your capture again. If that don't work make sure your vswitch you are using security is set to allow promiscuous mode</p><p>Thanks to these sites for their help :)</p><p>Vmware KB <a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1002934">http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1002934</a></p><p>Windows Settings (at bottom of article) <a href="http://community.spiceworks.com/topic/128883-vsphere-promiscuous-mode-only-receiving-packets-one-way-from-network-switch">http://community.spiceworks.com/topic/128883-vsphere-promiscuous-mode-only-receiving-packets-one-way-from-network-switch</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '12, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/edf4cff68dcf019bb024a3c430420ed1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chad_spack&#39;s gravatar image" /><p><span>chad_spack</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chad_spack has no accepted answers">0%</span></p></div></div><div id="comments-container-12839" class="comments-container"></div><div id="comment-tools-12839" class="comment-tools"></div><div class="clear"></div><div id="comment-12839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

