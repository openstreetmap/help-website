+++
type = "question"
title = "Automatically apply changeset to local OSM Rails stack"
description = '''I have setup a local OSM stack by following the instructions on INSTALL.md and CONFIGURE.md . I was able to do this without facing any major issues and loaded the database with a small portion of the map just to play around with it. Whenever I make an edit on the map, the changes are not applied to ...'''
date = "2017-06-29T22:10:00Z"
lastmod = "2017-07-06T22:45:00Z"
weight = 56805
keywords = [ "changeset", "editing", "rails", "localhost", "database" ]
aliases = [ "/questions/56805" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Automatically apply changeset to local OSM Rails stack](/questions/56805/automatically-apply-changeset-to-local-osm-rails-stack)

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
<span id="post-56805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56805-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have setup a local OSM stack by following the instructions on <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">INSTALL.md</a> and <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md">CONFIGURE.md</a> . I was able to do this without facing any major issues and loaded the database with a small portion of the map just to play around with it.</p>
<p>Whenever I make an edit on the map, the changes are not applied to the local database - I found this by querying via the website and also by exporting the data in the database to an .osm file using <em>osmosis</em> and searching for my edits in that. I wasn't able to find them</p>
<p>However, the changeset is created because when I go to my profile, I am able to see the changeset there. The only work around I was able to find for this is to download the changeset and manually apply the changeset to the database using <em>osmosis</em> . I came across this <a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated">answer</a> which suggests that whenever we save the changeset, it is immediately applied to the main database, and rendering could potentially take some time. I understand this, and I am not worried about the rendering part. I only want the changesets to get persisted to the database auotomatically.</p>
<p>Is there something different that I should be doing, or is this the expected behaviour?</p>
<p><strong>Edit:</strong> - To add more details I also tried to hit <a href="http://localhost:3000/api/0.6/node/1">http://localhost:3000/api/0.6/node/1</a> and <a href="http://localhost:3000/api/0.6/way/1/full">http://localhost:3000/api/0.6/way/1/full</a> -- which contains all the data that I edited.</p>
<p>The command that I am using to read data from DB and convert it to .osm is:</p>
<pre><code>osmosis --read-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot; user=&lt; username &gt; validateSchemaVersion=&quot;no&quot;   --log-progress interval=60  --write-xml file=db.osm</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '17, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/fa14b4df6993dc317311f422177fbd9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikhileshg92&#39;s gravatar image" />
<p><span>nikhileshg92</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikhileshg92 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '17, 01:15</strong> </span></p>
</div>
</div>
<div id="comments-container-56805" class="comments-container">
<span id="56807"></span>
<div id="comment-56807" class="comment">
<div id="post-56807-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In my experience editing both with iD directly on a local site, or via other editors with the API configuration pointing to a local server works without issues. Which editor are you using for testing?</p>
</div>
<div id="comment-56807-info" class="comment-info">
<span class="comment-age">(29 Jun '17, 23:27)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="56808"></span>
<div id="comment-56808" class="comment">
<div id="post-56808-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using iD. I just noticed something interesting in your comment. "with the API configuration pointing to a local server" - The Rails setup instructions don't say anything about this. Do I have to update a separate configuration?</p>
</div>
<div id="comment-56808-info" class="comment-info">
<span class="comment-age">(29 Jun '17, 23:33)</span> <span class="comment-user userinfo">nikhileshg92</span>
</div>
</div>
<span id="56824"></span>
<div id="comment-56824" class="comment">
<div id="post-56824-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>iD should be set up correctly if you followed the instructions, the only thing it needs is the OAuth configuration (I regularly use iD on my local instance to add test data).</p>
</div>
<div id="comment-56824-info" class="comment-info">
<span class="comment-age">(30 Jun '17, 23:42)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56805-form-container" class="comment-form-container">
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

<span id="56809"></span>

<div id="answer-container-56809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56809-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With regard to your addendum - it sounds that the data is indeed correctly added to your database, otherwise the localhost:3000 URLs would not work. Which means that when you write "the changes are not applied to the local database", you are mistaken. I don't know how you have determined that "the changes are not applied to the local database", but there must be an error in that reasoning.</p>
<p>You write that you're not interested in rendering for now, but are you sure that you are not perhaps looking at a local osm2pgsql-generated database (containing a copy of the data that is in your API database) and are you perhaps somehow expecting <em>that</em> database to get updated automatically? Because that won't happen unless you set up a process that dumps changes to the API database into .osc files (using Osmosis) that are then consumed by osm2pgsql.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '17, 06:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56809" class="comments-container">
<span id="56820"></span>
<div id="comment-56820" class="comment">
<div id="post-56820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I assumed the same thing, that everything works because the API requests work. So, as I mentioned in the question, the way I am trying to verify this is by exporting the database into a .osm file using osmosis. I have also pasted the corresponding command that I am using for that.</p>
<p>No where in my process I am using osm2pgsql. I use osmosis to load the data and osmosis to read from database and write to a file.</p>
</div>
<div id="comment-56820-info" class="comment-info">
<span class="comment-age">(30 Jun '17, 18:34)</span> <span class="comment-user userinfo">nikhileshg92</span>
</div>
</div>
<span id="56821"></span>
<div id="comment-56821" class="comment">
<div id="post-56821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You say that "you downloaded the changeset manually" and then "applied it to the database with osmosis", and that this worked. However, if you "download the changeset manually" then it clearly is already in the database (where else would you download it <em>from</em>?). Also the fact that you can get /node/1 etc. demonstrates that the data is in fact in the database. -- Is it possible that you have several databases, for example one "production" and one "development" and that your Rails API runs on the development database but your osmosis export runs on production (or vice versa)?</p>
</div>
<div id="comment-56821-info" class="comment-info">
<span class="comment-age">(30 Jun '17, 19:38)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="56921"></span>
<div id="comment-56921" class="comment">
<div id="post-56921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I finally realized what was happening. The data was getting saved into the DB like you said. The problem was with the way I was using osmosis to export it. the "--read-apidb" command reads from a different set of tables. I should be using "-read-apidb-current" which reads from the tables that contain the changes. I found this out by looking at the server logs when I query for my changes on the localhost and I found out that the API queries for data from the "current_nodes" table instead of "nodes".</p>
<p>Thanks for all the help!</p>
</div>
<div id="comment-56921-info" class="comment-info">
<span class="comment-age">(06 Jul '17, 22:35)</span> <span class="comment-user userinfo">nikhileshg92</span>
</div>
</div>
</div>
<div id="comment-tools-56809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56809-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56922"></span>

<div id="answer-container-56922" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56922-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found the solution myself with some help from Frederik who directed me to think about how I was using <em>osmosis</em></p>
<p>The data was getting saved into the DB which means my question is sort of void at this point. The problem was with the way I was using osmosis to export it. the "<a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.45#--read-apidb_.28--rd.29">--read-apidb</a>" command reads from a different set of tables. I should be using "<a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.45#--read-apidb-current_.28--rdcur.29">--read-apidb-current</a>" which reads from the tables that contain the changes. I found this out by looking at the server logs when I query for my changes on the localhost and I found out that the API queries for data from the "current_nodes" table instead of "nodes".</p>
<p>For example when I hit <em><a href="http://localhost:3000/api/0.6/node/1">http://localhost:3000/api/0.6/node/1</a></em> this is the log that I got:</p>
<p><code>Started GET "/api/0.6/node/1" for ::1 at 2017-07-06 14:43:36 -0700 Processing by NodeController#read as HTML Parameters: {"id"=&gt;"1"} Node Load (1.3ms) SELECT "current_nodes".* FROM "current_nodes" WHERE "current_nodes"."id" = $1 LIMIT 1 [["id", 1]] Changeset Load (0.5ms) SELECT "changesets".* FROM "changesets" WHERE "changesets"."id" = $1 LIMIT 1 [["id", 1]] User Load (12.9ms) SELECT "users".* FROM "users" WHERE "users"."id" = $1 LIMIT 1 [["id", 1]] NodeTag Load (0.9ms) SELECT "current_node_tags".* FROM "current_node_tags" WHERE "current_node_tags"."node_id" = $1 [["node_id", 1]] Rendered text template (0.1ms) Completed 200 OK in 72ms (Views: 7.5ms | ActiveRecord: 15.6ms)</code></p>
<p>This clearly shows that the API interacts with the <em>current_</em> <em>tables and hence using the other</em> osmosis* command helped me to resolve the issue</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '17, 22:45</strong></p>
<img src="https://secure.gravatar.com/avatar/fa14b4df6993dc317311f422177fbd9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikhileshg92&#39;s gravatar image" />
<p><span>nikhileshg92</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikhileshg92 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56922" class="comments-container">
&#10;</div>
<div id="comment-tools-56922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56922-form-container" class="comment-form-container">
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

