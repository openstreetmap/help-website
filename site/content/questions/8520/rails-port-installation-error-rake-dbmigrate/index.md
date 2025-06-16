+++
type = "question"
title = "[closed] Rails port installation error: rake db:migrate"
description = '''I followed this tutorial to setup an osm server: http://www.hyperionreactor.net/blog/how-build-your-own-osm-server-part-1-postgis-and-mapnik I&#x27;m still trying to make mapnik generate me images, but other than that everything worked well. Meanwhile i started to follow the official The Rails Port tutor...'''
date = "2011-10-20T08:58:00Z"
lastmod = "2011-10-20T10:21:00Z"
weight = 8520
keywords = [ "osm", "rails" ]
aliases = [ "/questions/8520" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Rails port installation error: rake db:migrate](/questions/8520/rails-port-installation-error-rake-dbmigrate)

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
<span id="post-8520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8520-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I followed this tutorial to setup an osm server: <a href="http://www.hyperionreactor.net/blog/how-build-your-own-osm-server-part-1-postgis-and-mapnik">http://www.hyperionreactor.net/blog/how-build-your-own-osm-server-part-1-postgis-and-mapnik</a> I'm still trying to make mapnik generate me images, but other than that everything worked well. Meanwhile i started to follow the official The Rails Port tutorial and i almost finished. (<a href="https://wiki.openstreetmap.org/wiki/Rails_on_Ubuntu">rails on ubuntu</a> and <a href="https://wiki.openstreetmap.org/wiki/The_Rails_Port">rails port</a>) This is the command i'm stuck at:</p>
<pre><code>alexandru@alex-lap:~/.osm/rail_port/rails$ rake db:migrate
rake/rdoctask is deprecated.  Use rdoc/task instead (in RDoc 2.4.2+)
Please install RDoc 2.4.2+ to generate documentation.
rake aborted!
fe_sendauth: no password supplied
Tasks: TOP =&gt; db:migrate
(See full trace by running task with --trace)</code></pre>
But also knowing that i already had setup my db in my first tutorial i went ahead and launched the server. If that would be of any help, this was the error:
<blockquote>
<p>The OpenStreetMap server encountered an unexpected condition that prevented it from fulfilling the request (HTTP 500)</p>
<p>Feel free to contact the OpenStreetMap community if your problem persists. Make a note of the exact URL / post data of your request.</p>
<p>This may be a problem in our Ruby On Rails code. 500 occurs with exceptions thrown outside of an action (like in Dispatcher setups or broken Ruby code)</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '11, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>20 Oct '11, 10:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-8520" class="comments-container">
&#10;</div>
<div id="comment-tools-8520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8520-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Not a simple question with a straightforward answer. You can get help with technical issues by subscribing to the OSM-dev mailing list." by Jonathan Bennett 20 Oct '11, 10:21

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8521"></span>

<div id="answer-container-8521" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8521-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first tutorial showed you how to set up a PostGIS rendering database using osm2pgsql for use with Mapnik.</p>
<p>This is <em>not</em> the same database used by the Rails port. The latter uses a Postgres database without PostGIS extensions and with a very different schema. You will need to set up the new database despite already having a rendering database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '11, 09:08</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8521" class="comments-container">
<span id="8522"></span>
<div id="comment-8522" class="comment">
<div id="post-8522-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much! Btw, i just fixed my problem. It was in the database.yml, i had users and their passwords commented out. Now everything works. But CAN YOU PLEASE TELL ME then why do i have the whole map available at localhost?</p>
</div>
<div id="comment-8522-info" class="comment-info">
<span class="comment-age">(20 Oct '11, 09:22)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8524"></span>
<div id="comment-8524" class="comment">
<div id="post-8524-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Because the web site doesn't render maps directly from it's own database. Instead it displays tiles from (by default) <a href="http://tile.openstreetmap.org">tile.openstreetmap.org</a> which naturally includes all data in the main database.</p>
</div>
<div id="comment-8524-info" class="comment-info">
<span class="comment-age">(20 Oct '11, 10:21)</span> <span class="comment-user userinfo">TomH ♦♦</span>
</div>
</div>
</div>
<div id="comment-tools-8521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8521-form-container" class="comment-form-container">
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

