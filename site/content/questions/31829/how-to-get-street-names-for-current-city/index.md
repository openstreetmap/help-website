+++
type = "question"
title = "How to get street names for current city?"
description = '''Hello, We want to do the following. Please tell us if it is possible and how is the easiest way to do this? We want to set a parameter - country and city and get all street names that are found in this city. Get them as a list. Could this happen? Can we use directly your database with API? We not ne...'''
date = "2014-03-24T11:47:00Z"
lastmod = "2014-03-27T10:34:00Z"
weight = 31829
keywords = [ "city", "streetnames" ]
aliases = [ "/questions/31829" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get street names for current city?](/questions/31829/how-to-get-street-names-for-current-city)

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
<span id="post-31829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31829-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>We want to do the following. Please tell us if it is possible and how is the easiest way to do this?</p>
<p>We want to set a parameter - country and city and get all street names that are found in this city. Get them as a list. Could this happen?</p>
<p>Can we use directly your database with API? We not need uploaded everything on our own server? Can we see somewhere a sample query, how to do it and get the data? Or step by step help info?</p>
<p>Thank you very much!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '14, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/b1f1fd6379c69bc7e75b9eb7f90afdf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Petar81&#39;s gravatar image" />
<p><span>Petar81</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Petar81 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31829" class="comments-container">
<span id="31938"></span>
<div id="comment-31938" class="comment">
<div id="post-31938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello,</p>
<p>I was trying to get all streets names from a service on <a href="http://www.gisgraphy.com">http://www.gisgraphy.com</a> when I saw that there is a Ban list in which my server can go in on multiple requests. My question is: what is the best way to get all streets from multiple Cities using PHP with given Name of City or Geo location?</p>
<p>Regards</p>
</div>
<div id="comment-31938-info" class="comment-info">
<span class="comment-age">(27 Mar '14, 10:34)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
</div>
<div id="comment-tools-31829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31829-form-container" class="comment-form-container">
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

<span id="31831"></span>

<div id="answer-container-31831" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31831-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-31831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap does not offer an interface for that. You will have to download the data for the city in question (or a whole country or even more), import it into a database, and extract the road names that lie within the boundary. The "Nominatim" geocoder could be a starting point for this, and there's even an export script for that here <a href="https://github.com/lonvia/Nominatim/blob/export-script/utils/export.php">https://github.com/lonvia/Nominatim/blob/export-script/utils/export.php</a> but I'm unsure if this still works.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '14, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31831" class="comments-container">
<span id="31879"></span>
<div id="comment-31879" class="comment">
<div id="post-31879-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
<p>Is not possible we contact with API to openstreetmap.org, right?</p>
</div>
<div id="comment-31879-info" class="comment-info">
<span class="comment-age">(25 Mar '14, 09:32)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
<span id="31883"></span>
<div id="comment-31883" class="comment">
<div id="post-31883-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Contacting the API is possible of course. But as already explained by Frederik it doesn't support such a query. And it should not be used for downloading huge amounts of data. See <a href="https://wiki.openstreetmap.org/wiki/Downloading_data">downloading data</a> in the wiki for alternative methods.</p>
</div>
<div id="comment-31883-info" class="comment-info">
<span class="comment-age">(25 Mar '14, 10:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="31887"></span>
<div id="comment-31887" class="comment">
<div id="post-31887-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's possible to use the API if it is for a limited area and if you do this only once. But as Frederik said, you will get OSM raw data where one street can be divided in multiple small segments/ways. You could also check the application <a href="http://maposmatic.org/">http://maposmatic.org/</a> creating street indexes (all details here <a href="http://maposmatic.org/about/)">http://maposmatic.org/about/)</a></p>
</div>
<div id="comment-31887-info" class="comment-info">
<span class="comment-age">(25 Mar '14, 13:31)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-31831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31831-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31894"></span>

<div id="answer-container-31894" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31894-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>please enter "street list" in the search field of this FAQ site.</p>
<p>There are already solutions for your aim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '14, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-31894" class="comments-container">
&#10;</div>
<div id="comment-tools-31894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31894-form-container" class="comment-form-container">
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

