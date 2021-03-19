+++
type = "question"
title = "wanted RTP, got UDP (?!)"
description = '''Hi. I decided to break a trace on three parts with filtering SIP, RTP and DIAMETER protocol. For SIP and DIAMETER it went ok - I filtered the original trace and saved it as a new (trace) file.  When a new file was opened, it was displayed ok. But now, when I filter the original file with RTP protoco...'''
date = "2011-04-28T16:43:00Z"
lastmod = "2011-04-29T04:06:00Z"
weight = 3797
keywords = [ "filter", "diameter", "sip", "unwanted", "rtp" ]
aliases = [ "/questions/3797" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wanted RTP, got UDP (?!)](/questions/3797/wanted-rtp-got-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3797-score" class="post-score" title="current number of votes">0</div><span id="post-3797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I decided to break a trace on three parts with filtering SIP, RTP and DIAMETER protocol. For SIP and DIAMETER it went ok - I filtered the original trace and saved it as a new (trace) file. When a new file was opened, it was displayed ok.</p><p>But now, when I filter the original file with RTP protocol, save it as a new file and then open this new file, instead of RTP it shows like I filtered with UDP protocol. Why? I don't want so...</p><p>Br Thomas.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-unwanted" rel="tag" title="see questions tagged &#39;unwanted&#39;">unwanted</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '11, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p><span>wired</span><br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3797" class="comments-container"><span id="3798"></span><div id="comment-3798" class="comment"><div id="post-3798-score" class="comment-score"></div><div class="comment-text"><p>Is the answer inside here?:</p><p>Protocol dependencies</p><pre><code>UDP: Typically, RTP uses UDP as its transport protocol. RTP does
not have a well known UDP port (although the IETF recommend ports
6970 to 6999). Instead, the ports are allocated dynamically and
then signalled using a different protocol such as SIP or H245.
In SIP and other protocols a RTP session is described by SDP
(Session Description Protocol), which is not really a protocol
itself but rather a formalised way to describe a media session.</code></pre></div><div id="comment-3798-info" class="comment-info"><span class="comment-age">(28 Apr '11, 16:54)</span> <span class="comment-user userinfo">wired</span></div></div></div><div id="comment-tools-3797" class="comment-tools"></div><div class="clear"></div><div id="comment-3797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3804"></span>

<div id="answer-container-3804" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3804-score" class="post-score" title="current number of votes">3</div><span id="post-3804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wired has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark parses the SDP information in the SIP packets to learn about the upcoming RTP sessions. So, without the SIP packets, it does not know that the UDP packets are actually RTP packets. Possible solutions:</p><ul><li>Save both the SIP and RTP in a new file and it should decode OK</li><li>Use "Decode as..." to decode the UDP packets as RTP</li><li>Enable the "Try to decode RTP outside of conversations" setting in the RTP protocol preferences</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '11, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3804" class="comments-container"><span id="3808"></span><div id="comment-3808" class="comment"><div id="post-3808-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I decided to use the third option (RTP preferences). At first I intended to choose the second option (decode as), but I'm not sure whether to choose transport on UDP source, UDP destination or both. (What's the point of choosing between these three options?)</p></div><div id="comment-3808-info" class="comment-info"><span class="comment-age">(29 Apr '11, 03:57)</span> <span class="comment-user userinfo">wired</span></div></div><span id="3809"></span><div id="comment-3809" class="comment"><div id="post-3809-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", as that's the way this site works best, see the FAQ)</p><p>For your purpose there is not much difference, as both ports will be dynamically chosen. But imagine an http-server on port 8080, then you want to decode all traffic to/from port 8080 as HTTP.</p><p>So in that case, choosing the other (dynamic) port will only decode that specific session as HTTP.</p></div><div id="comment-3809-info" class="comment-info"><span class="comment-age">(29 Apr '11, 04:06)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-3804" class="comment-tools"></div><div class="clear"></div><div id="comment-3804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

