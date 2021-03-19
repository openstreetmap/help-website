+++
type = "question"
title = "SIP - look inside of authentication packets?"
description = '''We experienced a problem today with all outbound SIP calls for about 10 minutes today. All inbound calls continued to function fine. None of the active calls were disconnected. I was lucky enough to capture the data going to/from the ISP edge router in our office.  What i noticed was a very large lo...'''
date = "2015-06-17T19:45:00Z"
lastmod = "2015-06-17T21:15:00Z"
weight = 43293
keywords = [ "sip", "5060", "401", "authenication" ]
aliases = [ "/questions/43293" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SIP - look inside of authentication packets?](/questions/43293/sip-look-inside-of-authentication-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43293-score" class="post-score" title="current number of votes">0</div><span id="post-43293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We experienced a problem today with all outbound SIP calls for about 10 minutes today. All inbound calls continued to function fine. None of the active calls were disconnected. I was lucky enough to capture the data going to/from the ISP edge router in our office.</p><p>What i noticed was a very large loop of Invites, Trying, Unauthorized, ACK then repeat for each call. This would continue until the user hung up their phone.</p><p>I'm using wireshark in Windows. How would i look inside of these packets to see what is wrong? My ISP and VOIP vendors are both pointing fingers at each other.</p><p>Below is a sample. I removed all the IPs and phone number. Any suggestions?</p><pre><code>|587.613086000|         INVITE SDP (g711U te          |SIP From: &quot;WORK&quot; &lt;[email protected]:5060;user=phone to:&lt;sip:[email protected]:5060;user=&quot;phone&quot; |=&quot;&quot; |(5060)=&quot;&quot; ------------------=&quot;&quot;&gt;  (5060)   |
|587.619187000|         100 Trying|                   |SIP Status
|         |(5060)   &lt;------------------  (5060)   |
|587.633932000|         401 Unauthorized              |SIP Status
|         |(5060)   &lt;------------------  (5060)   |
|587.636301000|         ACK       |                   |SIP Request
|         |(5060)   ------------------&gt;  (5060)   |
|587.637561000|         INVITE SDP (g711U te          |SIP From: &quot;WORK&quot; &lt;sip:[email protected]:5060;user=phone to:&lt;sip:[email protected]:5060;user=&quot;phone&quot; |=&quot;&quot; |(5060)=&quot;&quot; ------------------=&quot;&quot;&gt;  (5060)   |
|587.644035000|         100 Trying|                   |SIP Status
|         |(5060)   &lt;------------------  (5060)   |
|587.658965000|         401 Unauthorized              |SIP Status
|         |(5060)   &lt;------------------  (5060)   |
|587.661240000|         ACK       |                   |SIP Request
|         |(5060)   ------------------&gt;  (5060)   |
|587.662205000|         INVITE SDP (g711U te          |SIP From: &quot;WORK&quot; &lt;sip:[email protected]:5060;user=phone to:&lt;sip:[email protected]:5060;user=&quot;phone&quot; |=&quot;&quot; |(5060)=&quot;&quot; ------------------=&quot;&quot;&gt;  (5060)   |
|587.668582000|         100 Trying|                   |SIP Status
</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-5060" rel="tag" title="see questions tagged &#39;5060&#39;">5060</span> <span class="post-tag tag-link-401" rel="tag" title="see questions tagged &#39;401&#39;">401</span> <span class="post-tag tag-link-authenication" rel="tag" title="see questions tagged &#39;authenication&#39;">authenication</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 19:45</strong></p><img src="https://secure.gravatar.com/avatar/859ccf6a28f3696f21c0fe38ab59e2a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mjtvillanova&#39;s gravatar image" /><p><span>mjtvillanova</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mjtvillanova has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jun '15, 23:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-43293" class="comments-container"></div><div id="comment-tools-43293" class="comment-tools"></div><div class="clear"></div><div id="comment-43293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43297"></span>

<div id="answer-container-43297" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43297-score" class="post-score" title="current number of votes">1</div><span id="post-43297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's tough to see without an actual pcap, but your server is requiring Authentication, and either your UAC is not formulating an authentication response with the www-authenticate header, or it is failing in its response (i.e. bad password).</p><p>Again, too many variables.....need actual trace. You can anonymize it with Jasper's trace wrangler software if that is your concern for not providing a trace. ---&gt; <a href="http://www.tracewrangler.com/">http://www.tracewrangler.com</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 21:15</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-43297" class="comments-container"></div><div id="comment-tools-43297" class="comment-tools"></div><div class="clear"></div><div id="comment-43297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

