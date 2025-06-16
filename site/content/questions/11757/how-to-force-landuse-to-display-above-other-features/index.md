+++
type = "question"
title = "How to force landuse to display above other features?"
description = '''Currently the wikipage for the layer=* tag has all sort of recommandations. It seems that in practice, layers are hard-ignored in a number of circumstances. In this case I need a grassy area to be on top of the building: this parking garage is built &quot;into the hillside&quot; and at its top can be rolled o...'''
date = "2012-04-05T22:54:00Z"
lastmod = "2012-04-06T17:02:00Z"
weight = 11757
keywords = [ "layer", "landuse", "display" ]
aliases = [ "/questions/11757" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to force landuse to display above other features?](/questions/11757/how-to-force-landuse-to-display-above-other-features)

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
<span id="post-11757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11757-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Currently the <a href="https://wiki.openstreetmap.org/wiki/Key:layer">wikipage</a> for the <code>layer=*</code> tag has all sort of recommandations. It seems that in practice, layers are hard-ignored in a number of circumstances. In this case I need <a href="https://www.openstreetmap.org/browse/way/157742329">a grassy area</a> to be on top of the building: this parking garage is built "into the hillside" and at its top can be rolled onto (as can be clearly seen on aerial imagery). However I have been resolutely unable to force the landuse area to layer on top.</p>
<p>Is there a way to actually achieve that or has this been made specifically impossible in the Map style?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '12, 22:54</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
</div>
<div id="comments-container-11757" class="comments-container">
&#10;</div>
<div id="comment-tools-11757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11757-form-container" class="comment-form-container">
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

<span id="11770"></span>

<div id="answer-container-11770" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11770-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When editing osm-data you may want to keep in mind that osm is primarily a geo-database and the map on osm.org is only one possible representation out of this data. If you are not happy with the rendering style provided you are free to use the data and render with it another map according to your needs.</p>
<p>The argument <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">not to tag things incorrectly for the renderer</a> is often used to remind mappers that the database and a resulting map are two different things.</p>
<p>With regard to your case I would suggest to consider the "grassy area on a building" as a roof and tag it accordingly. There are various tagging options for <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Building_attributes">building attributes</a> however not widely used an thus not rendered ond osm.org (yet). Tagging the building a layer=-1 is factually incorrect as it is a building which is clearly above ground.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '12, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/d732dd313768bd27c4ecc89ab4898c69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FischersFritz&#39;s gravatar image" />
<p><span>FischersFritz</span><br />
<span class="score" title="191 reputation points">191</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FischersFritz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11770" class="comments-container">
<span id="11771"></span>
<div id="comment-11771" class="comment">
<div id="post-11771-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm going to go on stron record here as saying that if the renderer is <em>willfully</em> displaying correct tagging incorrectly, that's <strong>turning a feature into a bug</strong> and a terrible thing to have in the system. If layers work for roads and are not explicitly restricted to them features, telling people not to tag for the renderer and then specifically not following the tags in use <em>on semantic grounds</em> (reality is stranger than imagination!) is undermining the entire argument.</p>
</div>
<div id="comment-11771-info" class="comment-info">
<span class="comment-age">(06 Apr '12, 14:56)</span> <span class="comment-user userinfo">Circeus</span>
</div>
</div>
<span id="11773"></span>
<div id="comment-11773" class="comment">
<div id="post-11773-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I do have some doubt, if there is such a thing as an objectively "correct tagging" in osm.</p>
<p>I personally, do not see any good reasons to implement any layer-tagging for landuse objects. Landuse typically refers to somewhat larger areas, and in this case one might consider the landuse to be somewhat transportation-related, or somewhat hospital-related.</p>
<p>If landuse may be understood as the way the land is use by humans, then "grassy" doesn't seem to be an appropriate value for the landuse-tag. Grass rather refers to a surface. So why not use the surface=grass with the roof-tagging?</p>
</div>
<div id="comment-11773-info" class="comment-info">
<span class="comment-age">(06 Apr '12, 15:14)</span> <span class="comment-user userinfo">FischersFritz</span>
</div>
</div>
<span id="11777"></span>
<div id="comment-11777" class="comment">
<div id="post-11777-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm using "grass" because this is private land where no other use is really logical (universities do not have parks in them!). Additionally, the area in question is pretty much outright an <a href="http://g.co/maps/47azx">extension of the hillside on top of the building</a>, which is most certainly not carried over properly by a roof tag as far as I am concerned.</p>
</div>
<div id="comment-11777-info" class="comment-info">
<span class="comment-age">(06 Apr '12, 17:02)</span> <span class="comment-user userinfo">Circeus</span>
</div>
</div>
</div>
<div id="comment-tools-11770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11770-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11758"></span>

<div id="answer-container-11758" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11758-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>Did you try to use the layer=-1 tag for the parking garage ?</em></p>
<p>(I see you had the parking garage at layer=0 and the grassy area as layer=1 but they shared the same nodes in a couple places, so that may have been a cause of it).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Apr '12, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Apr '12, 23:28</strong> </span></p>
</div>
</div>
<div id="comments-container-11758" class="comments-container">
<span id="11759"></span>
<div id="comment-11759" class="comment">
<div id="post-11759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No. I was worried because of the surrounding amenity=university area, and one can only fiddle so much with layers before the map (or your brain) melts down.</p>
</div>
<div id="comment-11759-info" class="comment-info">
<span class="comment-age">(05 Apr '12, 23:24)</span> <span class="comment-user userinfo">Circeus</span>
</div>
</div>
<span id="11769"></span>
<div id="comment-11769" class="comment">
<div id="post-11769-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see you changed the nodes, thanks for that, but it seems unfortunately not to have helped one bit. Tried to put the building at layer -1 and the landuse at layer 1. If that fails, I'll be at a complete loss.</p>
</div>
<div id="comment-11769-info" class="comment-info">
<span class="comment-age">(06 Apr '12, 14:12)</span> <span class="comment-user userinfo">Circeus</span>
</div>
</div>
</div>
<div id="comment-tools-11758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11758-form-container" class="comment-form-container">
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

