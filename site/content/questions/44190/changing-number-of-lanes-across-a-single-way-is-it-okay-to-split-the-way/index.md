+++
type = "question"
title = "Changing number of lanes across a single way, is it okay to split the way?"
description = '''I am using OSM data to build a network for traffic simulation (using SUMO). I often notice errors in the data when it comes to the available number of lane, I have fixed one as an example Changeset 32608483. In the linked case, I am guessing it is okay to make the change but I have some other cases ...'''
date = "2015-07-15T06:38:00Z"
lastmod = "2015-07-15T23:43:00Z"
weight = 44190
keywords = [ "ways", "lanes" ]
aliases = [ "/questions/44190" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Changing number of lanes across a single way, is it okay to split the way?](/questions/44190/changing-number-of-lanes-across-a-single-way-is-it-okay-to-split-the-way)

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
<span id="post-44190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44190-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using OSM data to build a network for traffic simulation (using <a href="http://sumo.dlr.de/wiki/Main_Page">SUMO</a>). I often notice errors in the data when it comes to the available number of lane, I have fixed one as an example <a href="https://www.openstreetmap.org/changeset/32608483">Changeset 32608483</a>.</p>
<p>In the linked case, I am guessing it is okay to make the change but I have some other cases where a single way has its number of lanes change (some part of the way has 2 lanes, some part has 3, some other has 4 when the lane reaches an intersection). In this case, for the simulation purpose, I need to split this into three different ways, with the correct number of lane for each of them.</p>
<p>Is it okay to make this kind of split and commit them to the OSM database? In some cases, it can significantly increase the number of ways without improving the quality of the map render.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '15, 06:38</strong></p>
<img src="https://secure.gravatar.com/avatar/afb75334578f7ae076c30c918448d9a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BLUG_Julien&#39;s gravatar image" />
<p><span>BLUG_Julien</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BLUG_Julien has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '15, 11:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-44190" class="comments-container">
<span id="44196"></span>
<div id="comment-44196" class="comment">
<div id="post-44196-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi, and welcome to help.openstreetmap.org. You mention "sumo" - I added a link. Is that the right link (SUMO by DLR)?</p>
</div>
<div id="comment-44196-info" class="comment-info">
<span class="comment-age">(15 Jul '15, 11:23)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="44207"></span>
<div id="comment-44207" class="comment">
<div id="post-44207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is, thanks for adding the link.</p>
</div>
<div id="comment-44207-info" class="comment-info">
<span class="comment-age">(15 Jul '15, 16:47)</span> <span class="comment-user userinfo">BLUG_Julien</span>
</div>
</div>
</div>
<div id="comment-tools-44190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44190-form-container" class="comment-form-container">
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

<span id="44195"></span>

<div id="answer-container-44195" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44195-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-44195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BLUG_Julien has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, splitting the way is the right solution. It is established practice that ways are split whenever an attribute changes - different name, different width, or just different speed limit.</p>
<blockquote>
<p>in some cases, it can significantly increase the number of ways without improving the quality of the map render.</p>
</blockquote>
<p>This is not relevant - <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a> is generally not a good idea (plus in this case it does not even cause problems for the renderer, because renderers know that split ways should usually be combined for rendering). If the number of lanes change, split the way.</p>
<p>Note: While splitting, take care not to remove any data:</p>
<ul>
<li>copy over all tags that apply to both of the new ways</li>
<li>make sure membership in relations is preserved</li>
</ul>
<p>Most editors should help you with this, but it cannot hurt to check.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '15, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '15, 11:26</strong> </span></p>
</div>
</div>
<div id="comments-container-44195" class="comments-container">
<span id="44208"></span>
<div id="comment-44208" class="comment">
<div id="post-44208-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this is telling me what the next steps are for me, one thing I forgot to ask is if there is any way in the OSM database to tell which lane of a way connect to which lanes of the previous and following ways. By connect, I mean either through a merge or a split, not by typical lane change. Should I maybe ask this as a separate question?</p>
</div>
<div id="comment-44208-info" class="comment-info">
<span class="comment-age">(15 Jul '15, 16:49)</span> <span class="comment-user userinfo">BLUG_Julien</span>
</div>
</div>
<span id="44212"></span>
<div id="comment-44212" class="comment">
<div id="post-44212-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Take a look at the turn lane tagging. As an example if the right lane disappears and there are merge arrows on the pavement then the section where the arrows are can be tagged with "turn:lanes=none|slight_left"</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Key:turn:lanes">https://wiki.openstreetmap.org/wiki/Key:turn:lanes</a></p>
<p>For what it is worth some OSM based routers use this type of tagging to help provide lane guidance.</p>
</div>
<div id="comment-44212-info" class="comment-info">
<span class="comment-age">(15 Jul '15, 23:43)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-44195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44209"></span>

<div id="answer-container-44209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44209-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Is it okay to make this kind of split and commit them to the OSM database?</p>
</blockquote>
<p>Yep. Nothing wrong with that. That's what you're supposed to do. Ways are often split in OSM when an attribute changes.</p>
<blockquote>
<p>In some cases, it can significantly increase the number of ways without improving the quality of the map render.</p>
</blockquote>
<p>Nothing wrong with increasing the number of ways in the database. The world is big. It'll take a lot of time &amp; data to map it all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '15, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-44209" class="comments-container">
&#10;</div>
<div id="comment-tools-44209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44209-form-container" class="comment-form-container">
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

