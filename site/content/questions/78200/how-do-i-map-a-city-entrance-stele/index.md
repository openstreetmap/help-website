+++
type = "question"
title = "How do I map a city entrance stele?"
description = '''How would you map an object like this? Or this? Or this? Or this? These are city entrance steles. They can take all forms, shapes and sizes. One can be only 2 m tall, the other one would be 20 m. Can&#x27;t say for other countries, but these are popular in ex-USSR countries. Like, they&#x27;re in most cities ...'''
date = "2021-01-03T00:45:00Z"
lastmod = "2021-01-04T04:23:00Z"
weight = 78200
keywords = [ "information", "zoom", "tagging" ]
aliases = [ "/questions/78200" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I map a city entrance stele?](/questions/78200/how-do-i-map-a-city-entrance-stele)

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
<span id="post-78200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would you map an object like <a href="https://thumbs.dreamstime.com/z/stele-entrance-to-city-zadonsk-russia-october-contains-name-emblem-69394945.jpg">this</a>? Or <a href="https://upload.wikimedia.org/wikipedia/commons/e/e6/Stele_%28Novy_Urengoy%29.jpg">this</a>? Or <a href="https://severpost.ru/docs/upload/2016/09/1475240178.jpg">this</a>? Or <a href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcCSwX5VZu6u1aYOGBOeXsLtO4E7kQ9WRklQ&amp;usqp=CAU">this</a>?</p>
<p>These are city entrance steles. They can take all forms, shapes and sizes. One can be only 2 m tall, the other one would be 20 m. Can't say for other countries, but these are popular in ex-USSR countries. Like, they're in most cities and some towns or villages.</p>
<p>These kinds of steles have a name of the settlement where they're placed, and every driver entering the settlement would easily see them.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/RU:Как_обозначить#.D0.9F">Russian guide</a> suggests to use <code>tourism=information, information=stele</code> tags. But the problem is, the <code>tourism=information</code>-tagged objects, with a few exceptions, are only shown at <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/style/amenity-points.mss">zoom level 19</a>:</p>
<p><code>[feature = 'tourism_information'][zoom &gt;= 19], [feature = 'tourism_information']["information"='office'][zoom &gt;= 17] { marker-file: url('symbols/tourism/information.svg'); [information = 'audioguide'] { marker-file: url('symbols/tourism/audioguide.svg'); } [information = 'board'] { marker-file: url('symbols/tourism/board.svg'); } [information = 'guidepost'] { marker-file: url('symbols/tourism/guidepost.svg'); } [information = 'office'] { marker-file: url('symbols/tourism/office.svg'); marker-fill: @amenity-brown; } [information = 'map'], [information = 'tactile_map'] { marker-file: url('symbols/tourism/map.svg'); } [information = 'terminal'] { marker-file: url('symbols/tourism/terminal.svg'); } marker-fill: </code><a href="https://help.openstreetmap.org/users/13096/man"><code>@man</code></a><code>-made-icon; marker-clip: false; }</code></p>
<p>I don't think I should zoom to the level 19 to see an object that is, in reality, 12 m tall and is a landmark (I think, they should be shown at level 15), so I think a different category should be used. It could be <code>man_made=obelisk</code>, <code>landmark=pillar</code>, and even <code>landmark=large_rock</code>, but not always. Also, these don't show its purpose. It's not a monument either.</p>
<p>How am I supposed to mark such objects?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-information" rel="tag" title="see questions tagged &#39;information&#39;">information</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '21, 00:45</strong></p>
<img src="https://secure.gravatar.com/avatar/971622e9190841fe0acdf9a5fb8b46ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="efpies&#39;s gravatar image" />
<p><span>efpies</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="efpies has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '21, 00:47</strong> </span></p>
</div>
</div>
<div id="comments-container-78200" class="comments-container">
<span id="78216"></span>
<div id="comment-78216" class="comment">
<div id="post-78216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Am I correct in thinking these are rather large <a href="https://wiki.openstreetmap.org/wiki/Tag:traffic_sign%3Dcity_limit">city limit</a> signs? Las Vegas's famous sign seems to just be tagged as a tourist attraction in OSM.</p>
</div>
<div id="comment-78216-info" class="comment-info">
<span class="comment-age">(04 Jan '21, 04:23)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-78200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78200-form-container" class="comment-form-container">
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

<span id="78206"></span>

<div id="answer-container-78206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78206-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi efpies, the used terms look right. But your suggestion to change the key to get a better / earlier view on a map looks like tagging for the renderer. You can do a lot with OSM data, but tagging for the renderer is not done. Ps you could see them as monuments in/of time PPS did you post this also at the "Russian"(USSR) fora, its a concern of all those communities.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '21, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-78206" class="comments-container">
&#10;</div>
<div id="comment-tools-78206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78206-form-container" class="comment-form-container">
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

