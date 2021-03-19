+++
type = "question"
title = "Voice/Data Traffic Question"
description = '''Mitel phone plugged into jack, my pc plugged into phone. I don&#x27;t have the phone setup for mirroring as I wasn&#x27;t capturing voice packets. I ran WS and was investigating another issue when I found a bunch of TCP packets coming from the Mitel PBX destined to other phones. How and why would I be seeing ...'''
date = "2017-03-10T07:55:00Z"
lastmod = "2017-03-11T22:43:00Z"
weight = 59987
keywords = [ "and", "traffic", "voice", "data", "question" ]
aliases = [ "/questions/59987" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Voice/Data Traffic Question](/questions/59987/voicedata-traffic-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59987-score" class="post-score" title="current number of votes">0</div><span id="post-59987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Mitel phone plugged into jack, my pc plugged into phone. I don't have the phone setup for mirroring as I wasn't capturing voice packets. I ran WS and was investigating another issue when I found a bunch of TCP packets coming from the Mitel PBX destined to other phones. How and why would I be seeing this? I understand I would see broadcast messages as my phone is on the same vlan but direct conversations between devices that my equipment is not involved in?</p><p>thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-voice" rel="tag" title="see questions tagged &#39;voice&#39;">voice</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '17, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p><span>rock90</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div></div><div id="comments-container-59987" class="comments-container"><span id="59999"></span><div id="comment-59999" class="comment"><div id="post-59999-score" class="comment-score"></div><div class="comment-text"><p>It's hard to say without seeing a capture file. Can you leave one in a publicly downloadable location such as Dropbox or Google Drive?</p></div><div id="comment-59999-info" class="comment-info"><span class="comment-age">(10 Mar '17, 21:01)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="60011"></span><div id="comment-60011" class="comment"><div id="post-60011-score" class="comment-score"></div><div class="comment-text"><p>It's a bit hard to give an answer without a good understanding of the network topology and state of the upstream L2 network in particular, but if you're seeing destination MAC addresses other than those served by your phone or your PC there are a few possibilities. One is the presence of a hub in the network. Another is that MAC learning has been disabled on the VLAN (causing an L2 switch to treat these as broadcasts, never learning the specific destination port to forward to).</p></div><div id="comment-60011-info" class="comment-info"><span class="comment-age">(11 Mar '17, 22:43)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-59987" class="comment-tools"></div><div class="clear"></div><div id="comment-59987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

