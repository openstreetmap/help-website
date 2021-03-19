+++
type = "question"
title = "How do I only filter data/ip&#x27;s from a specific country?"
description = '''How do I only filter data/ip&#x27;s from a specific country? To keep this short: I want to specifically only display ip&#x27;s and packet data from India, not filter it out. I am unable to find anything on how to do this.'''
date = "2016-11-19T15:13:00Z"
lastmod = "2016-11-20T01:32:00Z"
weight = 57465
keywords = [ "filter", "ip", "data", "packet" ]
aliases = [ "/questions/57465" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I only filter data/ip's from a specific country?](/questions/57465/how-do-i-only-filter-dataips-from-a-specific-country)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57465-score" class="post-score" title="current number of votes">0</div><span id="post-57465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I only filter data/ip's from a specific country? To keep this short: I want to specifically only display ip's and packet data from <em>India</em>, not filter it out. I am unable to find anything on how to do this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '16, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/67ae2883925126d8dd68f61a6cf22a70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacob%20G&#39;s gravatar image" /><p><span>Jacob G</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacob G has no accepted answers">0%</span></p></div></div><div id="comments-container-57465" class="comments-container"></div><div id="comment-tools-57465" class="comment-tools"></div><div class="clear"></div><div id="comment-57465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57469"></span>

<div id="answer-container-57469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57469-score" class="post-score" title="current number of votes">0</div><span id="post-57469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Enable GeoIP lookups on IP and (display) filter <code>ip.geoip.src_country == "India"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '16, 16:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57469" class="comments-container"><span id="57475"></span><div id="comment-57475" class="comment"><div id="post-57475-score" class="comment-score"></div><div class="comment-text"><p>Please also take a look at two tutorials on how to attach GeoIP databases to Wireshark:</p><p><a href="http://www.lovemytool.com/blog/2014/10/wireshark-and-geoip-by-betty-dubois.html">http://www.lovemytool.com/blog/2014/10/wireshark-and-geoip-by-betty-dubois.html</a></p><p><a href="https://www.youtube.com/watch?v=fX3hllaCFl8">https://www.youtube.com/watch?v=fX3hllaCFl8</a></p></div><div id="comment-57475-info" class="comment-info"><span class="comment-age">(20 Nov '16, 00:39)</span> <span class="comment-user userinfo">Packet_vlad</span></div></div><span id="57478"></span><div id="comment-57478" class="comment"><div id="post-57478-score" class="comment-score"></div><div class="comment-text"><p>...and also bear in mind that as some intentional and unintentional source IP obfuscating schemes exist, GeoIP only tells you where the device with public IP which has sent the packet is located, not where the user is located. There may be a branch office in India with a VPN to the headquarters in U.S. and all the traffic from the branch office may get to the internet via the HQ, and you may also have a reverse scheme with the HQ in India and the branch office in the U.S.</p><p>To make things even more complex, some people use VPNs to reach "obfuscation gateways" for public use if they want to prevent their network administrator from seeing where they browse.</p></div><div id="comment-57478-info" class="comment-info"><span class="comment-age">(20 Nov '16, 01:32)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-57469" class="comment-tools"></div><div class="clear"></div><div id="comment-57469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

