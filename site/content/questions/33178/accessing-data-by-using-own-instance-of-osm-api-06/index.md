+++
type = "question"
title = "Accessing data by using own instance of OSM API 0.6"
description = '''Hello all, For developing purposes I&#x27;ve started to set up my own OSM infrastructure. The first step was, to install the overall OSM-Website. The github page states that the rails port includes the website itself (including the web front-end, user management, diary functions...), the editors, GPX Upl...'''
date = "2014-05-14T17:44:00Z"
lastmod = "2014-05-14T19:03:00Z"
weight = 33178
keywords = [ "openstreetmap", "api", "installation", "server" ]
aliases = [ "/questions/33178" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Accessing data by using own instance of OSM API 0.6](/questions/33178/accessing-data-by-using-own-instance-of-osm-api-06)

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
<span id="post-33178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33178-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,<br />
For developing purposes I've started to set up my own OSM infrastructure. The first step was, to install the overall OSM-Website. The <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/VAGRANT.md">github page</a> states that the rails port includes the website itself (including the web front-end, user management, diary functions...), the editors, GPX Uploader and the XML based API 0.6.<br />
For this question I want to concentrate on the OSM XML API 0.6 (more questions will pop up later on but to keep it as simple as possible, I will ask different type of questions in separate threads).<br />
</p>
<p>So...I've set up the osm website and I've also followed the <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md">Configuration Steps</a>. Now I've tested the website. I can browse the web frontend (it seems everything is working) and user management also works. Next step was to test the API.</p>
<hr />
<p>I've created some fist requests using a REST-Console and made the following queries:<br />
Creating a changeset using the following URL:</p>
<blockquote>
<p>localhost:3000/api/0.6/changeset/create</p>
</blockquote>
<p>And the following input using PUT:<br />
&lt;osm&gt;<br />
&lt;changeset&gt;<br />
&lt;tag k="created_by" v="JOSM 1.61"/&gt;<br />
&lt;tag k="comment" v="Just a comment"/&gt;<br />
&lt;/changeset&gt;<br />
&lt;/osm&gt;</p>
<p>This gives me a reasonable output of showing me a number. For example<br />
</p>
<blockquote>
<p>4</p>
</blockquote>
<p>So...I would assume that this is working, right?</p>
<hr />
<p>I've made another request by using GET with:<br />
</p>
<blockquote>
<p>192.168.178.66:3000/api/capabilities</p>
</blockquote>
<p>This gives me the following response:</p>
<p>&lt;?xml version="1.0" encoding="UTF-8"?&gt;<br />
&lt;osm version="0.6" generator="OpenStreetMap server" copyright="OpenStreetMap and contributors" attribution="http://www.openstreetmap.org/copyright" license="http://opendatacommons.org/licenses/odbl/1-0/"&gt;<br />
&lt;api&gt;<br />
&lt;version minimum="0.6" maximum="0.6"/&gt;<br />
&lt;area maximum="0.25"/&gt;<br />
&lt;tracepoints per_page="5000"/&gt;<br />
&lt;waynodes maximum="2000"/&gt;<br />
&lt;changesets maximum_elements="50000"/&gt;<br />
&lt;timeout seconds="300"/&gt;<br />
&lt;status database="online" api="online" gpx="online"/&gt;<br />
&lt;/api&gt;<br />
&lt;/osm&gt;</p>
<p>Looks like that this is also working.</p>
<hr />
<p>Now I want to get some data using the API, so I've tested this by using the following GET request, but there is nothing as a output. But actually this should give me the same output than using the openstreetmao.org link below, shouldn't it?</p>
<blockquote>
<p>localhost:3000/api/0.6/node/271428118<br />
<a href="http://www.openstreetmap.org/api/0.6/node/271428118">http://www.openstreetmap.org/api/0.6/node/271428118</a></p>
</blockquote>
<p>I've also tested it with a request using a bounding box, which offers, using the openstreetmap.org website a map.osm file download. Using my localhost instance, I get nothing. The site/connection is not available.</p>
<hr />
<p>So...for this part I have the question of how to get data using my own openstreetmap instance including the API. Hopefully I haven't missed anything.</p>
<p>Thanks for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '14, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/6fc6f0ce6b15926034073d61c76482fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schlomm&#39;s gravatar image" />
<p><span>schlomm</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schlomm has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33178" class="comments-container">
&#10;</div>
<div id="comment-tools-33178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33178-form-container" class="comment-form-container">
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

<span id="33181"></span>

<div id="answer-container-33181" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33181-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have not loaded anything into your database. Your installation is a totally separate one that knows nothing about any data that might exist in OpenStreetMap. Node 271428118 is a pub in Germany in OSM but the node with that ID could be a bus stop in Brazil in your database - or, more likely, just not exist in your database.</p>
<p>You can use <a href="http:://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> to load OSM data into your database (look for the <code>--write-apidb</code> task) but always remember, even if you do that, your database and OSM's database are two totally separate copies and changes to one do not influence the other.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '14, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33181" class="comments-container">
<span id="33182"></span>
<div id="comment-33182" class="comment">
<div id="post-33182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the explanation.Very helpful.Until now I haven't realized that my OSM-Website wants/tries to access other/local/own data than these from openstreetmap.org itself (although I've check the component overview about the OSM-Architecture before I've started). I've read through the setup guides, but I didn't find something regarding on how to integrate a own data-source as well as a own Tile-Server. Do you have any information about this? Of course I can create a new question about "How to integrate other services?" in another question - might be the best way of providing a good overview.</p>
</div>
<div id="comment-33182-info" class="comment-info">
<span class="comment-age">(14 May '14, 19:03)</span> <span class="comment-user userinfo">schlomm</span>
</div>
</div>
</div>
<div id="comment-tools-33181" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33181-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

