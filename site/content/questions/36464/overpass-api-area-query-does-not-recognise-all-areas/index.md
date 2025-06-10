+++
type = "question"
title = "Overpass API area query does not recognise all areas!"
description = '''Hello,  After installing a fresh version of the overpass api on my private server, I have imported a planet file (http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/planet/planet-latest.osm.bz2) and most of the features are running smoothly. However, running is_in area queries only ...'''
date = "2014-08-31T23:46:00Z"
lastmod = "2014-09-14T19:51:00Z"
weight = 36464
keywords = [ "overpass", "problem", "api", "query", "area" ]
aliases = [ "/questions/36464" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API area query does not recognise all areas!](/questions/36464/overpass-api-area-query-does-not-recognise-all-areas)

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
<span id="post-36464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36464-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>After installing a fresh version of the overpass api on my private server, I have imported a planet file (<a href="http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/planet/planet-latest.osm.bz2)">http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/planet/planet-latest.osm.bz2)</a> and most of the features are running smoothly. However, running <code>is_in</code> area queries only returns some areas like countries, rather than more specific areas like buildings. Has anyone encountered a problem like this before? There doesn't seem to be any sort of documentation on this matter. I have not altered the <code>areas.osm3s</code> file and am running version osm3s_v0.7.50.</p>
<p>Example problem:</p>
<p>If I run this request from the public server:</p>
<pre><code>http://overpass-api.de/api/interpreter?data=%0A%5Bout%3Ajson%5D%3B%0Ais_in(40.70523754289769%2C-74.05129551887512)%3Bout%3B%0A</code></pre>
<p>(should return Liberty State Park as an area),</p>
<p>my custom server does not return Liberty State Park, but does return everything else. Does anyone know what the problem here could be?</p>
<p>Thanks to everyone.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '14, 23:46</strong></p>
<img src="https://secure.gravatar.com/avatar/5abb2932327bb97ee8a2abc3c14caa8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister4&#39;s gravatar image" />
<p><span>gmeister4</span><br />
<span class="score" title="60 reputation points">60</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister4 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36464" class="comments-container">
&#10;</div>
<div id="comment-tools-36464" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36464-form-container" class="comment-form-container">
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

<span id="36808"></span>

