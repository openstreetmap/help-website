+++
type = "question"
title = "How to obtain all members of a relation that lack a specific key?"
description = '''I would like to extract, with Overpass Turbo, all members of a specific route relation that do not have a specific key (in my case, all ways that lack a surface tag).'''
date = "2015-09-29T16:08:00Z"
lastmod = "2015-09-29T21:19:00Z"
weight = 45654
keywords = [ "overpass-turbo", "relation", "key" ]
aliases = [ "/questions/45654" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to obtain all members of a relation that lack a specific key?](/questions/45654/how-to-obtain-all-members-of-a-relation-that-lack-a-specific-key)

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
<span id="post-45654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45654-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to extract, with Overpass Turbo, all members of a specific route relation that do not have a specific key (in my case, all ways that lack a surface tag).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '15, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0a45ba8bcc4b69a12b3e817afff187e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voschix&#39;s gravatar image" />
<p><span>voschix</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voschix has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '15, 20:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45654" class="comments-container">
&#10;</div>
<div id="comment-tools-45654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45654-form-container" class="comment-form-container">
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

<span id="45656"></span>

<div id="answer-container-45656" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45656-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-45656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="voschix has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We had the exact same question in the German forum thread <a href="http://forum.openstreetmap.org/viewtopic.php?pid=523277#p523277">"OverpassTurbo for Dummies"</a> .</p>
<p>Here's how query should look like. Please adjust the relation id selection as needed.</p>
<pre><code>relation(398874);way(r)[surface!~&quot;.&quot;];out;&gt;;out skel;</code></pre>
<p>Try it in Overpass Turbo: <a href="http://overpass-turbo.eu/s/bJg">http://overpass-turbo.eu/s/bJg</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '15, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '15, 17:31</strong> </span></p>
</div>
</div>
<div id="comments-container-45656" class="comments-container">
<span id="45660"></span>
<div id="comment-45660" class="comment">
<div id="post-45660-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>that's great - I often thought about the same! … And how to get a refinement of this? e.g. only tracks when searching for existence of tracktype? ;-) I tried <code>relation(398874);way(r)["highway"="track"][tracktype!~"."];out;&gt;;out skel;</code> but that runs much much longer (until I cancel).</p>
</div>
<div id="comment-45660-info" class="comment-info">
<span class="comment-age">(29 Sep '15, 20:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="45662"></span>
<div id="comment-45662" class="comment">
<div id="post-45662-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>That's also possible with QL, but the query needs to be rewritten a bit due to a very expensive evaluation sequence:</p>
<p><code>relation(398874);way(r);way._["highway"="track"][tracktype!~"."];out;&gt;;out skel;</code></p>
</div>
<div id="comment-45662-info" class="comment-info">
<span class="comment-age">(29 Sep '15, 20:47)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="45663"></span>
<div id="comment-45663" class="comment">
<div id="post-45663-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>great, thanks! I think this kind of refinement is often useful for those queries. I need to learn this language! :-)</p>
</div>
<div id="comment-45663-info" class="comment-info">
<span class="comment-age">(29 Sep '15, 21:19)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45656-form-container" class="comment-form-container">
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

