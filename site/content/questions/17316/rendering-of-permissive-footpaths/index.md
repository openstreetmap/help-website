+++
type = "question"
title = "Rendering of permissive footpaths"
description = '''I have recently stumbled upon a permissive footpath marked as:  designation = permissive_footpath foot = permissive highway = path  Since there is no access tag, it is rendered exactly like a public footpath. What is the right way to tag it so that it gets rendered as permissive access (green dotted...'''
date = "2012-10-31T09:45:00Z"
lastmod = "2012-12-16T22:43:00Z"
weight = 17316
keywords = [ "access", "footpath", "permissive" ]
aliases = [ "/questions/17316" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Rendering of permissive footpaths](/questions/17316/rendering-of-permissive-footpaths)

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
<span id="post-17316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17316-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have recently stumbled upon a <a href="http://www.openstreetmap.org/browse/way/3343696">permissive footpath</a> marked as:</p>
<ul>
<li>designation = permissive_footpath</li>
<li>foot = permissive</li>
<li>highway = path</li>
</ul>
<p>Since there is no access tag, it is rendered exactly like a public footpath. What is the right way to tag it so that it gets rendered as permissive access (green dotted lines)?</p>
<p>If I add access = permissive, won't it imply that access is permissive for all forms of transport?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span> <span class="post-tag tag-link-permissive" rel="tag" title="see questions tagged &#39;permissive&#39;">permissive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '12, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/08b67dfcf2bf107f25bbbd43c9bc987a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="priteau&#39;s gravatar image" />
<p><span>priteau</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="priteau has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17316" class="comments-container">
&#10;</div>
<div id="comment-tools-17316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17316-form-container" class="comment-form-container">
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

<span id="17331"></span>

<div id="answer-container-17331" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17331-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="priteau has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Usually we don't <a href="http://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tag for the renderer</a>.</p>
<p>It is true that the currently used stylesheet for <a href="http://wiki.openstreetmap.org/wiki/Mapnik">mapnik</a> (the renderer for our main slippy map) only recognizes <em>access=</em> and ignores the more specific access tags (with a few exceptions). You could create a <a href="https://trac.openstreetmap.org/report">feature request</a> but keep in mind that the main map cannot display every possible <a href="http://wiki.openstreetmap.org/wiki/Map_Features">map feature</a>. <a href="http://wiki.openstreetmap.org/wiki/Tag:highway%3Dpath">highway=path</a> for example allows <em>foot</em>, <em>bicycle</em> and <em>horse</em> according to the <a href="http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">default access restrictions</a>. Consequently you cannot render <em>foot=permissive</em> the same way as <em>access=permissive</em> because they don't have the same meaning and the access permissions for foot and horse would get ignored.</p>
<p>There are also several other map features like <a href="http://wiki.openstreetmap.org/wiki/Key:barrier">barriers</a> which can prevent you from using a specific way, not all of them are rendered. If you want to know whether you are allowed to use a way or a route then consult an up-to-date <a href="http://wiki.openstreetmap.org/wiki/Routing/OnlineRouters">routing engine</a> instead. The rendered map just gives you an overview but hides lots of detailed information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '12, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17331" class="comments-container">
&#10;</div>
<div id="comment-tools-17331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17331-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17318"></span>

<div id="answer-container-17318" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17318-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-17318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Path implies bicycle=yes, so the current tagging is not correct.</p>
<p>I would go for</p>
<ul>
<li>access=permissive</li>
<li>horse=no</li>
<li>vehicle=no</li>
</ul>
<p>This should be enough</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '12, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-17318" class="comments-container">
<span id="17320"></span>
<div id="comment-17320" class="comment">
<div id="post-17320-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>why not: highway=footway, access=permissive?</p>
</div>
<div id="comment-17320-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 10:56)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="17321"></span>
<div id="comment-17321" class="comment">
<div id="post-17321-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Apparently this is a matter of style: <a href="http://wiki.openstreetmap.org/wiki/UK_public_rights_of_way#Classic_vs_Alternative_tagging_schemes">http://wiki.openstreetmap.org/wiki/UK_public_rights_of_way#Classic_vs_Alternative_tagging_schemes</a></p>
</div>
<div id="comment-17321-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 13:03)</span> <span class="comment-user userinfo">priteau</span>
</div>
</div>
<span id="17328"></span>
<div id="comment-17328" class="comment">
<div id="post-17328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>highway=footway is equivalent to highway=path with horse=no and bicycle=no according to the <a href="http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">default access restrictions</a>.</p>
</div>
<div id="comment-17328-info" class="comment-info">
<span class="comment-age">(31 Oct '12, 15:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="18501"></span>
<div id="comment-18501" class="comment">
<div id="post-18501-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Highway=footway + access=permissive would imply (amongst others) hgv=permissive, so I'm not in favour of that.</p>
<p>My access rules can be used with every highway type and will be unambiguously correct.</p>
<p>I do not say which highway type is to be used, that's up to the mapper, but with this combination of access tags, nothing can go wrong.</p>
<p>Foot=permissive could indeed also be used, instead of access=permissive. But you don't tag for the renderer whichever you chose. Both are 100% correct.</p>
</div>
<div id="comment-18501-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 22:43)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-17318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17318-form-container" class="comment-form-container">
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

