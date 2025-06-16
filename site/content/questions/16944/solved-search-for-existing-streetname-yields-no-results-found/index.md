+++
type = "question"
title = "[solved] Search for existing streetname yields &quot;No results found&quot;"
description = '''Hello, I recently did a search for &quot;Forest Road Oceanside California&quot;. It yielded &quot;No results found&quot;, even when the street name was visible on the map in front of me. I&#x27;m I doing something wrong? Are streetname searches supported? Thank You for any guidance! John'''
date = "2012-10-16T20:19:00Z"
lastmod = "2012-10-16T21:26:00Z"
weight = 16944
keywords = [ "search", "nominatim", "streetname" ]
aliases = [ "/questions/16944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[solved\] Search for existing streetname yields "No results found"](/questions/16944/solved-search-for-existing-streetname-yields-no-results-found)

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
<span id="post-16944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16944-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I recently did a search for "Forest Road Oceanside California".</p>
<p>It yielded "No results found", even when the street name was visible on the map in front of me.</p>
<p>I'm I doing something wrong?</p>
<p>Are streetname searches supported?</p>
<p>Thank You for any guidance!</p>
<p>John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-streetname" rel="tag" title="see questions tagged &#39;streetname&#39;">streetname</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '12, 20:19</strong></p>
<img src="https://secure.gravatar.com/avatar/6117a321406484e67f25785d50c71361?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnea&#39;s gravatar image" />
<p><span>johnea</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnea has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '12, 21:29</strong> </span></p>
</div>
</div>
<div id="comments-container-16944" class="comments-container">
&#10;</div>
<div id="comment-tools-16944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16944-form-container" class="comment-form-container">
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

<span id="16947"></span>

<div id="answer-container-16947" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16947-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim (that is what powers the search box on the osm.org website) uses a combination of boundaries and place nodes to determine in which place a street lies. This is necessary because OSM does not have complete boundaries for every place in the world (yet ;)</p>
<p>If you search for "Forest Road, San Diego County, California", then it finds <a href="https://www.openstreetmap.org/?minlon=-117.33472442627&amp;minlat=33.2367172241211&amp;maxlon=-117.331588745117&amp;maxlat=33.2369842529297">Forest Road, Rancho San Luis Rey Trailer Park, San Diego County, California, 92054, United States of America</a>. Is that the one you are looking for?</p>
<p>For more technical details look at some other questions tagged with "nominatim".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '12, 21:14</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '12, 21:15</strong> </span></p>
</div>
</div>
<div id="comments-container-16947" class="comments-container">
<span id="16948"></span>
<div id="comment-16948" class="comment">
<div id="post-16948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you cartinus!</p>
<p>Yes, the search with "San Diego County" does return the correct location.</p>
<p>I'll use the county name for further local searches, rather than specific city names.</p>
<p>Thank you also for adding the "nominatim" tag.</p>
<p>I'll dig into some of the other questions with this tag to more deeply understand the search criteria.</p>
<p>Thank You for your contribution to openstreetmaps!</p>
<p>johnea</p>
</div>
<div id="comment-16948-info" class="comment-info">
<span class="comment-age">(16 Oct '12, 21:26)</span> <span class="comment-user userinfo">johnea</span>
</div>
</div>
</div>
<div id="comment-tools-16947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16947-form-container" class="comment-form-container">
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

