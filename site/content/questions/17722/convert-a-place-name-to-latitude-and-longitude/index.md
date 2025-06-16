+++
type = "question"
title = "Convert a Place name to Latitude and Longitude"
description = '''How can I convert a place name to its Latitude and Longitude values in OpenStreetMap?'''
date = "2012-11-15T08:49:00Z"
lastmod = "2012-11-15T10:44:00Z"
weight = 17722
keywords = [ "openstreetmap" ]
aliases = [ "/questions/17722" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Convert a Place name to Latitude and Longitude](/questions/17722/convert-a-place-name-to-latitude-and-longitude)

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
<span id="post-17722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17722-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I convert a place name to its Latitude and Longitude values in OpenStreetMap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '12, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/33db830785c3cf0e661acb05b7f01d89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nightfury&#39;s gravatar image" />
<p><span>Nightfury</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nightfury has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '12, 10:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-17722" class="comments-container">
&#10;</div>
<div id="comment-tools-17722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17722-form-container" class="comment-form-container">
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

<span id="17727"></span>

<div id="answer-container-17727" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17727-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM uses <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> for geocoding. If you have a look at that wiki page you'll see some examples, and the output format can be varied, so that for example:</p>
<pre><code>http://nominatim.openstreetmap.org/search?format=xml&amp;q=london</code></pre>
<p>produces <a href="http://nominatim.openstreetmap.org/search?format=xml&amp;q=london">these results</a>.</p>
<p>If you plan to call it more than once you'll need to read the <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">usage policy</a> that goes with OSM's nominatim instance. Mapquest also run a <a href="http://open.mapquestapi.com/nominatim/">Nominatim instance</a>, with their own terms of use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '12, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-17727" class="comments-container">
&#10;</div>
<div id="comment-tools-17727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17727-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17723"></span>

<div id="answer-container-17723" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17723-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you are looking for is called <strong>geocoding</strong>. Enter the term in the search box above and see what you find.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '12, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17723" class="comments-container">
<span id="17725"></span>
<div id="comment-17725" class="comment">
<div id="post-17725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sir I did that and I got the answer <a href="http://py-googlemaps.sourceforge.net/">http://py-googlemaps.sourceforge.net/</a> but I don't want to use googlemaps thats y i came here. please help</p>
</div>
<div id="comment-17725-info" class="comment-info">
<span class="comment-age">(15 Nov '12, 09:14)</span> <span class="comment-user userinfo">Nightfury</span>
</div>
</div>
<span id="17726"></span>
<div id="comment-17726" class="comment">
<div id="post-17726-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Frederik was talking about the search box <em>on this site</em>.</p>
</div>
<div id="comment-17726-info" class="comment-info">
<span class="comment-age">(15 Nov '12, 09:41)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-17723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17723-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17724"></span>

<div id="answer-container-17724" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17724-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Type place into search box, select correct one then right click permalink, then right click copy link address this can the be pasted into a doc so it can be emailed, or if you just want to read it paste it into the search box and scroll along it. The Potlatch2 editor will display lat long of the mouse pointer if you wish, it is in options drop down.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '12, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '12, 09:19</strong> </span></p>
</div>
</div>
<div id="comments-container-17724" class="comments-container">
&#10;</div>
<div id="comment-tools-17724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17724-form-container" class="comment-form-container">
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

