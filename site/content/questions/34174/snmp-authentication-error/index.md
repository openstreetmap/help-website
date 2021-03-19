+++
type = "question"
title = "SNMP Authentication Error"
description = '''I have a network running Windows 2008 R2 and Windows 7 64 Bit. All systems are fully patched. For some reason a few months ago my SNMP Manager started displaying Authentication Error trap messages. I see this trap being generated, randomly, on almost every machine on my network, at least the worksta...'''
date = "2014-06-25T09:27:00Z"
lastmod = "2014-06-26T00:59:00Z"
weight = 34174
keywords = [ "snmp", "trap", "error" ]
aliases = [ "/questions/34174" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SNMP Authentication Error](/questions/34174/snmp-authentication-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34174-score" class="post-score" title="current number of votes">0</div><span id="post-34174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a network running Windows 2008 R2 and Windows 7 64 Bit. All systems are fully patched. For some reason a few months ago my SNMP Manager started displaying Authentication Error trap messages. I see this trap being generated, randomly, on almost every machine on my network, at least the workstations. Some machines more than others. My SNMP manager is running on a .205 address. Earlier this machine started generating the Trap error so I ran a trace and the communication is between my server running SNMP Manager, .205 and a second server .78 which is running SolarWinds Orion. I double checked the SNMP settings on the two servers and everything is correct.</p><p>Weird thing is the message will appear for a while, then stop. Move to different machines etc. there appears to be no pattern to it.</p><p>Can anyone point my in the right direction to look. I could open a ticket with Solarwinds but I prefer to try first on my own.</p><p>I can post the trace file if that helps.</p><p>Thanks in advance.</p><p>Robert Mezzone</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span> <span class="post-tag tag-link-trap" rel="tag" title="see questions tagged &#39;trap&#39;">trap</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/9ac06e048db50cbb1f84e68e5517f0f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgm34&#39;s gravatar image" /><p><span>rgm34</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgm34 has no accepted answers">0%</span></p></div></div><div id="comments-container-34174" class="comments-container"><span id="34176"></span><div id="comment-34176" class="comment"><div id="post-34176-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry but I'm confused. Who exactly is sending the SNMP traps to whom?</p><ol><li>clients -&gt; .205</li><li>.205 -&gt; .78?</li></ol><p>If 1.) why did you mention .78?<br />
If 2.) why did you mention 'all' clients?</p><p>Furthermore: Are those traps about Windows authentication problems of the clients, or are you talking about SNMP error messages because of SNMPv3 authentication problems?</p><p>Is it possible to post a sample capture file somewhere (google drive, dropbox, cloudshark.org)?</p></div><div id="comment-34176-info" class="comment-info"><span class="comment-age">(25 Jun '14, 09:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="34178"></span><div id="comment-34178" class="comment"><div id="post-34178-score" class="comment-score"></div><div class="comment-text"><p>That makes two of us :-)</p><p>In the trace the source is .205 and the destination is .78.</p><p>The trace file reports the following</p><p>generic-trap: authenticationFailure (4)</p><p>I'm running SNMP v2.</p><p>I mentioned all clients because at some point during the course of a day, most but not all clients are reporting the Authentication Failure error in my SNMP Manager. It's very random. For instance, this has been happening for a couple of months. For the first time, my computer reported the Authentication Failure for the first time. It happened for an hour or so and that was it, hasn't happened again.</p><p>I will try and post the trace file to cloudshark.org, haven't used the service.</p><p>Robert</p></div><div id="comment-34178-info" class="comment-info"><span class="comment-age">(25 Jun '14, 10:00)</span> <span class="comment-user userinfo">rgm34</span></div></div><span id="34180"></span><div id="comment-34180" class="comment"><div id="post-34180-score" class="comment-score"></div><div class="comment-text"><p>I posted the capture file to a OneDrive account. Thank you for your help with this.</p><p><a href="https://onedrive.live.com/?cid=949862ff5b8a7a62&amp;id=949862FF5B8A7A62!107&amp;Bsrc=Share&amp;Bpub=SDX.SkyDrive&amp;authkey=!AoN8QwkLEE0IvwQ">https://onedrive.live.com/?cid=949862ff5b8a7a62&amp;id=949862FF5B8A7A62!107&amp;Bsrc=Share&amp;Bpub=SDX.SkyDrive&amp;authkey=!AoN8QwkLEE0IvwQ</a></p></div><div id="comment-34180-info" class="comment-info"><span class="comment-age">(25 Jun '14, 10:14)</span> <span class="comment-user userinfo">rgm34</span></div></div><span id="34182"></span><div id="comment-34182" class="comment"><div id="post-34182-score" class="comment-score"></div><div class="comment-text"><p>@rgm32</p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-34182-info" class="comment-info"><span class="comment-age">(25 Jun '14, 10:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="34208"></span><div id="comment-34208" class="comment"><div id="post-34208-score" class="comment-score"></div><div class="comment-text"><p>If the community name or access permission is incorrect, and the SNMP service has been configured to send an authentication trap, the agent sends an “authentication failure” trap to the specified trap destination.One notable point is that all traps with Authentication Failure error has SNMP Version set as 1.Could not relate this with error messages but you can search.</p></div><div id="comment-34208-info" class="comment-info"><span class="comment-age">(26 Jun '14, 00:59)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-34174" class="comment-tools"></div><div class="clear"></div><div id="comment-34174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34184"></span>

<div id="answer-container-34184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34184-score" class="post-score" title="current number of votes">0</div><span id="post-34184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I cannot see any reason for the traps in the capture files. So, it's either something you did not capture or related to a local problem on .205. I suggest to check the logs (event logs) on that system. Try to find something close to the time stamps of the traps. Maybe you'll find something that is related (somehow).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-34184" class="comments-container"></div><div id="comment-tools-34184" class="comment-tools"></div><div class="clear"></div><div id="comment-34184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

