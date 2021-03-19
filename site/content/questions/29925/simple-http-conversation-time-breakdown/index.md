+++
type = "question"
title = "Simple HTTP conversation | time breakdown"
description = '''Hi, I&#x27;m trying to understand the time breakdown for a simple HTTP conversation. I&#x27;ve Shared capture file http-png-wireshark.pcapng, uploaded at: https://drive.google.com/file/d/0BwRchYLsDMZiRE5wakNQVmpkODQ/edit?usp=sharing Please select the first filter: (ip.addr eq 192.168.43.92 and ip.addr eq 162....'''
date = "2014-02-17T01:53:00Z"
lastmod = "2014-02-18T03:33:00Z"
weight = 29925
keywords = [ "breakdown", "conversation", "http", "time" ]
aliases = [ "/questions/29925" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Simple HTTP conversation | time breakdown](/questions/29925/simple-http-conversation-time-breakdown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29925-score" class="post-score" title="current number of votes">0</div><span id="post-29925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to understand the time breakdown for a simple HTTP conversation. I've Shared capture file http-png-wireshark.pcapng, uploaded at: <a href="https://drive.google.com/file/d/0BwRchYLsDMZiRE5wakNQVmpkODQ/edit?usp=sharing">https://drive.google.com/file/d/0BwRchYLsDMZiRE5wakNQVmpkODQ/edit?usp=sharing</a></p><p>Please select the first filter: (ip.addr eq 192.168.43.92 and ip.addr eq 162.159.241.165) and (tcp.port eq 50117 and tcp.port eq 80)</p><p>The HTTP request is: <a href="http://www.wireshark.org/assets/images/hero_sprite.png">http://www.wireshark.org/assets/images/hero_sprite.png</a></p><p>Frame 30 is HTTP GET request. Please explain the time spent between: Frame 30-&gt;35 (219ms) - see the DeltaConv column Frame 35-&gt;36 (18ms) Frame 39-41 (196ms)</p><p>Thanks, Kapil</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-breakdown" rel="tag" title="see questions tagged &#39;breakdown&#39;">breakdown</span> <span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '14, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/143b1eb32813ac15979360fa89bc4cbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kapilok&#39;s gravatar image" /><p><span>kapilok</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kapilok has no accepted answers">0%</span></p></div></div><div id="comments-container-29925" class="comments-container"></div><div id="comment-tools-29925" class="comment-tools"></div><div class="clear"></div><div id="comment-29925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29931"></span>

<div id="answer-container-29931" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29931-score" class="post-score" title="current number of votes">2</div><span id="post-29931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Please explain the time spent between: Frame 30-&gt;35 (219ms)</p></blockquote><p>That's the RTT (Round-Tip-Time) of the line (0.137843 seconds - see delta between frame 26 (SYN) and 28 (SYN-ACK)) and the time the server OS needed to create the ACK (0.081865s == 0.219708s - 0.137843s). So, the delta between the GET and the ACK is actually just 0.081865s. That's quite O.K. and it obviously depends on the load on the server and/or network components.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/screenshot_29925_small.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '14, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '14, 04:22</strong> </span></p></div></div><div id="comments-container-29931" class="comments-container"><span id="29944"></span><div id="comment-29944" class="comment"><div id="post-29944-score" class="comment-score"></div><div class="comment-text"><p>The ACK in 35 is just an ACK, zero data length, so you might think it would be just as quick as the SYN-ACK. But it could be that the server delays the ack until the response is ready. The first byte of response data is packet 36.</p><p>If you are analysing server response time, it is also useful to differentiate the Time to First Byte (TTFB) with Time to Last Byte (TTLB). The server is "done" usually when it has started responding and sent the first byte - the client won't do much with the data until it receives the last byte.</p></div><div id="comment-29944-info" class="comment-info"><span class="comment-age">(17 Feb '14, 13:46)</span> <span class="comment-user userinfo">martyvis</span></div></div><span id="29953"></span><div id="comment-29953" class="comment"><div id="post-29953-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys, but still not very clear. Please correct my assertions below, if they are false:</p><ol><li>219ms consumed on server-side processing</li><li>18.6ms consumed by 1st TCP response packet on the network</li><li>1.1ms consumed by 2nd TCP response packet on the network (Why so less compared to 2. when length is exactly the same?)</li><li>196ms - Is this time included in the RTT time for HTTP response? If not, where does this go? Does it matter for the client?</li></ol><p>Thanks, Kapil</p></div><div id="comment-29953-info" class="comment-info"><span class="comment-age">(17 Feb '14, 23:08)</span> <span class="comment-user userinfo">kapilok</span></div></div><span id="29962"></span><div id="comment-29962" class="comment"><div id="post-29962-score" class="comment-score">1</div><div class="comment-text"><p>1.) No. It's the sum of</p><p>deltaSend + deltaProcess + deltaReceive = deltaTotal</p><p>where</p><ul><li>deltaSend = RTT/2 to send the request from client to server<br />
</li><li>deltaProcess = time to process the frame on the server (whatever it does with that request) and to create the ACK, with or without delay</li><li>deltaReceive = RTT/2 to send the ACK from server to client</li><li>deltaTotal = delta(Frame[35], Frame[30])</li></ul><p>Only deltaProcess is the time of server-side processing</p><p>Look at is this way:</p><pre><code>client ............................................ server

(1) Frame[30] ----- GET / (deltaSend = RTT/2) ---&gt;

                                           (2) deltaProcess 

(3) Frame[35] &lt;-- ACK/ (deltaReceive = RTT/2) ---

client ........................................... server</code></pre><p>So: <strong>deltaProcess</strong> = deltaTotal - 2 * RTT/2 = deltaTotal - RTT (see my answer)</p><p>2.) actually, the 18.6 ms are just the delta of the ACK (frame #35) and the first data fame (frame #36) sent by the server. That's another aspect of the processing time within the server. You cannot determine from a capture file on the client, why it took a certain amount of time, as most of that time is spent in the TCP stack of the server (not considering varying delay on the line, as that cannot be detected with only one capture point).</p><p>3.a.) that's the time it took the server to send the first data frame after the ACK. The server software writes x bytes (&gt; 1500) to the local TCP socket. The TCP stack splits that into several TCP frames. It took the TCP stack 18.6 ms to create and send that first data frame, following the ACK (not considering varying delay on the line, as that cannot be detected with only one capture point).</p><p>3.b.) It's less time, because the splitting operation took place in the TCP stack of the server. Apparently it took only 1.1 ms to do that. The size of the frame does not matter here, as the RTT is the same for all frames. So, the time <strong>difference/delta</strong> you see in the capture file on the client is exactly the same <strong>delta</strong> you would see in a server capture file or within the TCP stack.</p><p>4.) That's probably delayed ACK on the client.</p></div><div id="comment-29962-info" class="comment-info"><span class="comment-age">(18 Feb '14, 03:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29931" class="comment-tools"></div><div class="clear"></div><div id="comment-29931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29928"></span>

<div id="answer-container-29928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29928-score" class="post-score" title="current number of votes">1</div><span id="post-29928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Both hosts are delaying acknowledgements by 200ms. This is intentional and usually nothing to be worried about. both sides have nothing more to send in your conversation... <img src="https://osqa-ask.wireshark.org/upfiles/Selection_037.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '14, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-29928" class="comments-container"></div><div id="comment-tools-29928" class="comment-tools"></div><div class="clear"></div><div id="comment-29928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

