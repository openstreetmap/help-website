+++
type = "question"
title = "RE-Why my last edits are not displayed ?"
description = '''My last edits are visible in the OSM online editors ID and Polach, but doesn&#x27;t appear in the OSM view mode.  EDIT1 : It doesn&#x27;t seems to be...  On my userpage 1, I noticed my last edits (16758129, 16757928) were marked &quot;(en cours de modification)&quot; (French for &quot;currently under modification&quot;) while ot...'''
date = "2013-06-29T22:57:00Z"
lastmod = "2013-07-02T21:17:00Z"
weight = 23836
keywords = [ "review", "lag", "view" ]
aliases = [ "/questions/23836" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RE-Why my last edits are not displayed ?](/questions/23836/re-why-my-last-edits-are-not-displayed)

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
<span id="post-23836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23836-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My last edits are <a href="http://www.openstreetmap.org/edit?lat=44.466418&amp;lon=0.106374&amp;zoom=18">visible in the OSM online editors ID and Polach</a>, but doesn't appear in the OSM view mode.</p>
<hr />
<p><strong>EDIT1 : It doesn't seems to be...</strong></p>
<ol>
<li>On my userpage <a href="http://openstreetmap.org/user/Wikipedia/edits">1</a>, I noticed my last edits (16758129, 16757928) were marked <em>"(en cours de modification)"</em> (French for <strong>"currently under modification")</strong> while others have a date such <em>"samedi 29 juin 2013 20:23"</em>. But when one of them turned to a date, nothing associated appeared on th view mode.</li>
<li>I then suspected a <strong>tile bug</strong> since one of the houses I added have just one angle displayed<a href="http://www.openstreetmap.org/?lat=44.4626&amp;lon=0.093386&amp;zoom=23">2</a> This house is located on 2 tiles jointure, So it seems the right side tiles are not up to date. But actually, there are still a hand of houses disapearing from the view mode without reasons. (They are all building &gt; family houses )</li>
</ol>
<p>Any solution ?</p>
<hr />
<p><strong>EDIT 2:</strong> <strong>There are both a tile cache AND a zoom issue.</strong> Some tiles are not up to date. And some buildings &gt; houses of similar sizes, for unknow reasons, doesn't show up at a given zoom.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-review" rel="tag" title="see questions tagged &#39;review&#39;">review</span> <span class="post-tag tag-link-lag" rel="tag" title="see questions tagged &#39;lag&#39;">lag</span> <span class="post-tag tag-link-view" rel="tag" title="see questions tagged &#39;view&#39;">view</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '13, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/8ee4f9c6ccd42782d66f7fb11a7d29e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wikipedia&#39;s gravatar image" />
<p><span>wikipedia</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wikipedia has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '13, 10:25</strong> </span></p>
</div>
</div>
<div id="comments-container-23836" class="comments-container">
&#10;</div>
<div id="comment-tools-23836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23836-form-container" class="comment-form-container">
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

<span id="23841"></span>

<div id="answer-container-23841" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23841-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It can take a while (in rare cases, more than 24 hours) for the map to be updated after edits. Edits you make will immediately show up in the editor because the editor accesses the database directly, but the map tiles shown on www.openstreetmap.org are updated in a separate process.</p>
<p>The question "why do my edits not show up on the map" is the #1 most asked question on this help site, and in most cases it is just a matter of patience.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '13, 00:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23841" class="comments-container">
<span id="23842"></span>
<div id="comment-23842" class="comment">
<div id="post-23842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In this specific case there were multiple changesets left in state "still editing" until they timed out, so there is probably something more than just "wait and see"/"flush your cache" that can be done in order to speed things up.</p>
</div>
<div id="comment-23842-info" class="comment-info">
<span class="comment-age">(30 Jun '13, 00:31)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="23847"></span>
<div id="comment-23847" class="comment">
<div id="post-23847-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><strong>There are both a tile cache AND a zoom issue.</strong> See EDIT 2 in the question.</p>
</div>
<div id="comment-23847-info" class="comment-info">
<span class="comment-age">(30 Jun '13, 10:26)</span> <span class="comment-user userinfo">wikipedia</span>
</div>
</div>
<span id="23914"></span>
<div id="comment-23914" class="comment">
<div id="post-23914-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Changesets in state "still editing" will not by themselves keep the server from re-rendering the tiles. Edits are published as soon as you upload, not after you close the changeset.</p>
</div>
<div id="comment-23914-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 21:17)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23841-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23838"></span>

<div id="answer-container-23838" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23838-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both changesets are closed now, but your edit history sad "still editing" in English recently. <a href="https://wiki.openstreetmap.org/wiki/Changeset">A changeset can either be closed explicitly, or it closes itself if no edits are added to it for a period of inactivity (currently one hour).</a></p>
<p>There is no peer review of OSM data.</p>
<p>Tiles are not updated instantly, but seeing a partly rendered building is a good sign that it will be OK later on. You may have to flush your browser cache and reload the map to see the updates when they finally show up.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '13, 23:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-23838" class="comments-container">
<span id="23839"></span>
<div id="comment-23839" class="comment">
<div id="post-23839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I closed both Polach and the associated Chromium tabs a while ago. (yes, about one hour ago!). So... my change are kept and will appear later on, is it this ?</p>
</div>
<div id="comment-23839-info" class="comment-info">
<span class="comment-age">(29 Jun '13, 23:45)</span> <span class="comment-user userinfo">wikipedia</span>
</div>
</div>
<span id="23840"></span>
<div id="comment-23840" class="comment">
<div id="post-23840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can only see that <a href="http://www.openstreetmap.org/browse/changeset/16758653">http://www.openstreetmap.org/browse/changeset/16758653</a> has been added in your edit history after changeset 16758129. If you have done any other additions and closed your browser they a probably gone.</p>
<p>Letting the changeset timeout after one hour is not the normal workflow, but a protection against browser crashes and similar. I rarely use the iD and Potlatch editors (I'm mostly a JOSM user), so it's not obvious to me what you likely are doing wrong.</p>
</div>
<div id="comment-23840-info" class="comment-info">
<span class="comment-age">(30 Jun '13, 00:05)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="23849"></span>
<div id="comment-23849" class="comment">
<div id="post-23849-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Letting the changeset timeout after one hour is the normal workflow for the vast majority of Potlatch users. This is not a problem at all. (Potlatch doesn't close a changeset when saving data. It only closes them when you press "C".)</p>
<p>Whether a changeset is closed or not, has absolutely no impact on the rendering of data or on any state of individual objects (nodes, ways, relations) in OSM.</p>
</div>
<div id="comment-23849-info" class="comment-info">
<span class="comment-age">(30 Jun '13, 12:41)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-23838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23838-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

