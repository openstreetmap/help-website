+++
type = "question"
title = "How to include the downloaded spain.osm from cloudmade in my openlayers map?"
description = '''Hi again, I just downloaded spain.osm, but I don&#x27;t know how include it in a openlayers map which I have... What should I do? I&#x27;m very confused Thanks in advance.'''
date = "2012-07-05T17:24:00Z"
lastmod = "2012-07-06T12:12:00Z"
weight = 13997
keywords = [ "openlayers", "data", ".osm" ]
aliases = [ "/questions/13997" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to include the downloaded spain.osm from cloudmade in my openlayers map?](/questions/13997/how-to-include-the-downloaded-spainosm-from-cloudmade-in-my-openlayers-map)

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
<span id="post-13997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13997-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi again, I just downloaded spain.osm, but I don't know how include it in a openlayers map which I have...</p>
<p>What should I do? I'm very confused Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '12, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/b965fa99c7d633a6b79a722f6d1a0e30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="garciasanchezdani&#39;s gravatar image" />
<p><span>garciasanche...</span><br />
<span class="score" title="55 reputation points">55</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="garciasanchezdani has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '14, 14:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-13997" class="comments-container">
<span id="14016"></span>
<div id="comment-14016" class="comment">
<div id="post-14016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi friends, thanks very much for your answers. I'd like know what data contains this .osm ... this is, what can I see with this .osm of Spain? I imagine I can see pois, for example, right? And for I've understood, this .osm has a little portion of the real database of openstreetmap...Am I right? hehe Sorry for my english. Best regards.</p>
</div>
<div id="comment-14016-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 08:20)</span> <span class="comment-user userinfo">garciasanche...</span>
</div>
</div>
<span id="14022"></span>
<div id="comment-14022" class="comment">
<div id="post-14022-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please add your comments as comments not answers. To see yourself what this .osm file contains, just open it with text editor. And if you do it, then use some smaller extract (up to some MB instead of hundreds).</p>
</div>
<div id="comment-14022-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 10:36)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="14031"></span>
<div id="comment-14031" class="comment">
<div id="post-14031-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The problem with .osm files is that they tend to be large, so "opening it with an editor" might not be straightforward. Users of Unix-like operating systems already have tools such as "more", "head", "tail", "grep" etc. that make extracting data from large files relatively easy, but there isn't anything built-in on Windows, although versions of many of them compiled for Windows are available <a href="http://unxutils.sourceforge.net/">here</a>.</p>
<p>That said, it's often easier to deal with OSM data in a compressed format. If you have a look at <a href="http://download.geofabrik.de/osm/europe/">Geofabrik's download page</a>, you can see that the 5Gb spain.osm is only 292MB as a .pbf file (which is <a href="http://code.google.com/p/protobuf/">this</a> format). The <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">switch2osm pages</a> suggest using .pbf files because they're smaller, and recent versions of the OSM tools and things such as <a href="http://www.mkgmap.org.uk/">mkgmap</a> can work with them.</p>
<p>If you need to convert between .pbf and .osm formats, you can use <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> to do that.</p>
</div>
<div id="comment-14031-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 12:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="14033"></span>
<div id="comment-14033" class="comment">
<div id="post-14033-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One thing to mention - I notice that on the page <a href="http://downloads.cloudmade.com/europe/southern_europe/spain#downloads_breadcrumbs">that you probably downloaded from</a> it says "Last maps update: 13 December 2011". If that date's accurate, you may want to consider using a more recent extact - there's a list <a href="http://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">here</a>. Personnally I've found <a href="http://download.geofabrik.de/osm/europe/">Geofabrik's</a> to be up to date and reliable, but plenty of others are available.</p>
</div>
<div id="comment-14033-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 12:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13997-form-container" class="comment-form-container">
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

<span id="14003"></span>

<div id="answer-container-14003" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14003-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd have a look at the <a href="http://switch2osm.org/">switch2osm</a> site, particularly the "<a href="http://switch2osm.org/serving-tiles/">serving tiles</a>" sections. You've already got an OpenLayers map, so you'd then just need to add another layer to that, defining the layer something like:</p>
<pre><code>var newLayer = new OpenLayers.Layer.OSM(&quot;My new map&quot;, &quot;http://myserver/osm_tiles/${z}/${x}/${y}.png&quot;, {numZoomLevels: 19});</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '12, 20:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-14003" class="comments-container">
<span id="14017"></span>
<div id="comment-14017" class="comment">
<div id="post-14017-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi! Thanks for your answer. But I don't understand some things... - With this .osm, what I have to do? Upload it to a server mine? This file has 5 GB! - What is switch2osm? And what it serving tiles? For I understand, serving tiles offers me the possibility of make a dinamyc map serving me in each moment, the section of map where I am, right? Regards.</p>
</div>
<div id="comment-14017-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 08:26)</span> <span class="comment-user userinfo">garciasanche...</span>
</div>
</div>
<span id="14024"></span>
<div id="comment-14024" class="comment">
<div id="post-14024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Click the <a href="http://switch2osm.org/serving-tiles/">http://switch2osm.org/serving-tiles/</a> link above it explains how to set up a rendering server and database into which you could load the Spanish .osm file that you've downloaded - then you can point your Openlayers map at it.</p>
<p>(or does "a openlayers map which I have" in the question mean "an Openlayers map which I could set up in the future, but haven't done so yet")</p>
</div>
<div id="comment-14024-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 11:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="14027"></span>
<div id="comment-14027" class="comment">
<div id="post-14027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, I've it in local, but no of spain, I have a sample map with OpenLayers</p>
</div>
<div id="comment-14027-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 11:45)</span> <span class="comment-user userinfo">garciasanche...</span>
</div>
</div>
</div>
<div id="comment-tools-14003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14003-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13999"></span>

<div id="answer-container-13999" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13999-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to load the file into a database (using osm2pgsql or imposm) and then install a rendering engine that makes tiles from it for display in OpenLayers. You could use TileMill for that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '12, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13999" class="comments-container">
<span id="14020"></span>
<div id="comment-14020" class="comment">
<div id="post-14020-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't understand for what I need use TileMill...? The other thing, I understood...I have a .osm file (of Spain in my case) and I need upload in a database, using osm2pgsql for example. Thanks.</p>
</div>
<div id="comment-14020-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 09:31)</span> <span class="comment-user userinfo">garciasanche...</span>
</div>
</div>
<span id="14021"></span>
<div id="comment-14021" class="comment">
<div id="post-14021-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I downloaded and installed Tilemill in my computer. I'm going to start using it.</p>
</div>
<div id="comment-14021-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 09:59)</span> <span class="comment-user userinfo">garciasanche...</span>
</div>
</div>
</div>
<div id="comment-tools-13999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13999-form-container" class="comment-form-container">
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

