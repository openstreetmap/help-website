+++
type = "question"
title = "OSRM is still routing through barrier with access=no. Did I configure the barrier properly?"
description = '''There&#x27;s a whole mess of communities around me that have random fire gates across roads, and many of those gates are missing from OSM. Tonight I added three of them using the techniques I saw mentioned here several times:  Double click on the road segment to add a node to the line that defines the ro...'''
date = "2018-09-11T05:36:00Z"
lastmod = "2018-09-11T13:25:00Z"
weight = 65855
keywords = [ "gate", "navigation", "routing", "barrier", "update" ]
aliases = [ "/questions/65855" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSRM is still routing through barrier with access=no. Did I configure the barrier properly?](/questions/65855/osrm-is-still-routing-through-barrier-with-accessno-did-i-configure-the-barrier-properly)

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
<span id="post-65855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65855-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There's a whole mess of communities around me that have random fire gates across roads, and many of those gates are missing from OSM.</p>
<p>Tonight I added three of them using the techniques I saw mentioned here several times:</p>
<ol>
<li>Double click on the road segment to add a node to the line that defines the road</li>
<li>Make the node a barrier=gate, access=no</li>
</ol>
<p>Even though I've done this ORSM still routes through the gate when I test the changes using OSM and Car (OSRM) as the routing engine. Here's a link to one of my changesets: <a href="https://www.openstreetmap.org/changeset/62473213#map=19/47.74587/-122.18389.">https://www.openstreetmap.org/changeset/62473213#map=19/47.74587/-122.18389.</a></p>
<p>Am I missing something?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gate" rel="tag" title="see questions tagged &#39;gate&#39;">gate</span> <span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '18, 05:36</strong></p>
<img src="https://secure.gravatar.com/avatar/1b546917d615dd6c877a5f70ebb7efde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snohoflex&#39;s gravatar image" />
<p><span>snohoflex</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snohoflex has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '18, 08:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-65855" class="comments-container">
&#10;</div>
<div id="comment-tools-65855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65855-form-container" class="comment-form-container">
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

<span id="65857"></span>

<div id="answer-container-65857" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65857-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-65857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your update is just 1 hour ago. The usual routing engines need time to do heavy pre-calculations. Because these calculations are that intensive they are not done every some minutes. The routers OSRM and graphhopper update every few days, you have to wait until that.</p>
<p>By the way, <code>access=private</code> would be more usual than <code>=no</code> in your case.</p>
<p>It is usual to not only add the barrier, but also the access restrictions on the roads which are blocked by it (and as likely indicated by signs). Some routing software might (possibly depending on configuration) even not take point barriers into account and hence not obey your newly added gate. Graphhopper in the configuration which osm.org uses takes gates into account (<a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=50.08266%2C9.06144%3B50.08255%2C9.06103#map=19/50.08246/9.06156">example</a>) but OSRM not (<a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=50.08266%2C9.06144%3B50.08255%2C9.06103#map=19/50.08258/9.06119">same example</a>). This <a href="https://www.openstreetmap.org/node/846750746">example gate</a> has no special tags forbidding cars. The result may be different if it would have them.</p>
<p>See <a href="https://help.openstreetmap.org/questions/29866/add-name-on-an-existing-road-which-changes-its-name-how-do-i-devide-the-road-in-2-sections-with-the-id-editor">that older question on how to divide a way</a>, afterwards you can enter the access restrictions on the restricted part.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '18, 06:25</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '18, 20:56</strong> </span></p>
</div>
</div>
<div id="comments-container-65857" class="comments-container">
<span id="65860"></span>
<div id="comment-65860" class="comment">
<div id="post-65860-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the detailed reply! I'll go divide the way and then add access restrictions as well.</p>
</div>
<div id="comment-65860-info" class="comment-info">
<span class="comment-age">(11 Sep '18, 13:25)</span> <span class="comment-user userinfo">snohoflex</span>
</div>
</div>
</div>
<div id="comment-tools-65857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65857-form-container" class="comment-form-container">
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

