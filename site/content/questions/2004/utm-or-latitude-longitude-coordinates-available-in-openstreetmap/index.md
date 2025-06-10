+++
type = "question"
title = "UTM or Latitude-Longitude coordinates available in OpenStreetMap?"
description = '''I would like to use OpenStreetMap to help wade through the tons of orthophotos available on line from State of California, so as to save time over the tedious method of downloading the files, loading them into the GIS, and trying to identify a landmark! Is there a way to see the coordinates (prefera...'''
date = "2011-01-04T06:56:00Z"
lastmod = "2023-01-09T11:20:00Z"
weight = 2004
keywords = [ "latitude", "longitude", "coordinates", "utm" ]
aliases = [ "/questions/2004" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [UTM or Latitude-Longitude coordinates available in OpenStreetMap?](/questions/2004/utm-or-latitude-longitude-coordinates-available-in-openstreetmap)

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
<span id="post-2004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2004-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to use OpenStreetMap to help wade through the tons of orthophotos available on line from State of California, so as to save time over the tedious method of downloading the files, loading them into the GIS, and trying to identify a landmark! Is there a way to see the coordinates (preferably UTM, but latitude/longitude would work) of the map display, or of the mouse cursor? Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-utm" rel="tag" title="see questions tagged &#39;utm&#39;">utm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '11, 06:56</strong></p>
<img src="https://secure.gravatar.com/avatar/505a990822a036da6df5e1d314455e6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Catlike&#39;s gravatar image" />
<p><span>Catlike</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Catlike has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2004" class="comments-container">
&#10;</div>
<div id="comment-tools-2004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2004-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="2010"></span>

<div id="answer-container-2010" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2010-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-2010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many many way to do this. The first three that come to mind:</p>
<ul>
<li>Use the <a href="http://www.openstreetmap.org/"></a><a href="http://www.openstreetmap.org"></a><a href="http://www.openstreetmap.org">www.openstreetmap.org</a> website and hover the mouse pointer over the "permalink" link. The status bar in your browser should display the URL of the current map view which includes latitude and longitude of the map center. Or click the "export" tab which allows you to draw a rectangle on the map and see its edge coordinates.</li>
<li>Use the <a href="http://www.informationfreeway.org/"></a><a href="http://www.informationfreeway.org"></a><a href="http://www.informationfreeway.org">www.informationfreeway.org</a> website which offers a fullscreen map view and a coordinate display for the position of the mouse pointer in the lower right corner.</li>
<li>Use the <a href="http://gll.petschge.de/">gll.petschge.de</a> website which offers a crosshair at the center of the map view and a coordinate display at the top of the page. If you sufficiently bribe me I might even add a coordinate display in UTM.</li>
</ul>
<p>Another possibility would be to create a small page with <a href="http://openlayers.org/">openlayers</a> using Openstreetmap tiles and and a <a href="http://dev.openlayers.org/docs/files/OpenLayers/Control/MousePosition-js.html">MousePosition Control</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '11, 07:45</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jan '11, 10:31</strong> </span></p>
</div>
</div>
<div id="comments-container-2010" class="comments-container">
&#10;</div>
<div id="comment-tools-2010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2010-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86462"></span>

<div id="answer-container-86462" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86462-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the editor, press CTRL+SHIFT+L to display the Location Panel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '23, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/63bf3553cfc4f167abe24eaad9deaad1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joper34&#39;s gravatar image" />
<p><span>joper34</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joper34 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '23, 11:23</strong> </span></p>
</div>
</div>
<div id="comments-container-86462" class="comments-container">
&#10;</div>
<div id="comment-tools-86462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86462-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2009"></span>

<div id="answer-container-2009" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2009-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-2009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are using the editor potlatch 1 you can get the location coordinates of the mouse by pressing the <strong>l</strong>-key. Don't know if such a key exists in potlatch 2 though - the help does not state any...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '11, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katpatuka has 2 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-2009" class="comments-container">
<span id="2013"></span>
<div id="comment-2013" class="comment">
<div id="post-2013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, there's currently no equivalent key in Potlatch 2.</p>
</div>
<div id="comment-2013-info" class="comment-info">
<span class="comment-age">(04 Jan '11, 12:45)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-2009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2009-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27115"></span>

<div id="answer-container-27115" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27115-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-27115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try to use (software name removed) from (link removed). You can browse Google Maps, Bing Maps and OpenStreet Maps and see mouse position coordinate both Lat/Lon and UTM in the Datum of your choice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Oct '13, 19:02</strong></p>
<img src="https://secure.gravatar.com/avatar/d3e5b3415d5beb0d6eeda4a77b88f05a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark_879&#39;s gravatar image" />
<p><span>Mark_879</span><br />
<span class="score" title="-5 reputation points">-5</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark_879 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '13, 18:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-27115" class="comments-container">
&#10;</div>
<div id="comment-tools-27115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27115-form-container" class="comment-form-container">
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

