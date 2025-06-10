+++
type = "question"
title = "How to map garbage truck routes?"
description = '''In the city where I live was made public the routes and schedules of garbage trucks in PDF format. Editing the relations of the routes for public transport I asked myself, why not do it for those routes too? Reading the wiki page for relations of the routes I didn&#x27;t find information or specific tags...'''
date = "2013-12-22T21:47:00Z"
lastmod = "2013-12-23T12:27:00Z"
weight = 29283
keywords = [ "route", "trash", "truck", "tagging", "garbage" ]
aliases = [ "/questions/29283" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to map garbage truck routes?](/questions/29283/how-to-map-garbage-truck-routes)

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
<span id="post-29283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29283-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the city where I live was made public <a href="http://www.emsa.gob.bo/rutas/San%20Pedro-UMSS%20CH-19.pdf">the routes and schedules of garbage trucks</a> in PDF format. Editing the relations of the routes for public transport I asked myself, why not do it for those routes too?</p>
<p>Reading the wiki page for <a href="http://wiki.openstreetmap.org/wiki/Relation:route">relations of the routes</a> I didn't find information or specific tags</p>
<p>Someone did something similar?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-trash" rel="tag" title="see questions tagged &#39;trash&#39;">trash</span> <span class="post-tag tag-link-truck" rel="tag" title="see questions tagged &#39;truck&#39;">truck</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-garbage" rel="tag" title="see questions tagged &#39;garbage&#39;">garbage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '13, 21:47</strong></p>
<img src="https://secure.gravatar.com/avatar/b28923423b98dace80389ae64c99bf93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="5m4u9&#39;s gravatar image" />
<p><span>5m4u9</span><br />
<span class="score" title="156 reputation points">156</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="5m4u9 has one accepted answer">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Dec '13, 10:13</strong> </span></p>
</div>
</div>
<div id="comments-container-29283" class="comments-container">
&#10;</div>
<div id="comment-tools-29283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29283-form-container" class="comment-form-container">
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

<span id="29296"></span>

<div id="answer-container-29296" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29296-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="5m4u9 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://mappa-mercia.org/gritting-map.shtml">Gritting routes</a> have been mapped in some places. These were done by adding <code>maintenance=gritting</code> and other gritting prefixed tags to the ways rather than using route relations. <a href="http://www.openstreetmap.org/way/38791082">A link to an example way</a>.</p>
<p>I would be tempted though, if you decide to add (and maintain) the information, to use route relations with the tag <code>route=waste_collection</code> or similar (as waste seems to be used more in OSM for related items than garbage - see <a href="http://taginfo.openstreetmap.org/search?q=waste#values">taginfo</a>). This allows for multiple routes along the same way without needing to semi-colon separate references (for example) as in <code>gritting_route_ref=B;H</code> <a href="http://www.openstreetmap.org/way/7984151">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Dec '13, 09:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-29296" class="comments-container">
<span id="29301"></span>
<div id="comment-29301" class="comment">
<div id="post-29301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <span>@edloach</span>. The gritting routes and waste collection has fairly similarity. This solution is non-invasive, as you say, it would suffice define the prefixes of the tags for the ways and use the tags for waste containers (or similar tags).</p>
<p>In the "gritting_operator" tag, I see again (the controversy)... use prefix tag + "_operator" or ":operator" ¿? :(</p>
</div>
<div id="comment-29301-info" class="comment-info">
<span class="comment-age">(23 Dec '13, 11:45)</span> <span class="comment-user userinfo">5m4u9</span>
</div>
</div>
</div>
<div id="comment-tools-29296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29296-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29295"></span>

<div id="answer-container-29295" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29295-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, there seems to be currently <strong>no schema</strong> for tagging this routes. Of course you are welcome to be the first and describe this new feature :)</p>
<p>But IMHO you should always ask, if it makes sense to add a new feature to OSM. I'm not sure if this informations are in a wide interest and if we have enough people that like to keep them up to date. At least in my city we have a mixed system of static routes that get altered if people report extra garbage collections. So here it would IMHO make no sense :( I think there was already a discussion about the schedules for Public transport with the result, that it's not pure geodata and thus should not be modeled within OSM. Steve Coast himself wanted to start a project about collecting it externally and make them machine readable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Dec '13, 07:27</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-29295" class="comments-container">
<span id="29304"></span>
<div id="comment-29304" class="comment">
<div id="post-29304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks @¡¡¡. As you say, the persons concerned will be very few... eg waste collection companies.</p>
<p>Reading on the mailing list "talk-transit", I understood the problem of schedules and GTFS format. Apparently, Steve's "transiki" project are stopped. :(</p>
</div>
<div id="comment-29304-info" class="comment-info">
<span class="comment-age">(23 Dec '13, 12:27)</span> <span class="comment-user userinfo">5m4u9</span>
</div>
</div>
</div>
<div id="comment-tools-29295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29295-form-container" class="comment-form-container">
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

