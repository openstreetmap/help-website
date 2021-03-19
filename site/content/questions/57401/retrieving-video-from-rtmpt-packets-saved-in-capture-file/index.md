+++
type = "question"
title = "Retrieving Video from RTMPT packets saved in capture file"
description = '''Hello everyone!! I&#x27;m a newbie to wireshark and was trying to figure out if I could extract/save video from live video streaming. I&#x27;m able to store/get rtmpt data packets in a PACPNG filehowever, I&#x27;m unable to extract video from those data packets...  Is there any way to extract video from pcapng fil...'''
date = "2016-11-15T19:09:00Z"
lastmod = "2016-11-16T01:20:00Z"
weight = 57401
keywords = [ "videostream", "video", "rtmpt" ]
aliases = [ "/questions/57401" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieving Video from RTMPT packets saved in capture file](/questions/57401/retrieving-video-from-rtmpt-packets-saved-in-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57401-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone!! I'm a newbie to wireshark and was trying to figure out if I could extract/save video from live video streaming. I'm able to store/get rtmpt data packets in a PACPNG filehowever, I'm unable to extract video from those data packets...</p><ol><li>Is there any way to extract video from pcapng files?</li><li>Can I directly extract video while live streaming?</li></ol><p>Thanks in advance... Cheers :)</p></div><div id="question-tags" class="tags-container tags">videostream video rtmpt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '16, 19:09</strong></p><img src="https://secure.gravatar.com/avatar/d6dabe2b53a60d847d0c1dc3b948db86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zain%20Alvi&#39;s gravatar image" /><p>Zain Alvi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zain Alvi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Nov '16, 19:41</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-57401" class="comments-container"></div><div id="comment-tools-57401" class="comment-tools"></div><div class="clear"></div><div id="comment-57401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57406"></span>

<div id="answer-container-57406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57406-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Two points to look at:</p><ul><li><p>even if you have a RTMP tunneled through http or https (which is the meaning of the last T in RTMPT), it may still be encrypted itself, making it "RTMPST"</p></li><li><p>the RTMP payload, even if you successfully extract it to a file, may be in a format which your generic player would not understand as the original player used may use some proprietary encryption or encoding or codec.</p></li></ul><p>If you are not sure regarding the above, posting an example capture file according to Step 3 of <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">this tutorial</a> (ignoring steps 1 and 2 of course) will allow others to have a look.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '16, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57406" class="comments-container"><span id="57428"></span><div id="comment-57428" class="comment"><div id="post-57428-score" class="comment-score"></div><div class="comment-text"><p>Well thanks for replying, So what i understood from your answer is that RTMPT is encrypted and payload cant be extracted. In case, payload is extracted I wont be able to play it because of video settings... The point here is that I'm running my own server and I'm playing my own video over it. However I was trying to play and save video at the same time at client end. Would that be possible in any other way?? Thank you community for helping :)</p></div><div id="comment-57428-info" class="comment-info"><span class="comment-age">(16 Nov '16, 19:18)</span> Zain Alvi</div></div><span id="57429"></span><div id="comment-57429" class="comment"><div id="post-57429-score" class="comment-score"></div><div class="comment-text"><p>I am not a lawyer working for an operating system vendor, so when I write "it may happen", it doesn't actually mean "it always happens" :-)</p><p>So if you know that you use HTTP rather than HTTPS to tunnel the RTMP, and you know that you do not encrypt the RTMP contents, and you know which codec you use and that your player understands it, you should be able to use <code>File -&gt; Export Objects -&gt; HTTP</code> and save the RTMP stream as a file - if it was complete.</p></div><div id="comment-57429-info" class="comment-info"><span class="comment-age">(16 Nov '16, 23:09)</span> sindy</div></div><span id="57445"></span><div id="comment-57445" class="comment"><div id="post-57445-score" class="comment-score"></div><div class="comment-text"><p>thanks for replying :)</p><p>Let me check and get back to you in a while...</p></div><div id="comment-57445-info" class="comment-info"><span class="comment-age">(17 Nov '16, 19:28)</span> Zain Alvi</div></div></div><div id="comment-tools-57406" class="comment-tools"></div><div class="clear"></div><div id="comment-57406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

