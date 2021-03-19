+++
type = "question"
title = "Troubleshooting Write AndX Response and Request"
description = '''We are having an issue where moving files from one office to another is drastically different. If the file is in office X, and I am transferring it to office Y, the process is much slower going from X to Y, then it is from Y to X. To give you an idea, from X to Y, Windows was showing an average spee...'''
date = "2013-02-18T13:14:00Z"
lastmod = "2013-02-19T14:27:00Z"
weight = 18712
keywords = [ "request", "andx", "tcp", "response" ]
aliases = [ "/questions/18712" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Troubleshooting Write AndX Response and Request](/questions/18712/troubleshooting-write-andx-response-and-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18712-score" class="post-score" title="current number of votes">0</div><span id="post-18712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are having an issue where moving files from one office to another is drastically different. If the file is in office X, and I am transferring it to office Y, the process is much slower going from X to Y, then it is from Y to X. To give you an idea, from X to Y, Windows was showing an average speed of 800KB/sec. Going from Y to X with the same file, the transfer was about 6MB/sec.<br />
</p><p>When looking at the Wireshark data when I transfer in each direction, I noticed that in going from Y to X, the Request and Response occur right after one another. From X to Y, there are additional TCP packets being generated.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-andx" rel="tag" title="see questions tagged &#39;andx&#39;">andx</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '13, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/269026dc091d3df0196d0c83f4d38177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cnjbucks&#39;s gravatar image" /><p><span>cnjbucks</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cnjbucks has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-18712" class="comments-container"></div><div id="comment-tools-18712" class="comment-tools"></div><div class="clear"></div><div id="comment-18712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18726"></span>

<div id="answer-container-18726" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18726-score" class="post-score" title="current number of votes">2</div><span id="post-18726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since SMB is a block orientated protocol (and not stream orientated), there will be a roundtrip delay for each block. When transferring big files over a WAN, this delay can become substantial, as there will be many blocks.</p><p>When using NT explorer, for some unknown reason, the blocksize is different depending on the direction of the transfer. If you write a file to a remote system, the blocksize is 4K, when you read from a remote system it is 60K.</p><p>Solution: do the transfer in a command shell. See also: <a href="http://support.microsoft.com/kb/223140">http://support.microsoft.com/kb/223140</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '13, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18726" class="comments-container"></div><div id="comment-tools-18726" class="comment-tools"></div><div class="clear"></div><div id="comment-18726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18713"></span>

<div id="answer-container-18713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18713-score" class="post-score" title="current number of votes">0</div><span id="post-18713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Without having any further information, one possible reason could be an MTU size problem when you copy from X -&gt; Y. Do you see any ICMP "fragmentation needed" messages in the capture file? Do you have a VPN tunnel between X and Y?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '13, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-18713" class="comments-container"><span id="18753"></span><div id="comment-18753" class="comment"><div id="post-18753-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>I don't see any ICMP messages in the capture file. I think there is a problem at site X that I have to figure out. Today I had a PC setup at another site (I'll call it site Z). I transferred the same file I was moving between X and Y between Y and Z, and the file transfers were noticeably faster.</p><p>This is not a VPN tunnel, this is going over our MPLS network from one office to another.<br />
</p><p>I noticed in the captures going from X to Y, I see the AndX Request and then several lines that show micrsoft ds --&gt; 53367 [ACK]. From Y to X, I see the AndX Request and that is immediately followed by the AndX Response. I see this same behavior in the transfers I did today from Z to Y.</p><p>I did discover today that if I ping the storage at site Z from the switch that this storage is plugged into, the success on those pings was 968/1000.</p></div><div id="comment-18753-info" class="comment-info"><span class="comment-age">(19 Feb '13, 14:05)</span> <span class="comment-user userinfo">cnjbucks</span></div></div><span id="18756"></span><div id="comment-18756" class="comment"><div id="post-18756-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I don't see any ICMP messages in the capture file.</p></blockquote><p>did you use any capture filter that could have 'ignored' icmp?</p><blockquote><p>I transferred the same file I was moving between X and Y between Y and Z, and the file transfers were noticeably faster.</p></blockquote><p>O.K. to rule out a network problem <strong>not related</strong> to your file transfer protocol, I recommend to measure the connection with jperf (<a href="http://code.google.com/p/xjperf/).">http://code.google.com/p/xjperf/).</a></p><p>You need two systems. One in X and one in Y. You need Java on those systems!</p><p>Then run these tests:</p><blockquote><p>X: jperf is client, Y: jperf is server<br />
X: jperf is server, Y: jperf is client</p></blockquote><p>Let the test run for ~ 30 seconds.</p><p>If there are notable differences in speed, then there is either a problem in the MPLS (possibly wrong QoS settings) or a problem with your network equipment (whatever that might be). In that case, please record the two tests with Wireshark (at both sides) and post the capture files somewhere (google docs, cloudshark.org, one click file hoster, etc.), so we can have a look ourselves.</p><p>Regards<br />
Kurt</p></div><div id="comment-18756-info" class="comment-info"><span class="comment-age">(19 Feb '13, 14:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-18713" class="comment-tools"></div><div class="clear"></div><div id="comment-18713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

