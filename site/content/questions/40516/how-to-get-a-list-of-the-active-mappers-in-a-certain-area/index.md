+++
type = "question"
title = "How to get a list of the active mappers in a certain area?"
description = '''What is the best way to get a list of active mappers of a certain area. For instance I am interested to get the active mappers in San Francisco.  On possible way to do this, is to get the metro extract of San Francisco and load it into a database and query the users. But this way I only get the user...'''
date = "2015-01-22T08:24:00Z"
lastmod = "2015-01-22T11:14:00Z"
weight = 40516
keywords = [ "active", "area", "database", "user", "users" ]
aliases = [ "/questions/40516" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to get a list of the active mappers in a certain area?](/questions/40516/how-to-get-a-list-of-the-active-mappers-in-a-certain-area)

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
<span id="post-40516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40516-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best way to get a list of active mappers of a certain area. For instance I am interested to get the active mappers in San Francisco.</p>
<p>On possible way to do this, is to get the metro extract of San Francisco and load it into a database and query the users. But this way I only get the users that last touched the data. Is there a better way to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-active" rel="tag" title="see questions tagged &#39;active&#39;">active</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span> <span class="post-tag tag-link-users" rel="tag" title="see questions tagged &#39;users&#39;">users</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '15, 08:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e0304055ba107b43dc134e4a9e5a955c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wasus&#39;s gravatar image" />
<p><span>Wasus</span><br />
<span class="score" title="346 reputation points">346</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wasus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '15, 12:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-40516" class="comments-container">
&#10;</div>
<div id="comment-tools-40516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40516-form-container" class="comment-form-container">
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

<span id="40517"></span>

<div id="answer-container-40517" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40517-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Wasus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The non-programming way to do this is to use <a href="http://resultmaps.neis-one.org/oooc">http://resultmaps.neis-one.org/oooc</a></p>
<p>The alternative is to take the centers of changesets (probably only suitably small ones) and to select thoes users that edit often enough in SF. The changeset dump can be obtained from planet.openstreetmap.org</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '15, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-40517" class="comments-container">
<span id="40519"></span>
<div id="comment-40519" class="comment">
<div id="post-40519-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Also, history data is available so you could download the "history planet", exctract things in the SF area with osm-history-splitter, and count user names in that. Gives you a more accurate picture than simply going by changeset centres but is much more complicated.</p>
</div>
<div id="comment-40519-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 09:12)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="40521"></span>
<div id="comment-40521" class="comment">
<div id="post-40521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Cool thanks for the info. The website by @neis-one also kind of serves like an API. For instance <a href="http://resultmaps.neis-one.org/ooocs.php?ntype=activity6m&amp;bbox=-99.478917780764,19.278457412663,-98.685842219232,19.552391297125">http://resultmaps.neis-one.org/ooocs.php?ntype=activity6m&amp;bbox=-99.478917780764,19.278457412663,-98.685842219232,19.552391297125</a> gives you a GeoJSON based on your bbox.</p>
</div>
<div id="comment-40521-info" class="comment-info">
<span class="comment-age">(22 Jan '15, 09:26)</span> <span class="comment-user userinfo">Wasus</span>
</div>
</div>
</div>
<div id="comment-tools-40517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40517-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40525"></span>

<div id="answer-container-40525" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40525-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See the suggestions at <a href="/questions/23245/">how-do-i-find-out-who-is-also-contributing-to-osm-and-communicate-with-them</a>, although creating a real "list" is still your task (if you mean "list" strictly).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '15, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-40525" class="comments-container">
&#10;</div>
<div id="comment-tools-40525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40525-form-container" class="comment-form-container">
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

