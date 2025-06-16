+++
type = "question"
title = "Rails port on Apache Passenger"
description = '''Hi everyone! I have managed to successfuly install Rails port application (following this: https://wiki.openstreetmap.org/wiki/The_Rails_Port tutorial. When I run it under WEBRick server, it runs ok and i can access api. However I cannot make it run under Apache Passenger. Accessing any page I get fo...'''
date = "2012-12-02T14:33:00Z"
lastmod = "2013-05-20T12:26:00Z"
weight = 18148
keywords = [ "apache", "passenger", "problem", "port", "rails" ]
aliases = [ "/questions/18148" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rails port on Apache Passenger](/questions/18148/rails-port-on-apache-passenger)

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
<span id="post-18148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18148-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>I have managed to successfuly install Rails port application (following this: <a href="https://wiki.openstreetmap.org/wiki/The_Rails_Port">https://wiki.openstreetmap.org/wiki/The_Rails_Port</a> tutorial. When I run it under WEBRick server, it runs ok and i can access api. However I cannot make it run under Apache Passenger. Accessing any page I get following error:</p>
<p>Your application's database configuration file might be written incorrectly. Please check it and fix any errors. The database server may not be running. Please check whether it's running, and start it if it isn't.</p>
<p>Error message: PG::Error: ERROR: relation "oauth_tokens" does not exist LINE 5: WHERE a.attrelid = '"oauth_tokens"'::regclass ^ : SELECT a.attname, format_type(a.atttypid, a.atttypmod), pg_get_expr(d.adbin, d.adrelid), a.attnotnull, a.atttypid, a.atttypmod FROM pg_attribute a LEFT JOIN pg_attrdef d ON a.attrelid = d.adrelid AND a.attnum = d.adnum WHERE a.attrelid = '"oauth_tokens"'::regclass AND a.attnum &gt; 0 AND NOT a.attisdropped ORDER BY a.attnum (ActiveRecord::StatementInvalid)</p>
<p>Exception class: ActiveRecord::StatementInvalid</p>
<p>Its weird, because under WEBRick server it works. Can anyone help me solve this issue? I am using Debian 6.</p>
<p>thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-passenger" rel="tag" title="see questions tagged &#39;passenger&#39;">passenger</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '12, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/86dcc14b5b09a1edfccf25d37df806e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boksajak&#39;s gravatar image" />
<p><span>boksajak</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boksajak has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18148" class="comments-container">
&#10;</div>
<div id="comment-tools-18148" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18148-form-container" class="comment-form-container">
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

<span id="18396"></span>

<div id="answer-container-18396" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18396-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>By default, "rails server" will access your application using the 'development' rails environment, whereas passenger is configured to use the 'production' environment by default.</p>
<p>I suspect that your production database isn't configured properly, and that's what's giving you the error above. Check the settings in config/database.yml, and check that the expected tables are already set up.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '12, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-18396" class="comments-container">
<span id="18404"></span>
<div id="comment-18404" class="comment">
<div id="post-18404-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, I managed to repair production osm database (i needed to run gem install builder before creating database).</p>
<p>Now i have a new problem. I still cannot access Rails port application on Apache. I am getting OSM error page with error code 500. Apache log reveals two errors:</p>
<ol>
<li><p>ActionView::Template::Error (index.js isn't precompiled)</p></li>
<li><p>ActionController::RoutingError (No route matches [GET] "/assets/osm_logo.png")</p></li>
</ol>
</div>
<div id="comment-18404-info" class="comment-info">
<span class="comment-age">(12 Dec '12, 19:48)</span> <span class="comment-user userinfo">boksajak</span>
</div>
</div>
<span id="22566"></span>
<div id="comment-22566" class="comment">
<div id="post-22566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you manage to solve the issue with <strong>index.js isn't precompiled</strong>?</p>
</div>
<div id="comment-22566-info" class="comment-info">
<span class="comment-age">(20 May '13, 12:26)</span> <span class="comment-user userinfo">bibstha</span>
</div>
</div>
</div>
<div id="comment-tools-18396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18396-form-container" class="comment-form-container">
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

