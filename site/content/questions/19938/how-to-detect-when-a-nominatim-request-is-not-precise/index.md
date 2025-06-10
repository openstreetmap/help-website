+++
type = "question"
title = "How to detect when a Nominatim request is not precise?"
description = '''Hello everyone, I&#x27;m trying to do some reverse geocoding using Nominatim. So far it&#x27;s great. However, there is a problem. I&#x27;ll give an example: I&#x27;ve put some coordinates of a city that is yet to be mapped. Here are some coordinates: lat: -24.18019,lon: -46.78167 - Returns a road called &quot;Av. Condessa ...'''
date = "2013-02-14T18:30:00Z"
lastmod = "2013-02-15T17:01:00Z"
weight = 19938
keywords = [ "nominatim", "reverse", "precision" ]
aliases = [ "/questions/19938" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to detect when a Nominatim request is not precise?](/questions/19938/how-to-detect-when-a-nominatim-request-is-not-precise)

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
<span id="post-19938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19938-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone, I'm trying to do some reverse geocoding using Nominatim. So far it's great. However, there is a problem.</p>
<p>I'll give an example:</p>
<p>I've put some coordinates of a city that is yet to be mapped. Here are some coordinates:</p>
<p><a href="http://nominatim.openstreetmap.org/search.php?q=-24.18019%2C-46.78167">lat: -24.18019,lon: -46.78167</a> - Returns a road called "Av. Condessa de Vimieiros", even though those coordinates belong to "Av. Rui Barbosa".</p>
<p><a href="http://nominatim.openstreetmap.org/search.php?q=-24.18083%2C-46.78525">lat: -24.18083, lon: -46.78525</a> - Returns a road called "Av. Condessa de Vimieiros", even though those coordiantes belong to "R. João Mariano Ferreira".</p>
<p>Now, I think that this one road is being returned because it's the nearest thing mapped to the coordinates I provided. But is there some parameter Nominatim returns to identify wheter or not the location is precise? Or is there even a way to do this?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span> <span class="post-tag tag-link-precision" rel="tag" title="see questions tagged &#39;precision&#39;">precision</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '13, 18:30</strong></p>
<img src="https://secure.gravatar.com/avatar/dc06a3de85eb8aa3a8331e85c1390a79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabriel_casado&#39;s gravatar image" />
<p><span>gabriel_casado</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabriel_casado has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '13, 09:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span></p>
</div>
</div>
<div id="comments-container-19938" class="comments-container">
<span id="19945"></span>
<div id="comment-19945" class="comment">
<div id="post-19945-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Just to be clear about the problem: there <em>is</em> a street at the selected coordinates, but it doesn't have a name (and therefore no nominatim place_id ?), so nominatime returns the closest named object without a mention of the nameless one.</p>
</div>
<div id="comment-19945-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 09:19)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="19956"></span>
<div id="comment-19956" class="comment">
<div id="post-19956-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span></span><span>@Vincent de Phily</span></p>
<p>Exactly this. There is a street in the said coordinate, but it doesn't have a name so it returns the closest one.</p>
<p>Is there a way to impeach Nominatim from returning me the closest place, and instead returning me an error message or something?</p>
</div>
<div id="comment-19956-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 12:29)</span> <span class="comment-user userinfo">gabriel_casado</span>
</div>
</div>
</div>
<div id="comment-tools-19938" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19938-form-container" class="comment-form-container">
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

<span id="19962"></span>

<div id="answer-container-19962" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19962-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gabriel_casado has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The nominatim api does not have this feature.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '13, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-19962" class="comments-container">
<span id="19964"></span>
<div id="comment-19964" class="comment">
<div id="post-19964-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is no workaround to this?</p>
</div>
<div id="comment-19964-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 15:34)</span> <span class="comment-user userinfo">gabriel_casado</span>
</div>
</div>
<span id="19968"></span>
<div id="comment-19968" class="comment">
<div id="post-19968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are always workarounds:</p>
<ul>
<li>You could use a different (reverse) geocoder.</li>
<li>You could write some new <a href="http://github.com/twain47/Nominatim">code for Nominatim</a>, so it will support this in the future.</li>
<li>etc.</li>
</ul>
<p>Yes, I understand this is not the answer you wanted to get, but sometimes life is just that way.</p>
</div>
<div id="comment-19968-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 16:57)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="19970"></span>
<div id="comment-19970" class="comment">
<div id="post-19970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I get it. Thanks.</p>
</div>
<div id="comment-19970-info" class="comment-info">
<span class="comment-age">(15 Feb '13, 17:01)</span> <span class="comment-user userinfo">gabriel_casado</span>
</div>
</div>
</div>
<div id="comment-tools-19962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19962-form-container" class="comment-form-container">
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

