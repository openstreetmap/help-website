+++
type = "question"
title = "Automatically start capturing packets when bandwidth is high"
description = '''Hi there. I&#x27;d like to leave WireShark running on all my machines, and have it automatically capture packets when total bandwidth usage is above a user defined value. For example, I have WireShark running on my machine 24/7, and when the connection being monitored starts to use 20Mbps or more, WireSh...'''
date = "2011-01-11T15:43:00Z"
lastmod = "2012-10-11T19:07:00Z"
weight = 1709
keywords = [ "high", "capture", "bandwidth", "automatic" ]
aliases = [ "/questions/1709" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Automatically start capturing packets when bandwidth is high](/questions/1709/automatically-start-capturing-packets-when-bandwidth-is-high)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1709-score" class="post-score" title="current number of votes">0</div><span id="post-1709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there.</p><p>I'd like to leave WireShark running on all my machines, and have it automatically capture packets when total bandwidth usage is above a user defined value.</p><p>For example, I have WireShark running on my machine 24/7, and when the connection being monitored starts to use 20Mbps or more, WireShark will begin capturing the packets and dumping them into a file (Preferably timestamped).</p><p>This would be great for me as if a machine was being attacked by a Denial of Service attack, I would be able to log onto the machine after the attack stops and have a clear log of all packets going through that interface during the attack.</p><p>Please let me know if this is currently possible, or guide me in the right direction.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-high" rel="tag" title="see questions tagged &#39;high&#39;">high</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-automatic" rel="tag" title="see questions tagged &#39;automatic&#39;">automatic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '11, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/82bb9c1f0f94225eb33282bcb74e5e8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ninjadude101&#39;s gravatar image" /><p><span>Ninjadude101</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ninjadude101 has no accepted answers">0%</span></p></div></div><div id="comments-container-1709" class="comments-container"></div><div id="comment-tools-1709" class="comment-tools"></div><div class="clear"></div><div id="comment-1709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="1710"></span>

