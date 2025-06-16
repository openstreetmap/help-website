+++
type = "question"
title = "How do I geocode an address?"
description = '''Hello guys!! I&#x27;m pretty new in this openstreetmaps world, and I just want to know if the service provides a gecodification service as google, like this : http://maps.google.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&amp;amp;sensor=false This will return a json file wi...'''
date = "2011-11-26T20:23:00Z"
lastmod = "2014-05-08T03:33:00Z"
weight = 9237
keywords = [ "geocoding", "address" ]
aliases = [ "/questions/9237" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I geocode an address?](/questions/9237/how-do-i-geocode-an-address)

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
<span id="post-9237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9237-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello guys!! I'm pretty new in this openstreetmaps world, and I just want to know if the service provides a gecodification service as google, like this :</p>
<p><a href="http://maps.google.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&amp;sensor=false">http://maps.google.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&amp;sensor=false</a></p>
<p>This will return a json file with all the info of the address. The main problem is that google only provides this service 2500 times per 24 hours. And I would like to know if openstreetmaps provides the same information and with what kind of restrictions.</p>
<p>Many thanks in advance!!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '11, 20:23</strong></p>
<img src="https://secure.gravatar.com/avatar/78d44fb18a26323cea55b397ce197fae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mandm&#39;s gravatar image" />
<p><span>mandm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mandm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '11, 16:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-9237" class="comments-container">
&#10;</div>
<div id="comment-tools-9237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9237-form-container" class="comment-form-container">
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

<span id="9238"></span>

<div id="answer-container-9238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9238-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, read the <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Parameters">Nominatim docs</a>, since it is currently hosted by Mapquest there is currently no such limit, but a max of 50k requests per day was <a href="http://gis.638310.n2.nabble.com/Reverse-geocoding-on-Nominatim-acceptable-volumes-td5672254.html">mentioned on the mailing list</a>. But as always with webservices (like Googles services as well), ToS can change at anytime.</p>
<p>If you search like this:</p>
<p><a href="http://open.mapquestapi.com/nominatim/v1/search/us/ca/1600+Amphitheatre+Parkway,+Mountain+View,+CA?format=json&amp;polygon=1&amp;addressdetails=1">http://open.mapquestapi.com/nominatim/v1/search/us/ca/1600+Amphitheatre+Parkway,+Mountain+View,+CA?format=json&amp;polygon=1&amp;addressdetails=1</a></p>
<p>Will results in a json response including these matches:</p>
<pre><code>&quot;Mountainview Avenue, Woodlake, Tulare, California, 93286, United States of America&quot;,
&quot;Mountainview Lane, Orange, California, 92648, United States of America&quot;,
&quot;Mountainview Circle, Santa Clara, Santa Clara County, California, 95037, United States of America&quot;,
&quot;Mountainview Drive, Lakeshore, Placer, California, 95650, United States of America&quot;,
&quot;Mountainview Road, Lancaster, Kern, California, 93501, United States of America&quot;,
&quot;North Mountainview Avenue, Pomona, Los Angeles, California, 91767, United States of America&quot;,
&quot;Mountainview Road, Orange, California, 92678, United States of America&quot;,
&quot;Mountainview Place, Lafayette, Contra Costa, California, 94549, United States of America&quot;,
&quot;Mountainview Lane, Lafayette, Contra Costa, California, 94549, United States of America&quot;,</code></pre>
<p>You can limit you search by adding country code in front, which I find very convenient if you are doing matches out side of the USA. The MQ Nominatim does things like LA -&gt; Louisiana, which makes a search for "La Paz" kind of hard.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '11, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Nov '11, 04:56</strong> </span></p>
</div>
</div>
<div id="comments-container-9238" class="comments-container">
<span id="9260"></span>
<div id="comment-9260" class="comment">
<div id="post-9260-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Many thanks for the useful answer emj.</p>
<p>I was looking around the web trying to find the limits or restrictions of nominatim, and I didn't find it.</p>
<p>Here's a link talking about that : <a href="http://gis.638310.n2.nabble.com/Reverse-geocoding-on-Nominatim-acceptable-volumes-td5672254.html">http://gis.638310.n2.nabble.com/Reverse-geocoding-on-Nominatim-acceptable-volumes-td5672254.html</a></p>
<p>Thank you emj.</p>
<p>Regards.</p>
</div>
<div id="comment-9260-info" class="comment-info">
<span class="comment-age">(28 Nov '11, 13:34)</span> <span class="comment-user userinfo">mandm</span>
</div>
</div>
<span id="9276"></span>
<div id="comment-9276" class="comment">
<div id="post-9276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you want to click "accept answer"?</p>
</div>
<div id="comment-9276-info" class="comment-info">
<span class="comment-age">(29 Nov '11, 04:42)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="32958"></span>
<div id="comment-32958" class="comment">
<div id="post-32958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@mandm</span>, the link is dead</p>
</div>
<div id="comment-32958-info" class="comment-info">
<span class="comment-age">(08 May '14, 03:33)</span> <span class="comment-user userinfo">TomM</span>
</div>
</div>
</div>
<div id="comment-tools-9238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9238-form-container" class="comment-form-container">
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

