+++
type = "question"
title = "FSEconomy - Tile server options"
description = '''Hi all, I am the lead developer of an open source project called FSEconomy that provides a free service to flight sim enthusiasts. We have been serving the community for over 15 years now. As you would think, maps play an important part of flying, and over the years we have had various solutions, fi...'''
date = "2020-05-19T17:25:00Z"
lastmod = "2020-05-19T17:44:00Z"
weight = 74907
keywords = [ "opensource", "tileserver" ]
aliases = [ "/questions/74907" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FSEconomy - Tile server options](/questions/74907/fseconomy-tile-server-options)

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
<span id="post-74907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74907-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am the lead developer of an open source project called <a href="https://www.fseconomy.net">FSEconomy</a> that provides a free service to flight sim enthusiasts. We have been serving the community for over 15 years now. As you would think, maps play an important part of flying, and over the years we have had various solutions, finally ending up with Google Maps, which for quite some time satisfied those needs. Of course that changed from the free limit per day, which we never hit to a reduction of over half that daily limit for the whole month.</p>
<p>We are removing that dependency and started looking at using leafletjs and OSM for the mapping requirements.</p>
<p>The only funds we collect are strictly volunteer donations that are opened now and then (collecting a limited amount) to cover the basic server costs and registration fees.</p>
<p>Would anyone have any recommendations for a tile service that would perhaps provide free access for open source project with appropriate acknowledgements on the site, or for a reasonable fixed cost for a project like this?</p>
<p>Currently costs are computed to be so high we could get a completely new server to self-host for the monthly costs (not counting labor) that would be charged.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opensource" rel="tag" title="see questions tagged &#39;opensource&#39;">opensource</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '20, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/498c542a00de12a6477a02dc4535048d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FSEAirboss&#39;s gravatar image" />
<p><span>FSEAirboss</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FSEAirboss has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74907" class="comments-container">
<span id="74909"></span>
<div id="comment-74909" class="comment">
<div id="post-74909-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Self-hosting is definitely an option - see <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> for more information. How big a server you would need depends very much on how detailed you want the maps to be that you are serving.</p>
</div>
<div id="comment-74909-info" class="comment-info">
<span class="comment-age">(19 May '20, 17:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74907-form-container" class="comment-form-container">
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

<span id="74908"></span>

<div id="answer-container-74908" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74908-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem is that providing the resources and running the service isn't free for anybody and given that no income is derived from providing such a free service, it will always be dicey to -rely- on a third party providing it for free.</p>
<p>It is quite possible to run a global tile service using OSM data on a $100-$150 per month server (say from Hetzner), you still need to get donations to cover such a cost, but you get a lot more freedom from where to get them.</p>
<p>If you can live with pre-generated vector tiles, such a machine could be substantially smaller btw.</p>
<p>In any case here's a list of commercial providers <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '20, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 May '20, 17:43</strong> </span></p>
</div>
</div>
<div id="comments-container-74908" class="comments-container">
&#10;</div>
<div id="comment-tools-74908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74908-form-container" class="comment-form-container">
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

