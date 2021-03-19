+++
type = "question"
title = "window7 automatically remove the outer vlan tag?"
description = '''JDSU traffic generator is used to generate traffic(outer vlan 500,inner vlan 50) to pc(window7) and the packet captured in wireshark is shown: http://cloudshark.org/captures/d302f8040a52 JDSU traffic generator is used to generate traffic(outer vlan 500,inner vlan 50) to JDSU-MTS5800 and the packet c...'''
date = "2012-11-12T22:22:00Z"
lastmod = "2015-06-29T21:01:00Z"
weight = 15842
keywords = [ "vlan", "outer", "tag" ]
aliases = [ "/questions/15842" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [window7 automatically remove the outer vlan tag?](/questions/15842/window7-automatically-remove-the-outer-vlan-tag)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15842-score" class="post-score" title="current number of votes">0</div><span id="post-15842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>JDSU traffic generator is used to generate traffic(outer vlan 500,inner vlan 50) to pc(window7) and the packet captured in wireshark is shown: <a href="http://cloudshark.org/captures/d302f8040a52">http://cloudshark.org/captures/d302f8040a52</a></p><p>JDSU traffic generator is used to generate traffic(outer vlan 500,inner vlan 50) to JDSU-MTS5800 and the packet captured in wireshark inside JDSU-MTS5800 is shown: <a href="http://cloudshark.org/captures/7e88043f2e0d">http://cloudshark.org/captures/7e88043f2e0d</a></p><p>The traffic generator is the same and with the same configuration. However, the packet capture result is different. One interesting is that, the value for the outer tag, located at 0x0C to 0x0F, which is 81 00 01 f4 seems to be automatically removed at window7, pc environment, and the inner tag 81 00 00 32 exist in both case but in different location.</p><p>Thus, I wonder is it window7, pc environment,automatically remove the outer tag?</p><p>more information about MTS5800: <a href="http://www.jdsu.com/en-us/Test-and-Measurement/Products/a-z-product-list/Pages/mts-5800-handheld-network-tester.aspx">http://www.jdsu.com/en-us/Test-and-Measurement/Products/a-z-product-list/Pages/mts-5800-handheld-network-tester.aspx</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-outer" rel="tag" title="see questions tagged &#39;outer&#39;">outer</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '12, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/8ab2bc114b3fb950f50b5c340c4e580e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bennettfan&#39;s gravatar image" /><p><span>bennettfan</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bennettfan has no accepted answers">0%</span></p></div></div><div id="comments-container-15842" class="comments-container"><span id="43693"></span><div id="comment-43693" class="comment"><div id="post-43693-score" class="comment-score"></div><div class="comment-text"><p>I experienced the same as bennettfan as above. I used 2950 Cisco switch to do the monitor for wireshark with the same NIC Intel(R) 82567LM Gigabit Network Connection. I also followed your instruction in adding "MonitorEnableModed" in Regedit, but VLAN and COS still not appear in wireshark logfile. Do you have any suggestion?</p></div><div id="comment-43693-info" class="comment-info"><span class="comment-age">(29 Jun '15, 18:43)</span> <span class="comment-user userinfo">Hieuro</span></div></div></div><div id="comment-tools-15842" class="comment-tools"></div><div class="clear"></div><div id="comment-15842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15845"></span>

<div id="answer-container-15845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15845-score" class="post-score" title="current number of votes">1</div><span id="post-15845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Thus, I wonder is it window7, pc environment,automatically remove the outer tag?</p></blockquote><p>It's not windows itself, as there is no VLAN tag functionality in the Windows 7 kernel. But the driver of your NIC may (or may not) remove/modify the VLAN tag. So, what is the NIC in your capture PC?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-15845" class="comments-container"><span id="15847"></span><div id="comment-15847" class="comment"><div id="post-15847-score" class="comment-score"></div><div class="comment-text"><p>Intel(R) 82567LM Gigabit Network Connection</p><p>Can I view the vlan tag without being removed/modified by the NIC driver?</p></div><div id="comment-15847-info" class="comment-info"><span class="comment-age">(13 Nov '12, 00:07)</span> <span class="comment-user userinfo">bennettfan</span></div></div><span id="15855"></span><div id="comment-15855" class="comment"><div id="post-15855-score" class="comment-score"></div><div class="comment-text"><p>please check my answer to the following question.</p><blockquote><p><code>http://ask.wireshark.org/questions/15524/vlan-tagging-intel-82579lm-and-wireshark-183</code><br />
</p></blockquote><p>Your driver should have the parameter MonitorMode (or MonitorModeEnabled) as well.</p></div><div id="comment-15855-info" class="comment-info"><span class="comment-age">(13 Nov '12, 02:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15950"></span><div id="comment-15950" class="comment"><div id="post-15950-score" class="comment-score"></div><div class="comment-text"><p>i have already enable before asking the question. Any other suggestion?</p></div><div id="comment-15950-info" class="comment-info"><span class="comment-age">(15 Nov '12, 17:47)</span> <span class="comment-user userinfo">bennettfan</span></div></div><span id="15952"></span><div id="comment-15952" class="comment"><div id="post-15952-score" class="comment-score"></div><div class="comment-text"><p>Do you transmit the packet over a switch? If so, the switch can also remove the outer tag, depending on its configuration.</p></div><div id="comment-15952-info" class="comment-info"><span class="comment-age">(15 Nov '12, 23:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15845" class="comment-tools"></div><div class="clear"></div><div id="comment-15845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43695"></span>

<div id="answer-container-43695" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43695-score" class="post-score" title="current number of votes">0</div><span id="post-43695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Regarding Cisco switches, the following commands must be entered in global configuration mode:</p><p>Switch&gt; en</p><p>Switch# config t</p><p>Switch(config)# monitor session 1 source int gi1/0/1</p><p>Switch(config)# monitor session 1 destination int gi1/0/16 encapsulation dot1q</p><p>This will copy all the traffic from port 1 to port 16 while keeping the VLAN tag on the frame. You do NOT need to set-up the destination port (16 in this example) as a trunk with 802.1q encapsulation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '15, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span> </br></p></div></div><div id="comments-container-43695" class="comments-container"><span id="43698"></span><div id="comment-43698" class="comment"><div id="post-43698-score" class="comment-score"></div><div class="comment-text"><p>Thanks Amato for your suggestion. I've captured successfully following your instruction!</p></div><div id="comment-43698-info" class="comment-info"><span class="comment-age">(29 Jun '15, 21:01)</span> <span class="comment-user userinfo">Hieuro</span></div></div></div><div id="comment-tools-43695" class="comment-tools"></div><div class="clear"></div><div id="comment-43695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

