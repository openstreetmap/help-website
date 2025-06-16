+++
type = "question"
title = "How to obtain administrative boundaries within a higher level in Overpass Turbo"
description = '''I have admin_level=8 for South Oxfordshire District. I wish to obtain admin_level=10 civil parishes within that boundary.'''
date = "2017-10-23T13:01:00Z"
lastmod = "2020-04-27T07:05:00Z"
weight = 60241
keywords = [ "within", "overpass-turbo" ]
aliases = [ "/questions/60241" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to obtain administrative boundaries within a higher level in Overpass Turbo](/questions/60241/how-to-obtain-administrative-boundaries-within-a-higher-level-in-overpass-turbo)

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
<span id="post-60241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60241-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have admin_level=8 for South Oxfordshire District. I wish to obtain admin_level=10 civil parishes within that boundary.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-within" rel="tag" title="see questions tagged &#39;within&#39;">within</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '17, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60241" class="comments-container">
&#10;</div>
<div id="comment-tools-60241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60241-form-container" class="comment-form-container">
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

<span id="60243"></span>

<div id="answer-container-60243" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60243-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think this should do it:</p>
<p><a href="http://overpass-turbo.eu/s/sy3">http://overpass-turbo.eu/s/sy3</a></p>
<p>For queries like <code>in South Oxfordshire</code>, Overpass Turbo looks up the name using the service at <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a>. It takes the first result, which for "South Oxfordshire District" is not the area you want to search in: <a href="http://nominatim.openstreetmap.org/search.php?q=South+Oxfordshire+District&amp;polygon_geojson=1&amp;viewbox=">http://nominatim.openstreetmap.org/search.php?q=South+Oxfordshire+District&amp;polygon_geojson=1&amp;viewbox=</a></p>
<p>Here removing "district" does the trick. Overpass API also has some ways of retrieving an area created from a specific OpenStreetMap feature: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29</a></p>
<p>So <code>area(3600299097)-&gt;.searchArea;</code> or <code>area[admin_level=8][name="South Oxfordshire"]-&gt;.searchArea;</code> should also work to retrieve the area. These methods can be useful if Nominatim doesn't match a search or to move the query out of Overpass Turbo.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '17, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-60243" class="comments-container">
<span id="60246"></span>
<div id="comment-60246" class="comment">
<div id="post-60246-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Max</p>
<p>I thank you for your prompt and informative reply.</p>
<p>I realised my post should have read "admin_level"=8 and name="South Oxfordshire", and wanted to edit it but your reply beat me to it. Running your suggestion gives me a result but there are straight lines connecting certain points in addition to the boundaries themselves. The appearance is a mixture of white and yellow areas, suggesting some sort of overlap. This is the same result as I have achieved, myself, which is why I asked the question. Copying the result as a .kml file into uMap replicates all lines. Opening an exported and saved .kml file into JOSM displays the boundaries alone, however. Importing that saved .kml file into uMap gives the same result as copying it.</p>
<p>Looking into it further, my impression is this: each admin level 10 boundary is formed of a number of sections, as we contributors choose. The straight lines appear to run between the ends of such sections, when I view and select sections in JOSM.</p>
</div>
<div id="comment-60246-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 16:33)</span> <span class="comment-user userinfo">silver mapper</span>
</div>
</div>
<span id="60247"></span>
<div id="comment-60247" class="comment">
<div id="post-60247-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I expect the tools you are using expect the relations to be in a certain order, which isn't something OSM has treated as important.</p>
<p>You can use <a href="http://overpass-turbo.eu/s/syd">http://overpass-turbo.eu/s/syd</a> to download the OSM data directly into JOSM and see that it is able to process the areas reasonably. The relation editor window also has a feature where it visualizes how the ways are connected.</p>
<p>If you are looking for a KML file, the easiest solution is probably <code>out geom;</code> which will cause Overpass API to generate the areas (instead of Overpass Turbo): <a href="http://overpass-turbo.eu/s/sye">http://overpass-turbo.eu/s/sye</a></p>
</div>
<div id="comment-60247-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 16:58)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="60249"></span>
<div id="comment-60249" class="comment">
<div id="post-60249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Max</p>
<p>Between times, I thought the result was because the administrative boundaries are not closed ways.</p>
<p>I thank you for your further information and help, and <a href="http://overpass-turbo.eu/s/sye">http://overpass-turbo.eu/s/sye</a> does give me what I seek, indeed. This answers my post.</p>
</div>
<div id="comment-60249-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 18:24)</span> <span class="comment-user userinfo">silver mapper</span>
</div>
</div>
<span id="74389"></span>
<div id="comment-74389" class="comment">
<div id="post-74389-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi there, I want to get the city, district and Xian boundaries on that website too. I'm allergic to code, tried change number 10 to 5 in your link but not work. I want to draw the city, district, and County(Xian in China) level boundaries of those cities: Shanghai, Suzhou, Wuxi, Changzhou, Huzhou, Jiaxing, Hangzhou, Shaoxing and Ningbo. Please help. What should I code to achieve that, please</p>
</div>
<div id="comment-74389-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 03:53)</span> <span class="comment-user userinfo">CliffHU</span>
</div>
</div>
<span id="74392"></span>
<div id="comment-74392" class="comment">
<div id="post-74392-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18244/cliffhu">@CliffHU</a>, please ask a new question. Do not use comments to ask new questions.</p>
</div>
<div id="comment-74392-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 04:36)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="74397"></span>
<div id="comment-74397" class="comment not_top_scorer">
<div id="post-74397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, please check the QS here: <a href="/questions/74396/overpass-draw-multiple-cities-with-district-boundaries-to-calculate-population-in-driving-range">https://help.openstreetmap.org/questions/74396/overpass-draw-multiple-cities-with-district-boundaries-to-calculate-population-in-driving-range</a></p>
</div>
<div id="comment-74397-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 07:05)</span> <span class="comment-user userinfo">CliffHU</span>
</div>
</div>
</div>
<div id="comment-tools-60243" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-60243-form-container" class="comment-form-container">
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

