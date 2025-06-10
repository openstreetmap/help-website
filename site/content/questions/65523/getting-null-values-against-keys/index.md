+++
type = "question"
title = "Getting null values against keys ?"
description = '''Thank you for providing osm cake, that is wonderful an offer. Attempted to read india-latest.osm.pbf to .csv file using osmconvert.exe. Built structure with following keys: addr:street addr:postcode addr:district addr:subdistrict addr:state addr:country @id @lat @lon The outcome showed values only f...'''
date = "2018-08-23T05:34:00Z"
lastmod = "2018-08-25T04:54:00Z"
weight = 65523
keywords = [ "osmconvert", "csv", "key" ]
aliases = [ "/questions/65523" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting null values against keys ?](/questions/65523/getting-null-values-against-keys)

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
<span id="post-65523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65523-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Thank you for providing osm cake, that is wonderful an offer.</p>
<p>Attempted to read india-latest.osm.pbf to .csv file using osmconvert.exe. Built structure with following keys: addr:street addr:postcode addr:district addr:subdistrict addr:state addr:country <a href="https://help.openstreetmap.org/users/260/idoneus"></a><a href="https://help.openstreetmap.org/users/260/idoneus">@id</a></a> <a href="https://help.openstreetmap.org/users/5110/latroc"></a><a href="https://help.openstreetmap.org/users/5110/latroc">@lat</a></a> <a href="https://help.openstreetmap.org/users/1350/longestaugust"></a><a href="https://help.openstreetmap.org/users/1350/longestaugust">@lon</a></a></p>
<p>The outcome showed values only for three keys: id, latitude, longitude. The rest were null. Need your support to know the reason for null output and how get value instead.</p>
<p>The command used in osmconvert.exe is given below osmconvert india-latest.osm.pbf --csv="addr:street addr:postcode addr:district addr:subdistrict addr:state addr:country <a href="https://help.openstreetmap.org/users/260/idoneus"></a><a href="https://help.openstreetmap.org/users/260/idoneus">@id</a></a> <a href="https://help.openstreetmap.org/users/5110/latroc"></a><a href="https://help.openstreetmap.org/users/5110/latroc">@lat</a></a> <a href="https://help.openstreetmap.org/users/1350/longestaugust"></a><a href="https://help.openstreetmap.org/users/1350/longestaugust">@lon</a></a>" -o=indiancountry.csv</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '18, 05:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0ca8644bcdc86534a46ed412bed98874?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbracedevelop&#39;s gravatar image" />
<p><span>mbracedevelop</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbracedevelop has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65523" class="comments-container">
&#10;</div>
<div id="comment-tools-65523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65523-form-container" class="comment-form-container">
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

<span id="65531"></span>

<div id="answer-container-65531" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65531-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not 100% sure how <code>osmconvert</code> works, but I suspect that if there is no tag for those keys, then it will output a null value. So what you're seeing makes sense. Additionally, OSM has plenty of objects that do no have address details, so you might want to filter it first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '18, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-65531" class="comments-container">
<span id="65533"></span>
<div id="comment-65533" class="comment">
<div id="post-65533-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes you will need to filter the data only for those keys: something like : 1. osmconvert india.pbf --out-o5m &gt;india.o5m 2. osmfilter --keep="addr:street"= india.o5m &gt;india.addr.o5m 3. osmconvert to csv.</p>
<p>You will probably need quite a complex filter to cover addresses with only some of the addr:* tags you want. Also if you want pure lat/lon I'd recommend using --all-to-nodes.</p>
</div>
<div id="comment-65533-info" class="comment-info">
<span class="comment-age">(23 Aug '18, 14:35)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="65552"></span>
<div id="comment-65552" class="comment">
<div id="post-65552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tried the script. Displayed error :could not get 183500800 bytes of memory</p>
</div>
<div id="comment-65552-info" class="comment-info">
<span class="comment-age">(25 Aug '18, 04:54)</span> <span class="comment-user userinfo">mbracedevelop</span>
</div>
</div>
</div>
<div id="comment-tools-65531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65531-form-container" class="comment-form-container">
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

