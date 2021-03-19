+++
type = "question"
title = "Not all sites load, what is different?"
description = '''I have the problem that some webpages do not display any content but others do.  Im trying to figure out where this goes wrong and made 2 captures with wireshark. Siteone form the side loading not ok and Sitetwo from a site loading just fine.  http://ow.ly/M3wRO -siteone http://ow.ly/M3wXn -sitetwo ...'''
date = "2015-04-24T04:18:00Z"
lastmod = "2015-05-01T07:43:00Z"
weight = 41772
keywords = [ "capture", "http", "tcp", "wireshark" ]
aliases = [ "/questions/41772" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not all sites load, what is different?](/questions/41772/not-all-sites-load-what-is-different)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41772-score" class="post-score" title="current number of votes">0</div><span id="post-41772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the problem that some webpages do not display any content but others do. Im trying to figure out where this goes wrong and made 2 captures with wireshark. Siteone form the side loading not ok and Sitetwo from a site loading just fine. <a href="http://ow.ly/M3wRO">http://ow.ly/M3wRO</a> -siteone <a href="http://ow.ly/M3wXn">http://ow.ly/M3wXn</a> -sitetwo</p><p>In both captures i get messages that the "ethernet frame check sequence incorrect". So im not sure this is a problem. Where else could i look for to determine where this goes wrong ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/8cefdde8f03697913e850462ebd8a66d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="disinfector&#39;s gravatar image" /><p><span>disinfector</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="disinfector has no accepted answers">0%</span></p></div></div><div id="comments-container-41772" class="comments-container"><span id="41802"></span><div id="comment-41802" class="comment"><div id="post-41802-score" class="comment-score"></div><div class="comment-text"><p>which webpages are you traing to load in 'siteone' that fail?</p></div><div id="comment-41802-info" class="comment-info"><span class="comment-age">(24 Apr '15, 13:34)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="41907"></span><div id="comment-41907" class="comment"><div id="post-41907-score" class="comment-score"></div><div class="comment-text"><p>hi, that would be www.nu.nl</p></div><div id="comment-41907-info" class="comment-info"><span class="comment-age">(27 Apr '15, 23:42)</span> <span class="comment-user userinfo">disinfector</span></div></div><span id="41921"></span><div id="comment-41921" class="comment"><div id="post-41921-score" class="comment-score"></div><div class="comment-text"><p>These are not txt files, but pcap files. Please adjust their extension.</p></div><div id="comment-41921-info" class="comment-info"><span class="comment-age">(28 Apr '15, 09:02)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-41772" class="comment-tools"></div><div class="clear"></div><div id="comment-41772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41922"></span>

<div id="answer-container-41922" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41922-score" class="post-score" title="current number of votes">0</div><span id="post-41922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Seems like pure luck. Small differences in timing allow some retransmission to come through, in one case not the other, just enough the get the complete data stream into your host. I would seriously(!) look at the quality of your cabling, connectors, sockets, etc, especially when running at higher speeds.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41922" class="comments-container"><span id="42001"></span><div id="comment-42001" class="comment"><div id="post-42001-score" class="comment-score"></div><div class="comment-text"><p>we have replaced the router with a different version. Now it is working again. Strange thing is when we replaced the router with the exact same model we got the same weir results. Thanks for the help.</p></div><div id="comment-42001-info" class="comment-info"><span class="comment-age">(01 May '15, 07:43)</span> <span class="comment-user userinfo">disinfector</span></div></div></div><div id="comment-tools-41922" class="comment-tools"></div><div class="clear"></div><div id="comment-41922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

