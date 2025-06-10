+++
type = "question"
title = "How to view past years maps (2010-2020)"
description = '''Hi everyone! I am a final year student at my university, currently working on my project on rising popularity of coffee shops in the UK and Warwickshire specifically, and their market entry/exit decisions.  My theory is if a coffee shop is not on the map in the year, e.g 2008, but it is in years 200...'''
date = "2020-01-21T21:51:00Z"
lastmod = "2020-01-22T13:39:00Z"
weight = 72598
keywords = [ "past", "cafe", "old", "oldmap" ]
aliases = [ "/questions/72598" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to view past years maps (2010-2020)](/questions/72598/how-to-view-past-years-maps-2010-2020)

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
<span id="post-72598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72598-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>I am a final year student at my university, currently working on my project on rising popularity of coffee shops in the UK and Warwickshire specifically, and their market entry/exit decisions.</p>
<p>My theory is if a coffee shop is not on the map in the year, e.g 2008, but it is in years 2009 - 2013, and is not in 2014, it would mean it entered the market in 2009 and exited in 2014.</p>
<p>I am well aware this method has flaws and limitations, for instance the coffee shop might have been opened in 2000 but only appeared on a map in 2009.</p>
<p>Hopefully, someone would be able to help me.</p>
<p>Regards, M</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-past" rel="tag" title="see questions tagged &#39;past&#39;">past</span> <span class="post-tag tag-link-cafe" rel="tag" title="see questions tagged &#39;cafe&#39;">cafe</span> <span class="post-tag tag-link-old" rel="tag" title="see questions tagged &#39;old&#39;">old</span> <span class="post-tag tag-link-oldmap" rel="tag" title="see questions tagged &#39;oldmap&#39;">oldmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '20, 21:51</strong></p>
<img src="https://secure.gravatar.com/avatar/370ade38bcce8b55be675aa71e164c21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikhailL&#39;s gravatar image" />
<p><span>MikhailL</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikhailL has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72598" class="comments-container">
&#10;</div>
<div id="comment-tools-72598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72598-form-container" class="comment-form-container">
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

<span id="72605"></span>

