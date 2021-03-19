+++
type = "question"
title = "[closed] TFTP windowing not working"
description = '''Hi I&#x27;m using TFTP to transfer a 300mb boot file over a wan link as part of an Operating System Deployment solution. The file is hosted on a Windows 2012 server. It takes about 20 minutes to transfer the file. A packet trace revealed that the client was ACK&#x27;ing every block. Whilst I know that this us...'''
date = "2014-07-01T01:55:00Z"
lastmod = "2014-07-01T07:28:00Z"
weight = 34310
keywords = [ "tftp", "slow", "windowing" ]
aliases = [ "/questions/34310" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] TFTP windowing not working](/questions/34310/tftp-windowing-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34310-score" class="post-score" title="current number of votes">0</div><span id="post-34310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm using TFTP to transfer a 300mb boot file over a wan link as part of an Operating System Deployment solution.</p><p>The file is hosted on a Windows 2012 server. It takes about 20 minutes to transfer the file. A packet trace revealed that the client was ACK'ing every block. Whilst I know that this use to be normal for TFTP since Windows Server 08 the default value for Windowing is 4.</p><p>Does anyone have any idea why this might be happening or suggest any troubleshooting ideas?</p><p>Cheers</p><p>Alex</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tftp" rel="tag" title="see questions tagged &#39;tftp&#39;">tftp</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-windowing" rel="tag" title="see questions tagged &#39;windowing&#39;">windowing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '14, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/3dae5cbcca8fe70d5431e9d8ba7f8397?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="troubleshootist&#39;s gravatar image" /><p><span>troubleshootist</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="troubleshootist has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>01 Jul '14, 06:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-34310" class="comments-container"><span id="34315"></span><div id="comment-34315" class="comment"><div id="post-34315-score" class="comment-score"></div><div class="comment-text"><p>Some questions:</p><ul><li>what is your TFTP client (OS and OS version)</li><li>what is the RTT of the WAN link</li><li>what is the available bandwidth of the WAN link</li><li>can you post a sample capture file on google drive, dropbox or cloudshark.org, <strong>including the first 100 frames</strong> of the session</li></ul></div><div id="comment-34315-info" class="comment-info"><span class="comment-age">(01 Jul '14, 04:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="34320"></span><div id="comment-34320" class="comment"><div id="post-34320-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>the client is PXE booting so it has no meaningful OS at the time of the download. All the TFTP setting are dictated by the BSD on the server.</p><p>The RTT is about 12ms</p><p>I can't post a capture file but here is a screen shot. As you can see every block is being Ack'ed</p><p><img src="https://osqa-ask.wireshark.org/upfiles/block.png" alt="alt text" /></p></div><div id="comment-34320-info" class="comment-info"><span class="comment-age">(01 Jul '14, 06:12)</span> <span class="comment-user userinfo">troubleshootist</span></div></div></div><div id="comment-tools-34310" class="comment-tools"></div><div class="clear"></div><div id="comment-34310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Jaap 01 Jul '14, 06:31

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34321"></span>

<div id="answer-container-34321" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34321-score" class="post-score" title="current number of votes">0</div><span id="post-34321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>A packet trace revealed that the client was ACK'ing every block.</p></blockquote><p>As you said, TFTP requires every data block to be ACKed before the next block can be sent.</p><p><a href="http://tools.ietf.org/html/rfc1350">http://tools.ietf.org/html/rfc1350</a></p><pre><code>2. Overview of the Protocol
   ....
   length blocks of 512 bytes.  Each data packet contains one block of
   data, and must be acknowledged by an acknowledgment packet before the
   next packet can be sent.</code></pre><p>There are TFTP Extension options to change the block size, which will have an effect on the number of ACKs as well.</p><blockquote><p><a href="http://tools.ietf.org/html/rfc2348">http://tools.ietf.org/html/rfc2348</a></p></blockquote><p>However, that's an option the client requests and which the server must accept. In your example the blocksize is 1456 bytes. There are speed tests in the RFC mentioned above, that show tremendous performance gains by using larger block sizes (8K). This will especially help on a WAN link.</p><p>So, this is a config issue of the TFTP client in your PXE implementation on the client system and not related to the network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '14, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-34321" class="comments-container"><span id="34323"></span><div id="comment-34323" class="comment"><div id="post-34323-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt</p><p>you're right that the original implementation of TFTP reacquired every block to be ACK'ed before another was sent. However from Windows server 08 you can set a Window size so that not every block has to be ACK'ed immediately. The default is now set to 4, so that 4 blocks can be set before the client has to ACK them all. The windowing size is set in the BCD on te server and when I query it, it tells me the block size is 4.</p><p>We tried up'ing the block size but it made it grind to a halt. There's obviously a bit of network kit that doens't like alrge blocks and stops them ,so the Windowing issue seems to be the way to attach this problem.</p><p>Cheers</p><p>Alex</p></div><div id="comment-34323-info" class="comment-info"><span class="comment-age">(01 Jul '14, 07:28)</span> <span class="comment-user userinfo">troubleshootist</span></div></div></div><div id="comment-tools-34321" class="comment-tools"></div><div class="clear"></div><div id="comment-34321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

