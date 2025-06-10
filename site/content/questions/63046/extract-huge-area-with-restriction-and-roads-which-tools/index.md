+++
type = "question"
title = "Extract huge area with restriction and roads → which tools ?"
description = '''It&#x27;s been few weeks since i&#x27;m searching for a proper way to extract data from OSM. For the most part, i wanna work with data like big roads and restriction in order to do some path finding.  Currently, i&#x27;m using Postgis, Qgis for the database and the visualisation and i&#x27;m extracting data from geofab...'''
date = "2018-04-19T14:47:00Z"
lastmod = "2018-04-19T16:04:00Z"
weight = 63046
keywords = [ "restrictions", "area" ]
aliases = [ "/questions/63046" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extract huge area with restriction and roads → which tools ?](/questions/63046/extract-huge-area-with-restriction-and-roads-which-tools)

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
<span id="post-63046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63046-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It's been few weeks since i'm searching for a proper way to extract data from OSM. For the most part, i wanna work with data like big roads and restriction in order to do some path finding.</p>
<p>Currently, i'm using Postgis, Qgis for the database and the visualisation and i'm extracting data from geofabrik and overpass turbo. Geofabrik is being used thanks its big area that it offers and I did add restrictions column in by DB from overpass because i didn't find any in the shapefile uploaded by geofrabrik. Am I missing something with restriction in geofrabik ? If not, since the area should constantly change, I'd like a tool which can in one hand download huge area and in the other hand give be those restrictions so i don't have to merge data from geofrabrik and overpass.</p>
<p>• JOSM can't load a big enough area</p>
<p>• Mercaartor too</p>
<p>Thanks for your help !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '18, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/4b8dd060e17c162b72fa7b3802259eed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StillSomebodyElse&#39;s gravatar image" />
<p><span>StillSomebod...</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StillSomebodyElse has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63046" class="comments-container">
<span id="63047"></span>
<div id="comment-63047" class="comment">
<div id="post-63047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What format do you want the restrictions in? Raw OSM relations, or ...?</p>
</div>
<div id="comment-63047-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 15:08)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63048"></span>
<div id="comment-63048" class="comment">
<div id="post-63048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want the restriction to be in my data base. As a shapefile would be great (I hope I have answered correctly)</p>
</div>
<div id="comment-63048-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 15:47)</span> <span class="comment-user userinfo">StillSomebod...</span>
</div>
</div>
<span id="63049"></span>
<div id="comment-63049" class="comment">
<div id="post-63049-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But currently you have fetched the restriction from Overpass and then how did you get it into your database?</p>
</div>
<div id="comment-63049-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 15:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63050"></span>
<div id="comment-63050" class="comment">
<div id="post-63050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>With a python file that i wrote. It read Json from overpass, test if it's in the DB and if so it insert in a table</p>
</div>
<div id="comment-63050-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 16:04)</span> <span class="comment-user userinfo">StillSomebod...</span>
</div>
</div>
</div>
<div id="comment-tools-63046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63046-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

