+++
type = "question"
title = "When do directions get updated after changes are made to the maps?"
description = '''I made several changes to some roads in my local area about 4 days ago, using the iD in-browser editor. The changes rendered on the main OpenStreetMap map within about 12 hours. However, the directions have still not updated based on the edits I made. I have checked various directions sites that say...'''
date = "2016-12-26T02:39:00Z"
lastmod = "2016-12-26T19:12:00Z"
weight = 53722
keywords = [ "directions", "editing", "update" ]
aliases = [ "/questions/53722" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [When do directions get updated after changes are made to the maps?](/questions/53722/when-do-directions-get-updated-after-changes-are-made-to-the-maps)

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
<span id="post-53722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53722-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-53722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I made several changes to some roads in my local area about 4 days ago, using the iD in-browser editor. The changes rendered on the main OpenStreetMap map within about 12 hours. However, the directions have still not updated based on the edits I made.</p>
<p>I have checked various directions sites that say they use OpenStreetMap data (GraphHopper, MapQuest Open, Mapbox, and obviously the OpenStreetMap site itself). Of all the ones I checked, only GraphHopper has updated.</p>
<p>So does anyone know how often the directions get updated on OpenStreetMap? And is there any way to force a refresh of directions data (I believe there is a way to indicate a higher priority of tile refreshes so that your tiles will update faster). And does anyone know what the process is in terms of how and when the directions update?</p>
<p>Note that most questions I read here were related to how often the maps rendered the changes that someone made. This is not my question, as other people have answered that question very well. My question is solely related to the directions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Dec '16, 02:39</strong></p>
<img src="https://secure.gravatar.com/avatar/233d98b63c188b648e7e465cedee202d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsclev&#39;s gravatar image" />
<p><span>jsclev</span><br />
<span class="score" title="76 reputation points">76</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsclev has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Dec '16, 09:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-53722" class="comments-container">
&#10;</div>
<div id="comment-tools-53722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53722-form-container" class="comment-form-container">
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

<span id="53724"></span>

<div id="answer-container-53724" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53724-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-53724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jsclev has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most routing services need to completely regenerate their internal database from a full dump of the OpenStreetMap database, whereas rendering services can track updates ("diffs") as they are made. This can be a slow process - for example, the routing database at my own site ( <a href="http://cycle.travel/map">http://cycle.travel/map</a> ) takes over two days to generate just Western Europe and North America - so routers update less frequently and on their own schedules. There is no way to force a refresh.</p>
<p>For the OSRM demo server (the default router used by openstreetmap.org), the routing database is usually regenerated every day. I believe at the moment (late December 2016) there may be a bug which has caused updates to pause.</p>
<p>Mapbox uses OSRM and will have their own schedule. Mapquest Open have significantly reduced their commitment to OSM and have contracted most of their services out to Mapbox.</p>
<p>If you find that Graphhopper's own servers are being updated more quickly, you can choose Graphhopper from the dropdown menu on osm.org to use that there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '16, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '18, 06:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-53724" class="comments-container">
<span id="53729"></span>
<div id="comment-53729" class="comment">
<div id="post-53729-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, this was incredibly informative. Do you know if there is a ticket in OSM trac for the bug you referenced? I searched trac but could not find anything related to this problem.</p>
</div>
<div id="comment-53729-info" class="comment-info">
<span class="comment-age">(26 Dec '16, 17:48)</span> <span class="comment-user userinfo">jsclev</span>
</div>
</div>
<span id="53730"></span>
<div id="comment-53730" class="comment">
<div id="post-53730-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No problem. The OSRM demo server is an external service rather than something provided as part of OSM infrastructure, so any ticket would be at the OSRM issue tracker (<a href="https://github.com/Project-OSRM/osrm-backend/issues).">https://github.com/Project-OSRM/osrm-backend/issues).</a> I don't know what particular ticket it might be, but if you pop in on the OSRM IRC channel - <a href="http://irc.openstreetmap.org/">http://irc.openstreetmap.org/</a> , and choose channel #osrm - then you might catch one of the OSRM core developers who can give an update.</p>
</div>
<div id="comment-53730-info" class="comment-info">
<span class="comment-age">(26 Dec '16, 19:12)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53724-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53723"></span>

<div id="answer-container-53723" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53723-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had to wait several days for the routing services to take into account the turn restrictions i struggled to map. I will link to the questions i asked and hopefully the time elapsed can be seen from the comments and dates. Hope this helps. <a href="/questions/32420/turn-restrictions-and-routing-engines">https://help.openstreetmap.org/questions/32420/turn-restrictions-and-routing-engines</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '16, 05:34</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Dec '16, 05:36</strong> </span></p>
</div>
</div>
<div id="comments-container-53723" class="comments-container">
&#10;</div>
<div id="comment-tools-53723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53723-form-container" class="comment-form-container">
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

