+++
type = "question"
title = "Exporting entire railway network"
description = '''I need to export entire world railway network from planet file. I want to store them in PosGis database as collection of points and lines. I would like to simplify she shapes and remove parallel lines (in case of multiple tracks) In case of stations I need always to have point (even if in original i...'''
date = "2018-08-26T13:47:00Z"
lastmod = "2018-08-27T00:30:00Z"
weight = 65564
keywords = [ "railway", "export" ]
aliases = [ "/questions/65564" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting entire railway network](/questions/65564/exporting-entire-railway-network)

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
<span id="post-65564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65564-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to export entire world railway network from planet file. I want to store them in PosGis database as collection of points and lines. I would like to simplify she shapes and remove parallel lines (in case of multiple tracks) In case of stations I need always to have point (even if in original it is shape). I made some experiments with osmium but without success - I don't know how to merge all tags relations and ways into lines. Any advice</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '18, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/89c7b259f5dd9b117ae43fab4c037814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jkan997&#39;s gravatar image" />
<p><span>jkan997</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jkan997 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Aug '18, 21:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-65564" class="comments-container">
<span id="65565"></span>
<div id="comment-65565" class="comment">
<div id="post-65565-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is using osmium a requirement or would some other tool also be fine for you?</p>
</div>
<div id="comment-65565-info" class="comment-info">
<span class="comment-age">(26 Aug '18, 15:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="65567"></span>
<div id="comment-65567" class="comment">
<div id="post-65567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any free tool that will handle planet XML is fine.</p>
</div>
<div id="comment-65567-info" class="comment-info">
<span class="comment-age">(26 Aug '18, 20:25)</span> <span class="comment-user userinfo">jkan997</span>
</div>
</div>
<span id="65568"></span>
<div id="comment-65568" class="comment">
<div id="post-65568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>okay, I have made your question's tags less specific to osmium. Since only the railway network is quite sparse data, I guess that going via Overpass API (instead of the full planet) might be a better option. But I neither know osmium nor the Overpass query languages good enough to help any further.</p>
</div>
<div id="comment-65568-info" class="comment-info">
<span class="comment-age">(26 Aug '18, 21:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="65570"></span>
<div id="comment-65570" class="comment">
<div id="post-65570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Osmium is quite straightforward. You might just pick every tag you need, for example water-related I needed:</p>
<p>osmium tags-filter -o planet-water.osm.pbf planet-latest.osm.pbf natural=water landuse=reservoir landuse=basin waterway=dock</p>
<p>It can also do much more complex things, see the documentation:</p>
<p><a href="https://osmcode.org/osmium-tool/manual.html">https://osmcode.org/osmium-tool/manual.html</a></p>
</div>
<div id="comment-65570-info" class="comment-info">
<span class="comment-age">(27 Aug '18, 00:30)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
</div>
<div id="comment-tools-65564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65564-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

