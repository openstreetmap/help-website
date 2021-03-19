+++
type = "question"
title = "Examples of Google Hangouts traffic analysis?"
description = '''Hi, Has anyone got a sequence of events with example network capture for a Google Hangouts session? My client has just started using Google Hangouts. We have it working end to end through various Firewalls and Proxy servers but it&#x27;s only working over TCP which we believe is causing latency issues. W...'''
date = "2014-07-05T04:36:00Z"
lastmod = "2014-07-08T07:18:00Z"
weight = 34437
keywords = [ "analysis", "hangouts" ]
aliases = [ "/questions/34437" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Examples of Google Hangouts traffic analysis?](/questions/34437/examples-of-google-hangouts-traffic-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34437-score" class="post-score" title="current number of votes">1</div><span id="post-34437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Has anyone got a sequence of events with example network capture for a Google Hangouts session?</p><p>My client has just started using Google Hangouts. We have it working end to end through various Firewalls and Proxy servers but it's only working over TCP which we believe is causing latency issues. We're about to do some analysis to see where in our environment we're blocking UDP (we'd thought all our Corporate Firewalls had been configured to pass UDP to the correct ports but we must have missed one).</p><p>What I'm struggling with is understanding what a good end to end traffic flow should look like i.e. not just a clean capture (which I can obtain at home) but what each element sequence means. If it were 'normal' SIP/SDP with RTP/RTCP traffic then one of the Wireshark books has some good worked examples. However, Google uses STUN, RTP, RTCP and SRTP and I don't understand the hand-off's between each protocol (STUN seems very hard to understand even after reading the RFC's).</p><p>Any help or pointers to online information would be much appreciated.</p><p>Regards, Matt</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-hangouts" rel="tag" title="see questions tagged &#39;hangouts&#39;">hangouts</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '14, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/5e93021b7cfa7afa3ad4f8d1ea082d1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hootsmagandy&#39;s gravatar image" /><p><span>hootsmagandy</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hootsmagandy has no accepted answers">0%</span></p></div></div><div id="comments-container-34437" class="comments-container"></div><div id="comment-tools-34437" class="comment-tools"></div><div class="clear"></div><div id="comment-34437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34465"></span>

<div id="answer-container-34465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34465-score" class="post-score" title="current number of votes">0</div><span id="post-34465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately I don't have sample traffic, but maybe I can answer some of your questions without that.</p><blockquote><p>we'd thought all our Corporate Firewalls had been configured to pass UDP to the correct ports but we must have missed one).</p></blockquote><p>There is a list of ports that Hangout is using: <a href="https://support.google.com/a/answer/1279090?hl=en">https://support.google.com/a/answer/1279090?hl=en</a></p><blockquote><p>However, Google uses STUN, RTP, RTCP and SRTP and I don't understand the hand-off's between each protocol (STUN seems very hard to understand even after reading the RFC's).</p></blockquote><p>The mentioned protocols are all required for Video and Audio data. I'm not sure if this is the right place to explain all of them, especially as there are loads of explanation pages on the internet.</p><blockquote><p>STUN seems very hard to understand even after reading the RFC's)</p></blockquote><p>Actually it's pretty easy: By using STUN the client tries to figure out if it is placed behind a NAT device. The IP address of the STUN packet will be different than the IP address placed in the payload by the STUN server (the address the server sees - usually the NATed address). If the client knows it external (NATed) IP address, it can use that information in protocols like SIP and H.323 (and probably internally within the Hangout protocols) to allow the other side to send data to the correct (NATed) address.</p><p>The key to success for Hangout through a firewall is to allow <strong>incoming</strong> UDP traffic on ports 19302 through 19309 <strong>from the internet</strong>, as stated in the link I posted above.</p><p>Cite:</p><pre><code>The ideal connection for a user to make to a hangout is through UDP. To allow this connection attempt to succeed you will need to allow connections into your network from UDP ports 19302 through 19309.</code></pre><p>That's kind of odd and dumb, as they won't tell you the IP addresses of the Google Hangout/Conference servers (probably because there are too many and they are subject to change), so you'll have to break a hole into your firewall policy just to make Hangout work, or buy a firewall that is able to detect Hangout traffic and do the rest auto-magically in the background, hopefully in a secure way ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34465" class="comments-container"></div><div id="comment-tools-34465" class="comment-tools"></div><div class="clear"></div><div id="comment-34465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

