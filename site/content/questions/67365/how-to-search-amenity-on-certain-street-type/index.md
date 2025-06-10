+++
type = "question"
title = "How to search amenity on certain street type ?"
description = '''Hi, I am a volunteer in my small city for the security committee. We have a school near a &quot;main&quot; road and there is some security issue with the students and the traffic. A new planned development will increase dramatically the traffic in the next year. I would like to search other city in the area, ...'''
date = "2018-12-27T15:39:00Z"
lastmod = "2019-01-04T07:54:00Z"
weight = 67365
keywords = [ "school", "nominatim", "street", "searching", "amenity" ]
aliases = [ "/questions/67365" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to search amenity on certain street type ?](/questions/67365/how-to-search-amenity-on-certain-street-type)

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
<span id="post-67365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67365-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am a volunteer in my small city for the security committee.</p>
<p>We have a school near a "main" road and there is some security issue with the students and the traffic. A new planned development will increase dramatically the traffic in the next year.</p>
<p>I would like to search other city in the area, state, where a school is close to a main road (sometimes the postal address might be on a perpendicular street).</p>
<p>I tried using nominatim, but I don't think I have the correct coding sentence. I can find school in cities or area, but not based on the street type.</p>
<p>Any help ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-searching" rel="tag" title="see questions tagged &#39;searching&#39;">searching</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '18, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/8e2e222ea9f8740f424e5e268e4c6c53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Watever&#39;s gravatar image" />
<p><span>Watever</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Watever has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Dec '18, 19:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-67365" class="comments-container">
&#10;</div>
<div id="comment-tools-67365" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67365-form-container" class="comment-form-container">
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

<span id="67367"></span>

<div id="answer-container-67367" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67367-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is likely difficult to do in a meaningful way, but you will get some hits with an adaption of <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Banks_far_away_from_police_stations">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Banks_far_away_from_police_stations</a></p>
<p>See <a href="http://overpass-turbo.eu/s/ENe">http://overpass-turbo.eu/s/ENe</a></p>
<pre><code>[out:json][timeout:25];
// gather results
(
  node[amenity=school]({{bbox}});
  way[amenity=school]({{bbox}});
  rel[amenity=school]({{bbox}});
)-&gt;.schools;
(
  way[highway=primary]({{bbox}});
)-&gt;.primaries; //
&#10;(
  node.schools(around.primaries:200);
  way.schools(around.primaries:200);
  rel.schools(around.primaries:200);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>This will give you all schools in the bounding box that are near (200m) to a primary road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '18, 19:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Dec '18, 19:19</strong> </span></p>
</div>
</div>
<div id="comments-container-67367" class="comments-container">
<span id="67447"></span>
<div id="comment-67447" class="comment">
<div id="post-67447-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much !</p>
</div>
<div id="comment-67447-info" class="comment-info">
<span class="comment-age">(04 Jan '19, 02:51)</span> <span class="comment-user userinfo">Watever</span>
</div>
</div>
<span id="67448"></span>
<div id="comment-67448" class="comment">
<div id="post-67448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This worked. I changed it to have it for 25 meters only. That way it limit the results and remove the school that are really close but not perpendicular.</p>
<p>I have been playing for over 2-3 hours to get some of the data out. I couldn't find how to send to csv, it also seems most of the schools outside of the large cities don't have much tags.</p>
<p>I was hopping to have address or coordinates, so the other members can see the location on google map and use google street view.</p>
<p>I got results in json, then using <a href="http://geojson.io">http://geojson.io</a>, send it to CSV with all the coordinates. But theses do not work in google map. I am getting results in antarctica... Getting a little confuse now.</p>
</div>
<div id="comment-67448-info" class="comment-info">
<span class="comment-age">(04 Jan '19, 02:57)</span> <span class="comment-user userinfo">Watever</span>
</div>
</div>
<span id="67449"></span>
<div id="comment-67449" class="comment">
<div id="post-67449-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>why don't you try <a href="http://umap.openstreetmap.fr">http://umap.openstreetmap.fr</a> instead of Google ?</p>
<p>Are you sure that you did not switch lat/long, or that your workflow did not replace a decimal dot with a comma or another mistake in lat/long expectations of G-maps.</p>
</div>
<div id="comment-67449-info" class="comment-info">
<span class="comment-age">(04 Jan '19, 04:16)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="67450"></span>
<div id="comment-67450" class="comment">
<div id="post-67450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you mix lat and lon?</p>
<p>For <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#CSV_output_mode">CSV output</a> use <code>[out:csv(...)]</code> in combination with <code>out center</code>. <a href="https://overpass-turbo.eu/s/EXu">Example</a>:</p>
<pre><code>[out:csv(::id, ::type, ::lat, ::lon, amenity, name)][timeout:25];
// gather results
(
  node[amenity=school]({{bbox}});
  way[amenity=school]({{bbox}});
  rel[amenity=school]({{bbox}});
)-&gt;.schools;
(
  way[highway=primary]({{bbox}});
)-&gt;.primaries; //
&#10;(
  node.schools(around.primaries:200);
  way.schools(around.primaries:200);
  rel.schools(around.primaries:200);
);
// print results
out center;</code></pre>
</div>
<div id="comment-67450-info" class="comment-info">
<span class="comment-age">(04 Jan '19, 07:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67367-form-container" class="comment-form-container">
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

