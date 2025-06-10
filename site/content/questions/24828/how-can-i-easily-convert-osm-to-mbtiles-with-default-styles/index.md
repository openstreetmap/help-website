+++
type = "question"
title = "How can I easily convert OSM to MBtiles with default styles?"
description = '''I want to do a really simple thing:  download city data from http://metro.teczno.com/ do some magic (where I don&#x27;t have to write bazillion stylesheets by hand) to convert it to MBTiles run it on a mobile app offline  The problem is that I can&#x27;t find a way to sensibly convert the data. I&#x27;ve tried Til...'''
date = "2013-08-02T11:51:00Z"
lastmod = "2015-07-09T12:21:00Z"
weight = 24828
keywords = [ ".osm", "tilemill", "convert", "mbtiles" ]
aliases = [ "/questions/24828" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How can I easily convert OSM to MBtiles with default styles?](/questions/24828/how-can-i-easily-convert-osm-to-mbtiles-with-default-styles)

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
<span id="post-24828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24828-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to do a really simple thing:</p>
<ol>
<li>download city data from <a href="http://metro.teczno.com/">http://metro.teczno.com/</a></li>
<li><strong>do some magic (where I don't have to write bazillion stylesheets by hand) to convert it to MBTiles</strong></li>
<li>run it on a mobile app offline</li>
</ol>
<p>The problem is that I can't find a way to sensibly convert the data. I've tried Tilemill (trust me I really tried), but it just doesn't do what I expect. It doesn't really care if I add layers, most of the time it just errors or does nothing for 20 minutes, and even when I get it working the best I could do is this</p>
<p><img src="http://i.imgur.com/xFs0HHj.png" /></p>
<p>I don't want anything custom, I don't want to create my own layer thingies with custom graphics, or customize how the map works. <strong>All I want is to take the default look of OSM, slice a region and stick it into a MBTiles format.</strong> I also tried <a href="http://www.mapbox.com/tilemill/docs/guides/osm-bright-mac-quickstart/">osm2pgsql according to Tilemill guide</a>, but Tilemill crashed saying that there is some invalid data.</p>
<p>I've read tons of documentation but everything just refers to one more complicated tool than another and 1000 ways to customize things. I tried mapnik and mb-util (which tells me <code>file is encrypted or is not a database</code> for every single file format I've tried), but I couldn't find a simple way to do this.</p>
<p><strong>Could someone please point me to a resource or explain a simple way to take <code>.osm</code> and shove it into a <code>.MBTiles</code>?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '13, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/16a5eec5eca4550033c0e19dba3b32b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="darthdeus&#39;s gravatar image" />
<p><span>darthdeus</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="darthdeus has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '16, 14:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-24828" class="comments-container">
<span id="24844"></span>
<div id="comment-24844" class="comment">
<div id="post-24844-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you take a look at the various <a href="http://github.com/mapbox/mbtiles-spec/wiki/Implementations">implementations</a>?</p>
</div>
<div id="comment-24844-info" class="comment-info">
<span class="comment-age">(02 Aug '13, 15:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24828-form-container" class="comment-form-container">
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

<span id="24829"></span>

<div id="answer-container-24829" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24829-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no simple way, except "simply" paying someone to do the complicated stuff for you and send you the MBTiles file you're after. Most of the things that one would usually say in response to your question (osm2pgsql, tilemill etc) you seem to have tried already and failed. It seems to work for other people; maybe you should go to a TileMill support forum and post the exact error messages you received there.</p>
<p>If you are on Windows or Linux - and not on iOS - then another relatively simple option is <a href="www.maperitive.net">Maperitive</a> where you can load an OSM file and export to tiles with a few commands; after that you'd still have to run some utility (e.g. mbutil) to convert the raw tiles to MBTiles format.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '13, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24829" class="comments-container">
<span id="24832"></span>
<div id="comment-24832" class="comment">
<div id="post-24832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't understand why this should be something complicated. I'm not asking to customize anything, I just need to convert one file format to another, no changes, no nothing, just a simple export.</p>
</div>
<div id="comment-24832-info" class="comment-info">
<span class="comment-age">(02 Aug '13, 12:30)</span> <span class="comment-user userinfo">darthdeus</span>
</div>
</div>
<span id="24843"></span>
<div id="comment-24843" class="comment">
<div id="post-24843-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Conversions between file formats are rarely simple.</p>
</div>
<div id="comment-24843-info" class="comment-info">
<span class="comment-age">(02 Aug '13, 15:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="40202"></span>
<div id="comment-40202" class="comment">
<div id="post-40202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Look at this as an initial-days stage in a multi-year technology development process. At one time it was incredibly complicated to digitize sound and convert it. I also need to render osm data and after getting lost with MBTiles, bit the bullet and am doing it the png tiles way using Maperitive.</p>
</div>
<div id="comment-40202-info" class="comment-info">
<span class="comment-age">(11 Jan '15, 04:16)</span> <span class="comment-user userinfo">nikhilvj</span>
</div>
</div>
</div>
<div id="comment-tools-24829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24829-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44065"></span>

<div id="answer-container-44065" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44065-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maperitive will go from OSM data to Mbtiles directly. Using the default rules files from Maperitive, the output is identical (almost) to OSM rendering. I export to mbtiles for a 5 mile radius area (zooms 10-19) every few months without issue on a windows PC. Takes about 6 hours.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '15, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5085ea3bf927efbe9f98b1ac9a0d6b3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RJCorazza&#39;s gravatar image" />
<p><span>RJCorazza</span><br />
<span class="score" title="101 reputation points">101</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RJCorazza has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44065" class="comments-container">
&#10;</div>
<div id="comment-tools-44065" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44065-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24848"></span>

<div id="answer-container-24848" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24848-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two general approaches to making mbtiles archives.</p>
<p>1) Generate the tiles yourself, and put them in the mbtiles archive.</p>
<p>For this you'll need a working copy of <a href="http://www.mapbox.com/tilemill/">Tilemill</a>, <a href="https://github.com/openstreetmap/osm2pgsql">osm2pgsql</a> and <a href="https://github.com/gravitystorm/openstreetmap-carto">openstreetmap-carto</a>. Load your extract into the database with osm2pgsql, use the openstreetmap-carto stylesheets (which work fine as a Tilemill project) to apply the normal style rules to your data, and use the Tilemill as a nice user interface to pick the area that you want, and export your mbtiles archive.</p>
<p>2) Bulk-download someone else's map tile images, and put them into an mbtiles archive directly.</p>
<p>Note that very few people do this, and so I'm not sure there's even some scripts available for you to run that will do the whole thing, and it's against the T&amp;Cs of most tileserver providers to run bulk downloads anyway.</p>
<p>You ask for "a simple way to take .osm and shove it into a .MBTiles" but there's nothing fundamentally simple about it. At some point the raw OSM data needs styling and converting into tiles, either by you or by someone else.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '13, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-24848" class="comments-container">
&#10;</div>
<div id="comment-tools-24848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24848-form-container" class="comment-form-container">
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

