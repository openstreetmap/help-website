+++
type = "question"
title = "ISO Wireshark Tutor / Network Guru"
description = '''My business is focused on the integration of Audio, Video &amp;amp; automation systems in the residential and commercial markets. As technology has developed over the last 10 years, we have our greatest success when we &quot;own&quot; our client&#x27;s network as well as all the low voltage systems. We&#x27;ve had great lu...'''
date = "2016-09-06T05:39:00Z"
lastmod = "2016-09-07T08:03:00Z"
weight = 55347
keywords = [ "tutor", "wlan" ]
aliases = [ "/questions/55347" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ISO Wireshark Tutor / Network Guru](/questions/55347/iso-wireshark-tutor-network-guru)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55347-score" class="post-score" title="current number of votes">0</div><span id="post-55347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My business is focused on the integration of Audio, Video &amp; automation systems in the residential and commercial markets. As technology has developed over the last 10 years, we have our greatest success when we "own" our client's network as well as all the low voltage systems. We've had great luck designing, installing and servicing networks for our clients, but will occasionally run into problems that are difficult to troubleshoot. I think understanding WLAN packet analysis will be the key to diagnosing &amp; resolving the majority of these issues. That being said, I'm looking for assistance with the following:</p><ol><li>A recommendation for a spectrum analyzer (2.4G &amp; 5G) I believe that a handful of our client sites have a large amount of RF chatter that could be causing problems. I've looked at some of the Metageek products and I'm inclined to go that route.</li><li>A recommendation on a hardware solution for WLAN packet caputer. Is Airpcap the way to go?</li><li>An experienced &amp; patient individual who can teach me the nuts and bolts on packet analysis and troubleshooting at that level. I can only absorb so much from Youtube videos and online tutorials and would be happy to pay for the expertise of a network guru.</li></ol><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tutor" rel="tag" title="see questions tagged &#39;tutor&#39;">tutor</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '16, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/7435e7bcf5a6fa0b09afc54fc43fb01f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arib1&#39;s gravatar image" /><p><span>arib1</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arib1 has no accepted answers">0%</span></p></div></div><div id="comments-container-55347" class="comments-container"></div><div id="comment-tools-55347" class="comment-tools"></div><div class="clear"></div><div id="comment-55347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55360"></span>

<div id="answer-container-55360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55360-score" class="post-score" title="current number of votes">0</div><span id="post-55360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><blockquote><p>A recommendation for a spectrum analyzer (2.4G &amp; 5G) I believe that a handful of our client sites have a large amount of RF chatter that could be causing problems. I've looked at some of the Metageek products and I'm inclined to go that route.</p></blockquote></blockquote><p>Our North American field team uses <a href="http://enterprise.netscout.com/products/airmagnet-survey">Airmagnet</a> and my European colleagues like <a href="http://www.ekahau.com/">Ekahau</a> for site survey and interference measurements. These are professional tools and cost a lot of money. I have one of the MetaGeek devices and it is fine for quick-check work but for anything series, you might need something better.<br />
</p><blockquote><blockquote><p>A recommendation on a hardware solution for WLAN packet caputer. Is Airpcap the way to go?</p></blockquote></blockquote><p>I specifically would not recommend AirPcap. They are not capable enough and they are not keeping up with technology. For real work, you will want OmniPeek with the WiFi adapters - they have bundles for both 802.11n (3ss) and 802.11ac(2ss) capture. This will meet demands of most devices today but even this is ageing - newest laptops are 3 spatial streams for 802.11ac. Alternatively, if you have Linux skills, that can be a solution to a point. 802.11n with 3ss is doable, but 802.11ac is tough. It's possible, but I need a PCIe or M.2 card to do it, and having a mobile solution with a bunch of M.2 cards is not that easy to put together. Plus these devices all crash often in Linux. The Windows ones do too, but not as often. Its to the point that if I REALLY need the wireless capture, I will use a minimum of two, sometimes three, separate systems for capture redundancy.<br />
</p><p>To go all the way with full capability, use one of the Cisco lightweight APs that is 3 or 4ss and put it into sniffer mode and send the frames over to a PC with either Wireshark or OmniPeek. This will get you current technology at quite a price tag. Aruba has some instant APs that I recall will do sniffer as well, so that could avoid having to get a controller. Either way, it's not cheap or really portable without a healthy UPS.<br />
</p><p>Don't forget a MacBook - out of the box can do monitor mode. If you only need one channel (i.e. no roaming issues) then don't discount this as an all-in-one tool. Install Wireshark and away you go.</p><blockquote><blockquote><p>An experienced &amp; patient individual who can teach me the nuts and bolts on packet analysis and troubleshooting at that level. I can only absorb so much from Youtube videos and online tutorials and would be happy to pay for the expertise of a network guru.</p></blockquote></blockquote><p>Your best bet is to find someone local. Not saying it can't be done over collaborations tools, but nothing like being able to throw the capture tool at someone! This site, too, is amazing. I look at wireless packet captures every day in my day job but the people on this site blow me away with what they know about networks and protocols. The expertise on here is impressive - and usually free.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '16, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Sep '16, 14:15</strong> </span></p></div></div><div id="comments-container-55360" class="comments-container"><span id="55374"></span><div id="comment-55374" class="comment"><div id="post-55374-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the feedback and recommendations. Yes, I'd love to find someone local (Atlanta) to help us, but not sure on the best resource. I figured this would be a good starting point</p></div><div id="comment-55374-info" class="comment-info"><span class="comment-age">(07 Sep '16, 08:03)</span> <span class="comment-user userinfo">arib1</span></div></div></div><div id="comment-tools-55360" class="comment-tools"></div><div class="clear"></div><div id="comment-55360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

