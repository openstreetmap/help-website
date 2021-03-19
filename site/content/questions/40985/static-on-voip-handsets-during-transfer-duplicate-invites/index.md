+++
type = "question"
title = "Static on VOIP handsets during transfer &amp; Duplicate invites"
description = '''Can anyone with experience assist me with the following capture that I took from two VOIP handsets transferring a call to a SIP desk phone. What is the recommended next step for troubleshooting after receiving the data below? I don&#x27;t have a ton of experience with VOIP so I&#x27;m uncertain. RTP Stream An...'''
date = "2015-03-29T11:45:00Z"
lastmod = "2015-03-30T11:47:00Z"
weight = 40985
keywords = [ "during", "static", "transfer" ]
aliases = [ "/questions/40985" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Static on VOIP handsets during transfer & Duplicate invites](/questions/40985/static-on-voip-handsets-during-transfer-duplicate-invites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40985-score" class="post-score" title="current number of votes">0</div><span id="post-40985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone with experience assist me with the following capture that I took from two VOIP handsets transferring a call to a SIP desk phone. What is the recommended next step for troubleshooting after receiving the data below? I don't have a ton of experience with VOIP so I'm uncertain.</p><p><strong>RTP Stream Analysis</strong></p><pre><code>Max delta = 1798.95 ms at packet no. 30095 
Max jitter = 877.89 ms. Mean jitter = 314.40 ms.
Max skew = -1825.33 ms.
Total RTP packets = 656   (expected 656)   Lost RTP packets = -652 (-99.39%)   Sequence errors = 652 
Duration 13.08 s (-2560 ms clock drift, corresponding to 6435 Hz (-19.57%)</code></pre><p><strong>VOIP CALL FLOW</strong></p><pre><code>Invite SDP (g711)---&gt;
Invite SDP (g711)---&gt;
Invite SDP (g711)---&gt;
Invite SDP (g711)---&gt;
&lt;----100 Trying
&lt;----407 Proxy Auth
&lt;----100 Trying
&lt;----407 Proxy Auth
&lt;----100 Trying
&lt;----407 Proxy Auth
&lt;----100 Trying
&lt;----407 Proxy Auth
ACK----&gt;
ACK----&gt;
ACK----&gt;
ACK----&gt;
Invite SDP (g711)---&gt;
Invite SDP (g711)---&gt;
&lt;---100 Trying
&lt;---100 Trying
Invite SDP (g711)---&gt;
Invite SDP (g711)---&gt;
&lt;---100 Trying
&lt;---100 Trying
&lt;---180 Ringing
&lt;---180 Ringing
&lt;---180 Ringing
&lt;---180 Ringing
&lt;---200 OK SDP (g711)
&lt;---200 OK SDP (g711)
&lt;---200 OK SDP (g711)
&lt;----RTP(g711U)
&lt;----RTP(g711U)
ACK----&gt;
ACK----&gt;
ACK----&gt;
ACK----&gt;
RTP(g711U)----&gt;
RTP(g711U)----&gt;
&lt;---REFER
&lt;---REFER
&lt;---REFER
&lt;---REFER
202 Accepted----&gt;
202 Accepted----&gt;
202 Accepted----&gt;
202 Accepted----&gt;
NOTIFY----&gt;
NOTIFY----&gt;
NOTIFY----&gt;
NOTIFY----&gt;
BYE----&gt;
BYE----&gt;
BYE----&gt;
BYE----&gt;
&lt;----407 Proxy Auth
&lt;----407 Proxy Auth
&lt;----407 Proxy Auth
&lt;----407 Proxy Auth
BYE----&gt;
BYE----&gt;
BYE----&gt;
BYE----&gt;
&lt;----200 OK
&lt;----200 OK
&lt;----200 OK
&lt;----200 OK
&lt;----200 OK
&lt;----200 OK
&lt;----200 OK
&lt;----200 OK</code></pre><p>Why are there so many repeated invites, etc. above? Everything is duplicated and I'm not sure if this is normal behavior..and if it it's normal behavior what could be the root cause? I'm leaning towards the assumption that the issue is a network congestion issue?! ...but I'm quite uncertain at this point. Any help would be greatly appreciated..also I can provide additional information if needed. Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-during" rel="tag" title="see questions tagged &#39;during&#39;">during</span> <span class="post-tag tag-link-static" rel="tag" title="see questions tagged &#39;static&#39;">static</span> <span class="post-tag tag-link-transfer" rel="tag" title="see questions tagged &#39;transfer&#39;">transfer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '15, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/871f736acbe24c12f1fad6bf5ebadd5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="georgennc&#39;s gravatar image" /><p><span>georgennc</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="georgennc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Mar '15, 12:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-40985" class="comments-container"><span id="40998"></span><div id="comment-40998" class="comment"><div id="post-40998-score" class="comment-score"></div><div class="comment-text"><p>network troubleshooting based on a (text based) "screenshot" is near to impossible, as 98% of the relevant information is missing.</p><p>Can you please upload a capture file somewhere (google drive, dropbox, cloudshark.org) and post the link here?</p></div><div id="comment-40998-info" class="comment-info"><span class="comment-age">(30 Mar '15, 04:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="41003"></span><div id="comment-41003" class="comment"><div id="post-41003-score" class="comment-score"></div><div class="comment-text"><p>Thank you grahamb. I have uploaded the entire capture to Google Drive: <a href="https://drive.google.com/file/d/0B6jI0xk_UGx_SGhzeVNXcjgyQTg/view?usp=sharing">https://drive.google.com/file/d/0B6jI0xk_UGx_SGhzeVNXcjgyQTg/view?usp=sharing</a></p></div><div id="comment-41003-info" class="comment-info"><span class="comment-age">(30 Mar '15, 05:09)</span> <span class="comment-user userinfo">georgennc</span></div></div><span id="41005"></span><div id="comment-41005" class="comment"><div id="post-41005-score" class="comment-score"></div><div class="comment-text"><p>That file is a shortcut.</p></div><div id="comment-41005-info" class="comment-info"><span class="comment-age">(30 Mar '15, 05:24)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="41006"></span><div id="comment-41006" class="comment"><div id="post-41006-score" class="comment-score"></div><div class="comment-text"><p>Sorry.. Here is the capture: <a href="https://drive.google.com/file/d/0B6jI0xk_UGx_V2RQSE8tcVJOVG8/view?usp=sharing">https://drive.google.com/file/d/0B6jI0xk_UGx_V2RQSE8tcVJOVG8/view?usp=sharing</a></p></div><div id="comment-41006-info" class="comment-info"><span class="comment-age">(30 Mar '15, 05:29)</span> <span class="comment-user userinfo">georgennc</span></div></div><span id="41009"></span><div id="comment-41009" class="comment"><div id="post-41009-score" class="comment-score"></div><div class="comment-text"><p>There is quite some traffic in the capture file. Would you mind to tell us the IP addresses of the involved VoIP systems???</p></div><div id="comment-41009-info" class="comment-info"><span class="comment-age">(30 Mar '15, 06:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="41017"></span><div id="comment-41017" class="comment not_top_scorer"><div id="post-41017-score" class="comment-score"></div><div class="comment-text"><p>The handset that the call was initiated with was 10.7.16.159.</p></div><div id="comment-41017-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:03)</span> <span class="comment-user userinfo">georgennc</span></div></div><span id="41019"></span><div id="comment-41019" class="comment not_top_scorer"><div id="post-41019-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-41019-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:07)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-40985" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-40985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41012"></span>

<div id="answer-container-41012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41012-score" class="post-score" title="current number of votes">0</div><span id="post-41012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Why are there so many repeated invites, etc. above?</p></blockquote><p>One reason could be, that all your frames are duplicated, maybe due to a problem with your capture setup (mirroring traffic of ingress and egress port on the switch) !! Can you please try to capture the frames only once, because the duplicated frames makes troubleshooting harder than it needs to be ;-)) You can try to de-duplicate the capture file with editcap.</p><p>Then there are some of the following messages:</p><blockquote><p>Status: 401 Unauthorized<br />
Status: 407 Proxy Authentication Required</p></blockquote><p>which indicates failed authentication and thus a retry.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '15, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-41012" class="comments-container"><span id="41018"></span><div id="comment-41018" class="comment"><div id="post-41018-score" class="comment-score"></div><div class="comment-text"><p>Kurt, I don't believe that there is any error on my part with the captures.. I believe that there is something within the network that is causing these duplicates. I've used the same process to capture at other locations and my results have never shown duplicates. I've used the same process to make captures today and these captures show no duplicates.. I'm baffled as to why this location is showing duplicates..could this possibly be a symptom of network congestion? Maybe the data is being re transmitted?</p></div><div id="comment-41018-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:06)</span> <span class="comment-user userinfo">georgennc</span></div></div><span id="41020"></span><div id="comment-41020" class="comment"><div id="post-41020-score" class="comment-score"></div><div class="comment-text"><p>You can see a capture on multiple interfaces, whereby a remote capture and a local interface carry the same traffic. That's the duplication.</p></div><div id="comment-41020-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:09)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="41022"></span><div id="comment-41022" class="comment"><div id="post-41022-score" class="comment-score"></div><div class="comment-text"><p>Apply this filter</p><blockquote><p>ip.addr eq 10.7.16.159 and sip</p></blockquote><p>then look at frames #3062 and #3066. They look identical to me, besides the destination mac address AND the IP ID (0000 in 3062). That does not look like a "re-transmission". That looks like packet duplication somewhere.</p><p>Furthermore, as <span></span><span>@Jaap</span> mentioned, you have also captured all frames twice via remote capture, see frames #3069 and #3077 (duplicates of 3062 and 3066, encapsulated in rpcap).</p><p>As a result, <strong>you are seeing the same SIP frame 4 times</strong>.</p><blockquote><p>Maybe the data is being re transmitted?</p></blockquote><p>No. The frames are simlpy captured several times at different locations, see above...</p></div><div id="comment-41022-info" class="comment-info"><span class="comment-age">(30 Mar '15, 08:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="41027"></span><div id="comment-41027" class="comment"><div id="post-41027-score" class="comment-score"></div><div class="comment-text"><p>There must have been another interface selected by default when I took my capture. I'll recapture the data and post it in a few hours. Thank you all for your assistance.</p></div><div id="comment-41027-info" class="comment-info"><span class="comment-age">(30 Mar '15, 09:06)</span> <span class="comment-user userinfo">georgennc</span></div></div><span id="41028"></span><div id="comment-41028" class="comment"><div id="post-41028-score" class="comment-score"></div><div class="comment-text"><blockquote><p>There must have been another interface selected by default when I took my capture.</p></blockquote><p>maybe.</p><blockquote><p>I'll recapture the data and post it in a few hours. Thank you all for your assistance.</p></blockquote><p>I guess, if you're doing the capturing in the right way, there won't be any duplicates and "re-transmissions" any more..</p><p>In that case: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-41028-info" class="comment-info"><span class="comment-age">(30 Mar '15, 09:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="41032"></span><div id="comment-41032" class="comment not_top_scorer"><div id="post-41032-score" class="comment-score"></div><div class="comment-text"><p>I ensured that only one interface was being captured this time. I don't see nearly as many errors but there was still static on the line during the transfer. Link: <a href="https://drive.google.com/file/d/0B6jI0xk_UGx_Y05pTU5HQnZXclk/view?usp=sharing">https://drive.google.com/file/d/0B6jI0xk_UGx_Y05pTU5HQnZXclk/view?usp=sharing</a></p></div><div id="comment-41032-info" class="comment-info"><span class="comment-age">(30 Mar '15, 11:40)</span> <span class="comment-user userinfo">georgennc</span></div></div><span id="41033"></span><div id="comment-41033" class="comment not_top_scorer"><div id="post-41033-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I ensured that only one interface was being captured this time.</p></blockquote><p>The SIP frames are still duplicates. See frame #6 and #7 as well as #8 and #9. Same as before. Identical frames, just two differences: IP ID 0000 (#6 and #9) and different mac addresses.</p><p>I still believe there is something wrong with the capture setup. Can you please add more details about your capture setup?</p><ul><li>Where did you capture (I can see it in the summary, but I want confirmation)</li><li>How did you capture (rpcap, switch mirror port, etc.).</li></ul></div><div id="comment-41033-info" class="comment-info"><span class="comment-age">(30 Mar '15, 11:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-41012" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-41012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

