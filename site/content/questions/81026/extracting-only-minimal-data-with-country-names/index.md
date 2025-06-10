+++
type = "question"
title = "Extracting only minimal data with country names"
description = '''So, my plan is as follows:  Download planet-210712.osm.pbf  Convert it to planet.o5m using osmconvert64-0.8.8p.exe Extract all the details I need using osmfilter.exe (e.g. using this command: osmfilter.exe --keep=&quot;natural=coastline or ( boundary=administrative and admin_level=2 )&quot; --drop=&quot;maritime=y...'''
date = "2021-07-18T21:07:00Z"
lastmod = "2021-07-18T21:07:00Z"
weight = 81026
keywords = [ "countryname", "simplify", "osmfilter" ]
aliases = [ "/questions/81026" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting only minimal data with country names](/questions/81026/extracting-only-minimal-data-with-country-names)

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
<span id="post-81026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81026-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, my plan is as follows:</p>
<ol>
<li>Download <code>planet-210712.osm.pbf</code></li>
<li>Convert it to <code>planet.o5m</code> using <code>osmconvert64-0.8.8p.exe</code></li>
<li>Extract all the details I need using <code>osmfilter.exe</code> (e.g. using this command: <code>osmfilter.exe --keep="natural=coastline or ( boundary=administrative and admin_level=2 )" --drop="maritime=yes or admin_level!=2" planet.o5m &gt; planet.osm</code></li>
<li>Possibly simplify the shapes, since current file-size is ~12GB in OSM format.</li>
<li>Process data with <code>osm2pgsql.exe</code> and import it into PostGIS database.</li>
<li>Serve vector tiles using some web server like <code>pg_tileserv.exe</code>.</li>
</ol>
<p>Now, all this works more/less OK (I tried first on some smaller dataset of Netherlands), but it seems that I cannot get this to extract country names. Not sure if this is some additional display layer, or is this actually part of OSM files?</p>
<p>I'm adding screenshot of the country names that I would like to display, but that I cannot see when I open OSM file in some of the editors. Is there <code>country_3</code> inside the OSM files? I can find only <code>place=country</code>.</p>
<p>Is it easy to simplify shapes for <code>natural=coastline</code> and <code>boundary=administrative</code> inside OSM, so I can get smaller filesize?</p>
<p><img src="https://help.openstreetmap.org/upfiles/Capture_WILpdei.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-countryname" rel="tag" title="see questions tagged &#39;countryname&#39;">countryname</span> <span class="post-tag tag-link-simplify" rel="tag" title="see questions tagged &#39;simplify&#39;">simplify</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '21, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/cd56b4c10801fd7409ee898053120b53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bojanv55&#39;s gravatar image" />
<p><span>bojanv55</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bojanv55 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-81026" class="comments-container">
&#10;</div>
<div id="comment-tools-81026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81026-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

