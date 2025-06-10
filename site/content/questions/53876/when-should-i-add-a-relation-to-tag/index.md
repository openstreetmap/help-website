+++
type = "question"
title = "When should I add a relation to tag?"
description = '''When adding tags that apply to the whole object (mostly wikipedia/data, but there are others), should I create a relation and add the tag to the relation, or should I add the tag to every way that&#x27;s part of the object. For example the White Cliffs of Dover has several ways. Some have a different set...'''
date = "2017-01-05T17:11:00Z"
lastmod = "2017-01-06T08:02:00Z"
weight = 53876
keywords = [ "split", "relations" ]
aliases = [ "/questions/53876" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [When should I add a relation to tag?](/questions/53876/when-should-i-add-a-relation-to-tag)

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
<span id="post-53876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53876-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When adding tags that apply to the whole object (mostly wikipedia/data, but there are others), should I create a relation and add the tag to the relation, or should I add the tag to every way that's part of the object.</p>
<p>For example the <a href="http://www.openstreetmap.org/way/114618483">White Cliffs of Dover</a> has several ways. Some have a different set of tags than others, though. Some have different (specific) names, though they're all <a href="https://commons.wikimedia.org/wiki/File:White_Cliffs_of_Dover_map.png">part</a> of the Cliffs of Dover. Should we have a relation with name=White Cliffs of Dover, wikidata=Q754785, operator=National Trust, etc?</p>
<p>What about streets? I see there's <a href="http://wiki.openstreetmap.org/wiki/Relation:street">relation:street</a> so I think I'll go ahead and use that.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '17, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/5833f68b9cfce6017187678c495b6fc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdejean&#39;s gravatar image" />
<p><span>mdejean</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdejean has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53876" class="comments-container">
&#10;</div>
<div id="comment-tools-53876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53876-form-container" class="comment-form-container">
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

<span id="53881"></span>

<div id="answer-container-53881" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53881-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mdejean has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Relation tags do not cascade down to their member elements. If you create three ways and you don't name them, but instead put them in a relation which does have a name tag, virtually nothing (renderer, router, analysis tool, whatever) will understand what you mean.</p>
<p>As the <code>relation:street</code> page says: "Note that this relation is not established and unsupported by some applications." Translation: it's been made up by someone to whose sense of data consistency it appeals, but no-one else uses it.</p>
<p>Relations are used for a few distinct purposes, such as route relations (buses, bike routes, etc.), multipolygons, and so on. For everything else, there is nothing wrong with having two adjacent objects which have the same tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '17, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '17, 20:07</strong> </span></p>
</div>
</div>
<div id="comments-container-53881" class="comments-container">
<span id="53885"></span>
<div id="comment-53885" class="comment">
<div id="post-53885-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So the cliffs in the White Cliffs of Dover should each have name=White Cliffs of Dover, alt_name=Shakespeare Cliffs, Langdon Cliffs, etc., wikidata=Q754785?</p>
<p>Is there a way to select all of the ways with the same name to add a tag?</p>
</div>
<div id="comment-53885-info" class="comment-info">
<span class="comment-age">(05 Jan '17, 20:36)</span> <span class="comment-user userinfo">mdejean</span>
</div>
</div>
<span id="53889"></span>
<div id="comment-53889" class="comment">
<div id="post-53889-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is no way to select multiple objects in the iD editor, you can do so in JOSM</p>
</div>
<div id="comment-53889-info" class="comment-info">
<span class="comment-age">(06 Jan '17, 08:02)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-53881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53881-form-container" class="comment-form-container">
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

