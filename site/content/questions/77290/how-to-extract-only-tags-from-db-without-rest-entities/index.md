+++
type = "question"
title = "How to extract only tags from DB without rest entities"
description = '''The problem which I faced is quite complex. I work with OSM editor where I can override some ways properties. Those properties are tags called &quot;maxspeed:backward&quot; and &quot;maxspeed:forward&quot;. Sometimes I want to update my local map with OSM official data (new roads, roads under constructions etc.).  What...'''
date = "2020-10-28T14:45:00Z"
lastmod = "2020-11-04T11:06:00Z"
weight = 77290
keywords = [ "filter", "merge", "osmfilter", "osmosis", "tagging" ]
aliases = [ "/questions/77290" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract only tags from DB without rest entities](/questions/77290/how-to-extract-only-tags-from-db-without-rest-entities)

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
<span id="post-77290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77290-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The problem which I faced is quite complex. I work with OSM editor where I can override some ways properties. Those properties are tags called "maxspeed:backward" and "maxspeed:forward". Sometimes I want to update my local map with OSM official data (new roads, roads under constructions etc.).<br />
What I want is to merge my local map with official osm to keep all road and nodes changes from official source but keep my tags with values from editor. I work with Postgres DB, osmosis (merge tool), osmfilter and osmconvert tools.<br />
<br />
This is process which I found out:<br />
1. Take my local map from editor and filter out only tags. With no nodes, ways, relations.<br />
2. Take official OSM map and filter out only tags (the same as step 1)<br />
3. Merge those sources with osmosis with conflictResult strategy - my local tag values override official OSM map.<br />
4. Again take official OSM map but now I drop tags, so I get full map without tags I'm using.<br />
5. Merge result from step 3 (correct tags and values) with result from step 4 (official map without tags) with conflictResult strategy - official map nodes override my local.<br />
<br />
What I want to achieve is go teg most current map with my own tags.<br />
I have a problem with step 1. Can I retrieve from DB ONLY tags? Without any nodes or another informations which could override official map in step 5? What I can see in DB tags are placed in separate table and has got reference to whe <code>way_id</code>, so if I merge that values with another source with the same <code>way_id</code>.<br />
<br />
What I try with osmfilter is:<br />
<code>./osmfilter $EDITED_OSM_NAME --keep-tags="all maxspeed:backward= maxspeed:forward= maxspeed=" -o=$EDITED_OSM_TAGS</code><br />
It filter correctly- only listed tags are in output pbf file, but is there any possibility to retreive them without any nodes,ways,relations etc?<br />
<br />
I have also tried something with<br />
<code>--drop-relations</code>,<code>--drop-ways</code>,<code>--drop-nodes</code>, <code>--ignore-dependencies</code> but it didn't work the way I wish.<br />
<br />
Thank you in advance for help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '20, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '20, 09:20</strong> </span></p>
</div>
</div>
<div id="comments-container-77290" class="comments-container">
&#10;</div>
<div id="comment-tools-77290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77290-form-container" class="comment-form-container">
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

<span id="77318"></span>

<div id="answer-container-77318" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77318-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello! Try to use QGis, I once found instructions in yuotube on how to sort and unload certain tags, try to search, if you can't find it, I'll try to find it then and send it exactly where I saw it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '20, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0bfd43e5ecd2d06a1e20975a1e024514?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viki_travel_weak&#39;s gravatar image" />
<p><span>Viki_travel_...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viki_travel_weak has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-77318" class="comments-container">
&#10;</div>
<div id="comment-tools-77318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77318-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77393"></span>

