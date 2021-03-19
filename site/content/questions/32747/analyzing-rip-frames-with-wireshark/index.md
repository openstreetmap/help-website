+++
type = "question"
title = "Analyzing RIP frames with Wireshark"
description = '''Hi, I do not capture RIP packets from Wireshark. It is very important for me to show RIP packet contents to our students. Is there any solution to see RIP packets from Wireshark or Can I download some library? Thank you so much.'''
date = "2014-05-13T00:11:00Z"
lastmod = "2014-05-13T15:48:00Z"
weight = 32747
keywords = [ "capture-filter", "rip" ]
aliases = [ "/questions/32747" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Analyzing RIP frames with Wireshark](/questions/32747/analyzing-rip-frames-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32747-score" class="post-score" title="current number of votes">0</div><span id="post-32747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I do not capture RIP packets from Wireshark.</p><p>It is very important for me to show RIP packet contents to our students.</p><p>Is there any solution to see RIP packets from Wireshark or Can I download some library?</p><p>Thank you so much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-rip" rel="tag" title="see questions tagged &#39;rip&#39;">rip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '14, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/5667e1c088bae3d2fb830c09cc542432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gokhan%20Akyol&#39;s gravatar image" /><p><span>Gokhan Akyol</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gokhan Akyol has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '14, 01:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-32747" class="comments-container"></div><div id="comment-tools-32747" class="comment-tools"></div><div class="clear"></div><div id="comment-32747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32751"></span>

<div id="answer-container-32751" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32751-score" class="post-score" title="current number of votes">0</div><span id="post-32751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there any solution to see RIP packets from Wireshark or Can I download some library?</p></blockquote><p>Well, Wireshark support RIP. So, yes you can show the content of RIP frames to your students.</p><p>You can download a RIP sample capture file from here:</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=RIP_v1">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=RIP_v1</a></p></blockquote><p>Please save the file as <strong>RIP_v1.pcap</strong> and then open it in Wireshark.</p><p>Other sample capture files:</p><blockquote><p><a href="http://packetlife.net/captures/protocol/rip/">http://packetlife.net/captures/protocol/rip/</a><br />
<a href="http://uluru.ee.unsw.edu.au/~tim/zoo/#RIP">http://uluru.ee.unsw.edu.au/~tim/zoo/#RIP</a><br />
</p></blockquote><p><strong>++ UPDATE ++</strong></p><p>BTW: Based on your tag "capture-filter RIP" I'm not quite sure, if you are having a problem capturing RIP frames or if you needed just a sample capture file.</p><p>Capture filter: <strong>udp port 520</strong><br />
Sample captures: see above<br />
</p><p>Please comment on my answer if you need something different.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '14, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '14, 01:46</strong> </span></p></div></div><div id="comments-container-32751" class="comments-container"><span id="32752"></span><div id="comment-32752" class="comment"><div id="post-32752-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for quick response.</p><p>I have one more question. While packets are flowing in Wireshark, is there any chance to catch or capture RIP packets?</p><p>Thanks for interests</p></div><div id="comment-32752-info" class="comment-info"><span class="comment-age">(13 May '14, 02:44)</span> <span class="comment-user userinfo">Gokhan Akyol</span></div></div><span id="32770"></span><div id="comment-32770" class="comment"><div id="post-32770-score" class="comment-score"></div><div class="comment-text"><p>Wireshark will 'catch' whatever packets it sees while the capture is running. If you want to filter for only RIP, you can either use a capture filter of "udp port 520 or udp port 521" or you can use a display filter of "rip||ripng".</p><p>Consult the Wireshark user guide if you're not familiar with the terms "display filter" and "capture filter" here: <a href="http://www.wireshark.org/docs/wsug_html_chunked/">http://www.wireshark.org/docs/wsug_html_chunked/</a></p></div><div id="comment-32770-info" class="comment-info"><span class="comment-age">(13 May '14, 15:48)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-32751" class="comment-tools"></div><div class="clear"></div><div id="comment-32751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

