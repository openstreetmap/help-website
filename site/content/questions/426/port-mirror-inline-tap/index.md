+++
type = "question"
title = "Port Mirror Inline Tap"
description = '''Need a device that acts similar to port mirror / port spanning of a layer 2 switch. One I can carry to the end point unplug the device and use this hardware to give me one input for the cable from the network and two connectors one for the intended device (Telephone system) and the second port to pl...'''
date = "2010-10-05T15:32:00Z"
lastmod = "2010-10-06T06:09:00Z"
weight = 426
keywords = [ "port", "mirror" ]
aliases = [ "/questions/426" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Port Mirror Inline Tap](/questions/426/port-mirror-inline-tap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-426-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Need a device that acts similar to port mirror / port spanning of a layer 2 switch. One I can carry to the end point unplug the device and use this hardware to give me one input for the cable from the network and two connectors one for the intended device (Telephone system) and the second port to plug in my computer running wireshark. I found one for $ 1200. A little too fancy. Just need to tap in and watch the traffic passing that point.</p><p>Thanks, Gary</p></div><div id="question-tags" class="tags-container tags">port mirror</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '10, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/79e2938a11fa583058e06dab30eca850?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GaryC&#39;s gravatar image" /><p>GaryC<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GaryC has no accepted answers">0%</span></p></div></div><div id="comments-container-426" class="comments-container"></div><div id="comment-tools-426" class="comment-tools"></div><div class="clear"></div><div id="comment-426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="427"></span>

<div id="answer-container-427" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-427-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you're looking for a full-duplex tap (unless you're on a half duplex network, then you just need a hub)...</p><p>Yup - full-duplex taps can be pricey. NetOptics makes some (check out their technical docs - they have some good ones showing what aggregating/non-aggregating taps can do). Also see Critical Networks for taps.</p><p>If you are a hardware guru (I can't even crimp cables well so this is outta my league), check out http://hackaday.com/2008/09/14/passive-networking-tap/. For super cheap you can make a non-aggregating tap.</p><p>Oh - silly me - there are some taps on eBay too - http://shop.ebay.com/?_from=R40&amp;_trksid=p3907.m570.l1313&amp;_nkw=network+tap&amp;_sacat=See-All-Categories.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '10, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-427" class="comments-container"><span id="443"></span><div id="comment-443" class="comment"><div id="post-443-score" class="comment-score"></div><div class="comment-text"><p>That should work. We are breaking the line between the Phone system and the SIP trunk carrier to isolate registration faults as carrier or phone system. In other words who is not working. Thanks! Gary</p></div><div id="comment-443-info" class="comment-info"><span class="comment-age">(06 Oct '10, 13:18)</span> GaryC</div></div></div><div id="comment-tools-427" class="comment-tools"></div><div class="clear"></div><div id="comment-427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="428"></span>

<div id="answer-container-428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-428-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at <a href="http://www.dual-comm.com/">Dual-Comm</a><br />
Betty DuBois wrote <a href="http://www.lovemytool.com/blog/2010/04/review-of-dualcomm-5-port-pass-through-port-mirroring-switch-by-betty-dubois.html">an article</a> about it</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '10, 21:05</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div></div><div id="comments-container-428" class="comments-container"><span id="429"></span><div id="comment-429" class="comment"><div id="post-429-score" class="comment-score"></div><div class="comment-text"><p>Yes, these Dual-Comm boxes are great.</p></div><div id="comment-429-info" class="comment-info"><span class="comment-age">(05 Oct '10, 23:15)</span> Jaap ♦</div></div><span id="436"></span><div id="comment-436" class="comment"><div id="post-436-score" class="comment-score"></div><div class="comment-text"><p>Best thing is that they are USB powered. I carry one of them with me at all times, and can capture client workstations without the hassle of looking for a power socket since its powered through my laptop that is doing the capture. Very convenient.</p></div><div id="comment-436-info" class="comment-info"><span class="comment-age">(06 Oct '10, 06:47)</span> Jasper ♦♦</div></div></div><div id="comment-tools-428" class="comment-tools"></div><div class="clear"></div><div id="comment-428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="435"></span>

<div id="answer-container-435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-435-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are a poor man like myself and are on a low budget but want to do high-tech stuff try out the Netgear GS105E (make sure you look at the E model). $59 at Amazon, 5 Gig interfaces, 4 Gig throughput and while it does not have a traditional Web interface for configuration it does come with a little piece of software that you can carry with you that allows you to set an ip,qos and a bunch of other stuff. But most importantly it will let you span multiple ports. It is the size of a pack of cigarettes and work GREAT! If you can't afford a tap it is a GREAT alternative until you can. It's also great for studying for your wireshark cert :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '10, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/a6c5ad97e2cb05c2855f6e4cc79f9d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blacknight&#39;s gravatar image" /><p>blacknight<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blacknight has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Oct '10, 06:37</p></div></div><div id="comments-container-435" class="comments-container"></div><div id="comment-tools-435" class="comment-tools"></div><div class="clear"></div><div id="comment-435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