<div id="answer-container-72605" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72605-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-72605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> has said the key issue is that many are unlikely to have been mapped, particularly in the timeframe before around 2014. You may be interested in <a href="https://sk53-osm.blogspot.com/2018/07/can-we-identify-completeness-of.html">some work</a> I did on patterns of mapping retail outlets over time by local authority area.</p>
<p>You could use my techniques to get historical data for all cafes in Warwickshire mapped on OSM. It's fairly technical and requires compiling osmium-tool, some UNIX scripting and familiarity with SQL and PostGIS.</p>
<p>An alternative for smaller areas is to run a series of overpass queries with attic data. Unfortunately these only go back to Sept 2012, but they're certainly a way of sense checking the approach. These queries are for cafes in Warwickshire on <a href="https://overpass-turbo.eu/s/PZg">30th Sept 2012</a> (200 ish) and <a href="https://overpass-turbo.eu/s/PZe">now</a> (~580).</p>
<p>Another source of data which may work for some local authorities, and which ought to not suffer from the completeness issue, is Food Hygiene Ratings (FHRS). The FSA do not publish historical data, but may retain it. I have complete dumps of this data for various dates between (roughly) 2013 and 2017.</p>
<p>Lastly both OSM and FHRS have a generic café description. Not all cafes will be coffee shops, some will be tea shops and others greasy spoons. More recent entries may be dessert or shish cafes both of which I've noticed increasing in the past 5 years. I suspect most cafes are not tagged in detail as to precise type (and this is not available on FHRS which lumps them with restaurants).</p>
<p>For small areas standard on-line commercial directories may be a useful source of info as they seem to be very poor at removing outdated retail locations. Other places which could be useful to supplement a classification are local forums: people living in an area can often demonstrate fantastic recall of shops going back 50 years or so.</p>
<p>A couple of point items from Nottingham of coffee shop cafes which entered &amp; left the market in your timeframe: <a href="https://www.openstreetmap.org/node/2109855832">Smythsons</a> from 2012-2018, <a href="https://www.openstreetmap.org/way/241990245">Leaf &amp; Bean</a> 2013-2014, <a href="https://www.openstreetmap.org/way/100198312/history">The Footman's Rest</a> (not really a coffee shop), 2018-2019.</p>
<p>In practice I think you'll need to use multiple sources of data, but OSM may be a good start in Birmingham.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '20, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-72605" class="comments-container">
<span id="72609"></span>
<div id="comment-72609" class="comment">
<div id="post-72609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your help! I have already contacted Geofabrik and they gave me the history file for Warwickshire, however, I encountered some problems. I don't really care for specific types of coffee shops, as I am making a comparison between chains vs independents, however, it might be a good addition to the model. The problem is that some cafes are nodes whereas some are ways and even relations. So my question is whether it is possible to convert all of them into nodes (dots) whilst also saving data like name, address, type, etc. I was told I could do that by loading the OSM files for each year into a PostGIS database with osm2pgsql, however, I have very limited coding knowledge. Do you know if it is indeed a good way?</p>
</div>
<div id="comment-72609-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 12:50)</span> <span class="comment-user userinfo">MikhailL</span>
</div>
</div>
<span id="72610"></span>
<div id="comment-72610" class="comment">
<div id="post-72610-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can convert from ways to centroids using osmconvert, but I don't know if this works on history files (although some operations do work <a href="https://markiliffe.wordpress.com/tag/osmconvert/).">https://markiliffe.wordpress.com/tag/osmconvert/).</a> With a small file it's easy enough to try.</p>
<p>For limited data the overpass approach I described can be useful as you can save data as geojson and you can use out center to deliver the centroid rather than the polygon, and it also avoids the polygon assembly problem which plaques history files.</p>
<p>Certainly using PostGIS and SQL gives you the most control over your data, but QGIS is another possibility, which does allow converting line or area geometries to centroids.</p>
<p>If you want a more in-depth discussion feel free to contact me by email or OSM message (see <a href="https://wiki.openstreetmap.org/wiki/User:SK53)">https://wiki.openstreetmap.org/wiki/User:SK53)</a> as your problem interests me.</p>
</div>
<div id="comment-72610-info" class="comment-info">
<span class="comment-age">(22 Jan '20, 13:39)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-72605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72605-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72607"></span>

<div id="answer-container-72607" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72607-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll also have the problem that once an area has been "mapped", it relies on there being regular re-surveys to spot the changes - almost every time I go into my local town centre I notice at least one shop has changed, but that's without me even checking OSM and there might be many more. One non-coffee shop related example: Lloyds TSB split into two separate banks back in 2013 and we still have loads of objects bearing the "Lloyds TSB" name - <a href="https://overpass-turbo.eu/s/PZm">https://overpass-turbo.eu/s/PZm</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '20, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-72607" class="comments-container">
&#10;</div>
<div id="comment-tools-72607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72607-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72599"></span>

<div id="answer-container-72599" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72599-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem, as you already say, is:</p>
<pre><code>for instance the coffee shop might have been opened in 2000 but only appeared on a map in 2009.</code></pre>
<p>However, maybe you could try and control for "things being mapped in an area in OSM" by also taking into account:</p>
<ul>
<li>Those coffee shops that took over existing premises (i.e. it was a different sort of shop, but is now a coffee shop)</li>
<li>The rise of other shops in the same area. If a coffee shop "appeared" on the street at the same time as all the other shops, then clearly that street was only mapped at all at the time that they all appeared.</li>
</ul>
<p>If you're not interested in the overall numbers of coffee shops and just want a few case studies, then it's pretty straightforward. If you do want to measure overall numbers, then you'll need to use some clever statistics to model change. You won't be able to assume an even rate of mapping across the West Midlands, but you might be able to talk to some of the people who did it - try getting in touch with <a href="http://www.mappa-mercia.org/">Mappa Mercia</a>.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '20, 00:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72599" class="comments-container">
&#10;</div>
<div id="comment-tools-72599" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72599-form-container" class="comment-form-container">
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

