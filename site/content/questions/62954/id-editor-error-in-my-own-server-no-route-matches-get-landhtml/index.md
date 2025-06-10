+++
type = "question"
title = "iD Editor Error in My Own Server (no route matches [GET] &quot;/land.html&quot;"
description = '''Hi, I set up my own OSM server and launch it in the development mode. I have a backend RDS server in AWS with data populated. Also, per instruction (https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md), I registered application (in localhost) and update consumer key in ap...'''
date = "2018-04-09T06:50:00Z"
lastmod = "2018-04-10T12:37:00Z"
weight = 62954
keywords = [ "ideditor", "railsport" ]
aliases = [ "/questions/62954" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [iD Editor Error in My Own Server (no route matches \[GET\] "/land.html"](/questions/62954/id-editor-error-in-my-own-server-no-route-matches-get-landhtml)

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
<span id="post-62954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62954-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I set up my own OSM server and launch it in the development mode. I have a backend RDS server in AWS with data populated. Also, per instruction (<a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md),">https://github.com/openstreetmap/openstreetmap-website/blob/master/CONFIGURE.md),</a> I registered application (in localhost) and update consumer key in application.yml. However, every time when I try to save my local changes in the iD editor, a popup window shows up to ask permission. After clicking "Grant Access", I always see an error message: No route matches [GET] "/land.html". Full trace is attached below:</p>
<p>actionpack (5.1.5) lib/action_dispatch/middleware/debug_exceptions.rb:63:in <code>call' actionpack (5.1.5) lib/action_dispatch/middleware/show_exceptions.rb:31:in</code>call' railties (5.1.5) lib/rails/rack/logger.rb:36:in <code>call_app' railties (5.1.5) lib/rails/rack/logger.rb:24:in</code>block in call' activesupport (5.1.5) lib/active_support/tagged_logging.rb:69:in <code>block in tagged' activesupport (5.1.5) lib/active_support/tagged_logging.rb:26:in</code>tagged' activesupport (5.1.5) lib/active_support/tagged_logging.rb:69:in <code>tagged' railties (5.1.5) lib/rails/rack/logger.rb:24:in</code>call' sprockets-rails (3.2.1) lib/sprockets/rails/quiet_assets.rb:13:in <code>call' actionpack (5.1.5) lib/action_dispatch/middleware/remote_ip.rb:79:in</code>call' request_store (1.4.1) lib/request_store/middleware.rb:19:in <code>call' actionpack (5.1.5) lib/action_dispatch/middleware/request_id.rb:25:in</code>call' rack (2.0.4) lib/rack/method_override.rb:22:in <code>call' rack (2.0.4) lib/rack/runtime.rb:22:in</code>call' rack-uri_sanitizer (0.0.2) lib/rack/uri_sanitizer.rb:14:in <code>call' activesupport (5.1.5) lib/active_support/cache/strategy/local_cache_middleware.rb:27:in</code>call' actionpack (5.1.5) lib/action_dispatch/middleware/executor.rb:12:in <code>call' actionpack (5.1.5) lib/action_dispatch/middleware/static.rb:125:in</code>call' rack (2.0.4) lib/rack/sendfile.rb:111:in <code>call' secure_headers (5.0.5) lib/secure_headers/middleware.rb:13:in</code>call' railties (5.1.5) lib/rails/engine.rb:522:in <code>call' puma (3.11.3) lib/puma/configuration.rb:225:in</code>call' puma (3.11.3) lib/puma/server.rb:624:in <code>handle_request' puma (3.11.3) lib/puma/server.rb:438:in</code>process_client' puma (3.11.3) lib/puma/server.rb:302:in <code>block in run' puma (3.11.3) lib/puma/thread_pool.rb:120:in</code>block in spawn_thread'</p>
<p>If I set oauth_10_support to false in application.yml, the authorization process seems to come through. However, the popup window does not go away and the save button is still grayed out. If I reload the page and try to save again, I would still be asked for permission.</p>
<p>Interestingly, the Potlatch editor works perfectly fine. No permission is asked and changes can be saved to database successfully.</p>
<p>Does anyone have a hit what might go wrong?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '18, 06:50</strong></p>
<img src="https://secure.gravatar.com/avatar/113f3247b68d1f21a2c594b2b87519c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zlzhao1104&#39;s gravatar image" />
<p><span>zlzhao1104</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zlzhao1104 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-62954" class="comments-container">
&#10;</div>
<div id="comment-tools-62954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62954-form-container" class="comment-form-container">
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

<span id="62963"></span>

<div id="answer-container-62963" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62963-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SK53 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Never mind. I just resolved the issue. Originally, I only allowed iD to request the “modify the map” permission from user. I just tried to allow it to request all permissions and it worked well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '18, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/113f3247b68d1f21a2c594b2b87519c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zlzhao1104&#39;s gravatar image" />
<p><span>zlzhao1104</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zlzhao1104 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-62963" class="comments-container">
<span id="62965"></span>
<div id="comment-62965" class="comment">
<div id="post-62965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As you cannot accept your own answers, I've marked this as accepted.</p>
</div>
<div id="comment-62965-info" class="comment-info">
<span class="comment-age">(10 Apr '18, 12:37)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62963-form-container" class="comment-form-container">
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

