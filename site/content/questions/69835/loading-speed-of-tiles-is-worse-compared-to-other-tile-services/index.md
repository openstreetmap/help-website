+++
type = "question"
title = "loading speed of tiles is worse compared to other tile services"
description = ''' Why is it taking 1 second of loading when for example ArcGIS tiles only need 50 miliseconds? A strange behaviour is also that the image got shown 3/4 but for the rest it takes up to 1 second to show the missing 1/4. Are there some bottlenecks with redirecting in the background of the server? OSM ti...'''
date = "2019-07-02T08:03:00Z"
lastmod = "2019-07-03T08:01:00Z"
weight = 69835
keywords = [ "loading", "tiles", "slow", "tileserver" ]
aliases = [ "/questions/69835" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [loading speed of tiles is worse compared to other tile services](/questions/69835/loading-speed-of-tiles-is-worse-compared-to-other-tile-services)

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
<span id="post-69835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69835-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="https://help.openstreetmap.org/upfiles/osm_vs_arcgis_u5MThjs.png" alt="alt text" /></p>
<p>Why is it taking 1 second of loading when for example ArcGIS tiles only need 50 miliseconds? A strange behaviour is also that the image got shown 3/4 but for the rest it takes up to 1 second to show the missing 1/4. Are there some bottlenecks with redirecting in the background of the server?</p>
<p><a href="https://a.tile.openstreetmap.org/9/255/169.png">OSM tile</a></p>
<p><a href="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/9/255/169">ArcGIS tile</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-loading" rel="tag" title="see questions tagged &#39;loading&#39;">loading</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '19, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d90c2554287e3053dbc40af38bd79316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="black_gis&#39;s gravatar image" />
<p><span>black_gis</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="black_gis has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '19, 08:17</strong> </span></p>
</div>
</div>
<div id="comments-container-69835" class="comments-container">
<span id="69836"></span>
<div id="comment-69836" class="comment">
<div id="post-69836-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you say what "it" is? At a guess, you're trying to load OSM's "standard" tile layer as a background layer into some other software, but it would help to know what you're actually trying to do.</p>
</div>
<div id="comment-69836-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 08:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69838"></span>
<div id="comment-69838" class="comment">
<div id="post-69838-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does it really matter if i use it in a app or not (question ;-) ), because the behaviour is the same (chrome dev tools), thats why i came up with a speedtest of indiviual tiles, secondly yes of course in an basemap but because the paning took ages, compared to all the other services i included, i speedtested the tiles.</p>
</div>
<div id="comment-69838-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 08:24)</span> <span class="comment-user userinfo">black_gis</span>
</div>
</div>
<span id="69840"></span>
<div id="comment-69840" class="comment">
<div id="post-69840-score" class="comment-score">
2
</div>
<div class="comment-text">
<blockquote>
<p>Does it really matter if i use it in a app or not</p>
</blockquote>
<p>It will, because depending on how you load tiles they might not work at all. Some people have complained recently that OSM tiles have "stopped working" for them; generally that was because the frameworks they were using weren't following <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> .</p>
</div>
<div id="comment-69840-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 08:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69843"></span>
<div id="comment-69843" class="comment">
<div id="post-69843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, understood!</p>
<p>But 'OpenStreetMap data is free for everyone to use. Our tile servers are not.' where to buy then? For whom is it free?</p>
<p>when I load a tile in a webbrowser i am 'Note: modern web browsers in standard configuration generally pass all the above technical requirements.', so there should be no issue, but which clutter is then added to the image that makes it load so long -it is a technical interesst not so much a politcal or economical question</p>
<p>I really just want to improve the service with the question, i don't have bad intentions, and it is also a plus for the mappers if the tiles load faster when the pan in the osm editors</p>
</div>
<div id="comment-69843-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 09:01)</span> <span class="comment-user userinfo">black_gis</span>
</div>
</div>
</div>
<div id="comment-tools-69835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69835-form-container" class="comment-form-container">
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

<span id="69846"></span>

<div id="answer-container-69846" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69846-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="black_gis has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tiles served from tile.openstreetmap.org are <em>intentionally</em> prioritised for users of the www.openstreetmap.org website.</p>
<p>If you use them in other contexts, the tiles will still be served, just more slowly.</p>
<p>Tileserver load has increased in recent months, particularly from apps and high-traffic websites which have the resources to set up their own servers but are not doing so. This policy helps encourage those apps and sites to move towards their own servers, while still allowing small-scale uses to benefit from the OSM tileservers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '19, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-69846" class="comments-container">
<span id="69853"></span>
<div id="comment-69853" class="comment">
<div id="post-69853-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thy, now finally my impression of an artificial delay got confirmed and it seems to be a feature than a bug. Fully understandable now why this needs to happen, unfortunately.</p>
</div>
<div id="comment-69853-info" class="comment-info">
<span class="comment-age">(03 Jul '19, 08:01)</span> <span class="comment-user userinfo">black_gis</span>
</div>
</div>
</div>
<div id="comment-tools-69846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69846-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69837"></span>

<div id="answer-container-69837" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69837-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe it is because the OSM tile servers are run on a shoestring budget by a tiny group of volunteers and other tile services are run by teams of admins with the huge budget of multibillion-dollar companies?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '19, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-69837" class="comments-container">
<span id="69839"></span>
<div id="comment-69839" class="comment">
<div id="post-69839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As i said the delivery would be as fast as the ESRI (3/4)50ms (look at the image - blue line!) but for what reason it makes somewhere an extra turn that take up to 1sec to get all loaded</p>
</div>
<div id="comment-69839-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 08:29)</span> <span class="comment-user userinfo">black_gis</span>
</div>
</div>
</div>
<div id="comment-tools-69837" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69837-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69841"></span>

<div id="answer-container-69841" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69841-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To address the implicit point in the title - the tiles you're trying to load are <em>not</em> a tile service. OpenStreetMap is basically just a big pile of data. The tiles that you see at <a href="https://openstreetmap.org"></a><a href="https://openstreetmap.org">https://openstreetmap.org</a> are primarily there to help OSM's mappers improve that data.</p>
<p>If you want to create your own tiles from OSM data then by all means do so (creating some identical tiles <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">isn't particularly difficult</a>), or you're welcome to use other tile services based on OSM data, provided you follow their terms of use, whatever those might be.</p>
<p>Ultimately servers cost money to run and so anyone hosting free map tiles of any sort on the internet will have some sort of "anti bulk use" policy in place.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '19, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69841" class="comments-container">
<span id="69842"></span>
<div id="comment-69842" class="comment">
<div id="post-69842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You have missed my question. Its not about cost and not about self building, that can be an extra steps in the future. I am self very active on OSM and i know that for sure that nothing is for free, unfortuantelly but in dev time i am not concerning about these issues as it comes later.</p>
<p>They are both TMS - pls my question is a technical question and is asking where the extra loading time (look now finally on the image to the blue line) is coming from? Is it this bulk detektor?</p>
</div>
<div id="comment-69842-info" class="comment-info">
<span class="comment-age">(02 Jul '19, 08:55)</span> <span class="comment-user userinfo">black_gis</span>
</div>
</div>
</div>
<div id="comment-tools-69841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69841-form-container" class="comment-form-container">
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

