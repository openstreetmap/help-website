+++
type = "question"
title = "How to make Overpass QL query from local .osm/pbf"
description = '''Hi, I have about 160k WW geo-coordinates and I need some additional information for each lat/lon. Im already create Overpass QL query but it seems thats take a lot of time to make requests via web (overpass-turbo.eu). Is it possible to make such queries locally? Download planet.osm/pbf and execute o...'''
date = "2015-09-18T00:48:00Z"
lastmod = "2015-09-18T15:47:00Z"
weight = 45350
keywords = [ "overpass", "overpass-ql" ]
aliases = [ "/questions/45350" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to make Overpass QL query from local .osm/pbf](/questions/45350/how-to-make-overpass-ql-query-from-local-osmpbf)

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
<span id="post-45350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have about 160k WW geo-coordinates and I need some additional information for each lat/lon. I<code>m already create Overpass QL query but it seems that</code>s take a lot of time to make requests via web (overpass-turbo.eu). Is it possible to make such queries locally? Download planet.osm/pbf and execute overpass ql queries locally using some tools or libs or something similar.</p>
<p>Thanks in advance, Vic</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '15, 00:48</strong></p>
<img src="https://secure.gravatar.com/avatar/964b4e1026e8488babee25c77ff988fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gaploid&#39;s gravatar image" />
<p><span>Gaploid</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gaploid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '15, 06:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45350" class="comments-container">
<span id="45372"></span>
<div id="comment-45372" class="comment">
<div id="post-45372-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/163452/how-to-get-distance-to-different-poi-around-lat-lon">https://gis.stackexchange.com/questions/163452/how-to-get-distance-to-different-poi-around-lat-lon</a></p>
</div>
<div id="comment-45372-info" class="comment-info">
<span class="comment-age">(18 Sep '15, 14:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45350-form-container" class="comment-form-container">
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

<span id="45352"></span>

<div id="answer-container-45352" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45352-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"need some additional information for each lat/lon" is called <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding">reverse geocoding</a> if you mean to get an address/description of the location. Is there a reason for you to use Overpass? Maybe there are faster options. If you really only need reverse geocoding, <a href="/questions/12057/">bulk-geo-coding-of-business-addresses</a> .</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Introduction">https://wiki.openstreetmap.org/wiki/Overpass_API#Introduction</a> for info about the public servers and their capacity/usage policy.</p>
<p>If you want a local instance of Overpass you can get it here <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Developers_.2F_System_Administrators">https://wiki.openstreetmap.org/wiki/Overpass_API#Developers_.2F_System_Administrators</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '15, 06:20</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-45352" class="comments-container">
<span id="45360"></span>
<div id="comment-45360" class="comment">
<div id="post-45360-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer, I need to find distance to different POIs around each lat/lon therefore I don`t need geocoding. Maybe there is a tool like osmosis to make overpass queries locally or the best way to import planet.osm to POSTGIS and make queries there?</p>
</div>
<div id="comment-45360-info" class="comment-info">
<span class="comment-age">(18 Sep '15, 11:43)</span> <span class="comment-user userinfo">Gaploid</span>
</div>
</div>
<span id="45375"></span>
<div id="comment-45375" class="comment">
<div id="post-45375-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>To run Overpass queries locally, you really need to install Overpass API locally. See the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">installation instructions</a> for details. Loading a full planet may take quite a bit more than 24 hours (depends on your HW), maybe check out the 'clone' feature. Once you have the DB available, you can run <code>osm3s_query</code>. Skip the parts for dispatcher, attic and minutely updates. You probably don't want that. If you get lost during the installation, simply ask on the Overpass development list (see Installation page for link).</p>
</div>
<div id="comment-45375-info" class="comment-info">
<span class="comment-age">(18 Sep '15, 15:47)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-45352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45352-form-container" class="comment-form-container">
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

