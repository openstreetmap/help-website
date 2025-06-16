+++
type = "question"
title = "How to map railway ventilation shafts/vents?"
description = '''These are structures at the surface where hot air from an underground railway is expelled. They can take the form of short chimneys, buildings, grates on the ground or more decorative features.  The London Undergound vents/shafts listed at https://www.openstreetmap.org/relation/2223191 show that a v...'''
date = "2017-12-23T13:28:00Z"
lastmod = "2017-12-26T13:28:00Z"
weight = 61334
keywords = [ "railway", "public-transport", "metro" ]
aliases = [ "/questions/61334" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to map railway ventilation shafts/vents?](/questions/61334/how-to-map-railway-ventilation-shaftsvents)

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
<span id="post-61334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61334-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>These are structures at the surface where hot air from an underground railway is expelled. They can take the form of short chimneys, buildings, grates on the ground or more decorative features.</p>
<p>The London Undergound vents/shafts listed at <a href="https://www.openstreetmap.org/relation/2223191">https://www.openstreetmap.org/relation/2223191</a> show that a variety of tagging methods are used - including building=air_shaft/yes/industrial, man_made=chimney, landuse=railway, name="xxx air vent shaft". There's a few uses of railway=ventilation_shaft on the Washington metro.</p>
<p>Without using a descriptive name what's the best way to tag one?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-metro" rel="tag" title="see questions tagged &#39;metro&#39;">metro</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Dec '17, 13:28</strong></p>
<img src="https://secure.gravatar.com/avatar/9f18ba3d13472af00b3b6e2befad85e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakedistrict&#39;s gravatar image" />
<p><span>lakedistrict</span><br />
<span class="score" title="221 reputation points">221</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakedistrict has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-61334" class="comments-container">
<span id="61368"></span>
<div id="comment-61368" class="comment">
<div id="post-61368-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually, I noticed that some of the 'name="xxx air vent shaft"' ones were in areas where I was familiar with them (and I knew they weren't named). I've retagged these as either man_made= or railway= (if another man_made= tag was already used).</p>
</div>
<div id="comment-61368-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 13:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61334-form-container" class="comment-form-container">
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

<span id="61336"></span>

<div id="answer-container-61336" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61336-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lakedistrict has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've tended to use <code>man_made=</code> or <code>railway=ventilation_shaft</code>, because when I last looked that was the most popular most sensible tagging, at least in the UK. See for example <a href="https://www.openstreetmap.org/node/33479108">here</a> which is rendered as a short chimney <a href="http://map.atownsend.org.uk/maps/map/map.html#zoom=19&amp;lat=53.170958&amp;lon=-1.410024">here</a>.</p>
<p>As an aside, because as you mention the tagging for these can be a bit variable, that map style has some code that brings all these together <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/90e0733593029ab5c4d4ab6d03cc4793853ea982/style.lua#L1564">here</a>. If there's any significant usage of other options I'd be grateful if you could let me know, although "building=blah" and "man_made=chimney" will be rendered as other things elsewhere. The ones identified only by "name=XYZ" could do with a main tag adding, assuming they're genuine.</p>
<p>Taginfo for <a href="https://taginfo.openstreetmap.org/search?q=ventilation_shaft#values"><code>ventilation_shaft</code></a>.</p>
<p>Taginfo for <a href="https://taginfo.openstreetmap.org/search?q=air_shaft#values"><code>air_shaft</code></a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Dec '17, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Dec '17, 20:19</strong> </span></p>
</div>
</div>
<div id="comments-container-61336" class="comments-container">
<span id="61367"></span>
<div id="comment-61367" class="comment">
<div id="post-61367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks SomeoneElse. Although man_made=ventilation_shaft is slightly more popular, I've gone for railway=ventilation_shaft because I think that makes it more obvious that the ventilation shaft is for the railway. I've written a few lines at <a href="https://wiki.openstreetmap.org/wiki/Tyne_and_Wear#Metro_ventilation_shafts">https://wiki.openstreetmap.org/wiki/Tyne_and_Wear#Metro_ventilation_shafts</a> for future reference.</p>
</div>
<div id="comment-61367-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 13:23)</span> <span class="comment-user userinfo">lakedistrict</span>
</div>
</div>
</div>
<div id="comment-tools-61336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61336-form-container" class="comment-form-container">
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

