+++
type = "question"
title = "Problems installing Nominatim: relations and functions not found"
description = '''I have problems installing nominatim. I run the installation process by this sentence: /usr/src/Nominatim-2.3.1$ /usr/src/Nominatim-2.2.0/utils/setup.php --osm-file /home/carto/spain-latest.osm --all --osm2pgsql-cache 18000 2&amp;gt;&amp;amp;1  I iniatilly thought it was right and the installation went ok. ...'''
date = "2015-05-27T08:48:00Z"
lastmod = "2015-05-28T13:35:00Z"
weight = 43244
keywords = [ "problem", "nominatim", "installation" ]
aliases = [ "/questions/43244" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problems installing Nominatim: relations and functions not found](/questions/43244/problems-installing-nominatim-relations-and-functions-not-found)

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
<span id="post-43244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43244-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have problems installing nominatim. I run the installation process by this sentence:</p>
<pre><code>/usr/src/Nominatim-2.3.1$ /usr/src/Nominatim-2.2.0/utils/setup.php --osm-file /home/carto/spain-latest.osm --all --osm2pgsql-cache 18000 2&gt;&amp;1</code></pre>
<p>I iniatilly thought it was right and the installation went ok. It araised an error called "missing relation search_blank_name" at the end of installation, but the data was there and I was able to work with it from my own scripts. However, when trying to use Nominatim when searching problmes are there and I can't use search tool. I already did a question and the sugestion for debuging with "debug=1" help mi to realized it was a problem of functions not found, functions that were suposed to be generated when installing nominatim. So I debug deeper the install process and I detected many problems of tables and functions not found. The first ones are the following:</p>
<pre><code>    2015-05-21 17:36:59 CEST ERROR:  no existe la tabla «import_status»
2015-05-21 17:36:59 CEST SENTENCIA:  drop table import_status;
2015-05-21 17:36:59 CEST ERROR:  no existe la tabla «import_osmosis_log»
2015-05-21 17:36:59 CEST SENTENCIA:  drop table import_osmosis_log;
2015-05-21 17:37:00 CEST ERROR:  no existe la tabla «import_npi_log»
2015-05-21 17:37:00 CEST SENTENCIA:  drop table import_npi_log;
2015-05-21 17:37:02 CEST ERROR:  no existe la secuencia «seq_word»
2015-05-21 17:37:02 CEST SENTENCIA:  DROP SEQUENCE seq_word;
2015-05-21 17:37:06 CEST ERROR:  no existe la tabla «country»
2015-05-21 17:37:06 CEST SENTENCIA:  drop table country;
2015-05-21 17:37:06 CEST ERROR:  no existe la relación «worldboundaries» en cará    cter 171
2015-05-21 17:37:06 CEST SENTENCIA:  insert into country select iso3166::varchar    (2), &#39;name:en&#39;-&gt;cntry_name, null,
          ST_Transform(geometryn(the_geom, generate_series(1, numgeometries(the_    geom))), 4326) from worldboundaries;
2015-05-21 17:37:06 CEST ERROR:  no existe la tabla «placex»
2015-05-21 17:37:06 CEST SENTENCIA:  drop table placex;</code></pre>
<p>I have tried this process many times with the spanish dataset and reduced versions of it by regional entities. The results are the same.</p>
<p>Can anyone help me to debug deeeper or point what I am doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '15, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/8ff71fc907067296fbfac86e637faa50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juanma%20MR&#39;s gravatar image" />
<p><span>Juanma MR</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juanma MR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43244" class="comments-container">
<span id="43280"></span>
<div id="comment-43280" class="comment">
<div id="post-43280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am still trying to find a solution to this.</p>
<p>I tried again another installation and the results are the same. When trying to use the nominatim search it says:</p>
<p>"function make_standard_name not found"</p>
<p>Afterwards, I have tried as follows:</p>
<p>"./utils/setup.php --create-functions"</p>
<p>But it did not add the functions.</p>
<p>I also tried updating using the same file and it did not through any error, but this process do not create missing functions:</p>
<p>"./utils/update.php --osm-file my_osm_file"</p>
<p>I am trying to debug localy to see where is it failing but making setup.php to work in local is another challenge for me. I want to make the install process to work propperly as ot havin gwarranties of the data being imported propperly is frightening.</p>
<p>Is there an alternative way to import data for nominatim, as imposm or any other method?</p>
</div>
<div id="comment-43280-info" class="comment-info">
<span class="comment-age">(28 May '15, 13:35)</span> <span class="comment-user userinfo">Juanma MR</span>
</div>
</div>
</div>
<div id="comment-tools-43244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43244-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

