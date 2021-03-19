+++
type = "question"
title = "Zero packets detected - HP Procurve 5400 series &amp; Marvell Yukon  88E8055"
description = '''Hi all Hope someone has come across this before and can help me before I tear my hair out! I have Wireshark set up on a Sony Vaio PCG-4N1M which has a Marvell Yukon 88E8055 NIC and am trying to packet sniff by linking it to a mirror output port on a HP 5400 series switch. I know Wireshark is install...'''
date = "2013-09-23T01:17:00Z"
lastmod = "2013-10-01T01:04:00Z"
weight = 25103
keywords = [ "procurve" ]
aliases = [ "/questions/25103" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Zero packets detected - HP Procurve 5400 series & Marvell Yukon 88E8055](/questions/25103/zero-packets-detected-hp-procurve-5400-series-marvell-yukon-88e8055)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25103-score" class="post-score" title="current number of votes">0</div><span id="post-25103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>Hope someone has come across this before and can help me before I tear my hair out!</p><p>I have Wireshark set up on a Sony Vaio PCG-4N1M which has a Marvell Yukon 88E8055 NIC and am trying to packet sniff by linking it to a mirror output port on a HP 5400 series switch.</p><p>I know Wireshark is installed correctly as I can see the packet count incrementing on the wireless NIC when I view 'Capture Interfaces'.</p><p>However, when I link the Vaio to the mirror port through the wired NIC and a length of ethernet cable I get a zero packet count.</p><p>Below are the instructions I followed. I'm hoping I've made a daft mistake!</p><p>INSTRUCTIONS I FOLLOWED</p><p>The port I am monitoring is untagged on a VLAN called 'Inward'. I ensured the spare port I would be using as the mirror output port matched this configuration.</p><p>I then set up a mirror port on the 5400 series switch as follows:</p><h6 id="section"></h6><p>mirror-port &lt;port&gt;</p><p>where &lt;port&gt; is the port you want to use for the output.</p><p>To select the ports you want to monitor, use the command</p><p>interface ethernet &lt; monitor-list &gt; monitor</p><p>where: &lt; monitor-list &gt; includes port numbers and static trunk names such as a4, c7, b5-b8, and trk1.</p><h6 id="section-1"></h6><p>Using the 'show monitor' command I checked the mirror port configuration is set up as it should be.</p><p>I then connect my monitoring PC (which is a Sony Vaio PCG-4N1M) to the mirror output port using a length of ethernet cable.</p><p>This laptop has a Marvell Yukon 88E8055 NIC so I have made sure I have changed the registry as per the instructions on the Wireshark website. These are as follows:</p><h6 id="section-2"></h6><p>You should add the DWORD SkDisableVlanStrip with value of 1 and the DWORD *PriorityVLANTag (including the star) with value of 0 under the registry key: "HKLM\SYSTEM\CurrentControlSet\Control\Class{4D36E972-E325-11CE-BFC1-08002bE10318}\000" , where 000 is the number of the folder for the Marvel ethernet controller.</p><h6 id="section-3"></h6><p>Finally I have unticked all the settings under the connection properties for the NIC to ensure Wireshark is only capturing traffic from the mirror output port.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-procurve" rel="tag" title="see questions tagged &#39;procurve&#39;">procurve</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '13, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/aed9b121a449090351a0f6a13f3c0151?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TQMan&#39;s gravatar image" /><p><span>TQMan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TQMan has no accepted answers">0%</span></p></div></div><div id="comments-container-25103" class="comments-container"></div><div id="comment-tools-25103" class="comment-tools"></div><div class="clear"></div><div id="comment-25103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25430"></span>

<div id="answer-container-25430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25430-score" class="post-score" title="current number of votes">0</div><span id="post-25430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is the monitor port enabled?</p><p>If you connect the Vaio to a "normal" network port, do you see broadcast traffic in Wireshark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25430" class="comments-container"><span id="25438"></span><div id="comment-25438" class="comment"><div id="post-25438-score" class="comment-score"></div><div class="comment-text"><p>My apologies. I should have replied to this sooner.</p><p>The list of commands I entered into the CLI did not bring back any error message and (from checking through the CLI) all appeared to be set up OK.</p><p>However, when I tried enabling monitoring through the web console (after undoing everything I had done in the CLI) it all worked as it should.</p><p>Bizarre, but I'm happy it worked and Wireshark proved itself invaluable again.</p><p>Many thanks.</p></div><div id="comment-25438-info" class="comment-info"><span class="comment-age">(01 Oct '13, 01:04)</span> <span class="comment-user userinfo">TQMan</span></div></div></div><div id="comment-tools-25430" class="comment-tools"></div><div class="clear"></div><div id="comment-25430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

