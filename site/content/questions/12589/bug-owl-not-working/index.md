+++
type = "question"
title = "[closed] BUG - OWL not working"
description = '''http://wiki.openstreetmap.org/wiki/OWL_%28OpenStreetMap_Watch_List%29 Ruby on Rails application could not be started These are the possible causes: There may be a syntax error in the application&#x27;s code. Please check for such errors and fix them. A required library may not installed. Please install a...'''
date = "2012-05-07T10:34:00Z"
lastmod = "2012-05-07T10:34:00Z"
weight = 12589
keywords = [ "owl", "ruby" ]
aliases = [ "/questions/12589" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] BUG - OWL not working](/questions/12589/bug-owl-not-working)

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
<span id="post-12589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12589-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="http://wiki.openstreetmap.org/wiki/OWL_%28OpenStreetMap_Watch_List%29">http://wiki.openstreetmap.org/wiki/OWL_%28OpenStreetMap_Watch_List%29</a></p>
<p>Ruby on Rails application could not be started These are the possible causes:</p>
<pre><code>There may be a syntax error in the application&#39;s code. Please check for such errors and fix them.
A required library may not installed. Please install all libraries that this application requires.
The application may not be properly configured. Please check whether all configuration files are written correctly, fix any incorrect configurations, and restart this application.
A service that the application relies on (such as the database server or the Ferret search engine server) may not have been started. Please start that service.</code></pre>
<p>Further information about the error may have been written to the application's log file. Please check it in order to analyse the problem.</p>
<p>Error message: undefined method <code>name' for "SystemTimer":String Exception class: NoMethodError Application root: /home/matt/public_html/../owl_viewer Backtrace: # File Line Location 0 /var/lib/gems/1.8/gems/rails-2.3.8/lib/rails/gem_dependency.rb 275 in</code>==' 1 /usr/lib/ruby/vendor_ruby/1.8/rubygems/dependency.rb 217 in <code>===' 2 /usr/lib/ruby/vendor_ruby/1.8/rubygems/dependency.rb 217 in</code>matching_specs' 3 /usr/lib/ruby/vendor_ruby/1.8/rubygems/custom_require.rb 36 in <code>find_all' 4 /usr/lib/ruby/vendor_ruby/1.8/rubygems/specification.rb 411 in</code>each' 5 /usr/lib/ruby/vendor_ruby/1.8/rubygems/specification.rb 410 in <code>each' 6 /usr/lib/ruby/vendor_ruby/1.8/rubygems/dependency.rb 216 in</code>find_all' 7 /usr/lib/ruby/vendor_ruby/1.8/rubygems/dependency.rb 216 in <code>matching_specs' 8 /usr/lib/ruby/vendor_ruby/1.8/rubygems/dependency.rb 238 in</code>to_specs' 9 /usr/lib/ruby/vendor_ruby/1.8/rubygems/dependency.rb 256 in <code>to_spec' 10 /usr/lib/ruby/vendor_ruby/1.8/rubygems.rb 1230 in</code>gem' 11 /var/lib/gems/1.8/gems/rails-2.3.8/lib/rails/gem_dependency.rb 73 in <code>add_load_paths' 12 /var/lib/gems/1.8/gems/rails-2.3.8/lib/initializer.rb 301 in</code>add_gem_load_paths' 13 /var/lib/gems/1.8/gems/rails-2.3.8/lib/initializer.rb 301 in <code>each' 14 /var/lib/gems/1.8/gems/rails-2.3.8/lib/initializer.rb 301 in</code>add_gem_load_paths' 15 /var/lib/gems/1.8/gems/rails-2.3.8/lib/initializer.rb 132 in <code>process' 16 /var/lib/gems/1.8/gems/rails-2.3.8/lib/initializer.rb 113 in</code>send' 17 /var/lib/gems/1.8/gems/rails-2.3.8/lib/initializer.rb 113 in <code>run' 18 /home/matt/owl_viewer/config/environment.rb 9 19 /usr/lib/ruby/vendor_ruby/1.8/rubygems/custom_require.rb 36 in</code>gem_original_require' 20 /usr/lib/ruby/vendor_ruby/1.8/rubygems/custom_require.rb 36 in <code>require' 21 /usr/lib/ruby/1.8/phusion_passenger/classic_rails/application_spawner.rb 222 in</code>preload_application' 22 /usr/lib/ruby/1.8/phusion_passenger/classic_rails/application_spawner.rb 181 in <code>initialize_server' 23 /usr/lib/ruby/1.8/phusion_passenger/utils.rb 572 in</code>report_app_init_status' 24 /usr/lib/ruby/1.8/phusion_passenger/classic_rails/application_spawner.rb 174 in <code>initialize_server' 25 /usr/lib/ruby/1.8/phusion_passenger/abstract_server.rb 204 in</code>start_synchronously' 26 /usr/lib/ruby/1.8/phusion_passenger/abstract_server.rb 180 in <code>start' 27 /usr/lib/ruby/1.8/phusion_passenger/classic_rails/application_spawner.rb 149 in</code>start' 28 /usr/lib/ruby/1.8/phusion_passenger/spawn_manager.rb 219 in <code>spawn_rails_application' 29 /usr/lib/ruby/1.8/phusion_passenger/abstract_server_collection.rb 132 in</code>lookup_or_add' 30 /usr/lib/ruby/1.8/phusion_passenger/spawn_manager.rb 214 in <code>spawn_rails_application' 31 /usr/lib/ruby/1.8/phusion_passenger/abstract_server_collection.rb 82 in</code>synchronize' 32 /usr/lib/ruby/1.8/phusion_passenger/abstract_server_collection.rb 79 in <code>synchronize' 33 /usr/lib/ruby/1.8/phusion_passenger/spawn_manager.rb 213 in</code>spawn_rails_application' 34 /usr/lib/ruby/1.8/phusion_passenger/spawn_manager.rb 132 in <code>spawn_application' 35 /usr/lib/ruby/1.8/phusion_passenger/spawn_manager.rb 275 in</code>handle_spawn_application' 36 /usr/lib/ruby/1.8/phusion_passenger/abstract_server.rb 357 in <code>__send__' 37 /usr/lib/ruby/1.8/phusion_passenger/abstract_server.rb 357 in</code>server_main_loop' 38 /usr/lib/ruby/1.8/phusion_passenger/abstract_server.rb 206 in `start_synchronously' 39 /usr/share/phusion-passenger/helper-scripts/passenger-spawn-server 99<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-owl" rel="tag" title="see questions tagged &#39;owl&#39;">owl</span> <span class="post-tag tag-link-ruby" rel="tag" title="see questions tagged &#39;ruby&#39;">ruby</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '12, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/92a51d3af99ee124bb9e06dd35249910?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Badita%20Florin&#39;s gravatar image" />
<p><span>Badita Florin</span><br />
<span class="score" title="112 reputation points">112</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Badita Florin has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>07 May '12, 10:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-12589" class="comments-container">
&#10;</div>
<div id="comment-tools-12589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Bug reports should be reported at trac.osm.org not here." by Gnonthgol 07 May '12, 10:57

</div>

</div>

</div>

