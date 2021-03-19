+++
type = "question"
title = "The number of TCP connections"
description = '''I did&#x27;nt work with Wireshark but now I should answer a question. When I captured a traffic between my host and different pages of a site, how can I get only the number of TCP connections and the corresponding durations?'''
date = "2017-10-21T14:45:00Z"
lastmod = "2017-10-22T06:51:00Z"
weight = 64070
keywords = [ "filter", "duration", "destination", "tcp" ]
aliases = [ "/questions/64070" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [The number of TCP connections](/questions/64070/the-number-of-tcp-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64070-score" class="post-score" title="current number of votes">0</div><span id="post-64070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I did'nt work with Wireshark but now I should answer a question. When I captured a traffic between my host and different pages of a site, how can I get only the number of TCP connections and the corresponding durations?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '17, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/b90455f6d0102aa9ca4214adea90d889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maryamtvk&#39;s gravatar image" /><p><span>maryamtvk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maryamtvk has no accepted answers">0%</span></p></div></div><div id="comments-container-64070" class="comments-container"></div><div id="comment-tools-64070" class="comment-tools"></div><div class="clear"></div><div id="comment-64070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64071"></span>

<div id="answer-container-64071" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64071-score" class="post-score" title="current number of votes">1</div><span id="post-64071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maryamtvk has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The conversations tool: under</p><p>Statistics -&gt; Conversations</p><p>you will have a TCP tab that contains each TCP connection and the start/duration. Note that you can apply display filter in the main packet pane and then select the check box for</p><p>Limit to Display Filter</p><p>to only roll up what is currently displayed. This is often useful on a mirror port where you are only interested in two hosts, or whatever.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '17, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-64071" class="comments-container"><span id="64083"></span><div id="comment-64083" class="comment"><div id="post-64083-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your respond. Can I filter them for a specific domain name?not just an IP address?</p></div><div id="comment-64083-info" class="comment-info"><span class="comment-age">(22 Oct '17, 02:28)</span> <span class="comment-user userinfo">maryamtvk</span></div></div><span id="64088"></span><div id="comment-64088" class="comment"><div id="post-64088-score" class="comment-score"></div><div class="comment-text"><p>Are you looking to do something like this with a filter:</p><p><a href="https://ask.wireshark.org/questions/9916/capturing-traffic-to-any-host-within-a-specific-domain">https://ask.wireshark.org/questions/9916/capturing-traffic-to-any-host-within-a-specific-domain</a></p><p>I don't think you can in a one-pass view. Most frames don't have domain name information in them so no easy way to link an IP to a Domain - it usually takes DNS or a hosts file to link the two. Exceptions are DNS packets which have requests/replies and contain domain name in plain text, or perhaps something like http requests which might have the domain name listed. However, this presumed link between an IP and a domain in an http context breaks down when you use a proxy: in that case the IP will be for the proxy, not the actual domain you are attempting to link. Someone else may have other ideas.</p><p>I don't know exactly what you are hunting for, but maybe check out ntop-ng (<a href="http://www.ntop.org/)">http://www.ntop.org/)</a> . This does a good job at trying to break down traffic by ASN, country, etc. May or may not be detailed enough. Omnipeek as well has some tools to aggregate the view.</p></div><div id="comment-64088-info" class="comment-info"><span class="comment-age">(22 Oct '17, 06:24)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="64090"></span><div id="comment-64090" class="comment"><div id="post-64090-score" class="comment-score">1</div><div class="comment-text"><p>If we stick to Wireshark capabilities, I'd like to draw your attention to MATE which allows to link together the DNS communication with TCP (and, at higher layer, HTTP) one, so you can add an "fqdn" metafield to TCP packets to allow filtering sessions by fqdn. Or you can do the same using Lua post-dissector.</p><p>In either case, you are likely to lack DNS resolutions for many sessions in a given capture, as most systems use DNS response caching. Reverse DNS helps only partially as it is not rare to run several web sites (with totally different fqdns) on a single IP address.</p></div><div id="comment-64090-info" class="comment-info"><span class="comment-age">(22 Oct '17, 06:51)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-64071" class="comment-tools"></div><div class="clear"></div><div id="comment-64071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

