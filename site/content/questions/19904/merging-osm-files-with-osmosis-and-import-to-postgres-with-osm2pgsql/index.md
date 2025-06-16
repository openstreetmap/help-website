+++
type = "question"
title = "Merging OSM files with OSMOSIS and import to Postgres with OSM2PGSQL"
description = '''I have a problem merging and then importing two OSM files. I downloaded to distinct .osm-files from cloudmade. They are not sharing any geographical attribute (as the first is the country Monaco, the 2nd is the county Bremen in Germany). I merged the with OSMOSIS and it gives me an output file. Then...'''
date = "2013-02-13T10:45:00Z"
lastmod = "2013-02-13T11:46:00Z"
weight = 19904
keywords = [ "merge", "osm2pgsql", "osmosis", "postgis" ]
aliases = [ "/questions/19904" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merging OSM files with OSMOSIS and import to Postgres with OSM2PGSQL](/questions/19904/merging-osm-files-with-osmosis-and-import-to-postgres-with-osm2pgsql)

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
<span id="post-19904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19904-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a problem merging and then importing two OSM files. I downloaded to distinct .osm-files from cloudmade. They are not sharing any geographical attribute (as the first is the country Monaco, the 2nd is the county Bremen in Germany).</p>
<p>I merged the with OSMOSIS and it gives me an output file.</p>
<p>Then I import it via OSM2PGSQL.</p>
<p>Looking at the dataset using QGIS it either shows me the data of Bremen or Monaco (depending the order in the OSMOSIS merge statement).</p>
<p>Does anyone has a solution for this problem?</p>
<p>Thanks a lot Carsten</p>
<p>EDIT: I imported like described further down. Downloaded Bremen and Monaco planet files and imported them like this:</p>
<p>$osm2pgsql -l --create --database gis --username postgres --prefix planet --slim --cache 2048 /home/katia/Downloads/monaco.osm.bz2 -S /usr/share/osm2pgsql/default.style</p>
<p>$osm2pgsql -l --append --database gis --username postgres --prefix planet --slim --cache 2048 /home/katia/Downloads/bremen_1.osm.bz2 -S /usr/share/osm2pgsql/default.style</p>
<p>The two files seems to be correctly imported into postgis. No duplicates. But trying them visualizing them in OpenJump it displayes only the bremen.osm data. In PGAdmin3 it shows me that the tables do not have any primary key. How do set them correctly?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '13, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/284f6352fb39456e8b78c29840526353?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoge6b01&#39;s gravatar image" />
<p><span>hoge6b01</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoge6b01 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '13, 23:01</strong> </span></p>
</div>
</div>
<div id="comments-container-19904" class="comments-container">
<span id="19905"></span>
<div id="comment-19905" class="comment">
<div id="post-19905-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(not that it's directly related to your question but) do be aware that the date quoted for the data at <a href="http://downloads.cloudmade.com/">http://downloads.cloudmade.com/</a> is 13 December 2011.</p>
</div>
<div id="comment-19905-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 10:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="19907"></span>
<div id="comment-19907" class="comment">
<div id="post-19907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>oh, i haven't seen that. Thank you! What do you suggest to download from?</p>
</div>
<div id="comment-19907-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 11:24)</span> <span class="comment-user userinfo">hoge6b01</span>
</div>
</div>
<span id="19909"></span>
<div id="comment-19909" class="comment">
<div id="post-19909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are lots of extract sites available - see <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Downloading">this page</a>. I tend to use <a href="http://download.geofabrik.de/openstreetmap/">Geofabrik</a> myself, but there are lots of others.</p>
</div>
<div id="comment-19909-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 11:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="19910"></span>
<div id="comment-19910" class="comment">
<div id="post-19910-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought Geofabrik "pre-selects" the OSM content. Not that OSM2PGSQL selects the content defined in the default.style as well, but does Geofabrik contain the tags from default.style?</p>
</div>
<div id="comment-19910-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 11:46)</span> <span class="comment-user userinfo">hoge6b01</span>
</div>
</div>
</div>
<div id="comment-tools-19904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19904-form-container" class="comment-form-container">
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

<span id="19906"></span>

<div id="answer-container-19906" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19906-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing that you're missing the "append" on the second import? If you have a look <a href="/questions/5389/merging-2-countries-with-osm2pgsql">here</a> you'll see how that can be used, and also a description of a further problem that you might get if there's any data overlap between the two (which in your case there probably won't be).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '13, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-19906" class="comments-container">
<span id="19908"></span>
<div id="comment-19908" class="comment">
<div id="post-19908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I will give it a new try when I'm at home. btw, how do I temporary drop contrains?</p>
</div>
<div id="comment-19908-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 11:26)</span> <span class="comment-user userinfo">hoge6b01</span>
</div>
</div>
</div>
<div id="comment-tools-19906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19906-form-container" class="comment-form-container">
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

