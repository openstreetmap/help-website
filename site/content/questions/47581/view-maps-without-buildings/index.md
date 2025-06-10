+++
type = "question"
title = "View maps without buildings"
description = '''Hey everyone, this is more of a user based question than a technical one. If I wanted to embed OSM on my website, how can I turn off the buildings and other overlays like commerical areas and residential areas? Thanks!'''
date = "2016-01-19T09:59:00Z"
lastmod = "2016-01-19T19:01:00Z"
weight = 47581
keywords = [ "layers", "overlays" ]
aliases = [ "/questions/47581" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [View maps without buildings](/questions/47581/view-maps-without-buildings)

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
<span id="post-47581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47581-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey everyone, this is more of a user based question than a technical one. If I wanted to embed OSM on my website, how can I turn off the buildings and other overlays like commerical areas and residential areas?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-overlays" rel="tag" title="see questions tagged &#39;overlays&#39;">overlays</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '16, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/01d0d9046e3c896488038c8755ba6d48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeteInIndia&#39;s gravatar image" />
<p><span>PeteInIndia</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeteInIndia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47581" class="comments-container">
<span id="47597"></span>
<div id="comment-47597" class="comment">
<div id="post-47597-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which rendering are you referring to? There are countless different renderings of the OpenStreetMap data, and quite a few of them don't contain any "overlays".</p>
</div>
<div id="comment-47597-info" class="comment-info">
<span class="comment-age">(19 Jan '16, 16:54)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="47599"></span>
<div id="comment-47599" class="comment">
<div id="post-47599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, to clarify I meant with the Standard layer or the MapQuest Open layer. I wanted to be able to display the map but without the buildings and most of the overlays that denote the commercial/residential neighbourhoods.</p>
</div>
<div id="comment-47599-info" class="comment-info">
<span class="comment-age">(19 Jan '16, 17:54)</span> <span class="comment-user userinfo">PeteInIndia</span>
</div>
</div>
</div>
<div id="comment-tools-47581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47581-form-container" class="comment-form-container">
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

<span id="47602"></span>

<div id="answer-container-47602" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47602-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-47602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The standard and MapQuest Open layers use pre-rendered tiles. That is, they take the OSM data, apply certain rules that they've determined ahead of time to define how objects should be rendered, and then static image files are created. There are no overlays, so if someone wanted to remove some objects, such a change would have to occur earlier in the rendering process by changing the rules.</p>
<p>If you want a rendering without buildings, you'll have to look at alternate providers. <a href="http://wiki.openstreetmap.org/wiki/List_of_OSM-based_services">This list</a> is a good starting point, but there are probably many others out there that may not be on this list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '16, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-47602" class="comments-container">
&#10;</div>
<div id="comment-tools-47602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47602-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47605"></span>

<div id="answer-container-47605" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47605-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another option that may or may not work for you is to <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">create your own map tiles</a>. If you only want a small area (say the size of one smallish country rather than the whole world) the server you'd need to do that is "desktop PC" or smaller not "large expensive server". You could if you wanted to use the <a href="https://github.com/gravitystorm/openstreetmap-carto">"standard" style</a> unchanged and remove buildings from the data before creating map tiles (actually only about 3 lines of code), though of course "creating your own map tiles" is always going to be more complicated than "using someone else's".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '16, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-47605" class="comments-container">
&#10;</div>
<div id="comment-tools-47605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47605-form-container" class="comment-form-container">
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

