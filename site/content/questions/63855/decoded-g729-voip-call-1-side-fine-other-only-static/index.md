+++
type = "question"
title = "Decoded g729 Voip call. 1 side fine other only static"
description = '''Hi, I am troubleshooting call quality issues for a site using g729. I followed https://wiki.wireshark.org/HowToDecodeG729 and https://wiki.freepbx.org/display/PC/How+to+decode+and+playback+G.729+audio+streams (Followed this one worked for my side of the stream) For my side of the RTP stream I was ab...'''
date = "2017-10-12T13:42:00Z"
lastmod = "2017-10-18T10:06:00Z"
weight = 63855
keywords = [ "g729", "voip", "call_audio" ]
aliases = [ "/questions/63855" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decoded g729 Voip call. 1 side fine other only static](/questions/63855/decoded-g729-voip-call-1-side-fine-other-only-static)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63855-score" class="post-score" title="current number of votes">0</div><span id="post-63855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am troubleshooting call quality issues for a site using g729. I followed <a href="https://wiki.wireshark.org/HowToDecodeG729">https://wiki.wireshark.org/HowToDecodeG729</a> and <a href="https://wiki.freepbx.org/display/PC/How+to+decode+and+playback+G.729+audio+streams">https://wiki.freepbx.org/display/PC/How+to+decode+and+playback+G.729+audio+streams</a> (Followed this one worked for my side of the stream)</p><p>For my side of the RTP stream I was able to get everything decoded and it came through fine. For their side of the RTP stream it came out to pure static. This isn't what I heard during the actual call.</p><p>I started the pcap before the call so wireshark gets the SIP signalling. Wireshark sees both rtp streams clearly.</p><p>Any insight shared is appreciated.</p><p>edit: The audio file I got from the other rtp stream ended up about twice as long as my side's rtp.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-g729" rel="tag" title="see questions tagged &#39;g729&#39;">g729</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-call_audio" rel="tag" title="see questions tagged &#39;call_audio&#39;">call_audio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '17, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/b457c5b47bfe9186f3fa57045c99d238?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hIGH_aND_mIGHTY&#39;s gravatar image" /><p><span>hIGH_aND_mIGHTY</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hIGH_aND_mIGHTY has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Oct '17, 14:34</strong> </span></p></div></div><div id="comments-container-63855" class="comments-container"></div><div id="comment-tools-63855" class="comment-tools"></div><div class="clear"></div><div id="comment-63855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63872"></span>

<div id="answer-container-63872" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63872-score" class="post-score" title="current number of votes">1</div><span id="post-63872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hIGH_aND_mIGHTY has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would say <a href="https://ask.wireshark.org/questions/63646/g729-issues-with-reverse-audio">this recent question</a> is relevant. To me it seems that the decoder recommended above has some issues, causing it to interpret some streams worse than others. The decoder which is part of Wireshark's RTP player provides better results, but to date it is only available in a development version of Wireshark (2.5.x).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '17, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63872" class="comments-container"><span id="64012"></span><div id="comment-64012" class="comment"><div id="post-64012-score" class="comment-score"></div><div class="comment-text"><p>This took care of my question. Thank you for responding.</p></div><div id="comment-64012-info" class="comment-info"><span class="comment-age">(18 Oct '17, 09:56)</span> <span class="comment-user userinfo">hIGH_aND_mIGHTY</span></div></div><span id="64013"></span><div id="comment-64013" class="comment"><div id="post-64013-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/43746/high_and_mighty">@hIGH_aND_mIGHTY</a></p><p>I've converted the comment from <a href="https://ask.wireshark.org/users/19586/sindy">@sindy</a> to an answer. As it seems to have solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer.</p></div><div id="comment-64013-info" class="comment-info"><span class="comment-age">(18 Oct '17, 10:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-63872" class="comment-tools"></div><div class="clear"></div><div id="comment-63872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

