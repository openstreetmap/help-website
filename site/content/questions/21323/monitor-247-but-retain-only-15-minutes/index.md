+++
type = "question"
title = "monitor 24/7 but retain only 15 minutes?"
description = '''I need to investigate a problem I am having with my phone system. However the problem cannot be reproduced intentionally so I there is no way that I can plan ahead to capture traffic. Is it possible to leave wireshark on 24/7 but only keep a specified amount of transactions, or say even like 20 minu...'''
date = "2013-05-20T11:36:00Z"
lastmod = "2013-06-03T15:16:00Z"
weight = 21323
keywords = [ "voip" ]
aliases = [ "/questions/21323" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [monitor 24/7 but retain only 15 minutes?](/questions/21323/monitor-247-but-retain-only-15-minutes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21323-score" class="post-score" title="current number of votes">0</div><span id="post-21323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to investigate a problem I am having with my phone system. However the problem cannot be reproduced intentionally so I there is no way that I can plan ahead to capture traffic.</p><p>Is it possible to leave wireshark on 24/7 but only keep a specified amount of transactions, or say even like 20 minutes of data? This way when the problem does occur again, I will have a capture of hopefully, of what's going down.</p><p>Thanks Robbie</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '13, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/87fc30d7b1bbbb4a2c7df57aabf071c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobbieRobski&#39;s gravatar image" /><p><span>RobbieRobski</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobbieRobski has no accepted answers">0%</span></p></div></div><div id="comments-container-21323" class="comments-container"></div><div id="comment-tools-21323" class="comment-tools"></div><div class="clear"></div><div id="comment-21323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21326"></span>

<div id="answer-container-21326" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21326-score" class="post-score" title="current number of votes">6</div><span id="post-21326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RobbieRobski has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can use dumpcap with a ring buffer of files.</p><blockquote><p><code>dumpcap -ni 1 -w c:\temp\phone_problem.pcap -b duration:1200 -b files:5</code><br />
</p></blockquote><p>This will create a new capture file every 20 minutes (1200 Seconds). It will rotate the capture files, keeping only the latest five. For more help, see <code>dumpcap -h</code>. Please replace the interface number with whatever is appropriate on your system. The following command will show you the interfaces.</p><blockquote><p><code>dumpcap -D -M</code><br />
</p></blockquote><p>BTW: You cannot do this with Wireshark for a long time, as it's memory consumption will constantly grow (accumulation of internal data structures), which is not the case with dumpcap.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 May '13, 12:08</strong> </span></p></div></div><div id="comments-container-21326" class="comments-container"><span id="21360"></span><div id="comment-21360" class="comment"><div id="post-21360-score" class="comment-score"></div><div class="comment-text"><p>Thanks!! I really hope the problem occurs during these logs so I can squash this problem once and for all.</p></div><div id="comment-21360-info" class="comment-info"><span class="comment-age">(21 May '13, 15:56)</span> <span class="comment-user userinfo">RobbieRobski</span></div></div><span id="21720"></span><div id="comment-21720" class="comment"><div id="post-21720-score" class="comment-score"></div><div class="comment-text"><p>So far no luck with my pbx vendor, they're passing the buck to phone hardware. I just got a nibble from a cisco employee via forum post for me to send the logs so hopefully this will get solved!</p></div><div id="comment-21720-info" class="comment-info"><span class="comment-age">(03 Jun '13, 15:16)</span> <span class="comment-user userinfo">RobbieRobski</span></div></div></div><div id="comment-tools-21326" class="comment-tools"></div><div class="clear"></div><div id="comment-21326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21325"></span>

<div id="answer-container-21325" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21325-score" class="post-score" title="current number of votes">0</div><span id="post-21325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I hope wireshark ring buffer feature will be your savior/.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span> </br></p></div></div><div id="comments-container-21325" class="comments-container"><span id="21327"></span><div id="comment-21327" class="comment"><div id="post-21327-score" class="comment-score"></div><div class="comment-text"><p>also see <a href="http://ask.wireshark.org/questions/14745/long-term-capture">http://ask.wireshark.org/questions/14745/long-term-capture</a></p></div><div id="comment-21327-info" class="comment-info"><span class="comment-age">(20 May '13, 11:47)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-21325" class="comment-tools"></div><div class="clear"></div><div id="comment-21325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

