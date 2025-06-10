+++
type = "question"
title = "service timed out"
description = '''We&#x27;re receiving timeout errors this morning. Is the nominatim service down? _call_geocoder  raise GeocoderTimedOut(&#x27;Service timed out&#x27;) GeocoderTimedOut: Service timed out'''
date = "2017-05-08T16:24:00Z"
lastmod = "2017-05-24T22:53:00Z"
weight = 56086
keywords = [ "nominatim" ]
aliases = [ "/questions/56086" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [service timed out](/questions/56086/service-timed-out)

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
<span id="post-56086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We're receiving timeout errors this morning. Is the nominatim service down?</p>
<p>_call_geocoder raise GeocoderTimedOut('Service timed out') GeocoderTimedOut: Service timed out</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '17, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/2d84322421c1c1015b13fec5689ac625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gadgroup&#39;s gravatar image" />
<p><span>gadgroup</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gadgroup has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56086" class="comments-container">
<span id="56088"></span>
<div id="comment-56088" class="comment">
<div id="post-56088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There seem to be sporadic problems at <a href="http://nominatim.openstreetmap.org">http://nominatim.openstreetmap.org</a>. Sometimes it is working, sometimes I'm receiving a 503 Service Unavailable.</p>
</div>
<div id="comment-56088-info" class="comment-info">
<span class="comment-age">(08 May '17, 16:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56089"></span>
<div id="comment-56089" class="comment">
<div id="post-56089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm calling the service from a python program using the following...</p>
<pre><code># Initialize the Geo Locator
 geolocator = Nominatim()</code></pre>
<p>Then sending a location.....</p>
<p>My log file is reporting the following...</p>
<p>_call_geocoder raise GeocoderTimedOut('Service timed out') GeocoderTimedOut: Service timed out</p>
</div>
<div id="comment-56089-info" class="comment-info">
<span class="comment-age">(08 May '17, 16:53)</span> <span class="comment-user userinfo">gadgroup</span>
</div>
</div>
</div>
<div id="comment-tools-56086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56086-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="56306"></span>

<div id="answer-container-56306" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56306-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The server is again having trouble with users over-using the service. Remember that we are running on volunteer-run machines with limited resources. So when you are seeing <code>Service timed out</code> errors, you can help greatly by stopping your scripts for a while until admins have taken measures to get the traffic under control.</p>
<p>Given that Python scripts are a significant contributor to the server issues, I'd like to remind everybody at this point that we have a <a href="https://operations.osmfoundation.org/policies/nominatim/">usage policy</a>. Among other things, you should be</p>
<ul>
<li>sending a user agent other than <code>Python-urllib</code> and</li>
<li>limit your queries to 1 request per second.</li>
</ul>
<p>It would be greatly appreciated if you could take a minute and check that your script fulfills these requirements.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '17, 22:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-56306" class="comments-container">
&#10;</div>
<div id="comment-tools-56306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56306-form-container" class="comment-form-container">
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

