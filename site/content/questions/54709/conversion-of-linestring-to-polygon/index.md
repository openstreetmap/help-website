+++
type = "question"
title = "Conversion of LineString to Polygon"
description = '''I am using overpass api to get the OpenStreetMap data. I have a following query: [out:json][timeout:25]; // gather results (  // query part for: “&quot;Land Use&quot;”  way[&quot;landuse&quot;](around:1000, 49.058008 , 2.275715);  ); // print results out body; &amp;gt;; out skel qt;  Try it out here: http://overpass-turbo....'''
date = "2017-02-18T18:57:00Z"
lastmod = "2017-02-20T13:07:00Z"
weight = 54709
keywords = [ "overpass", "polygon", "area" ]
aliases = [ "/questions/54709" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Conversion of LineString to Polygon](/questions/54709/conversion-of-linestring-to-polygon)

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
<span id="post-54709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54709-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using overpass api to get the OpenStreetMap data. I have a following query:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query part for: “&quot;Land Use&quot;”
  way[&quot;landuse&quot;](around:1000, 49.058008 , 2.275715);
&#10;);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>Try it out here: <a href="http://overpass-turbo.eu/s/mOu">http://overpass-turbo.eu/s/mOu</a></p>
<p>The problem is that it always returns LineString instead of Polygons. I would like to convert LineString to Polygon in order to use this data for intersection analysis of different Polygons. Is there a way to convert LineString to Polygon(e.g. with geoJSON library ), or should I change my query for this?</p>
<p>Thanks you in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '17, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/930511599dcc50013d959453f3d7b03c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tivalex&#39;s gravatar image" />
<p><span>tivalex</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tivalex has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Feb '17, 07:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-54709" class="comments-container">
<span id="54710"></span>
<div id="comment-54710" class="comment">
<div id="post-54710-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/42303410/convertion-of-linestring-to-polygon">https://stackoverflow.com/questions/42303410/convertion-of-linestring-to-polygon</a></p>
</div>
<div id="comment-54710-info" class="comment-info">
<span class="comment-age">(18 Feb '17, 19:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="54711"></span>
<div id="comment-54711" class="comment">
<div id="post-54711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even-though it is a crosspost neither community has given an answers so far.</p>
</div>
<div id="comment-54711-info" class="comment-info">
<span class="comment-age">(18 Feb '17, 19:54)</span> <span class="comment-user userinfo">tivalex</span>
</div>
</div>
<span id="54735"></span>
<div id="comment-54735" class="comment">
<div id="post-54735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13300/tivalex">@tivalex</a>: but, please, if you really need to crosspost, mention and link both. Also keep them in sync.</p>
</div>
<div id="comment-54735-info" class="comment-info">
<span class="comment-age">(19 Feb '17, 20:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="54736"></span>
<div id="comment-54736" class="comment">
<div id="post-54736-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I found the question a bit confusing: after a while I realised it was because you provide a link to Overpass-turbo from which one can save polygons. However that is not true of the Overpass API. Overpass-turbo uses <a href="https://github.com/tyrasd/osmtogeojson">https://github.com/tyrasd/osmtogeojson</a></p>
</div>
<div id="comment-54736-info" class="comment-info">
<span class="comment-age">(19 Feb '17, 22:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="54741"></span>
<div id="comment-54741" class="comment not_top_scorer">
<div id="post-54741-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for confusing you. Does your answer means that I can query raw OSM data and then convert it to a POLYGON or any other type of shape using osmtogeojson?</p>
</div>
<div id="comment-54741-info" class="comment-info">
<span class="comment-age">(20 Feb '17, 07:56)</span> <span class="comment-user userinfo">tivalex</span>
</div>
</div>
<span id="54746"></span>
<div id="comment-54746" class="comment">
<div id="post-54746-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Should be yes. There are similar queries on GIS Stackoverflow.</p>
</div>
<div id="comment-54746-info" class="comment-info">
<span class="comment-age">(20 Feb '17, 13:07)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54709" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-54709-form-container" class="comment-form-container">
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

<span id="54733"></span>

<div id="answer-container-54733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54733-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM only knows nodes, ways and relations. Ways can be closed in which case they form an area. So when you export a landuse via OverPass, you get a closed way. Isn't a polygon just another word for closed way ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '17, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-54733" class="comments-container">
<span id="54734"></span>
<div id="comment-54734" class="comment">
<div id="post-54734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for you answer. Indeed, it is a polygon,when it is a closed way and when the line does not intersect itself. Otherwise it is a more then one polygon. I would like to compute the area of these polygons. The problem is that I am not sure that it is possible, unless it is a polygon. I am using python shapely or gdal for this. So I started to think about conversion of the strngline to polygon.</p>
</div>
<div id="comment-54734-info" class="comment-info">
<span class="comment-age">(19 Feb '17, 20:31)</span> <span class="comment-user userinfo">tivalex</span>
</div>
</div>
<span id="54740"></span>
<div id="comment-54740" class="comment">
<div id="post-54740-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Since OSM does not know polygons, in which programming language are you working ? To find out whether an OSM way is a closed way, you could test whether the first and last point are the same, not ? So it is up to your processing software to determine whether a way is closed and if it is closed, calculate the area.</p>
</div>
<div id="comment-54740-info" class="comment-info">
<span class="comment-age">(20 Feb '17, 06:34)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="54742"></span>
<div id="comment-54742" class="comment">
<div id="post-54742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is totally make sense. However, I tought that there is some kind of a way to define a shape in the query. Or automatically convert Linestring to Polygon with help of some library. And I query only type of data that should be a polygon eg. landuse or building. Like described here: <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/Polygon_Features">https://wiki.openstreetmap.org/wiki/Overpass_turbo/Polygon_Features</a> Most likely I don't need to check whether it is a polygon or not. Asking to your question: I use Python for this.</p>
</div>
<div id="comment-54742-info" class="comment-info">
<span class="comment-age">(20 Feb '17, 08:07)</span> <span class="comment-user userinfo">tivalex</span>
</div>
</div>
</div>
<div id="comment-tools-54733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54733-form-container" class="comment-form-container">
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