<div id="answer-container-77393" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77393-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe my answer will be valuable for anyone who faces the same problem.<br />
Just to remind, I want to download official OSM map but keep my local informations (in my case <code>maxspeed</code> tags).<br />
Process which I wrote goes like this:<br />
1) When my current changes are saved in local OSM editor, than I run my SQL script directly on Postgres database. That script export all tags from <code>maxspeed</code>, <code>maxspedd:forward</code>, <code>maxspeed:backward</code> from <code>way_tags</code> table to the CSV file.</p>
<hr />
<pre><code>CREATE TABLE IF NOT EXISTS temp_tags (LIKE way_tags);
ALTER TABLE temp_tags 
ADD COLUMN IF NOT EXISTS ah_edited boolean default TRUE;
&#10;ALTER TABLE way_tags
ADD COLUMN IF NOT EXISTS ah_edited boolean DEFAULT FALSE;
&#10;
COPY 
  (SELECT DISTINCT ON(way_id, k)
  way_tags.way_id, way_tags.k, way_tags.v, way_tags.version, way_tags.ah_edited
  FROM way_tags
  JOIN ways ON way_tags.way_id = ways.way_id AND way_tags.version = ways.version
  JOIN changesets on ways.changeset_id=changesets.id
  JOIN users ON changesets.user_id=users.id
  WHERE (k like &#39;maxspeed:backward&#39;
         OR k like &#39;maxspeed:forward&#39;
         OR k like &#39;maxspeed&#39;)
  AND ((users.email like &#39;%admin.com%&#39; AND ways.changeset_id != 0)
        OR way_tags.ah_edited = TRUE)
  ORDER BY way_id, k, version desc)  TO STDOUT (format csv, delimiter &#39;;&#39;, header false);
&#10;ALTER TABLE way_tags
DROP COLUMN IF EXISTS ah_edited;
&#10;DROP TABLE IF EXISTS temp_tags;</code></pre>
<hr />
<p>As some can notice I use additional column <code>ah_edited</code> just to keep information that information is my edited one and should overwrite the "world" data if exists with the same tag.<br />
After doing SAVE in OSM editor, in fact we save two copies of the same tags but with different version and incremented <code>changeset_id</code> - that's why I look for tags which has that value !=0, and I use DISTINCT ON function which returns higher version value (after my modifications).<br />
Thanks to that I got an CSV with my tags which I want to keep in the future downloaded map.<br />
<br />
2) Truncate DB<br />
3) Download latest map version from geofabrik.de<br />
4) Upload map to the database<br />
</p>
<p><em>Here lets pause for a moment<br />
Our data we can divide into two groups -&gt; completely new tags for some ways, and already existing in official maps but our values should overwrite them. That's why I divided that process into two parts.</em><br />
<br />
5) Insert new values to the DB -- Get table to the original structure</p>
<pre><code>ALTER TABLE way_tags
ADD COLUMN IF NOT EXISTS ah_edited boolean default FALSE;
&#10;--  Create temp table from CSV which holds pre-merge changes
CREATE TABLE IF NOT EXISTS temp_tags (LIKE way_tags);
&#10;COPY temp_tags(way_id, k, v, version, ah_edited) FROM &#39;/home/map-data/exportedTags.csv&#39;     (FORMAT csv, delimiter &#39;;&#39;, header false);
&#10;--  Add edidtion column to the way_tags and insert unique values which only AH added
&#10;INSERT INTO way_tags (way_id, k, v, version, ah_edited)
SELECT temp_tags.way_id, temp_tags.k, temp_tags.v, w.version, temp_tags.ah_edited  
FROM temp_tags 
FULL JOIN way_tags ON temp_tags.way_id = way_tags.way_id AND temp_tags.k like way_tags.k
JOIN ways w ON w.way_id = temp_tags.way_id
WHERE way_tags.way_id IS NULL;
&#10;--  DROP temp table from CSV which holds pre-merge changes
DROP TABLE public.temp_tags;</code></pre>
<p><br />
6) Next we update already existing values CREATE TABLE IF NOT EXISTS temp_tags (LIKE way_tags); ALTER TABLE temp_tags ADD COLUMN IF NOT EXISTS ah_edited boolean default true;</p>
<pre><code>COPY temp_tags(way_id, k, v, version, ah_edited) FROM &#39;/home/map-data/exportedTags.csv&#39; (FORMAT csv, delimiter &#39;;&#39;, header false);
&#10;UPDATE temp_tags SET ah_edited= TRUE;
&#10;
--  Add edidtion column to the way_tags and insert unique values which only AH added
&#10;ALTER TABLE way_tags
ADD COLUMN IF NOT EXISTS ah_edited boolean default FALSE;
&#10;UPDATE way_tags 
SET v=csv_source.v, ah_edited = true
FROM  temp_tags csv_source 
WHERE csv_source.way_id = way_tags.way_id
AND csv_source.k like way_tags.k
AND csv_source.ah_edited = true;
&#10;--  DROP temp table from CSV which holds pre-merge changes
DROP TABLE public.temp_tags;</code></pre>
<p><br />
<em>I know that I create and drop temporal tables every time, but every script is written to be executable independly</em><br />
Almost done. Thanks to that We have got our datas in DB but... are not visible in editor. During read process PBF to the editor some inner structures are created that's why We need to save our map to the PBF file and reaload again.<br />
And again little problem... OSM doesn't know our <code>ah_edited</code> column values. He will restore column, but not values. That way I need to run one little script:<br />
</p>
<pre><code>--  Create temp table from CSV which holds pre-merge changes
CREATE TABLE IF NOT EXISTS temp_tags (LIKE way_tags);
&#10;ALTER TABLE temp_tags 
ADD COLUMN IF NOT EXISTS ah_edited boolean default TRUE;
&#10;COPY temp_tags(way_id, k, v, version, ah_edited) FROM &#39;/home/map-data/exportedTags.csv&#39; (FORMAT csv, delimiter &#39;;&#39;, header false);
&#10;--  Add edidtion column to the way_tags and insert unique values which only AH added
&#10;ALTER TABLE way_tags
ADD COLUMN IF NOT EXISTS ah_edited boolean default FALSE;
&#10;UPDATE way_tags 
SET ah_edited = true
FROM  temp_tags
WHERE way_tags.way_id = temp_tags.way_id
AND way_tags.k = temp_tags.k;
&#10;--  DROP temp table from CSV which holds pre-merge changes
DROP TABLE public.temp_tags;</code></pre>
<p>Voila! Done. We have new OSM map with our custom tags transferred.<br />
Additional information. I use additional column <code>ah_edited</code> to keep information for the further process that one specific values are edited by me, and I want it to be exported into CSV in the future. After that process, our changeset_id values are set to 0 so we don't have any current information which informations were changed by me as owner -&gt; that's why I use <code>ah_edited</code> column.<br />
<br />
P.S. I know it's complicated, but it works and I couldn't find any answer for my question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '20, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '20, 11:10</strong> </span></p>
</div>
</div>
<div id="comments-container-77393" class="comments-container">
&#10;</div>
<div id="comment-tools-77393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77393-form-container" class="comment-form-container">
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

