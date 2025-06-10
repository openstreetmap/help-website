+++
type = "question"
title = "Postgres DB SQL calls resulting in inconsistent results"
description = '''Hello OSM, As mentioned here, I have an extract of a recent planet file created with Osmosis (with the command line arguement that keeps ways even if they extend outside the cut polygon). I dumped the extract into a Postgres database using the snapshot schema. I then have a Java program that calls t...'''
date = "2012-08-29T10:18:00Z"
lastmod = "2012-08-29T20:32:00Z"
weight = 15633
keywords = [ "postgres", "osmosis", "sql" ]
aliases = [ "/questions/15633" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Postgres DB SQL calls resulting in inconsistent results](/questions/15633/postgres-db-sql-calls-resulting-in-inconsistent-results)

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
<span id="post-15633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15633-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OSM,</p>
<p>As mentioned <a href="http://help.openstreetmap.org/questions/15496/sql-statement-to-get-all-of-the-xy-pairs-from-a-way">here</a>, I have an extract of a recent planet file created with Osmosis (with the command line arguement that keeps ways even if they extend outside the cut polygon). I dumped the extract into a Postgres database using the snapshot schema. I then have a Java program that calls the following two SQL statements in two nested loops to draw the data.</p>
<pre><code>OUTER LOOP BEGIN
     &quot;SELECT nodes, id from public.ways LIMIT 1 OFFSET&quot; + val
     INNER LOOP BEGIN
          &quot;SELECT ST_X(geom) as x, ST_Y(geom) as y from public.nodes WHERE id=&quot; + nodes[i] + &quot;LIMIT 1&quot;
     INNER LOOP END
     val++
OUTER LOOP END</code></pre>
<p>When I run this, if a node belonging to a given way is not found, my program fires off a message to the log and keeps chugging. I have noticed that these logs are showing up in a VERY inconsistent fashion. To demonstrate this, I took the outer loop of my program and clamped it to only loop 1000 times (IE draw 1000 ways) and ran the program twice, which should yield the same results. This is what I got...</p>
<p><img src="http://help.openstreetmap.org/upfiles/osmwtf.jpg" alt="alt text" /></p>
<p>Now please understand that I already know that:</p>
<p>A. Planet files dumps take hours so SOME nodes will be missing unless you grab a daily build and use Osmosis to update your planet file...</p>
<p>B. My extract included ways that crossed my cut polygon, for my needs I require the entire road system to be intact.</p>
<p>But this is different, this is one isolated database and one program asking it for the same exact data, and I'm getting inconsistencies between runs which is driving me mad! I don't understand it at all. Do I need to order this data by the id in order to get consistent results? Is this a Postgres "thing" or should I be looking for some kind of illusive bug in my program (which is pretty strait-forward)? Any help would be vastly appreciated.</p>
<p>Thanks, -Cody</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '12, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/aa9f28cc449a272dbd654e8edf660877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smartkid&#39;s gravatar image" />
<p><span>Smartkid</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smartkid has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '12, 10:27</strong> </span></p>
</div>
</div>
<div id="comments-container-15633" class="comments-container">
&#10;</div>
<div id="comment-tools-15633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15633-form-container" class="comment-form-container">
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

<span id="15662"></span>

<div id="answer-container-15662" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15662-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I figured it out, for anyone who stumbles upon this in the future I'm going to break down the problem.</p>
<p>I made a dumb noob mistake by writing a function that executed my SQL statement for me and returned a ResultSet which I then operated on in my main loop. Problem is this little line found in the JavaDocs on <a href="http://docs.oracle.com/javase/1.5.0/docs/api/java/sql/ResultSet.html">ResultSet</a>...</p>
<pre><code>A ResultSet object is automatically closed when the Statement object that generated it is closed, re-executed, or used to retrieve the next result from a sequence of multiple results.</code></pre>
<p>With that alone the problem becomes obvious, my function is closing - leaving the SQL statement object unreferenced and thus a target for garbage collection. Most of the time the garbage collection wasn't getting to the statement object in time to cause problems, but sometimes it was able to which resulted in my rs.getDouble statements throwing seemingly random SQL Exceptions, which registered in my program as a missing point (because with OSM we have to assume that some nodes are in fact missing).</p>
<p>Case closed, hope this helps someone out there eventually... -Cody</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/aa9f28cc449a272dbd654e8edf660877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smartkid&#39;s gravatar image" />
<p><span>Smartkid</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smartkid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15662" class="comments-container">
&#10;</div>
<div id="comment-tools-15662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15662-form-container" class="comment-form-container">
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

