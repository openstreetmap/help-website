+++
type = "question"
title = "GADM for Iran"
description = '''I noticed today that at least Kerman province, and possibly others in Iran, do not have sub-provinces included in Nominatim. I was looking at this blurb, which states:  Borders in Turkey, Bahrain, Iran, Iraq, Ivory Coast, Jordan, Saudi Arabia, Sudan, and Syria are derived from GADM data. We have bee...'''
date = "2014-06-08T12:02:00Z"
lastmod = "2014-06-08T12:19:00Z"
weight = 33800
keywords = [ "gadm", "admin_boundary", "iran" ]
aliases = [ "/questions/33800" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GADM for Iran](/questions/33800/gadm-for-iran)

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
<span id="post-33800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33800-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed today that at least Kerman province, and possibly others in Iran, do not have sub-provinces included in Nominatim. I was looking at <a href="https://wiki.openstreetmap.org/wiki/Contributors#GADM_.28Global_Administrative_Areas.29">this blurb</a>, which states:</p>
<blockquote>
<p>Borders in Turkey, Bahrain, Iran, Iraq, Ivory Coast, Jordan, Saudi Arabia, Sudan, and Syria are derived from GADM data. We have been given explicit permission to distribute the datasets for these countries under OSM licensing condistions, including commercial use.</p>
</blockquote>
<p>Does that mean that the boundaries can be imported from GADM for Iran? GADM does correctly have the sub-provinces, so far as I can tell, and it would be nice to import them to Open Street Map, but I want to make sure it's okay before doing anything about it. Thanks!</p>
<p>FYI, my test point in Kerman sub province, Kerman, Iran. See nominatim results, at <a href="http://open.mapquestapi.com/nominatim/v1/reverse.php?format=json&amp;json_callback=renderExampleThreeResults&amp;lat=30.311667&amp;lon=57.04">http://open.mapquestapi.com/nominatim/v1/reverse.php?format=json&amp;json_callback=renderExampleThreeResults&amp;lat=30.311667&amp;lon=57.04</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gadm" rel="tag" title="see questions tagged &#39;gadm&#39;">gadm</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-iran" rel="tag" title="see questions tagged &#39;iran&#39;">iran</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '14, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ada90dc82e9546879ac95847117d1a3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kd7uiy&#39;s gravatar image" />
<p><span>kd7uiy</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kd7uiy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '14, 12:27</strong> </span></p>
</div>
</div>
<div id="comments-container-33800" class="comments-container">
&#10;</div>
<div id="comment-tools-33800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33800-form-container" class="comment-form-container">
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

<span id="33801"></span>

<div id="answer-container-33801" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33801-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem is that the source of the data that GADM uses may have changed and with it the licence, if it hasn't, yes than you can use GADM. So you would need to have a look at when the boundaries for Iran were imported and check with historic and current GADM data. Naturally in principle the simplest way to determine that would be to ask GADM directly, but in our experience it has taken a very long time to get answers if at all.</p>
<p>Not directed at you, but given the amount of trouble it has caused, I do have to make this comment:</p>
<p>GADM DATA IS PROVIDED UNDER A NON-COMMERCIAL USE LICENCE AND THEREFORE IS NOT SUITABLE FOR IMPORTING IN TO OSM EXCEPT IF EXPLICIT PERMISSION HAS BEEN OBTAINED.<br />
</p>
<p>Further note: determing if a data source is licenced in a way that would allow it to be imported or used for OSM purposes is just one of the required steps prior to an import, see <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">https://wiki.openstreetmap.org/wiki/Import/Guidelines</a> for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '14, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '14, 13:12</strong> </span></p>
</div>
</div>
<div id="comments-container-33801" class="comments-container">
&#10;</div>
<div id="comment-tools-33801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33801-form-container" class="comment-form-container">
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

