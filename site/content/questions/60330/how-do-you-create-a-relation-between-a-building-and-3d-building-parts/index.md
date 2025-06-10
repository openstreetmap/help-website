+++
type = "question"
title = "How do you create a relation between a building and 3D building parts?"
description = '''I assume it&#x27;s unnecessary, but just out of curiosity, the building part here has a relation linked to the building. How do you create that? Are there any pros/cons in doing it?  http://www.openstreetmap.org/edit?relation=3824021#map=22/52.51651/13.45273'''
date = "2017-10-27T18:53:00Z"
lastmod = "2017-10-29T14:57:00Z"
weight = 60330
keywords = [ "building", "relation", "3d" ]
aliases = [ "/questions/60330" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you create a relation between a building and 3D building parts?](/questions/60330/how-do-you-create-a-relation-between-a-building-and-3d-building-parts)

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
<span id="post-60330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60330-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I assume it's unnecessary, but just out of curiosity, the building part here has a relation linked to the building. How do you create that? Are there any pros/cons in doing it?</p>
<p><a href="http://www.openstreetmap.org/edit?relation=3824021#map=22/52.51651/13.45273">http://www.openstreetmap.org/edit?relation=3824021#map=22/52.51651/13.45273</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '17, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/97e2f141b910d9a08dabfc0865382491?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chachafish&#39;s gravatar image" />
<p><span>chachafish</span><br />
<span class="score" title="411 reputation points">411</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chachafish has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-60330" class="comments-container">
&#10;</div>
<div id="comment-tools-60330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60330-form-container" class="comment-form-container">
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

<span id="60332"></span>

<div id="answer-container-60332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60332-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-60332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most 3D buildings in the database do not use building relations. In the absence of relations, building parts simply belong to the building that geometrically contains them. Situations where that simple rule doesn't work are very rare, but they do exist: When multiple building outlines overlap, relations are needed to avoid ambiguity.</p>
<p>Except in those rare cases, building relations are redundant and provide no additional information. Adding them would not only be a waste of time, it would also further raise the barrier of entry for new mappers (who often consider relation editing challenging and counter-intuitive). As such, adding them unnecessarily is generally not a good idea.</p>
<p>To create a building relation in JOSM, follow the following steps:</p>
<ul>
<li>Select all the building parts and building outlines (use shift+click or draw a selection box).</li>
<li>Create a new relation by using the "create new relation" button.</li>
<li>The <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/RelationEditor">relation editor</a> will open. Add all the selected elements to the relation.</li>
<li>Add the role <code>part</code> to all parts, and the role <code>outline</code> to the outline.</li>
<li>Add the tag <code>type=building</code> to the relation itself.</li>
<li>Close the relation editor by pressing "OK".</li>
</ul>
<p>You can also create a buildling relation in iD as follows:</p>
<ul>
<li>Select the building outline.</li>
<li>In the "all relations" section on the bottom left, click the "+" button and select "New relation".</li>
<li>There's no preset for building relation, so select the plain "Relation".</li>
<li>In the "type" field, enter <code>building</code>.</li>
<li>In the "all members" section below that, add the role <code>outline</code> for your building outline.</li>
<li>Now perform the following steps for each building part:</li>
<li>Select the building part</li>
<li>In the "all relations" section on the bottom left, click the "+" button and select your recently created building relation from the drop-down list.</li>
<li>Add <code>part</code> in the role field that appears.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '17, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '17, 20:07</strong> </span></p>
</div>
</div>
<div id="comments-container-60332" class="comments-container">
<span id="60335"></span>
<div id="comment-60335" class="comment">
<div id="post-60335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Cheers, buddy</p>
</div>
<div id="comment-60335-info" class="comment-info">
<span class="comment-age">(28 Oct '17, 02:54)</span> <span class="comment-user userinfo">chachafish</span>
</div>
</div>
</div>
<div id="comment-tools-60332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60332-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60336"></span>

<div id="answer-container-60336" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60336-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>"Except in those rare cases, building relations are redundant and provide no additional information. Adding them would not only be a waste of time, it would also further raise the barrier of entry for new mappers (who often consider relation editing challenging and counter-intuitive). As such, adding them unnecessarily is generally not a good idea."</em></p>
<p>Tordanik, while I appreciate the fact that relation processing is difficult, relations by itself are not "bad". To continuously stress that building relations should be avoided, is in my opinion unnecessary and counter productive. If you want to ignore them in processing, you always can, but they do also have clear merits in relation to (web)navigation of parts, and as such I object to your statement that they "provide no additional information". I have seen many complex 3D buildings that were almost incomprehensible and impossible to navigate on the main OSM website without a type=building relation to group the parts in a logical way. The simple answer as to which parts belong to the building, is often most easily answered on the main OSM website through a building relation. If setup carefully, you can than easily drill down different parts or even levels through weblinks, greatly easing insight into the structure in a plain 2D view.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '17, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-60336" class="comments-container">
<span id="60343"></span>
<div id="comment-60343" class="comment">
<div id="post-60343-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I say that building relations don't add information, I'm talking about the data, not about what shows up on any particular map. The information is already there without the relation, it's just not easily visible on osm.org.</p>
<p>However, the osm.org website has never intentionally added the ability to render or browse 3D buildings. So any ability to inspect 3D buildings on osm.org is pretty much accidental at this point. It's still an advantage to be able to do so, but I feel that it's not an important enough benefit on its own to justify using building relations. Instead of altering the data to achieve this result, I'd much rather see the software improved.</p>
<p>And just to avoid a possible misunderstanding: Processing building relations isn't particularly hard, and as building relations cannot always be avoided (most of the time, yes, but not always), that ability is necessary for a feature-complete 3D renderer anyway. So my concern isn't processing the data, it's editing it.</p>
</div>
<div id="comment-60343-info" class="comment-info">
<span class="comment-age">(29 Oct '17, 14:57)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-60336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60336-form-container" class="comment-form-container">
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

