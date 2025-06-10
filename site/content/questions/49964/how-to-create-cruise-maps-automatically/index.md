+++
type = "question"
title = "how to create cruise maps automatically"
description = '''Hi, so I have a project here that requires to create maps of cruises (with ships) (e.g. cruises of Carnival Cruise Line or RCCL or MSC). So usually these maps are painted by hand either really painted or edited in some sort of map editor. The challenge is that you only have the GPS coordinates of th...'''
date = "2016-06-02T02:29:00Z"
lastmod = "2016-06-02T19:41:00Z"
weight = 49964
keywords = [ "itinerary", "cruise" ]
aliases = [ "/questions/49964" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to create cruise maps automatically](/questions/49964/how-to-create-cruise-maps-automatically)

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
<span id="post-49964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49964-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>so I have a project here that requires to create maps of cruises (with ships) (e.g. cruises of Carnival Cruise Line or RCCL or MSC). So usually these maps are painted by hand either really painted or edited in some sort of map editor. The challenge is that you only have the GPS coordinates of the ports where the ship is calling. Since there are no streets all of the routing mechanism <em>just use straight lines</em> even if an island is in between.</p>
<p>So what I'm looking for is a way to just enter GPS coordinates and then have a tool generating cruise route maps automatically.</p>
<p>That should be the result: <img src="http://media.montrosetravel.com/montrosetravel/images/group-travel/mediterranean_wine_cruise_map.jpg" alt="http://media.montrosetravel.com/montrosetravel/images/group-travel/mediterranean_wine_cruise_map.jpg" /></p>
<p>looking forward to creative ideas!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-itinerary" rel="tag" title="see questions tagged &#39;itinerary&#39;">itinerary</span> <span class="post-tag tag-link-cruise" rel="tag" title="see questions tagged &#39;cruise&#39;">cruise</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '16, 02:29</strong></p>
<img src="https://secure.gravatar.com/avatar/d9322b9f975f9e0ecefa79d460447f6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="das_ubersoldat&#39;s gravatar image" />
<p><span>das_ubersoldat</span><br />
<span class="score" title="55 reputation points">55</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="das_ubersoldat has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '16, 19:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-49964" class="comments-container">
<span id="49967"></span>
<div id="comment-49967" class="comment">
<div id="post-49967-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Could this question be more suitable for <a href="http://gis.stackexchange.com/">GIS Stack Exchange</a>?</p>
</div>
<div id="comment-49967-info" class="comment-info">
<span class="comment-age">(02 Jun '16, 08:43)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
<span id="49968"></span>
<div id="comment-49968" class="comment">
<div id="post-49968-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Well, you do have coast outlines in OSM; so it's a matter of finding a short-ish Bezier path from one hop to next, one which doesn't intersect coastlines, and keeps reasonably clear of the coast (perhaps by extending the coastlines a few km out and routing in the resulting shape). Getting from that to an algorithm should be smooth sailing (pardon the pun). This, of course, will be an approximation only, as shipping lanes are dictated by other factors, and you'd need to tweak the map by hand (e.g. for the strait of Sicily).</p>
</div>
<div id="comment-49968-info" class="comment-info">
<span class="comment-age">(02 Jun '16, 08:46)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="49973"></span>
<div id="comment-49973" class="comment">
<div id="post-49973-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Cross-posted here: <a href="http://forum.openstreetmap.org/viewtopic.php?id=54771">http://forum.openstreetmap.org/viewtopic.php?id=54771</a></p>
</div>
<div id="comment-49973-info" class="comment-info">
<span class="comment-age">(02 Jun '16, 17:25)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="49974"></span>
<div id="comment-49974" class="comment">
<div id="post-49974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Record them with a gps, smart phone or a car sat nav which you could power with one of high capacity power banks or from the ship's power supply, as i assume you may have to keep the device powered up for a few days. Getting a signal below decks will be a problem, although i recorded one by the window on a holiday jet. If you are working for the cruise line get a gpx from the company.</p>
</div>
<div id="comment-49974-info" class="comment-info">
<span class="comment-age">(02 Jun '16, 17:35)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="49976"></span>
<div id="comment-49976" class="comment">
<div id="post-49976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I forgot the mention that the route doesn't have to be precisely the route the ship is taking. It is just for informational purposes.</p>
</div>
<div id="comment-49976-info" class="comment-info">
<span class="comment-age">(02 Jun '16, 18:26)</span> <span class="comment-user userinfo">das_ubersoldat</span>
</div>
</div>
<span id="49978"></span>
<div id="comment-49978" class="comment not_top_scorer">
<div id="post-49978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/12376/das_ubersoldat">@das_ubersoldat</a>: In general, please do not post your questions to several places (at least not without mentioning it and linking all places). That wastes help resources.</p>
</div>
<div id="comment-49978-info" class="comment-info">
<span class="comment-age">(02 Jun '16, 19:41)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49964" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-49964-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

