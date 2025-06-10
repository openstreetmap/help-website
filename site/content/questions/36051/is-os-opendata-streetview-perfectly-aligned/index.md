+++
type = "question"
title = "Is OS OpenData StreetView perfectly aligned?"
description = '''I&#x27;ve just started with OSM, and one of my first edits was to (slightly) realign my road to the OS OpenData StreetView background, under the assumption that this would make it correctly aligned. Is this assumption right? From a practical perspective, am I better to align to bing, since this default b...'''
date = "2014-08-21T13:53:00Z"
lastmod = "2014-08-27T22:55:00Z"
weight = 36051
keywords = [ "bing", "streetview", "alignment" ]
aliases = [ "/questions/36051" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is OS OpenData StreetView perfectly aligned?](/questions/36051/is-os-opendata-streetview-perfectly-aligned)

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
<span id="post-36051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36051-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-36051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've just started with OSM, and one of my first edits was to (slightly) realign my road to the OS OpenData StreetView background, under the assumption that this would make it correctly aligned. Is this assumption right? From a practical perspective, am I better to align to bing, since this default background is the one that many will use as a guide to map generation? Please note that the differences here are only a couple of metres, and the GPS traces are insufficient to discriminate between the two.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bing" rel="tag" title="see questions tagged &#39;bing&#39;">bing</span> <span class="post-tag tag-link-streetview" rel="tag" title="see questions tagged &#39;streetview&#39;">streetview</span> <span class="post-tag tag-link-alignment" rel="tag" title="see questions tagged &#39;alignment&#39;">alignment</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '14, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a56aacf4d1e927dcd675dfc85cb7e992?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="u003f&#39;s gravatar image" />
<p><span>u003f</span><br />
<span class="score" title="351 reputation points">351</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="u003f has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36051" class="comments-container">
&#10;</div>
<div id="comment-tools-36051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36051-form-container" class="comment-form-container">
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

<span id="36056"></span>

<div id="answer-container-36056" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36056-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-36056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="u003f has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ordnance Survey probably have the most accurate available mapping of the United Kingdom, so I would expect their open data to be very accurate. I have checked a few locations where I am confident that OSM is accurate (it agrees with the average of many GPS traces), and in those areas, the agreement between OSM and OS Open Data is impressive.</p>
<p>I have found in the past that Bing imagery can be offset by a few metres, as a result of the difficulty of converting aerial images to georeferenced maps. As far as I know, it is impossible to do so unless really accurate height information is available. See this question (<a href="https://help.openstreetmap.org/questions/17661/aligning-roads-to-proper-location)">https://help.openstreetmap.org/questions/17661/aligning-roads-to-proper-location)</a> for some more thoughts on that point.</p>
<p>Please keep in mind that one GPS trace may be inaccurate, but if you have the opportunity to collect several traces of the same road or path, any 'rogue' tracks will be easily visible, and in most cases the average of the others will be amply good enough to use for mapping. You can improve the accuracy of the average by taking several tracks at different times of day (which gives different satellite configurations), and by taking tracks in both directions along roads (which should eliminate the overshoot / undershoot errors that many GPS receivers generate, and also eliminates the effect of driving on one side of the road).</p>
<p>In some areas I have mapped the main roads as accurately as I can using multiple GPS traces, then aligned the Bing imagery with the main roads, and then adjusted the side roads to agree with Bing. When I have subsequently been able to check the mapping, it has proved to be accurate.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '14, 18:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-36056" class="comments-container">
<span id="36069"></span>
<div id="comment-36069" class="comment">
<div id="post-36069-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A couple of important points:</p>
<ol>
<li><p>the accuracy of OSGB data is dependent on how it is transformed to the co-ordinate system used by OSM. If EPSG:27700 is used as the datum then accuracy varies from 0-6 metres. If a more specific transform is used as specified by the OS then this should be more accurate. I imagine JOSM used 27700 for OSGB shape files.</p></li>
<li><p>the OP was about StreetView (OSSV) which is a generalised view of the Vector Map District data. In my experience road features are too generalised with this product for accurate alignment (VMD is OK). They do use the more accurate transform.</p></li>
</ol>
</div>
<div id="comment-36069-info" class="comment-info">
<span class="comment-age">(22 Aug '14, 10:03)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36293"></span>
<div id="comment-36293" class="comment">
<div id="post-36293-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I simply selected OS OpenData StreetView as the background in Potlatch 2, and was impressed when the roads in OSM ran down the middle of the roads shown in the background image. I confess that I did not consider the accuracy of the datum transformation. I was looking at an area in central southern England, where a Helmert transformation between OSGB36 and WGS84 does seem to give accurate results.</p>
<p>Can anyone say how OS provides the georeferencing information for StreetView images, and how Potlatch transforms it to create a background image on the OSM datum and projection?</p>
</div>
<div id="comment-36293-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 22:36)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="36294"></span>
<div id="comment-36294" class="comment">
<div id="post-36294-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The original images are GeoTIFFs with 1 pixel / metre. This will be tiled using osgeo tools and altered to Spherical Mercator using the full OS transform. Major roads &amp; such will be fine, but short cul-de-sacs tend to have a lot of wiggles taken out. It's very noticeable that roads initially traced from OSSV may need a fair bit of refinement now that aerial imagery is more widely available.</p>
</div>
<div id="comment-36294-info" class="comment-info">
<span class="comment-age">(27 Aug '14, 22:55)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36056-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36070"></span>

<div id="answer-container-36070" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A good GPS trace is the preferred data to align OpenStreetMap to. You can easily know the accuracy you had and if any processing has taken place to convert it (i.e. with OSSV and aerial rasters a lot goes on to create the raster tile images).</p>
<p>If I am not confident in my GPS accuracy then I try to leave existing features where they are. If I have good confidence in my GPS trace but not 100% (especially if the existing OSM data looks detailed but is substantially different) then I have a habit of moving the features halfway between where I think they should be and where they are already.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '14, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/f846f21cfbcf60a35e1f69c2cc74df77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LivingWithDragons&#39;s gravatar image" />
<p><span>LivingWithDr...</span><br />
<span class="score" title="524 reputation points">524</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LivingWithDragons has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-36070" class="comments-container">
&#10;</div>
<div id="comment-tools-36070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36070-form-container" class="comment-form-container">
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

