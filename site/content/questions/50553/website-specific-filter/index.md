+++
type = "question"
title = "Website Specific Filter"
description = '''What would be the method to filter traffic to show a conversation with a specific website? I want to examine the conversation that occurs not between a server and my own machine, but rather all content from a specific website and my machine. It is seen when trying to do this with a simple Port/IP fi...'''
date = "2016-02-26T10:37:00Z"
lastmod = "2016-02-26T14:37:00Z"
weight = 50553
keywords = [ "filter", "website", "tcp" ]
aliases = [ "/questions/50553" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Website Specific Filter](/questions/50553/website-specific-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50553-score" class="post-score" title="current number of votes">0</div><span id="post-50553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What would be the method to filter traffic to show a conversation with a specific website? I want to examine the conversation that occurs not between a server and my own machine, but rather all content from a specific website and my machine. It is seen when trying to do this with a simple Port/IP filter you end up filtering out a massive part of the conversation, specifically all content hosted on external servers. Furthering the problem, you'll find after time a website will begin serving you content from a different one of its own servers, making it difficult to pin down your data. Ultimately, I am aiming to extract TCP and SSL (port 80, 443) data to calculate packet interarrival times.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '16, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/cd19b53227c855660a28125a22ae6177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AGauvin&#39;s gravatar image" /><p><span>AGauvin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AGauvin has no accepted answers">0%</span></p></div></div><div id="comments-container-50553" class="comments-container"><span id="50557"></span><div id="comment-50557" class="comment"><div id="post-50557-score" class="comment-score">1</div><div class="comment-text"><p>It is not fully clear (at least to me) what exactly you want to achieve.</p><p>By starting no other application but Wireshark and the web browser, and then using just a single window in the browser towards a single web page, you should be reasonably sure that all the http and https connections you capture are related to that site. The most complex part is the discrimination between "own servers" of the website and the "different ones".</p><p>So if I read you right and you want to see all traffic from a particular domain (like e.g. free.fr), regardless what the IP addresses of the various servers in that domain are, you need to look first at the DNS responses using a display filter like <code>(dns.flags.response == 1) and (dns.qry.name contains "free.fr")</code> and then to http/https communication with the IPs returned in those DNS responses. However, some companies use several domain names, so this method of telling apples from pears is not 100% reliable.</p><p>Wireshark includes a powerful tool allowing you to associate DNS requests and responses with consequent http(s) conversations called MATE, which should allow you to filter even not decrypted https sessions by server hostname, yet it only makes sense to discuss its use once you are sure you can unambiguously identify the domain names you are interested in.</p><p>Also, bear in mind that DNS records have expiration times of hours, so be sure that after reboot, you start capturing before you visit the site you are interested in for the first time. If you'd visit it before starting the capture, the DNS response would be cached and a new DNS request would not be sent the next time you'd open the website.</p></div><div id="comment-50557-info" class="comment-info"><span class="comment-age">(26 Feb '16, 14:37)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50553" class="comment-tools"></div><div class="clear"></div><div id="comment-50553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

