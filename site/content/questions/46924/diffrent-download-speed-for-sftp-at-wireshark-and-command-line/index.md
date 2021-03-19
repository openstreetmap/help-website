+++
type = "question"
title = "Diffrent download speed for sftp at wireshark and command line"
description = '''Hi All, I have tested the bandwidth with simply tranfering a big file with sftp from one Linux server to another. But the transfer rates are demonsrated diferently at wireshark and command line. Command Line: xxxxx.rpm 100% 127MB 11.5MB/s 00:11 Wireshark: I couldn&#x27;t copy the image but the data at Pr...'''
date = "2015-10-26T01:51:00Z"
lastmod = "2015-10-27T01:15:00Z"
weight = 46924
keywords = [ "download", "sftp", "speed", "wireshark", "linux" ]
aliases = [ "/questions/46924" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Diffrent download speed for sftp at wireshark and command line](/questions/46924/diffrent-download-speed-for-sftp-at-wireshark-and-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46924-score" class="post-score" title="current number of votes">0</div><span id="post-46924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I have tested the bandwidth with simply tranfering a big file with sftp from one Linux server to another. But the transfer rates are demonsrated diferently at wireshark and command line.</p><p>Command Line: xxxxx.rpm 100% 127MB 11.5MB/s 00:11</p><p>Wireshark: I couldn't copy the image but the data at Protocol Hierarchy Statistics for SSH Protocol is 18.332 Mbit/s</p><p>Do you have any idea why this difference happenned?</p><p>BR Ercan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-sftp" rel="tag" title="see questions tagged &#39;sftp&#39;">sftp</span> <span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '15, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/c7ce0ed4a3c46aaf8537d15d497b5cd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ercansah&#39;s gravatar image" /><p><span>Ercansah</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ercansah has no accepted answers">0%</span></p></div></div><div id="comments-container-46924" class="comments-container"></div><div id="comment-tools-46924" class="comment-tools"></div><div class="clear"></div><div id="comment-46924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46930"></span>

<div id="answer-container-46930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46930-score" class="post-score" title="current number of votes">0</div><span id="post-46930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark takes the paket length for it's statistics, while your tool might use the application payload bytes to calculate the throughput (dpends on that tools). That will certainly result in different throughput values.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '15, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46930" class="comments-container"><span id="46965"></span><div id="comment-46965" class="comment"><div id="post-46965-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Thanks for your answer but it doesn't seem logical to me. The difference beyween application payload and the whole packet is the headers. Do you really think that headers can cause almost %50 b/w speed difference?</p><p>BR Ercan</p></div><div id="comment-46965-info" class="comment-info"><span class="comment-age">(26 Oct '15, 22:54)</span> <span class="comment-user userinfo">Ercansah</span></div></div><span id="46968"></span><div id="comment-46968" class="comment"><div id="post-46968-score" class="comment-score"></div><div class="comment-text"><p>Well, hard to tell without a capture file. In theory it would be possible, if you have a lot of small frames + plus what <span></span><span>@mrEEde</span> said. <strong>However</strong> we are talking about 11.5 Mbyte/s, so this is all rather unlikely. As I said, hard to tell without a capture file. Is it possible to upload it somewhere (dropbox, etc.) and post the link here?</p><p>BTW: Your tool reports 11.5 M<strong>byte</strong>/s, while you say that Wireshark reports 18.332 M<strong>bits</strong>/s. So it's Mbyte/s versus Mbit/s. Is that a typo?</p></div><div id="comment-46968-info" class="comment-info"><span class="comment-age">(27 Oct '15, 01:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46930" class="comment-tools"></div><div class="clear"></div><div id="comment-46930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46966"></span>

<div id="answer-container-46966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46966-score" class="post-score" title="current number of votes">0</div><span id="post-46966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Protocol Hierarchy Statistics for SSH takes packets in both directions into account whereas the SFTP only measures the throughput based on the payload in one direction.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '15, 23:40</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-46966" class="comments-container"></div><div id="comment-tools-46966" class="comment-tools"></div><div class="clear"></div><div id="comment-46966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

