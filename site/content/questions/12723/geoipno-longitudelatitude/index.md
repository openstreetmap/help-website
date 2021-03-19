+++
type = "question"
title = "GeoIP...no longitude/latitude"
description = '''Hello All, I have installed the GeoIP database. I&#x27;ve pointed my wireshark to the correct database. But when I take a capture and go to statistics-endpoints, I do not see the Latitude/Longitude even for Public IP addresses. Does anyone know why its not working ?'''
date = "2012-07-14T22:38:00Z"
lastmod = "2012-10-02T19:07:00Z"
weight = 12723
keywords = [ "geoip" ]
aliases = [ "/questions/12723" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [GeoIP...no longitude/latitude](/questions/12723/geoipno-longitudelatitude)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12723-score" class="post-score" title="current number of votes">0</div><span id="post-12723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I have installed the GeoIP database. I've pointed my wireshark to the correct database. But when I take a capture and go to statistics-endpoints, I do not see the Latitude/Longitude even for Public IP addresses. Does anyone know why its not working ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-geoip" rel="tag" title="see questions tagged &#39;geoip&#39;">geoip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '12, 22:38</strong></p><img src="https://secure.gravatar.com/avatar/a465ff7d49c648c5acabe4ee20eb87c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parvikram&#39;s gravatar image" /><p><span>parvikram</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parvikram has no accepted answers">0%</span></p></div></div><div id="comments-container-12723" class="comments-container"></div><div id="comment-tools-12723" class="comment-tools"></div><div class="clear"></div><div id="comment-12723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12724"></span>

<div id="answer-container-12724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12724-score" class="post-score" title="current number of votes">2</div><span id="post-12724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It works with Wireshark 1.8.0 and the latest GeoLiteCity.dat file (just checked). So, did you read the GeoIP wiki?</p><blockquote><p><code>http://wiki.wireshark.org/HowToUseGeoIP</code><br />
</p></blockquote><p>There are several reasons why GeoIP Location does not work</p><ul><li>Wireshark is not compiled with GeoIP (see wiki)</li><li>You did not restart Wireshark after configuring GeoIP (see wiki)</li><li>You need at least these files for a decent result: GeoLiteCity.dat (city) and GeoIP.dat (country). They are stored in compressed format on Maxminds FTP server and you need to uncompress them (<a href="http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz">GeoLiteCity.dat.gz</a> and <a href="http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz">GeoIP.dat.zip</a>) !</li></ul><p>If you did all that and it still does not work:</p><ul><li>did you try the latest stable Wireshark (1.8.0)</li><li>do you see country and city</li><li>maybe the accuracy of the IP database is not good enough (free!) for your specific IP address</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '12, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '12, 06:33</strong> </span></p></div></div><div id="comments-container-12724" class="comments-container"><span id="12763"></span><div id="comment-12763" class="comment"><div id="post-12763-score" class="comment-score"></div><div class="comment-text"><ol><li>I do see "with GeoIP" in the Help-&gt; About</li><li>I have the latest version of Wireshark.</li><li>I've checked the path multiple times and extracted the data files.</li><li>I've restarted Wireshark after that .</li><li>Can anyone take a webex sometime and see what the issue is ? And yes, I do have a lot of Public IP addresses in my trace .</li></ol><p>I've at a loss as to where I might be going wrong. Have gone through almost all the blogs and checked almost everything.</p></div><div id="comment-12763-info" class="comment-info"><span class="comment-age">(16 Jul '12, 07:55)</span> <span class="comment-user userinfo">parvikram</span></div></div><span id="12769"></span><div id="comment-12769" class="comment"><div id="post-12769-score" class="comment-score"></div><div class="comment-text"><p>what is you OS?<br />
can you please post a screenshot?</p></div><div id="comment-12769-info" class="comment-info"><span class="comment-age">(16 Jul '12, 08:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12724" class="comment-tools"></div><div class="clear"></div><div id="comment-12724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14650"></span>

<div id="answer-container-14650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14650-score" class="post-score" title="current number of votes">0</div><span id="post-14650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to the <em>"<a href="http://ask.wireshark.org/questions/8961/geoip-nothing-shows-on-map">GeoIP Nothing Shows On Map</a>"</em> question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '12, 19:07</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div></div><div id="comments-container-14650" class="comments-container"></div><div id="comment-tools-14650" class="comment-tools"></div><div class="clear"></div><div id="comment-14650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

