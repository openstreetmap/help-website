+++
type = "question"
title = "Adress handover via URI?"
description = '''Hello, is it possible to commit an adress to OSM via an URI? I&#x27;ve got an Access database, which contains the fields postcode, city, street and company name. I would like to commit these fields to OSM for visualizing the adress on the map. In Google Maps, I can add the adress fields in the URI, e.g.:...'''
date = "2013-06-13T08:41:00Z"
lastmod = "2013-06-13T09:37:00Z"
weight = 23304
keywords = [ "url", "access", "search", "address" ]
aliases = [ "/questions/23304" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Adress handover via URI?](/questions/23304/adress-handover-via-uri)

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
<span id="post-23304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23304-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>is it possible to commit an adress to OSM via an URI?</p>
<p>I've got an Access database, which contains the fields postcode, city, street and company name.</p>
<p>I would like to commit these fields to OSM for visualizing the adress on the map.</p>
<p>In Google Maps, I can add the adress fields in the URI, e.g.:</p>
<p><em><a href="http://maps.google.de/maps?f=q&amp;source=s_q&amp;hl=de&amp;geocode=&amp;q=">http://maps.google.de/maps?f=q&amp;source=s_q&amp;hl=de&amp;geocode=&amp;q=</a><strong>Street</strong>,+<strong>City</strong></em></p>
<p>Kind regards, Daniel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '13, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/bb2fc3c6f40eed5fdcede8194a60cd79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniel%20Schunk&#39;s gravatar image" />
<p><span>Daniel Schunk</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniel Schunk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23304" class="comments-container">
&#10;</div>
<div id="comment-tools-23304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23304-form-container" class="comment-form-container">
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

<span id="23309"></span>

<div id="answer-container-23309" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23309-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Daniel Schunk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM uses nominatim for geocoding - use for example <a href="http://nominatim.openstreetmap.org/search.php?q=Haarenfeld%2010%2C+Oldenburg&amp;viewbox=8.17%2C53.16%2C8.18%2C53.15&amp;polygon=1">http://nominatim.openstreetmap.org/search.php?q=Haarenfeld%2010%2C+Oldenburg&amp;viewbox=8.17%2C53.16%2C8.18%2C53.15&amp;polygon=1</a> , where you pass the same q parameter as for google maps. You'll need to experiment with the viewbox and polygon parameters.</p>
<p>See and comply with the <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '13, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '13, 09:39</strong> </span></p>
</div>
</div>
<div id="comments-container-23309" class="comments-container">
&#10;</div>
<div id="comment-tools-23309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23309-form-container" class="comment-form-container">
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

