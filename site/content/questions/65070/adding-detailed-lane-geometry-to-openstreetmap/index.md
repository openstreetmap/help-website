+++
type = "question"
title = "adding detailed lane geometry to OpenStreetMap"
description = '''Suppose I wished to add detailed lane geometry to OpenStreetMap, like (1) lane centerlines, or (2) lane boundaries, (3) variable lane width (4) lane predecessors/successors. Currently, all I see are: (1) how many marked lanes are there on a highway, e.g. &amp;lt;tag k=&quot;lanes&quot; v=&quot;4&quot;/&amp;gt; (2) which lanes ...'''
date = "2018-08-02T07:14:00Z"
lastmod = "2018-08-03T10:50:00Z"
weight = 65070
keywords = [ "lanes" ]
aliases = [ "/questions/65070" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [adding detailed lane geometry to OpenStreetMap](/questions/65070/adding-detailed-lane-geometry-to-openstreetmap)

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
<span id="post-65070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Suppose I wished to add detailed lane geometry to OpenStreetMap, like (1) lane centerlines, or (2) lane boundaries, (3) variable lane width (4) lane predecessors/successors.</p>
<p>Currently, all I see are:</p>
<p>(1) how many marked lanes are there on a highway, e.g. &lt;tag k="lanes" v="4"/&gt;</p>
<p>(2) which lanes on a two way road are not distributed evenly between the driving directions &lt;tag k="lanes:forward" v="3"/&gt;, &lt;tag k="lanes:backward" v="1"/&gt;</p>
<p>(3) turn=* key, specifying the indicated direction in which a way or a lane will lead for turning or merging, e.g. &lt;tag k="turn:lanes" v="reverse|through|through;right|right"/&gt; &lt;tag k="turn:lanes" v="left|left||||right"/&gt;</p>
<p>I also saw that a proposed feature is <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Street_area">street area</a> (area:highway), where a Way would depict the polygon area of a street. Have you seen any use of this feature, or do you know if/when the feature will be adopted?</p>
<p>My understanding, however, is that this proposed feature will only allow the enumeration of drivable road areas, and not per-lane width/boundaries. I've seen the figure <a href="https://wiki.openstreetmap.org/wiki/File:StreetsLogicalLevel.JPG">here</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '18, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ff26095ec3818f79d4415a297a856903?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnwl1000&#39;s gravatar image" />
<p><span>johnwl1000</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnwl1000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65070" class="comments-container">
&#10;</div>
<div id="comment-tools-65070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65070-form-container" class="comment-form-container">
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

<span id="65073"></span>

<div id="answer-container-65073" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65073-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no reason that the current lane model could not be extended to include lane widths (actually this would be trivial). Adding explicit lane centerlines does not fit well into the current model, and is unlikely to find much support (not the least because that is how we used to model lanes, a model that was discarded).</p>
<p>But in general before embarking on whatever project somebody is asking you to do with OSM, you should familiarize yourself with how things actually work in practical terms.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '18, 08:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-65073" class="comments-container">
<span id="65083"></span>
<div id="comment-65083" class="comment">
<div id="post-65083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for the response Simon.</p>
<p>You are right about the lane widths, these can already be specified <a href="https://taginfo.openstreetmap.org/search?q=width%3Alanes">as I see</a>.</p>
<p>Could you point me to that previous model of lane centerlines that was discarded?</p>
<p>It seems like we would need a "Way" to describe each lane's centerline. My understanding is that it is not permitted to add an extra "Way" ID to a specific lane tag currently. Would the OSM server reject such an upload?</p>
<p>Would a line width have to be uniform across an entire "Way," or can different line widths be expressed for each separate chunk of the Way?</p>
<p>Thanks so much.</p>
<p>Best wishes, John</p>
</div>
<div id="comment-65083-info" class="comment-info">
<span class="comment-age">(02 Aug '18, 19:36)</span> <span class="comment-user userinfo">johnwl1000</span>
</div>
</div>
<span id="65084"></span>
<div id="comment-65084" class="comment">
<div id="post-65084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>whenever road attributes change, you have to split the OSM way into multiple OSM ways.</p>
</div>
<div id="comment-65084-info" class="comment-info">
<span class="comment-age">(02 Aug '18, 19:45)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="65097"></span>
<div id="comment-65097" class="comment">
<div id="post-65097-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@johnw1000 there is essentially no such thing as "not permitted" in OSM, as I pointed out in my answer you need to familiarize yourself with how OSM works. The individual mapping of lanes was never a specifically documented way of mapping lanes AFAIK and always had issues in modelling.</p>
</div>
<div id="comment-65097-info" class="comment-info">
<span class="comment-age">(03 Aug '18, 10:50)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65073-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65074"></span>

<div id="answer-container-65074" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65074-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>there are already +5000 width:lanes, width:lanes:forward and width:lanes:backward according to <a href="https://taginfo.openstreetmap.org/search?q=width%3Alanes">taginfo</a></p>
<p>More information on how to tag properties of individual lanes (maxspeed, surfaces, widths, etc.) can be found on the <a href="https://wiki.openstreetmap.org/wiki/Lanes">wiki</a></p>
<p>There is a <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/change">proposal for change lanes</a> as well, which is more "<a href="https://wiki.openstreetmap.org/wiki/Key:change">in use</a>" than proposed imho.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '18, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '18, 09:23</strong> </span></p>
</div>
</div>
<div id="comments-container-65074" class="comments-container">
&#10;</div>
<div id="comment-tools-65074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65074-form-container" class="comment-form-container">
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

