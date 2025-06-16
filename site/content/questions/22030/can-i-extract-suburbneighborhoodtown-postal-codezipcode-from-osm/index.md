+++
type = "question"
title = "Can I extract suburb/neighborhood/town &amp; postal code/zipcode from OSM?"
description = '''For my current application I require the following data from a selection of countries: -Suburb/Neighborhood/Town/etc -Postal Code/Zip Code -State I&#x27;m weighing up whether to learn the OSM protocol &amp;amp; postgreSQL (as I currently use mySQL), and would like to know for sure that I can obtain this data...'''
date = "2013-05-02T02:24:00Z"
lastmod = "2013-05-02T14:37:00Z"
weight = 22030
keywords = [ "streetnames", "extract", "postgresql", "postcode", "zip-code" ]
aliases = [ "/questions/22030" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I extract suburb/neighborhood/town & postal code/zipcode from OSM?](/questions/22030/can-i-extract-suburbneighborhoodtown-postal-codezipcode-from-osm)

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
<span id="post-22030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For my current application <strong>I require the following data</strong> from a selection of countries:<br />
<strong>-Suburb/Neighborhood/Town/etc<br />
-Postal Code/Zip Code<br />
-State</strong><br />
I'm weighing up whether to learn the OSM protocol &amp; postgreSQL (as I currently use mySQL), and would like to know for sure that I can obtain this data (&amp; this is within the OSM licence as I don't want to abuse the service). Also if anyone knows some links to a step-by-step guide to:<br />
Download &amp; install postgreSQL (im using ubuntu)<br />
Commands I will require to extract neighborhood, zipcode, state to my database</p>
<p>Thank-you in advance</p>
<p>Here is an <strong>example</strong> of the data I require:<br />
Palo Alto, 94301, California (USA)<br />
London, SW3 4BN, England<br />
Richmond, 3121, Victoria (Australia)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-zip-code" rel="tag" title="see questions tagged &#39;zip-code&#39;">zip-code</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '13, 02:24</strong></p>
<img src="https://secure.gravatar.com/avatar/11762c3c4b5c6351ae149ce3c8f4e4c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephenvcroft&#39;s gravatar image" />
<p><span>stephenvcroft</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephenvcroft has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-22030" class="comments-container">
&#10;</div>
<div id="comment-tools-22030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22030-form-container" class="comment-form-container">
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

<span id="22032"></span>

<div id="answer-container-22032" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22032-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM postcode data is very incomplete across the world. If post codes are integral to your application you will likely have to buy them elsewhere. Other administrative data is also not guaranteed to be complete but is at least more likely to be there than postcode data. Do a few spot checks with the <a href="https://wiki.openstreetmap.org/wiki/Nominatim">online Nominatim service</a> to see if the data quality looks good enough for you in the regions you are interested in. If yes, download and install Nominatim, and then use suitable SQL queries against the Nominatim database to extract the areas you are interested in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '13, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-22032" class="comments-container">
&#10;</div>
<div id="comment-tools-22032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22032-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22039"></span>

<div id="answer-container-22039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22039-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Doing a text search on this FAQ site with key words like "extract boundaries" or "extract data" or Postalcode gives you already many topics here about your aims.</p>
<p>or even see topics tagges with "extract": <a href="https://help.openstreetmap.org/tags/extract/">https://help.openstreetmap.org/tags/extract/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '13, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-22039" class="comments-container">
&#10;</div>
<div id="comment-tools-22039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22039-form-container" class="comment-form-container">
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

