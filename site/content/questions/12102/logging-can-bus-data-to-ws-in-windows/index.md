+++
type = "question"
title = "Logging CAN bus data to WS in Windows"
description = '''I&#x27;d like to add CAN bus support to Wireshark under Windows (unfortunately), and I&#x27;m hoping someone can give me an idea where to start. WS currently has a dissector for CAN (Controller Area Network) data - but I&#x27;m assuming that the source of the data is from the socketcan library (is that correct?) w...'''
date = "2012-06-21T02:17:00Z"
lastmod = "2012-06-22T01:01:00Z"
weight = 12102
keywords = [ "windows", "winpcap", "can", "wireshark" ]
aliases = [ "/questions/12102" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Logging CAN bus data to WS in Windows](/questions/12102/logging-can-bus-data-to-ws-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12102-score" class="post-score" title="current number of votes">1</div><span id="post-12102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to add CAN bus support to Wireshark under Windows (unfortunately), and I'm hoping someone can give me an idea where to start.</p><p>WS currently has a dissector for CAN (Controller Area Network) data - but I'm assuming that the source of the data is from the socketcan library (is that correct?) which is a patch to the Linux sockets stack.</p><p>I've got a USB CAN interface with a Windows driver, so I can get the live data very easily, but I'm trying to work out the best way to get that data into WS.<br />
1. Should I be attempting to write my own driver, to pass the data to WS?<br />
2. Is it a better idea to try to modify WinPCAP to collect the CAN data?<br />
3. Am I trying to do something really dumb? As a newbie to WS (although not to programming), should I give up?<br />
</p><p>Any pointers gratefully accepted.</p><p>Thanks, Jon.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-can" rel="tag" title="see questions tagged &#39;can&#39;">can</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '12, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/e9ddf5046ef4fe346849deb82837dd5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonmills&#39;s gravatar image" /><p><span>jonmills</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonmills has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '12, 02:18</strong> </span></p></div></div><div id="comments-container-12102" class="comments-container"></div><div id="comment-tools-12102" class="comment-tools"></div><div class="clear"></div><div id="comment-12102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12126"></span>

<div id="answer-container-12126" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12126-score" class="post-score" title="current number of votes">1</div><span id="post-12126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jonmills has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm assuming that the source of the data is from the socketcan library (is that correct?)</p></blockquote><p>Yes, there is a dissector that uses SocketCAN. It's defined in the file: <strong><code>epan/packet-socketcan.c</code></strong>.</p><p>If you have to ability to write a driver, I would go that way on Windows, as there is no direct USB sniffer support right now (on windows).</p><p>One idea, would be to allow wireshark to read from a pipe. Your driver would access the CAN bus via USB and provide the data through a pipe. If you provide the data in a from the SocketCAN dissector understands (not sure if that's easy or even possible), you might be able to re-use that dissector.</p><p>Take a look at <a href="http://freaklabs.org/index.php/WSBridge.html">Wsbridge</a> (<a href="http://freaklabs.org/index.php/Tutorials/Software/Feeding-the-Shark-Turning-the-Freakduino-into-a-Realtime-Wireless-Protocol-Analyzer-with-Wireshark.html">Article about WSbridge</a>) for an example of a disscetor with pipe support. You could do something similar.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '12, 23:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jun '12, 01:01</strong> </span></p></div></div><div id="comments-container-12126" class="comments-container"><span id="12127"></span><div id="comment-12127" class="comment"><div id="post-12127-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, I'll take a look at the named pipe idea.</p></div><div id="comment-12127-info" class="comment-info"><span class="comment-age">(22 Jun '12, 01:01)</span> <span class="comment-user userinfo">jonmills</span></div></div></div><div id="comment-tools-12126" class="comment-tools"></div><div class="clear"></div><div id="comment-12126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

