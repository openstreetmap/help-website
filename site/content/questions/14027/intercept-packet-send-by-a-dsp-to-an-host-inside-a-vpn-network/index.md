+++
type = "question"
title = "intercept packet send by a DSP to an host inside a VPN network"
description = '''Hi all, i&#x27;m new... i&#x27;m facing this problem for a while and i&#x27;m a bit out of ideas. Basically i&#x27;d like to intercept the packet send by a remote DSP/DSPs to a host directly connected to them via ssh. I can connect to a third host via VPN that communicate with those two parts. Please somebody help me :...'''
date = "2012-09-04T03:24:00Z"
lastmod = "2012-09-04T14:29:00Z"
weight = 14027
keywords = [ "host", "intercept", "ssh", "dsp", "wireshark" ]
aliases = [ "/questions/14027" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [intercept packet send by a DSP to an host inside a VPN network](/questions/14027/intercept-packet-send-by-a-dsp-to-an-host-inside-a-vpn-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14027-score" class="post-score" title="current number of votes">0</div><span id="post-14027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, i'm new... i'm facing this problem for a while and i'm a bit out of ideas. Basically i'd like to intercept the packet send by a remote DSP/DSPs to a host directly connected to them via ssh. I can connect to a third host via VPN that communicate with those two parts. Please somebody help me :)...</p><p>Thanks to all,</p><p>Stefano</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-host" rel="tag" title="see questions tagged &#39;host&#39;">host</span> <span class="post-tag tag-link-intercept" rel="tag" title="see questions tagged &#39;intercept&#39;">intercept</span> <span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span> <span class="post-tag tag-link-dsp" rel="tag" title="see questions tagged &#39;dsp&#39;">dsp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '12, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/078f85e502ffc0dae466cfc46ce25955?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stefano_r&#39;s gravatar image" /><p><span>stefano_r</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stefano_r has no accepted answers">0%</span></p></div></div><div id="comments-container-14027" class="comments-container"></div><div id="comment-tools-14027" class="comment-tools"></div><div class="clear"></div><div id="comment-14027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14032"></span>

<div id="answer-container-14032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14032-score" class="post-score" title="current number of votes">0</div><span id="post-14032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>DSP/ssh/vpn? I'm afraid, but that's all a bit vague. Can you please post some more information about your network infrastructure? Something like this:</p><blockquote><p><code>C1[DSP] -- C2[ssh] --- VPN Tunnel -- C3</code><br />
</p></blockquote><p>Some questions:</p><ul><li>What is "remote DSP"?</li><li>What traffic do you want to capture (ssh, DSP traffic,etc.)?</li><li>Where do you want to capture: C1, C2, C3 ??</li><li>What is the OS of the involved computers (is Wireshark available)?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14032" class="comments-container"><span id="14035"></span><div id="comment-14035" class="comment"><div id="post-14035-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>sorry for my poor explanation, yes exactly like this! Well with remote DSP i mean that i'm working in Italy while the DSPs are located in Germany, along with the what you marked as C2 host. Iìd like to be able to analyze the DSP traffic between C1 and C2......regarding the last question well...i'm not aware of the OS in those PC right now, the same for Wireshark.</p><p>Br,</p><p>Stefano</p></div><div id="comment-14035-info" class="comment-info"><span class="comment-age">(04 Sep '12, 08:43)</span> <span class="comment-user userinfo">stefano_r</span></div></div><span id="14038"></span><div id="comment-14038" class="comment"><div id="post-14038-score" class="comment-score"></div><div class="comment-text"><p>O.K. so, the "DSP" traffic (did you explain what that is?) gets tunneled through ssh. Right?</p><p>If so, you will only be able to capture ssh traffic on C1 and C2, as Wireshark will only see the network packets leaving or entering the machine. That does not help, as ssh is encrypted and Wireshark cannot decrypt it.</p><p>What happens to the data after it leaves the ssh tunnel? Is it forwarded to another system, written to disk, processed by another process?</p><p>Regarding the OS. If the OS does not support Wireshark (that's why I asked), your out of business, at least in terms of using Wireshark. ;-)</p></div><div id="comment-14038-info" class="comment-info"><span class="comment-age">(04 Sep '12, 14:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-14032" class="comment-tools"></div><div class="clear"></div><div id="comment-14032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

