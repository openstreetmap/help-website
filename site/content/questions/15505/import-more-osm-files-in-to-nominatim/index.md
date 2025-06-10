+++
type = "question"
title = "Import more osm files in to Nominatim"
description = '''Hi! I succeeded to import the OSM data for Netherlands (by the way, took 38 hours to finish) and now I want also to import (in the same database) the OSM data for Belgium and Luxembourg. Do you know how can be done? I have tried using ./utils/setup.php --osm-file belgium.pbf --import-data , but didn...'''
date = "2012-08-25T09:31:00Z"
lastmod = "2019-12-04T08:05:00Z"
weight = 15505
keywords = [ "files", "import", "nominatim", "data" ]
aliases = [ "/questions/15505" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Import more osm files in to Nominatim](/questions/15505/import-more-osm-files-in-to-nominatim)

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
<span id="post-15505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15505-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I succeeded to import the OSM data for Netherlands (by the way, took 38 hours to finish) and now I want also to import (in the same database) the OSM data for Belgium and Luxembourg.</p>
<p>Do you know how can be done? I have tried using ./utils/setup.php --osm-file belgium.pbf --import-data , but didn’t work (stopped at some point: Setting up table: planet_osm_ways) Should I use ./utils/setup.php --osm-file belgium.pbf --load-data?</p>
<p>Thank you!</p>
<p>Best regards, Roxana</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '12, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/2f496486f3d04cfe5b6d1d8ce9b660af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RoxanaO&#39;s gravatar image" />
<p><span>RoxanaO</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RoxanaO has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '17, 22:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-15505" class="comments-container">
<span id="15542"></span>
<div id="comment-15542" class="comment">
<div id="post-15542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/2921/lonvia"></a><a href="http://help.openstreetmap.org/users/2921/lonvia">@lonvia</a> Unfortunately didn't work! Here is the result:</p>
<p>/var/www/public_html/Nominatim/osmosis-0.40.1/bin/osmosis --read-xml 'belgium.pbf' --read-empty --derive-change --write-xml-change /var/www/public_html/Nominatim/data/osmosischange.osc ... org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to parse xml file belgium.pbf.</p>
<p><a href="http://help.openstreetmap.org/users/2933/cartinus"></a><a href="http://help.openstreetmap.org/users/2933/cartinus">@Cartinus</a> Thank you for the link! It will help me, but I wanted to know how to do if I want to import countries one by one.</p>
</div>
<div id="comment-15542-info" class="comment-info">
<span class="comment-age">(27 Aug '12, 09:15)</span> <span class="comment-user userinfo">RoxanaO</span>
</div>
</div>
<span id="40097"></span>
<div id="comment-40097" class="comment">
<div id="post-40097-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are using the wrong Osmosis flag, use --read-pbf, not --read-xml, see <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#PBF_Binary_Tasks">http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#PBF_Binary_Tasks</a> (I have removed superfluous parts of above error message).</p>
</div>
<div id="comment-40097-info" class="comment-info">
<span class="comment-age">(07 Jan '15, 12:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="53681"></span>
<div id="comment-53681" class="comment">
<div id="post-53681-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, I have the same problem with you. And I use the following statement to import the first country data:</p>
<p><code>./utils/setup.php --osm-file countryA.bz2</code></p>
<p>However, it shows "countryA.bz2" not readable.</p>
<p>Do you know Why such problems have appeared?</p>
</div>
<div id="comment-53681-info" class="comment-info">
<span class="comment-age">(23 Dec '16, 08:31)</span> <span class="comment-user userinfo">PasserbyAmen</span>
</div>
</div>
<span id="53686"></span>
<div id="comment-53686" class="comment">
<div id="post-53686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does the file <em>countryA.bz2</em> exist? Is it located in your current directory? Is it readable by your user?</p>
</div>
<div id="comment-53686-info" class="comment-info">
<span class="comment-age">(23 Dec '16, 18:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15505-form-container" class="comment-form-container">
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

<span id="15506"></span>

<div id="answer-container-15506" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15506-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-15506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RoxanaO has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume you are talking about importing into a Nominatim DB.</p>
<p>In theory, you could do that by using the update script:</p>
<pre><code>./utils/update.php --import-file belgium.xml.bz2</code></pre>
<p>(pbf files will not work here) and then reindex your data:</p>
<pre><code>./utils/update.php --index</code></pre>
<p>But that will be very, <em>very</em> slow.</p>
<p>The import will go much faster if you first merge the three country excerpts and then import the result in one go.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '12, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '12, 08:48</strong> </span></p>
</div>
</div>
<div id="comments-container-15506" class="comments-container">
<span id="15507"></span>
<div id="comment-15507" class="comment">
<div id="post-15507-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In the case of these three countries, there is even an excerpt available that already contains all three of them: <a href="http://planet.openstreetmap.nl/benelux/?order=N">planet-benelux</a></p>
</div>
<div id="comment-15507-info" class="comment-info">
<span class="comment-age">(25 Aug '12, 12:52)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="15578"></span>
<div id="comment-15578" class="comment">
<div id="post-15578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried also to import the merged made with the country excerpts and got a fatal error and stopped:</p>
<p><strong>COPY_END for COPY planet_osm_rels FROM STDIN; failed: ERROR: duplicate key value violates unique constraint "planet_osm_rels_pkey"</strong></p>
<p>And tried again with <strong>./utils/update.php --import-file belgium.pbf</strong> but still have java errors from above.</p>
<p>Any other ideas? Sorry for bother and thank you!</p>
</div>
<div id="comment-15578-info" class="comment-info">
<span class="comment-age">(28 Aug '12, 13:09)</span> <span class="comment-user userinfo">RoxanaO</span>
</div>
</div>
<span id="15579"></span>
<div id="comment-15579" class="comment">
<div id="post-15579-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ages ago someone posted a <a href="http://www.mail-archive.com/dev@openstreetmap.org/msg10349.html">patch</a> for osm2pgsql to modify instead of create data. If you really must merge data, you could try something like that - I'm sure that it'd be much slower than importing the data that <a href="http://help.openstreetmap.org/users/2933/cartinus">cartinus</a> <a href="http://planet.openstreetmap.nl/benelux/?order=N">linked to</a>, though.</p>
</div>
<div id="comment-15579-info" class="comment-info">
<span class="comment-age">(28 Aug '12, 13:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15592"></span>
<div id="comment-15592" class="comment">
<div id="post-15592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like it cannot read pdf format. Try with the belgium.xml.bz2 file.</p>
</div>
<div id="comment-15592-info" class="comment-info">
<span class="comment-age">(28 Aug '12, 19:37)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="15618"></span>
<div id="comment-15618" class="comment">
<div id="post-15618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have tried with belgium.osm (extracted from belgium.osm.bz2) and worked, but when I want to search (on local website) Belgium as a text: No results found. If I search after coordinates, for example: [51.4494967087473,4.46587880577936] should get: Oude Baan, Schildershof, Essen, Antwerpen, Antwerp, Flanders, 2910, Belgium, but instead I get only: Oude Baan, Belgium.</p>
<p>Do you know why is this happening?</p>
</div>
<div id="comment-15618-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 07:18)</span> <span class="comment-user userinfo">RoxanaO</span>
</div>
</div>
<span id="15620"></span>
<div id="comment-15620" class="comment not_top_scorer">
<div id="post-15620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, sorry, forgot to mention that you also have to reindex your data. I've added that step to my original answer.</p>
</div>
<div id="comment-15620-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 07:30)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="18671"></span>
<div id="comment-18671" class="comment not_top_scorer">
<div id="post-18671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you use osmosis to do the merge, it will merge the files correctly when there are duplicate objects in the same files.</p>
</div>
<div id="comment-18671-info" class="comment-info">
<span class="comment-age">(23 Dec '12, 00:04)</span> <span class="comment-user userinfo">smsm1</span>
</div>
</div>
<span id="40089"></span>
<div id="comment-40089" class="comment not_top_scorer">
<div id="post-40089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Solution works, but you can speed up the process by using osm2pgsql cahce like this(12G) ./utils/update.php --import-file ../azerbaijan-latest.osm.bz2 --osm2pgsql-cache 12000 And when indexing you can use threads aka index instances depending on your cpus count: ./utils/update.php –index --index-instances 4</p>
</div>
<div id="comment-40089-info" class="comment-info">
<span class="comment-age">(07 Jan '15, 07:57)</span> <span class="comment-user userinfo">ttrumm</span>
</div>
</div>
<span id="60245"></span>
<div id="comment-60245" class="comment not_top_scorer">
<div id="post-60245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I approve that I had successfully imported the missing osm file into the existing nominatim database (europe+asia). I took an osm.bz2 file from geofabrik, unpacked it to an osm (to speed things up) and ran --import-file. It took me very reasonable 2 days on 4 core 5GB RAM VM. Next step will be indexing.</p>
</div>
<div id="comment-60245-info" class="comment-info">
<span class="comment-age">(23 Oct '17, 15:16)</span> <span class="comment-user userinfo">sunsetjunks</span>
</div>
</div>
<span id="63033"></span>
<div id="comment-63033" class="comment not_top_scorer">
<div id="post-63033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When i try to import a little <code>pbf</code> or <code>osm</code> file, this error appears:</p>
<p><code>Osm2pgsql failed due to ERROR: Flatnode store cannot save negative IDs.</code></p>
</div>
<div id="comment-63033-info" class="comment-info">
<span class="comment-age">(18 Apr '18, 22:19)</span> <span class="comment-user userinfo">cybercoder</span>
</div>
</div>
<span id="63041"></span>
<div id="comment-63041" class="comment not_top_scorer">
<div id="post-63041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please ask a new question.</p>
</div>
<div id="comment-63041-info" class="comment-info">
<span class="comment-age">(19 Apr '18, 07:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="71982"></span>
<div id="comment-71982" class="comment not_top_scorer">
<div id="post-71982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is command:</p>
<blockquote>
./utils/update.php --import-file belgium.xml.bz2
</blockquote>
<p>not working! Although the data fills, table "word" - updated!</p>
<p>As well checked command :</p>
<blockquote>
./utils/setup.php --import-data --osm-file belgium.osm.pbf
</blockquote>
<p>It does not updated "placex" table, because of this not updated "search_word" table</p>
</div>
<div id="comment-71982-info" class="comment-info">
<span class="comment-age">(04 Dec '19, 08:05)</span> <span class="comment-user userinfo">Uffik</span>
</div>
</div>
</div>
<div id="comment-tools-15506" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-15506-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50621"></span>

<div id="answer-container-50621" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50621-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, the easy way is to do the following:</p>
<ol>
<li>cd /yourNominatimFolder/build;</li>
<li>mkdir data; cd data;</li>
<li>Download your pbf files (<a href="http://download.geofabrik.de">http://download.geofabrik.de</a>) wget <a href="http://download.geofabrik.de/south-america/peru-latest.osm.pbf">http://download.geofabrik.de/south-america/peru-latest.osm.pbf</a> wget <a href="http://download.geofabrik.de/south-america/chile-latest.osm.pbf">http://download.geofabrik.de/south-america/chile-latest.osm.pbf</a> wget <a href="http://download.geofabrik.de/south-america/colombia-latest.osm.pbf">http://download.geofabrik.de/south-america/colombia-latest.osm.pbf</a> wget <a href="http://download.geofabrik.de/south-america/mexico-latest.osm.pbf">http://download.geofabrik.de/south-america/mexico-latest.osm.pbf</a></li>
<li>apt-get install osmctools;</li>
<li>Convert your PBF, so you can merge all of them in one file: osmconvert peru-latest.osm.pbf -o=peru.o5m; osmconvert colombia-latest.osm.pbf -o=colombia.o5m; osmconvert chile-latest.osm.pbf -o=chile.o5m; osmconvert peru.o5m colombia.o5m chile.o5m -o=allcountries.o5m; osmconvert allcountries.o5m -o=allcountries.osm.pbf;</li>
<li>cd /yourNominatimFolder/build;</li>
<li>./utils/setup.php --osm-file data/allcountries.osm.pbf --all --osm2pgsql-cache 8000 2&gt;&amp;1 | tee setup.log</li>
<li>Take a coffee. :)</li>
</ol>
<p>If you have questions or need support, you can contact me: sistemas@aguilacontrol.com</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '16, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/68e2bb6560d2120152e8d951001aa4f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aguilacontrol&#39;s gravatar image" />
<p><span>aguilacontrol</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aguilacontrol has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50621" class="comments-container">
<span id="50622"></span>
<div id="comment-50622" class="comment">
<div id="post-50622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Step 3:</p>
<ul>
<li>wget <a href="http://download.geofabrik.de/south-america/peru-latest.osm.pbf">http://download.geofabrik.de/south-america/peru-latest.osm.pbf</a></li>
<li>wget <a href="http://download.geofabrik.de/south-america/chile-latest.osm.pbf">http://download.geofabrik.de/south-america/chile-latest.osm.pbf</a></li>
<li>wget <a href="http://download.geofabrik.de/south-america/colombia-latest.osm.pbf">http://download.geofabrik.de/south-america/colombia-latest.osm.pbf</a></li>
<li>wget <a href="http://download.geofabrik.de/south-america/mexico-latest.osm.pbf">http://download.geofabrik.de/south-america/mexico-latest.osm.pbf</a></li>
</ul>
<p>Step 5:</p>
<ul>
<li>osmconvert peru-latest.osm.pbf-o=peru.o5m;</li>
<li>osmconvert colombia-latest.osm.pbf -o=colombia.o5m;</li>
<li>osmconvert chile-latest.osm.pbf -o=chile.o5m;</li>
<li>osmconvert peru.o5m colombia.o5m chile.o5m -o=allcountries.o5m;</li>
<li>osmconvert allcountries.o5m -o=allcountries.osm.pbf;</li>
</ul>
</div>
<div id="comment-50622-info" class="comment-info">
<span class="comment-age">(04 Jul '16, 22:19)</span> <span class="comment-user userinfo">aguilacontrol</span>
</div>
</div>
<span id="53903"></span>
<div id="comment-53903" class="comment">
<div id="post-53903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi aguilacontrol, thank you for the very clear instructions. I'm currently in the process of the last line of point 5. After point 5 succeeds and I want to update the Nominatim database, is your recommendation to do (from the wiki)</p>
<p>rm settings/configuration.txt</p>
<p>./utils/setup.php --osmosis-init</p>
<p>./utils/setup.php --create-functions --enable-diff-updates</p>
<p>./utils/update.php --import-osmosis-all --no-npi</p>
<p>and then have coffee, or do something else?</p>
</div>
<div id="comment-53903-info" class="comment-info">
<span class="comment-age">(07 Jan '17, 14:14)</span> <span class="comment-user userinfo">OttoH</span>
</div>
</div>
</div>
<div id="comment-tools-50621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50621-form-container" class="comment-form-container">
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

