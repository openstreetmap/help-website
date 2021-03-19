+++
type = "question"
title = "Any plan for analytics support in wireshark?"
description = '''Hi Developers, Any plan for Analytics support in wireshark ? As lots and lots of applications are getting developed in each and every category(Games,Social Networking,News,Financials,Adult content etc..) and it might be good that if wireshark gives a nice overview with charts(Bar/pie etc..)to make e...'''
date = "2013-04-08T16:49:00Z"
lastmod = "2013-04-08T20:11:00Z"
weight = 20222
keywords = [ "analytics", "wireshark" ]
aliases = [ "/questions/20222" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Any plan for analytics support in wireshark?](/questions/20222/any-plan-for-analytics-support-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20222-score" class="post-score" title="current number of votes">0</div><span id="post-20222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Developers,</p><p>Any plan for Analytics support in wireshark ? As lots and lots of applications are getting developed in each and every category(Games,Social Networking,News,Financials,Adult content etc..) and it might be good that if wireshark gives a nice overview with charts(Bar/pie etc..)to make end user more informed about traffic patterns.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-analytics" rel="tag" title="see questions tagged &#39;analytics&#39;">analytics</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '13, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-20222" class="comments-container"></div><div id="comment-tools-20222" class="comment-tools"></div><div class="clear"></div><div id="comment-20222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20228"></span>

<div id="answer-container-20228" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20228-score" class="post-score" title="current number of votes">1</div><span id="post-20228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Various open-source projects are, to differing degrees, "crowdsourced". Wireshark's probably on the "very crowdsourced" end of that spectrum, so that what shows up in Wireshark is less a matter of formal plans by the core developers and more a matter of "somebody decides to implement it in Wireshark and contribute it" (the contributor might be a core developer, but, if so, they're probably not doing it as part of a formal plan).</p><p>If you want, for example, something to show traffic broken up into categories such as "Games,Social Networking,News,Financials,Adult content,etc.", you'd probably have to have lists of hosts for those categories (as a lot of the traffic is just HTTP at the protocol layer) and something that, instead of showing a graph or chart based on hosts, shows it based on host categories.</p><p>(That would also require code in Wireshark for drawing charts other than the line graphs we have currently, e.g. pie or bar chart code.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 20:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20228" class="comments-container"></div><div id="comment-tools-20228" class="comment-tools"></div><div class="clear"></div><div id="comment-20228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20226"></span>

<div id="answer-container-20226" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20226-score" class="post-score" title="current number of votes">0</div><span id="post-20226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at the graphing functions available under the Statistics menu. Basically, anything you can use as a display filter can be graphed. Those graphs are exportable in several formats.</p><p>I'm not a Wireshark developer, but as far as pie charts, bar graphs, etc...<em>shrug</em></p><p>Part of the problem with "doing graphs" is the question of which formats to use. I know folks who won't use any graph they can't generate in their favorite tool (Excel, OpenOffice, whatever). I'd rather have the ability to export analytics as CSVs, which I could then import into the tool of my choice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 19:33</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-20226" class="comments-container"></div><div id="comment-tools-20226" class="comment-tools"></div><div class="clear"></div><div id="comment-20226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

