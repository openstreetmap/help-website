+++
type = "question"
title = "Desperately need advice on monitoring data usage"
description = '''Hi there, firstly, I&#x27;m not a software novice, but new to Wireshark. I have a leak in my home network that is using about 5gb of data per day. I don&#x27;t have time (due to traveling) to simply pull a device off the network every day until I find the culprit. I really need a simple way to view only -MAC ...'''
date = "2015-06-18T17:33:00Z"
lastmod = "2015-06-18T19:40:00Z"
weight = 43349
keywords = [ "monitoring", "bandwidthutilization" ]
aliases = [ "/questions/43349" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Desperately need advice on monitoring data usage](/questions/43349/desperately-need-advice-on-monitoring-data-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43349-score" class="post-score" title="current number of votes">0</div><span id="post-43349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, firstly, I'm not a software novice, but new to Wireshark.</p><p>I have a leak in my home network that is using about 5gb of data per day. I don't have time (due to traveling) to simply pull a device off the network every day until I find the culprit.</p><p>I really need a simple way to view only</p><p><strong>-MAC or Physical name</strong></p><p><strong>-Total data usage (up and down)</strong></p><p><strong>-over a given time span</strong></p><p>You think that would be simple enough to find, but no. I can't seem to organize a template that makes sense to me. I have a leak somewhere and I'm pulling my hair out. (And my wallet)</p><p>Surely Wireshark can do this, right?</p><p>Thanks in advance!</p><p>db.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span> <span class="post-tag tag-link-bandwidthutilization" rel="tag" title="see questions tagged &#39;bandwidthutilization&#39;">bandwidthutilization</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '15, 17:33</strong></p><img src="https://secure.gravatar.com/avatar/0f2fa51dc3d59272cb19d7a915ad805d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dab3838&#39;s gravatar image" /><p><span>dab3838</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dab3838 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '15, 17:36</strong> </span></p></div></div><div id="comments-container-43349" class="comments-container"></div><div id="comment-tools-43349" class="comment-tools"></div><div class="clear"></div><div id="comment-43349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43351"></span>

<div id="answer-container-43351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43351-score" class="post-score" title="current number of votes">0</div><span id="post-43351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have a packet capture of all the data that was passing through the network (from all machines) at the time of the leak? If so, just go to Statistics -&gt; Conversations and you'll see how many bytes up/down for each "conversation" between one address and another. Sort by the Bytes column and you'll get the worst offender.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '15, 19:39</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-43351" class="comments-container"><span id="43352"></span><div id="comment-43352" class="comment"><div id="post-43352-score" class="comment-score"></div><div class="comment-text"><p>Edit: for the timespan question, you can go to Statistics -&gt; IO Graph and filter on IP address (eg: ip.addr==1.2.3.4) to see usage over time for each host.</p><p>For home networks, usually the bigger challenge is GETTING the packets from all the machines in the home into a single Wireshark trace since one host in a LAN won't normally receive all the traffic from the other hosts to be analyzed. Once you have such a trace, the analysis part you're asking about is fairly straightforward.</p></div><div id="comment-43352-info" class="comment-info"><span class="comment-age">(18 Jun '15, 19:40)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-43351" class="comment-tools"></div><div class="clear"></div><div id="comment-43351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

