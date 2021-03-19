+++
type = "question"
title = "Wireshark - Traffic monitoring/accounting for home network"
description = '''Hi New to Wireshark from today. 70 yr + (be gentle on me) I have a problem with excessive data usage, gone from 30G per month to 100G per month. And I would like to know why. Will this software show me the laptop in use and the web IP from where the data is going/from. Setup is two wireless laptops ...'''
date = "2014-04-19T21:33:00Z"
lastmod = "2014-04-21T09:18:00Z"
weight = 32010
keywords = [ "wanmonitordslrouter", "windows7", "bandwidthutilization" ]
aliases = [ "/questions/32010" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - Traffic monitoring/accounting for home network](/questions/32010/wireshark-traffic-monitoringaccounting-for-home-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32010-score" class="post-score" title="current number of votes">0</div><span id="post-32010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi New to Wireshark from today. 70 yr + (be gentle on me)</p><p>I have a problem with excessive data usage, gone from 30G per month to 100G per month. And I would like to know why. Will this software show me the laptop in use and the web IP from where the data is going/from. Setup is two wireless laptops and 1 internet capable tv (not used much at all). All going thru a wireless router.</p><p>Wireshark asks me to select interface, 3 options, local area, wireless network, and wireless network 2. How do I establish which one to use ?</p><p>Running the capture seems to look ok.</p><p>For the capture all I need for the report is data in capture that is say over 500m per event, the size, date/time, IP of laptop or device, and the IP address of the web IP. Don't need anything else.</p><p>Can someone help set a template for just only this info. (I guess this is capture options?) So for my old brain I can just look at the basic 4 or 5 columns.</p><p>Any help or comments would be appreciated. Charlie Harris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wanmonitordslrouter" rel="tag" title="see questions tagged &#39;wanmonitordslrouter&#39;">wanmonitordslrouter</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-bandwidthutilization" rel="tag" title="see questions tagged &#39;bandwidthutilization&#39;">bandwidthutilization</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '14, 21:33</strong></p><img src="https://secure.gravatar.com/avatar/846395d71b48eb703c22e680a19a16f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swchuck&#39;s gravatar image" /><p><span>swchuck</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swchuck has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Apr '14, 15:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-32010" class="comments-container"><span id="32028"></span><div id="comment-32028" class="comment"><div id="post-32028-score" class="comment-score"></div><div class="comment-text"><p>Like Kurt said below, if you wanted to use Wireshark for this purpose, you would have to create a bridged connection so that Wireshark can see all the data flowing between your router and the internet and capture it. But... Wireshark isn't really meant to perform this type of analysis unless you have a good idea of what you're looking for. Have you checked your router's settings? Maybe it has the ability to show you the data from each connected client?</p></div><div id="comment-32028-info" class="comment-info"><span class="comment-age">(21 Apr '14, 09:18)</span> <span class="comment-user userinfo">mire3212</span></div></div></div><div id="comment-tools-32010" class="comment-tools"></div><div class="clear"></div><div id="comment-32010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32014"></span>

<div id="answer-container-32014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32014-score" class="post-score" title="current number of votes">1</div><span id="post-32014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is primarily a network analysis and troubleshooting tool. While you can use it to get some traffic statistics, it's not built with that purpose in mind and thus it is not the best tool to use for such a scenario, especially if you want to get information for a long period of time (days, weeks, months) and with large amounts of data (30-100 Gbyte).</p><p>So, please consider using a different tool like <a href="http://humdi.net/vnstat/">vnstat</a> (sample output: <a href="http://humdi.net/vnstat/cgidemo/">http://humdi.net/vnstat/cgidemo/</a> ) or any other network monitoring tool (ntop, iftop, etc.). If you don't know or don't like Linux, other Unix like systems or *BSD systems (and how to build a bridge or router with those systems to monitor the whole internet traffic), take a look at similar tools for Windows (just google for "network monitoring windows") and run them on every Windows system in your network (except the TV set). Those tools will tell you how much traffic is consumed by which system and probably also the 'top talkers'.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '14, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Apr '14, 14:51</strong> </span></p></div></div><div id="comments-container-32014" class="comments-container"></div><div id="comment-tools-32014" class="comment-tools"></div><div class="clear"></div><div id="comment-32014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32012"></span>

<div id="answer-container-32012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32012-score" class="post-score" title="current number of votes">0</div><span id="post-32012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With wireshark you can not do selective capturing for file size. You can do selective capturing for source IP, Destination IP, serivices, etc. But not file size.</p><p>Feel free to ask me more questions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '14, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/ee0dd9b5ea44e7f8db0040e34109a712?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hardshah4&#39;s gravatar image" /><p><span>hardshah4</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hardshah4 has no accepted answers">0%</span></p></div></div><div id="comments-container-32012" class="comments-container"></div><div id="comment-tools-32012" class="comment-tools"></div><div class="clear"></div><div id="comment-32012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