<div id="answer-container-36808" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36808-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gmeister4 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I could import a 26GB pbf planet file into my local Overpass API instance on my laptop (4GB RAM, SSD, 16GB swap space) without much issue. Database import took around 38 hours, area creation around 6 hours. Total disk usage now is about 182GB for the database. Note: No attic data at this time (I don't need it right now).</p>
<p>For the area creation I used the original script, but had to increase the element-limit to "2073741824" - otherwise the script would terminate with a runtime error "Query run out of memory in "recurse" at line 255 using about 1157 MB" as you mentioned. This is not an OS level error but enforced by Overpass API itself.</p>
<p>I could not reproduce the missing tags as you describe it. However, I removed all "area*" files in the database directory after a failed area creation before trying again. Not sure, if this is really necessary. Just wanted to give it a clean start.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '14, 18:13</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '14, 18:13</strong> </span></p>
</div>
</div>
<div id="comments-container-36808" class="comments-container">
<span id="36819"></span>
<div id="comment-36819" class="comment">
<div id="post-36819-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This did it! You are a life saver mmd! I had tried increasing the <code>element-limit</code> to 3073741824 before, but this did not work. I cleaned up the old area files and used your recommended limit which did the trick.</p>
<p>For the record, the missing tags were arising from replacing the area rules file with the <code>areas_low_ram.osm3s</code> from the overpass misc folder, which would complete the batch runs but like I said, would leave missing tags from the area elements. Thanks again! You are like the patron saint of the overpass api!</p>
</div>
<div id="comment-36819-info" class="comment-info">
<span class="comment-age">(14 Sep '14, 19:51)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
</div>
<div id="comment-tools-36808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36808-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36469"></span>

<div id="answer-container-36469" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36469-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please check the following things:</p>
<ul>
<li>does "way(27459219);out meta;" find the Liberty Park outline and has it a name tag and a tag "leisure=park", and is it version 25?</li>
<li>does the areas.osm3s in $DB_DIR/rules contain the rule for "leisure" (I know it's unchanged but just in case)</li>
<li>Are there two dispatcher processes running (one with --osm-base and one with --areas)?</li>
<li>What is the content of $DB_DIR/rules_loop.out (last 10 lines should be sufficient)?</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '14, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '14, 07:38</strong> </span></p>
</div>
</div>
<div id="comments-container-36469" class="comments-container">
<span id="36471"></span>
<div id="comment-36471" class="comment">
<div id="post-36471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response,</p>
<ul>
<li>"way(27459219);out;" finds Liberty Park, it has a name and leisure tag (but I do not have metadata so cannot see version number)</li>
<li>rules contains the leisure node</li>
<li>Both dispatcher processes are running</li>
<li>Last 9 lines of rules_loop.log are:</li>
</ul>
<p>2014-08-31 22:49:36: update started 2014-08-31 23:54:41: update finished 2014-08-31 23:54:44: update started 2014-09-01 01:00:35: update finished 2014-09-01 01:00:38: update started 2014-09-01 02:05:22: update finished 2014-09-01 02:05:25: update started 2014-09-01 03:09:48: update finished 2014-09-01 03:09:51: update started</p>
</div>
<div id="comment-36471-info" class="comment-info">
<span class="comment-age">(01 Sep '14, 08:32)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
<span id="36476"></span>
<div id="comment-36476" class="comment">
<div id="post-36476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any suggestions as to what could be going wrong? All other node/ way queries work that I have tried so far</p>
</div>
<div id="comment-36476-info" class="comment-info">
<span class="comment-age">(01 Sep '14, 15:19)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
<span id="36477"></span>
<div id="comment-36477" class="comment">
<div id="post-36477-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At least it is nothing obvious. The area generation is suspiciously fast (should be closer to 7 hours than to 1.5 hours). So I would ask you to check</p>
<ul>
<li><p>Does "area[leisure=park];out ids;" have any results?</p></li>
<li><p>When you look at $EXEC_DIR/bin/nohup.out, do you have a line containing the term "part 0, on line 257" (or line 255)? This would tell us whether the area generation terminates for some reason in between.</p></li>
</ul>
</div>
<div id="comment-36477-info" class="comment-info">
<span class="comment-age">(01 Sep '14, 16:55)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="36479"></span>
<div id="comment-36479" class="comment">
<div id="post-36479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Area[leisure = park] does return around 4500 id's, however, $EXEC_DIR/bin/nohup.out does not exist but you were right! in /root/nohup.out I have found <code>After 1h4m32s: in "recurse", part 0, on line 255. Stack: 1 of 3884956 0 of 1</code> and also <code>runtime error: Query run out of memory in "recurse" at line 255 using about 1157 MB of RAM.</code>. My server has 4gb. Note: My server is running 99.9% RAM load, with 'top' telling me that osm3s_query is running heavy:</p>
<p>6898 root 20 0 725m 215m 872 R 94.2 5.3 19:51.32 osm3s_query</p>
<p>What can I do to rectify this? Thanks Roland.</p>
</div>
<div id="comment-36479-info" class="comment-info">
<span class="comment-age">(01 Sep '14, 18:34)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
<span id="36481"></span>
<div id="comment-36481" class="comment">
<div id="post-36481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please replace the areas.osm3s in $DB_DIR/rules by the file <a href="http://overpass-api.de/misc/areas_low_ram.osm3s">http://overpass-api.de/misc/areas_low_ram.osm3s</a></p>
<p>It contains the same queries, but it generates areas immediately after each block. It is probably slower, but it should use less RAM.</p>
<p>A second approach would be to raise the number 1073741824 in the first line of areas.osm3s or its replacement. That is the soft upper limit of RAM the query should use. But it likely won't help much if the script is killed by the operating system instead of the scheduler, because it hits the hard limit of 4GB RAM minus other processes.</p>
</div>
<div id="comment-36481-info" class="comment-info">
<span class="comment-age">(01 Sep '14, 19:16)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="36548"></span>
<div id="comment-36548" class="comment not_top_scorer">
<div id="post-36548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have managed to complete the first block in 8h 30m with the areas_low_ram. All of the areas are now showing up, but many of the areas do not have all their correct tags, such as the 'name' tag. Is this due to the modified script? Or should these tags appear after successive blocks?</p>
</div>
<div id="comment-36548-info" class="comment-info">
<span class="comment-age">(03 Sep '14, 09:56)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
<span id="36590"></span>
<div id="comment-36590" class="comment not_top_scorer">
<div id="post-36590-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Still not the correct tags</p>
</div>
<div id="comment-36590-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 11:27)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
</div>
<div id="comment-tools-36469" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-36469-form-container" class="comment-form-container">
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

