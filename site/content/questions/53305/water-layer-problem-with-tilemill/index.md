+++
type = "question"
title = "Water layer problem with Tilemill"
description = '''I&#x27;m currently using Tilemill on windows for designing maps. I noticed that there was a problem with the water layer for a particular city (Montreal). For example, some small islands of this city, like St-Helen, are completely covered with water. While other area came out as land instead of water. Is...'''
date = "2016-12-07T17:00:00Z"
lastmod = "2016-12-14T04:29:00Z"
weight = 53305
keywords = [ "water", "shapefile", "tilemill", "layer", "montreal" ]
aliases = [ "/questions/53305" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Water layer problem with Tilemill](/questions/53305/water-layer-problem-with-tilemill)

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
<span id="post-53305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53305-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently using Tilemill on windows for designing maps. I noticed that there was a problem with the water layer for a particular city (Montreal).</p>
<p>For example, some small islands of this city, like St-Helen, are completely covered with water. While other area came out as land instead of water. Is this a known problem ? Do I need some special shapefile or something to render the map ?</p>
<p><strong>2 screenshots:</strong></p>
<p>*<em>Picture #1 : (1) The island is covered with water. (2) This area should have been covered with water.</em></p>
<p><img src="http://help.openstreetmap.org/upfiles/prob1.jpg" alt="alt text" /></p>
<p><em>Picture #2 : I commented the line: <strong><em>polygon-fill: @water;</em></strong> so it is disabled (see red square #2). The island look normal now. It looks like the water layer bypass the others. It still doesn't explain why there is no water fill in the #2 red square in picture #1</em></p>
<p><img src="http://help.openstreetmap.org/upfiles/prob2_WxDNT9h.jpg" alt="alt text" /></p>
<p>Any help would be greatly appreciated! Ty in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-montreal" rel="tag" title="see questions tagged &#39;montreal&#39;">montreal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '16, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/91e9d7555ec6a5d6f6c4abd2313646fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanielQc&#39;s gravatar image" />
<p><span>DanielQc</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanielQc has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '16, 20:14</strong> </span></p>
</div>
</div>
<div id="comments-container-53305" class="comments-container">
<span id="53399"></span>
<div id="comment-53399" class="comment">
<div id="post-53399-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd also like to understand the reason behind this behavior. Why it's happening in the first place ?</p>
<p>I used the most recent map for this area on geofabrik. I confirm you that it's not from the map itself because when I imported it in JOSM, everything was correct. So it means, it must come from tilemill (and not from my map's extract.)</p>
<p>I also googled how to manually change the color for a specific area and I found nothing.. This workaround proposed could do the job. I'm not an expert and maybe it's something very simple that I missed.</p>
<p>Feel free to tell me if i'm not addressing my demand in the right forum.</p>
<p>ty again</p>
</div>
<div id="comment-53399-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 23:03)</span> <span class="comment-user userinfo">DanielQc</span>
</div>
</div>
</div>
<div id="comment-tools-53305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53305-form-container" class="comment-form-container">
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

<span id="53420"></span>

<div id="answer-container-53420" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53420-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DanielQc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a couple of possibilities - one is that the style you're using is getting confused by the riverbank (the relevant relation I think is <a href="http://www.openstreetmap.org/relation/1775822">this</a> one). The other is that someone that relation is somehow broken in your data. I wouldn't expect that to be the case, since that relation is fully within Quebec as defined at <a href="http://download.geofabrik.de/north-america/canada/quebec.html">Geofabrik</a>, assuming you didn't cut Quebec down any more before importing.</p>
<p>Another possibility is how Tilemill is accessing the data. You're using Tilemill on Windows - is that using an osm2pgsql database to render from, or are you doing something else? If it is a database, what are you using to import the data? If not, how is Tilemill accessing it?</p>
<p>In order to find out which is likely to be the problem, the first thing I'd do is to see if other similiar riverbank relations are rendered OK?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '16, 01:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Dec '16, 01:53</strong> </span></p>
</div>
</div>
<div id="comments-container-53420" class="comments-container">
<span id="53458"></span>
<div id="comment-53458" class="comment">
<div id="post-53458-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For info, I've just downloaded a Montreal metro extract from Mapzen, loaded it using osm2pgsql and had a look at it in OSMBright in TileMill. The water displays as water, and the Ile Ste Helene as land.</p>
<p>The OSMBright and TileMill versions are from around 2013, but I suspect that neither have changed much.</p>
</div>
<div id="comment-53458-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 13:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53420" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53420-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53450"></span>

