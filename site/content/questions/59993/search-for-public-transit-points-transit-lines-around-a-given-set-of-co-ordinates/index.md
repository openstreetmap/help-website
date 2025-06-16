+++
type = "question"
title = "Search for Public Transit Points &amp; transit lines around a given set of co-ordinates"
description = '''Hello, Given a set of lat/long in Germany, I would like to search for all the Public Transportation Points in a 500m radius. Then, would like to fetch all the public transit lines that pass through that Public transit point. When I state Public Transportation Points, I mean stops where Buses, Trains...'''
date = "2017-10-06T14:39:00Z"
lastmod = "2018-09-30T12:35:00Z"
weight = 59993
keywords = [ "transit", "public-transport" ]
aliases = [ "/questions/59993" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Search for Public Transit Points & transit lines around a given set of co-ordinates](/questions/59993/search-for-public-transit-points-transit-lines-around-a-given-set-of-co-ordinates)

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
<span id="post-59993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59993-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Given a set of lat/long in Germany, I would like to search for all the Public Transportation Points in a 500m radius. Then, would like to fetch all the public transit lines that pass through that Public transit point.</p>
<p>When I state Public Transportation Points, I mean stops where Buses, Trains/Subways &amp; Trams stop. Specifically, looking for nodes with the following tags:</p>
<ul>
<li>Bus: public_transport=stop_position + bus=yes.</li>
<li>Subway/Train: public_transport=stop_position + train=yes + railway=stop + name=*</li>
<li>Tram: public_transport=stop_position + tram=yes + name=*</li>
</ul>
<p>On knowing the Points, I would then like to know all the Bus, Tram &amp; Subway lines that pass through these points.</p>
<p>Is it feasible to fetch this sort of information with OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-transit" rel="tag" title="see questions tagged &#39;transit&#39;">transit</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '17, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/23e8dfc00665c15d1992486c171921db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="urbanground&#39;s gravatar image" />
<p><span>urbanground</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="urbanground has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '17, 15:59</strong> </span></p>
</div>
</div>
<div id="comments-container-59993" class="comments-container">
<span id="60007"></span>
<div id="comment-60007" class="comment">
<div id="post-60007-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is a "Public Transportation Points" supposed to be? A station/halt, a junction of multiple routes? ....</p>
</div>
<div id="comment-60007-info" class="comment-info">
<span class="comment-age">(08 Oct '17, 09:50)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="60013"></span>
<div id="comment-60013" class="comment">
<div id="post-60013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am looking for Bus, Subway &amp; Trams. For bus, nodes with Tags: public_transport=stop_position + bus=yes. For Subway/Train: public_transport=stop_position + train=yes + railway=stop + name= <em>For Tram: public_transport=stop_position + tram=yes + name=</em></p>
</div>
<div id="comment-60013-info" class="comment-info">
<span class="comment-age">(08 Oct '17, 15:54)</span> <span class="comment-user userinfo">urbanground</span>
</div>
</div>
<span id="66102"></span>
<div id="comment-66102" class="comment">
<div id="post-66102-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This would be very useful feature and quite easily done with existing code I assume. Now already manully one can click all public transportation (PT) stops around some POI and see eg. all the busses/trams/metros which stops there. With a pen and paper (or snapshot) then collect all those PT-lines. Now just the code optionally would automatically "click" all those PT-stops around some radius and return a list of stops and PT-lines. See also: <a href="/questions/45635/public-transport?">https://help.openstreetmap.org/questions/45635/public-transport?</a></p>
</div>
<div id="comment-66102-info" class="comment-info">
<span class="comment-age">(30 Sep '18, 12:35)</span> <span class="comment-user userinfo">zimon</span>
</div>
</div>
</div>
<div id="comment-tools-59993" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59993-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

