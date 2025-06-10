+++
type = "question"
title = "Street with No Way"
description = '''Would someone please help me understand what&#x27;s happening here: www.openstreetmap.org/?lon=-117.62042&amp;amp;lat=33.46172?  If you zoom all the way in there, in the &quot;Standard&quot; view, you see that Camino Vera Cruz changes color between Carretera and Costero Risco. However, if you zoom out at all, Camino V...'''
date = "2012-07-31T03:17:00Z"
lastmod = "2012-08-01T02:43:00Z"
weight = 14712
keywords = [ "newbie" ]
aliases = [ "/questions/14712" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Street with No Way](/questions/14712/street-with-no-way)

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
<span id="post-14712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14712-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Would someone please help me understand what's happening here: <a href="http://www.openstreetmap.org/?lon=-117.62042&amp;lat=33.46172">www.openstreetmap.org/?lon=-117.62042&amp;lat=33.46172</a>?<br />
</p>
<p>If you zoom all the way in there, in the "Standard" view, you see that Camino Vera Cruz changes color between Carretera and Costero Risco. However, if you zoom out at all, Camino Vera Cruz appears to end there. The street continues west as shown when you are zoomed all the way in (or in the other views). If you "Browse Map Data," it shows that the way ends at that point. It still shows nodes to the west and even draws the outline of the street if you're zoomed in all the way, but the way ends. Same thing in Edit view; the nodes are there but no way.</p>
<p>I have some tiles from a couple of months ago that show the entirety of Camino Vera Cruz, so I know it used to be there. When I view the history of the area, I don't see it being deleted. Can we tell where it went?</p>
<p>I was doing some editing a little farther north and I noticed that <a href="http://www.openstreetmap.org/?lon=-117.62844&amp;lat=33.47836">Camino de los Mares</a> had the same issue out at its northern end. I thought I might have damaged it accidentally, so I added it back in. But I wasn't doing anything around Vera Cruz.</p>
<p>Thanks for helping!</p>
<p>Rex</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '12, 03:17</strong></p>
<img src="https://secure.gravatar.com/avatar/1bf03822033b29eb90fd19e767c5dda8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RexTCA&#39;s gravatar image" />
<p><span>RexTCA</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RexTCA has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-14712" class="comments-container">
&#10;</div>
<div id="comment-tools-14712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14712-form-container" class="comment-form-container">
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

<span id="14714"></span>

<div id="answer-container-14714" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14714-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to the <a href="http://tools.geofabrik.de/osmi/?view=redactionbot&amp;lon=-117.62351&amp;lat=33.46347&amp;zoom=17&amp;overlays=overview,bot_point_superseded,bot_line_superseded_cp,bot_line_superseded,bot_point_modified,bot_line_modified_cp,bot_line_modified,bot_point_deleted,bot_line_deleted_cp,bot_line_deleted">OSMI redaction bot view</a> the Camino Vera Cruz road has been deleted by the <a href="http://blog.osmfoundation.org/2012/07/09/licence-redaction-ready/">redaction bot</a>. I don't know why this road is still visible in the <a href="http://www.openstreetmap.org/?lat=33.462602&amp;lon=-117.621488&amp;zoom=18&amp;layers=M">highest zoom level</a>, might just be a rendering bug. However, after I triggered a re-render of <a href="http://c.tile.openstreetmap.org/18/45422/105189.png">one of the tiles</a> (see the <a href="http://wiki.openstreetmap.org/wiki/Slippy_Map#Mapnik_tile_rendering">Slippy Map wiki page</a> or <a href="http://help.openstreetmap.org/questions/1049/how-to-trigger-a-repaint-for-a-specific-osm-map-tile">this question</a> for information how to do this) the road disappeared. So the tile still wasn't up to date.</p>
<p>I cannot see any problem with <a href="http://www.openstreetmap.org/?lat=33.479378&amp;lon=-117.627892&amp;zoom=18&amp;layers=M">Camino de los Mares</a> though, except that there is an overlapping <em>highway=proposed</em> road which should be fixed and the highway=path may miss a connection with the residential road. Maybe there has been a similar problem in the past but the tiles have been re-rendered meanwhile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '12, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '12, 07:41</strong> </span></p>
</div>
</div>
<div id="comments-container-14714" class="comments-container">
<span id="14715"></span>
<div id="comment-14715" class="comment">
<div id="post-14715-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can see some of it at full zoom. Oddly different bits to what I can see in Potlach2. The main thing to do (as bing? is so good) is to remap it, I was tempted but without a little local knowledge it's best to leave it to some one on the ground to confirm it.</p>
</div>
<div id="comment-14715-info" class="comment-info">
<span class="comment-age">(31 Jul '12, 08:24)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="14739"></span>
<div id="comment-14739" class="comment">
<div id="post-14739-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ah, my paranoid worries about disappearing data were well founded! Many thanks for your explanation and helpful links. I guess I must have been living in a hole to not know of this deletion bot. Now, on to the repairs!</p>
<p>Rex</p>
</div>
<div id="comment-14739-info" class="comment-info">
<span class="comment-age">(01 Aug '12, 02:43)</span> <span class="comment-user userinfo">RexTCA</span>
</div>
</div>
</div>
<div id="comment-tools-14714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14714-form-container" class="comment-form-container">
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

