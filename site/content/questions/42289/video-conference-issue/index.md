+++
type = "question"
title = "video conference issue"
description = '''Hi, I have no experience using Wireshark and in packet analysis, which I&#x27;ll start studying because having such skills are valuable. I want to know if it could be used to troubleshoot a web based video conference issue occurring in one of our sites. The video and audio are becoming choppier as more p...'''
date = "2015-05-10T16:34:00Z"
lastmod = "2015-05-12T06:16:00Z"
weight = 42289
keywords = [ "videoconference" ]
aliases = [ "/questions/42289" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [video conference issue](/questions/42289/video-conference-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42289-score" class="post-score" title="current number of votes">0</div><span id="post-42289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have no experience using Wireshark and in packet analysis, which I'll start studying because having such skills are valuable. I want to know if it could be used to troubleshoot a web based video conference issue occurring in one of our sites. The video and audio are becoming choppier as more participants join the session. The site has DOWN:100Mbps/UP:5Mbps Internet connection with no QoS configuration and the participants are connecting most of the time from home.</p><p>I can set a packet capture on the host that initiates the video conference session or on the intermediate network devices if that is more preferred. I would greatly appreciate it if someone can provide step-by-step guides what to look for in the packet capture and if there's any customization or configuration needed in Wireshark to troubleshoot this kind of issue..</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-videoconference" rel="tag" title="see questions tagged &#39;videoconference&#39;">videoconference</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '15, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/b657a24f4ac373df3ca8e4925d529564?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zombietek&#39;s gravatar image" /><p><span>zombietek</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zombietek has no accepted answers">0%</span></p></div></div><div id="comments-container-42289" class="comments-container"></div><div id="comment-tools-42289" class="comment-tools"></div><div class="clear"></div><div id="comment-42289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42299"></span>

<div id="answer-container-42299" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42299-score" class="post-score" title="current number of votes">0</div><span id="post-42299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Going in at the deep end, are you? Why not start with something mundane, like <a href="https://wiki.wireshark.org/SampleCaptures">sample captures</a>, or <a href="http://wiresharkbook.com">a study guide</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '15, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42299" class="comments-container"><span id="42325"></span><div id="comment-42325" class="comment"><div id="post-42325-score" class="comment-score"></div><div class="comment-text"><p>Not really being thrown into the deep end. I am looking for options tools wise to get to the bottom of the issue though the vendor is also checking things on its end.</p></div><div id="comment-42325-info" class="comment-info"><span class="comment-age">(12 May '15, 05:31)</span> <span class="comment-user userinfo">zombietek</span></div></div><span id="42327"></span><div id="comment-42327" class="comment"><div id="post-42327-score" class="comment-score"></div><div class="comment-text"><p>If the conferencing tool uses the central system as a "hub" for all participants, the bottleneck will the the 5 Mbit/s! Did you take that into consideration?</p></div><div id="comment-42327-info" class="comment-info"><span class="comment-age">(12 May '15, 06:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-42299" class="comment-tools"></div><div class="clear"></div><div id="comment-42299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

