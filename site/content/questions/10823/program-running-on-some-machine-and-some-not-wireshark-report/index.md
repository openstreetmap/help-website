+++
type = "question"
title = "program running on some machine and some not wireshark report"
description = '''i made an application that stream an video from a live source to a particular ip address,but when i open the network stream through vlc it says unidentified format.My wireshark shows the following report:- 446 3.534718 192.168.0.1 192.168.0.2 IPv4 1314 Fragmented IP protocol (proto=UDP 0x11, off=0, ...'''
date = "2012-05-09T05:02:00Z"
lastmod = "2012-05-09T13:50:00Z"
weight = 10823
keywords = [ "udp", "wireshark", "port", "rtp" ]
aliases = [ "/questions/10823" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [program running on some machine and some not wireshark report](/questions/10823/program-running-on-some-machine-and-some-not-wireshark-report)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10823-score" class="post-score" title="current number of votes">0</div><span id="post-10823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i made an application that stream an video from a live source to a particular ip address,but when i open the network stream through vlc it says unidentified <a href="http://format.My">format.My</a> wireshark shows the following report:-</p><pre><code>446 3.534718    192.168.0.1 192.168.0.2 IPv4    1314    Fragmented IP protocol (proto=UDP 0x11, off=0, ID=164f) [Reassembled in #447]
447 3.534773    192.168.0.1 192.168.0.2 UDP 90  Source port: 18886  Destination port: 18886
448 3.534785    192.168.0.2 192.168.0.1 ICMP    190 Destination unreachable (Port unreachable)
449 3.534804    192.168.0.2 192.168.0.1 ICMP    190 Destination unreachable (Port unreachable)</code></pre><p>This program is running on some machines and not running on my machine what might be the cause of the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '12, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/cee05f82c57e924cf7bc9dd6912ad22b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tarun&#39;s gravatar image" /><p><span>tarun</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tarun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '12, 05:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10823" class="comments-container"></div><div id="comment-tools-10823" class="comment-tools"></div><div class="clear"></div><div id="comment-10823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10827"></span>

<div id="answer-container-10827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10827-score" class="post-score" title="current number of votes">0</div><span id="post-10827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"<strong>Destination unreachachble (Port unreachable)</strong>" means, that there is no service listening on UDP port (18886 ??) on the machine that reports the problem (192.168.0.2). Pleaase check that with "netstat -na" on 192.168.0.2. If it's a dynamic port, then something is wrong with your streaming config.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-10827" class="comments-container"><span id="10831"></span><div id="comment-10831" class="comment"><div id="post-10831-score" class="comment-score"></div><div class="comment-text"><p>hey Kurt Thanks for the reply,but i had an query that on machine(192.168.0.2),i ran vlc player to open network stream,so vlc player must be listening that....</p></div><div id="comment-10831-info" class="comment-info"><span class="comment-age">(09 May '12, 05:59)</span> <span class="comment-user userinfo">tarun</span></div></div><span id="10834"></span><div id="comment-10834" class="comment"><div id="post-10834-score" class="comment-score"></div><div class="comment-text"><p>and its too a static port..</p></div><div id="comment-10834-info" class="comment-info"><span class="comment-age">(09 May '12, 06:14)</span> <span class="comment-user userinfo">tarun</span></div></div><span id="10837"></span><div id="comment-10837" class="comment"><div id="post-10837-score" class="comment-score"></div><div class="comment-text"><p>did you check with 'netstat -na' ?</p></div><div id="comment-10837-info" class="comment-info"><span class="comment-age">(09 May '12, 07:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10838"></span><div id="comment-10838" class="comment"><div id="post-10838-score" class="comment-score"></div><div class="comment-text"><p>ya i checked with netstat -na and here is mine output:- (C) Copyright 1985-2001 Microsoft Corp.</p><pre><code>C:\Documents and Settings\Administrator&gt;netstat -na

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:2222           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:2226           0.0.0.0:0              LISTENING
  TCP    127.0.0.1:1025         0.0.0.0:0              LISTENING
  TCP    127.0.0.1:1796         127.0.0.1:2226         TIME_WAIT
  TCP    127.0.0.1:1797         127.0.0.1:2226         TIME_WAIT
  TCP    127.0.0.1:2227         0.0.0.0:0              LISTENING
  TCP    127.0.0.1:2228         0.0.0.0:0              LISTENING
  TCP    127.0.0.1:5152         0.0.0.0:0              LISTENING
  TCP    192.168.0.2:139        0.0.0.0:0              LISTENING
  UDP    0.0.0.0:445            *:*
  UDP    127.0.0.1:123          *:*
  UDP    192.168.0.2:123        *:*
  UDP    192.168.0.2:137        *:*
  UDP    192.168.0.2:138        *:*

C:\Documents and Settings\Administrator&gt;</code></pre></div><div id="comment-10838-info" class="comment-info"><span class="comment-age">(09 May '12, 07:32)</span> <span class="comment-user userinfo">tarun</span></div></div><span id="10852"></span><div id="comment-10852" class="comment"><div id="post-10852-score" class="comment-score"></div><div class="comment-text"><p>I don't see udp port 18886, so there is no process 'accepting data' on that port. I really think this is a VLC config problem.</p></div><div id="comment-10852-info" class="comment-info"><span class="comment-age">(09 May '12, 13:50)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-10827" class="comment-tools"></div><div class="clear"></div><div id="comment-10827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

