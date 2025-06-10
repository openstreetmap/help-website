+++
type = "question"
title = "Forest displayed below university grounds"
description = '''This happens on many renderings, including the default openstreetmap.org map and OSMAnd. On those maps, a part of forest I mapped (natural=wood) that intersects with a university campus (amenity=university) is displayed below the university campus instead of above it. I have seen many places with wo...'''
date = "2021-04-01T11:36:00Z"
lastmod = "2021-04-01T13:08:00Z"
weight = 79466
keywords = [ "rendering", "university", "forest" ]
aliases = [ "/questions/79466" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Forest displayed below university grounds](/questions/79466/forest-displayed-below-university-grounds)

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
<span id="post-79466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79466-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This happens on many renderings, including the default openstreetmap.org map and OSMAnd.</p>
<p>On those maps, a part of forest I mapped (natural=wood) that intersects with a university campus (amenity=university) is displayed below the university campus instead of above it. I have seen many places with woods on campuses that were displayed fine, it's just this one, and I don't understand why. Should I map it differently?</p>
<p>The area is question is <a href="https://www.openstreetmap.org/#map=19/59.21747/17.93989">here</a>.</p>
<p><img src="https://help.openstreetmap.org/upfiles/forest_campus.png" alt="illustration of the issue" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-university" rel="tag" title="see questions tagged &#39;university&#39;">university</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '21, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/11d9b17a075215f8f0069f3e9f2aaebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Giom&#39;s gravatar image" />
<p><span>Giom</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Giom has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-79466" class="comments-container">
&#10;</div>
<div id="comment-tools-79466" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79466-form-container" class="comment-form-container">
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

<span id="79468"></span>

<div id="answer-container-79468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79468-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Should I map it differently?</p>
</blockquote>
<p>No - if you've mapped what really exists it's up to the renderers to show it properly.</p>
<p>Note that some woodland areas in universities display <a href="https://www.openstreetmap.org/relation/10547132#map=17/53.94977/-1.01621https://www.openstreetmap.org/relation/10547132#map=17/53.94977/-1.01621">as expected</a>. What might be happening here (in OSM Carto at least) is the "display smaller things on top of larger things" logic not working in you edge case. Note the use of "way_pixels" <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/b10aef3866bacf387581b8fea4eec265010b0d14/style/landcover.mss#L575">here</a>.</p>
<p>For OSM Carto, perhaps see if someone has already asked about it at the <a href="https://github.com/gravitystorm/openstreetmap-carto/issues">issues list</a>, and if not ask yourself?</p>
<p>For Osmand there is currently a <a href="https://groups.google.com/g/osmand">Google Group</a> in which those sorts of questions can be asked of other users.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '21, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '21, 12:22</strong> </span></p>
</div>
</div>
<div id="comments-container-79468" class="comments-container">
<span id="79469"></span>
<div id="comment-79469" class="comment">
<div id="post-79469-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is certainly an issue about this, I'll see if I can find it.</p>
</div>
<div id="comment-79469-info" class="comment-info">
<span class="comment-age">(01 Apr '21, 13:08)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79468-form-container" class="comment-form-container">
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

