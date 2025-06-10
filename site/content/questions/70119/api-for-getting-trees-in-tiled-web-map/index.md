+++
type = "question"
title = "API for getting trees in tiled web map"
description = '''I am looking for an API where I can retrieve the co-ordinates (GeoJson or topojson) of trees (Or POIs which consists of trees) . I want the request to be sent in tiled web map format (ie https://data.osmbuildings.org/0.2/anonymous/tree/15/33187/22545.json something like this). I have checked OSMBuil...'''
date = "2019-07-17T14:59:00Z"
lastmod = "2019-07-22T12:33:00Z"
weight = 70119
keywords = [ "api", "tiles", "pois", "geojson", "trees" ]
aliases = [ "/questions/70119" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [API for getting trees in tiled web map](/questions/70119/api-for-getting-trees-in-tiled-web-map)

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
<span id="post-70119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70119-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for an API where I can retrieve the co-ordinates (GeoJson or topojson) of trees (Or POIs which consists of trees) . I want the request to be sent in tiled web map format (ie <a href="https://data.osmbuildings.org/0.2/anonymous/tree/15/33187/22545.json">https://data.osmbuildings.org/0.2/anonymous/tree/15/33187/22545.json</a> something like this). I have checked OSMBuildings it doesn't have details of trees.</p>
<pre><code>{
    &quot;type&quot;: &quot;FeatureCollection&quot;,
    &quot;features&quot;: [
        {
            &quot;id&quot;: &quot;Id&quot;,
            &quot;type&quot;: &quot;Feature&quot;,
            &quot;properties&quot;: {
                &quot;type&quot;: &quot;tree&quot;
            },
            &quot;geometry&quot;: {
                &quot;type&quot;: &quot;Point&quot;,
                &quot;coordinates&quot;: [
                        [
                            13.420876,
                            52.53766
                        ]
                ]
            }
        }
    ]
}</code></pre>
<p>I am expecting this kind of response from the server</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-pois" rel="tag" title="see questions tagged &#39;pois&#39;">pois</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span> <span class="post-tag tag-link-trees" rel="tag" title="see questions tagged &#39;trees&#39;">trees</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '19, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/b2a848310ef5f6fccb46794b8d4ac5de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aravinda_b&#39;s gravatar image" />
<p><span>aravinda_b</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aravinda_b has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '19, 08:42</strong> </span></p>
</div>
</div>
<div id="comments-container-70119" class="comments-container">
<span id="70120"></span>
<div id="comment-70120" class="comment">
<div id="post-70120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You seem to have conflicting requests. Do you want to get raw data for the trees, or rendered image tiles? If you want the raw data, then you'll have to use whatever syntax the given API expects, which almost certainly won't be the Slippy Map syntax.</p>
</div>
<div id="comment-70120-info" class="comment-info">
<span class="comment-age">(17 Jul '19, 16:59)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="70121"></span>
<div id="comment-70121" class="comment">
<div id="post-70121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd be really suprised if there was an off-the-shelf server that provided what you want. I'm sure that you can download OSM data and extract what you want, though, or use <a href="https://overpass-turbo.eu/s/KOH">overpass</a> to obtain it for a particular area.</p>
</div>
<div id="comment-70121-info" class="comment-info">
<span class="comment-age">(17 Jul '19, 17:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70123"></span>
<div id="comment-70123" class="comment">
<div id="post-70123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks to alester and SomeoneElse for responding. I have updated question with sample response. This makes solves the confusion i guess.</p>
</div>
<div id="comment-70123-info" class="comment-info">
<span class="comment-age">(18 Jul '19, 08:22)</span> <span class="comment-user userinfo">aravinda_b</span>
</div>
</div>
</div>
<div id="comment-tools-70119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70119-form-container" class="comment-form-container">
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

<span id="70131"></span>

<div id="answer-container-70131" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70131-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's the <a href="http://www.opentrees.org/">OpenTrees</a> site which seems to do what you are seeking as an end product. The code is viewable <a href="https://github.com/stevage/opentrees">here</a>, this might help you set up your own project.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '19, 01:39</strong></p>
<img src="https://secure.gravatar.com/avatar/109b4b042580ca2017fb1f29d0602e71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philam48&#39;s gravatar image" />
<p><span>philam48</span><br />
<span class="score" title="86 reputation points">86</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philam48 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70131" class="comments-container">
<span id="70156"></span>
<div id="comment-70156" class="comment">
<div id="post-70156-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you but that doesn't have data of my region</p>
</div>
<div id="comment-70156-info" class="comment-info">
<span class="comment-age">(22 Jul '19, 12:33)</span> <span class="comment-user userinfo">aravinda_b</span>
</div>
</div>
</div>
<div id="comment-tools-70131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70131-form-container" class="comment-form-container">
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

