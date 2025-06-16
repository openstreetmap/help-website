+++
type = "question"
title = "IP Geolocation"
description = '''We need to be able to put points on a map, based on IP address. Is this possible? What is the best way to geolocate By IP? Any suggestions are appreciated. Thanks!'''
date = "2012-10-17T15:54:00Z"
lastmod = "2023-03-28T10:07:00Z"
weight = 16965
keywords = [ "ip", "geocoding", "geolocation" ]
aliases = [ "/questions/16965" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [IP Geolocation](/questions/16965/ip-geolocation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16965-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We need to be able to put points on a map, based on IP address. Is this possible? What is the best way to geolocate By IP? Any suggestions are appreciated. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '12, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/fa58dbf18e3e3a4606bab8850485befd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bouncefish&#39;s gravatar image" />
<p><span>bouncefish</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bouncefish has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16965" class="comments-container">
<span id="17103"></span>
<div id="comment-17103" class="comment">
<div id="post-17103-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks everyone for their feedback!</p>
</div>
<div id="comment-17103-info" class="comment-info">
<span class="comment-age">(22 Oct '12, 16:22)</span> <span class="comment-user userinfo">bouncefish</span>
</div>
</div>
</div>
<div id="comment-tools-16965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16965-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="16979"></span>

<div id="answer-container-16979" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16979-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-16979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Best way? That depends on your needs. There are various APIs (some free) that you send the IP to and they return the approximate location. These would be fine for casual/light usage. If you need to do heavy work then you may be best to pull bulk geoip data down periodically into your own database and serve it out from there.</p>
<p>The thing to note about location based on IP is that the accuracy can range from very accurate to very inaccurate depening on many different factors and it's practically impossible to know in advance whether the result will be accurate or not! Using HTML5 geolocation (providing the client enables it) should offer better accuracy as it does not rely on IP address alone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '12, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7408fce5260e98922355385680be0179?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="porjo&#39;s gravatar image" />
<p><span>porjo</span><br />
<span class="score" title="183 reputation points">183</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="porjo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16979" class="comments-container">
&#10;</div>
<div id="comment-tools-16979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16979-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16978"></span>

<div id="answer-container-16978" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16978-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How to <a href="/questions/1778/how-can-i-display-a-map-with-multiple-markers">display a map with multiple markers</a> has already been answered and IP Geolocation is out of the scope of OSM (and there are multiple possibilities like a simple geoip database and the HTML5 geolocation feature).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '12, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16978" class="comments-container">
&#10;</div>
<div id="comment-tools-16978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16978-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17080"></span>

<div id="answer-container-17080" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17080-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>HTML5 geolocation provides you higher accuracy compare to IP geolocation, but, the drawbacks is, permission need to be explicitly granted from the end user for solution.</p>
<p>Getting location information from IP will be less intrusive and seamless way with a little bit trade off on the accuracy. Anyway, it's depend on the the nature of your solutions.</p>
<p>Anyway, both solution above shall provide you the latitude and longitude information enabling you to plot the marker in your map.</p>
<p>If you need information on the differences between these 2, this site shall be able to give you some idea: <a href="http://www.ipgeo5.com">ipgeo5.com</a> and <a href="http://www.ipinfodb.com">ipinfodb.com</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '12, 01:47</strong></p>
<img src="https://secure.gravatar.com/avatar/af34d2bd722a734b208f2164b8032c6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrislim2888&#39;s gravatar image" />
<p><span>chrislim2888</span><br />
<span class="score" title="30 reputation points">30</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrislim2888 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17080" class="comments-container">
<span id="17089"></span>
<div id="comment-17089" class="comment">
<div id="post-17089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you need it, here's a <a href="http://www.w3schools.com/html/html5_geolocation.asp">very simple HTML5 geolocation example</a>.</p>
</div>
<div id="comment-17089-info" class="comment-info">
<span class="comment-age">(22 Oct '12, 09:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17080-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79074"></span>

<div id="answer-container-79074" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79074-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you can use free IP geolocation API that provides point coordinates based on the IP address.</p>
<p>There are tonnes of IP geolocation APIs which can do the job. Try <a href="https://www.bigdatacloud.com/ip-geolocation-apis/ip-address-geolocation-with-confidence-area-and-hazard-report-api">BigDataCloud's IP geolocation API</a> which provides not just the coordinates of the IP address but also the area where the IP address might have been allocated. This is unique data that might be helpful.</p>
<p>They provide 10K queries per month for free and can be upgraded at a nominal feed.</p>
<p><img src="/upfiles/Screen_Shot_2021-03-01_at_11.58.51_am.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '21, 01:29</strong></p>
<img src="https://secure.gravatar.com/avatar/92f1d9e7e34bda0fbb8a8a5f46e1e6f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deepBDC&#39;s gravatar image" />
<p><span>deepBDC</span><br />
<span class="score" title="8 reputation points">8</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deepBDC has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-79074" class="comments-container">
&#10;</div>
<div id="comment-tools-79074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79074-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86991"></span>

<div id="answer-container-86991" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86991-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another provider that provides you with a really extensive and free dataset is <a href="https://ipbase.com"></a><a href="https://ipbase.com">https://ipbase.com</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '23, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/23cf56f6ddc62113a26b60ccdd4566bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndreasA1990&#39;s gravatar image" />
<p><span>AndreasA1990</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndreasA1990 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86991" class="comments-container">
&#10;</div>
<div id="comment-tools-86991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86991-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

