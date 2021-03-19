+++
type = "question"
title = "Testing connectivity to Websites"
description = '''Hi, I would like to be able to monitor activity to a few different websites. Never used Wireshark before. We are having trouble accessing a few websites and wanted to be able to determine if our issues are on the local WiFi side or the Websites themselves. Very erratic behavior from the sites. Somet...'''
date = "2016-01-22T07:14:00Z"
lastmod = "2016-01-22T07:42:00Z"
weight = 49456
keywords = [ "websites" ]
aliases = [ "/questions/49456" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Testing connectivity to Websites](/questions/49456/testing-connectivity-to-websites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49456-score" class="post-score" title="current number of votes">0</div><span id="post-49456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to be able to monitor activity to a few different websites. Never used Wireshark before. We are having trouble accessing a few websites and wanted to be able to determine if our issues are on the local WiFi side or the Websites themselves. Very erratic behavior from the sites. Sometimes they work fine and other times they don't respond. Any suggestions?</p><p>Thanks, Jason</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-websites" rel="tag" title="see questions tagged &#39;websites&#39;">websites</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '16, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/b11e53d9c9dfa78e838c10d1d41b3fb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jason%20Bauer&#39;s gravatar image" /><p><span>Jason Bauer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jason Bauer has no accepted answers">0%</span></p></div></div><div id="comments-container-49456" class="comments-container"></div><div id="comment-tools-49456" class="comment-tools"></div><div class="clear"></div><div id="comment-49456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49458"></span>

<div id="answer-container-49458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49458-score" class="post-score" title="current number of votes">0</div><span id="post-49458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My first step here would be to compare the behaviour of those problematic sites to the behaviour of other sites at the time when the issue with the problematic ones exists. This should tell you quite quickly whether it is a WiFi capacity problem (too many users generating traffic at the same time) or another one. For this step, you even don't need to switch Wireshark on.</p><p>If those problematic sites account for vast majority of the traffic of the clients of the WiFi, as is e.g. often the case with companies using cloud applications, the issue may be also that there is a NAT between the WiFi clients and the internet, and it runs out of available TCP ports as too many clients are using too many short-lived TCP sessions per unit of time. After closing a session to a given server, the TCP port used for that session at client side is usually unusable for a new session for the next two minutes.</p><p>If none of the two cases above seems likely to you, and also to verify whether the second one actually happens, run one Wireshark capture at one of the client PCs and, simultaneously, another Wireshark capture at the AP's wired interface looking towards the internet (using a tap, a hub, a monitoring port of a switch) or, if your infrastructure is more complex than a single AP which gets a public IP address from an ISP, at more points along the path between the client and the ISP-facing interface of your gateway router. Then you should be able to align the two (or more) traces and see whether all what gets to the AP from one side gets successfully to the other one (client -&gt; internet and internet -&gt; client), and if not, which box doesn't let the packets through.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '16, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49458" class="comments-container"></div><div id="comment-tools-49458" class="comment-tools"></div><div class="clear"></div><div id="comment-49458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

