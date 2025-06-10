+++
type = "question"
title = "Boardwalk renders as bridge"
description = '''Hi -  I need to convince the people at trailforks.com that they have a configuration issue - I am claiming something is a boardwalk (we built it, so yeah) - When I added it, the icon rendered on the map is a bridge - rather than the boardwalk icon. https://www.trailforks.com/poi/69665/ It knows it i...'''
date = "2022-02-03T02:10:00Z"
lastmod = "2022-02-03T13:25:00Z"
weight = 83320
keywords = [ "#icons", "#boardwalk" ]
aliases = [ "/questions/83320" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Boardwalk renders as bridge](/questions/83320/boardwalk-renders-as-bridge)

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
<span id="post-83320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83320-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi -</p>
<p>I need to convince the people at trailforks.com that they have a configuration issue - I am claiming something is a boardwalk (we built it, so yeah) - When I added it, the icon rendered on the map is a bridge - rather than the boardwalk icon.</p>
<p><a href="https://www.trailforks.com/poi/69665/">https://www.trailforks.com/poi/69665/</a></p>
<p>It knows it is a boardwalk - but take a look at the map!</p>
<p>What do I tell the admin person?</p>
<p>In case you can't follow the link above, here is a screen shot:</p>
<p><a href="https://drive.google.com/file/d/1Bf8wn0mB8m7wSTVU9-QztgB01CDSHVIF/view?usp=sharing">https://drive.google.com/file/d/1Bf8wn0mB8m7wSTVU9-QztgB01CDSHVIF/view?usp=sharing</a></p>
<p>Just opening a ticket on trailforks got crickets.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-#icons" rel="tag" title="see questions tagged &#39;#icons&#39;">#icons</span> <span class="post-tag tag-link-#boardwalk" rel="tag" title="see questions tagged &#39;#boardwalk&#39;">#boardwalk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '22, 02:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a033931ba2efb4208587afc0a14fe243?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fidodie&#39;s gravatar image" />
<p><span>Fidodie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fidodie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83320" class="comments-container">
<span id="83330"></span>
<div id="comment-83330" class="comment">
<div id="post-83330-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> and <a href="https://help.openstreetmap.org/users/2925/bcnorwich">@BCNorwich</a>. My role with trailforks is a region admin (state of NJ) with permission to add/approve/edit trails and features. I have no access to any config or policy on the interaction with OSM.</p>
<p>I'm new to OSM but have ArcGIS and shapefile programming (i'm old.)</p>
<p>Our version of the Red Trail is based on the <a href="https://www.openstreetmap.org/way/48017859#map=17/40.46529/-74.53260">deleted Way 48017859</a></p>
<p>Trailfork's layer for the bridges, boardwalks, etc, are added as points (points of interest, the same as a picnic table or restroom,) rather than having length/endpoints. I'm sure that will not change.</p>
<p>When hovering over the boardwalk icon (displayed as a bridge) then <a href="https://www.trailforks.com/poi/69665/">following the link</a>, it is clearly marked at type:Boardwalk - With the icon on the map displaying as bridge.</p>
<p>As a first level correction, getting it to render with the boardwalk icon on the map would be nice.</p>
<p>Looking at the trailforks app, vs the web interface, the boardwalk renders as a green star, yet still has type:Boardwalk when selected.</p>
<p>Ideas on where this is configured locally?</p>
</div>
<div id="comment-83330-info" class="comment-info">
<span class="comment-age">(03 Feb '22, 09:44)</span> <span class="comment-user userinfo">Fidodie</span>
</div>
</div>
<span id="83331"></span>
<div id="comment-83331" class="comment">
<div id="post-83331-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The answer given by <a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> explains how to add the data to OSM - that way whenever Trailforks fetch data from OSM in the future (however they do that) it'll incorporate the boardwalk.</p>
<p>This appears to be separate to Trailforks' "there is something interesting with a picture" layer, which will presumably remain and adds extra value at Trailforks.</p>
</div>
<div id="comment-83331-info" class="comment-info">
<span class="comment-age">(03 Feb '22, 10:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="83335"></span>
<div id="comment-83335" class="comment">
<div id="post-83335-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/21367/fidodie">@Fidodie</a> RE: "Ideas on where this is configured locally?" If you think the data being displayed isn't actually linked to underlying OSM data then we are unlikely to be able to help. The further you get from this help site's niche, the more of a fluke it'd be if we knew the answer.</p>
</div>
<div id="comment-83335-info" class="comment-info">
<span class="comment-age">(03 Feb '22, 13:25)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-83320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83320-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="83322"></span>

<div id="answer-container-83322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83322-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The data may be incorrect in OSM. Your link seems to correspond to <a href="https://www.openstreetmap.org/way/48017038#map=17/40.46723/-74.53648">way 48017038</a>. This is just marked as a dirt path, it needs to be edited so that the extent of the boardwalk is correctly split from the rest of the path and appropriately tagged. In OSM boardwalks are mapped <a href="https://wiki.openstreetmap.org/wiki/Tag:bridge%3Dboardwalk">as a subtype of bridge</a>. Once the data in OSM is tagged correctly then there is nothing that can be done on the OSM side of things. Anyone using the data will have to update according to their own preferred pace (although you may be able to prompt them to update an area sooner).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '22, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-83322" class="comments-container">
<span id="83323"></span>
<div id="comment-83323" class="comment">
<div id="post-83323-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is the second attempt at an answer after finding a way to get coordinates out of your link. Sorry about the duplicate notifications.</p>
</div>
<div id="comment-83323-info" class="comment-info">
<span class="comment-age">(03 Feb '22, 08:10)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-83322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83322-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83324"></span>

<div id="answer-container-83324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83324-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, I take it you are referring to this area of OSM data:- <a href="https://www.openstreetmap.org/changeset/37899960#map=17/40.46745/-74.53707&amp;layers=D">https://www.openstreetmap.org/changeset/37899960#map=17/40.46745/-74.53707&amp;layers=D</a> If so then OSM does not have any bridges or boardwalks mapped here.</p>
<p>The bridges and boardwalks on your link seem to be a layer that's been added to Trailforks. Even the Red Trail is not as drawn on OSM. If you add the data to OSM then it can be seen when the OSM basemap in Trailforks is activated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '22, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-83324" class="comments-container">
<span id="83325"></span>
<div id="comment-83325" class="comment">
<div id="post-83325-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The boardwalk and bridge icon are the same, so if you add either the icon will be the as same one. Rest your cursor over an icon and its name will appear, then they are marked as bridge or boardwalk as the case may be. So Trailforks data looks correct, rendering one icon for two features seems to be the problem</p>
</div>
<div id="comment-83325-info" class="comment-info">
<span class="comment-age">(03 Feb '22, 08:21)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="83326"></span>
<div id="comment-83326" class="comment">
<div id="post-83326-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The <a href="https://www.trailforks.com/map/legend/">legend</a> suggests a slightly different icon should be showing.</p>
</div>
<div id="comment-83326-info" class="comment-info">
<span class="comment-age">(03 Feb '22, 08:27)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-83324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83324-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83327"></span>

<div id="answer-container-83327" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83327-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you say "when I added it", do you mean that you added a POI in Trailforks (rather than OpenStreetMap)? If that is the case, and the icon displayed on the map is driven by Trailforks' own POI database, then this doesn't seem to be anything to do with OSM (there is no mechanism for information in Trailforks to be fed into the OSM database). Given that the correct Boardwalk icon is displayed on the POI page you linked, it does seem like an internal error where they are not using this icon in their POI layer on the displayed map.</p>
<p>As it happens, the data in OpenStreetMap probably could be improved. Looking at this area <a href="https://www.openstreetmap.org/#map=19/40.46747/-74.53771">https://www.openstreetmap.org/#map=19/40.46747/-74.53771</a> , I don't see the boardwalk mapped anywhere. I also don't see anything mapped a bit to the north where the trail crosses Six Mile Run - so there is no way to tell from OSM data if there is a bridge or a ford here. The same applies at other water crossings in the area. If you improve the OpenStreetMap data here, that will potentially feed through to all applications that use OSM data.</p>
<p>BUT as I said above, if Trailforks are displaying icons based on their own POI database, improving OSM won't fix that specific issue (although perhaps some indication of bridges and boardwalks would be visible in the background layer, depending on how the tiles are generated).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '22, 08:31</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-83327" class="comments-container">
<span id="83329"></span>
<div id="comment-83329" class="comment">
<div id="post-83329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/14272/alan_gr">@alan_gr</a>. I believe your analysis is correct - I'm working at the TF level, not the OSM level - so everything is local. See my answer below (i'm not sure if i should answer or comment when i update info)</p>
<p>Thank you for taking the time to help educate me.</p>
</div>
<div id="comment-83329-info" class="comment-info">
<span class="comment-age">(03 Feb '22, 09:43)</span> <span class="comment-user userinfo">Fidodie</span>
</div>
</div>
</div>
<div id="comment-tools-83327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83327-form-container" class="comment-form-container">
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

