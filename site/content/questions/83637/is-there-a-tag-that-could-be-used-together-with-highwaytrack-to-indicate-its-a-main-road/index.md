+++
type = "question"
title = "Is there a tag that could be used together with highway=track to indicate it’s a main road?"
description = '''Please kindly carefully read the context and requirements below before posting an answer/comment: Context: In Thailand, many remote roads linking villages are only suitable for high clearance pickup trucks which are the standard car in mountainous and remote areas. Our recent wiki update says those ...'''
date = "2022-03-04T10:58:00Z"
lastmod = "2022-03-10T10:15:00Z"
weight = 83637
keywords = [ "track", "unclassified", "4wd" ]
aliases = [ "/questions/83637" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a tag that could be used together with highway=track to indicate it’s a main road?](/questions/83637/is-there-a-tag-that-could-be-used-together-with-highwaytrack-to-indicate-its-a-main-road)

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
<span id="post-83637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83637-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<h4 id="please-kindly-carefully-read-the-context-and-requirements-below-before-posting-an-answercomment">Please kindly carefully read the context and requirements below before posting an answer/comment:</h4>
<p><strong>Context:</strong> In Thailand, many remote roads linking villages are only suitable for high clearance pickup trucks which are the standard car in mountainous and remote areas. Our recent wiki update says those roads should be tagged as highway=unclassified+surface=unpaved, however, some community members would prefer to keep highway=track+surface=unpaved for safety concerns.</p>
<p>This is purely a rendering concern as most basic renderers will show an unclassified road as paved, but I am always open to new ideas.</p>
<p>The main issue with this change request is that there are often multiple tracks between two villages, and one is clearly used as the main way: it may be partially paved or will be in the future, while other tracks are used only for agricultural purposes and are often in worst conditions or take much longer due to change of elevation. It’s important to know for an end-user where off-road conditions could be but so is knowing what is the main way.</p>
<p>Also, we also have highway=tertiary roads (based on official gov. reference) that are off-road only conditions.</p>
<p><strong>Requirements:</strong> for now the community is very small, so the following tags cannot be used for this purpose:</p>
<ul>
<li>tracktype because it has been abused with completely different interpretations and will require major efforts to clean up</li>
<li>smoothness: too detailed</li>
<li>4wd_only: the great majority of dirt roads in Thailand are not really suitable for a city car, and many high clearance pickup trucks using these roads are not technically 4WD.</li>
</ul>
<p>so looking for other potential simpler ideas, e.g.:</p>
<ul>
<li>convert the unpaved sections to track and keep the paved sections as unclassified ? Since those main tracks have often concrete sections, it might be sufficient to figure them out in the map. Once all the unpaved sections become paved, the unclassified road gets extended automatically.</li>
<li>use a new tag xxxxx=xxxxx with highway=track ?</li>
<li>keep highway=unclassified + surface=unpaved as it is now</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-unclassified" rel="tag" title="see questions tagged &#39;unclassified&#39;">unclassified</span> <span class="post-tag tag-link-4wd" rel="tag" title="see questions tagged &#39;4wd&#39;">4wd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '22, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/e3f994b2488e2182c63a7c44a5028ff6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmoffroad&#39;s gravatar image" />
<p><span>cmoffroad</span><br />
<span class="score" title="205 reputation points">205</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmoffroad has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '22, 11:11</strong> </span></p>
</div>
</div>
<div id="comments-container-83637" class="comments-container">
<span id="83648"></span>
<div id="comment-83648" class="comment">
<div id="post-83648-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Side note : you might want to push for better support of <code>surface</code> tag in common renderers and routers. OsmAnd and OrganicMaps support routing based on unpaved tags. The latter does not render it though AFAIK. openstreetmap-carto has been trying to render it for a loooong time (see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/110">here</a>, you might want to show your support with a +1... :-/).</p>
<p>Best regards.</p>
</div>
<div id="comment-83648-info" class="comment-info">
<span class="comment-age">(04 Mar '22, 17:49)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83662"></span>
<div id="comment-83662" class="comment">
<div id="post-83662-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Added a +1. I am amazed that after all this time, most renderers still show correctly tagged unpaved roads as paved. No wonder that highway=track has been completely misused.</p>
</div>
<div id="comment-83662-info" class="comment-info">
<span class="comment-age">(05 Mar '22, 11:21)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83663"></span>
<div id="comment-83663" class="comment">
<div id="post-83663-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20238/cmoffroad"></a><a href="https://help.openstreetmap.org/users/20238/cmoffroad">@cmoffroad</a> It's actually a difficult problem to solve. If I remember correctly the problem that OSM Carto hit was that it was difficult to introduce a distinction between paved and unpaved roads while still showing the functional difference between them and tracks. If you don't need to show that functional difference it's <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/style.lua#L602">easy</a> to just "render unpaved roads as tracks" but that's unhelpful in places in the world where there are lots of tracks <em>and</em> quite a few unsurfaced main roads.</p>
</div>
<div id="comment-83663-info" class="comment-info">
<span class="comment-age">(05 Mar '22, 12:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="83665"></span>
<div id="comment-83665" class="comment not_top_scorer">
<div id="post-83665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know the code specifics, but in terms of UX using different stroke width/color, it should be possible. I was able to achieve this with my own OSMAnd renderer.</p>
</div>
<div id="comment-83665-info" class="comment-info">
<span class="comment-age">(05 Mar '22, 12:25)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83666"></span>
<div id="comment-83666" class="comment not_top_scorer">
<div id="post-83666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am tempted to go back to highway=track, because there are not so many of those and only end-users for those are off-road enthusiasts using basic renderers.</p>
</div>
<div id="comment-83666-info" class="comment-info">
<span class="comment-age">(05 Mar '22, 12:26)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83670"></span>
<div id="comment-83670" class="comment">
<div id="post-83670-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20238/cmoffroad">@cmoffroad</a></p>
<p>Respectfully, you've got to separate the rendering issue from developing criteria we should use to tag highways. Ideally, considerations of how something is rendered in this app or on that device should have nothing whatever to do with the nature of the data we collect for OSM. Ideally.</p>
<p>If we could come to a consensus about how best to tag tracks and unclassified highways, we'd go a long way towards setting this problem aside. But, it's OSM and everybody feels free to do it their own way. I'm guilty of that as well as others.</p>
<p>Also, it's a difficult question because in order to answer it a mapper has to make a subjective decision. IMO, this is a track; no, IMO, this is an unpaved unclassified highway. Check the Wiki. Is there a useful and clear description of how to tag them? If not, then that's where the work needs to be done, IMO.</p>
<p>I applaud you for taking this on and working to improve our thinking about it.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div id="comment-83670-info" class="comment-info">
<span class="comment-age">(05 Mar '22, 15:07)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="83686"></span>
<div id="comment-83686" class="comment not_top_scorer">
<div id="post-83686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/5016/alaskadave"></a><a href="https://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a> :) I understand tagging for the renderer is wrong, and I have moved away from this, but at the same time, most mapping is driven from end-users, and as long as renderers do not take into account basic tag (surface, tracktype, or 4wd_only) for other road classification, mappers will continue abusing highway=track for anything unpaved.</p>
<p>Our recent wiki update is clear on what tag to use for links between settlements (unclassified), and is meant to prevent future conflicts/edit wars, but as you know some mappers have been mapping a certain way for a long time and are reticent or simply against change.</p>
<p>However, when I read their arguments, I can understand part of their frustration, 4WD-only links between settlements are not the norm in Thailand, and maps are heavily relied on by the off-road community, of which I am also trying to bring members to join OSM. Hence the dilemna.</p>
</div>
<div id="comment-83686-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 04:23)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83687"></span>
<div id="comment-83687" class="comment not_top_scorer">
<div id="post-83687-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13231/h_mlet">@H_mlet</a> I would like to compile a list of common renderers/routers and show a table of currently supported tags, and for those missing a link to their technical support so that people can +1. Does this info already exist? If not, would you be interested in helping me compile this?</p>
</div>
<div id="comment-83687-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 04:31)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83693"></span>
<div id="comment-83693" class="comment">
<div id="post-83693-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>as long as renderers do not take into account basic tag (surface, tracktype, or 4wd_only) for other road classification, mappers will continue abusing highway=track for anything unpaved.</p>
</blockquote>
<p><a href="https://help.openstreetmap.org/users/20238/cmoffroad">@cmoffroad</a> For me the main concern if about routing, renderers fell less of a problem IMHO.</p>
</div>
<div id="comment-83693-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 11:31)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83694"></span>
<div id="comment-83694" class="comment not_top_scorer">
<div id="post-83694-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>Does this info already exist?</p>
</blockquote>
<p>In the wiki there are pages of functionalities (<a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">online routers</a>, <a href="https://wiki.openstreetmap.org/wiki/Routing/offline_routers">offline routers</a>) but most of it is incomplete or outdated and does not include the data you're interested in.</p>
<p>For renderers, or more accurately stylesheets, there are some incomplete lists, with not much details. The list of <a href="https://wiki.openstreetmap.org/wiki/Featured_tile_layers">tile layers on osm.org</a>, some <a href="https://wiki.openstreetmap.org/wiki/Tile_servers">others</a>...</p>
<blockquote>
<p>If not, would you be interested in helping me compile this?</p>
</blockquote>
<p>Well, I'd be happy to help fill the blank for the apps/styles I know about. But unfortunately I don't have time to bootstrap the process. I guess it would mean creating huge lists on the wiki, with proper templating, contacting project maintainer to get data, and so on..</p>
<p>You might want to check the "<a href="https://wiki.openstreetmap.org/wiki/Taginfo/Projects">Projects</a>" tab of taginfo about <a href="https://taginfo.openstreetmap.org/keys/surface#projects">surface tag</a>.</p>
<p>You can contact me through the wiki if you start on this project.</p>
<p>Regards</p>
</div>
<div id="comment-83694-info" class="comment-info">
<span class="comment-age">(06 Mar '22, 11:52)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83779"></span>
<div id="comment-83779" class="comment not_top_scorer">
<div id="post-83779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13231/h_mlet">@H_mlet</a> what is your OSM user id ? I would like to send you a DM.</p>
</div>
<div id="comment-83779-info" class="comment-info">
<span class="comment-age">(10 Mar '22, 08:55)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83784"></span>
<div id="comment-83784" class="comment not_top_scorer">
<div id="post-83784-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>I would like to compile a list of common renderers/routers and show a table of currently supported tags</p>
</blockquote>
<p>Taginfo already has support for this and is used by many projects. See <a href="https://taginfo.openstreetmap.org/projects">https://taginfo.openstreetmap.org/projects</a></p>
</div>
<div id="comment-83784-info" class="comment-info">
<span class="comment-age">(10 Mar '22, 09:34)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="83785"></span>
<div id="comment-83785" class="comment not_top_scorer">
<div id="post-83785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/5/richard">@Richard</a>. Useful site. I was looking more for something less technical/detailed, targeting the most popular outdoor applications and their rendering support (Komoot, strava, alltrails, opentopomap, maps.me...). Didn't find anything yet so working on a new wiki page...</p>
</div>
<div id="comment-83785-info" class="comment-info">
<span class="comment-age">(10 Mar '22, 10:15)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
</div>
<div id="comment-tools-83637" class="comment-tools">
<span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-83637-form-container" class="comment-form-container">
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

<span id="83639"></span>

<div id="answer-container-83639" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83639-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-83639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In short: No, something that is a main road isn't <code>highway=track</code>.</p>
<p>In general tagging for the rendered is <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">strongly discouraged</a>. Some renderers and phone apps absolutely do render additional 'quality' tags including the humanitarian layer on OpenStreetMap.org. Some others will take this into account for routing even if it isn't displayed.</p>
<p>Roads should be tagged according to their use within the road network regardless of surface or smoothness. The surface and smoothness tags should be used to indicate physical characteristics. If they really are agricultural only then they may qualify as track, but a badly maintained part of the road network should still be appropriately tagged as part of the road network.</p>
<p>Unpaved or rutted "real" roads are not unique to Thailand. As a starting point I would suggest following something like the <a href="https://wiki.openstreetmap.org/wiki/Australian_Tagging_Guidelines#Unsealed_and_4wd_Roads_.28Dirt.2C_Gravel.2C_Formed.2C_etc.29">Australian</a> or <a href="https://wiki.openstreetmap.org/wiki/Highway_Tag_Africa">African</a> tagging guidelines which are written with similar issues in mind.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '22, 12:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '22, 12:50</strong> </span></p>
</div>
</div>
<div id="comments-container-83639" class="comments-container">
<span id="83643"></span>
<div id="comment-83643" class="comment">
<div id="post-83643-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the confirmation and the links!</p>
</div>
<div id="comment-83643-info" class="comment-info">
<span class="comment-age">(04 Mar '22, 14:38)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
</div>
<div id="comment-tools-83639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83639-form-container" class="comment-form-container">
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

