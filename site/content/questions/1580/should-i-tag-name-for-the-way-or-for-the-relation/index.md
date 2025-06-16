+++
type = "question"
title = "Should I tag &quot;name&quot; for the way or for the relation?"
description = '''Hello, I have a hiking route that I want to add a tag &quot;name&quot; for. The route is consisting of several ways which are gathered together in a relation. Where should I add the &quot;name&quot; tag? To each of the different ways, or to the relation itself. In order to display a name along the route, Mapnik and Osm...'''
date = "2010-11-21T17:39:00Z"
lastmod = "2010-11-21T18:04:00Z"
weight = 1580
keywords = [ "osmarender", "mapnik", "tagging", "relations", "name" ]
aliases = [ "/questions/1580" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should I tag "name" for the way or for the relation?](/questions/1580/should-i-tag-name-for-the-way-or-for-the-relation)

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
<span id="post-1580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1580-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have a hiking route that I want to add a tag "name" for. The route is consisting of several ways which are gathered together in a relation. Where should I add the "name" tag? To each of the different ways, or to the relation itself.</p>
<p>In order to display a name along the route, Mapnik and Osmarender require each of the ways to have the "name" tag. If I add name only to the relation it is not rendered. However something tells that tagging is not correct, because it is not right to name a way. It is not a street, but a field track or path. It does not have a specific naming and doesn't seem right to name it after one of the many targets you can reach via that way. Also it is hard to add name for all of the relation ways (they can be many) - the right thing seem to be adding name to the relation itself.</p>
<p>What do you think is the correct naming here?</p>
<p>Just for information, this is the relation I'm talking about: <a href="https://www.openstreetmap.org/browse/relation/1279512">https://www.openstreetmap.org/browse/relation/1279512</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmarender" rel="tag" title="see questions tagged &#39;osmarender&#39;">osmarender</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '10, 17:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
</div>
<div id="comments-container-1580" class="comments-container">
&#10;</div>
<div id="comment-tools-1580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1580-form-container" class="comment-form-container">
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

<span id="1581"></span>

<div id="answer-container-1581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1581-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-1581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the name only applies to the whole hiking route, then set the name tag on the relation connection the ways that form the different ways.</p>
<p>Don't worry that mapnik and osmarender don't render the name of the hiking route. A map dedicated on hiking or a navigation device will still pick it up. Changing the tagging just to make it render on a particular map rendering is called "tagging for the renderer" and is frowned upon. Keep in mind that the mapnik rendering can't render all information and cater to all audiences because it would get so crowded that it's useless for everybody.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '10, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-1581" class="comments-container">
&#10;</div>
<div id="comment-tools-1581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1581-form-container" class="comment-form-container">
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

