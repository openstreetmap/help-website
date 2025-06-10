+++
type = "question"
title = "Using different city names"
description = '''Hi, I am using Overpass API to count the number of POIs for different categories and for different cities. However, the the city names I use, sometimes don&#x27;t match the ones tagged in OSM. Example: I use &quot;Southbridge Town&quot; but in OSM is listed as &quot;Southbridge&quot; (sometimes using &quot;Southbridge Town&quot; retu...'''
date = "2022-03-09T10:24:00Z"
lastmod = "2022-03-09T19:14:00Z"
weight = 83760
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/83760" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using different city names](/questions/83760/using-different-city-names)

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
<span id="post-83760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83760-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am using Overpass API to count the number of POIs for different categories and for different cities. However, the the city names I use, sometimes don't match the ones tagged in OSM.</p>
<p>Example: I use "Southbridge Town" but in OSM is listed as "Southbridge" (sometimes using "Southbridge Town" returns some POIs)</p>
<p>Example request:</p>
<pre><code>[out:json][timeout:600];
area[admin_level=4][&quot;name&quot;=&quot;Massachusetts&quot;]-&gt;.country;
area[place~&quot;city|village|town|locality&quot;][&quot;name&quot;=&quot;Southbridge Town&quot;]-&gt;.city;
area[&quot;addr:city&quot;=&quot;Southbridge Town&quot;]-&gt;.address;
(
nwr(area.country)(area.city)[&quot;amenity&quot;~&quot;school&quot;];
nwr(area.country)(area.address)[&quot;amenity&quot;~&quot;school&quot;];
);     
out count;</code></pre>
<p>I am looking for a general method for matching my city names with the ones used in OSM using regular expressions or Overpass tools. I use Python to build the query and make the request.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '22, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e1355929c54f543d740a00e29c063c3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ocabanas&#39;s gravatar image" />
<p><span>ocabanas</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ocabanas has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '22, 18:20</strong> </span></p>
</div>
</div>
<div id="comments-container-83760" class="comments-container">
&#10;</div>
<div id="comment-tools-83760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83760-form-container" class="comment-form-container">
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

<span id="83767"></span>

<div id="answer-container-83767" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83767-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First to answer your question the solution is ot use the 'something like' operative which you've already used - <code>[name~"Southbridge"]</code></p>
<p>However it's not required as there's only one Southbridge place.</p>
<p><code>addr:city</code> is a tag of an object &amp; can not be used to construct areas.</p>
<p>This routine returns the same results as your routine</p>
<pre><code>area[admin_level=4][name=Massachusetts];
rel(area)[place=town][name=Southbridge];
map_to_area;
nwr(area)[amenity=school];
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '22, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83767" class="comments-container">
<span id="83768"></span>
<div id="comment-83768" class="comment">
<div id="post-83768-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There was an error in my initial question. I use ["name"="Southbridge Town"] and it should be recognized as "Southbridge". Also, using "addr:city" works well in my tests.</p>
</div>
<div id="comment-83768-info" class="comment-info">
<span class="comment-age">(09 Mar '22, 18:23)</span> <span class="comment-user userinfo">ocabanas</span>
</div>
</div>
<span id="83770"></span>
<div id="comment-83770" class="comment">
<div id="post-83770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Show the areas produced by the addr:city line.</p>
<p>The are no 2Southbridge Town" objects. <a href="https://overpass-turbo.eu/s/1gLY">https://overpass-turbo.eu/s/1gLY</a></p>
</div>
<div id="comment-83770-info" class="comment-info">
<span class="comment-age">(09 Mar '22, 19:14)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-83767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83767-form-container" class="comment-form-container">
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

