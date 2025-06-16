+++
type = "question"
title = "changesets with huge objects modified"
description = '''Is there a way to detect/know changesets with more than 500 to 1000 objects modified in and around a region? Like for example, changesets like these https://www.openstreetmap.org/changeset/34317657 where more than 3k objects are modified. '''
date = "2015-10-28T05:38:00Z"
lastmod = "2015-10-30T22:39:00Z"
weight = 46157
keywords = [ "changesets" ]
aliases = [ "/questions/46157" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [changesets with huge objects modified](/questions/46157/changesets-with-huge-objects-modified)

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
<span id="post-46157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46157-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to detect/know changesets with more than 500 to 1000 objects modified in and around a region? Like for example, changesets like these <a href="https://www.openstreetmap.org/changeset/34317657">https://www.openstreetmap.org/changeset/34317657</a> where more than 3k objects are modified.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '15, 05:38</strong></p>
<img src="https://secure.gravatar.com/avatar/3f717814f68a3cda575f27d0798aa2a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogi_ks&#39;s gravatar image" />
<p><span>yogi_ks</span><br />
<span class="score" title="246 reputation points">246</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogi_ks has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46157" class="comments-container">
<span id="46245"></span>
<div id="comment-46245" class="comment">
<div id="post-46245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you give a few more details about why you're concerned about large changesets?</p>
</div>
<div id="comment-46245-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 15:37)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
<span id="46247"></span>
<div id="comment-46247" class="comment">
<div id="post-46247-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That particular example contained a "slip of the mouse" with someone selecting all elements and assigning a tag/value to them Similar issues might be an attempt to change tags on ways and inadvertantly adding the same tags to nodes as well, and selecting all nodes and moving them slightly (I've done that one). There have been examples of each of these apart from the last one fairly recently, and it'd be nice to be able to detect the "unbalanced" (or just large) changesets that result from "faux pas" such as the above.</p>
</div>
<div id="comment-46247-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 17:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46253"></span>
<div id="comment-46253" class="comment">
<div id="post-46253-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5070/lightsider">@Lightsider</a>, I'm only concerned when the large changesets are done by mistake and adding to <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>'s comment, it'd be nice to detect these kind of changesets.</p>
</div>
<div id="comment-46253-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 22:39)</span> <span class="comment-user userinfo">yogi_ks</span>
</div>
</div>
</div>
<div id="comment-tools-46157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46157-form-container" class="comment-form-container">
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

<span id="46241"></span>

<div id="answer-container-46241" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46241-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-46241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is not a super simple way to do it currently.</p>
<p>You might want to look at <a href="https://github.com/MichaelVL/osm-analytic-tracker">https://github.com/MichaelVL/osm-analytic-tracker</a> <a href="http://osm.expandable.dk/osm/index.html">http://osm.expandable.dk/osm/index.html</a> for a recent effort. You would need to add special highlighting or a filter for larger changesets (note 500-1000 objects is resonably common and as such not directly a cause for alarm).</p>
<p>You can find more tools here <a href="https://wiki.openstreetmap.org/wiki/Quality_assurance#Monitoring_Tools">https://wiki.openstreetmap.org/wiki/Quality_assurance#Monitoring_Tools</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '15, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '15, 09:52</strong> </span></p>
</div>
</div>
<div id="comments-container-46241" class="comments-container">
<span id="46251"></span>
<div id="comment-46251" class="comment">
<div id="post-46251-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See also some tools/libs at <a href="https://wiki.openstreetmap.org/wiki/Detect_Vandalism">https://wiki.openstreetmap.org/wiki/Detect_Vandalism</a></p>
</div>
<div id="comment-46251-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 21:50)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
</div>
<div id="comment-tools-46241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46241-form-container" class="comment-form-container">
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

