+++
type = "question"
title = "How to tag flood prone points and areas?"
description = '''In the summer of 2018, we conducted a project called Assets and Threats mapping under the Ramani Huria project in Dar es Salaam, Tanzania that aims to make Dar es Salaam a more flood-resilient city. In this project, we focused on the assets/amenities in the city that are important to the community a...'''
date = "2019-08-20T09:04:00Z"
lastmod = "2019-08-31T18:09:00Z"
weight = 70433
keywords = [ "flood", "poi", "assets", "aoi", "risk" ]
aliases = [ "/questions/70433" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag flood prone points and areas?](/questions/70433/how-to-tag-flood-prone-points-and-areas)

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
<span id="post-70433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70433-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the summer of 2018, we conducted a project called <a href="https://docs.google.com/document/d/11HQttl5Pb8IFgATufV4LxaDn0eCXEcEuA56phrf1X0Y/edit#heading=h.gdboihqvh9gy">Assets and Threats mapping</a> under the Ramani Huria project in Dar es Salaam, Tanzania that aims to make Dar es Salaam a more flood-resilient city. In this project, we focused on the assets/amenities in the city that are important to the community and are at risk of flooding or not.</p>
<p>After collecting all the information, we decided we should upload them in OSM to be shared with the world since it was a successful project to some extent. The challenge came when we could not upload these data since there is no specific tag to use for amenities or AoIs affected by floods, the only tag that we could find is <a href="https://wiki.openstreetmap.org/wiki/Key:flood_prone">flood_prone=yes</a> but this is mostly applicable to “roads/ways" that go underwater after heavy rains.</p>
<ol>
<li>Is there any other tag that can be used for points under flooding threat or can we use another tag?</li>
<li>Our initial thought was to create a new tag i.e. <code>asset:risk=yes</code> and <code>asset:risk=no</code> or we could overcome this challenge by <strong>having one tag that is used by the entire OSM community to identify ways, areas, or points</strong> that are prone to floods</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-flood" rel="tag" title="see questions tagged &#39;flood&#39;">flood</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span> <span class="post-tag tag-link-assets" rel="tag" title="see questions tagged &#39;assets&#39;">assets</span> <span class="post-tag tag-link-aoi" rel="tag" title="see questions tagged &#39;aoi&#39;">aoi</span> <span class="post-tag tag-link-risk" rel="tag" title="see questions tagged &#39;risk&#39;">risk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '19, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/2a226ee3bf76ec222b0bf6ade02e59f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Imma%20Mwanja&#39;s gravatar image" />
<p><span>Imma Mwanja</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Imma Mwanja has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70433" class="comments-container">
&#10;</div>
<div id="comment-tools-70433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70433-form-container" class="comment-form-container">
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

<span id="70435"></span>

<div id="answer-container-70435" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70435-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Imma,</p>
<p>flood_prone=yes could be used. As <a href="https://taginfo.openstreetmap.org/keys/?key=flood_prone#combinations">taginfo shows</a> this tag has been used over 6600 times on an amenity of some kind (only 2800 times on highways actually).</p>
<p>For a more detailed discussion on benefits of a separate/new tag I would suggest you take this question to the <a href="https://lists.openstreetmap.org/listinfo/tagging">tagging</a> <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">mailing list</a>. There are more people listening in who might have some valuable suggestions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '19, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-70435" class="comments-container">
<span id="70576"></span>
<div id="comment-70576" class="comment">
<div id="post-70576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello, <a href="https://help.openstreetmap.org/users/10133/tzorn">TZorn</a> thank you for your reply. I followed your suggestion and took my question to the <a href="https://lists.openstreetmap.org/listinfo/tagging">tagging mailing list</a> and like you, they think that <code>flood_prone=yes</code> is the right tag</p>
</div>
<div id="comment-70576-info" class="comment-info">
<span class="comment-age">(31 Aug '19, 18:09)</span> <span class="comment-user userinfo">Imma Mwanja</span>
</div>
</div>
</div>
<div id="comment-tools-70435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70435-form-container" class="comment-form-container">
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

