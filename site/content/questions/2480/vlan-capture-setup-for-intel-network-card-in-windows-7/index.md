+++
type = "question"
title = "Vlan capture setup for Intel network card in windows 7"
description = '''Hi guys, i&#x27;m trying to define VLAN tagging in windows7 for Intel(R) 82566DM Gigabit Network Connection. i tried the &quot;windows xp configuration like:  find out the network card brand. open registry editor (start &amp;gt; run &amp;gt; regedit or regedt32 ) find the following location: etc... but didn&#x27;t work fo...'''
date = "2011-02-22T07:16:00Z"
lastmod = "2011-02-23T11:20:00Z"
weight = 2480
keywords = [ "capture", "windows7", "vlan" ]
aliases = [ "/questions/2480" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Vlan capture setup for Intel network card in windows 7](/questions/2480/vlan-capture-setup-for-intel-network-card-in-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2480-score" class="post-score" title="current number of votes">0</div><span id="post-2480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, i'm trying to define VLAN tagging in windows7 for Intel(R) 82566DM Gigabit Network Connection. i tried the "windows xp configuration like: find out the network card brand. open registry editor (start &gt; run &gt; regedit or regedt32 ) find the following location: etc... but didn't work for me in windows7, so Wireshark app don't show VLAN Tagging when "Capture".</p><p>there is any different\special settings for windows7?</p><p>please advice.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '11, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/da27acbb8d0d02e6e47777314ffb52ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mishiago&#39;s gravatar image" /><p><span>mishiago</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mishiago has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Mar '12, 21:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-2480" class="comments-container"></div><div id="comment-tools-2480" class="comment-tools"></div><div class="clear"></div><div id="comment-2480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2481"></span>

<div id="answer-container-2481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2481-score" class="post-score" title="current number of votes">0</div><span id="post-2481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure the traffic contains VLAN tags? On most switches you have to configure the spanport to replicate the vlan tags. Depending on the brand and model you need to specify it when configuring the spanport, configure the destination port as a vlan tagging port, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '11, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2481" class="comments-container"></div><div id="comment-tools-2481" class="comment-tools"></div><div class="clear"></div><div id="comment-2481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2494"></span>

<div id="answer-container-2494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2494-score" class="post-score" title="current number of votes">0</div><span id="post-2494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are trying to capture the VLAN tags on a Cisco 802.1Q trunk port, then use this syntax:-</p><p>monitor session x source interface fa0/y</p><p>monitor session x destination interface fa0/z encpssulation dot1q</p><p>You may also need a registry edit to prevent the NIC stripping the VLAN header. I have another post ongoing on the same subject. You probably need to add a DWORD like MonitorMode or MonitoModeEnabled (I am not familar with your card, but one of these works for other Intel NICs).</p><p>Also look for a "Priority &amp; VLAN" option in the NICs configuration (Advanced tab). Set this to "Priority &amp; VLAN Enabled".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '11, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p><span>KeithFrench</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-2494" class="comments-container"><span id="2495"></span><div id="comment-2495" class="comment"><div id="post-2495-score" class="comment-score"></div><div class="comment-text"><p>That depends on the Cisco model you're talking about... on a 65xx you need to put the destination port into trunk mode as it does not have the "... encapsulation dot1q" option when defining a spanport</p></div><div id="comment-2495-info" class="comment-info"><span class="comment-age">(22 Feb '11, 11:33)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="2503"></span><div id="comment-2503" class="comment"><div id="post-2503-score" class="comment-score"></div><div class="comment-text"><p>Yes I agree &amp; if it is running CatOS......</p></div><div id="comment-2503-info" class="comment-info"><span class="comment-age">(22 Feb '11, 14:11)</span> <span class="comment-user userinfo">KeithFrench</span></div></div><span id="2504"></span><div id="comment-2504" class="comment"><div id="post-2504-score" class="comment-score"></div><div class="comment-text"><p>I wish that was true, IOS based 6500 also requires it: See <a href="http://www.cisco.com/en/US/docs/switches/lan/catalyst6500/ios/12.2SX/configuration/guide/span.html#wp1118844">http://www.cisco.com/en/US/docs/switches/lan/catalyst6500/ios/12.2SX/configuration/guide/span.html#wp1118844</a></p></div><div id="comment-2504-info" class="comment-info"><span class="comment-age">(22 Feb '11, 14:20)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="2508"></span><div id="comment-2508" class="comment"><div id="post-2508-score" class="comment-score"></div><div class="comment-text"><p>I just meant that CatOS is totally different to IOS based 65xx cats.</p></div><div id="comment-2508-info" class="comment-info"><span class="comment-age">(22 Feb '11, 14:28)</span> <span class="comment-user userinfo">KeithFrench</span></div></div><span id="2509"></span><div id="comment-2509" class="comment"><div id="post-2509-score" class="comment-score"></div><div class="comment-text"><p>Oops... I seem to have misinterpreted the "&amp;" :-)</p></div><div id="comment-2509-info" class="comment-info"><span class="comment-age">(22 Feb '11, 14:30)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="2513"></span><div id="comment-2513" class="comment not_top_scorer"><div id="post-2513-score" class="comment-score"></div><div class="comment-text"><p>it's seems like the configuration settings same as windows xp. i tried to define like the instruction below but unsuccessfully.</p><p>Note: In windows xp it's working excellent and obviously VLAN tagging is enabled.</p><p>please advice.</p></div><div id="comment-2513-info" class="comment-info"><span class="comment-age">(23 Feb '11, 01:43)</span> <span class="comment-user userinfo">mishiago</span></div></div></div><div id="comment-tools-2494" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-2494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2526"></span>

<div id="answer-container-2526" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2526-score" class="post-score" title="current number of votes">0</div><span id="post-2526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have a different Intel NIC in my Windows 7 laptop &amp; with the registry edits it works fine. Have you tried searching Intels KnowledgeBase?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '11, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p><span>KeithFrench</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-2526" class="comments-container"></div><div id="comment-tools-2526" class="comment-tools"></div><div class="clear"></div><div id="comment-2526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

