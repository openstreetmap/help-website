+++
type = "question"
title = "Find Highways beside lake, greeneries etc"
description = '''How do I find highways, could be of any type i.e. secondary, tertiary etc., which are beside a water body or which are beside green places or mountain roads.'''
date = "2017-06-30T13:56:00Z"
lastmod = "2017-07-04T07:43:00Z"
weight = 56813
keywords = [ "greenery", "lake", "highway" ]
aliases = [ "/questions/56813" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Find Highways beside lake, greeneries etc](/questions/56813/find-highways-beside-lake-greeneries-etc)

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
<span id="post-56813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56813-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I find highways, could be of any type i.e. secondary, tertiary etc., which are beside a water body or which are beside green places or mountain roads.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-greenery" rel="tag" title="see questions tagged &#39;greenery&#39;">greenery</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '17, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/85d97df64f090abb5cfb29a669e37913?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ones%20Infinite&#39;s gravatar image" />
<p><span>Ones Infinite</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ones Infinite has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56813" class="comments-container">
&#10;</div>
<div id="comment-tools-56813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56813-form-container" class="comment-form-container">
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

<span id="56855"></span>

<div id="answer-container-56855" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56855-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ones Infinite has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"mountain roads" is a little vague, and I don't think roads are tagged like that in OSM. Likewise what exactly do you mean by "green areas"?</p>
<p>Some idea:</p>
<ul>
<li>I'm not really aware of a general way to do this, you might be able to do it with some PostGIS querying. Import the data with osm2pgsql then do some spatial analyze.</li>
<li>Use Overpass Turbo to find all waterbodies, and then just "eyeball" it to find roads that are interesting to you.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '17, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-56855" class="comments-container">
<span id="56866"></span>
<div id="comment-56866" class="comment">
<div id="post-56866-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>+1 for finding water bodies and looking for roads nearby... By green areas, I mean roads beside forests, gardens with trees, plants etc. And these roads should be as wide so that a car would be easily driven on them. Any specific tags for locating such areas?</p>
</div>
<div id="comment-56866-info" class="comment-info">
<span class="comment-age">(04 Jul '17, 02:30)</span> <span class="comment-user userinfo">Ones Infinite</span>
</div>
</div>
<span id="56868"></span>
<div id="comment-56868" class="comment">
<div id="post-56868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>take a look at the wiki page for <a href="https://wiki.openstreetmap.org/wiki/Key:highway">highway</a>, anything that is not "a path" should be OK for cars. Please note that you might also have to take surface etc into account, because some roads/tracks are only accessible with a 4x4.</p>
</div>
<div id="comment-56868-info" class="comment-info">
<span class="comment-age">(04 Jul '17, 04:48)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="56869"></span>
<div id="comment-56869" class="comment">
<div id="post-56869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> and what would be the tag for green areas?</p>
</div>
<div id="comment-56869-info" class="comment-info">
<span class="comment-age">(04 Jul '17, 04:57)</span> <span class="comment-user userinfo">Ones Infinite</span>
</div>
</div>
<span id="56873"></span>
<div id="comment-56873" class="comment">
<div id="post-56873-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>landuse=forest, leisure=park, leisure=garden, natural=tree_row, landuse=orchard, natural=scrub, ... Please take a look at the wiki, especially the page listing the "main" <a href="https://wiki.openstreetmap.org/wiki/Map_Features">features</a></p>
</div>
<div id="comment-56873-info" class="comment-info">
<span class="comment-age">(04 Jul '17, 07:43)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-56855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56855-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56817"></span>

<div id="answer-container-56817" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56817-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not aware of a general way to find roads near water bodies or beside or in mountainous areas. However if I were looking for roads of that nature, I'd likely be looking for them as a scenic way to travel. Based on that, you might be able to search for roads with the <a href="https://wiki.openstreetmap.org/wiki/Key:scenic">scenic tag</a> on them. That said, I know of a number of highways around my area that are officially signed as scenic roads but are not tagged as such in OSM. (I guess one of these days I need to drive them and note the exact extent of the official scenic signage and then tag them in OSM.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '17, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-56817" class="comments-container">
<span id="56835"></span>
<div id="comment-56835" class="comment">
<div id="post-56835-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5918/stf">@stf</a> Any other way, any trick to sort of find something close to what I'm looking for here?</p>
</div>
<div id="comment-56835-info" class="comment-info">
<span class="comment-age">(02 Jul '17, 12:44)</span> <span class="comment-user userinfo">Ones Infinite</span>
</div>
</div>
</div>
<div id="comment-tools-56817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56817-form-container" class="comment-form-container">
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

