+++
type = "question"
title = "Imagery offset for Oceana county, Michigan (USA)"
description = '''Oceana county in the state of Michigan (USA) coordinates (ll by ur: -86.54,43.47 by -86.05,43.82) is offset to the northwest for the streets compared to imagery and to googlemaps and yahoo: http://sautter.com/map/?zoom=17&amp;amp;lat=43.78148&amp;amp;lon=-86.433&amp;amp;layers=B000000TFFFFFFFF I first wanted to...'''
date = "2011-04-05T22:35:00Z"
lastmod = "2021-11-14T16:34:00Z"
weight = 4285
keywords = [ "street", "offset" ]
aliases = [ "/questions/4285" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Imagery offset for Oceana county, Michigan (USA)](/questions/4285/imagery-offset-for-oceana-county-michigan-usa)

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
<span id="post-4285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4285-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Oceana county in the state of Michigan (USA) coordinates (ll by ur: -86.54,43.47 by -86.05,43.82) is offset to the northwest for the streets compared to imagery and to googlemaps and yahoo: <a href="http://sautter.com/map/?zoom=17&amp;lat=43.78148&amp;lon=-86.433&amp;layers=B000000TFFFFFFFF">http://sautter.com/map/?zoom=17&amp;lat=43.78148&amp;lon=-86.433&amp;layers=B000000TFFFFFFFF</a> I first wanted to report this disparity with the OSM street data within this area and also how could I temporarily patch this data within my OSM postgres database so that this offset is eliminated?</p>
<p>Thanks,</p>
<p>John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-offset" rel="tag" title="see questions tagged &#39;offset&#39;">offset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '11, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/6290d7090ea2280af9ffdc1e300b454e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mitchelljj&#39;s gravatar image" />
<p><span>mitchelljj</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mitchelljj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Apr '11, 00:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-4285" class="comments-container">
<span id="4309"></span>
<div id="comment-4309" class="comment">
<div id="post-4309-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have you already compared the OSM data for the streets AND the aerial photos with exact GPS traces for that area? In some constellations OSM data can be right and only the aerial photos have an offset. Does <a href="https://wiki.openstreetmap.org/wiki/True_Offset_Process">https://wiki.openstreetmap.org/wiki/True_Offset_Process</a> help?</p>
</div>
<div id="comment-4309-info" class="comment-info">
<span class="comment-age">(06 Apr '11, 16:27)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="4311"></span>
<div id="comment-4311" class="comment">
<div id="post-4311-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There aren't a lot of GPS traces there but what there are tend to match Bing (and the other imagery providers he linked to).</p>
<p>The problem seems to be that the Tiger imported data is offset to the NW of everything else. The (small) sample of roads that I looked at seem to be raw Tiger data; so perhaps few local mappers are active? There have been a few POIs added though.</p>
<p>Perhaps this is a good candidate for actually mapping the road grid on the ground before too much other work is done, so that further POIs don't get added relative to the roads in the wrong place.</p>
</div>
<div id="comment-4311-info" class="comment-info">
<span class="comment-age">(06 Apr '11, 16:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-4285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4285-form-container" class="comment-form-container">
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

<span id="82568"></span>

<div id="answer-container-82568" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82568-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a definitive answer to this question there needs to be some reference "ground truth" data on the ground to determine the respective offsets. Comments above note that both the Tiger streets and the satellite images can be offset.</p>
<p>If you are local to the study area it would be useful to collect ground truth data by making multiple accurate GPS traces of the street layout centerlines. Walk the GPS along the central paint stripe - preferably in a quiet street for your own safety. Make sure you have multiple good measurements in both NS and EW directions.</p>
<p>Using the GPS traces of the centerline you can apply corrections to move existing map features like the road network and any other features to their correct positions. The same data can enable offsetting the image of the centerline in photos to match the ground data.</p>
<p>Existing GPS traces on US31 and in Pentwater seem to show that the road positioning in that county is fairly (not precisely) accurate.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '21, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/501b17d27bd2cafce3d62e9705f09e3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cRaIgalLAn&#39;s gravatar image" />
<p><span>cRaIgalLAn</span><br />
<span class="score" title="70 reputation points">70</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cRaIgalLAn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82568" class="comments-container">
&#10;</div>
<div id="comment-tools-82568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82568-form-container" class="comment-form-container">
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

