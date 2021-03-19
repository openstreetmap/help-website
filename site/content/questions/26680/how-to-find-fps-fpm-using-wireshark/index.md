+++
type = "question"
title = "How to find fps / fpm using wireshark?"
description = '''In my enviroment we have cisco nexsus 7k which is configured to send flow records (netflows v9) to flow collector / analyzer. Due to how cisco iso is written, there is not a command (at least in my knowledge) which lets me pull flow record based upon interval (seconds etc). This is important to me a...'''
date = "2013-11-05T08:07:00Z"
lastmod = "2013-11-06T04:34:00Z"
weight = 26680
keywords = [ "netflows", "wireshark" ]
aliases = [ "/questions/26680" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find fps / fpm using wireshark?](/questions/26680/how-to-find-fps-fpm-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26680-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my enviroment we have cisco nexsus 7k which is configured to send flow records (netflows v9) to flow collector / analyzer. Due to how cisco iso is written, there is not a command (at least in my knowledge) which lets me pull flow record based upon interval (seconds etc).</p><p>This is important to me as I want to do licensing for the flow exporter/collector. I have options of downloading tools like solar winds/manage-engine / ntop etc to calculate this number but I feel its going over too much hassle of setting up those software to grab a simple value.</p><p>I'm wondering if the already in market packet sniffer tools e.g tcpdump or wireshark can get me this number. I tried with tcpdump but it seems there is no support to decode such information.</p><p>In my little research for wireshark I see there is a built in filter cflows but there are hundreds attributes and sub-attributes don't know which will get me information I want.</p><p>Also, do i need some special configuration on the wireshark end , before I point the flow-records from cisco towards the destinations. I need to have a port opened and a service (flow analyzing) to receive the flow data? I appreciate if someone has a recommendation for flow analyzer software as well thanks.</p></div><div id="question-tags" class="tags-container tags">netflows wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '13, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/a5e36ef8cc4416aa199a3a82dcb1deb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lazerz&#39;s gravatar image" /><p>lazerz<br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lazerz has no accepted answers">0%</span></p></div></div><div id="comments-container-26680" class="comments-container"></div><div id="comment-tools-26680" class="comment-tools"></div><div class="clear"></div><div id="comment-26680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26695"></span>

<div id="answer-container-26695" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26695-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>there is not a command (at least in my knowledge) which lets me <strong>pull flow record based upon interval</strong> (seconds etc).</p></blockquote><p>well, the following command does show flows/sec, however I'm not sure if that is what you need.</p><blockquote><p>show ip cache flow</p></blockquote><pre><code>Flows/Sec

Average number of flows for this protocol per second; equal to the total flows divided by the number of seconds for this summary period.</code></pre><blockquote><p>This is important to me as I want to do licensing for the flow exporter/collector.</p></blockquote><p>It's hard to talk about numbers, as long as it's unclear how the vendor of that software defines what "flows/second" means? There are several vendors that license based on flows/sec or flows/minute, however their definition is totally different (one uses Netflows, the other 'IP flows', etc.). So, I suggest to contact that vendor and ask</p><ul><li>how do you define 'flows/sec'?</li><li>Please provide us a tool that is able to measure that metric in our network, in order for us to be able to purchase the correct license ;-)</li></ul><blockquote><p>In my little research for wireshark I see there is a built in filter cflows but there are hundreds attributes and sub-attributes don't know which will get me information I want.</p></blockquote><p>see above. Unless we know how "flows/sec" is defined, it is impossible to tell what you need to look at.</p><blockquote><p>Also, do i need some special configuration on the wireshark end , before I point the flow-records from cisco towards the destinations.</p></blockquote><p>You just need to mirror the switch port of the Netflow collector (where all Netflow traffic of your network devices are sent to).</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch</a></p></blockquote><p>Then use a PC with Wireshark to capture on the mirrored/monitored port.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '13, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26695" class="comments-container"><span id="26697"></span><div id="comment-26697" class="comment"><div id="post-26697-score" class="comment-score"></div><div class="comment-text"><p>@Kurt thanks for phrase to phrase response to my queries. I will the matter regarding the definition of terminologies (e.g fps) with the vendor. I just have a comment on last part of your reply, why I need to mirror traffic, can i not use netflow v9 and tell the cisco switch to send flow records to port 2055 then on a flow analyzer / collector running locally on my machine i can use wireshark ? does it make sense.</p></div><div id="comment-26697-info" class="comment-info"><span class="comment-age">(06 Nov '13, 07:26)</span> lazerz</div></div><span id="26705"></span><div id="comment-26705" class="comment"><div id="post-26705-score" class="comment-score"></div><div class="comment-text"><blockquote><p>why I need to mirror traffic,</p></blockquote><p>I assumed you already have a Netflow collector in place. To be able to capture traffic to that collector, you would need a mirror port.</p><p>Of course, you can send the Netflwo traffic directly to the Wireshark PC, if that is possible in your environment (re-configuration of routers/switches).</p></div><div id="comment-26705-info" class="comment-info"><span class="comment-age">(07 Nov '13, 01:56)</span> Kurt Knochner ♦</div></div><span id="26711"></span><div id="comment-26711" class="comment"><div id="post-26711-score" class="comment-score"></div><div class="comment-text"><p>@Kurt. Yes re-configuration is possible in our enviroment,not saying we in any way approve the network admins unhappy faces. Anyhow, I was reading your reply on a question posted on the site. <a href="http://ask.wireshark.org/questions/11349/calculating-enterprise-netflow-volume">http://ask.wireshark.org/questions/11349/calculating-enterprise-netflow-volume</a> thought it would be helpful in my case as well.But the filter cflows.flow gives me no result. It returns empty. Any suggestions?</p></div><div id="comment-26711-info" class="comment-info"><span class="comment-age">(07 Nov '13, 05:18)</span> lazerz</div></div><span id="26715"></span><div id="comment-26715" class="comment"><div id="post-26715-score" class="comment-score"></div><div class="comment-text"><p>It does not show anything on my system either. I'll have to check that.</p></div><div id="comment-26715-info" class="comment-info"><span class="comment-age">(07 Nov '13, 06:15)</span> Kurt Knochner ♦</div></div><span id="27047"></span><div id="comment-27047" class="comment"><div id="post-27047-score" class="comment-score"></div><div class="comment-text"><p>any updates?</p></div><div id="comment-27047-info" class="comment-info"><span class="comment-age">(16 Nov '13, 05:37)</span> lazerz</div></div><span id="27061"></span><div id="comment-27061" class="comment not_top_scorer"><div id="post-27061-score" class="comment-score"></div><div class="comment-text"><p>I did not have a chance to test it yet. Maybe during the next couple of days...</p></div><div id="comment-27061-info" class="comment-info"><span class="comment-age">(17 Nov '13, 17:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26695" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-26695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

