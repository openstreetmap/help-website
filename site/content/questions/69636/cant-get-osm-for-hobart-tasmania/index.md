+++
type = "question"
title = "Can&#x27;t get OSM for Hobart, Tasmania"
description = '''Hi, I am trying to download the street map for Hobart Tasmania but no matter what size I select I keep getting the error that says it&#x27;s larger than 5000 nodes. I&#x27;ve tried changing the layers of the map even to the point of black and white, and even tried the other sites mentioned but have either sim...'''
date = "2019-06-17T01:03:00Z"
lastmod = "2019-06-20T16:22:00Z"
weight = 69636
keywords = [ "issue", "osm" ]
aliases = [ "/questions/69636" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't get OSM for Hobart, Tasmania](/questions/69636/cant-get-osm-for-hobart-tasmania)

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
<span id="post-69636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69636-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to download the street map for Hobart Tasmania but no matter what size I select I keep getting the error that says it's larger than 5000 nodes. I've tried changing the layers of the map even to the point of black and white, and even tried the other sites mentioned but have either similar issues or for some reason the file doesn't want to work on my Mac.</p>
<p>I've got the height map from terrain party and it worked fine. The co-ordinates are: West 147.163020 North -42.780237 East 147.556507 South -43.067697</p>
<p>Any help would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-issue" rel="tag" title="see questions tagged &#39;issue&#39;">issue</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '19, 01:03</strong></p>
<img src="https://secure.gravatar.com/avatar/37e2938bff514a178498edc9988fcd02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PETER&#39;s gravatar image" />
<p><span>PETER</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PETER has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69636" class="comments-container">
<span id="69638"></span>
<div id="comment-69638" class="comment">
<div id="post-69638-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Can you explain the purpose for downloading the area? This would help in suggesting other ways to retrieve the data. The download functionality on the main site is rather limited but is also not meant for GPS or GIS use.</p>
</div>
<div id="comment-69638-info" class="comment-info">
<span class="comment-age">(17 Jun '19, 04:07)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="69639"></span>
<div id="comment-69639" class="comment">
<div id="post-69639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My main purpose is to load the roads onto the map. As am trying to build as good as can get replica of Hobart in Cities Skylines. So would like to have close enough setup of the infrastructure so can play the game with most of it setup.</p>
</div>
<div id="comment-69639-info" class="comment-info">
<span class="comment-age">(17 Jun '19, 04:11)</span> <span class="comment-user userinfo">PETER</span>
</div>
</div>
</div>
<div id="comment-tools-69636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69636-form-container" class="comment-form-container">
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

<span id="69640"></span>

<div id="answer-container-69640" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69640-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Downloading data through the export function on the main OSM website (which is what I presume you are doing) will rarely work. Exporting data from the main (API) database is costly, so is given a low priority compared with API calls for editing. Therefore any export activity over a certain size is likely to fail.</p>
<p>Standard ways of getting OSM for an area are:</p>
<ul>
<li>Overpass &amp; <a href="http://overpass-turbo.eu/">Overpass turbo</a> queries: these allow a broad range of queries and are most frequently used to filter data.</li>
<li>Pre-prepared download services. The best known is that of <a href="https://download.geofabrik.de/australia-oceania/australia.html">Geofabrik</a>, which organises dowanload extracts by geographical regions (which can be quite large).</li>
<li>Dynamic downloads, such as those of <a href="https://extract.bbbike.org/">bbbike</a>, which allow an area (within size limits) to be selected and an extract prepared in a few minutes.</li>
<li>Tool based extracts, such as those used by QGIS OSM plugins. These are often closely related to Overpass.</li>
</ul>
<p>I would think bbbike is the most suitable for your immediate purposes.</p>
<p>NOTE: data can come in 3 typical formats: .pbf, .zip, and .osm (or .xml). You may need a specific format depending on which tools you are using.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '19, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-69640" class="comments-container">
<span id="69653"></span>
<div id="comment-69653" class="comment">
<div id="post-69653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help but I think I'm just going to give up. No matter which file formats I download I just can't seem to get the game to recognise the files.</p>
<p>I might just have to upload the map (height map) as is to the steam workshop for someone else to attempt getting the roads loaded, just cause it's causing me too much annoyance and too much time.</p>
</div>
<div id="comment-69653-info" class="comment-info">
<span class="comment-age">(18 Jun '19, 14:25)</span> <span class="comment-user userinfo">PETER</span>
</div>
</div>
<span id="69668"></span>
<div id="comment-69668" class="comment">
<div id="post-69668-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>According to <a href="https://steamcommunity.com/app/255710/discussions/0/1456202492182996717/">this discussion</a> you need a *.osm file.</p>
<p>You can try to export Raw data via Overpass. Try <a href="http://overpass-turbo.eu/s/K2V">this query</a>, choose Export -&gt; Download/copy as Raw OSM Data. Of course, you can adapt the query to download other areas as well.</p>
</div>
<div id="comment-69668-info" class="comment-info">
<span class="comment-age">(19 Jun '19, 04:26)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="69680"></span>
<div id="comment-69680" class="comment">
<div id="post-69680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks great but only seems does Hobart CBD I'm needing .osm for the area I've selected: West 147.163020, North -42.780237, East 147.556507, South -43.067697 Which basically covers down to Margate, Summit of Mount Wellington, Berriedale, Opossum Bay, and just after the Hobart Airport.</p>
</div>
<div id="comment-69680-info" class="comment-info">
<span class="comment-age">(20 Jun '19, 12:06)</span> <span class="comment-user userinfo">PETER</span>
</div>
</div>
<span id="69687"></span>
<div id="comment-69687" class="comment">
<div id="post-69687-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>then try this query: <a href="http://overpass-turbo.eu/s/K6I">http://overpass-turbo.eu/s/K6I</a> this searches for all roads in the bounding box (aka visible area on the map)</p>
</div>
<div id="comment-69687-info" class="comment-info">
<span class="comment-age">(20 Jun '19, 16:22)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-69640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69640-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69684"></span>

<div id="answer-container-69684" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69684-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you press the "export" button in OSM the following text is displayed:</p>
<pre><code>If the above export fails, please consider using one of the sources listed below:</code></pre>
<p>If you do as it suggests, one of those options is Overpass and that will take you to an overpass download of that area, just like escada's above but for whatever area you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '19, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69684" class="comments-container">
&#10;</div>
<div id="comment-tools-69684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69684-form-container" class="comment-form-container">
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

