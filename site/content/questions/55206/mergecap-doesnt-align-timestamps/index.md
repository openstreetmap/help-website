+++
type = "question"
title = "mergecap doesn&#x27;t align timestamps"
description = '''Hi, I am trying to use mergecap to correct a packet ordering issue across multiple files from the same interface on an appliance, but it isn&#x27;t working. In original file, timestamps do not monotonically increase based on the packet order in the file. I would like help in how to use mergecap or some o...'''
date = "2016-08-30T08:39:00Z"
lastmod = "2016-08-30T11:12:00Z"
weight = 55206
keywords = [ "timestamp", "mergecap" ]
aliases = [ "/questions/55206" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [mergecap doesn't align timestamps](/questions/55206/mergecap-doesnt-align-timestamps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55206-score" class="post-score" title="current number of votes">0</div><span id="post-55206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to use mergecap to correct a packet ordering issue across multiple files from the same interface on an appliance, but it isn't working. In original file, timestamps do not monotonically increase based on the packet order in the file. I would like help in how to use mergecap or some other tool to re-order based on timestamp.</p><p>Details:</p><p>I have an appliance that uses an ASIC to apply rules to certain packets, then forward them out various interfaces. This appliance has a pcap utility that allows the ASIC to feed packets from the ASIC to the capture processing running on host OS. When we capture with the utility, packets come in out of order; that is, the timestamps are correct (as confirmed by external capture device in front of and behind the appliance), but sequential packets may have timestamps that vary forwards or backwards. I can't post the packets but here's an example:<br />
Packet Timestamp</p><ol><li>15:42:26.163</li><li>15:42:34.164</li><li>15:42:34.165</li><li>15:42:26.165</li><li>15:42:53.166</li><li>15:42:26.167</li></ol><p>The reason they do this is, in my opinion because when they write to disk, they're sorting chunks of packets on the sub-second portion of the timestamp rather than on the full timestamp, but that's irrelevant for this question.</p><p>When I use mergecap (default, not with -a option) on either a single or multiple files, it doesn't re-order the packets as I thought it would.</p><p>Does mergecap not actually read the timestamps? Is there a limit on how many frames ahead/behind it can look for the reordering process?<br />
</p><p>Thanks, Tim</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-mergecap" rel="tag" title="see questions tagged &#39;mergecap&#39;">mergecap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '16, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/3f2f87a6a68e4c51c3851c20b6c56a1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CMH_Tim&#39;s gravatar image" /><p><span>CMH_Tim</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CMH_Tim has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-55206" class="comments-container"><span id="55216"></span><div id="comment-55216" class="comment"><div id="post-55216-score" class="comment-score">1</div><div class="comment-text"><p>Thanks to you both. Reordercap did work on the individual and unmerged files to get the traces cleaned up. Guess I just used the wrong search terms when looking for an answer.</p><p>I marked cmaynard's response as the answer since it apparently came in slightly ahead. What's appropriate in terms of awarding points or splitting credit for another near-simultaneous answer?</p><p>looking further at mergecap's documentation, I did see that it explicitly states that it assumes each capture file is in order, so it makes sense for sequential capture files from a given interface, it would have no effect on ordering.</p></div><div id="comment-55216-info" class="comment-info"><span class="comment-age">(30 Aug '16, 11:02)</span> <span class="comment-user userinfo">CMH_Tim</span></div></div><span id="55217"></span><div id="comment-55217" class="comment"><div id="post-55217-score" class="comment-score">1</div><div class="comment-text"><p><em>What's appropriate in terms of awarding points or splitting credit for another near-simultaneous answer?</em></p><p>Since it seems your intention to split the karma, I awarded <span>@BruteForce</span> 1/2 the points.</p></div><div id="comment-55217-info" class="comment-info"><span class="comment-age">(30 Aug '16, 11:12)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-55206" class="comment-tools"></div><div class="clear"></div><div id="comment-55206-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55210"></span>

<div id="answer-container-55210" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55210-score" class="post-score" title="current number of votes">1</div><span id="post-55210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CMH_Tim has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried using <a href="https://www.wireshark.org/docs/man-pages/reordercap.html">reordercap</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '16, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-55210" class="comments-container"></div><div id="comment-tools-55210" class="comment-tools"></div><div class="clear"></div><div id="comment-55210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55211"></span>

<div id="answer-container-55211" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55211-score" class="post-score" title="current number of votes">1</div><span id="post-55211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried reordercap?</p><p>DESCRIPTION Reordercap is a program that reads an input capture file and rewrites the frames to an output capture file, but with the frames sorted by increasing timestamp. This functionality may be useful when capture files have been created by combining frames from more than one well-synchronised source, but the frames have not been combined in strict time order. Reordercap writes the output capture file in the same format as the input capture file. Reordercap is able to detect, read and write the same capture files that are supported by Wireshark.</p><p><a href="https://www.wireshark.org/docs/man-pages/reordercap.html">https://www.wireshark.org/docs/man-pages/reordercap.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '16, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p><span>BruteForce</span><br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-55211" class="comments-container"><span id="55212"></span><div id="comment-55212" class="comment"><div id="post-55212-score" class="comment-score"></div><div class="comment-text"><p>Looks like we had a race condition on the forum cmaynard. Concur.</p></div><div id="comment-55212-info" class="comment-info"><span class="comment-age">(30 Aug '16, 10:11)</span> <span class="comment-user userinfo">BruteForce</span></div></div><span id="55213"></span><div id="comment-55213" class="comment"><div id="post-55213-score" class="comment-score"></div><div class="comment-text"><p>Yes, I suppose you were in the middle of composing your answer when mine had just posted.</p></div><div id="comment-55213-info" class="comment-info"><span class="comment-age">(30 Aug '16, 10:37)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-55211" class="comment-tools"></div><div class="clear"></div><div id="comment-55211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

