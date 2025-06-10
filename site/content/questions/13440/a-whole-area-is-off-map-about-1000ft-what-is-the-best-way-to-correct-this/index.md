+++
type = "question"
title = "a whole area is off map (about 1000ft) - what is the best way to correct this?"
description = '''I have found that a whole area north of Millington TN (USA) is off map about 1000ft.  Way: 19638736 is for Hwy US 51 as an example, but the area around is shifted too. . In addition i have found that US 51 in its whole length in the OSM map is altering several time between 2 lane and 4 lane, one lin...'''
date = "2012-06-12T00:57:00Z"
lastmod = "2012-06-19T16:51:00Z"
weight = 13440
keywords = [ "millington" ]
aliases = [ "/questions/13440" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [a whole area is off map (about 1000ft) - what is the best way to correct this?](/questions/13440/a-whole-area-is-off-map-about-1000ft-what-is-the-best-way-to-correct-this)

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
<span id="post-13440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13440-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have found that a whole area north of Millington TN (USA) is off map about 1000ft. Way: 19638736 is for Hwy US 51 as an example, but the area around is shifted too. . In addition i have found that US 51 in its whole length in the OSM map is altering several time between 2 lane and 4 lane, one line and 2 lines, where there is in fact only 4 lane in 2 separate directions. . Sure, i can try to edit it, but it seems to be way too much data to correct and my question is: how can a whole area get corrected? . On most of the OSM details i have found that the source is TIGER. When looking up this map-area in TIGERweb (U.S. Census Bureau), it seem to be correct. I am wondering if there was a problem with the import in general and if this can be redone with the newest data to make sure that the map for this state is correct.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-millington" rel="tag" title="see questions tagged &#39;millington&#39;">millington</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '12, 00:57</strong></p>
<img src="https://secure.gravatar.com/avatar/48722e67517690a7aa78df0c2228c203?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wunderlicht&#39;s gravatar image" />
<p><span>wunderlicht</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wunderlicht has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13440" class="comments-container">
&#10;</div>
<div id="comment-tools-13440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13440-form-container" class="comment-form-container">
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

<span id="13457"></span>

<div id="answer-container-13457" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13457-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I took a look at the area and based on Bing, NAIP aerial and GPS tracks, I agree that much of the area is way off. It will all need to be updated to 4 lanes; I'm guessing that the 4 lane road has been completed since the original TIGER survey (likely in the last 10-20 years). And the whole of Tipton County is not shifted; the road comes into proper alignment further northeast. I'm guessing that they used some misaligned aerial imagery in the past to produce the original import data.</p>
<p>The updated TIGER in Tipton County is much better, but it will be difficult to use a "delete and replace" strategy everywhere because there has been much work in assigning attributes and relations to the US Highways and Interstates in the area. So the only way to fix it will be manual realignment of anything that has been edited. The smaller roads in the area could be deleted and replaced with TIGER 2011 data.</p>
<p>An alternative to delete and replace is to use JOSM with the <a href="http://josm.openstreetmap.de/wiki/Help/Plugin/UtilsPlugin2">Utils2 Plugin</a> and the "Replace Geometry" command, then making sure the intersections are reconnected. I can make a processed TIGER 2011 extract of Tipton County available for use with JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '12, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-13457" class="comments-container">
<span id="13481"></span>
<div id="comment-13481" class="comment">
<div id="post-13481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this sounds like a nice challenge. i have to say that i just have started to look into OSM data and just started looking into Potlatch2, but haven't edited anything yet. Maybe someone with more experience can take this in the hand? I sure would love to help, since i am living nearby of this area, i would be able to verify mapping-points or take gps-traces where needed.</p>
<p>But in case there is nobody available to edit this area, it would take a bit of time for me to learn more about JOSM and how to edit OSM-data correctly, then i would love to get it going...</p>
</div>
<div id="comment-13481-info" class="comment-info">
<span class="comment-age">(13 Jun '12, 00:06)</span> <span class="comment-user userinfo">wunderlicht</span>
</div>
</div>
<span id="13486"></span>
<div id="comment-13486" class="comment">
<div id="post-13486-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'll do the major highway, since I have done quite a few of these and have the workflow optimized for JOSM.</p>
</div>
<div id="comment-13486-info" class="comment-info">
<span class="comment-age">(13 Jun '12, 02:07)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
<span id="13499"></span>
<div id="comment-13499" class="comment">
<div id="post-13499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>excellent, US51 has been corrected, how do i get access to the new TIGER data to work on the residential roads?</p>
</div>
<div id="comment-13499-info" class="comment-info">
<span class="comment-age">(13 Jun '12, 16:08)</span> <span class="comment-user userinfo">wunderlicht</span>
</div>
</div>
<span id="13516"></span>
<div id="comment-13516" class="comment">
<div id="post-13516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have posted it on <a href="http://greenvilleopenmap.inf/Tipton_TN_TIGER_2011.zip">http://greenvilleopenmap.inf/Tipton_TN_TIGER_2011.zip</a> , and it will be there for several weeks.</p>
</div>
<div id="comment-13516-info" class="comment-info">
<span class="comment-age">(14 Jun '12, 00:29)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
<span id="13541"></span>
<div id="comment-13541" class="comment">
<div id="post-13541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much - i have analysed the TIGER-data and have found even in those are some little areas off the real position. It will need a lot of detail work and i will get it going soon</p>
</div>
<div id="comment-13541-info" class="comment-info">
<span class="comment-age">(14 Jun '12, 16:37)</span> <span class="comment-user userinfo">wunderlicht</span>
</div>
</div>
</div>
<div id="comment-tools-13457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13457-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13575"></span>

<div id="answer-container-13575" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13575-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>quick update what is happening:</p>
<p>MikeN has corrected US 51 and with his help with the TIGER 2011 import I am able to work on the residential roads in this area. So far i have completed about 1/4 and i will post an update when i have completed the job.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '12, 13:10</strong></p>
<img src="https://secure.gravatar.com/avatar/48722e67517690a7aa78df0c2228c203?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wunderlicht&#39;s gravatar image" />
<p><span>wunderlicht</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wunderlicht has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13575" class="comments-container">
&#10;</div>
<div id="comment-tools-13575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13575-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13624"></span>

<div id="answer-container-13624" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13624-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>done...</p>
<p>Boy, that was quite some work, but thanks to Mike, who brought me on the right track, it was fairly simple to do. I like to share the steps i have taken so that other newbie's like me will have it easier.</p>
<p>In order to make changes you need to have good reference data. One good source is TIGER 2011 (<a href="http://www.census.gov/geo/www/tiger/tgrshp2011/tgrshp2011.html).">http://www.census.gov/geo/www/tiger/tgrshp2011/tgrshp2011.html).</a> An other very good source are GPS-traces you have taken yourself in the area you like to edit the map. So get familiar with GPS tracing devices, i have used my Android-smartphone so that i can make geocoded notes and pictures too. One very good app is OSMTracker for Android. As imagery i have use Bing Sat, because it is in my area most accurate and nearly to 100% aligned to the GPS data. So, all three together will give you enough data as reference to start editing the map in your area.</p>
<p>I have used Potlatch2 and JOSM for editing the map, i like both, P2 because it is quick and easy to start with, JOSM because it lets you work on the map very detailed. In JOSM you can load your GPS-traces, Bing Sat, OSM-map-area, Tiger2011 shape-file, each as an individual layer. You just do the editing in the data-layer with the OSM-map, and use the other layers as reference.</p>
<p>Sat-imagery-alignment: It is highly recommended to check the alignment of the Sat-image. The best way to do this is to take GPS-traces in the area and align the Sat-image to those.</p>
<p>TIGER 2011 import: First i found it difficult to handle the TIGER2011 shape-files, but with the help of Mike who has converted the shape-files into OSM-files by using some python-scripts, it was easy enough. Unfortunately those scripts were not working on my system so that i was not able to convert other areas myself. The main thing with the import is that the road-tags need to get changed into what OSM can understand. That the script shall do. But, after some little research, i have found that there is a JOSM-plugin called 'opendata' which can do the import. the difference is that this plugin is NOT changing the tags, so you have to edit the tags manually if you copy-paste road/suburbs from the import-layer into the data-layer. Be careful when using the TIGER2011 data, it is needing a lot of detail re-work like road-tags, road-names, and road connection to way's. But if you want to use the TIGER2011 data JUST as a reference and do the edit only in the data-layer, this method is super easy.</p>
<p>Thats it, wish yall happy mapping ... wunderlicht</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '12, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/48722e67517690a7aa78df0c2228c203?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wunderlicht&#39;s gravatar image" />
<p><span>wunderlicht</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wunderlicht has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '12, 16:54</strong> </span></p>
</div>
</div>
<div id="comments-container-13624" class="comments-container">
&#10;</div>
<div id="comment-tools-13624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13624-form-container" class="comment-form-container">
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

