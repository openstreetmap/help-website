+++
type = "question"
title = "Latitude and longitude via VBA into excel"
description = '''Hello there, i&#x27;m working on an excel based VBA tool. The tool is offering a function to show a map of germany with different locations of companies. To locate the companies I want to get the latitude and longitude of each company with an extract of a .xml response. I got it running with the google a...'''
date = "2013-05-23T12:01:00Z"
lastmod = "2013-05-23T12:06:00Z"
weight = 22679
keywords = [ "search", "nominatim", "geocoding" ]
aliases = [ "/questions/22679" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Latitude and longitude via VBA into excel](/questions/22679/latitude-and-longitude-via-vba-into-excel)

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
<span id="post-22679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22679-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello there,</p>
<p>i'm working on an excel based VBA tool. The tool is offering a function to show a map of germany with different locations of companies.</p>
<p>To locate the companies I want to get the latitude and longitude of each company with an extract of a .xml response.</p>
<p>I got it running with the google api, but want to change it wo openstreetmap. Is there something like this in openstreetmap?</p>
<p>For example:</p>
<p><a href="http://maps.google.com/maps/api/geocode/xml?sensor=false&amp;address=Marienplatz+1+Muenchen&amp;language=de">http://maps.google.com/maps/api/geocode/xml?sensor=false&amp;address=Marienplatz+1+Muenchen&amp;language=de</a></p>
<p>this url is giving me a xml file where I can extract the latitude and longitude from.</p>
<p>Thanks for your help!</p>
<p>Jan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '13, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/bd0b3ee30996f34b11ca02d55ed8568b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jan&#39;s gravatar image" />
<p><span>Jan</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 May '13, 12:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span></p>
</div>
</div>
<div id="comments-container-22679" class="comments-container">
&#10;</div>
<div id="comment-tools-22679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22679-form-container" class="comment-form-container">
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

<span id="22681"></span>

<div id="answer-container-22681" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22681-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We have nominantim for that.</p>
<p>Example: <a href="http://nominatim.openstreetmap.org/search?q=135+pilkington+avenue,+birmingham&amp;format=xml&amp;polygon=1&amp;addressdetails=1"><code>http://nominatim.openstreetmap.org/search?q=135+pilkington+avenue,+birmingham&amp;format=xml&amp;polygon=1&amp;addressdetails=1</code></a></p>
<p>See the wiki at <a href="http://wiki.openstreetmap.org/wiki/Nominatim">http://wiki.openstreetmap.org/wiki/Nominatim</a> for more information.</p>
<p>Note that you must not use this for "batch geocoding" i.e. it is ok to find the location for a single business but you are not allowed to run through a long list of addresses and geocode them all at once (see the usage policy linked at the bottom of the Nominatim page).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '13, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 May '13, 13:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-22681" class="comments-container">
&#10;</div>
<div id="comment-tools-22681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22681-form-container" class="comment-form-container">
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

