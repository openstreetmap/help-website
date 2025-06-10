+++
type = "question"
title = "where to get the standard osm style file for mapnik?"
description = '''Hi, For my OS aircraft navigation app I use OSM maps. I used to download tiles of 2 degr lon and 1 degr lat. Then using imagemagick to glue them all together. Combersome, and the downloading doesn&#x27;t seem to work (in time) anymore. Now I want to create the maps myself. I have Mapnik installed. Used o...'''
date = "2014-02-24T23:46:00Z"
lastmod = "2014-02-25T13:05:00Z"
weight = 30985
keywords = [ "style", "mapnik", "file" ]
aliases = [ "/questions/30985" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [where to get the standard osm style file for mapnik?](/questions/30985/where-to-get-the-standard-osm-style-file-for-mapnik)

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
<span id="post-30985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30985-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>For my OS aircraft navigation app I use OSM maps. I used to download tiles of 2 degr lon and 1 degr lat. Then using imagemagick to glue them all together. Combersome, and the downloading doesn't seem to work (in time) anymore.</p>
<p>Now I want to create the maps myself. I have Mapnik installed. Used osm2pgsql to load some osm data into the database. Now I want to use Mapnik to create a map. Just using the default OSM style.</p>
<p>Where can I get it? (BTW tilemill and carto [converting from css] won't work on Ubuntu 12.10). Can somebody please help me out here (my project depends on it). Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '14, 23:46</strong></p>
<img src="https://secure.gravatar.com/avatar/1a92bff5cdfa9e20e409daab589665ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wim%20de%20vries&#39;s gravatar image" />
<p><span>wim de vries</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wim de vries has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '14, 23:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30985" class="comments-container">
&#10;</div>
<div id="comment-tools-30985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30985-form-container" class="comment-form-container">
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

<span id="30995"></span>

<div id="answer-container-30995" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30995-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The stylesheets used by openstreetmap for the "standard" layer are found at <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> . The files at <a href="https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik">https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik</a> are for an old version of the style and are no longer used or maintained.</p>
<p>The openstreetmap-carto stylesheet can be used by Tilemill. I develop them using Tilemill (and CartoCSS) on Ubuntu 12.04, so I don't know why you've said that it won't work on 12.10.</p>
<p>For what you need though, you might not need to install Tilemill. I would suggest converting the stylesheets from CartoCSS to XML using the command line converter from <a href="https://github.com/mapbox/carto">https://github.com/mapbox/carto</a> and then using the XML with <a href="http://code.google.com/p/mapnik-utils/wiki/Nik2Img">nik2img</a> to generate the large images that you require.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '14, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-30995" class="comments-container">
<span id="31008"></span>
<div id="comment-31008" class="comment">
<div id="post-31008-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. The conversion went OK now. Just explaining a bit more about the OSM maps I use currently. scale 1:500000 (which is also standard in aviation maps) covering south and west and mid europe. Runs on a netbook (rendering in 3D). (see <a href="http://sourceforge.net/projects/openflightnav/?source=directory)">http://sourceforge.net/projects/openflightnav/?source=directory)</a> Now I am porting it to a mobile platform (Sailfish/Jolla). My current OSM map -including the 3D data- is to big, so I want to create smaller sets (now testing the netherlands). The exact (lon/lat) borders of the map must be known to enable navigation.</p>
</div>
<div id="comment-31008-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 13:03)</span> <span class="comment-user userinfo">wim de vries</span>
</div>
</div>
<span id="31009"></span>
<div id="comment-31009" class="comment">
<div id="post-31009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, possibly you are right by using sth simpler like nik2img (btw the URI isn't there anymore). I installed Tilemill from a package, it just shows a page with some dead links/buttons. Possibly it is outdated.</p>
</div>
<div id="comment-31009-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 13:04)</span> <span class="comment-user userinfo">wim de vries</span>
</div>
</div>
<span id="31010"></span>
<div id="comment-31010" class="comment">
<div id="post-31010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, the link is not dead, but <a href="http://trac.mapnik.org/wiki/Nik2Img">http://trac.mapnik.org/wiki/Nik2Img</a> within that page.</p>
</div>
<div id="comment-31010-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 13:05)</span> <span class="comment-user userinfo">wim de vries</span>
</div>
</div>
</div>
<div id="comment-tools-30995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30995-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30986"></span>

<div id="answer-container-30986" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not really a good answer (as I did never, not even nearly, try this myself), but maybe still helpful (checking our documentation …). Wait for better answers.</p>
<p>These style sheets are out of date but similar to the current one. You can use them if your carto converter does not work.</p>
<p><a href="http://switch2osm.org">http://switch2osm.org</a> → <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a> → section "Install Mapnik style-sheet" → <a href="http://svn.openstreetmap.org/applications/rendering/mapnik">http://svn.openstreetmap.org/applications/rendering/mapnik</a> → README and osm.xml seem to be what you are searching for.</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> → (previous non-carto stylsheets) → <a href="https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik">https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '14, 00:08</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '14, 11:44</strong> </span></p>
</div>
</div>
<div id="comments-container-30986" class="comments-container">
<span id="30991"></span>
<div id="comment-30991" class="comment">
<div id="post-30991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the fast reply. I will try this. Still a bit confused for I thought that the osm.xml was an OSM data file, not a style file.</p>
</div>
<div id="comment-30991-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 00:22)</span> <span class="comment-user userinfo">wim de vries</span>
</div>
</div>
<span id="30992"></span>
<div id="comment-30992" class="comment">
<div id="post-30992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>as far as I understand it it is a style file (look into it — this is no osm data)</p>
</div>
<div id="comment-30992-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 00:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="30994"></span>
<div id="comment-30994" class="comment">
<div id="post-30994-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The old, non-carto style sheets can be used but they don't show the same map that you see on openstreetmap.org these days. Converting the Carto CSS to XML is simple and will work with Ubuntu 12.10 - use the command line converter from <a href="https://github.com/mapbox/carto">https://github.com/mapbox/carto</a>.</p>
</div>
<div id="comment-30994-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 07:05)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="30998"></span>
<div id="comment-30998" class="comment">
<div id="post-30998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. The link above is not valid anymore.</p>
<p>I installed the ubuntu carto package: running it:</p>
<p>"/usr/bin/nodejs: symbol lookup error: /usr/lib/nodejs/zipfile/_zipfile.node: undefined symbol: _ZN2v814ObjectTemplate11SetAccessorENS_6HandleINS_6StringEEEPFNS1 INS_5ValueEEENS_5LocalIS2_EERKNS_12AccessorInfoEEPFvS7_NS6 IS4_EESA_ES5_NS_13AccessControlENS_17PropertyAttributeE" (replaced some "<code>_</code>" by space for line breaks)</p>
<p>I googled on that but could not find a solution that worked. Maybe there is a updated carto somewhere?</p>
</div>
<div id="comment-30998-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 10:32)</span> <span class="comment-user userinfo">wim de vries</span>
</div>
</div>
<span id="30999"></span>
<div id="comment-30999" class="comment">
<div id="post-30999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@wim de vries</span>: I've updated the link - the help site software had added a spurious full stop.</p>
</div>
<div id="comment-30999-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 10:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="31000"></span>
<div id="comment-31000" class="comment not_top_scorer">
<div id="post-31000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot.</p>
</div>
<div id="comment-31000-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 10:53)</span> <span class="comment-user userinfo">wim de vries</span>
</div>
</div>
<span id="31004"></span>
<div id="comment-31004" class="comment not_top_scorer">
<div id="post-31004-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Frederik</span>: sure, they are out of date but similar <em>and</em> it was mentioned that carto does not work for the OP.</p>
</div>
<div id="comment-31004-info" class="comment-info">
<span class="comment-age">(25 Feb '14, 11:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30986" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-30986-form-container" class="comment-form-container">
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