<div id="answer-container-1710" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1710-score" class="post-score" title="current number of votes">0</div><span id="post-1710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Why not just use a rotating ring buffer? What you are asking is to capture traffic when it is high and would actually have the most impact on the machine and its storage. I assume the reason for this question is that you are wanting to lessen the impact on the machine and its storage. However, adding a service and collecting the packets will actually add to the potential of a DoS.<br />
</p><p>I do find this to be an interesting way to think outside the box. I think it could be done by writing a shell script or batch file to invoke dumpcap. Then triggering the script by querying the interface with some WMI or SNMP probe and watch for the crossing of a threshhold. I could certainly help with the dumpcap syntax, but the trigger is outside of my expertise.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '11, 16:57</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></p></div></div><div id="comments-container-1710" class="comments-container"><span id="1715"></span><div id="comment-1715" class="comment"><div id="post-1715-score" class="comment-score"></div><div class="comment-text"><p>Paul, actually the reason behind my question is not to lessen the impact on the storage, but to provide an always-on solution for retrieving information behind DoS attacks.</p><p>Unfortunately, due to the nature of my business, my servers see a few (D)DoS attacks each month, and I am not always able to get onto the machine to start WireShark (Which in most cases provides information useful for finding out who is responsible). This solution will simply mean that after a (D)DoS attack, all I'd need to do is log onto the server via remote desktop and open up the latest log file to see that information.</p><p>Once I am done with the log file, it would be removed, so in fact this shouldn't have a massive impact on the storage as it will only be logging packets when the bandwidth is high.</p><p>I hope I've made myself clearer.</p><p>hansangb, Could you possibly go into more detail with the ring buffers, as I am relatively new to WireShark and lack the understanding of the terminology. I had a look at CACE Pilot, but it's quite expensive!</p><p>Thanks all.</p></div><div id="comment-1715-info" class="comment-info"><span class="comment-age">(12 Jan '11, 05:16)</span> <span class="comment-user userinfo">Ninjadude101</span></div></div><span id="1717"></span><div id="comment-1717" class="comment"><div id="post-1717-score" class="comment-score"></div><div class="comment-text"><p>Ninjadude, When you open the capture options (CTRL-K), 1) Specify the file name (under Capture Files section). 2) Check the "Use multiple files" 3) Determine if you want the rotation of files to happen based on time (next file every x min) or by capture file size (next file every x MB) 4) Check the "Ring buffer with x files" and figure out how many files you want to create before wrapping around. Make sure you have enough HD space.</p><p>That's pretty much it.</p></div><div id="comment-1717-info" class="comment-info"><span class="comment-age">(12 Jan '11, 05:36)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="1718"></span><div id="comment-1718" class="comment"><div id="post-1718-score" class="comment-score"></div><div class="comment-text"><p>I think there is some legitimacy to your reasoning. However, one concern is that you would miss the traffic prior to the trigger event. Obviously you know your business and constraints better than I do. If it were me, I'd consider capturing the traffic off box. In other words build an adequate size capture pc or server. Place it on a span or monitor port that has visibility to all of the servers. Then set up dumpcap to capture to a 'ring buffer' set of files. I'd make them a reasonable size (100MB or so). Then configure the number of files based on the maximum space you have on this dedicated machine. This approach will give you greater visibility. I'd give examples, but I'm posting from my phone.</p></div><div id="comment-1718-info" class="comment-info"><span class="comment-age">(12 Jan '11, 05:41)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div></div><div id="comment-tools-1710" class="comment-tools"></div><div class="clear"></div><div id="comment-1710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1711"></span>

<div id="answer-container-1711" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1711-score" class="post-score" title="current number of votes">0</div><span id="post-1711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ninjadude101 Unfortunately, Wireshark lacks the trigger mechanism. So you'll have to go with ring buffers (and capture just 96 bytes if all you want is the header info) or get Cace's Pilot which has trigger mechanisms (called Watches)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '11, 18:42</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-1711" class="comments-container"></div><div id="comment-tools-1711" class="comment-tools"></div><div class="clear"></div><div id="comment-1711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1716"></span>

<div id="answer-container-1716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1716-score" class="post-score" title="current number of votes">0</div><span id="post-1716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ninjadude, When you open the capture options (CTRL-K), 1) Specify the file name (under Capture Files section). 2) Check the "Use multiple files" 3) Determine if you want the rotation of files to happen based on time (next file every x min) or by capture file size (next file every x MB) 4) Check the "Ring buffer with x files" and figure out how many files you want to create before wrapping around. Make sure you have enough HD space.</p><p>That's pretty much it.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '11, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-1716" class="comments-container"><span id="10107"></span><div id="comment-10107" class="comment"><div id="post-10107-score" class="comment-score"></div><div class="comment-text"><p>I followed your instructions above. Why are the files captured contain unreadble characters??? I was going to do the same problem for Ninjadude101, capturing the DoS attack events to a log.</p></div><div id="comment-10107-info" class="comment-info"><span class="comment-age">(13 Apr '12, 01:18)</span> <span class="comment-user userinfo">misteryuku</span></div></div></div><div id="comment-tools-1716" class="comment-tools"></div><div class="clear"></div><div id="comment-1716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14945"></span>

<div id="answer-container-14945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14945-score" class="post-score" title="current number of votes">0</div><span id="post-14945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>how to start capture automatically when i copy any remote file and it should stop as it file transfer complete??</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 19:07</strong></p><img src="https://secure.gravatar.com/avatar/66d9f832d9f5762ba4c0ddec8c68cfd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ali&#39;s gravatar image" /><p><span>Ali</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ali has no accepted answers">0%</span></p></div></div><div id="comments-container-14945" class="comments-container"></div><div id="comment-tools-14945" class="comment-tools"></div><div class="clear"></div><div id="comment-14945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

