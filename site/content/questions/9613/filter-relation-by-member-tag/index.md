+++
type = "question"
title = "Filter relation by member tag"
description = '''How do I filter a given relation to only keep its members that have specific tag? For instance I have a bad relation of a river that contains both river itself and also riverbank... I want to get rid of the riverbank - that means to keep members that have waterway=river and drop members that have wa...'''
date = "2011-12-25T23:48:00Z"
lastmod = "2011-12-28T11:30:00Z"
weight = 9613
keywords = [ "josm", "filtering", "tag", "relations" ]
aliases = [ "/questions/9613" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filter relation by member tag](/questions/9613/filter-relation-by-member-tag)

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
<span id="post-9613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I filter a given relation to only keep its members that have specific tag? For instance I have a bad relation of a river that contains both river itself and also riverbank... I want to get rid of the riverbank - that means to keep members that have waterway=river and drop members that have waterway=riverbank tags.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Dec '11, 23:48</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Dec '11, 16:37</strong> </span></p>
</div>
</div>
<div id="comments-container-9613" class="comments-container">
&#10;</div>
<div id="comment-tools-9613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9613-form-container" class="comment-form-container">
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

<span id="9615"></span>

<div id="answer-container-9615" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9615-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kozuch has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming you know the relation id:</p>
<p>a) load JOSM</p>
<p>b) File, Download Object - select relation and enter the id. Don't forget to also download relation members</p>
<p>c) Use Edit, Search (or Ctrl-F) and enter <code>child(type:relation id:&lt;id&gt;) waterway=river</code> but replace &lt;id&gt; with the id of the relation</p>
<p>This selects the children (the way members) of the relation with the id &lt;id&gt; but only where they have the tag <code>waterway=river</code>. You might instead want to search for the relation members that have waterway=riverbank tagged, so you can then remove them from the relation in one go. If so just replace waterway=river with waterway=riverbank and once they are selected you should be able to remove them from the relation by selecting the relation entry in the properties panel and clicking the dustbin icon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '11, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-9615" class="comments-container">
<span id="9624"></span>
<div id="comment-9624" class="comment">
<div id="post-9624-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem is the relation is too large and JOSM returns "Internal server error" (so does web front end). Is there a way to import the relation to JOSM in .osm XML format? I have the .osm file for that relation...</p>
<p>Edit #1: Well I just tried to load that file into JOSM but I can not see any data imported (nothing showing in map screen). Does JOSM need nodes to be contained within the .osm file? My file only contains members of the relation (=IDs of ways).</p>
<p>Edit #2: I see the relation loaded but was "incomplete", so nothing showed. So I just downloaded the members and now its OK.</p>
</div>
<div id="comment-9624-info" class="comment-info">
<span class="comment-age">(26 Dec '11, 21:56)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="9655"></span>
<div id="comment-9655" class="comment">
<div id="post-9655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've had that with a few relations recently, and used the download incomplete option you have already found (this seems slower, but more reliable).</p>
</div>
<div id="comment-9655-info" class="comment-info">
<span class="comment-age">(28 Dec '11, 11:30)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-9615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9615-form-container" class="comment-form-container">
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

