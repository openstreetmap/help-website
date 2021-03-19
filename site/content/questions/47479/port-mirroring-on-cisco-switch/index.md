+++
type = "question"
title = "Port Mirroring on cisco switch"
description = '''If I am configuring SPAN on cisco switch and the source port is hard coded to 1000/FULL. Do I have to configure the destination port(port where I am connecting my laptop running wireshark) to 1000/FULL or I can leave it to Auto/auto. Please confirm. Thanks..'''
date = "2015-11-10T11:59:00Z"
lastmod = "2015-11-10T13:29:00Z"
weight = 47479
keywords = [ "on", "switch", "cisco", "port", "mirroring" ]
aliases = [ "/questions/47479" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Port Mirroring on cisco switch](/questions/47479/port-mirroring-on-cisco-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47479-score" class="post-score" title="current number of votes">0</div><span id="post-47479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I am configuring SPAN on cisco switch and the source port is hard coded to 1000/FULL. Do I have to configure the destination port(port where I am connecting my laptop running wireshark) to 1000/FULL or I can leave it to Auto/auto. Please confirm.</p><p>Thanks..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-on" rel="tag" title="see questions tagged &#39;on&#39;">on</span> <span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-mirroring" rel="tag" title="see questions tagged &#39;mirroring&#39;">mirroring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '15, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/c05e904ef1440a84c484a2afc923b8ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetninja101&#39;s gravatar image" /><p><span>packetninja101</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetninja101 has no accepted answers">0%</span></p></div></div><div id="comments-container-47479" class="comments-container"></div><div id="comment-tools-47479" class="comment-tools"></div><div class="clear"></div><div id="comment-47479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="47481"></span>

<div id="answer-container-47481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47481-score" class="post-score" title="current number of votes">0</div><span id="post-47481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>If I am configuring SPAN on cisco switch and the source port is hard coded to 1000/FULL. Do I have to configure the destination port(port where I am connecting my laptop running wireshark) to 1000/FULL</code></p><p>Depends on what you mean with source port:<br />
1. If you mean with the <strong>source port</strong> the <strong>source of the span definition</strong>, then you can leave it at <strong>Auto</strong> if your <strong>Laptop</strong> is at <strong>Auto</strong>, too. And both devices should support <strong>1000 MBit/s</strong>. (<em>This happens mostly if want to monitor a FX link on a TX Port</em>)<br />
<br />
2. If you mean with <strong>source port</strong>: The <strong>switch port</strong> your <strong>laptop is connected directly</strong>, then you should configure the switch port and the laptop in the same way. (<em>Hint: If it is a <strong>TX</strong> Link and you want to use it with <strong>1000 MBit/s</strong>, then the mandatory/recommended setup by Cisco is <strong>Speed: Auto,</strong> <strong>Duplex</strong>: <strong>Auto</strong></em>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '15, 13:37</strong> </span></p></div></div><div id="comments-container-47481" class="comments-container"></div><div id="comment-tools-47481" class="comment-tools"></div><div class="clear"></div><div id="comment-47481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47482"></span>

<div id="answer-container-47482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47482-score" class="post-score" title="current number of votes">0</div><span id="post-47482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Do I have to configure the destination port(port where I am connecting my laptop running wireshark) to 1000/FULL or I can leave it to Auto/auto.</p></blockquote><p><strong>Solution:</strong> The best way would be to leave both at Auto-Negotiation and let them negotiate or set <strong>both</strong> at 1000 Full.</p><p>Sometimes an "asymmetric" combination works, sometimes it does not. Most of the time you will get a Duplex mismatch. It really depends on your switch and your Laptop.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '15, 12:32</strong> </span></p></div></div><div id="comments-container-47482" class="comments-container"></div><div id="comment-tools-47482" class="comment-tools"></div><div class="clear"></div><div id="comment-47482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47484"></span>

<div id="answer-container-47484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47484-score" class="post-score" title="current number of votes">0</div><span id="post-47484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1) There is no relationship between how the link speed and duplex is obtained at the monitored port(s) and at the SPAN port.</p><p>2) when talking about a single port, you may have actually three types of setting:</p><ul><li>fixed with no negotiation (e.g. 1000, full)</li><li>fixed with negotiation permitted (e.g. auto, auto but only a single negotiable value 1000, full),</li><li>negotiation permitted with a choice of several permitted options (e.g. 10/100/1000, half/full).</li></ul><p>Here what Kurt wrote applies - depending on the particular equipment types on the two ends of a cable, some "asymmetric" combinations may work.</p><p>3) the most important point is that the sum of traffic on the monitored port(s) must not exceed the unidirectional speed of the SPAN port. I.e. if you monitor a single 1000/full port, the sum of traffic volumes "in" and "out" may be up to 2 Gbit/s, so if it really exceeds 1 Gbit/s for an extended period of time, it won't fit to the SPAN port and you won't see part of it in your Wireshark capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '15, 13:47</strong> </span></p></div></div><div id="comments-container-47484" class="comments-container"></div><div id="comment-tools-47484" class="comment-tools"></div><div class="clear"></div><div id="comment-47484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

