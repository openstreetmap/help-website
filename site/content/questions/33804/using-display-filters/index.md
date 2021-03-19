+++
type = "question"
title = "Using display filters"
description = '''My use of wireshark is only to monitor what sites my family is going to (incognito or not). I have my suspicions that incognito is being used and so I would like to figure out how to filter and capture searches and all urls being accessed on the network.  I know very very little about network analys...'''
date = "2014-06-14T12:52:00Z"
lastmod = "2014-06-17T08:53:00Z"
weight = 33804
keywords = [ "capture-filter", "incognito", "display-filter", "wireshark" ]
aliases = [ "/questions/33804" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using display filters](/questions/33804/using-display-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33804-score" class="post-score" title="current number of votes">0</div><span id="post-33804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My use of wireshark is only to monitor what sites my family is going to (incognito or not). I have my suspicions that incognito is being used and so I would like to figure out how to filter and capture searches and all urls being accessed on the network. I know very very little about network analysis and I'm in over my head trying to figure it out by myself. I downloaded Wireshark 101 Pdf file and I'm reading it but its like a foreign language. I just want to know how to filter out only what I'm looking for.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-incognito" rel="tag" title="see questions tagged &#39;incognito&#39;">incognito</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '14, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/e6c607c6aa62572ae069de9e6f4b64c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashley%20Lynne%20Torgerson&#39;s gravatar image" /><p><span>Ashley Lynne...</span><br />
<span class="score" title="5 reputation points">5</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashley Lynne Torgerson has no accepted answers">0%</span></p></div></div><div id="comments-container-33804" class="comments-container"></div><div id="comment-tools-33804" class="comment-tools"></div><div class="clear"></div><div id="comment-33804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33810"></span>

<div id="answer-container-33810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33810-score" class="post-score" title="current number of votes">1</div><span id="post-33810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Although this is a Wireshark QA site, you may want to look into OpenDNS and put the OpenDNS servers into your router. You can then view reports of all the url lookups from your ISP connection.</p><p>If wanting to view this information in Wireshark, just filter on DNS traffic. Display filter is "dns", and capture filter would be "tcp port 53 or udp port 53"</p><p>Travis</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '14, 19:49</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-33810" class="comments-container"><span id="33837"></span><div id="comment-33837" class="comment"><div id="post-33837-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p></div><div id="comment-33837-info" class="comment-info"><span class="comment-age">(15 Jun '14, 10:23)</span> <span class="comment-user userinfo">Ashley Lynne...</span></div></div><span id="33847"></span><div id="comment-33847" class="comment"><div id="post-33847-score" class="comment-score"></div><div class="comment-text"><p>Caution: If the goal is to track usage from users you don't necessarily trust, they could bypass your OpenDNS server and specify their own, or go to a site with direct IP info. It's a clever solution and is probably one of the easiest to deploy, but it's tricky because it is within the power of untrusted and presumably smart wrong-doers to bypass it.</p></div><div id="comment-33847-info" class="comment-info"><span class="comment-age">(15 Jun '14, 14:08)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="33848"></span><div id="comment-33848" class="comment"><div id="post-33848-score" class="comment-score"></div><div class="comment-text"><p>Furthermore: DNS gives you insight into host names that have been accessed (www.xyz.com) - actually that have been <strong>resolved</strong>, not URLs that have been accessed (<a href="http://www.xyz.com/pictures/bad_stuff/xxxx.jpeg)!">http://www.xyz.com/pictures/bad_stuff/xxxx.jpeg)!</a> So, you might totally misinterpret what the users are doing, if you only look at DNS answers. And on the other side you might miss important things.</p><p>So, the best thing you could do to monitor the whole internet traffic is what <span></span><span>@Quadratic</span> suggested in the other question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/33805/tracking-incognito-use/33846">http://ask.wireshark.org/questions/33805/tracking-incognito-use/33846</a></p></blockquote><p>Could have been the answer to this question ;-)</p></div><div id="comment-33848-info" class="comment-info"><span class="comment-age">(15 Jun '14, 14:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="33887"></span><div id="comment-33887" class="comment"><div id="post-33887-score" class="comment-score"></div><div class="comment-text"><p>Clever people will always have a way to work around anything. If they want, they could purchase a VPN and then show the "Capture all Wireshark traffic" solution absolutely nothing but encrypted traffic.</p><p>Furthermore, most XXX material is not going to be at a "http://disney.com" domain, the domain will usually give you an insight to the type of traffic your users are looking for......i.e. "http://porn-tube-site-1.com, <a href="http://port-tube-site-of-the-month.com">http://port-tube-site-of-the-month.com</a>, etc".</p></div><div id="comment-33887-info" class="comment-info"><span class="comment-age">(17 Jun '14, 03:41)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="33898"></span><div id="comment-33898" class="comment"><div id="post-33898-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Clever people will always have a way to work around anything.</p></blockquote><p>sure, but this question is not about those clever familiy members, it's about how to follow what sites (URLs, Content) users are accessing on the internet and looking at DNS replies is certainly not the ideal method for that.</p><blockquote><p>Furthermore, most XXX material is not going to be at</p></blockquote><p>XXX sites are using CDNs (content delivery networks) as well, so the 'real' content is not delivered from xxxtube.com, but from <strong>s76ushd-xxx-w76e-tube.sf.cdn.com</strong>. Hard to imagine, that an inexperienced Wireshark user will be able to draw the right conclusions if he/she sees DNS replies for the CDN host ;-)</p><p>Sure, you will see at least one DNS request to xxxtube.com, but that could have been an <strong>ad</strong> on another site as well, which is another reason why DNS replies will give you sub-optimal results.</p></div><div id="comment-33898-info" class="comment-info"><span class="comment-age">(17 Jun '14, 08:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33810" class="comment-tools"></div><div class="clear"></div><div id="comment-33810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

