+++
type = "question"
title = "Full history dump database WITH timestamp"
description = '''Hello everyone, I&#x27;m currently trying to perform a historical analysis on OSM data. At the moment I have extracted my study areas from the full history dump using the bounding box command in Osmosis. Second to this, I have used osm2pgsql to input my data into a postgresql database (using the Postgres...'''
date = "2013-07-25T10:27:00Z"
lastmod = "2013-07-25T15:16:00Z"
weight = 24562
keywords = [ "timestamps", "postgres", "database" ]
aliases = [ "/questions/24562" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Full history dump database WITH timestamp](/questions/24562/full-history-dump-database-with-timestamp)

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
<span id="post-24562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24562-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I'm currently trying to perform a historical analysis on OSM data. At the moment I have extracted my study areas from the full history dump using the bounding box command in Osmosis. Second to this, I have used osm2pgsql to input my data into a postgresql database (using the Postgres app). However, I can find no option that would allow me to enter the timestamp as well. Supposedly, there was once a command "--extra-attributes" that would allow user_id and timestamp (and a few other variables) to be input into the database along with the remaining data. However, this no longer works.</p>
<p>Is there ANY way I can get my timestamps into my database? Either with Osmosis, Osm2pgsql or another software I am unfamiliar with?</p>
<p>All the best,</p>
<p>S</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '13, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d4a04e10efc69f43f9eefd6cd8e118b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SophieKS&#39;s gravatar image" />
<p><span>SophieKS</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SophieKS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24562" class="comments-container">
&#10;</div>
<div id="comment-tools-24562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24562-form-container" class="comment-form-container">
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

<span id="24563"></span>

<div id="answer-container-24563" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24563-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If --extra-attributes really doesn't work then please submit a bug report here:</p>
<p><a href="https://github.com/openstreetmap/osm2pgsql">https://github.com/openstreetmap/osm2pgsql</a></p>
<p>Also, you should be able to retrieve an earlier version of osm2pgsql from that repository where --extra-attributes still worked.</p>
<p>Note that this will greatly blow up your storage requirements. 5.9.119.141 A potential workaround for the problem is writing a small tool that reads an OSM file, takes the time stamp of an object, and inserts it as a tag. I.e. if there's a</p>
<pre><code>&lt;node id=&quot;1&quot; timestamp=&quot;something&quot; lat=&quot;1&quot; lon=&quot;2&quot; user=&quot;fred&quot; user_id=&quot;3&quot; changeset=&quot;4&quot; /&gt;</code></pre>
<p>in the input, it creates</p>
<pre><code>&lt;node id=&quot;1&quot; timestamp=&quot;something&quot; lat=&quot;1&quot; lon=&quot;2&quot; user=&quot;fred&quot; user_id=&quot;3&quot; changeset=&quot;4&quot;&gt;
&lt;tag k=&quot;timestamp&quot; v=&quot;something&quot; /&gt;
&lt;/node&gt;</code></pre>
<p>That would be easy to do in most scripting languages that have an XML parser. Here's an Osmium based C++ solution: <a href="https://github.com/woodpeck/osmium_based_utils/blob/master/add_timestamp.cpp">https://github.com/woodpeck/osmium_based_utils/blob/master/add_timestamp.cpp</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '13, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '13, 18:48</strong> </span></p>
</div>
</div>
<div id="comments-container-24563" class="comments-container">
<span id="24564"></span>
<div id="comment-24564" class="comment">
<div id="post-24564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik,</p>
<p>As far as this post states... <a href="http://www.mail-archive.com/dev@openstreetmap.org/msg19527.html...">http://www.mail-archive.com/dev@openstreetmap.org/msg19527.html...</a> someone has already created a ticket about the bug.</p>
<p>Thanks for your comments. It's a great help.</p>
<p>S.</p>
</div>
<div id="comment-24564-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 12:10)</span> <span class="comment-user userinfo">SophieKS</span>
</div>
</div>
<span id="24567"></span>
<div id="comment-24567" class="comment">
<div id="post-24567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the problem is the PBF parser (as implied in that message), then why don't you convert to .osm XML with Osmosis and import that: osmosis --read-pbf my.file.osm.pbf --write-xml - | osm2pgsql ...</p>
</div>
<div id="comment-24567-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 13:14)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="24569"></span>
<div id="comment-24569" class="comment">
<div id="post-24569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have tried using .osh file. Do you think converting from an .osh to .osm would make any difference?</p>
<p>S.</p>
</div>
<div id="comment-24569-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 13:28)</span> <span class="comment-user userinfo">SophieKS</span>
</div>
</div>
<span id="24572"></span>
<div id="comment-24572" class="comment">
<div id="post-24572-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am surprised that an .osh file would even work given that it contains multiple versions of each object. What is your desired outcome? osm2pgsql will <em>certainly</em> not import more than one version of each object into the database - likely the latest. I would have thought it would just abort due to the same object being there twice. Having said that, yes, .osh is XML and would use the XML parser.</p>
</div>
<div id="comment-24572-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 15:16)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24563-form-container" class="comment-form-container">
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

