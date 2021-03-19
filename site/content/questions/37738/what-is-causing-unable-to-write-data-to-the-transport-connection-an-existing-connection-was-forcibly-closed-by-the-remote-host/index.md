+++
type = "question"
title = "What is causing &quot;Unable to write data to the transport connection: An existing connection was forcibly closed by the remote host.&quot;"
description = '''We are getting this error when performing a save within the application. It is a click once application and the data is stored in the cloud. The application is normally open for 2+ hours before performing the save. Recently upgraded to Juniper switches (this error did not happen prior to this). I ha...'''
date = "2014-11-10T12:51:00Z"
lastmod = "2014-12-15T07:53:00Z"
weight = 37738
keywords = [ "dup-ack", "rst", "retransmission" ]
aliases = [ "/questions/37738" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is causing "Unable to write data to the transport connection: An existing connection was forcibly closed by the remote host."](/questions/37738/what-is-causing-unable-to-write-data-to-the-transport-connection-an-existing-connection-was-forcibly-closed-by-the-remote-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37738-score" class="post-score" title="current number of votes">0</div><span id="post-37738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are getting this error when performing a save within the application. It is a click once application and the data is stored in the cloud. The application is normally open for 2+ hours before performing the save. Recently upgraded to Juniper switches (this error did not happen prior to this). I have a Wireshark capture file but need assistance analyzing it for possible causes for the error. Any help greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '14, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/6c647cab1a9ff885efc3926aaf5f22ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carey&#39;s gravatar image" /><p><span>Carey</span><br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '14, 13:02</strong> </span></p></div></div><div id="comments-container-37738" class="comments-container"><span id="37844"></span><div id="comment-37844" class="comment"><div id="post-37844-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys for the information provided. I wanted to post the link to the anonymized capture file from the client...</p><p><a href="https://drive.google.com/file/d/0Bz2uKfNM3FQfMV81UGVpUDBpSjA/view?usp=sharing">https://drive.google.com/file/d/0Bz2uKfNM3FQfMV81UGVpUDBpSjA/view?usp=sharing</a></p></div><div id="comment-37844-info" class="comment-info"><span class="comment-age">(13 Nov '14, 14:29)</span> <span class="comment-user userinfo">Carey</span></div></div><span id="37867"></span><div id="comment-37867" class="comment"><div id="post-37867-score" class="comment-score"></div><div class="comment-text"><p>If you have opportunity please review client capture file and see if it provides clues to the issue. thx again!</p></div><div id="comment-37867-info" class="comment-info"><span class="comment-age">(14 Nov '14, 08:36)</span> <span class="comment-user userinfo">Carey</span></div></div></div><div id="comment-tools-37738" class="comment-tools"></div><div class="clear"></div><div id="comment-37738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37761"></span>

<div id="answer-container-37761" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37761-score" class="post-score" title="current number of votes">2</div><span id="post-37761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Carey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>What is causing</strong> "Unable to write data to the transport connection: An existing connection was forcibly closed by the remote host"</p></blockquote><p>well, let's first talk about the issue. Based on that message (and some information found through Google), I assume that a TCP session was closed by one side, either by sending a FIN or a RESET (more likely).</p><p>So, <strong>what</strong> can cause this? Many things:</p><ul><li>a bug in the software</li><li>intended behavior of the server (or client) software, like some kind of timeout</li><li>a problem with a device between client/server</li><li>a firewall/loadbalancer/WAN accelerator as you hit a session limit and/or a session timeout on that device</li><li>etc.</li><li>etc.</li></ul><p>As you can see, there are a few good reasons for that behavior. Without a capture file taken near the client <strong>and in parallel</strong> near the server, you won't be able to figure out what <strong>exactly</strong> is causing the problem. In such a case, it's also a good idea to look at the server logs (if you have access to those logs).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '14, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37761" class="comments-container"><span id="37769"></span><div id="comment-37769" class="comment"><div id="post-37769-score" class="comment-score">1</div><div class="comment-text"><p>I think you need to consider <em>exactly</em> what changes were made implementing the new Juniper switches. I expect that you may have introduced a stateful aspect into the connection between client and server. This is likely to be that " firewall/loadbalancer/WAN accelerator " function that Kurt refers to. This may simply be a function of say having an ACL with a "Established" check in the switch.</p><p>If that is the case you should be able to either set a longer session timer, or see if you can configure your application to use TCP keep-alive to maintain session state.</p></div><div id="comment-37769-info" class="comment-info"><span class="comment-age">(11 Nov '14, 19:09)</span> <span class="comment-user userinfo">martyvis</span></div></div><span id="38578"></span><div id="comment-38578" class="comment"><div id="post-38578-score" class="comment-score"></div><div class="comment-text"><p>The ISP had changed as well and this error did not happen prior to that. We found the ISP had some sort of "inactivity timeout" for the TCP port (appx. 90 seconds). Thanks again for the input.</p></div><div id="comment-38578-info" class="comment-info"><span class="comment-age">(15 Dec '14, 07:53)</span> <span class="comment-user userinfo">Carey</span></div></div></div><div id="comment-tools-37761" class="comment-tools"></div><div class="clear"></div><div id="comment-37761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

