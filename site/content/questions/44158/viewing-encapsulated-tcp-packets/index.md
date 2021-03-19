+++
type = "question"
title = "Viewing encapsulated TCP packets"
description = '''Hi,  I am working on a product that encapsulate a TCP inside a UDP packet.  I have a capture of UDP packets. I want to see inner TCP packet. Can this be done? Thanks.'''
date = "2015-07-14T16:13:00Z"
lastmod = "2015-07-15T12:42:00Z"
weight = 44158
keywords = [ "2975" ]
aliases = [ "/questions/44158" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Viewing encapsulated TCP packets](/questions/44158/viewing-encapsulated-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44158-score" class="post-score" title="current number of votes">0</div><span id="post-44158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am working on a product that encapsulate a TCP inside a UDP packet.</p><p>I have a capture of UDP packets. I want to see inner TCP packet. Can this be done?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-2975" rel="tag" title="see questions tagged &#39;2975&#39;">2975</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/9dc921391de97b40dee396f5b13eb11f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jincept&#39;s gravatar image" /><p><span>jincept</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jincept has no accepted answers">0%</span></p></div></div><div id="comments-container-44158" class="comments-container"><span id="44159"></span><div id="comment-44159" class="comment"><div id="post-44159-score" class="comment-score"></div><div class="comment-text"><p>Does it directly encapsulate TCP segments inside UDP, so that <em>immediately</em> after the UDP header is a TCP header, or does it encapsulate IP packets inside UDP, so that immediately after the UDP header is an IP header, with a protocol/next header field of 6 for TCP, followed by a TCP header, or does it encapsulate some sort of link-layer protocol inside UDP?</p></div><div id="comment-44159-info" class="comment-info"><span class="comment-age">(14 Jul '15, 18:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="44185"></span><div id="comment-44185" class="comment"><div id="post-44185-score" class="comment-score"></div><div class="comment-text"><p>HI Guy,</p><p>No it is not direct encapsulation.</p><p>After UDP, there is a custom 12 byte header, followed by IP and then TCP header.</p><p>IP &gt; UDP &gt; Custom &gt; IP &gt; TCP &gt; ...</p></div><div id="comment-44185-info" class="comment-info"><span class="comment-age">(15 Jul '15, 12:16)</span> <span class="comment-user userinfo">jincept</span></div></div></div><div id="comment-tools-44158" class="comment-tools"></div><div class="clear"></div><div id="comment-44158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44186"></span>

<div id="answer-container-44186" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44186-score" class="post-score" title="current number of votes">0</div><span id="post-44186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so it's "some real or fake link-layer packet encapsulated within UDP".</p><p>The best way to do that would be to write a dissector (in C, in Lua if your Wireshark includes Lua support, or in <a href="http://wsgd.free.fr">wsgd</a> if you're added it to your Wireshark) for your custom header, and have it hand the remainder of the packet off to the IP dissector after it dissects the custom header.</p><p>See the "Writing a Wireshark Dissector Using WSGD, Lua and C" talk by Graham Bloice, and the "Changing Wireshark with Lua: Writing a Lua Plug-in to Create a Custom Decoder" talk by Hadriel Kaplan, from the <a href="http://sharkfest.wireshark.org/sf15.html">SharkFest'15 Retrospective</a> (slides and videos available).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '15, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44186" class="comments-container"></div><div id="comment-tools-44186" class="comment-tools"></div><div class="clear"></div><div id="comment-44186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

