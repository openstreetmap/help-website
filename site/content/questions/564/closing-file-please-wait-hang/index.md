+++
type = "question"
title = "Closing file please wait - hang"
description = '''I am running 1.4.1 on Win 7 x64 laptop with 4G ram.  Packet capture as follows: Limit each packet to 150 bytes Use multiple files Ring buffer - 20 files Buffer size - 300 megabytes Update list of packets in real time - unchecked Automatic scrolling in live capture - unchecked Enable MAC name resolut...'''
date = "2010-10-20T12:09:00Z"
lastmod = "2011-08-04T18:56:00Z"
weight = 564
keywords = [ "hang", "windows7", "crash" ]
aliases = [ "/questions/564" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Closing file please wait - hang](/questions/564/closing-file-please-wait-hang)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-564-score" class="post-score" title="current number of votes">1</div><span id="post-564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running 1.4.1 on Win 7 x64 laptop with 4G ram.</p><p>Packet capture as follows:</p><p>Limit each packet to 150 bytes Use multiple files Ring buffer - 20 files</p><p>Buffer size - 300 megabytes Update list of packets in real time - unchecked Automatic scrolling in live capture - unchecked</p><p>Enable MAC name resolution - checked Enable network name resolution - unchecked Enable transport name resolution - checked</p><p>About 4 or 5 files in, I see several instances of the badly formed window with "Closing file please wait". If I close the multiple windows, wireshark starts capturing packets again.</p><p>This problem seems very similiar to this old bug <a href="http://ipv4.wireshark.org/lists/wireshark-bugs/200903/msg00223.html">http://ipv4.wireshark.org/lists/wireshark-bugs/200903/msg00223.html</a></p><p>Anyone have any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hang" rel="tag" title="see questions tagged &#39;hang&#39;">hang</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '10, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/4accd5688e2fcad7ef1e2136c07f4c47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ramasan&#39;s gravatar image" /><p><span>ramasan</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ramasan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Aug '11, 15:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-564" class="comments-container"><span id="5513"></span><div id="comment-5513" class="comment"><div id="post-5513-score" class="comment-score"></div><div class="comment-text"><p>Next file every ??? I rolled every 100K, just as an example. Any capture filter? I did not specify one. The system I am currently running on only has 2GB of RAM so I was not able to use a 300MB Buffer size. Instead Wireshark set it to the default of 1MB. Running with 1.6.1 with these settings, I did not experience this problem. Can you try with version 1.6.1?</p></div><div id="comment-5513-info" class="comment-info"><span class="comment-age">(04 Aug '11, 18:56)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-564" class="comment-tools"></div><div class="clear"></div><div id="comment-564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="575"></span>

<div id="answer-container-575" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-575-score" class="post-score" title="current number of votes">0</div><span id="post-575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Same problem here. The worst part is that I'm capturing with 10 wireshark instances 10 remote daemons and after a couple of hours when I close the capture it opens 150 "closing file" instances and crashes my windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '10, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/d3439144f4810a1b7813b18d35d55993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mreg&#39;s gravatar image" /><p><span>mreg</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mreg has no accepted answers">0%</span></p></div></div><div id="comments-container-575" class="comments-container"></div><div id="comment-tools-575" class="comment-tools"></div><div class="clear"></div><div id="comment-575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

