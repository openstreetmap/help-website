+++
type = "question"
title = "Convert ATCO Code to Lat/Lng coordinates?"
description = '''Hi, I have a large set of XML files following the TransXchange data standard. I have created a parser to extract bus stops a bus will run through when making a specific journey. These bus stops are identified by an &#x27;ATCO Code&#x27;. Below is an example of an ATCO Code. 43000804705 Are there any resources...'''
date = "2013-09-23T20:55:00Z"
lastmod = "2013-09-24T10:13:00Z"
weight = 26658
keywords = [ "bus", "atcocode", "transxchange", "coordinates", "busstops" ]
aliases = [ "/questions/26658" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Convert ATCO Code to Lat/Lng coordinates?](/questions/26658/convert-atco-code-to-latlng-coordinates)

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
<span id="post-26658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26658-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have a large set of XML files following the TransXchange data standard. I have created a parser to extract bus stops a bus will run through when making a specific journey. These bus stops are identified by an 'ATCO Code'. Below is an example of an ATCO Code.</p>
<p>43000804705</p>
<p>Are there any resources OpenStreetMap has that will help me convert this code into a set of coordinates? If not and anyone has any ideas as to how I can do this I would really appreciate it. I have about 60 codes to convert and will have many more in the near future so ideally I need something that is fast and easy to use.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-atcocode" rel="tag" title="see questions tagged &#39;atcocode&#39;">atcocode</span> <span class="post-tag tag-link-transxchange" rel="tag" title="see questions tagged &#39;transxchange&#39;">transxchange</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '13, 20:55</strong></p>
<img src="https://secure.gravatar.com/avatar/798374ef5cfa2acd48be598c543fdcd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jskidd3&#39;s gravatar image" />
<p><span>jskidd3</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jskidd3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26658" class="comments-container">
&#10;</div>
<div id="comment-tools-26658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26658-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="26659"></span>

<div id="answer-container-26659" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26659-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The ATCO code is an identifier for bus stops in the <a href="http://wiki.openstreetmap.org/wiki/NaPTAN">NaPTAN</a> database, which has been imported into OSM in parts of the UK. You can search OSM for bus stops with the naptan:AtcoCode tag key that you want, otherwise it should be possible to find the stop in NaPTAN itself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '13, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/8d2104911958906e2105c27461780d2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wynndale&#39;s gravatar image" />
<p><span>Wynndale</span><br />
<span class="score" title="565 reputation points">565</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wynndale has one accepted answer">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '13, 07:28</strong> </span></p>
</div>
</div>
<div id="comments-container-26659" class="comments-container">
<span id="26660"></span>
<div id="comment-26660" class="comment">
<div id="post-26660-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. Would you be able to give me an example of how I can search OSM for the data? I'd really appreciate that as I'm pretty new to it. Ideally I'd need some sort of URL where I can pass the AtcoCode as a parameter? Thanks again</p>
</div>
<div id="comment-26660-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 21:28)</span> <span class="comment-user userinfo">jskidd3</span>
</div>
</div>
<span id="26662"></span>
<div id="comment-26662" class="comment">
<div id="post-26662-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A good place to start is <a href="http://overpass-turbo.eu">http://overpass-turbo.eu</a> .</p>
<p>Try choosing where you are interested in on the map view and edit the script on the left to say: &lt;query type="node"&gt; &lt;has-kv k="naptan:AtcoCode" v="43000804705"/&gt;</p>
<p>and so on.</p>
</div>
<div id="comment-26662-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 21:38)</span> <span class="comment-user userinfo">Wynndale</span>
</div>
</div>
<span id="26663"></span>
<div id="comment-26663" class="comment">
<div id="post-26663-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you know where the bus stops are you can use the Export data link on the left of the map to get an XML extract of the OSM database including coordinates and ATCO codes of bus stops.</p>
</div>
<div id="comment-26663-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 21:45)</span> <span class="comment-user userinfo">Wynndale</span>
</div>
</div>
</div>
<div id="comment-tools-26659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26659-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26661"></span>

<div id="answer-container-26661" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26661-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not OSM data, but you might want to look at the <a href="http://data.gov.uk/dataset/naptan">NaPTAN data</a>. Some of this was imported as a trial into OpenStreetMap and where that has been done the stops may have a naptan:AtcoCode tag, <a href="http://www.openstreetmap.org/browse/node/474890256">such as this one</a>. Where the data has been verified the position is likely to be more accurate than the original NaPTAN data, though their data may well have been updated since the original data was made available and the trial imports were done.</p>
<p>The NaPTAN data states precision of: "+/- 1 metre spatial accuracy of Ordnance Survey Grid Reference" so you may need to convert the grid reference to lat/lon (and then perhaps to WGS84 or whatever you need).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '13, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-26661" class="comments-container">
<span id="26675"></span>
<div id="comment-26675" class="comment">
<div id="post-26675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>automatic coordinate conversion can be done using the excellent proj4 library. There are a lot of proj4 bindings for different languages.</p>
</div>
<div id="comment-26675-info" class="comment-info">
<span class="comment-age">(24 Sep '13, 10:13)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-26661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26661-form-container" class="comment-form-container">
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

