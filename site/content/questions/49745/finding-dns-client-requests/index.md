+++
type = "question"
title = "Finding DNS Client Requests"
description = '''My internal DNS servers point to Google DNS 8.8.8.8 for Internet traffic. On my firewall I am seeing some curious traffic where there the DNS servers make a request to a suspicious URL but I cannot find a corresponding web or Internet traffic entry. For instance under normal traffic if a user goes t...'''
date = "2016-02-02T15:03:00Z"
lastmod = "2016-02-03T19:53:00Z"
weight = 49745
keywords = [ "dns" ]
aliases = [ "/questions/49745" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Finding DNS Client Requests](/questions/49745/finding-dns-client-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49745-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My internal DNS servers point to Google DNS 8.8.8.8 for Internet traffic. On my firewall I am seeing some curious traffic where there the DNS servers make a request to a suspicious URL but I cannot find a corresponding web or Internet traffic entry. For instance under normal traffic if a user goes to www.wireshark.org I will see the DNS query from my internal DNS to Google DNS and then see web browser traffic from the user in the web logs. These periodic suspicious entries show up as requests from my DNS servers to Google but I can find no entries in the firewall logs of any client visiting those URLs.</p><p>I have setup packet captures on the DNS servers. With a normal query I see the DNS entry from the client to the DNS server followed by the DNS query to Google. With these strange entries all I see is the DNS server contacting Google and then nothing.<br />
</p><p>What additional traffic besides port 53 should I monitor? Is there some way to monitor for DNS packets that possibly are not connecting on port 53?</p></div><div id="question-tags" class="tags-container tags">dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '16, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/d3db4630e13acceff60d7f0b6626ce66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Naami&#39;s gravatar image" /><p>Tim Naami<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Naami has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-49745" class="comments-container"><span id="49756"></span><div id="comment-49756" class="comment"><div id="post-49756-score" class="comment-score"></div><div class="comment-text"><p>A sample capture would be nice.</p></div><div id="comment-49756-info" class="comment-info"><span class="comment-age">(02 Feb '16, 22:44)</span> Jaap ♦</div></div><span id="49789"></span><div id="comment-49789" class="comment"><div id="post-49789-score" class="comment-score"></div><div class="comment-text"><p>Two problems. I can't post the PCAPs for confidential reasons. The PCAPs are 20MB+ most of the time as I have to leave them run until I see an alert from the firewall.</p></div><div id="comment-49789-info" class="comment-info"><span class="comment-age">(03 Feb '16, 09:15)</span> Tim Naami</div></div><span id="49793"></span><div id="comment-49793" class="comment"><div id="post-49793-score" class="comment-score"></div><div class="comment-text"><p>20 megs are not a problem, confidentiality is a different issue. Can you post the two packets carrying the DNS query for the "suspicious url" and the DNS response to it (if it ever comes from Google DNS)? <code>File -&gt; Export Specifed Packets -&gt; Range [ 122678, 122913 ]</code> (the values are example ones of course) can do the trick.</p></div><div id="comment-49793-info" class="comment-info"><span class="comment-age">(03 Feb '16, 13:42)</span> sindy</div></div></div><div id="comment-tools-49745" class="comment-tools"></div><div class="clear"></div><div id="comment-49745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49801"></span>

<div id="answer-container-49801" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49801-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The question is not so clear to me, but here are some ideas for a diagnostic: - Try shutting off all your machines (perhaps you can, in the night?) and only leave your internal DNS Servers on, then check your firewall logs and see if the curious traffic is still happening. - Then try shutting on one machine by one machine, until you see the curious traffic comng again. - If you suspect the DNS Servers themselves, try starting your DNS Servers in Windows Safe Mode with Networking, and see if the curious traffic is there or not. - Lastly, can you post again with clearer explanations and cases. Best: some sample captures. M.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '16, 19:53</strong></p><img src="https://secure.gravatar.com/avatar/0d34cdc32519fc3c7ebcbbfa3aa5873a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thewol&#39;s gravatar image" /><p>thewol<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thewol has no accepted answers">0%</span></p></div></div><div id="comments-container-49801" class="comments-container"></div><div id="comment-tools-49801" class="comment-tools"></div><div class="clear"></div><div id="comment-49801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

