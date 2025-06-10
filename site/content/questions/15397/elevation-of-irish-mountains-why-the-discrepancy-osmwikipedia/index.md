+++
type = "question"
title = "Elevation of Irish mountains: Why the discrepancy OSM/Wikipedia"
description = '''I use Osmand 0.8.1 beta and the offline vector map of Ireland. Question: Why does osmand indicate a considerably greater elevation for mountains in Ireland than other sources? For instance Ireland&#x27;s &quot;Holy Mountain&quot; Croagh Patrick (53.7595°N 9.6584°W): 818.3 m according to osmand, 764 m according to ...'''
date = "2012-08-22T17:25:00Z"
lastmod = "2021-07-29T23:34:00Z"
weight = 15397
keywords = [ "mountains", "irish", "elevation" ]
aliases = [ "/questions/15397" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Elevation of Irish mountains: Why the discrepancy OSM/Wikipedia](/questions/15397/elevation-of-irish-mountains-why-the-discrepancy-osmwikipedia)

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
<span id="post-15397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15397-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-15397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use Osmand 0.8.1 beta and the offline vector map of Ireland. Question:</p>
<p>Why does osmand indicate a considerably greater elevation for mountains in Ireland than other sources?</p>
<p>For instance Ireland's "Holy Mountain" Croagh Patrick (53.7595°N 9.6584°W):</p>
<p>818.3 m according to osmand, 764 m according to Wikipedia (<a href="http://en.wikipedia.org/wiki/Croagh_Patrick).">http://en.wikipedia.org/wiki/Croagh_Patrick).</a></p>
<p>Or Ireland's highest peak Carrauntoohil (51°59′58″N 9°44′34″W):</p>
<p>1092.4 m according to osmand, 1038 m according to Wikipedia (<a href="http://en.wikipedia.org/wiki/Carrauntoohil).">http://en.wikipedia.org/wiki/Carrauntoohil).</a></p>
<p>In the osmand forum a received the followwing answer by sanderd17 to my question:</p>
<p>"Interesting question, but not the fault of OsmAnd.</p>
<p>The data comes from OSM, and was donated to OSM by mountainviews.ie (this links to your Croagh Patrick). Now, as you see on that site, the correct elevation is shown, from TM75 data. In OSM, the same elevation is shown in the tag ele:local. But for some reason, the ele tag has an offset of 54 meters (in both cases you mentioned), and is the same as ele:wsg84.</p>
<p>I don't know how the offset is introduced (I don't know a lot about those data collections either, or how to convert between them), but this is certainly not the fault of OsmAnd. Maybe you can ask it at help.openstreetmap.org (please do mention what I mentioned here)."</p>
<p><a href="https://groups.google.com/forum/?fromgroups=#!topic/osmand/pc2XvBae56w">Discussion in osmand forum</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mountains" rel="tag" title="see questions tagged &#39;mountains&#39;">mountains</span> <span class="post-tag tag-link-irish" rel="tag" title="see questions tagged &#39;irish&#39;">irish</span> <span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '12, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ccf2ba3ce249481a9de21aa159026405?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wandro&#39;s gravatar image" />
<p><span>wandro</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wandro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15397" class="comments-container">
&#10;</div>
<div id="comment-tools-15397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15397-form-container" class="comment-form-container">
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

<span id="15423"></span>

<div id="answer-container-15423" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15423-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-15423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wandro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is easy to explain the difference: both the ele and the ele:wgs84 tag give the elevation above the wgs84 ellipsoid. The ellipsoid is a simplified model of the shape of the earth. The wiki page on the ele tag misleadingly states this as "above sea level" which is only very roughly true.</p>
<p>The elevations given elsewhere are likely to be using the official local reference system, see <a href="http://wiki.openstreetmap.org/wiki/Key:ele">http://wiki.openstreetmap.org/wiki/Key:ele</a></p>
<p>Simon</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '12, 07:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '12, 10:05</strong> </span></p>
</div>
</div>
<div id="comments-container-15423" class="comments-container">
<span id="15425"></span>
<div id="comment-15425" class="comment">
<div id="post-15425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks for your quick response, but I wonder why for most other countries there isn't such a discrepancy. Why doesn't OSM use ele:local everywhere if this is the more common elevation measure?</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Key:ele">http://wiki.openstreetmap.org/wiki/Key:ele</a> seems to be an empty page ("There is currently no text in this page").</p>
</div>
<div id="comment-15425-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 07:55)</span> <span class="comment-user userinfo">wandro</span>
</div>
</div>
<span id="15427"></span>
<div id="comment-15427" class="comment">
<div id="post-15427-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There are a number of additonal points to make</p>
<ul>
<li>the differences between the local reference system and WGS84 depends naturally on the definition of the local system and will differ depending on where you are measuring</li>
<li>most GPS devices don't indicate directly which elevation they are reporting (most however have a setting that will force the device to return the WGS84 value), so we have a lot of erroneously entered non-WGS84 ele values</li>
<li>values copied from sign posts and other markers will in general not be the WGS84 value</li>
</ul>
<p>You have a '.' at the end of the wiki link that causes the problem.</p>
</div>
<div id="comment-15427-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 08:37)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="15468"></span>
<div id="comment-15468" class="comment">
<div id="post-15468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My actual questions were:</p>
<ol>
<li>Why doesn't there exist such a discrepancy OSM/Wikipedia for most other countries?</li>
<li>Why doesn't OSM use ele:local everywhere if this is the more common elevation measure used in many lookup resources?</li>
</ol>
</div>
<div id="comment-15468-info" class="comment-info">
<span class="comment-age">(24 Aug '12, 09:32)</span> <span class="comment-user userinfo">wandro</span>
</div>
</div>
<span id="15469"></span>
<div id="comment-15469" class="comment">
<div id="post-15469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The basic misunderstanding is that you are assuming that there is some kind of master plan behind this, when it is just a coincidence.</p>
<p>As you point out in your original question the altitude values in Ireland were imported, and obviously the importer used the wiki definitions and converted the values to the WGS84 ellipsoid values.</p>
<p>In other countries there have been no such imports and the ele values have been tagged by individual mappers by various means. It is just very likely that most of these values are either relative to WGS84 MSL (mean sea level) or relative to local vertical datums.</p>
</div>
<div id="comment-15469-info" class="comment-info">
<span class="comment-age">(24 Aug '12, 10:26)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="15470"></span>
<div id="comment-15470" class="comment">
<div id="post-15470-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Comment on point 2: I don't know the original reasoning, but it is likely to have been that the WGS84 ellipsoid value is easy to obtain and can easily be converted to other reference systems.</p>
<p>Naturally this was doomed from the start and I would suspect that if defined today, it would be done differently.</p>
</div>
<div id="comment-15470-info" class="comment-info">
<span class="comment-age">(24 Aug '12, 10:29)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="15473"></span>
<div id="comment-15473" class="comment not_top_scorer">
<div id="post-15473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another comment on "Why doesn't OSM use ele:local everywhere" - there may very well be places where multiple "ele:local"s could apply. For example, parts of the north of the island of Ireland could have OSGB grid references as well as the more normally used IR ones.</p>
</div>
<div id="comment-15473-info" class="comment-info">
<span class="comment-age">(24 Aug '12, 10:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15423" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-15423-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76935"></span>

<div id="answer-container-76935" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76935-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have fixed this one-by-one for many of the higher mountains (by updating the "ele" value to the correct "ele:local" value)</p>
<p>if anyone has rights to the underlying database it could probably be fixed via a sql query along the lines of</p>
<p>set "ele" to "ele:local" where node type = "peak" and country = "ireland" and "ele" between (ele:local+40, ele:local+60)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '20, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ec0467f68a7d411868e2d5b8f913e0a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roryrw&#39;s gravatar image" />
<p><span>roryrw</span><br />
<span class="score" title="26 reputation points">26</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roryrw has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76935" class="comments-container">
&#10;</div>
<div id="comment-tools-76935" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76935-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81111"></span>

<div id="answer-container-81111" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81111-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've just been looking peaks in the British Isles and identified this problem as well. I've created a <a href="https://charlie9578.github.io/gallery/BritishIsles_Munros.html">plot</a> using Python, that compares SRTM data and the <a href="http://www.hills-database.co.uk/downloads.html">Database of British and Irish Hills</a> with the OSM elevation data. It appears ~12 years ago the <a href="https://www.openstreetmap.org/user/xybot">xybot</a> used the wgs84 rather than local elevation for the "ele" tag, whereas local/EGM96 elevations are now prefered according to the latest <a href="https://wiki.openstreetmap.org/wiki/Key:ele">tagging recommendations</a>. I've also found a discussion on the <a href="https://forum.openstreetmap.org/viewtopic.php?id=23168">OSM Forum</a>, which is probably the best place to continue any discussion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '21, 23:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a11f88658d756f9b34bf0dc6c330d6fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charlie9578&#39;s gravatar image" />
<p><span>Charlie9578</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charlie9578 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81111" class="comments-container">
&#10;</div>
<div id="comment-tools-81111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81111-form-container" class="comment-form-container">
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

