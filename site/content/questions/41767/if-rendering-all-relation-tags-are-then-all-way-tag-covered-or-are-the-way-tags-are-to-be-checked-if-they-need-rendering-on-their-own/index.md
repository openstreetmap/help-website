+++
type = "question"
title = "If rendering all relation-tags, are then all way-tag covered, or are the way-tags are to be checked if they need rendering on their own?"
description = '''Hi! If I render all relations (&amp;lt;relation ...&amp;gt;) that I find in an osm data file, are then all way (&amp;lt;way ...&amp;gt;) covered with that, or do I have to check the ways, if there are ways that haven&#x27;t been rendered so far? I have osm-data from two sources: the openstreetmap-export function, and fr...'''
date = "2015-03-17T16:14:00Z"
lastmod = "2015-03-18T14:40:00Z"
weight = 41767
keywords = [ "ways", "rendering", "orphan-nodes", "relations" ]
aliases = [ "/questions/41767" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [If rendering all relation-tags, are then all way-tag covered, or are the way-tags are to be checked if they need rendering on their own?](/questions/41767/if-rendering-all-relation-tags-are-then-all-way-tag-covered-or-are-the-way-tags-are-to-be-checked-if-they-need-rendering-on-their-own)

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
<span id="post-41767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41767-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>If I render all relations (<code>&lt;relation ...&gt;</code>) that I find in an osm data file, are then all way (<code>&lt;way ...&gt;</code>) covered with that, or do I have to check the ways, if there are ways that haven't been rendered so far?</p>
<p>I have osm-data from two sources: the openstreetmap-export function, and from geofabrik.de</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-orphan-nodes" rel="tag" title="see questions tagged &#39;orphan-nodes&#39;">orphan-nodes</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '15, 16:14</strong></p>
<img src="https://secure.gravatar.com/avatar/bd22ae7be4920107ca423b9cc035185d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John215&#39;s gravatar image" />
<p><span>John215</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John215 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>17 Mar '15, 16:19</strong> </span></p>
</div>
</div>
<div id="comments-container-41767" class="comments-container">
&#10;</div>
<div id="comment-tools-41767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41767-form-container" class="comment-form-container">
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

<span id="41781"></span>

<div id="answer-container-41781" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41781-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Relations are not more than lists of other objects. You can't actually "render" relations in any sensible way, what you -can- do is render the objects that are in the "list". Which in the case of ways means actually taking one more indirection step: ways are simply ordered lists of nodes + the way specific tags.</p>
<p>So tl;dr version: you actually have to render all the ways that the relation refers to.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '15, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Mar '15, 13:45</strong> </span></p>
</div>
</div>
<div id="comments-container-41781" class="comments-container">
<span id="41782"></span>
<div id="comment-41782" class="comment">
<div id="post-41782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>...and all the ways that no relation refers to :)</p>
</div>
<div id="comment-41782-info" class="comment-info">
<span class="comment-age">(18 Mar '15, 14:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="41783"></span>
<div id="comment-41783" class="comment">
<div id="post-41783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes the title is actually somewhat at oddes with the content of the question, as the relationship between tags on relations and tags on the consituent objects is complicated and depends on the relation type in question.</p>
<p>I don't think that John215 was actually assuming that all ways are a relation member .....</p>
</div>
<div id="comment-41783-info" class="comment-info">
<span class="comment-age">(18 Mar '15, 14:40)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41781-form-container" class="comment-form-container">
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

