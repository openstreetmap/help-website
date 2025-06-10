+++
type = "question"
title = "Is it possible to specify a language for results in reverse geocoding?"
description = '''Hi all!  I was checking out this map creator page that uses OSM - http://developer.skobbler.de/mapcreator and I noticed there was an option to use transliteration. I was just wondering, is it possible to do this with reverse geocoding in Open Street Maps? It would just be super handy for me at the m...'''
date = "2014-10-31T23:10:00Z"
lastmod = "2014-11-01T21:43:00Z"
weight = 38202
keywords = [ "reversegeocoding", "transliteration", "language" ]
aliases = [ "/questions/38202" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to specify a language for results in reverse geocoding?](/questions/38202/is-it-possible-to-specify-a-language-for-results-in-reverse-geocoding)

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
<span id="post-38202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38202-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all!</p>
<p>I was checking out this map creator page that uses OSM - <a href="http://developer.skobbler.de/mapcreator">http://developer.skobbler.de/mapcreator</a> and I noticed there was an option to use transliteration. I was just wondering, is it possible to do this with reverse geocoding in Open Street Maps? It would just be super handy for me at the moment to specify the language results were coming back as.</p>
<p>Thanks Pete</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-transliteration" rel="tag" title="see questions tagged &#39;transliteration&#39;">transliteration</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '14, 23:10</strong></p>
<img src="https://secure.gravatar.com/avatar/fdee47c249b4ebfd61a032083b8a59a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peteskiii&#39;s gravatar image" />
<p><span>Peteskiii</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peteskiii has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38202" class="comments-container">
&#10;</div>
<div id="comment-tools-38202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38202-form-container" class="comment-form-container">
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

<span id="38226"></span>

<div id="answer-container-38226" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38226-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-38226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Peteskiii has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's even a URL parameter accept_language available in case you want to override your browser's default language. This might come in handy, if you call this stuff from your own web application.</p>
<p>Example:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;accept-language=de">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;accept-language=de</a></p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;accept-language=fr">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;accept-language=fr</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-38226" class="comments-container">
<span id="38238"></span>
<div id="comment-38238" class="comment">
<div id="post-38238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Awesome! Thanks, that's perfect!</p>
</div>
<div id="comment-38238-info" class="comment-info">
<span class="comment-age">(01 Nov '14, 21:43)</span> <span class="comment-user userinfo">Peteskiii</span>
</div>
</div>
</div>
<div id="comment-tools-38226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38226-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38206"></span>

<div id="answer-container-38206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38206-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Nominatim geocoder honours the Accept-Language HTTP header and will return results in the requested language - only if it has been mapped of course. This has nothing to do with transliteration though, but instead just influences which name:xx tag will be used.</p>
<p>To see the difference, compare the output of</p>
<pre><code>curl -H Accept-Language:de &#39;http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&#39;</code></pre>
<p>and</p>
<pre><code>curl -H Accept-Language:en &#39;http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&#39;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 00:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-38206" class="comments-container">
&#10;</div>
<div id="comment-tools-38206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38206-form-container" class="comment-form-container">
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