<div id="answer-container-53450" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I did two tests from what you mentionned. First, I tried one specific area (ID : 156816898) from the <a href="http://www.openstreetmap.org/relation/1775822">link</a> you posted and I got the same problem. The island was also covered with water and St-Lawrence river was "land-filled". (sry no picture)</p>
<p>Then I did another test with Quebec city and the result was exactly like as expected. <img src="http://help.openstreetmap.org/upfiles/Sans_titre.png" alt="alt text" /></p>
<p>On the picture, you can see that the island on the top right is coming out correctly. Like you said, I’m supposing it is the style that get confused by the riverbank. But I don't know why the result is different for Montreal.</p>
<p>To answer your questions, I'm using osm2pgsql (PostgreSQL with PostGIS) for importing data. I installed everything from the following <a href="https://ircama.github.io/osm-carto-tutorials/tilemill-osm-carto">procedure</a>. Do you think the problem might come from openstreetmap carto ?</p>
<p>I also want to thank you for your elaborate answer. It's helping me and I’m feeling closer to a solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '16, 06:56</strong></p>
<img src="https://secure.gravatar.com/avatar/91e9d7555ec6a5d6f6c4abd2313646fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanielQc&#39;s gravatar image" />
<p><span>DanielQc</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanielQc has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '16, 06:58</strong> </span></p>
</div>
</div>
<div id="comments-container-53450" class="comments-container">
<span id="53457"></span>
<div id="comment-53457" class="comment">
<div id="post-53457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Out of interest, where did you get the data from? I'm wondering if whatever process was used could have chopped off part of the multipolygon.</p>
<p>Also I don't quite understand "Do you think the problem might come from openstreetmap carto" - it looks like you're using OSM Bright as a style not OSM Carto?</p>
</div>
<div id="comment-53457-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 13:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53469"></span>
<div id="comment-53469" class="comment">
<div id="post-53469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think I got confused.. I was thinking about the openstreetmap carto (or OSMBright)because I thought that maybe some tags were missing in the style (like Wetitpig0 proposed)</p>
</div>
<div id="comment-53469-info" class="comment-info">
<span class="comment-age">(10 Dec '16, 20:51)</span> <span class="comment-user userinfo">DanielQc</span>
</div>
</div>
</div>
<div id="comment-tools-53450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53450-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53454"></span>

<div id="answer-container-53454" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53454-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Problem should be fixed.</p>
<p>Whenever you get water-filled islands, most probably it is because there are no tags about whether it is an island or not. If that is the case, choose the area and tag it with "natural=coastline" &amp; "place=island".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '16, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-53454" class="comments-container">
&#10;</div>
<div id="comment-tools-53454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53454-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53322"></span>

<div id="answer-container-53322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53322-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just change the water-filled area by yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '16, 23:29</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-53322" class="comments-container">
<span id="53326"></span>
<div id="comment-53326" class="comment">
<div id="post-53326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ty for your answer. It looks simple. Maybe I missed something.. How may I do this ?</p>
</div>
<div id="comment-53326-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 00:27)</span> <span class="comment-user userinfo">DanielQc</span>
</div>
</div>
<span id="53406"></span>
<div id="comment-53406" class="comment">
<div id="post-53406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is the way of the river bank drawn already?</p>
</div>
<div id="comment-53406-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 00:01)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
</div>
<div id="comment-tools-53322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53322-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53468"></span>

<div id="answer-container-53468" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just downloaded the Mapzen extract and it worked. I’m happy :-)</p>
<p>You were right SomeoneElse, it’s probably the process of extracting the data that caused my problem. It's still curious... I was using quebec-latest.osm from <a href="http://download.geofabrik.de/north-america/canada/quebec.html">Geofabrik</a>.</p>
<p>Here, the osmosis command line that I was using for extracting a smaller part from the quebec-latest map:</p>
<p><strong><em>bzcat quebec-latest.osm.bz2 | osmosis --read-xml enableDateParsing=no file=- --bounding-box top=45.993 left=-74.312 bottom=45.228 right=-72.812 --write-xml file=- | bzip2 &gt; mtl.osm.bz2</em></strong></p>
<p>I think it might be the command line.. (or the coordinates ?)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '16, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/91e9d7555ec6a5d6f6c4abd2313646fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanielQc&#39;s gravatar image" />
<p><span>DanielQc</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanielQc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53468" class="comments-container">
<span id="53481"></span>
<div id="comment-53481" class="comment">
<div id="post-53481-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm guessing that you'd need to use both the "complete" options and also "cascading" option in osmosis as per:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.41">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.41</a></p>
</div>
<div id="comment-53481-info" class="comment-info">
<span class="comment-age">(11 Dec '16, 16:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53517"></span>
<div id="comment-53517" class="comment">
<div id="post-53517-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Tyvm.. you've found it! This command line did the trick!</p>
<p>bzcat quebec-latest.osm.bz2 | osmosis --read-xml enableDateParsing=no file=- --bounding-box top=45.993 left=-74.312 bottom=45.228 right=-72.812 <strong>completeRelations=yes cascadingRelations=yes</strong> --write-xml file=- | bzip2 &gt; mtl.osm.bz2</p>
</div>
<div id="comment-53517-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 03:52)</span> <span class="comment-user userinfo">DanielQc</span>
</div>
</div>
<span id="53531"></span>
<div id="comment-53531" class="comment">
<div id="post-53531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, the "trick" actually does not solve the problem. If your request scripts are properly constructed, something is still wrong in the sw involved.<br />
In the first case, you ask the sw for clipping out the objects using the bbox from your image 1. Clipping large and complex areas is complicated and full of error traps. The areas may radically change their structures and shapes and in some cases, the clipping may result in an incomplete polygon in an “outer-inner-outer-inner...” chain. Then, all the following polygons will change their rules and rendered inversed (as in your example).<br />
In the second case, your request asks the sw to extract all the objects having something common with the bbox. Therefore, no clipping is involved and you will get much, much larger area to render than you actually need and this may become highly inefficient/unpractical. The two requests/scripts are logically quite different.<br />
So, if you still insist on vector (pre- or on-the-fly-) tiling, you must use a version of the fist script but with a more robust clipping model. You should contact the intellectual owner of the involved sw and send an error warning with the example in your question.</p>
</div>
<div id="comment-53531-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 11:13)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="53532"></span>
<div id="comment-53532" class="comment">
<div id="post-53532-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/3194/sanser">@sanser</a> - I'm sure that pull requests at <a href="https://github.com/openstreetmap/osmosis">https://github.com/openstreetmap/osmosis</a> would be welcomed :) Personally I think that the options that they're offering are more than adequate.</p>
</div>
<div id="comment-53532-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 11:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53542"></span>
<div id="comment-53542" class="comment">
<div id="post-53542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It dit the trick for my needs..</p>
<p>I understand from your post that the first command line should have worked. In fact, It worked properly with JOSM. The problem was only with Tilemill (inverted colors). By adding those 2 additional arguments I got at least the expected result.</p>
</div>
<div id="comment-53542-info" class="comment-info">
<span class="comment-age">(14 Dec '16, 04:29)</span> <span class="comment-user userinfo">DanielQc</span>
</div>
</div>
</div>
<div id="comment-tools-53468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53468-form-container" class="comment-form-container">
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

