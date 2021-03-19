+++
type = "question"
title = "RTCDC filter"
description = '''Hello everyone, I&#x27;m trying to capture rtcdc traffic using this test page http://webrtc.googlecode.com/svn/trunk/samples/js/demos/html/dc1.html I use rtcdc filter in wireshark without results, instead of that, the traffic from that web is tagged as UDP traffic. How can I see it as rtcdc traffic?'''
date = "2013-08-14T00:06:00Z"
lastmod = "2013-08-16T00:39:00Z"
weight = 23766
keywords = [ "capture", "udp", "datachannel", "webrtc", "rtcdc" ]
aliases = [ "/questions/23766" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RTCDC filter](/questions/23766/rtcdc-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23766-score" class="post-score" title="current number of votes">0</div><span id="post-23766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I'm trying to capture rtcdc traffic using this test page <a href="http://webrtc.googlecode.com/svn/trunk/samples/js/demos/html/dc1.html">http://webrtc.googlecode.com/svn/trunk/samples/js/demos/html/dc1.html</a> I use rtcdc filter in wireshark without results, instead of that, the traffic from that web is tagged as UDP traffic. How can I see it as rtcdc traffic?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-datachannel" rel="tag" title="see questions tagged &#39;datachannel&#39;">datachannel</span> <span class="post-tag tag-link-webrtc" rel="tag" title="see questions tagged &#39;webrtc&#39;">webrtc</span> <span class="post-tag tag-link-rtcdc" rel="tag" title="see questions tagged &#39;rtcdc&#39;">rtcdc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '13, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/9c2957b8a8c394e5b03b5ffda5917bc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miguelo&#39;s gravatar image" /><p><span>Miguelo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miguelo has no accepted answers">0%</span></p></div></div><div id="comments-container-23766" class="comments-container"><span id="23789"></span><div id="comment-23789" class="comment"><div id="post-23789-score" class="comment-score">1</div><div class="comment-text"><p>Are you sure it's UDP traffic? When I do <code>nslookup webrtc.googlecode.com</code>, I get 74.125.140.82. Applying a display filter of <code>ip.addr eq 74.125.140.0/24</code>, I only see TCP and SSL traffic when I <code>Start -&gt; [type some text] -&gt; Send Data -&gt; Stop Send Data</code>. To me it looks like the traffic is encrypted, and if so, you won't be able to see the RTCDC traffic.</p></div><div id="comment-23789-info" class="comment-info"><span class="comment-age">(14 Aug '13, 20:29)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-23766" class="comment-tools"></div><div class="clear"></div><div id="comment-23766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23788"></span>

<div id="answer-container-23788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23788-score" class="post-score" title="current number of votes">2</div><span id="post-23788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://datatracker.ietf.org/doc/draft-ietf-rtcweb-data-protocol/?include_text=1">RTCWeb</a> runs over SCTP, not UDP, according to the Internet-Draft in question. If this is something such as RTCWeb-over-SCTP-over-DTLS-over-ICE-over-UDP, as per <a href="http://tools.ietf.org/html/draft-jesup-rtcweb-data-01">this Internet-Draft</a>, in order to see it as RTCWeb traffic you'd have to modify the Wireshark code to handle all those encapsulations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '13, 20:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23788" class="comments-container"></div><div id="comment-tools-23788" class="comment-tools"></div><div class="clear"></div><div id="comment-23788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23799"></span>

<div id="answer-container-23799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23799-score" class="post-score" title="current number of votes">2</div><span id="post-23799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>the traffic from that web is tagged as UDP traffic.</p></blockquote><p>according to their web page, the transport protocol is RTP. So, it sounds reasonable that you see UDP traffic.</p><blockquote><p><a href="http://www.webrtc.org/reference/architecture#TOC-Transport-Session">http://www.webrtc.org/reference/architecture#TOC-Transport-Session</a></p></blockquote><p>Although in my test, that page created only a local connection to itself, according to Chromes Developer Tools and I did <strong>not</strong> see any UDP traffic!</p><p>So, there is no <strong>rtcdc protocol</strong> involved and I believe the name WebRTC is just coincidental the same.</p><p>You can try to decode the UDP traffic as RTP like this:</p><ul><li>right click one of those UDP packets</li><li>select "Decode As.."</li><li>select "RTP"</li></ul><p>However, the payload seems to be encrypted with AES. I found some hints in the Chrome developer tools, but did not invest any time to figure out what was going on. So, even if you decode that packets as RTP, you may not be able to read the payload if it is indeed encrypted.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '13, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23799" class="comments-container"><span id="23816"></span><div id="comment-23816" class="comment"><div id="post-23816-score" class="comment-score"></div><div class="comment-text"><p>Tanks for the answers.</p><p>Kurt you are right, all the UDP traffic I analysed related to WebRTC can be decoded as RTP traffic properly, and the payload is encrypted as you said.</p><p>Anyway, I'm still trying to capture any RTCDC traffic from any webpage, but I can't find anyone. Does anybody know any web for testing?</p><p>Thanks</p></div><div id="comment-23816-info" class="comment-info"><span class="comment-age">(16 Aug '13, 00:39)</span> <span class="comment-user userinfo">Miguelo</span></div></div></div><div id="comment-tools-23799" class="comment-tools"></div><div class="clear"></div><div id="comment-23799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

