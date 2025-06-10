+++
type = "question"
title = "Ruby tile generator"
description = '''Sorry for absolute dumb question... I need to generate the OSM map tiles on the fly on Ruby (Actually on Rhomobile app, which is Ruby based) , so could you hint out which library, extention can do it?  On mobile device I have only Sqlite, and I think I should use something like mapName.map as a row,...'''
date = "2011-11-26T15:50:00Z"
lastmod = "2012-08-29T17:27:00Z"
weight = 9234
keywords = [ "tiles", "ruby" ]
aliases = [ "/questions/9234" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Ruby tile generator](/questions/9234/ruby-tile-generator)

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
<span id="post-9234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9234-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sorry for absolute dumb question... I need to generate the OSM map tiles on the fly on Ruby (Actually on Rhomobile app, which is Ruby based) , so could you hint out which library, extention can do it? On mobile device I have only Sqlite, and I think I should use something like mapName.map as a row, and let it generate the map tiles..Or? Any ideas,hints?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-ruby" rel="tag" title="see questions tagged &#39;ruby&#39;">ruby</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '11, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '11, 15:50</strong> </span></p>
</div>
</div>
<div id="comments-container-9234" class="comments-container">
&#10;</div>
<div id="comment-tools-9234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9234-form-container" class="comment-form-container">
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

<span id="14871"></span>

<div id="answer-container-14871" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14871-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using Ruby will be a difficult requirement here; you might want to try using a webview or similar to dodge it. That said, you can try to compile Mapnik statically and use <a href="https://github.com/mapnik/Ruby-Mapnik">Ruby-Mapnik</a>, or use propublica's <a href="https://github.com/propublica/simple-tiles">simple-tiles</a> library.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '12, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5eea0a101ed06779f56546479dcc80b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcw&#39;s gravatar image" />
<p><span>mcw</span><br />
<span class="score" title="416 reputation points">416</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcw has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-14871" class="comments-container">
<span id="15573"></span>
<div id="comment-15573" class="comment">
<div id="post-15573-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, but deal is that I want to generate tiles on the fly on RhoMobile Framework, which is on Ruby</p>
</div>
<div id="comment-15573-info" class="comment-info">
<span class="comment-age">(28 Aug '12, 10:47)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="15657"></span>
<div id="comment-15657" class="comment">
<div id="post-15657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes; so, you'll either need to compile a static library, or build something yourself in Ruby, which is likely to non-performant and a long process. There is no magic bullet - using RhoMobile restricts what you can do, so either use it with its restrictions, or don't.</p>
</div>
<div id="comment-15657-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 17:27)</span> <span class="comment-user userinfo">mcw</span>
</div>
</div>
</div>
<div id="comment-tools-14871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14871-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14535"></span>

<div id="answer-container-14535" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14535-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-14535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please check my gem <a href="https://github.com/akwiatkowski/gpx2exif">https://github.com/akwiatkowski/gpx2exif</a></p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '12, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/9c980de1d89c9eda9cbe366c24562978?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobik314&#39;s gravatar image" />
<p><span>bobik314</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobik314 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '12, 13:54</strong> </span></p>
</div>
</div>
<div id="comments-container-14535" class="comments-container">
&#10;</div>
<div id="comment-tools-14535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14535-form-container" class="comment-form-container">
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

