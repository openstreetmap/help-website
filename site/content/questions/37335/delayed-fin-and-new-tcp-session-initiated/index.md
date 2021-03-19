+++
type = "question"
title = "Delayed FIN and new TCP Session initiated"
description = '''Before I upload the capture I need to anonymize it. But let me post the question first, perhaps someone knows a quick answer. I&#x27;ve been having problems where clients in China are experiencing performance issues when browsing to a sharepoint website. It redirects, and uses single sign on, then tries ...'''
date = "2014-10-24T04:08:00Z"
lastmod = "2014-10-27T02:56:00Z"
weight = 37335
keywords = [ "fin", "timeout", "tcp", "sessions" ]
aliases = [ "/questions/37335" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Delayed FIN and new TCP Session initiated](/questions/37335/delayed-fin-and-new-tcp-session-initiated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37335-score" class="post-score" title="current number of votes">0</div><span id="post-37335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Before I upload the capture I need to anonymize it. But let me post the question first, perhaps someone knows a quick answer.</p><p>I've been having problems where clients in China are experiencing performance issues when browsing to a sharepoint website. It redirects, and uses single sign on, then tries to load the page. This last page may stay completely blank (except for the titlebar) for about 90 - 120 seconds, then the entire page loads. Other webpages do not show this symptom.</p><p>When analyzing a packet capture I can see that all foreign TCP sessions (towards the internet, not local) have a FIN,ACK packet which is received 90 - 120 seconds after the previous packet ... Then, after the sessions is closed, the client starts a new sessions towards the same external server and then everything looks normal again.</p><p>In other words, the delay in FIN,ACK matches exactly the delay in showing the webpage. The re-initiation of the TCP sessions looks like it's trying again to load the webpage.</p><p>Could this be caused by a session timeout? Does anyone know if this is 'expected' behavior for some phenomenon I haven't found yet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sessions" rel="tag" title="see questions tagged &#39;sessions&#39;">sessions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '14, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/25daf811ebe1190b06093b3676a2533f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoepMeloen86&#39;s gravatar image" /><p><span>JoepMeloen86</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoepMeloen86 has one accepted answer">50%</span></p></div></div><div id="comments-container-37335" class="comments-container"></div><div id="comment-tools-37335" class="comment-tools"></div><div class="clear"></div><div id="comment-37335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37370"></span>

<div id="answer-container-37370" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37370-score" class="post-score" title="current number of votes">0</div><span id="post-37370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JoepMeloen86 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think I figured it out. I thought the answer was a network phenomenon, but you got me thinking it was a client thing. While loading this website, it also loads all kinds of other stuff in the background (like office356.com, microsoftonline.com, sharepoint.com just to name a few).</p><p>One of these websites is maps.google.com (don't ask me why, web designers &gt;.&lt;) I saw a recurring pattern that reaching this website (in all captures) failed dramatically with lots of retransmissions and RST packets. The delay on these transmissions went from 3 sec, 6 sec, 12, 3, 6 etc. Adding all these up results in the exact time the website 'chokes' in loading.</p><p>So as a test I put all traffic in trough a proxy. This solved the problem, then I manually excluded maps.google.com and the problem returned.</p><p>Thanks again for your help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '14, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/25daf811ebe1190b06093b3676a2533f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoepMeloen86&#39;s gravatar image" /><p><span>JoepMeloen86</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoepMeloen86 has one accepted answer">50%</span></p></div></div><div id="comments-container-37370" class="comments-container"></div><div id="comment-tools-37370" class="comment-tools"></div><div class="clear"></div><div id="comment-37370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37343"></span>

<div id="answer-container-37343" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37343-score" class="post-score" title="current number of votes">1</div><span id="post-37343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>It's quite difficult to understand the capture from your description. Where was the capture taken? I assume adjacent to the web server. You really need to trace from the PC as well but I'll have a crack at it.</p><p>One reason the above can happen is through the following scenario:</p><ol><li>Starting from after completion of the single sign on, the browser starts a TCP connection to the web server</li><li>The browser sends a GET for the first page you mention which has a main page containing the Title Bar and a body contains an IFRAME (effectively another web page)</li><li>An intervening device (load balancer, firewall or proxy) RESETs the TCP connection, maybe because something in the chain doesn't support Persistent Connections</li><li>The RESET gets dropped somewhere (e.g. some firewalls drop RESETs by default) and so the browser believes the TCP connection is still good</li><li>The browser sends a GET (in a packet) on the initial (now dead) TCP connection</li><li>The TCP Send times out (no ACK received) and so re-sends the GET packet</li><li>The TCP stack on the PC retries the operation 4 more times, doubling the timeout each time</li><li>The TCP stack on the PC sends a RESET on the dead TCP connection</li><li>An intermediate device may translate to the FIN you see in the trace</li><li>The TCP stack on the PC returns an error to the browser</li><li>The browser starts a new connection (SYN, SYN/ACK, etc.)</li><li>Everything bursts back into life</li></ol><p>This is similar to a scenario I have in the RPR course I teach and that was based on an eCommerce use case.</p><p>The network RTT for China will probably be about 300 ms and so the initial timeout will be 600 ms. The timeout will double with each retry. So the delay will be .6 + 1.2 + 2.4 + 4.8 + 9.6 + 19.2 = 28.8, unfortunately not enough to explain your problem but maybe there are some variations to my theory above.</p><p>The trace at the PC is key.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '14, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-37343" class="comments-container"><span id="37369"></span><div id="comment-37369" class="comment"><div id="post-37369-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your elaborate answer Paul. I will have a look to post a part of the capture as soon as possible. (there's a lot of confidential info I don't want on the internet ;) )</p><p>I will have a look at you theory as well. Ill get back with a reply soon.</p></div><div id="comment-37369-info" class="comment-info"><span class="comment-age">(27 Oct '14, 01:54)</span> <span class="comment-user userinfo">JoepMeloen86</span></div></div></div><div id="comment-tools-37343" class="comment-tools"></div><div class="clear"></div><div id="comment-37343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

