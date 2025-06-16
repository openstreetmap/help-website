+++
type = "question"
title = "Source geometry in OSM maps?"
description = '''Is there an OSM map that shows the original/source geometry without manipulation, for instance in the highest zoom/scale?  Testing some 20-25 publicly available maps I could not find one. Many geometries look just fine/perfect but actually they are wrong. Consequently, many anomalies remain not corr...'''
date = "2017-04-25T11:03:00Z"
lastmod = "2017-04-27T13:08:00Z"
weight = 55850
keywords = [ "mapsource", "rendering", "anomalies" ]
aliases = [ "/questions/55850" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Source geometry in OSM maps?](/questions/55850/source-geometry-in-osm-maps)

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
<span id="post-55850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55850-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-55850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there an OSM map that shows the original/source geometry without manipulation, for instance in the highest zoom/scale?<br />
Testing some 20-25 publicly available maps I could not find one. Many geometries look just fine/perfect but actually they are wrong. Consequently, many anomalies remain not corrected in a long time (maybe for ever) because they look fine in maps the (local) mappers are looking at. Let me illustrate the issue with some line-work objects, for instance roundabouts. Looking at examples here <a href="https://goo.gl/VMTwSI">https://goo.gl/VMTwSI</a> or here <a href="https://goo.gl/zOHfJZ">https://goo.gl/zOHfJZ</a> we may get an impression that these geometries are correct and nice. However, in the source data these geometries look badly like here <a href="https://goo.gl/eEImHh">https://goo.gl/eEImHh</a> or here <a href="https://goo.gl/UsUS3m.">https://goo.gl/UsUS3m.</a> There are some 10K similar roundabout ussies (not counting error cases) some of them being really serious anomalies like here <a href="http://osm.org/go/T87HnTe2C">http://osm.org/go/T87HnTe2C</a> . The roundabout looks just perfect but, essentially, in the source data this roundabout does not exist at all.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapsource" rel="tag" title="see questions tagged &#39;mapsource&#39;">mapsource</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-anomalies" rel="tag" title="see questions tagged &#39;anomalies&#39;">anomalies</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '17, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></p>
</div>
</div>
<div id="comments-container-55850" class="comments-container">
&#10;</div>
<div id="comment-tools-55850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55850-form-container" class="comment-form-container">
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

<span id="55851"></span>

<div id="answer-container-55851" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55851-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most maps generated from OSM data are intended to be maps and the rendering process will tend to smooth out small irregularities and (for example if Bezier curves are used) might even show geometries that do not exist in that form in the original data. This is not specific to OSM btw. The data layer on openstreetmap.org shows the original geometry as do most editors.</p>
<p>Naturally from a pedantic pov the roundabouts themselves should really be cleaned up and it would seem to be a good subject for a <a href="http://maproulette.org/">maproulette challenge</a> if you can generate a list.</p>
<p>Note: your last example may simply be a case of wrong tagging (not everything that looks circular is legally a roundabout).</p>
<p>Edit: see my comment below DaveF answer: what is likely happening is that whatever you are using to extract OSM data is loosing precision on export, as the geometries you have in your illustrations have nothing to do with what is in the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '17, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Apr '17, 14:25</strong> </span></p>
</div>
</div>
<div id="comments-container-55851" class="comments-container">
<span id="55901"></span>
<div id="comment-55901" class="comment">
<div id="post-55901-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Simon, thanks for your time. I fully agree about the map-makers data preparation strategies. Implicitly you are saying that you don't no for an OSM map that has an option to show the source (not manipulated) data in some higher scale. I know this is not a place for arguing but for clarity I have to add two more comments.<br />
The "edit" text is confusing and could be valid in one and only one case - if the OSM regular dump is wrong (essentially not a "dump"). Otherwise, the examples perfectly reflect the data from the dump with no precision loss and the image format here is irrelevant.<br />
The "note" related to the last example is also confusing. The problem/error is more in geometry than in tagging. In the roundabout construct ( <a href="https://goo.gl/aVc6JN">https://goo.gl/aVc6JN</a> ) there are 4 poly-lines all tagged roundabout. So, there is much higher probability that the circular shape in the middle is a roundabout compared to your suggestion (in brackets). Though, there is no even a segment of that shape in the source data.</p>
</div>
<div id="comment-55901-info" class="comment-info">
<span class="comment-age">(26 Apr '17, 22:24)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-55851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55851-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55858"></span>

<div id="answer-container-55858" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55858-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Where are you getting your source data/images from?</p>
<p>This is the first roundabout in Wireframe mode in Potlatch 2. Looks pretty round to me: <a href="https://www.openstreetmap.org/edit#map=21/45.52146/-122.64957">https://www.openstreetmap.org/edit#map=21/45.52146/-122.64957</a></p>
<p>Could your Jpeg creator be set to low detail?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '17, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-55858" class="comments-container">
<span id="55860"></span>
<div id="comment-55860" class="comment">
<div id="post-55860-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would not be a JPEG artefact, if it is actually on output only it looks like (too) limited precision in the output coordinates as you can clearly see a point raster.</p>
</div>
<div id="comment-55860-info" class="comment-info">
<span class="comment-age">(25 Apr '17, 14:20)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="55897"></span>
<div id="comment-55897" class="comment">
<div id="post-55897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The data is from the OSM dump, XML format, from some weeks ago. The images are JPG format of the screen dump from a vector map/rendering, and perfectly reflect the vectors/poly-lines in 1:1 scale from the source and there is no precision loss. The objects are the same in years and that is my point. In maps they are rendered manipulated and just fine, so there is no anomaly visualisation that could trigger the local mappers attention.</p>
</div>
<div id="comment-55897-info" class="comment-info">
<span class="comment-age">(26 Apr '17, 21:03)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="55902"></span>
<div id="comment-55902" class="comment">
<div id="post-55902-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just loaded way 158898111 into JOSM and the nodes in the source data are arranged in a perfect circle. Whatever's causing the loss of precision is happening somewhere in your toolchain, which apparently isn't the perfect 1:1 reflection that you thought. What software are you using that displays the "drunken" roundabouts?</p>
</div>
<div id="comment-55902-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 00:16)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="55911"></span>
<div id="comment-55911" class="comment">
<div id="post-55911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/3194/sanser">@sanser</a> Provide your source XML for this one: <a href="https://goo.gl/eEImHh">https://goo.gl/eEImHh</a></p>
</div>
<div id="comment-55911-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 13:08)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-55858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55858-form-container" class="comment-form-container">
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

