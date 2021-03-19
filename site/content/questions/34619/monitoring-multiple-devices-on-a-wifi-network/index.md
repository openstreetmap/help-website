+++
type = "question"
title = "monitoring multiple devices on a wifi network"
description = '''Hello one and all I have several devices that connects to a single wifi network. Myself who does normal business internet and searches, my sons who play games such as clash of clans and three students who are spending their summer with me - they use mainly email, facebook and a couple of clash of cl...'''
date = "2014-07-13T04:07:00Z"
lastmod = "2014-07-15T07:01:00Z"
weight = 34619
keywords = [ "usage", "multiple", "monitoring", "devices", "data" ]
aliases = [ "/questions/34619" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [monitoring multiple devices on a wifi network](/questions/34619/monitoring-multiple-devices-on-a-wifi-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34619-score" class="post-score" title="current number of votes">0</div><span id="post-34619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello one and all</p><p>I have several devices that connects to a single wifi network. Myself who does normal business internet and searches, my sons who play games such as clash of clans and three students who are spending their summer with me - they use mainly email, facebook and a couple of clash of clans type games. We have a new 20gb data plan and in short are using this up in a matter of three weeks. My question is this, would wireshark be able to indicate much data each device is using daily so that I can try to identify which device is using up most of the data? I have a Windows 7 PC.</p><p>I would appreciate any information/advice anyone can give me. The easier to use, the better!</p><p>Thank you in advance.</p><p>Regards, Nerina</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span> <span class="post-tag tag-link-devices" rel="tag" title="see questions tagged &#39;devices&#39;">devices</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '14, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/ebca7e032f648db14df3ee2cd419dd18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="warthog&#39;s gravatar image" /><p><span>warthog</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="warthog has no accepted answers">0%</span></p></div></div><div id="comments-container-34619" class="comments-container"></div><div id="comment-tools-34619" class="comment-tools"></div><div class="clear"></div><div id="comment-34619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34648"></span>

<div id="answer-container-34648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34648-score" class="post-score" title="current number of votes">0</div><span id="post-34648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is primarily a network troubleshooting tool. While it <strong>can be used</strong> to monitor traffic, it's not perfect for that purpose, especially if you have limited networking knowledge (which I assume, based on your question). So, I suggest another solution for you:</p><ul><li>Look at the traffic stats of your router. Some routers do summarize the traffic of internal clients and create neat stats that should help you to figure out who is consuming that much traffic.</li><li>If your router does not provide that kind of stats, <strong>consider to buy a new router</strong>, as everything I'm going to suggest now, will be <strong>much more work</strong> and probably <strong>even cost more</strong></li><li>Install Linux on an unused PC. Install some <a href="http://dynacont.net/documentation/linux/network_monitoring/">network statistics tool</a> on it (google will help to find one - like: Bandwidthd). Buy a network switch with port mirroring capabilities. Attach your router to the switch. Attach your PC to the switch. Mirror the traffic to/from the router to the PC. Let the network stats software monitor the whole network traffic.</li></ul><blockquote><p>and three students who are spending their summer with me - <strong>they use mainly</strong> email, facebook and a couple of clash of clans type games</p></blockquote><p>Yeah, that's what they tell <strong>you</strong> ;-)) 20 Gbyte/month is really <strong>nothing</strong> for a gang of young students. Youtube videos and/or online music/video channels do consume more download data than you might think, so 20 Gybtes are gone within days, not weeks ;-))</p><p>Isn't there a flat rate available where you live?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '14, 02:57</strong> </span></p></div></div><div id="comments-container-34648" class="comments-container"><span id="34661"></span><div id="comment-34661" class="comment"><div id="post-34661-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt</p><p>Many thanks for taking the time out to answer my question.<br />
</p><p>I understand that wireshark is not the answer for me and I will certainly explore what my router is or is not capable of doing. It is an relatively cheap fix if I have to replace it and I'll not have to worry about even trying to understand your second option! You are right, I'm afraid this kind of technology overtook me years ago and my knowledge is very limited.</p><p>I'm not sure where you are based, but in South Africa network technology is still expensive and unlimited internet is not available on our cellular network.</p><p>The students are pretty sensitive to my internet battle, but I will ask again that they make sure they don't do any streaming and that all automatic updates are turned off.</p><p>Thanks again for your time. Have a good day.</p><p>Regards, Nerina</p></div><div id="comment-34661-info" class="comment-info"><span class="comment-age">(15 Jul '14, 06:40)</span> <span class="comment-user userinfo">warthog</span></div></div><span id="34664"></span><div id="comment-34664" class="comment"><div id="post-34664-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm not sure where you are based, but in South Africa network technology is still expensive and unlimited internet is not available on our cellular network.</p></blockquote><p>well, compared to a cellular network, our connectivity is <strong>a bit</strong> better here in central europe ;-))</p><p>BTW: Before buying a new router, you should check if your current router is able to run</p><ul><li><a href="http://openwrt.org/">OpenWRT</a></li><li><a href="http://www.dd-wrt.com/">DD-WRT</a> or</li><li><a href="http://www.gargoyle-router.com/">Gargoyle</a>,</li></ul><p>as those OSes will offer at least some stats.</p><p>Good luck!</p></div><div id="comment-34664-info" class="comment-info"><span class="comment-age">(15 Jul '14, 06:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="34665"></span><div id="comment-34665" class="comment"><div id="post-34665-score" class="comment-score"></div><div class="comment-text"><p>The alternative router software is a good idea.</p><p>I use <a href="http://victek.is-a-geek.com/">Tomato RAF</a> software on my Linksys E3000 and that shows me bandwidth use on a per IP basis. I fix all the known clients to the same IP's so I can see at a glance which device is hammering the network.</p></div><div id="comment-34665-info" class="comment-info"><span class="comment-age">(15 Jul '14, 07:01)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-34648" class="comment-tools"></div><div class="clear"></div><div id="comment-34648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

