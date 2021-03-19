+++
type = "question"
title = "wireshark selectively displaying packets?"
description = '''I have noticed that when I am sending/receiving &#x27;too many&#x27; packets through my interface, that some don&#x27;t get displayed in wireshark, but I know that they are being transmitted. For example, once that I started receiving many UDP packets, my ping that was running in the background didn&#x27;t show up in w...'''
date = "2014-03-23T04:50:00Z"
lastmod = "2014-04-07T02:36:00Z"
weight = 31091
keywords = [ "virtual-jamming" ]
aliases = [ "/questions/31091" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark selectively displaying packets?](/questions/31091/wireshark-selectively-displaying-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31091-score" class="post-score" title="current number of votes">0</div><span id="post-31091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have noticed that when I am sending/receiving 'too many' packets through my interface, that some don't get displayed in wireshark, but I know that they are being transmitted. For example, once that I started receiving many UDP packets, my ping that was running in the background didn't show up in wireshark, yet was successfully comunicating in the background. What is the reason for this, and how can I make sure that I know <em>all</em> what is being communicated between two devices?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-virtual-jamming" rel="tag" title="see questions tagged &#39;virtual-jamming&#39;">virtual-jamming</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '14, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/2cd7abf8008d63d7e08f46aa75bff063?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itrustedyou&#39;s gravatar image" /><p><span>itrustedyou</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itrustedyou has no accepted answers">0%</span></p></div></div><div id="comments-container-31091" class="comments-container"></div><div id="comment-tools-31091" class="comment-tools"></div><div class="clear"></div><div id="comment-31091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31095"></span>

<div id="answer-container-31095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31095-score" class="post-score" title="current number of votes">1</div><span id="post-31095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try increasing the buffer size in the capture options and don't use Update list of packets in real time.</p><p>Please read <a href="http://wiki.wireshark.org/Performance">http://wiki.wireshark.org/Performance</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '14, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-31095" class="comments-container"><span id="31127"></span><div id="comment-31127" class="comment"><div id="post-31127-score" class="comment-score"></div><div class="comment-text"><p>This is useful info, but I still don't receive many packets that I know are being transmitted, even with this option!</p></div><div id="comment-31127-info" class="comment-info"><span class="comment-age">(24 Mar '14, 11:13)</span> <span class="comment-user userinfo">itrustedyou</span></div></div><span id="31131"></span><div id="comment-31131" class="comment"><div id="post-31131-score" class="comment-score"></div><div class="comment-text"><p>Have you also tried increasing the buffer size when capturing with dumpcap?</p><p>You can use a hardware based capture device if you need to see everything. There was a presentation about capture drops at SharkFest 2013 - PA-05</p><p><a href="http://sharkfest.wireshark.org/sharkfest.13/index.html">http://sharkfest.wireshark.org/sharkfest.13/index.html</a></p></div><div id="comment-31131-info" class="comment-info"><span class="comment-age">(24 Mar '14, 13:12)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="31592"></span><div id="comment-31592" class="comment"><div id="post-31592-score" class="comment-score"></div><div class="comment-text"><p>ok just saw this. Wow, that sharkfest looks damn cool. I'll look at the presentation in the next couple of days. Thank you!!</p></div><div id="comment-31592-info" class="comment-info"><span class="comment-age">(07 Apr '14, 02:36)</span> <span class="comment-user userinfo">itrustedyou</span></div></div></div><div id="comment-tools-31095" class="comment-tools"></div><div class="clear"></div><div id="comment-31095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31097"></span>

<div id="answer-container-31097" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31097-score" class="post-score" title="current number of votes">1</div><span id="post-31097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Best capture performance is achieved by not using Wireshark to capture the data, but to run dumpcap on a command line. Dumpcap is the tool that Wireshark uses to capture packets and re-reads the file constantly. If you need maximum capture performance it is best to avoid using Wireshark while dumpcap is capturing. You can find dumpcap in the Wireshark installation directory.</p><p>Use "dumpcap -D" to get a list of available capture interfaces and their indexes, then run "dumpcap -i [interfaceindex] -w [filename]" to capture on the interface you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '14, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31097" class="comments-container"><span id="31126"></span><div id="comment-31126" class="comment"><div id="post-31126-score" class="comment-score"></div><div class="comment-text"><p>Ok, I have done this, but still I see only one packet(this is an improvement though) from ping, while I know that many are being transmitted back and forth. I don't know what else I can do?</p></div><div id="comment-31126-info" class="comment-info"><span class="comment-age">(24 Mar '14, 11:11)</span> <span class="comment-user userinfo">itrustedyou</span></div></div></div><div id="comment-tools-31097" class="comment-tools"></div><div class="clear"></div><div id="comment-31097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

