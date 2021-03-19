+++
type = "question"
title = "Newbie question: counting bytes going through satellite modem"
description = '''We live 10 miles past the middle of nowhere, and the only Internet service we can get (apart from dial-up) is via satellite, which is extremely bandwidth limited (among other problems). According to our service provider, our upload/download usage varies alarmingly. We&#x27;ll go through a week of normal ...'''
date = "2014-11-22T18:42:00Z"
lastmod = "2014-11-23T03:56:00Z"
weight = 38072
keywords = [ "count", "satellite", "modem", "bytes" ]
aliases = [ "/questions/38072" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Newbie question: counting bytes going through satellite modem](/questions/38072/newbie-question-counting-bytes-going-through-satellite-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38072-score" class="post-score" title="current number of votes">0</div><span id="post-38072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We live 10 miles past the middle of nowhere, and the only Internet service we can get (apart from dial-up) is via satellite, which is extremely bandwidth limited (among other problems).</p><p>According to our service provider, our upload/download usage varies alarmingly. We'll go through a week of normal usage with only a 1% drop in our allocated bandwidth, followed by a day of similar usage during which we use up our allotted bandwidth by a percentage point every five minutes. Their tech people have seen this happen while we are logged on with only one computer connected (straight from the modem to the NIC on the computer - no router connected), but they still assume it is somehow our fault that we get such multiple-order-of-magnitude fluctuations in our usage. I don't believe it. I think something is screwy on their end.</p><p>What I would like to do is to monitor how many actual bytes pass through our satellite modem during fixed time periods (say every hour, for example) and then compare this to what our service provider says we are using. I believe that this will demonstrate even to them that the problem is NOT on our end.</p><p>So my question is simple... can Wireshark do this? I have downloaded it, and it looks like a wonderful product, but before I invest the necessary time to learn it sufficiently to do a task like this I'd like to at least have some degree of confidence that it will be able to do what I am needing. I don't mind figuring out myself how to do this, but I just want to make sure that it is possible.</p><p>Many thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-satellite" rel="tag" title="see questions tagged &#39;satellite&#39;">satellite</span> <span class="post-tag tag-link-modem" rel="tag" title="see questions tagged &#39;modem&#39;">modem</span> <span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '14, 18:42</strong></p><img src="https://secure.gravatar.com/avatar/3fdf50cbc8700835a49ecdf0988bb38b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="landbrake&#39;s gravatar image" /><p><span>landbrake</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="landbrake has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '14, 02:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-38072" class="comments-container"></div><div id="comment-tools-38072" class="comment-tools"></div><div class="clear"></div><div id="comment-38072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38075"></span>

<div id="answer-container-38075" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38075-score" class="post-score" title="current number of votes">3</div><span id="post-38075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="landbrake has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark isn't really the correct tool for this task.</p><p>Wireshark can only capture traffic that flows past the NIC(s) of the host machine it's running on. With multiple devices connected via a home router likely to be on a switched network, you would need to run Wireshark on every connected device (which may not be possible e.g. phones and tablets) and then correlate all the stats, still probably missing stuff that happens before Wireshark gets to start.</p><p>I think you're likely to be better off getting the traffic data from your router. Hopefully it allows you to see traffic data, possibly on a diagnostic screen that you can inspect manually (or grab via some programmatic means), or even better via SNMP so that you can run an SNMP application .e.g <a href="http://www.paessler.com/prtg">PRTG</a> on one (permanently on) computer that will periodically retrieve the interface byte counters from the router and display them graphically.</p><p>If your router doesn't do this, either buy another router that does (hopefully out of the box or with an alternative firmware such as <a href="http://www.openwrt.org/">OpenWrt</a>, <a href="http://www.dd-wrt.com/site/index">DD-Wrt</a> or similar).</p><p>There are also other network traffic monitors that can run on each device, but again you would need to correlate all the info, and it might be difficult to run such applications on all devices, e.g. phones.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '14, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38075" class="comments-container"><span id="38076"></span><div id="comment-38076" class="comment"><div id="post-38076-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for the great answer! That is exactly what I was wondering, but I wasn't able to tell without investing quite a bit of time into poring through the documentation... time that it looks as though will be better spent investigating my router (and possibly looking into getting a more powerful one).</p></div><div id="comment-38076-info" class="comment-info"><span class="comment-age">(23 Nov '14, 03:14)</span> <span class="comment-user userinfo">landbrake</span></div></div><span id="38078"></span><div id="comment-38078" class="comment"><div id="post-38078-score" class="comment-score"></div><div class="comment-text"><p>It doesn't necessarily have to be a more powerful router, the alternative router firmwares run on a wide range of devices. They also tend to give you a lot more control of what's happening through the router.</p></div><div id="comment-38078-info" class="comment-info"><span class="comment-age">(23 Nov '14, 03:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38079"></span><div id="comment-38079" class="comment"><div id="post-38079-score" class="comment-score"></div><div class="comment-text"><p>I have a consumer level Belkin wireless router that, in its "out of the box" configuration, does not show any statistics like number of bytes passing through a port. Do routers like this tend to support the type of alternate firmware you are referring to? I'm a programming guy, and while I have had to set up lots of home networks I have never delved into the networking depths at this level.</p></div><div id="comment-38079-info" class="comment-info"><span class="comment-age">(23 Nov '14, 03:40)</span> <span class="comment-user userinfo">landbrake</span></div></div><span id="38080"></span><div id="comment-38080" class="comment"><div id="post-38080-score" class="comment-score"></div><div class="comment-text"><p>I checked both the OpenWrt and DD-Wrt sites and it appears as though neither supports my particular router (Belkin F5D9230). :-(</p></div><div id="comment-38080-info" class="comment-info"><span class="comment-age">(23 Nov '14, 03:56)</span> <span class="comment-user userinfo">landbrake</span></div></div></div><div id="comment-tools-38075" class="comment-tools"></div><div class="clear"></div><div id="comment-38075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

