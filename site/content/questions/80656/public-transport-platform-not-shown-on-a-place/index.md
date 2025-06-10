+++
type = "question"
title = "public transport platform not shown on a place"
description = '''How can a bus platform be shown (on a place)? I guessed that at least the border line of the platform would be visible, but nothing can be seen. Should I do the tagging different? One of my platforms is www.openstreetmap.org/way/951470608, the others are near by.  Maybe the problem is that the platf...'''
date = "2021-06-22T13:09:00Z"
lastmod = "2021-08-26T10:28:00Z"
weight = 80656
keywords = [ "not_shown", "platform", "public-transport", "public_transport" ]
aliases = [ "/questions/80656" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [public transport platform not shown on a place](/questions/80656/public-transport-platform-not-shown-on-a-place)

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
<span id="post-80656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80656-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can a bus platform be shown (on a place)? I guessed that at least the border line of the platform would be visible, but nothing can be seen. Should I do the tagging different?<br />
One of my platforms is <a href="https://www.openstreetmap.org/way/951470608">www.openstreetmap.org/way/951470608</a>, the others are near by.</p>
<p>Maybe the problem is that the platform is on a waiting area. (So the <em>public transport platform</em> is on a <em>public transport platform</em>.) The whole place is used as a bus terminal, but next to the elevated platforms is where the bus (most likely) holds.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-platform" rel="tag" title="see questions tagged &#39;platform&#39;">platform</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-public_transport" rel="tag" title="see questions tagged &#39;public_transport&#39;">public_transport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '21, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/85f87038fc28103fa96acb10e6f931b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Simo_He&#39;s gravatar image" />
<p><span>Simo_He</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Simo_He has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-80656" class="comments-container">
&#10;</div>
<div id="comment-tools-80656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80656-form-container" class="comment-form-container">
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

<span id="80657"></span>

<div id="answer-container-80657" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80657-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"Why a particular map does not not show something" is a question for that map. The relevant discussion for the "standard" map is at <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/435">https://github.com/gravitystorm/openstreetmap-carto/issues/435</a> .</p>
<p>In this case the answer seems to be "<a href="https://github.com/gravitystorm/openstreetmap-carto/issues/435#issuecomment-516276212">because that map style chose not to show it</a>". A <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/4191">separate issue</a> (specifically with regard to areas) was marked as a duplicate - maybe you could make a case that areas are a special case and should be shown in some way, whereas a "<code>public_transport=platform</code>" that simply duplicates a "<code>highway=bus_stop</code>" doesn't really add any value.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '21, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '21, 13:32</strong> </span></p>
</div>
</div>
<div id="comments-container-80657" class="comments-container">
<span id="80772"></span>
<div id="comment-80772" class="comment">
<div id="post-80772-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I see, it definitely has to do with this.</p>
<p>But before I ask to adapt rendering, I prefer to check my tagging. Did I do it in a good way? My intention is to show the area which is elevated. And still keep the existing "bus station", which is the whole place where the buses stop.</p>
<p>The view of <a href="https://www.openstreetmap.org/way/155067852">https://www.openstreetmap.org/way/155067852</a> would be desired. I found this by looking for the place shown for "amenity: bus_station" on <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbus_station">https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbus_station</a></p>
<p>So possible adaptions of the tags:</p>
<ul>
<li>whole place: set "amenity: bus_station" and change "public_transport: " to "platform"<br />
There is also a node with "amenity: bus_station". Should it be kept?</li>
<li>passenger platform: add "highway: platform" (which is as recommended on <a href="https://wiki.openstreetmap.org/wiki/Public_transport#Buses">https://wiki.openstreetmap.org/wiki/Public_transport#Buses</a> , but I missed it because the editior did not set it automatically)</li>
</ul>
</div>
<div id="comment-80772-info" class="comment-info">
<span class="comment-age">(29 Jun '21, 13:30)</span> <span class="comment-user userinfo">Simo_He</span>
</div>
</div>
<span id="81500"></span>
<div id="comment-81500" class="comment">
<div id="post-81500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did the adaptions (on the place and the platforms), and it is visible now (see <a href="https://www.openstreetmap.org/way/951470608">https://www.openstreetmap.org/way/951470608</a> now). (The changes are in <a href="https://www.openstreetmap.org/changeset/107148951)">https://www.openstreetmap.org/changeset/107148951)</a></p>
</div>
<div id="comment-81500-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 10:28)</span> <span class="comment-user userinfo">Simo_He</span>
</div>
</div>
</div>
<div id="comment-tools-80657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80657-form-container" class="comment-form-container">
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

