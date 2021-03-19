+++
type = "question"
title = "Packets appear twice"
description = '''Hi folks! I have a strange issue. It seems that the GSM packets which I filter out by gsm_map are shown twice, as appears in the below screenshot:  I use the following command from command line to capture the traffic: tcpdump -i any -s0 -w test.cap  Any clue why such behavior could occur? Thanks!'''
date = "2012-04-19T07:47:00Z"
lastmod = "2012-04-19T09:23:00Z"
weight = 10283
keywords = [ "capture", "gui", "gsm", "duplicate" ]
aliases = [ "/questions/10283" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packets appear twice](/questions/10283/packets-appear-twice)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10283-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks!</p><p>I have a strange issue. It seems that the GSM packets which I filter out by <code>gsm_map</code> are shown twice, as appears in the below screenshot: <img src="https://osqa-ask.wireshark.org/upfiles/double_appearance_2.JPG" alt="alt text" /></p><p>I use the following command from command line to capture the traffic:</p><pre><code>tcpdump -i any -s0 -w test.cap</code></pre><p>Any clue why such behavior could occur?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">capture gui gsm duplicate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/aab36e75e2a1b09199da99501429f49e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eugene%20S&#39;s gravatar image" /><p>Eugene S<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eugene S has no accepted answers">0%</span></p></img></div></div><div id="comments-container-10283" class="comments-container"></div><div id="comment-tools-10283" class="comment-tools"></div><div class="clear"></div><div id="comment-10283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10288"></span>

<div id="answer-container-10288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10288-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are capturing of an interface connected to a monitor/span port of a switch you might get packets written to your trace file twice ingress/egress depending on how you have set up your monitoring.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-10288" class="comments-container"><span id="10291"></span><div id="comment-10291" class="comment"><div id="post-10291-score" class="comment-score">1</div><div class="comment-text"><p>...or if you capture on the "any" interface of a Linux-based router and the traffic shows up on multiple physical interfaces.</p></div><div id="comment-10291-info" class="comment-info"><span class="comment-age">(19 Apr '12, 10:16)</span> Gerald Combs ♦♦</div></div><span id="10332"></span><div id="comment-10332" class="comment"><div id="post-10332-score" class="comment-score"></div><div class="comment-text"><p>@Anders and @Gerald Combs, thanks a lot for your comments! However I'm still a novice in this area and I'm not sure I understand your answers completely. Could you please provide a bit more details about what causing this behavior and how to solve this problem. Maybe you can provide some links for further reading.. Thanks again!</p></div><div id="comment-10332-info" class="comment-info"><span class="comment-age">(20 Apr '12, 01:32)</span> Eugene S</div></div></div><div id="comment-tools-10288" class="comment-tools"></div><div class="clear"></div><div id="comment-10288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

