+++
type = "question"
title = "How does Nominatim reverse geocode?"
description = '''How does Nominatim reverse-geocode? I&#x27;m interested in knowing how the process works, and even trying to optimize it, if possible. I&#x27;ve Googled for an answer but could not find it. How does Nominatim resolve a GPS coordinate into a place?  Thanks in advance'''
date = "2014-02-06T23:05:00Z"
lastmod = "2014-02-07T19:07:00Z"
weight = 30512
keywords = [ "reversegeocoding", "nominatim" ]
aliases = [ "/questions/30512" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How does Nominatim reverse geocode?](/questions/30512/how-does-nominatim-reverse-geocode)

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
<span id="post-30512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30512-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How does Nominatim reverse-geocode? I'm interested in knowing how the process works, and even trying to optimize it, if possible. I've Googled for an answer but could not find it. How does Nominatim resolve a GPS coordinate into a place?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '14, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Feb '14, 00:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30512" class="comments-container">
<span id="30546"></span>
<div id="comment-30546" class="comment">
<div id="post-30546-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please avoid crosspostings as they consume a lot of the ressources that try to help you: <a href="https://stackoverflow.com/questions/21616476/how-does-reverse-geocoding-work">https://stackoverflow.com/questions/21616476/how-does-reverse-geocoding-work</a></p>
</div>
<div id="comment-30546-info" class="comment-info">
<span class="comment-age">(07 Feb '14, 19:07)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-30512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30512-form-container" class="comment-form-container">
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

<span id="30523"></span>

<div id="answer-container-30523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30523-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-30523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "grunt work" of reverse geocoding in Nominatim is done by the PostGIS database. Nominatim uses a helper program, osm2pgsql, to import OSM data into a PostGIS database, and then queries PostGIS to return the nearest feature to a given coordinate. That's the core of it. (See <a href="https://github.com/twain47/Nominatim/blob/edc5733715a65158919c1abc4d765b754f5dc659/lib/ReverseGeocode.php#L93-L101">the SQL query that does this.)</a></p>
<p>After identifying the nearest feature, Nominatim will go through a few extra database queries to actually give you the full place hierarchy (country, state, city etc.) for it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '14, 07:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Feb '14, 09:17</strong> </span></p>
</div>
</div>
<div id="comments-container-30523" class="comments-container">
&#10;</div>
<div id="comment-tools-30523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30513"></span>

<div id="answer-container-30513" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30513-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, it does reverse-geocode. See section one in <span>Nominatim wiki page</span>.</p>
<p>To see how it works you could see the source code. Also the development overview might be useful for understanding (linked in the intro section).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '14, 00:17</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-30513" class="comments-container">
<span id="30515"></span>
<div id="comment-30515" class="comment">
<div id="post-30515-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the answer. I am fully aware that Nominatim has a reverse geocoding capability. My question was how it does it, not whether or not it does it. I could look at the source code, but I'm not too fluent in the language Nominatim is written.</p>
</div>
<div id="comment-30515-info" class="comment-info">
<span class="comment-age">(07 Feb '14, 02:09)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="30538"></span>
<div id="comment-30538" class="comment">
<div id="post-30538-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@baekacaek</span>: Indeed ... For whatever reason I missed the "How" while reading, sorry.</p>
</div>
<div id="comment-30538-info" class="comment-info">
<span class="comment-age">(07 Feb '14, 14:28)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30513-form-container" class="comment-form-container">
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

