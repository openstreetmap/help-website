+++
type = "question"
title = "using wireshark with rv042g gateway with SNMP for moniting"
description = '''I have the Cisco RV042G router/gateway that has SNMP built into it. Is there a way I can use wireshark with the built in SNMP(rv042g) to monitor my entire network ? If so, how ? Thanks !'''
date = "2014-08-16T23:39:00Z"
lastmod = "2014-08-17T04:11:00Z"
weight = 35517
keywords = [ "snmpwireshark" ]
aliases = [ "/questions/35517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using wireshark with rv042g gateway with SNMP for moniting](/questions/35517/using-wireshark-with-rv042g-gateway-with-snmp-for-moniting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35517-score" class="post-score" title="current number of votes">0</div><span id="post-35517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the Cisco RV042G router/gateway that has SNMP built into it. Is there a way I can use wireshark with the built in SNMP(rv042g) to monitor my entire network ? If so, how ?</p><p>Thanks !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmpwireshark" rel="tag" title="see questions tagged &#39;snmpwireshark&#39;">snmpwireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '14, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/8062a0be34441ccf6103cfd4955d6ae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elochtefeld38&#39;s gravatar image" /><p><span>elochtefeld38</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elochtefeld38 has no accepted answers">0%</span></p></div></div><div id="comments-container-35517" class="comments-container"></div><div id="comment-tools-35517" class="comment-tools"></div><div class="clear"></div><div id="comment-35517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35518"></span>

<div id="answer-container-35518" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35518-score" class="post-score" title="current number of votes">0</div><span id="post-35518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a packet analyser and can dissect snmp traffic but doesn't really provide any useful tools for network monitoring. You would still need an application to generate the snmp traffic by querying your router and as that is likely to be a network monitoring application, that is probably the best option for you.</p><p>Have a look at applications such as Nagios and Zenoss.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '14, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35518" class="comments-container"></div><div id="comment-tools-35518" class="comment-tools"></div><div class="clear"></div><div id="comment-35518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

