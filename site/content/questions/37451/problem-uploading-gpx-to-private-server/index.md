+++
type = "question"
title = "Problem uploading GPX to private server"
description = '''Hello guys, I am trying to upload GPX tracks to my private OSM server but it seems like i am running into a server error while doing so Here is the cURL command i am using curl -u arsaXXXX:XXXXX -H &quot;Expect: &quot; -F &quot;file=@C:&#92;Users&#92;arsa3858&#92;Desktop&#92;1.gpx -F description=description &#92; -F tags=tags -F visi...'''
date = "2014-10-09T10:11:00Z"
lastmod = "2014-10-10T08:55:00Z"
weight = 37451
keywords = [ "tile", "api", "gpx", "upload", "server" ]
aliases = [ "/questions/37451" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem uploading GPX to private server](/questions/37451/problem-uploading-gpx-to-private-server)

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
<span id="post-37451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37451-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello guys,</p>
<p>I am trying to upload GPX tracks to my private OSM server but it seems like i am running into a server error while doing so</p>
<p>Here is the cURL command i am using</p>
<p><code>curl -u arsaXXXX:XXXXX -H "Expect: " -F "file=</code><a href="https://help.openstreetmap.org/users/23/cohort"><code>@C</code></a><code>:\Users\arsa3858\Desktop\1.gpx -F description=description \ -F tags=tags -F visibility=public </code><a href="http://b20003:3000/api/0.6/gpx/create"><code>http://b20003:3000/api/0.6/gpx/create</code></a></p>
<p>Below is the error report that i am seeing , i understand that its a ruby on rails server problem but i have no idea how to go about fixing this. Thanks in advance for your help</p>
<pre><code>API threw unexpected Errno::ENOENT exception: No such file or directory - (/tmp/0.7056756430417218, /home/osm/traces/11.gpx)
/usr/lib/ruby/1.9.1/fileutils.rb:519:in `rename&#39;
/usr/lib/ruby/1.9.1/fileutils.rb:519:in `block in mv&#39;
/usr/lib/ruby/1.9.1/fileutils.rb:1515:in `block in fu_each_src_dest&#39;
/usr/lib/ruby/1.9.1/fileutils.rb:1531:in `fu_each_src_dest0&#39;
/usr/lib/ruby/1.9.1/fileutils.rb:1513:in `fu_each_src_dest&#39;
/usr/lib/ruby/1.9.1/fileutils.rb:508:in `mv&#39;
/data/src/openstreetmap-website-master/app/controllers/trace_controller.rb:374:in `block in do_create&#39;
/var/lib/gems/1.9.1/gems/activerecord-4.0.5/lib/active_record/connection_adapters/abstract/database_statements.rb:213:in `block in transaction&#39;
/var/lib/gems/1.9.1/gems/activerecord-4.0.5/lib/active_record/connection_adapters/abstract/database_statements.rb:221:in `within_new_transaction&#39;
/var/lib/gems/1.9.1/gems/activerecord-4.0.5/lib/active_record/connection_adapters/abstract/database_statements.rb:213:in `transaction&#39;
/var/lib/gems/1.9.1/gems/activerecord-4.0.5/lib/active_record/transactions.rb:209:in `transaction&#39;
/var/lib/gems/1.9.1/gems/deadlock_retry-1.2.0/lib/deadlock_retry.rb:31:in `transaction_with_deadlock_handling&#39;
/data/src/openstreetmap-website-master/app/controllers/trace_controller.rb:368:in `do_create&#39;
/data/src/openstreetmap-website-master/app/controllers/trace_controller.rb:330:in `api_create&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal/implicit_render.rb:4:in `send_action&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/abstract_controller/base.rb:189:in `process_action&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal/rendering.rb:10:in `process_action&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/abstract_controller/callbacks.rb:18:in `block in process_action&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/callbacks.rb:514:in `block in _run__252704330398790117__process_action__callbacks&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/callbacks.rb:212:in `block in _conditional_callback_around_5&#39;
/data/src/openstreetmap-website-master/app/controllers/application_controller.rb:322:in `api_call_handle_error&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/callbacks.rb:211:in `_conditional_callback_around_5&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/callbacks.rb:513:in `_run__252704330398790117__process_action__callbacks&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/callbacks.rb:80:in `run_callbacks&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/abstract_controller/callbacks.rb:17:in `process_action&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal/rescue.rb:29:in `process_action&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal/instrumentation.rb:31:in `block in process_action&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/notifications.rb:159:in `block in instrument&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/notifications/instrumenter.rb:20:in `instrument&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/notifications.rb:159:in `instrument&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal/instrumentation.rb:30:in `process_action&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal/params_wrapper.rb:250:in `process_action&#39;
/var/lib/gems/1.9.1/gems/activerecord-4.0.5/lib/active_record/railties/controller_runtime.rb:18:in `process_action&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/abstract_controller/base.rb:136:in `process&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/abstract_controller/rendering.rb:44:in `process&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal.rb:195:in `dispatch&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal/rack_delegation.rb:13:in `dispatch&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_controller/metal.rb:231:in `block in action&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/routing/route_set.rb:80:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/routing/route_set.rb:80:in `dispatch&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/routing/route_set.rb:48:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/journey/router.rb:71:in `block in call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/journey/router.rb:59:in `each&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/journey/router.rb:59:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/routing/route_set.rb:674:in `call&#39;
/var/lib/gems/1.9.1/gems/oauth-plugin-0.5.1/lib/oauth/rack/oauth_filter.rb:75:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-cors-0.2.9/lib/rack/cors.rb:54:in `call&#39;
/data/src/openstreetmap-website-master/config/initializers/cors.rb:9:in `call&#39;
/var/lib/gems/1.9.1/gems/http_accept_language-2.0.1/lib/http_accept_language/middleware.rb:13:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-openid-1.4.2/lib/rack/openid.rb:98:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/etag.rb:23:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/conditionalget.rb:35:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/head.rb:11:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/flash.rb:241:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/session/abstract/id.rb:225:in `context&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/session/abstract/id.rb:220:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/cookies.rb:486:in `call&#39;
/var/lib/gems/1.9.1/gems/activerecord-4.0.5/lib/active_record/connection_adapters/abstract/connection_pool.rb:626:in `call&#39;
/var/lib/gems/1.9.1/gems/activerecord-4.0.5/lib/active_record/migration.rb:373:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/callbacks.rb:29:in `block in call&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/callbacks.rb:373:in `_run__4521713156344120633__call__callbacks&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/callbacks.rb:80:in `run_callbacks&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/callbacks.rb:27:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/reloader.rb:64:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/remote_ip.rb:76:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/debug_exceptions.rb:17:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/show_exceptions.rb:30:in `call&#39;
/var/lib/gems/1.9.1/gems/railties-4.0.5/lib/rails/rack/logger.rb:38:in `call_app&#39;
/var/lib/gems/1.9.1/gems/railties-4.0.5/lib/rails/rack/logger.rb:20:in `block in call&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/tagged_logging.rb:68:in `block in tagged&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/tagged_logging.rb:26:in `tagged&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/tagged_logging.rb:68:in `tagged&#39;
/var/lib/gems/1.9.1/gems/railties-4.0.5/lib/rails/rack/logger.rb:20:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/request_id.rb:21:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/methodoverride.rb:21:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/runtime.rb:17:in `call&#39;
/var/lib/gems/1.9.1/gems/activesupport-4.0.5/lib/active_support/cache/strategy/local_cache.rb:83:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/lock.rb:17:in `call&#39;
/var/lib/gems/1.9.1/gems/actionpack-4.0.5/lib/action_dispatch/middleware/static.rb:64:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/sendfile.rb:112:in `call&#39;
/var/lib/gems/1.9.1/gems/railties-4.0.5/lib/rails/engine.rb:511:in `call&#39;
/var/lib/gems/1.9.1/gems/railties-4.0.5/lib/rails/application.rb:97:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/lock.rb:17:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/content_length.rb:14:in `call&#39;
/var/lib/gems/1.9.1/gems/rack-1.5.2/lib/rack/handler/webrick.rb:60:in `service&#39;
/usr/lib/ruby/1.9.1/webrick/httpserver.rb:138:in `service&#39;
/usr/lib/ruby/1.9.1/webrick/httpserver.rb:94:in `run&#39;
/usr/lib/ruby/1.9.1/webrick/server.rb:191:in `block in start_thread&#39;
  Rendered text template (0.0ms)
Completed 500 Internal Server Error in 90ms (Views: 0.7ms | ActiveRecord: 2.7ms)</code></pre>
<p>Atjun</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '14, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0be8b0bc55610645ad634cb9f680c48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osm_Enthu&#39;s gravatar image" />
<p><span>Osm_Enthu</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osm_Enthu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '14, 10:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-37451" class="comments-container">
<span id="37455"></span>
<div id="comment-37455" class="comment">
<div id="post-37455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is some error within the path of the file , seems like the uploaded gpx trace needs to be saved on the server but the destination address isnt correct/ does not exist</p>
</div>
<div id="comment-37455-info" class="comment-info">
<span class="comment-age">(09 Oct '14, 12:47)</span> <span class="comment-user userinfo">Osm_Enthu</span>
</div>
</div>
<span id="37456"></span>
<div id="comment-37456" class="comment">
<div id="post-37456-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Source:</p>
<p><a href="https://trac.openstreetmap.org/ticket/1396#comment:1">https://trac.openstreetmap.org/ticket/1396#comment:1</a></p>
</div>
<div id="comment-37456-info" class="comment-info">
<span class="comment-age">(09 Oct '14, 12:59)</span> <span class="comment-user userinfo">Osm_Enthu</span>
</div>
</div>
</div>
<div id="comment-tools-37451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37451-form-container" class="comment-form-container">
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

<span id="37482"></span>

<div id="answer-container-37482" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37482-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So , i seem to have figured this problem out.</p>
<p>The path of the</p>
<p>gpx_trace_dir: "/home/../osm/traces" gpx_image_dir: "/home/../osm/images"</p>
<p>needs to be matching to your exact home folder location.</p>
<p>You can find these paths in the application.yml file in /openstreetmap-website/config</p>
<p>Happy coding !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '14, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/0be8b0bc55610645ad634cb9f680c48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osm_Enthu&#39;s gravatar image" />
<p><span>Osm_Enthu</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osm_Enthu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37482" class="comments-container">
&#10;</div>
<div id="comment-tools-37482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37482-form-container" class="comment-form-container">
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

