+++
type = "question"
title = "Searching within relations which are not boundarys."
description = '''One can search withing relations like this: node(area:3600062422)[&quot;addr:city&quot;]; out meta; But this does only work for boundary relations because they are preprocessed by the overpass api. How to search within other relations like this one: http://www.openstreetmap.org/relation/3734750'''
date = "2014-05-22T22:36:00Z"
lastmod = "2014-05-26T18:49:00Z"
weight = 33388
keywords = [ "relation", "overpass-api" ]
aliases = [ "/questions/33388" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Searching within relations which are not boundarys.](/questions/33388/searching-within-relations-which-are-not-boundarys)

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
<span id="post-33388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33388-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>One can search withing relations like this:</p>
<p><code>node(area:3600062422)["addr:city"]; out meta;</code></p>
<p>But this does only work for boundary relations because they are preprocessed by the overpass api. How to search within other relations like this one: <a href="http://www.openstreetmap.org/relation/3734750">http://www.openstreetmap.org/relation/3734750</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 May '14, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-33388" class="comments-container">
<span id="33434"></span>
<div id="comment-33434" class="comment">
<div id="post-33434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In case of no sufficient answer here, try to ask at the discussion page in the OSM wiki: <a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo">http://wiki.openstreetmap.org/wiki/Overpass_turbo</a></p>
</div>
<div id="comment-33434-info" class="comment-info">
<span class="comment-age">(23 May '14, 17:14)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-33388" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33388-form-container" class="comment-form-container">
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

<span id="33488"></span>

<div id="answer-container-33488" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33488-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The relation you mentioned doesn't match any of the existing extraction rules, that's why you won't get any result when querying with this relation id. A similar requirement to relax this restriction is currently on the Overpass API "Enhancement Suggestions" list. Please see <span></span><a href="https://github.com/drolbr/Overpass-API/issues/77">https://github.com/drolbr/Overpass-API/issues/77</a> for more details.</p>
<p>For the time being you could set up your own Overpass API instance and adjust areas.osm3s to suit your needs. However, to get this up and running might require some significant time and effort depending on your prior experience.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '14, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-33488" class="comments-container">
&#10;</div>
<div id="comment-tools-33488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33488-form-container" class="comment-form-container">
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

