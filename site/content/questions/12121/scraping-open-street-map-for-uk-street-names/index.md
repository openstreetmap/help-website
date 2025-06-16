+++
type = "question"
title = "Scraping Open Street Map for UK street names"
description = '''Hi,  I am looking to compile a list of UK street names for an infographic project. Would it be possible to scrape the OSM for every street name, and output that data into a spreadsheet? If anyone out there can help with this I&#x27;d be very grateful.  Thanks,  Chris'''
date = "2012-04-18T11:26:00Z"
lastmod = "2012-04-18T11:59:00Z"
weight = 12121
keywords = [ "scraping", "street", "data", "names" ]
aliases = [ "/questions/12121" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Scraping Open Street Map for UK street names](/questions/12121/scraping-open-street-map-for-uk-street-names)

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
<span id="post-12121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12121-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am looking to compile a list of UK street names for an infographic project. Would it be possible to scrape the OSM for every street name, and output that data into a spreadsheet? If anyone out there can help with this I'd be very grateful.</p>
<p>Thanks,</p>
<p>Chris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-scraping" rel="tag" title="see questions tagged &#39;scraping&#39;">scraping</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '12, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/c90386cf05f399429028d31a6c3785ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrishall&#39;s gravatar image" />
<p><span>chrishall</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrishall has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12121" class="comments-container">
&#10;</div>
<div id="comment-tools-12121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12121-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="12122"></span>

<div id="answer-container-12122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12122-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We reserve the word "scraping" for people who, to our dismay, write clumsy scripts that make tons of individual requests against our API or web site. Don't do that - we're an open data project and we make our data available for download!</p>
<p>Grab a data extract for the UK e.g. from the <a href="http://download.geofabrik.de/">Geofabrik download server</a>, then use a program like <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> to filter out only highways:</p>
<pre><code>osmosis --read-pbf file.osm.pbf --tf accept-ways highway=\* --write-xml myfile.osm</code></pre>
<p>From the resulting XML file, extract all names - easiest on Linux with something like</p>
<pre><code>grep &#39;k=&quot;name&quot;&#39; myfile.osm | cut -d\&quot; -f4</code></pre>
<p>and you have your list. (If you prefer DBF files to XML, you could probably download the shp.zip file from the download server and simply open the roads.dbf file.)</p>
<p>Caveats:</p>
<ol>
<li><p>This procedure will yield names for everything tagged "highway", including cycleways, footways, steps, roundabouts.</p></li>
<li><p>This procedure does not allow you to count how often each name occurs in reality, because a road may consist of several parts in OSM, so the same road might feature multiple times in your file. Should you want to eliminate such double mentions, some programming or GIS magic will be required.</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '12, 11:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '12, 11:49</strong> </span></p>
</div>
</div>
<div id="comments-container-12122" class="comments-container">
<span id="12125"></span>
<div id="comment-12125" class="comment">
<div id="post-12125-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik,</p>
<p>Thanks for coming back to me. Apologies re. 'scraping', I'm not looking to inconvenience anyone!</p>
<p>The second point you make is probably the most relevant - and thanks for bringing it to my attention. I'm not sure I know how to solve this myself - can you help, or recommend anyone who can? If it's time-consuming work I'm willing to pay for the research/make an appropriate donation.</p>
<p>Many thanks,</p>
<p>Chris</p>
</div>
<div id="comment-12125-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 11:54)</span> <span class="comment-user userinfo">chrishall</span>
</div>
</div>
<span id="12126"></span>
<div id="comment-12126" class="comment">
<div id="post-12126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems like the data set mentioned by Richard and Ed would conveniently circumvent this problem!</p>
</div>
<div id="comment-12126-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 11:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12122-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12123"></span>

<div id="answer-container-12123" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12123-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It might be better to start with something like OS OpenData, particularly the Locator dataset I think.</p>
<p><a href="http://www.ordnancesurvey.co.uk/oswebsite/products/os-locator/index.html">http://www.ordnancesurvey.co.uk/oswebsite/products/os-locator/index.html</a></p>
<p>As yet, OpenStreetMap does not have as comprehensive a coverage as the OS data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '12, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-12123" class="comments-container">
&#10;</div>
<div id="comment-tools-12123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12123-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12124"></span>

<div id="answer-container-12124" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12124-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap is arguably not the best data source for your application. You would be better served by using <a href="http://www.ordnancesurvey.co.uk/oswebsite/products/os-locator/">OS Locator</a>, from the Ordnance Survey OpenData release, which has a better licence, a simpler file format, more consistent data, and is more complete.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '12, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-12124" class="comments-container">
&#10;</div>
<div id="comment-tools-12124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12124-form-container" class="comment-form-container">
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

