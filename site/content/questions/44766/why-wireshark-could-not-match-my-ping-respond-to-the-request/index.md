+++
type = "question"
title = "Why Wireshark could not match my Ping respond to the request?"
description = '''Hello i am implementing icmp on my device and made a ping to it for test. On the windows console, i got replies to all my requests. However, Wireshark sais the Ping requests 4 and 7 do not match (Echo (ping) request ... etc ... no response found).  I could not find anything wrong on my frames, what&#x27;...'''
date = "2015-08-03T05:23:00Z"
lastmod = "2015-08-03T11:07:00Z"
weight = 44766
keywords = [ "icmp", "ping", "response" ]
aliases = [ "/questions/44766" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why Wireshark could not match my Ping respond to the request?](/questions/44766/why-wireshark-could-not-match-my-ping-respond-to-the-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44766-score" class="post-score" title="current number of votes">0</div><span id="post-44766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello i am implementing icmp on my device and made a ping to it for test. On the windows console, i got replies to all my requests. However, Wireshark sais the Ping requests 4 and 7 do not match (Echo (ping) request ... etc ... no response found). I could not find anything wrong on my frames, what's more in the ICMP of the frame, Wireshark even created a link to the corresponding frame (Reply/Request).</p><p>The device is connected directly to my network kard.</p><p>This seems contradictory to me. Is this a bug in Wireshark or am i overlooking something?</p><p>I tried to prepare a .pcapng for you but then realized that on opening that file, "no response found" has dissappeared.</p><p>So here is the link to the capture, it's a txt you can load it with wireshark. On ping request 4 (frame number 9) and 7 (frame number 15) it said (no response found) in the "Info" column.</p><p><a href="https://mega.co.nz/#!w55CgTAJ!G1h8sHwn3x4gZ8ChU59BVhviKN272ydWSdjJVsbPS2U">link</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '15, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/1f0c47999f5cc5b43fbdfda32d6431e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MOd24&#39;s gravatar image" /><p><span>MOd24</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MOd24 has no accepted answers">0%</span></p></div></div><div id="comments-container-44766" class="comments-container"></div><div id="comment-tools-44766" class="comment-tools"></div><div class="clear"></div><div id="comment-44766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44767"></span>

<div id="answer-container-44767" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44767-score" class="post-score" title="current number of votes">1</div><span id="post-44767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MOd24 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So do I understand you correctly: during capture Wireshark said "no response found", but after reopening the file everything was fine? If so it looks like the "runtime" processing of frames cannot match all ping requests to replies. As long as the loading does I wouldn't complain - I guess there is a technical reason for this, usually that there is only single pass processing during capture.</p><p>BTW, please post PCAPng or PCAP files; hex dumps are not useful at all, and nobody here will spent much time on decoding it or converting it back to a useful format. Which may lead to you not getting any answer at all because it's too annoying.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44767" class="comments-container"><span id="44777"></span><div id="comment-44777" class="comment"><div id="post-44777-score" class="comment-score"></div><div class="comment-text"><p>Yes, that is exactly what i mean. Thanks for the reply. I was able to open the .txt file in Wireshark just fine. I manually removed all frames after the ping since they do not matter (therefore the txt). I just made a screenshot of Wireshark to clarify before i read your comment.</p><p>Anyway, i think it is just like you said, and only appearing on live capture, so problem solved.</p><p><a href="https://www.dropbox.com/s/e717fhps12xroa8/ping.png?dl=0">https://www.dropbox.com/s/e717fhps12xroa8/ping.png?dl=0</a></p><p>On the image, the issue appears on frame no. 3</p></div><div id="comment-44777-info" class="comment-info"><span class="comment-age">(03 Aug '15, 06:45)</span> <span class="comment-user userinfo">MOd24</span></div></div><span id="44780"></span><div id="comment-44780" class="comment"><div id="post-44780-score" class="comment-score">1</div><div class="comment-text"><p><em>only appearing on live capture, so problem solved.</em></p><p>That looks like a bug to me. I'd recommend filing a bug report. I wrote the original ICMP request/response tracking (See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5770">Bug 5770</a>), and later Ronnie Sahlberg made some changes (See commit <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=16936274786ce9b22821b4ee33b876ac5ce1fef1">16936274786ce9b22821b4ee33b876ac5ce1fef1</a>).</p><p>If you file a bug report, please include the screen capture and also CC Ronnie.</p></div><div id="comment-44780-info" class="comment-info"><span class="comment-age">(03 Aug '15, 07:18)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="44781"></span><div id="comment-44781" class="comment"><div id="post-44781-score" class="comment-score"></div><div class="comment-text"><p><span>@MOd24</span> right, I just tried, Wireshark can open that kind of file - didn't know that, so I've got my check mark for having something new learned today... :-)</p></div><div id="comment-44781-info" class="comment-info"><span class="comment-age">(03 Aug '15, 07:25)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="44794"></span><div id="comment-44794" class="comment"><div id="post-44794-score" class="comment-score"></div><div class="comment-text"><p><span>@cmaynard</span>, how do i CC Ronnie?</p></div><div id="comment-44794-info" class="comment-info"><span class="comment-age">(03 Aug '15, 09:59)</span> <span class="comment-user userinfo">MOd24</span></div></div><span id="44797"></span><div id="comment-44797" class="comment"><div id="post-44797-score" class="comment-score"></div><div class="comment-text"><p>It would appear you (or someone else) already CC'd him on the bug report.</p></div><div id="comment-44797-info" class="comment-info"><span class="comment-age">(03 Aug '15, 11:07)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-44767" class="comment-tools"></div><div class="clear"></div><div id="comment-44767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

