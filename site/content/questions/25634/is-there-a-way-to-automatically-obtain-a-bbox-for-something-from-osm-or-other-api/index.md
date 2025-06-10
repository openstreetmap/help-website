+++
type = "question"
title = "Is there a way to automatically obtain a BBOX for something from OSM or other api"
description = '''Is there maybe any new easy way or api to get the BBOX of the city to use in mapnik to generate tiles? For example if I have Paris, London, Hong-Kong etc.  How can I automatically or semiautomatically from some API get the BBOX of those cities, and then use it in mapnik&#x27;s generate_tiles.py ???? '''
date = "2013-08-22T07:37:00Z"
lastmod = "2013-09-07T17:50:00Z"
weight = 25634
keywords = [ "bbox" ]
aliases = [ "/questions/25634" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to automatically obtain a BBOX for something from OSM or other api](/questions/25634/is-there-a-way-to-automatically-obtain-a-bbox-for-something-from-osm-or-other-api)

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
<span id="post-25634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25634-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there maybe any new easy way or api to get the BBOX of the city to use in mapnik to generate tiles?</p>
<p>For example if I have Paris, London, Hong-Kong etc.</p>
<p>How can I automatically or semiautomatically from some API get the BBOX of those cities, and then use it in mapnik's generate_tiles.py ????</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '13, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '13, 09:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-25634" class="comments-container">
<span id="26179"></span>
<div id="comment-26179" class="comment">
<div id="post-26179-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have found out that Yahoo Geo Api gives exactly what I want! You search for a city, and it gives you bounding box points!</p>
</div>
<div id="comment-26179-info" class="comment-info">
<span class="comment-age">(07 Sep '13, 17:50)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
</div>
<div id="comment-tools-25634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25634-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="25639"></span>

<div id="answer-container-25639" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25639-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are numerous ways to find a bbox manually: Overpass Turbo and the BBBike site are two which enable one to draw a box.</p>
<p>You, however, ask for an automated way. Probably the easiest way is to use <a href="http://wiki.openstreetmap.org/wiki/Nominatim#Search">Nominatim</a> which returns a bounding box as part of its XML format. Care needs to taken with this because you may find yourself getting the node which marks the centre of a city rather than its administrative extent. Also, if by Paris, you mean the Parisian Metropolitan area then I think you can't get this from Nominatim.</p>
<p>Lastly, do not think of then using the bbox returned for direct API queries. The amount of data contained in the areas of large cities is very large, and this is not appropriate usage of the API: consider Overpass or similar methods.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '13, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-25639" class="comments-container">
<span id="25641"></span>
<div id="comment-25641" class="comment">
<div id="post-25641-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't want to draw anything. Each city has a polygonal outlined relations. There should be some way to request those and on basis of that calculate the quadrate. No?</p>
</div>
<div id="comment-25641-info" class="comment-info">
<span class="comment-age">(22 Aug '13, 10:21)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="25642"></span>
<div id="comment-25642" class="comment">
<div id="post-25642-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do please read the answer, which is in the second paragraph (i.e., Nominatim).</p>
<p>Your question did not emphasise your desire for an automated approach, and at first glance seemed to ask how to find a bbox for a city.</p>
</div>
<div id="comment-25642-info" class="comment-info">
<span class="comment-age">(22 Aug '13, 10:24)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="25648"></span>
<div id="comment-25648" class="comment">
<div id="post-25648-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could also take a look at <a href="http://maposmatic.org/">http://maposmatic.org/</a> 's code to see how they implemented the feature you describe, as part of a nice user interface.</p>
</div>
<div id="comment-25648-info" class="comment-info">
<span class="comment-age">(22 Aug '13, 12:22)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25639-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25635"></span>

<div id="answer-container-25635" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25635-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you know the coordinates, you can download the data with</p>
<pre><code>http://overpass-api.de/api/map?bbox=lower_lon,lower_lat,upper_lon,upper_lat</code></pre>
<p>Other options for larger cities are <a href="http://download.geofabrik.de/">downloads from the Geofabrik</a>. Or <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#timeout">setting a larger timeout</a> on the respective <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Simplest_possible_map_call">Overpass API map query</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '13, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-25635" class="comments-container">
<span id="25636"></span>
<div id="comment-25636" class="comment">
<div id="post-25636-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The problem is that i don't know the BBOX itself. I need to generate tiles myself and not to download.</p>
</div>
<div id="comment-25636-info" class="comment-info">
<span class="comment-age">(22 Aug '13, 08:14)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
</div>
<div id="comment-tools-25635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25635-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25638"></span>

<div id="answer-container-25638" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25638-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can go to openstreetmap.org, select "export", and then "manually select a different area". Shift-drag the box to the size that you want. Don't click export - just use those numbers in <code>generate_tiles.py</code> (making sure that you've commented out any areas already in <code>generate_tiles.py</code>).</p>
<p>Another helpful site is <a href="http://osm.duschmarke.de/bbox.html">http://osm.duschmarke.de/bbox.html</a> - use alt-drag, and you'll see bbox examples suitable for lots of programs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '13, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '13, 09:25</strong> </span></p>
</div>
</div>
<div id="comments-container-25638" class="comments-container">
<span id="25640"></span>
<div id="comment-25640" class="comment">
<div id="post-25640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://osm.duschmarke.de/bbox.html">http://osm.duschmarke.de/bbox.html</a> is perfect, but it has to be done again manually. If there was city search on it would be much easier.</p>
</div>
<div id="comment-25640-info" class="comment-info">
<span class="comment-age">(22 Aug '13, 10:19)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="25666"></span>
<div id="comment-25666" class="comment">
<div id="post-25666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also have a look at the XAPI Query Builder:<br />
</p>
<p><a href="http://harrywood.co.uk/maps/uixapi/xapi.html">http://harrywood.co.uk/maps/uixapi/xapi.html</a></p>
<p>but it also has no search feature for a place name.</p>
</div>
<div id="comment-25666-info" class="comment-info">
<span class="comment-age">(22 Aug '13, 17:47)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-25638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25638-form-container" class="comment-form-container">
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

