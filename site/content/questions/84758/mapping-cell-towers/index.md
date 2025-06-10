+++
type = "question"
title = "Mapping Cell Towers"
description = '''Are there any useful apps for displaying Cell Towers (eg OpenCelliD) on a map with OSM data? Scenario: I&#x27;m driving through the desert, and I suddenly have to join a video conference. I notice that I have no cellular data, and I&#x27;m at a 4-way cross roads: each going North, South, East, and West. I&#x27;m l...'''
date = "2022-06-12T16:32:00Z"
lastmod = "2024-02-23T16:26:00Z"
weight = 84758
keywords = [ "radio" ]
aliases = [ "/questions/84758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping Cell Towers](/questions/84758/mapping-cell-towers)

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
<span id="post-84758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84758-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Are there any useful apps for displaying Cell Towers (eg OpenCelliD) on a map with OSM data?</p>
<p>Scenario: I'm driving through the desert, and I suddenly have to join a video conference. I notice that I have no cellular data, and I'm at a 4-way cross roads: each going North, South, East, and West.</p>
<p>I'm looking for an app that has all this data offline and will show me [a] my location and [b] all the nearby cell towers. Ideally, it should tell me if the cell tower will work with my specific mobile provider's SIM card.</p>
<p>I already use OpenStreetMaps for offline maps, so a plugin for OSM would be ideal.</p>
<p>Is there a way to get an offline map of the cell towers near my current location, so I know where to go for the best possible signal and least possible packet loss?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-radio" rel="tag" title="see questions tagged &#39;radio&#39;">radio</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '22, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0f7bbdc746034db6f838997f2a85a59c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maltfield&#39;s gravatar image" />
<p><span>maltfield</span><br />
<span class="score" title="55 reputation points">55</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maltfield has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84758" class="comments-container">
<span id="88258"></span>
<div id="comment-88258" class="comment">
<div id="post-88258-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note: This question was migrated to the OSM Discourse here <a href="https://community.openstreetmap.org/t/mapping-cell-towers/109663">https://community.openstreetmap.org/t/mapping-cell-towers/109663</a></p>
</div>
<div id="comment-88258-info" class="comment-info">
<span class="comment-age">(23 Feb '24, 16:26)</span> <span class="comment-user userinfo">maltfield</span>
</div>
</div>
</div>
<div id="comment-tools-84758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84758-form-container" class="comment-form-container">
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

<span id="85109"></span>

<div id="answer-container-85109" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85109-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>I don't know of any. You can explore the osm data, through the tag <a href="https://wiki.openstreetmap.org/wiki/Key:communication:mobile_phone">communication:mobile_phone</a>, via <a href="https://overpass-turbo.eu/?template=key&amp;key=communication%3Amobile_phone">overpass turbo</a>, for example, you can check out the mapped cell towers of a given region. Around my place (in France), mapping is pretty erratic, various tagging schemes, places left out, not so useful I'm afraid.</p>
<p>Mainly there is not documented way of specifying the mobile provider. <a href="https://taginfo.openstreetmap.org/keys/communication:mobile_phone#combinations">Taginfo</a> says that quite a lot use the operator key, but not consistently. I guess the best data for automatic matching would be MCC and MNC, but it's only on 10.000 places, worldwide... And again, it is not a documented practice.</p>
<p>Some king of matching between OpenCellID and OSM would be nice, and I guess have already been discussed, but it would be a lot of work, and nobody is on it AFAIK.</p>
<p>As for access on a mobile phone, I assume you're talking about OsmAnd, as OpenStreetMap is not an app. In OsmAnd you can search for <a href="https://wiki.openstreetmap.org/wiki/Tag:tower:type%3Dcommunication">tower:type=communication</a> and display them on the map, which is a start, but not so useful in your case I'm afraid.</p>
<p>As a kind of workaround, you can probably download OpenCellID data, convert it to gpx (or kml if you want coloring by provider for example), and import that into OsmAnd. Maybe filter only those for your provider and crop to the region you need, to keep OsmAnd running smoothly. Then you can display the points on your map, search for them...</p>
<p>Best regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '22, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-85109" class="comments-container">
<span id="85110"></span>
<div id="comment-85110" class="comment">
<div id="post-85110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>I guess the best data for automatic matching would be MCC and MNC</p>
</blockquote>
<p>The challenge with MCC/MNC is that one tower (and one operator) will match lots of MCC/MNC combinations - both brands (including former brands) belonging to one carrier and MVNOs using that carrier.</p>
<p>Also in the UK at least sharing towers between networks is a thing, and there are also third-party operators to further complicate matters.</p>
</div>
<div id="comment-85110-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 14:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="85130"></span>
<div id="comment-85130" class="comment">
<div id="post-85130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think that it's possible to record the various codes used when the phone is connected to some network, and then search for them in the surrounding or distant towers.</p>
<p>For the few nodes I've checked, MNC are usually semi-colon separated lists of codes, so it's not impossible to parse. MCC is always the same. Main trouble is the lack of data for now...</p>
<p>operator value are more free style concatenation of operators names (only 4 in France, all the others are virtual, and usually attached to only one of the 4, but I don't think this applies elsewhere).</p>
</div>
<div id="comment-85130-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 18:22)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-85109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85109-form-container" class="comment-form-container">
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

