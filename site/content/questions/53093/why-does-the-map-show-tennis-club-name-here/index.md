+++
type = "question"
title = "Why does the map show tennis club name here?"
description = '''I noticed the name St Peters Tennis Club showing in the centre of this area of the map https://www.openstreetmap.org/#map=18/-37.79216/175.27879&amp;amp;layers=N From local knowledge I&#x27;m pretty certain there isn&#x27;t a tennis club here and one isn&#x27;t visible on Bing imagery. I checked on JOSM but wasn&#x27;t abl...'''
date = "2016-11-24T08:16:00Z"
lastmod = "2016-11-25T08:58:00Z"
weight = 53093
keywords = [ "display_error" ]
aliases = [ "/questions/53093" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does the map show tennis club name here?](/questions/53093/why-does-the-map-show-tennis-club-name-here)

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
<span id="post-53093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53093-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed the name St Peters Tennis Club showing in the centre of this area of the map <a href="https://www.openstreetmap.org/#map=18/-37.79216/175.27879&amp;layers=N">https://www.openstreetmap.org/#map=18/-37.79216/175.27879&amp;layers=N</a></p>
<p>From local knowledge I'm pretty certain there isn't a tennis club here and one isn't visible on Bing imagery. I checked on JOSM but wasn't able to activate a node or area relating to the club in this area.</p>
<p>The 'real' tennis club is further south east on Palmerston Street <a href="https://www.openstreetmap.org/relation/5317658">https://www.openstreetmap.org/relation/5317658</a> Did I do something wrong when I mapped it last year that causes the name to display in the wrong position?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-display_error" rel="tag" title="see questions tagged &#39;display_error&#39;">display_error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Nov '16, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0b78593a39b9f71b9697697876327c6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NZGraham&#39;s gravatar image" />
<p><span>NZGraham</span><br />
<span class="score" title="1814 reputation points"><span>1.8k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="49 badges"><span class="bronze">●</span><span class="badgecount">49</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NZGraham has 7 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '16, 09:30</strong> </span></p>
</div>
</div>
<div id="comments-container-53093" class="comments-container">
<span id="53101"></span>
<div id="comment-53101" class="comment">
<div id="post-53101-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure if it's the same issue, but a similar problem is <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/2428">https://github.com/gravitystorm/openstreetmap-carto/issues/2428</a> , and some of the comments there apply here.</p>
<p>Not entirely sure why you've got the grounds of the club as "leisure=pitch" though and the courts not tagged as anything though? I'd have thought, if you're mapping individual courts, that they'd be leisure=pitch like for example <a href="https://www.openstreetmap.org/way/337033246">https://www.openstreetmap.org/way/337033246</a> is?</p>
</div>
<div id="comment-53101-info" class="comment-info">
<span class="comment-age">(24 Nov '16, 18:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53093-form-container" class="comment-form-container">
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

<span id="53099"></span>

<div id="answer-container-53099" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53099-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is likely a rendering artefact (aka bug in the style or mapnik and rather unlikely) or corrupted data in the rendering database(s). I've checked the object itself and there doesn't seem to be anything wrong, which is further supported by other styles not having the issue.</p>
<p>After various attempts to get the rendering to change I suspect that it is in fact a label placement issue (I'll investigate further). In any case mapping the facility as a multi-polygon was IMHO incorrect since the pitches are clearly part of the facility and shouldn't be punched as holes out of it (if site relation were better supported I would have suggested that). Unluckily there is no really well established tagging for clubs that I could find so the net result of the changes that I've made now are not really satisfactory, you might want to move the name of the club to the building.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '16, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '16, 19:57</strong> </span></p>
</div>
</div>
<div id="comments-container-53099" class="comments-container">
<span id="53104"></span>
<div id="comment-53104" class="comment">
<div id="post-53104-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Simon, I'd agree that name position is possibly a rendering issue especially given that everything displays ok on OsmAnd. My original intention of using a multi-polygon was to 'unify' all elements relating to the tennis club (overall area, actual courts, clubhouse, parking) in a single feature. Possibly this was misguided - I'm very much at 'toe-in-the-water' stage so far as multi-polygons / relations are concerned. I've now added the name of the club to the building although I have still left it on the area outline. Maybe it shouldn't be on both? Perhaps I should be using something similar to mapping school premises as a guideline <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool</a></p>
</div>
<div id="comment-53104-info" class="comment-info">
<span class="comment-age">(24 Nov '16, 22:40)</span> <span class="comment-user userinfo">NZGraham</span>
</div>
</div>
<span id="53107"></span>
<div id="comment-53107" class="comment">
<div id="post-53107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Removing the name on the building makes sense to me. Also, we tend to not abbreviate names in OSM, because a machine can make St from Saint, but not Saint from St.</p>
</div>
<div id="comment-53107-info" class="comment-info">
<span class="comment-age">(25 Nov '16, 08:58)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-53099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53099-form-container" class="comment-form-container">
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

