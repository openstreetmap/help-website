+++
type = "question"
title = "Real Time Capture Video Stream"
description = '''Hello, I am doing performing research in particular the security vulnerabilities of of Parrot Drone 2.0. When performing a man in the middle attack using ettercap, we can use Wireshark (Graphival mode) and I can recreate the video stream (Filtering TCP 5555) post event. Easy enough and we can replay...'''
date = "2016-04-29T19:20:00Z"
lastmod = "2016-04-29T19:20:00Z"
weight = 52092
keywords = [ "mitm", "decoding", "ettercap", "stream", "real-time" ]
aliases = [ "/questions/52092" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Real Time Capture Video Stream](/questions/52092/real-time-capture-video-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52092-score" class="post-score" title="current number of votes">0</div><span id="post-52092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am doing performing research in particular the security vulnerabilities of of Parrot Drone 2.0. When performing a man in the middle attack using ettercap, we can use Wireshark (Graphival mode) and I can recreate the video stream (Filtering TCP 5555) post event. Easy enough and we can replay the h264 video using ffmpeg. Our next task is to perform real time man in the middle attack, which requires us to have real time access to the video feed from the Parrot Drone 2 to the controller (such as an iPad).<br />
If we use just ettercap to perform a mitm attack, we can saved the file to a named pipe and play it through ffmpeg, we can get something that resembles a video but because its a raw file with no filtering, its just really not properly decoded by mpeg. That because we are not filtering for the tcp 5555 connection (which we did in the first pert of experiment using Wireshark). In the first part, after using ettercap to perform an mitm, I can recreate it post event. Can I do this in real time. That is play the tcp 5555 in real time? I know that there is tshark and this might help but we are just really stuck on this task at the moment.<br />
I'm sure this is achievable using Tshark or Wireshark, any ehlp or suggestion would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mitm" rel="tag" title="see questions tagged &#39;mitm&#39;">mitm</span> <span class="post-tag tag-link-decoding" rel="tag" title="see questions tagged &#39;decoding&#39;">decoding</span> <span class="post-tag tag-link-ettercap" rel="tag" title="see questions tagged &#39;ettercap&#39;">ettercap</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-real-time" rel="tag" title="see questions tagged &#39;real-time&#39;">real-time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '16, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/caee4da3afe707dd184f806fedead31b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dr%20Dre&#39;s gravatar image" /><p><span>Dr Dre</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dr Dre has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-52092" class="comments-container"></div><div id="comment-tools-52092" class="comment-tools"></div><div class="clear"></div><div id="comment-52092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

