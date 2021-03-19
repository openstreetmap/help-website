+++
type = "question"
title = "Why are packets incorrectly identified as PCLI?"
description = '''While capturing a multicast video feed on port 9000, I noticed Wireshark was identifying the content of the UDP packets as PCLI (Packet Cable Lawful Intercept) containing another IP datagram. Has anyone seen this issue before? Disabling the PCLI dissector fixes this.'''
date = "2012-03-15T07:56:00Z"
lastmod = "2014-06-16T07:39:00Z"
weight = 9557
keywords = [ "pcli", "multicast", "udp" ]
aliases = [ "/questions/9557" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why are packets incorrectly identified as PCLI?](/questions/9557/why-are-packets-incorrectly-identified-as-pcli)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9557-score" class="post-score" title="current number of votes">0</div><span id="post-9557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While capturing a multicast video feed on port 9000, I noticed Wireshark was identifying the content of the UDP packets as PCLI (Packet Cable Lawful Intercept) containing another IP datagram.</p><p>Has anyone seen this issue before?</p><p>Disabling the PCLI dissector fixes this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcli" rel="tag" title="see questions tagged &#39;pcli&#39;">pcli</span> <span class="post-tag tag-link-multicast" rel="tag" title="see questions tagged &#39;multicast&#39;">multicast</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '12, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/7dbdec8eb185b7587ef44dacef29e6e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manu&#39;s gravatar image" /><p><span>Manu</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Mar '12, 08:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9557" class="comments-container"></div><div id="comment-tools-9557" class="comment-tools"></div><div class="clear"></div><div id="comment-9557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9558"></span>

<div id="answer-container-9558" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9558-score" class="post-score" title="current number of votes">3</div><span id="post-9558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Manu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The PCLI dissector is registered to decode anything on UDP Port 9000. There are no heuristics in the dissector to check if the packet is indeed PCLI, nor does it seem to be an IANA allocated port.</p><p>Disabling the dissector is the correct approach if your traffic isn't PCLI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '12, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9558" class="comments-container"><span id="9559"></span><div id="comment-9559" class="comment"><div id="post-9559-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb.</p></div><div id="comment-9559-info" class="comment-info"><span class="comment-age">(15 Mar '12, 08:32)</span> <span class="comment-user userinfo">Manu</span></div></div><span id="9564"></span><div id="comment-9564" class="comment"><div id="post-9564-score" class="comment-score">1</div><div class="comment-text"><p>Setting the PCLI port preference to 0 would permanently disable it too. (Maybe the default port should be 0 since 9000 isn't IANA-registered.)</p></div><div id="comment-9564-info" class="comment-info"><span class="comment-age">(15 Mar '12, 15:12)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="33797"></span><div id="comment-33797" class="comment"><div id="post-33797-score" class="comment-score"></div><div class="comment-text"><p>I am facing the same situation. Above mentioned disable PCLI protocol is the correct approach if it's not a PCLI traffic. My question is what is PCLI traffic and how to identify a traffic is PCLI traffic? Port 9000 is a IANA-registered port for UDPCast.</p></div><div id="comment-33797-info" class="comment-info"><span class="comment-age">(14 Jun '14, 03:12)</span> <span class="comment-user userinfo">a278497234</span></div></div><span id="33863"></span><div id="comment-33863" class="comment"><div id="post-33863-score" class="comment-score"></div><div class="comment-text"><p>(For completeness) you created a <a href="http://ask.wireshark.org/questions/33798/what-is-pcli-traffic-and-how-to-identify-a-traffic-is-pcli-traffic">new question</a> for this latest comment..</p></div><div id="comment-33863-info" class="comment-info"><span class="comment-age">(16 Jun '14, 07:39)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-9558" class="comment-tools"></div><div class="clear"></div><div id="comment-9558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

