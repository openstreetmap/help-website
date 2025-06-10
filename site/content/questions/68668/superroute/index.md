+++
type = "question"
title = "Superroute"
description = '''Background I am creating a series local of logically connected hiking routes. Where one ends, another starts. These local routes go through cities and towns as well a country side. I use hiking.waymarkedtrails.org to view the results. I am conscious these routes can have a large number of elements. ...'''
date = "2019-04-05T21:28:00Z"
lastmod = "2022-05-11T16:19:00Z"
weight = 68668
keywords = [ "superroute", "super-relations", "relations" ]
aliases = [ "/questions/68668" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Superroute](/questions/68668/superroute)

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
<span id="post-68668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Background</strong> I am creating a series local of logically connected hiking routes. Where one ends, another starts. These local routes go through cities and towns as well a country side. I use hiking.waymarkedtrails.org to view the results. I am conscious these routes can have a large number of elements. I wish to keep each local route to between 1 and 3 days walking and so keep the number of elements at around 200 in each route.</p>
<p>I have found the practice of the European Long Distance path. Taking route E2 as an example. I note this passes through five countries (from near Stranraer, west Scotland, UK to Nice, south France) and has a nested set of super relations. Each super relation has as members the relations at the lower level. Thus E2 (1956169, type:Superroute) has 5 members. One of these members is "... - part UK" (1959505, type Superroute). This Superroute has 8 members, one of which is "... - part UK: Scotland" (4515206). And this Superroute has two members 50235 Portpatrick to Melrose and 360996 Melrose to Kirk Yetholm.</p>
<p>In my case there would one national Superroute with six members. In total there will be about 50 local routes (containing elements such as Path, Bridge etc). Where one local route finishes, another begins. These local routes will be allocated to the relevant regional Superroute.</p>
<p>I have read the one question I could find (dated 2013?) on type: Superroute and believe it doesn't address my question below.</p>
<p>My only tools are the standard OSM browser loaded in Chrome. I have considered downloading "JOSM", for example, but it looks too complicated for a simpleton like me to install on a desktop with Windows 10.</p>
<p><strong>My Question</strong></p>
<p>1) How do I create a relation of type Superroute to which I can then add members?</p>
<p>2) How do I add Members to a Superroute?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-superroute" rel="tag" title="see questions tagged &#39;superroute&#39;">superroute</span> <span class="post-tag tag-link-super-relations" rel="tag" title="see questions tagged &#39;super-relations&#39;">super-relations</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '19, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/74f0fedc2fe8cb83660a329f79f88791?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlwynWellington&#39;s gravatar image" />
<p><span>AlwynWellington</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlwynWellington has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Apr '19, 01:54</strong> </span></p>
</div>
</div>
<div id="comments-container-68668" class="comments-container">
&#10;</div>
<div id="comment-tools-68668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68668-form-container" class="comment-form-container">
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

<span id="68680"></span>

<div id="answer-container-68680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68680-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Based on the answer to <a href="https://help.openstreetmap.org/questions/58270/how-i-can-create-relation-in-id-editor">this question</a> I think you would need to</p>
<ol>
<li>select one of the route relations you would like to edit,</li>
<li>scroll to the bottom (after the enumeration of ways) and</li>
<li>click on the plus to create a new parent relation.</li>
</ol>
<p>After the first one I <em>think</em> the subsequent sub-relations should then have the option to choose the new relation as parent (instead of step 3). It doesn't appear to be a supported type for iD so I think it will probably involve rather a lot of manual tag entry.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '19, 00:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-68680" class="comments-container">
&#10;</div>
<div id="comment-tools-68680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68680-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84437"></span>

<div id="answer-container-84437" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84437-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Superroute is a normal relation with attribute: type=superroute. Superroute has 'route' members usually (instead of tracks and paths).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '22, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ef2a31b4564fe582ee8195026dad53c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Milan%20Kerslager&#39;s gravatar image" />
<p><span>Milan Kerslager</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Milan Kerslager has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84437" class="comments-container">
&#10;</div>
<div id="comment-tools-84437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84437-form-container" class="comment-form-container">
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

