+++
type = "question"
title = "Play VIDEO - RTP packets"
description = '''Hi! I have a doubt. I am sniffing RTP packets from a IP camera. WireShark shows the RTP packets (payload type 96) in the capture. Is there any way to re-play those packets once it has been captured? I mean, I want to sniff some rtp data of a ip camera with videostreamming, and after that, play te vi...'''
date = "2016-08-10T10:29:00Z"
lastmod = "2016-08-10T11:44:00Z"
weight = 54723
keywords = [ "videostream", "rtp", "ipcamera" ]
aliases = [ "/questions/54723" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Play VIDEO - RTP packets](/questions/54723/play-video-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54723-score" class="post-score" title="current number of votes">0</div><span id="post-54723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I have a doubt. I am sniffing RTP packets from a IP camera. WireShark shows the RTP packets (payload type 96) in the capture. Is there any way to re-play those packets once it has been captured? I mean, I want to sniff some rtp data of a ip camera with videostreamming, and after that, play te video captured.</p><p>Thanks,</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-videostream" rel="tag" title="see questions tagged &#39;videostream&#39;">videostream</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-ipcamera" rel="tag" title="see questions tagged &#39;ipcamera&#39;">ipcamera</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '16, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/dd2ab8306fed22feed7aa6232c839454?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="avatarreturn&#39;s gravatar image" /><p><span>avatarreturn</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="avatarreturn has no accepted answers">0%</span></p></div></div><div id="comments-container-54723" class="comments-container"></div><div id="comment-tools-54723" class="comment-tools"></div><div class="clear"></div><div id="comment-54723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54724"></span>

<div id="answer-container-54724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54724-score" class="post-score" title="current number of votes">0</div><span id="post-54724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on what you mean by re-play.</p><ul><li><p>If you expect Wireshark to play the video from the camera, then the answer is currently no.</p></li><li><p>If you want to replay the captured packets to an application or hardware which can show an incoming video stream live, then it is still not a task for Wireshark or tshark, but there are tools which can replay capture files saved by Wireshark (or other application which can save a pcap formatted file). However, you'll need to complement the RTP stream with some control protocol which the video application supports, so that you could inform it what video codec to expect etc. To my knowledge, there are two options how to do this. You can use <a href="http://sipp.sourceforge.net/doc3.3/reference.html">SIPp</a> which allows you to control the video session using SIP (and no other protocol) and play only the RTP from a pcap file, or you can use <a href="http://tcpreplay.synfin.net/wiki/manual">tcpreplay</a> which would need a pre-captured and modified control session (in any protocol but lacking any interactivity, i.e. the video playing application would have to expect the RTP to come to a predictable port so that you could ask tcpreplay to modify the packet headers accordingly).</p></li></ul><p>Or there is yet another chance: to repack the payload from the RTP packets to some media file format like Ogg which can be played by video file player such as VLC media player. That, however, requires some coding in [your favourite programming language], or filing an enhancement request at WIreshark bugzilla.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '16, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Aug '16, 12:06</strong> </span></p></div></div><div id="comments-container-54724" class="comments-container"></div><div id="comment-tools-54724" class="comment-tools"></div><div class="clear"></div><div id="comment-54724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

