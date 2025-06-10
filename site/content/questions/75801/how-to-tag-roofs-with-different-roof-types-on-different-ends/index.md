+++
type = "question"
title = "How to tag roofs with different roof types on different ends?"
description = '''Simple 3D buildings on the OSM wiki defines several roof shapes. However, they all seem to be mostly symmetric. In the area where I was thinking of tagging roof shapes, it is a very common pattern to have the roof be &quot;hipped&quot; towards the end of the building that faces the street, and &quot;gabled&quot; in the...'''
date = "2020-07-20T11:38:00Z"
lastmod = "2020-07-20T15:19:00Z"
weight = 75801
keywords = [ "roof", "3d" ]
aliases = [ "/questions/75801" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag roofs with different roof types on different ends?](/questions/75801/how-to-tag-roofs-with-different-roof-types-on-different-ends)

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
<span id="post-75801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75801-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Simple_3D_buildings">Simple 3D buildings</a> on the OSM wiki defines <a href="https://wiki.openstreetmap.org/wiki/Simple_3D_buildings#Roof_shape">several roof shapes</a>. However, they all seem to be mostly symmetric.</p>
<p>In the area where I was thinking of tagging roof shapes, it is a very common pattern to have the roof be "hipped" towards the end of the building that faces the street, and "gabled" in the back.</p>
<p><img src="https://wiki.openstreetmap.org/w/images/thumb/6/67/Roof2_4.jpg/160px-Roof2_4.jpg" alt="Hipped" /> <img src="https://wiki.openstreetmap.org/w/images/thumb/e/e8/Roof2_0.jpg/160px-Roof2_0.jpg" alt="Gabled" /></p>
<p><em>Hipped (left) and gabled (right) roof shapes.</em></p>
<p>What would be the correct way of tagging the roof shapes of such buildings?</p>
<hr />
<p><em>This question was migrated from <a href="https://gis.stackexchange.com/q/368165">gis.stackexchange.com/q/368165</a>.</em></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roof" rel="tag" title="see questions tagged &#39;roof&#39;">roof</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '20, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/30da9041adebce11705bb6cf8eff9b28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="attilaolah&#39;s gravatar image" />
<p><span>attilaolah</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="attilaolah has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-75801" class="comments-container">
&#10;</div>
<div id="comment-tools-75801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75801-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="75811"></span>

<div id="answer-container-75811" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75811-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="attilaolah has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At the time of writing, there is no established tagging in OSM that allows you to model this as a single roof shape. If you want to limit yourself to standard tags, you'd have to split this into multiple building parts with simpler roof shapes, e.g. a <code>gabled</code> roof plus one or more <code>skillion</code> roofs.</p>
<p>There are some proposals which would allow you to model this as a single roof. None of these have much software support at the time of writing:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/OSM-4D/Roof_table">OSM-4D</a> suggests <code>roof:shape=side_hipped</code>, which is actually quite common in the database as well (also note the definition for the roof's orientation, although the <code>roof:direction</code> key which has become more common after OSM-4D was written would probably be a better fit).</li>
<li>OSM-4D also suggests parameters for roof shapes, but it doesn't clearly state which keys should be used to tag these parameters. If it did, we could treat this as a hipped roof that has a ridge distance of 0 on one side.</li>
<li><a href="https://wiki.openstreetmap.org/wiki/ProposedRoofLines">ProposedRoofLines</a> lets you draw ways for the roof's ridge (<code>roof:ridge=yes</code>) and edge (<code>roof:edge=yes</code>). It also suggests linking these ways to the building with a relation, but the only implementation I know of (my own in OSM2World) does not require this.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '20, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</img>
</div>
</div>
<div id="comments-container-75811" class="comments-container">
&#10;</div>
<div id="comment-tools-75811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75811-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75806"></span>

<div id="answer-container-75806" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75806-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-75806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a far more extensive <a href="https://wiki.openstreetmap.org/wiki/OSM-4D/Roof_table">roof table</a> which lists this type as <a href="https://wiki.openstreetmap.org/wiki/OSM-4D/Roof_table#Roofs_with_2_faces"><code>side_hipped</code></a>. Be sure to note orientation.</p>
<p>There is also a proposed <a href="https://wiki.openstreetmap.org/wiki/ProposedRoofLines">roof lines relation</a> which looks very involved and probably isn't supported by any software yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '20, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-75806" class="comments-container">
<span id="75810"></span>
<div id="comment-75810" class="comment">
<div id="post-75810-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>OSM-4D is not an established standard and doesn't really have any better software support at the moment than roof lines (which are supported in OSM2World, but nowhere else as far as I know). Doesn't mean one can't use it, but it merits a disclaimer imo.</p>
</div>
<div id="comment-75810-info" class="comment-info">
<span class="comment-age">(20 Jul '20, 14:50)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-75806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75806-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75802"></span>

<div id="answer-container-75802" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75802-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In advanced settings you could could put roof_type = your examples or flat, or Solar have a look at what has been used before. <a href="https://taginfo.openstreetmap.org/">https://taginfo.openstreetmap.org/</a></p>
<p><a href="https://taginfo.openstreetmap.org/keys/roof_type">https://taginfo.openstreetmap.org/keys/roof_type</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '20, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '20, 12:56</strong> </span></p>
</div>
</div>
<div id="comments-container-75802" class="comments-container">
<span id="75805"></span>
<div id="comment-75805" class="comment">
<div id="post-75805-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Inventing an arbitrary roof type isn't of much use here.</p>
</div>
<div id="comment-75805-info" class="comment-info">
<span class="comment-age">(20 Jul '20, 13:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75802" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75802-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

