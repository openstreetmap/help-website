+++
type = "question"
title = "How to filter data"
description = '''Hello I try to filter the power line out of openstreetmap. The problem is i can&#x27;t open the whole data and filter them later because the data are to big. So I&#x27;m looking for a programm what filters the data I need. I already tried a programm from the University of Stuttgard. With that programm you fil...'''
date = "2012-11-21T14:18:00Z"
lastmod = "2012-11-26T17:37:00Z"
weight = 17864
keywords = [ "filter" ]
aliases = [ "/questions/17864" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter data](/questions/17864/how-to-filter-data)

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
<span id="post-17864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17864-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello I try to filter the power line out of openstreetmap. The problem is i can't open the whole data and filter them later because the data are to big. So I'm looking for a programm what filters the data I need. I already tried a programm from the University of Stuttgard. With that programm you filter your data out of the osmosis database via the URL: <a href="http://www.faveve.uni-stuttgart.de/~troll/OSM/osm-poll.cgi?format=gpx&amp;filename=baenke&amp;query=%5Bamenity=bench%5D%5Bbbox=11.28,49.57,11.4,49.68%5D">http://www.faveve.uni-stuttgart.de/~troll/OSM/osm-poll.cgi?format=gpx&amp;filename=baenke&amp;query=[amenity=bench][bbox=11.28,49.57,11.4,49.68]</a> This is an example for all bench there are in a small area around the city semmelsdorf. The example worked perfectly, but when I tried to filter the powerline it did'nt work anymore. Is there any other chance to filter the data of all power lines of a whole country? Thanks for the help. Gesa</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '12, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/9e00b0d834699c374a4e3b1677139f35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="member100&#39;s gravatar image" />
<p><span>member100</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="member100 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17864" class="comments-container">
&#10;</div>
<div id="comment-tools-17864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17864-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="17866"></span>

<div id="answer-container-17866" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17866-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="member100 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, that is possible. Try</p>
<pre><code>(way[power=line](50.6,7.0,50.8,7.3);rel[power=line](50.6,7.0,50.8,7.3););(._;&gt;;);out;</code></pre>
<p>on <a href="http://overpass-api.de/query_form.html">http://overpass-api.de/query_form.html</a></p>
<p>Please note that "50.6,7.0,50.8,7.3" is the bounding box in order "min_lat,min_lon,max_lat,max_lon" (instead of "lon, lat") and that the bounding bix is repeated twice. If you want such a big bounding box that the query takes more than 3 minutes, you need to preceed "[timeout:900]", where 900 is the number of seconds maximum runtime:</p>
<pre><code>[timeout:900];(way[power=line](50.6,7.0,50.8,7.3);rel[power=line](50.6,7.0,50.8,7.3););(._;&gt;;);out;</code></pre>
<p>Longer times are also possible. If the program you want to process the data with afterwards complains about missing version information, please change "out" to "out meta" (this adds the needed extra data but is significantly slower):</p>
<pre><code>(way[power=line](50.6,7.0,50.8,7.3);rel[power=line](50.6,7.0,50.8,7.3););(._;&gt;;);out meta;</code></pre>
<p>To finally convert to GPX, please have a look a <a href="http://forum.openstreetmap.org/viewtopic.php?id=14788">this forum thread</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '12, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '12, 15:02</strong> </span></p>
</div>
</div>
<div id="comments-container-17866" class="comments-container">
<span id="17983"></span>
<div id="comment-17983" class="comment">
<div id="post-17983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Roland, thanks for the fast answer. But I tried your programm and when I tried (way<a href="47.25,5.69,55.14,15.22">power=line</a>;rel<a href="47.25,5.69,55.14,15.22">power=line</a>;);(.<em>;&gt;;);out meta; to get the whole data of germany. But my data file is just 341 Bytes big and doesn't have the information ein need. When I use a smaller area like: (way<a href="47.25,5.69,50.14,10.22">power=line</a>;rel<a href="47.25,5.69,50.14,10.22">power=line</a>;);(.</em>;&gt;;);out meta; the programm worked fine. Is there a limit, thats why it doesn't work with the first coordinates? Thanks for your help</p>
</div>
<div id="comment-17983-info" class="comment-info">
<span class="comment-age">(26 Nov '12, 12:44)</span> <span class="comment-user userinfo">member100</span>
</div>
</div>
<span id="17985"></span>
<div id="comment-17985" class="comment">
<div id="post-17985-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, there is a limit. If a query comes without speical mark, it is terminated after 3 minutes. Please read <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#timeout">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#timeout</a></p>
<p>You can start your query with "[timeout:900];" or a higher value to let the query longer running.</p>
</div>
<div id="comment-17985-info" class="comment-info">
<span class="comment-age">(26 Nov '12, 17:37)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-17866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17866-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17871"></span>

<div id="answer-container-17871" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17871-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the program called <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">Osmfilter</a>.</p>
<p>You can download an OSM raw data country extract e.g. from geofabrik.de and (if neccesary) convert it with osmconvert.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '12, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-17871" class="comments-container">
&#10;</div>
<div id="comment-tools-17871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17871-form-container" class="comment-form-container">
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

