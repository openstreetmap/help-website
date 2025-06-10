+++
type = "question"
title = "Am I allowed to store some data from OSM/Nominatim in our own database?"
description = '''We are a non-profit organisation developing a platform to share accessibility information of POIs. Although similar to Wheelmap it collects completely different and more complex data for various kind of disabilities. The data is crowd sourced by our users with the help of a Smartphone-App. The data ...'''
date = "2016-10-22T22:19:00Z"
lastmod = "2016-11-06T17:36:00Z"
weight = 52643
keywords = [ "copyleft", "copyright", "legal" ]
aliases = [ "/questions/52643" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Am I allowed to store some data from OSM/Nominatim in our own database?](/questions/52643/am-i-allowed-to-store-some-data-from-osmnominatim-in-our-own-database)

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
<span id="post-52643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52643-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are a non-profit organisation developing a platform to share accessibility information of POIs. Although similar to Wheelmap it collects completely different and more complex data for various kind of disabilities. The data is crowd sourced by our users with the help of a Smartphone-App. The data is stored in our database. Everybody can search and use the data for free though the data is not (yet) under an open data licence.</p>
<p>To simplify the data acquiring process, we would like to suggest POIs in his suroundings to the user by searching them in OSM with Nominatim. The user can then select a POI and add the data we want to collect. For this to work we need to store the coordinates, the name and the place_id of the POI in our own database.</p>
<p>Is this allowed with data from OSM? What are the legal consequences, do we have to release our data under an odbl as well?</p>
<p>I read the licence information of OSM on <a href="http://opendatacommons.org/licenses/odbl/">http://opendatacommons.org/licenses/odbl/</a> but I am not quite sure if I understood it correctly...</p>
<p>Thanks for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-copyleft" rel="tag" title="see questions tagged &#39;copyleft&#39;">copyleft</span> <span class="post-tag tag-link-copyright" rel="tag" title="see questions tagged &#39;copyright&#39;">copyright</span> <span class="post-tag tag-link-legal" rel="tag" title="see questions tagged &#39;legal&#39;">legal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '16, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/184999104034d85f3b6114f1dd685fa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acgjheeb&#39;s gravatar image" />
<p><span>acgjheeb</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acgjheeb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52643" class="comments-container">
<span id="52652"></span>
<div id="comment-52652" class="comment">
<div id="post-52652-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Legal or not, if the data your users add is of interest for OSM, it's certainely not fair.</p>
</div>
<div id="comment-52652-info" class="comment-info">
<span class="comment-age">(23 Oct '16, 18:21)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
<span id="52655"></span>
<div id="comment-52655" class="comment">
<div id="post-52655-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>please keep in mind that OSM ids are not stable. id of the POI can be changed at any time, e.g. when a node is replaced with an area</p>
</div>
<div id="comment-52655-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 06:01)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="52665"></span>
<div id="comment-52665" class="comment">
<div id="post-52665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5587/yvecai">@yvecai</a> We are willing to licence our data under ODbl as well and for example add a tag with a link to our data to the places in OSM. Due to the complexity of our data model I do not see how it could be completely integrated in OSM in a feasible way. We do want to give back to the community as much as possible and are open for suggestions.</p>
</div>
<div id="comment-52665-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 20:03)</span> <span class="comment-user userinfo">acgjheeb</span>
</div>
</div>
<span id="52666"></span>
<div id="comment-52666" class="comment">
<div id="post-52666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5390/escada">@escada</a> You do mean the place_id? Thanks for the useful hint! I will keep that in mind!</p>
</div>
<div id="comment-52666-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 20:07)</span> <span class="comment-user userinfo">acgjheeb</span>
</div>
</div>
<span id="52667"></span>
<div id="comment-52667" class="comment">
<div id="post-52667-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>indeed, if you use the id of an OSM object as your "place_id", they are not edged in stone and can change over time.</p>
<p>As for donating data back. Suppose there is a restaurant in OSM without wheelchair=yes/no information, it would be nice that you could "donate" that data based on your more elaborate data.</p>
</div>
<div id="comment-52667-info" class="comment-info">
<span class="comment-age">(25 Oct '16, 04:20)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-52643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52643-form-container" class="comment-form-container">
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

<span id="52645"></span>

<div id="answer-container-52645" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52645-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="acgjheeb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For authoritative answers (or at least for as-authoritative-as-you-can-get answers), email legal-questions@osmfoundation.org.</p>
<p>What you are planning to do is certainly <em>allowed</em>, however it will most likely trigger the ODbL share-alike clause meaning that if you publicly use your data which is derived from OSM, you will need to make it available under ODbL on request. And of course you need to attribute the source.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '16, 22:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52645" class="comments-container">
<span id="52647"></span>
<div id="comment-52647" class="comment">
<div id="post-52647-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much for you extremly quick answer! I have just written an email as you have suggested.</p>
</div>
<div id="comment-52647-info" class="comment-info">
<span class="comment-age">(22 Oct '16, 22:40)</span> <span class="comment-user userinfo">acgjheeb</span>
</div>
</div>
</div>
<div id="comment-tools-52645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52645-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52840"></span>

<div id="answer-container-52840" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52840-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've got an answer from the email suggested by <a href="http://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a>.</p>
<p>It suggests to read the following pages:</p>
<ul>
<li><a href="http://www.openstreetmap.org/copyright">http://www.openstreetmap.org/copyright</a></li>
<li><a href="http://wiki.osmfoundation.org/wiki/License">http://wiki.osmfoundation.org/wiki/License</a></li>
<li><a href="http://wiki.osmfoundation.org/wiki/License/Community_Guidelines">http://wiki.osmfoundation.org/wiki/License/Community_Guidelines</a></li>
<li><a href="http://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline">http://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline</a></li>
</ul>
<p>Roughly speaking the OSM data can be used with my data if we do not use accessibility data from OSM which we also collect via our website. The OSM data will remain licenced under ODbL no matter how they are extracted.</p>
<p>The exact details depend on the specific use case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '16, 17:36</strong></p>
<img src="https://secure.gravatar.com/avatar/184999104034d85f3b6114f1dd685fa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acgjheeb&#39;s gravatar image" />
<p><span>acgjheeb</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acgjheeb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52840" class="comments-container">
&#10;</div>
<div id="comment-tools-52840" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52840-form-container" class="comment-form-container">
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

