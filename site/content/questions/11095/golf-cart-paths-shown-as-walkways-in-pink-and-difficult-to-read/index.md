+++
type = "question"
title = "Golf cart paths shown as walkways (in pink) and difficult to read."
description = '''I live in a community (Peachtree City, GA - USA) with over one-hundred miles of golf cart paths separate from roadways for automobiles. On OpenStreeMap, these pathways are listed as walkways and the color &quot;pink&quot; is used to indicate their presence. The use of this color makes it difficult to follow t...'''
date = "2012-03-10T14:43:00Z"
lastmod = "2012-03-12T14:01:00Z"
weight = 11095
keywords = [ "color", "difficult", "format" ]
aliases = [ "/questions/11095" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Golf cart paths shown as walkways (in pink) and difficult to read.](/questions/11095/golf-cart-paths-shown-as-walkways-in-pink-and-difficult-to-read)

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
<span id="post-11095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11095-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I live in a community (Peachtree City, GA - USA) with over one-hundred miles of golf cart paths separate from roadways for automobiles.</p>
<p>On OpenStreeMap, these pathways are listed as walkways and the color "pink" is used to indicate their presence. The use of this color makes it difficult to follow the golf cart paths.</p>
<p>Is there a way in OpenStreetMap.org to change the color and / or use a different format for golf cart paths?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-color" rel="tag" title="see questions tagged &#39;color&#39;">color</span> <span class="post-tag tag-link-difficult" rel="tag" title="see questions tagged &#39;difficult&#39;">difficult</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '12, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/b3b70421e4ad3beb10af9c85737ba2c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trucker777&#39;s gravatar image" />
<p><span>Trucker777</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trucker777 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11095" class="comments-container">
&#10;</div>
<div id="comment-tools-11095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11095-form-container" class="comment-form-container">
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

<span id="11097"></span>

<div id="answer-container-11097" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11097-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you considered using access tags on a <code>highway=service</code> or <code>highway=unclassified</code> tag? Sounds like <code>motor_vehicle=no</code>+<code>golf_cart=yes</code> on one of those will do what you need. <code>highway=path</code> with golf_cart=yes` may be another more appropriate tag. The tag is usually applied to unpaved routes, but it's meaning ("A route open to the public which is not intended for motor vehicles, unless so tagged separately.") applies fine here and is devoid of specifics regarding cover.</p>
<p>Anything having to do with access will tend to be a bit messy because of the OSM tag source being the UK, which has cause a complex web of access-tied highway tags to develop that do not necessarily translate well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '12, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
</div>
<div id="comments-container-11097" class="comments-container">
<span id="11136"></span>
<div id="comment-11136" class="comment">
<div id="post-11136-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Additionally, I see some highways with ref= tags that neglect to include "GA " prefixes (presuming they're state highways).</p>
</div>
<div id="comment-11136-info" class="comment-info">
<span class="comment-age">(12 Mar '12, 14:01)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-11097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11097-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11110"></span>

<div id="answer-container-11110" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11110-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(assuming we're talking about <a href="https://www.openstreetmap.org/?lat=33.39176&amp;lon=-84.57129&amp;zoom=17">here</a>)</p>
<p>The rendering of "highway=footway" in red is probably a historical artefact - footpaths on GB Ordnance Survey 1:50,000 maps are shown in red, and I suspect that it seemed like a good idea on OSM too (the same as with blue motorways).</p>
<p>If the OSM home page's "Standard" rendering isn't working for you you shouldn't need to change the data; just use a different renderer. It might be that the "Cycle Map" on OSM's home page works better for you (that shows them in brown rather than red, or maybe you might want to create your own maps based on OSM data.<br />
</p>
<p>There have been help questions in the past about it - if you search for "maperitive" (which is a way of creating your own maps that is often suggested) you'll find most of them. There are also numerous wiki pages - the "rendering" page is a bunch of links to get you started.</p>
<p>Finally if all you want to do is change the colour of "highway-footway" you could follow one of the sets of instructions on <a href="http://switch2osm.org/serving-tiles/">switch2osm</a> - that describes setting up a standard OSM Mapnik stylesheet, but if you change "salmon" to "other colour of your choice" in there you'll get "highway-footway" rendered in that other colour.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '12, 00:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-11110" class="comments-container">
<span id="11124"></span>
<div id="comment-11124" class="comment">
<div id="post-11124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the suggestions. I will give them a try and see how it looks.</p>
</div>
<div id="comment-11124-info" class="comment-info">
<span class="comment-age">(11 Mar '12, 16:43)</span> <span class="comment-user userinfo">Trucker777</span>
</div>
</div>
</div>
<div id="comment-tools-11110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11110-form-container" class="comment-form-container">
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

